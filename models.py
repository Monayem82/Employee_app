from django.db import models

class Employee(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    degignation=models.CharField(max_length=20)
    email=models.EmailField()
    phone_number=models.CharField(max_length=14)
    url=models.URLField(null=True)
    image=models.ImageField(upload_to='employee_app/images/',null=True,default="myimage")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"
