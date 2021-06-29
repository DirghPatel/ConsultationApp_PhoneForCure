from django.db.models.expressions import Value
from django.db.models.functions.text import Replace
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import CommonHealthProblem, Patient
from django.contrib.auth.models import User
from doctor.models import Doctor
from django.conf import settings
from patient.models import CommonHealthProblem
from patient.models import bookAppointment


def patients(request):
    return render(request, 'patient/patienthome.html')


def doctorslist(request):
    doctors = Doctor.objects.all()
    context = {'doctors': doctors}
    return render(request, 'patient/doctorslist.html', context)


def consultation(request):
    problems = CommonHealthProblem.objects.all()
    path = settings.MEDIA_URL
    context = {'problems': problems, 'path': path}
    # if request.user.is_authenticated:
    return render(request, 'patient/consultation.html', context)
    # else:
    #     return redirect('home')


def problem(request, slug):
    problem = CommonHealthProblem.objects.filter(slug=slug).first()
    print(problem)

    if problem.__getattribute__('problem') == 'Cough & Cold':
        doctors = Doctor.objects.filter(speciality='Physician')
    if problem.__getattribute__('problem') == 'Stomach Issues':
        doctors = Doctor.objects.filter(speciality='Gastroenterologist')
    if problem.__getattribute__('problem') == 'Sick Kid':
        doctors = Doctor.objects.filter(speciality='Pediatrician')
    if problem.__getattribute__('problem') == 'Period Problems':
        doctors = Doctor.objects.filter(speciality='Gynaecologist')
    if problem.__getattribute__('problem') == 'Depression & Anxiety':
        doctors = Doctor.objects.filter(speciality='Psychiatrist')
    if problem.__getattribute__('problem') == 'Performance Issue In Bed?':
        doctors = Doctor.objects.filter(speciality='Sexologist')
    if problem.__getattribute__('problem') == 'Skin Problems':
        doctors = Doctor.objects.filter(speciality='Dermatologist')
    if problem.__getattribute__('problem') == 'Weight Lose':
        doctors = Doctor.objects.filter(speciality='Nutritian')
    path = settings.MEDIA_URL
    context = {'problem': problem, 'path': path, 'doctors': doctors}
    return render(request, 'patient/filterdoc.html', context)


def appointment(request):
    doctor = Doctor.objects.all()
    context = {'doctors': doctor }
    if request.user.is_authenticated:
        return render(request, 'patient/appointment.html', context)
    else:
        return redirect('home')


def appointmentForm(request, id):

    if(request.user.is_authenticated):
        doctor = Doctor.objects.get(id=id)
        patient = Patient.objects.get(email = request.user)
        print(patient)
        
        print(doctor)
        if request.method == 'POST':

                doctor = Doctor.objects.get(email=doctor.email)
                name = request.POST.get('name')
                phone = request.POST.get('phone')
                email = request.POST.get('email')
                time = request.POST.get('time')
                problem = request.POST.get('problem')

                appointment = bookAppointment(
                    doctor=doctor, name=name, phone=phone, email=email, time=time, problem=problem)
                appointment.save()
                return redirect('/patient')

        context = {'doctor': doctor , 'patient': patient}
        return render(request, 'patient/appointmentForm.html', context)
    else:
        return redirect('home')

def appointmentList(request):
    if(request.user.is_authenticated):
        patient = Patient.objects.get(email = request.user)
        print(patient.email)
        appointments = bookAppointment.objects.filter(email = patient.email)
        context={'appointments': appointments}
        return render(request , 'patient/appointmentList.html' , context)
    else:
        return redirect('home')