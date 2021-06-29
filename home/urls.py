from django.urls import path
from . import views

urlpatterns = [
    path('', views.home ,name='home'),
    path('loginpage/' , views.loginpage , name="loginpage"),
    # path('loginpage/handlelogin/' , views.handlelogin , name="handlelogin"),
    path('registerationpage' , views.registerationpage , name="registerationpage"),
    path('handleregister/' , views.handleregister , name="handleregister"),
    path('logout/' , views.handlelogout , name="handlelogout")
]