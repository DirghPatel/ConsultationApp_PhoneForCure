from django.db import models
from doctor.models import Doctor

# Create your models here.


class Patient(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name 


class CommonHealthProblem(models.Model):
    problem = models.CharField(max_length=200)
    fees = models.IntegerField()
    image = models.ImageField(upload_to='')
    slug = models.CharField(max_length=200, default="a")

    def __str__(self):
        return self.problem


class bookAppointment(models.Model):

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    time = models.CharField(max_length=20)
    problem = models.TextField()
    status = models.CharField(default=False , max_length=100)

    def __str__(self):
        return self.name
