from django.shortcuts import render
from rest_framework.views import APIView
from django.views.generic import TemplateView
# Create your views here.


class Introduction(TemplateView):
    template_name = 'index.html'
    


 