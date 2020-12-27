from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView, DetailView
from .models import School, Student

from . import models

class LoginView(TemplateView):
    template_name = 'school_app/login.html'

class IndexView(TemplateView):
    template_name = 'school_app/index.html'

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'school_app/school_detail.html'
    



