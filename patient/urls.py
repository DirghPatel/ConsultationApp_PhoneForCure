from patient.models import bookAppointment
from django.urls import path
from patient import views

urlpatterns = [
    path('', views.patients, name='patients'),
    path('doctorslist/', views.doctorslist, name="doctorslist"),
    path('consultation/', views.consultation, name="consultation"),
    path('consultation/<str:slug>', views.problem, name="slug"),
    path('appointment/', views.appointment, name="appointment"),
    path('appointment/appointmentform/<str:id>',
         views.appointmentForm, name="appointmentForm"),
    path('appointment/appointmentList/' , views.appointmentList , name="appointmentList")
    
    # path('appointment/appointmentform/handleAppointment/' , views.handleAppointment , name='handleAppointment')
]
