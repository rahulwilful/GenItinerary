from django.db import models

# Create your models here.

# Department Model
class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=30,default='India', choices=(
                                                        ('India', 'India'),
                                                        ('England','England'),
                                                        ('China','China')
                                                        ))
    createdDate = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    #department = models.CharField(max_length=30, choices=(
    #                                                        ('IT', 'IT'),
    #                                                        ('Admin','Admin'),
    #                                                        ('HR','HR')
    #                                                    ))

    def __str__(self):
        return self.name 
    

# User Model
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    address = models.TextField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)



