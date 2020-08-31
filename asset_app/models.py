from django.db import models

# Create your models here.
class Laptop(models.Model):
    UserId = models.IntegerField(default='0')
    FullName = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Brand = models.CharField(max_length=50)
    RAM = models.CharField(max_length=50)
    HardDisk = models.CharField(max_length=50, default='')
    SSD = models.CharField(max_length=50)
    Battery = models.CharField(max_length=50)
    Processor_Model = models.CharField(max_length=50)
    Charger = models.CharField(max_length=50)
    MacAddress = models.CharField(max_length=50)
    date1 = models.DateField()
    time1 = models.TimeField()


    def __str__(self):
        return self.FullName


class Desktop(models.Model):
    UserId = models.IntegerField(default='0')
    FullName = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Brand = models.CharField(max_length=50)
    RAM = models.CharField(max_length=50)
    HardDisk = models.CharField(max_length=50, default='')
    SSD = models.CharField(max_length=50)
    Battery = models.CharField(max_length=50)
    Charger = models.CharField(max_length=50)
    Processor_Model = models.CharField(max_length=50)
    MacAddress = models.CharField(max_length=50)
    date1 = models.DateField()
    time1 = models.TimeField()


    def __str__(self):
        return self.FullName


