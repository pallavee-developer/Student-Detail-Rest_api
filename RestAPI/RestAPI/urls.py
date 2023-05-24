from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from student.StudentViewset import StudentViewset

router = routers.DefaultRouter()
router.register(r'stu', StudentViewset)
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
