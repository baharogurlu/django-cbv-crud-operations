from django.contrib import admin
from basic_app.models import Student,School

# Register your models here.

admin.site.register(School)
admin.site.register(Student)