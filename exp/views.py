from django.shortcuts import render
from django.http import HttpResponse
from .models import Edu, Experience, Tech

# Create your views here.
def index(request):
    edus = Edu.objects.all()
    exps = Experience.objects.all()
    techs = Tech.objects.all()
    context = {"edus" : edus, "exps" : exps, "techs": techs}
    return render(request, "exp.html", context)