from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory

from ..models import Book
from ..serializers import BookSerializer


class BookViewSetTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        Book.objects.create(
            name='Book 1', author='Author 1', publication_date='2019-03-05', isbn='978-3-16-148410-1'
        )
        Book.objects.create(
            name='Book 2', author='Author 2', publication_date='2000-11-17', isbn='978-5-699-12014-7'
        )
        Book.objects.create(
            name='Book 3', author='Author 3', publication_date='2010-08-01', isbn='978-1-56619-909-4'
        )

    def test_post_book_request(self):
        url = reverse('book-list')
        data = {
            'name': 'Чистый Python. Тонкости программирования для профи',
            'author': 'Дэн Бейдер',
            'publication_date': '2019-06-20',
            'isbn': '978-3-16-148410-0'
        }
        response = self.client.post(url, data=data)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

        response = self.client.get(url)
        self.assertEqual(4, len(response.data))

    def test_post_book_request_negative(self):
        url = reverse('book-list')
        data = {
            'name': 'Book 4',
            'author': 'Author 4',
            'publication_date': '2019-06-20',
            'isbn': '978-1-56619-909-4'
        }
        response = self.client.post(url, data=data)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_get_books_list_request(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        books = [
            Book.objects.get(pk=1),
            Book.objects.get(pk=2),
            Book.objects.get(pk=3)
        ]
        serialised_data = self.__get_serialized_data(books, many=True)
        self.assertEqual(serialised_data, response.data.get('results'))
        self.assertTrue(3 == response.data.get('count'))
        self.assertTrue(response.data.get('next') is None)
        self.assertTrue(response.data.get('previous') is None)

    def test_get_book_detail_request(self):
        url = reverse('book-detail', args=[1])
        response = self.client.get(url)
        self.assertEquals(status.HTTP_200_OK, response.status_code)

        serialized_data = self.__get_serialized_data(Book.objects.get(pk=1))
        self.assertEqual(serialized_data, response.data)

    def test_put_book_request(self):
        url = reverse('book-detail', args=[1])
        data = {
            'name': 'Book 1 (edited)', 'author': 'Author 1 (edited)',
            'publication_date': '2019-06-20', 'isbn': '978-3-16-148410-0'
        }
        response = self.client.put(url, data=data)
        self.assertEquals(status.HTTP_200_OK, response.status_code)

        serialized_data = self.__get_serialized_data(Book.objects.get(pk=1))
        self.assertEqual(serialized_data, response.data)

    def test_patch_book_request(self):
        url = reverse('book-detail', args=[2])
        data = {
            'name': 'Book 2 (edited)'
        }
        response = self.client.patch(url, data=data)
        self.assertEquals(status.HTTP_200_OK, response.status_code)

        serialized_data = self.__get_serialized_data(Book.objects.get(pk=2))
        self.assertEqual(serialized_data, response.data)

    def test_delete_book_request(self):
        url = reverse('book-detail', args=[1])
        response = self.client.delete(url)
        self.assertEquals(status.HTTP_204_NO_CONTENT, response.status_code)

        with self.assertRaises(Book.DoesNotExist):
            Book.objects.get(pk=1)

    def __get_serialized_data(self, obj, many=False):
        url = reverse('book-list')
        request = APIRequestFactory().get(url)
        return BookSerializer(obj, many=many, context={'request': request}).data
