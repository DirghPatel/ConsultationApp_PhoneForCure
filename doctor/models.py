from django.db import models
import uuid

# Create your models here.


class Doctor(models.Model):
    doctorid = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    speciality = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)
    hospitalname = models.CharField(max_length=50)
    hospitalcity = models.CharField(max_length=50)
    hospitalarea = models.CharField(max_length=50)
    onlinefees = models.CharField(max_length=50)
    feesatclinic = models.CharField(max_length=50)
    image = models.ImageField(upload_to="doctor/", blank=True)

    def __str__(self):
        return self.name
