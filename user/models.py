# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from car_app.models import Sellrequest
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
from django.db.models import OneToOneField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg",
                              null=True,
                              blank=True,
                              upload_to='profile_imgs')
    surname = models.CharField(db_column='Surname', max_length=45, blank=True,
                               null=True)
    telephone = models.IntegerField(db_column='Telephone', blank=True,
                                    null=True)
    city = models.CharField(db_column='City', max_length=100, blank=True,
                            null=True)
    street = models.CharField(db_column='Street', max_length=255, blank=True,
                               null=True)
    country = models.CharField(db_column='Country', max_length=100, blank=True,
                               null=True)
    postcode = models.CharField(db_column='PostCode', max_length=45, blank=True,
                                null=True)
    def __str__(self):
        return f"{self.user.username} Profile"

    @classmethod
    def create(cls, user):
        profile = cls(user=user)
        return profile

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            img.thumbnail((300, 300))
            img.save(self.image.path)
