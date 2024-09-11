"""
    Summary: The core app contains all of the 
             models that represents the table as well as 
             the schema of the ERD
"""

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Facility(models.Model):
    """
        Summary:
            The model that represents the mapping
            of the facility table
    """
    facility_id = models.AutoField(primary_key=True)
    facility_name = models.CharField(max_length=50, null=False)
    number_of_floors = models.IntegerField(null=False)

class User(AbstractUser):
    """
        Summary:
            The model that represents the mapping
            of the user table
    """
    employee_id = models.AutoField(primary_key=True)
    user_Firstname = models.CharField(max_length=35, null=False)
    user_Middlename = models.CharField(max_length=35, blank=True)
    user_Lastname = models.CharField(max_length=35, null=False)
    position = models.CharField(max_length=50)

class Date(models.Model):
    """
        Summary:
            The model that represents the mapping
            of the date table
    """
    date_id = models.AutoField(primary_key=True)
    month = models.CharField(max_length=15, null=False)
    day = models.CharField(max_length=3, null=False)
    year = models.CharField(max_length=5, null=False)

class Asset(models.Model):
    """
        Summary:
            The model that represents the mapping
            of the asset table
    """
    asset_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=50)
    item_total_count = models.IntegerField()
    floor_number = models.IntegerField()

class Status(models.Model):
    """
        Summary:
            The model that represents the mapping
            of the status table
    """
    status_id = models.AutoField(primary_key=True)
    status_message = models.CharField(max_length=25)

class Inspection(models.Model):
    """
        Summary:
            The model that represents the mapping
            of the inspection table
    """
    inspection_reference_num = models.AutoField(primary_key=True)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.ForeignKey(Date, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

class Details(models.Model):
    """
        Summary:
            The model that represents the mapping
            of the details table
    """
    detail_id = models.AutoField(primary_key=True)
    damaged = models.CharField(max_length=4, null=False)
    comment = models.CharField(max_length=500)
    inspection = models.ForeignKey(Inspection, on_delete=models.CASCADE)
