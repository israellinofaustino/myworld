from django.db import models


class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(auto_now_add=True, null=True)
    slug = models.SlugField(default="", null=True)


def __str__(self):
    return f"{self.firstname} {self.lastname}"


class FeedBack(models.Model):
    text = models.CharField(max_length=1000, null=True)
