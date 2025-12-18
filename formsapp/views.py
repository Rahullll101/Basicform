from django.shortcuts import render
from formsapp.forms import StudentForm
# Create your views here.

def index(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            print("Validation Successfull")
            
    return render(request,"index.html",{'form': form})