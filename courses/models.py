import datetime

from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f"{self.name}"


class Сourses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=False, blank=False)
    company = models.CharField(max_length=255, null=False, blank=False)
    type = models.BooleanField(default=False, null=True, blank=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    image = models.ImageField(default='default.jpg', upload_to='post_image/')
    price = models.IntegerField( null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)
    created_date = models.DateTimeField(default=datetime.datetime.now())
    website = models.URLField(max_length=255, null=False, blank=False)
    job_openings = models.CharField(max_length=255, null=True, blank=True)
    adress = models.URLField(max_length=255, null=False, blank=False)





    def __str__(self):
        return f"{self.name}"

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Сourses,null=True, blank=True)


    def __str__(self):
        return f"{self.user}"


