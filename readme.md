# Django Forms
# This repository contains a basic Django Forms project that demonstrates how to create, display, and validate a form on a single HTML page, without using models or database operations.

The project focuses purely on understanding Django Forms workflow.

🚀 Project Overview

Django Forms provide a clean and secure way to:

Generate HTML forms automatically

Validate user input

Handle form submission using views

Avoid writing raw HTML input validation logic

In this project:

❌ No models are used

❌ No database interaction

❌ No data storage

✅ Single page form handling

✅ Form validation using Django Forms

🛠️ Technologies Used

Python

Django 5.x

HTML (Django Templates)

## 📂 Project Structure
Basicform/
│
├── Basicform/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── formsapp/
│   ├── templates/
│   │   └── index.html
│   ├── forms.py
│   ├── views.py
│   ├── models.py
│   ├── tests.py
│   └── apps.py
│
├── manage.py
└── README.md

##⚙️ Step-by-Step Implementation
1️⃣ Create Django Project
django-admin startproject Basicform
cd Basicform

2️⃣ Create Django App
python manage.py startapp formsapp


## ⚠️ Important Design Choice
The formsapp is NOT added to INSTALLED_APPS because:

No models are used

No migrations are required

No admin features are needed

The app is used only for views, forms, and templates, which Django can load directly.

## 3️⃣ Create Django Form

📁 formsapp/forms.py
from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    Phone = forms.IntegerField()
    address = forms.CharField(max_length=100)
    marks = forms.IntegerField()

✔ Defines form fields in Python
✔ Enables automatic validation
✔ Independent of database 

## 4️⃣ Create View

📁 formsapp/views.py

from django.shortcuts import render
from formsapp.forms import StudentForm

def index(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            print("Validation Successfull")
            
    return render(request,"index.html",{'form': form})


✔ Handles GET & POST requests
✔ Validates form data using is_valid()
✔ Displays form on the same page

# 5️⃣ Configure URLs

📁 Basicform/urls.py

from django.contrib import admin
from django.urls import path
from formsapp import views

urlpatterns = [
    path("", views.index),
    path('admin/', admin.site.urls),
]


✔ Directly maps URL to view
✔ No app-level urls.py required

# 6️⃣ Create Template

📁 formsapp/templates/index.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Django Forms</title>
</head>
<body>
    <h1>Student Forms</h1>
    <form method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="submit">
    </form>
</body>
</html>

## ▶️ Run the Project
python manage.py runserver


Open in browser:

http://127.0.0.1:8000/

✔ csrf_token for security
✔ form.as_p auto-renders fields
✔ No manual HTML inputs needed


# ✅ Output

Student form is displayed

User enters details

On submit:

Django validates all fields

Console prints “Validation Successfull”

Page reloads with validated data

## 🔍 Why This Works Without INSTALLED_APPS (Diagram-Style)
Browser Request
      ↓
Basicform/urls.py
      ↓
View Function (index)
      ↓
StudentForm (forms.py)
      ↓
Template (index.html)

✔ Key Insight:

Django only needs INSTALLED_APPS for framework-level features like:

Models

Admin

Migrations

Views, forms, and templates are plain Python modules and can be imported directly.





## 👤 Author

Rahul Halkarni
🔗 GitHub: https://github.com/Rahullll101

🔗 LinkedIn: www.linkedin.com/in/rahul-h-7a3456225
