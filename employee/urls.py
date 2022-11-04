from django.urls import path
from .api import EmployeeCreateApi, EmployeeApi, EmployeeUpdateApi, EmployeeDeleteApi

urlpatterns = [
    path('create/',EmployeeCreateApi.as_view()),
    path('api',EmployeeApi.as_view()),
    path('api/<int:pk>',EmployeeUpdateApi.as_view()),
    path('api/<int:pk>/delete',EmployeeDeleteApi.as_view()),
]