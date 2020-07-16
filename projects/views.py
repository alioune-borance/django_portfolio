from django.shortcuts import render
from projects.models import Project

def index(request):
    projects = Project.objects.all()

    context = {
        'projects': projects
    }

    return render(request,"indexView.html",context)


def detail(request,id):
    project = Project.objects.get(pk=id)
    context = {
        'project': project
    }
    return render(request,"detail.html",context)
