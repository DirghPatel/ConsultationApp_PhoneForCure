from patient.models import bookAppointment
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from doctor.models import Doctor
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login
from patient.models import bookAppointment

# Create your views here.


def doctors(request):
    return render(request, 'doctor/doctorhome.html')


def handledocregister(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        speciality = request.POST.get('speciality')
        experience = request.POST.get('experience')
        hospitalname = request.POST.get('hospitalname')
        hospitalcity = request.POST.get('hospitalcity')
        hospitalarea = request.POST.get('hospitalarea')
        onlinefees = request.POST.get('onlinefees')
        feesatclinic = request.POST.get('feesatclinic')

        doctors = Doctor(name=name, phone=phone, email=email, password=password, speciality=speciality, experience=experience,
                         hospitalname=hospitalname, hospitalcity=hospitalcity, hospitalarea=hospitalarea, onlinefees=onlinefees, feesatclinic=feesatclinic)
        doctors.save()
        myuser = User.objects.create_user(email, email, password)
        myuser.save()

        user = authenticate(username=email,
                            password=password)
        login(request, user)
        return redirect('/doctor/')
    return redirect('/patient')

def register(request):
    logout(request)
    return render(request, 'doctor/docregistration.html')


def requests(request):
    doctor = Doctor.objects.get(email=request.user)
    appointments = bookAppointment.objects.filter(
        doctor=doctor, status='False')
    print(appointments)
    context = {'appointment': appointments}
    return render(request, 'doctor/requests.html', context)


def approveAppointment(request, id):
    if (request.user):
        approved = bookAppointment.objects.get(id=id)
        approved.status = "True"
        approved.save()
        return redirect('/doctor/requests/')
    else:
        return HttpResponse("abcs")


def declineAppointment(request, id):
    if(request.user):
        approved = bookAppointment.objects.get(id=id)
        approved.status = "No"
        approved.save()
        return redirect('/doctor/requests/')
    else:
        return HttpResponse("abcs")
