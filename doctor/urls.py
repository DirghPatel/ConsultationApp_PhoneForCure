from django.urls import path
from doctor import views

urlpatterns = [
    path('' , views.doctors , name='doctors'),
    path('register/' , views.register , name='register'),
    path('register/handledocregister/' , views.handledocregister , name='handledocregister'),
    path('requests/' , views.requests , name='requests'),
    path('requests/approveAppointment/<int:id>',
         views.approveAppointment, name="approveAppointment"),
    path('requests/declineAppointment/<int:id>',
         views.declineAppointment, name="declineAppointment"),
]