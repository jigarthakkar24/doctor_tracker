from django.shortcuts import render
from .models import doctor,patient

# Create your views here.
def first(request):
    doctor_data = doctor.objects.create(first_name ='rajan',last_name = 'sharma',email='rajan@gmail.com')
    all_data_doc = doctor.objects.all()
    doctor.objects.get(id=1).delete()
    return render(request,'doc_enterprise/index.html',{'all_data_doc':all_data_doc})
