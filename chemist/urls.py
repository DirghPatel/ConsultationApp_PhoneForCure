from django.urls import path
from chemist import views

urlpatterns = [
    path('' , views.chemists , name='chemists')
]