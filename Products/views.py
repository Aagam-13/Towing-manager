from re import template
from django.shortcuts import render
from .models import * 

# Create your views here.
def show(request):
    sd = StudentData.objects.all()
    template = "table.html"
    return render(request,template,{'data':sd})