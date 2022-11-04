from django.db import models

class Employee(models.Model):
    emplyee_regNo = models.CharField(max_length=20,unique=True)
    emplyee_name = models.CharField(max_length=20)
    employee_email = models.EmailField(max_length=20)
    employee_mobile = models.CharField(max_length=20,null=True)
    created_at = models.DateTimeField(auto_now=True)
