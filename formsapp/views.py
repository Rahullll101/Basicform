from django.shortcuts import render
from formsapp.forms import StudentForm
# Create your views here.

def index(request):
    form = StudentForm()
    return render(request,"index.html",{'form': form})