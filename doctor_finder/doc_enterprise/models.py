from django.db import models


class doctor(models.Model):
    first_name = models.CharField(max_length = 100,db_index= True)
    last_name = models.CharField(max_length= 100)
    mobile = models.IntegerField(default=7567377)
    profile_pic = models.FileField(upload_to='images/',default='set.jpg')

class patient(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length= 100)
    email = models.EmailField(unique = True)
    doctor_assigned = models.ForeignKey(doctor, on_delete= models.CASCADE)



