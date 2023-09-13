from django.contrib.auth.models import User
from celery import shared_task
from django.core.mail import send_mail
from social_media import settings

@shared_task(bind=True)
def send_mail_func(self):
    users = User.objects.all()
    for user in users:
<<<<<<< HEAD
<<<<<<< HEAD
        mail_subject = "Sign up confirmation"
        message = "Thank you for signing up to my website!"
=======
        mail_subject = "Login confirmation"
        message = "You have successfully logged in to your account!"
>>>>>>> 9a23bda09f0df9f60a91fbfe2ead0f71d5c1ff7a
=======
        mail_subject = "Login confirmation"
        message = "You have successfully logged in to your account!"
>>>>>>> 9a23bda09f0df9f60a91fbfe2ead0f71d5c1ff7a
        to_email = user.email
        send_mail(
            subject = mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=False,
        )
<<<<<<< HEAD
<<<<<<< HEAD
    return "Task completed!"
=======
    return "Task completed!"
>>>>>>> 9a23bda09f0df9f60a91fbfe2ead0f71d5c1ff7a
=======
    return "Task completed!"
>>>>>>> 9a23bda09f0df9f60a91fbfe2ead0f71d5c1ff7a
