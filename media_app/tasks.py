from django.contrib.auth.models import User
from celery import shared_task
from django.core.mail import send_mail
from social_media import settings

@shared_task(bind=True)
def send_mail_func(self):
    users = User.objects.all()
    for user in users:
        mail_subject = "Sign up confirmation"
        message = "Thank you for signing up to my website!"
        to_email = user.email
        send_mail(
            subject = mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=False,
        )
    return "Task completed!"