from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


@shared_task
def send_customer_register_email_task(data):
    """Асинхронная задача для отправки email-а после регистрации пользователя"""

    try:
        msg_plain = render_to_string('customer/emails/customer_register/email.txt', {'data': data})
        msg_html = render_to_string('customer/emails/customer_register/email.html', {'data': data})
        send_mail(
            subject=settings.EMAIL_SUBJECT,
            from_email=settings.EMAIL_FROM,
            recipient_list=[data.get('email')],
            message=msg_plain,
            html_message=msg_html,
            fail_silently=False
        )
    except Exception:
        raise Exception("Internal server error! Your message cannot be send. Try it later.")

