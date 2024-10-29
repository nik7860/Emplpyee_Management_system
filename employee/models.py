from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class employeedetail(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    empcode=models.CharField(max_length=100)
    gender=models.CharField(max_length=100,null=True)
    dept=models.CharField(max_length=100,null=True)
    contact=models.CharField(max_length=15,null=True)
    designation=models.CharField(max_length=100,null=True)
    joingdate=models.DateField(null=True)
    
    def __str__(self):
        return self.user.username

class employee_education(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    epg=models.CharField(max_length=100,null=True)
    colpg=models.CharField(max_length=200,null=True)
    perpg=models.CharField(max_length=30,null=True)
    ypg=models.CharField(max_length=30,null=True)
    
    eg=models.CharField(max_length=100,null=True)
    colg=models.CharField(max_length=200,null=True)
    perg=models.CharField(max_length=30,null=True)
    yg=models.CharField(max_length=30,null=True)
    
    ess=models.CharField(max_length=100,null=True)
    colss=models.CharField(max_length=200,null=True)
    perss=models.CharField(max_length=30,null=True)
    yss=models.CharField(max_length=30,null=True)
    
    eh=models.CharField(max_length=100,null=True)
    colh=models.CharField(max_length=200,null=True)
    perh=models.CharField(max_length=30,null=True)
    yh=models.CharField(max_length=30,null=True)
    
    
    def __str__(self):
        return self.user.username
    
class employee_experience(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    company1=models.CharField(max_length=200,null=True)
    company1_des=models.CharField(max_length=200,null=True)
    company1_salary=models.CharField(max_length=100,null=True)
    company1dur=models.CharField(max_length=100,null=True)
    
    company2=models.CharField(max_length=200,null=True)
    company2_des=models.CharField(max_length=200,null=True)
    company2_salary=models.CharField(max_length=100,null=True)
    company2dur=models.CharField(max_length=100,null=True)
    
    company3=models.CharField(max_length=200,null=True)
    company3_des=models.CharField(max_length=200,null=True)
    company3_salary=models.CharField(max_length=100,null=True)
    company3dur=models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.user.username
