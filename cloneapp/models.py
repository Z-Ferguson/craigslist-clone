from django.db import models
from django.contrib.auth.models import User


class Region(models.Model):
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.location


class Category(models.Model):
    name = models.CharField(max_length=50, default=None)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='child')

    def __str__(self):
        return self.name


# class subCategory(models.Model):
#     sub_name = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.sub_name


class Listing(models.Model):
    user = models.ForeignKey(User, null=True)
    title = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=15)
    location = models.ForeignKey(Region, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    body = models.TextField()
    # photo = models.ImageField(upload_to="None", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # sub_category = models.ForeignKey(subCategory, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User)
    location = models.ForeignKey(Region, default=1)
