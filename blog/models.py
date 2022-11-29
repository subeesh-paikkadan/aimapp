from django.db import models

# Create your models here.
class Post(models.Model):
    Heading = models.CharField(max_length = 200)
    image = models.ImageField(upload_to= 'uploads')
    content = models.TextField()
    