from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    branch = models.CharField(max_length=30)
    college = models.CharField(max_length=40)
    city = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    def __str__(self) -> str:
        return self.name
