from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from exp.models import Tech

# Create your views here.
def index(request):
    projects = Project.objects.all()
    tech = Tech.objects.all()
    context = {"projects" : projects, "techs": tech}
    return render(request, "projects.html", context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    tech = Tech.objects.all()
    context = {"project": project, "techs": tech}
    return render(request, "projectDetail.html", context)