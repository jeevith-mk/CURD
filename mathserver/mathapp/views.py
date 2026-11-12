
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