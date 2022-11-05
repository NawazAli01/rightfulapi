# rightfulapi
CRUD Apis

In this project, I have added four main Api requests that are GET, POST, PUT, DELETE.

And there are specific urls which should be needed to make requests so I am adding the urls here:

Create: http://127.0.0.1:8000/employee/create/
Retreive: http://127.0.0.1:8000/employee/api/
Update: http://127.0.0.1:8000/employee/api/<int:pk>
Delete: http://127.0.0.1:8000/employee/api/<int:pk>/delete

With the create request we can add employee data. 
With Retrieve request we can retrieve/list employee data. 
with update request we can update specific id data. 
with delete request we can delete specific id data. 

I have used django's generic views classes for apis in this project.
