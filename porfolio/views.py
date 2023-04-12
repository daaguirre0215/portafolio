from django.shortcuts import render
from .models import Project

def home(request):
        projects = Project.objects.all() #antes de renderizar el HTML, hacemos la query a la bdd
        return render(request,'home.html',{'projects':projects})


