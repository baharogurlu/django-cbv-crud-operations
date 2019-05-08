from django.shortcuts import render
from django.views.generic import (View, TemplateView, DetailView, ListView, CreateView, DeleteView, UpdateView)
from . import models
from django.urls import reverse_lazy

class SchoolListView(ListView):
    context_object_name = 'schools'

    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'


class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal') #Location ın değiştirilmesini istemiyoruz
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")


"""
STUDENT OPERATIONS
"""


class StudentListView(ListView):
    context_object_name = 'students'
    model = models.Student

class StudentDetailView(DetailView):
    context_object_name = 'student_detail'
    model = models.Student
    template_name = 'basic_app/student_detail.html'


class StudentCreateView(CreateView):
    fields = ('name', 'age', 'school')
    model = models.Student


class StudentUpdateView(UpdateView):
    fields = ('name', 'age', 'school')
    model = models.Student

class StudentDeleteView(DeleteView):
    model = models.Student
    success_url = reverse_lazy("basic_app:student_list")



class IndexView(TemplateView):
    template_name = 'index.html'

