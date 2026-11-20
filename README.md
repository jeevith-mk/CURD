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
views.py
from django.shortcuts import render

def calculate_churn_rate(request):
    context = {}
    
    if request.method == "POST":
        initial_str = request.POST.get("Initialcust", "0")
        present_str = request.POST.get("Presentcust", "0")
        
        Initialcust = int(initial_str) if initial_str else 0
        Presentcust = int(present_str) if present_str else 0
        
        if Initialcust > 0:
            churn_rate = ((Initialcust - Presentcust) / Initialcust) * 100
        else:
            churn_rate = 0
            
        # This will output the calculated value directly in your terminal
        print("Calculated Churn Rate:", round(churn_rate, 2), "%")
            
        context = {
            "Initialcust": Initialcust,
            "Presentcust": Presentcust,
            "churn_rate": round(churn_rate, 2),
        }
            
    return render(request, "mathapp/math.html", context)

    urls.py
    from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns=[
    path('admin/', admin.site.urls),
    path('',views.calculate_churn_rate,name='calculate_churn_rate'),
]

math.html
<html>
    <head>
        <title>churn calculator</title>
        <h1 align="center">M.K.JEEVITH</h1>
        <h1 align="center">26018300</h1>
    </head>
    <body>
        <h1>jeevith 26018300</h1>
        <form method="POST">
            {%csrf_token%}
            <label style="color: rgb(255, 0, 0);"">INITIAL CUSTOMER:</label>
            <input type="number" name="Initialcust" value="{{Initialcust}}" ><br><br>
            <label style="color:blue">PRESENT CUSTOMER:</label>
            <input type="number" name="Presentcust" value="{{Presentcust}}"><br><br>
            <input style="color: blueviolet;" type="submit" value="calculate">
            <input  style="color:indigo" type="reset" value="clear">
            <h2>churnRate:{{ churn_rate }}</h2>
        </form>
        
    </body>
</html>
```
## OUTPUT
## Server Side Processing
![alt text](<Screenshot (127).png>)
## Home page
![alt text](<Screenshot (128).png>)
## RESULT
The programme for server side process is completed successfully


