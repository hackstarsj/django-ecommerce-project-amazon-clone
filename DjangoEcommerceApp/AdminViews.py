from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url="/admin/")
def admin_home(request):
    return render(request,"admin_templates/home.html")