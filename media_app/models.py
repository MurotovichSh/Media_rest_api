from django.db import models
# Create your models here.
class Post(models.Model):
    topic=models.CharField(max_length=15)
    message=models.CharField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
