from django.shortcuts import render
from .models import doctor,patient
from .forms import DoctorRegister

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

def doctorFormRegister(request):
    form = DoctorRegister()
    return render(request,'doc_enterprise/doctor-registration2.html',{'form':form})

def doctor_form_register(request):
    if request.method == 'POST':

        form = DoctorRegister(request.POST,request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.first_name = form.cleaned_data['first_name']
            post.last_name = form.cleaned_data['last_name']
            post.mobile = form.cleaned_data['mobile']
            post.profile_pic = form.cleaned_data['profile_pic']
            # doc_data = doctor.objects.create(first_name= first_name,last_name=last_name,mobile=mobile,profile_pic=profile_pic)
            post.save()
            return render(request,'doc_enterprise/doctor-info.html',{'doctor':post})
    else:
        form = DoctorRegister(request.POST)
        return render(request,'doc_enterprise/doctor-info.html',{'form':form})

def registration(request):
    return render(request,'doc_enterprise/registration-form.html')

def registrationDoctor(request):
    print(request.POST)
    return render(request,'doc_enterprise/registration-form.html')

def login(request):
    return render(request,'doc_enterprise/login.html')