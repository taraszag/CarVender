from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from PIL import Image

import user


class Carbodytype(models.Model):
    carbodyname = models.CharField(db_column='CarBodyName', max_length=45, blank=True,
                                   null=True)  # Field name made lowercase.

    def __str__(self):
        return self.carbodyname

    class Meta:
        managed = False
        db_table = 'CarBodyType'


class Carmodel(models.Model):
    modelname = models.CharField(db_column='ModelName', max_length=45, blank=True,
                                 null=True)  # Field name made lowercase.
    carvenderid = models.ForeignKey('Carvender', models.DO_NOTHING, db_column='CarVenderID', blank=True,
                                    null=True)  # Field name made lowercase.

    def __str__(self):
        return self.modelname

    class Meta:
        managed = False
        db_table = 'CarModel'


class Carstate(models.Model):
    state = models.CharField(db_column='State', max_length=45, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.state

    class Meta:
        managed = False
        db_table = 'CarState'


class Cart(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserId', blank=True,
                               null=True)  # Field name made lowercase.
    requestid = models.ForeignKey('SellRequest', models.DO_NOTHING, db_column='RequestId', blank=True,
                                  null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cart'


class Carvender(models.Model):
    carvendername = models.CharField(db_column='CarVenderName', max_length=45, blank=True,
                                     null=True)  # Field name made lowercase.

    def __str__(self):
        return self.carvendername

    class Meta:
        managed = False
        db_table = 'CarVender'


class Drivetype(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=45, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.type

    class Meta:
        managed = False
        db_table = 'DriveType'


class Fueltype(models.Model):
    fuelname = models.CharField(db_column='FuelName', max_length=45, blank=True,
                                null=True)  # Field name made lowercase.

    def __str__(self):
        return self.fuelname

    class Meta:
        managed = False
        db_table = 'FuelType'


class Gearbox(models.Model):
    gearboxcotype = models.CharField(db_column='GearBoxcoType', max_length=45, blank=True,
                                     null=True)  # Field name made lowercase.

    def __str__(self):
        return self.gearboxcotype

    class Meta:
        managed = False
        db_table = 'GearBox'


class Region(models.Model):
    region = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.region

    class Meta:
        managed = False
        db_table = 'Region'


class SellRequest(models.Model):
    price = models.IntegerField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    region = models.ForeignKey(Region, models.DO_NOTHING, db_column='Region', blank=True,
                               null=True)  # Field name made lowercase.
    inginvolume = models.FloatField(db_column='InginVolume', blank=True, null=True)  # Field name made lowercase.
    fueltypeid = models.ForeignKey(Fueltype, models.DO_NOTHING, db_column='FuelTypeId', blank=True,
                                   null=True)  # Field name made lowercase.
    carbodyid = models.ForeignKey(Carbodytype, models.DO_NOTHING, db_column='CarBodyId', blank=True,
                                  null=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserId', blank=True,
                               null=True)  # Field name made lowercase.
    drivetypeid = models.ForeignKey(Drivetype, models.DO_NOTHING, db_column='DriveTypeId', blank=True,
                                    null=True)  # Field name made lowercase.
    gearboxid = models.ForeignKey(Gearbox, models.DO_NOTHING, db_column='GearBoxId', blank=True,
                                  null=True)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=45, blank=True, null=True)  # Field name made lowercase.
    carmodelid = models.ForeignKey(Carmodel, models.DO_NOTHING, db_column='CarModelId', blank=True,
                                   null=True)  # Field name made lowercase.
    carstateid = models.ForeignKey(Carstate, models.DO_NOTHING, db_column='CarStateId', blank=True,
                                   null=True)  # Field name made lowercase.
    CreationDate = models.TimeField(db_column='CreationDate', auto_now_add=True, null=True, blank=True)
    # Image = models.ImageField(db_column='Image',default="33.jpg", null=True, blank=True, upload_to='cars_imgs')
    Author = models.ForeignKey(User, db_column='Author', null=True, default=None, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(f"{self.carmodelid.modelname},{self.carmodelid.carvenderid.carvendername}")

    # def get_absolute_url(self):
    #   return reverse("sell_detail", kwargs={"pk": self.pk})

    # def save(self,*args,**kwargs):
    #     super().save(*args, **kwargs)
    #     img=Image.open(self.Image.path)
    #
    #     if img.height>300 or img.width>300:
    #         img.thumbnail((300,300))
    #         img.save(self.Image.path)

    class Meta:
        db_table = 'SellRequest'
        ordering = ('-CreationDate',)


class User(models.Model):
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=45, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=45, blank=True,
                                   null=True)  # Field name made lowercase.
    birthday = models.CharField(db_column='Birthday', max_length=45, blank=True,
                                null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=45, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=45, blank=True, null=True)  # Field name made lowercase.
    region = models.ForeignKey(Region, models.DO_NOTHING, db_column='Region', blank=True,
                               null=True)  # Field name made lowercase.
    Author = models.ForeignKey(User, db_column='Author', null=True, default=None, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(f"{self.name} {self.surname}")

    class Meta:
        db_table = 'user'
        ordering = ('name',)
