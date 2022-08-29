from django.shortcuts import render

# Create your views here.
def index(request):
    name = "Java Python"
    template = "index.html"
    return render(request,template,{'nm':name})
