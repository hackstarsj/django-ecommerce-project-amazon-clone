from django.shortcuts import render

def admin_home(request):
    return render(request,"admin_templates/home.html")