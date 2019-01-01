from django.shortcuts import render
from .models import doctor,patient

# Create your views here.
def doctor_registration_page(request):
    return render(request,"doc_enterprise/doctor-registration.html")

def doctor_profile(request):
    return render(request,"doc_enterprise/doctor-profile.html")


def doctor_register(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    mobile = request.POST['mobile']
    profile_pic = request.FILES['profile_pic']

    doctor_new = doctor.objects.create(first_name= first_name,last_name=last_name,mobile=mobile,profile_pic=profile_pic)
    return render(request,"doc_enterprise/doctor-profile.html",{'doctor_data':doctor_new})


    # d = doctor()
    # d.first_name =  request.POST['first_name']
    # d.save()
