from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Name(models.Model):
    title = models.CharField(max_length=90)
    image = models.ImageField()

    def __str__(self):
        return self.title
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''

        return url

class Information(models.Model):
    name = models.ForeignKey(Name, on_delete=models.CASCADE)
    message = models.TextField()

    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''

        return url