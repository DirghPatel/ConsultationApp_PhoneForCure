from django.contrib import admin
from patient.models import Patient
from patient.models import CommonHealthProblem
from patient.models import bookAppointment
# Register your models here.

admin.site.register(Patient)
admin.site.register(CommonHealthProblem)
admin.site.register(bookAppointment)