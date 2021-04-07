from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,CreateView,UpdateView,DetailView
from DjangoEcommerceApp.models import Categories,SubCategories
from django.contrib.messages.views import SuccessMessageMixin

@login_required(login_url="/admin/")
def admin_home(request):
    return render(request,"admin_templates/home.html")

class CategoriesListView(ListView):
    model=Categories
    template_name="admin_templates/category_list.html"

class CategoriesCreate(SuccessMessageMixin,CreateView):
    model=Categories
    success_message="Category Added!"
    fields="__all__"
    template_name="admin_templates/category_create.html"

class CategoriesUpdate(SuccessMessageMixin,UpdateView):
    model=Categories
    success_message="Category Updated!"
    fields="__all__"
    template_name="admin_templates/category_update.html"


class SubCategoriesListView(ListView):
    model=SubCategories
    template_name="admin_templates/sub_category_list.html"

class SubCategoriesCreate(SuccessMessageMixin,CreateView):
    model=SubCategories
    success_message="Sub Category Added!"
    fields="__all__"
    template_name="admin_templates/sub_category_create.html"

class SubCategoriesUpdate(SuccessMessageMixin,UpdateView):
    model=SubCategories
    success_message="Sub Category Updated!"
    fields="__all__"
    template_name="admin_templates/sub_category_update.html"

