"""doctor_finder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('doctor-registration-page/',views.doctor_registration_page,name='doctor-registration-page'),
    path('doctor-registration/',views.doctor_register,name='doctor-register'),
    path('doctor-profile/',views.doctor_profile,name='doctor_profile'),
    path('doctor-register/',views.doctorFormRegister,name='doctor-form-register'),
    path('doctor-register-data/',views.doctor_form_register,name='doctor-data'),
    path('registration-form/',views.registration,name='registration'),
    path('registration-form-2/',views.registrationDoctor,name='register-doctor-data'),
    path('login/',views.login,name='login')
    

]
