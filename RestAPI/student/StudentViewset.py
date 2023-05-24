from rest_framework import viewsets
from .StudentSerializer import StudentSerializer
from. models import Student

class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer