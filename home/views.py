from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login
from django.contrib.auth.models import User
from patient.models import Patient
from doctor.models import Doctor


# Create your views here.


def home(request):
    return render(request, 'home/home.html')

# def handlelogin(request ):

#     if request.method == "POST":
#         loginemail = request.POST.get('email')
#         loginpassword = request.POST.get('password')

#         try:
#             var = Patient.objects.get(email = loginemail)
#             if var.password == loginpassword:
#                 # request.session['user'] = var.email
#                 return redirect('patient')
#             else:
#                 messages.add_message(request, messages.INFO, 'Hello world.')
#         except:
#             return HttpResponse("Hello Not Logged in")

#         # user = authenticate(username=loginemail , password=loginpassword)


#         # if user is not None:
#         #     login(request ,user)
#         #     return redirect('patients')

#         else:
#             return HttpResponse("Not logged in")

def loginpage(request):
    if request.method == "POST":
        loginemail = request.POST.get('email')
        loginpassword = request.POST.get('password')
        try:
            username = Patient.objects.get(email=loginemail)
            print(username.password)
            if username.password == loginpassword:
                user = authenticate(username=loginemail,
                                    password=loginpassword)
                print(user)
                login(request, user)
                return redirect('patients')
        except:
            username = Doctor.objects.get(email=loginemail)
            if username.password == loginpassword:
                user = authenticate(username=loginemail,
                                    password=loginpassword)
                login(request, user)
                return redirect('/doctor/')
    return render(request, 'home/login.html')


def handleregister(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')

        patient = Patient(name=name, phone=phone,
                          email=email, password=password)
        patient.save()
        myuser = User.objects.create_user(email, email, password)
        myuser.save()
        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('patients')

        return redirect('/patient')
    print("request.user")
    print("request.user")
    print(request.user)


def registerationpage(request):
    return render(request, 'home/home.html')


def handlelogout(request):
    logout(request)
    return redirect('patients')
