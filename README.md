# EX.No: 03 DEVELOP A DJANGO-BASED CRUD APPLICATION
## Date:12/11/2026
## AIM
create a webpage to find the churn rate of a company

## ALGORITHM
## Step 1:
clone git repository
## Step 2:
create a project inside the repo using Django Admin
## Step 3:
create a app inside the project by pyhton
## Step 4:
code the views.py and urls.py 
## Step 5:
code the math.html and add the url link to urls.py 
## Step 6:
run the webpage
## PROGRAM
```
math.html
<html>
    <head>
        <title>area calculator</title>
        <h1 align="center">M.K.JEEVITH</h1>
        <h1 align="center">26018300</h1>
    </head>
    <body>
        <form method="POST">
            {% csrf_token %}
            <label style="color: rgb(255, 0, 0);"">INITIAL CUSTOMER:</label>
            <input type="number" name="x" ><br><br>
            <label style="color:blue">PRESENT CUSTOMER:</label>
            <input type="number" name="y"><br><br>
            <input style="color: blueviolet;" type="submit" value="calculate">
            <input  style="color:indigo" type="reset" value="clear">
        </form>
        <h2>churnRate:{{ churnRate }}</h2>
        <p>{{ error }}</p>
    </body>
</html>

views.py

from django.shortcuts import render

def calculate_churnRate(request):
    x = 0
    y = 0
    churnRate = 0
    try:
        if request.method == "POST":
            x = int(request.POST.get("x"))
            y = int(request.POST.get("y"))
            churnRate = ((x-y)/x)*100
    except(ValueError,KeyError):
        print("error")

    return render(request, "mathapp/math.html", {
        "INITIAL_CUSTOMER":x ,
        "PRESENT_CUSTOMER": y,
        "churnRate": churnRate
    })

urls.py
from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns=[
    path('admin/', admin.site.urls),
    path('',views.calculate_churnRate,name='calculate_churnRate'),
]
```


## OUTPUT
## Server Side Processing
![alt text](<Screenshot (119).png>)
## Home page
![alt text](<Screenshot (118).png>)
## RESULT
The programme for server side process is completed successfully


