from django.shortcuts import render
from django.http import HttpResponse
from projects.models import Project

# Create your views here

# return project list ...
def project_index(request):
    # query db to get all objects
    proj = Project.objects.all()
    context = {
        'projects': proj
    }
    return render(request, 'projects/index.html', context)

def project_detail(request, specificProj):
    proj = Project.objects.get(pk = specificProj)
    context = {
        'project' : proj
    }
    return render(request, 'project_detail.html', context)
