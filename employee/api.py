from rest_framework import generics
from rest_framework.response import Response
from .serializer import EmployeeSerializer
from .models import Employee

# Class is for create api view and query all objects
class EmployeeCreateApi(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# Class is for Retrieve apis and query all objects
class EmployeeApi(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# Class is for Update apis data and query all objects
class EmployeeUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# Class is for Delete request api and query all objects
class EmployeeDeleteApi(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
