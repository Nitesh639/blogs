from django.db import models


# Create your models here.
class blog(models.Model):
    user_id = models.IntegerField(null=False)
    user_username = models.CharField(max_length=200)
    date = models.DateTimeField(null=False)
    post_id = models.CharField(max_length=200)
    topic = models.CharField(max_length=500)
    content = models.TextField(max_length=10000)
    tags = models.CharField(max_length=200)
    post_img = models.ImageField(null=False)
    table_connect = models.CharField(max_length=200)
