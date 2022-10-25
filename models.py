from django.db import models

import email
# from location_field.models.plain import PlainLocationField
from django.db import models
# from django.contrib.gis.geos import Point
# from location_field.models.spatial import LocationField



class Talent(models.Model):
    name                  = models.CharField( max_length=255)
    email                 = models.EmailField(max_length=255)
    phone_number          = models.IntegerField()
    age                   = models.IntegerField()
    gender                = models.CharField(max_length=255)
    ethnicity             = models.CharField(max_length=255)
    weight                = models.IntegerField()
    height                = models.DecimalField(max_digits=2, decimal_places=1)
    
    def __self__(self):
        return self.gender
    
    
class Company(models.Model):
    name                  = models.CharField(max_length=255)
    email                 = models.EmailField(max_length=255)
    description           = models.TextField(max_length=255)
    
    class Meta:
        verbose_name = ("company")
        verbose_name_plural = ("companies")
    
    def __self__(self):
        return self.name
     

# from django.db import models
# from location_field.models.plain import PlainLocationField

# class Place(models.Model):
#     city = models.CharField(max_length=255)
#     location = PlainLocationField(based_fields=['city'], zoom=7)

    


class Role(models.Model):
    talent_age         = models.IntegerField()
    talent_gender      = models.CharField(max_length=255)
    talent_ethnicity   = models.CharField(max_length=255)   
    talent_weight      = models.IntegerField()
    talent_height      = models.DecimalField(max_digits=2, decimal_places=1)
    
    def __self__(self):
       return self.talent_gender



class Project(models.Model):
    name               = models.CharField("Name", max_length=255)
    description        = models.TextField()
    city               = models.CharField(max_length=255)
    Location           = models.CharField(max_length=255)
    # roles              = models.ManyToManyField("Role", related_name="projects")
    role              = models.ForeignKey(Role, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.name




