"""
from django.shortcuts import render
from .forms import MyForm

# Create your views here.
def Home(request):
    return render(request, "home.html")

def my_view(request):
    form = MyForm()
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MyForm()
    return render(request, "home.html", {"form": form})
"""
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from . import forms


class TopView(TemplateView):
    template_name = "myapp/top.html"

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "myapp/home.html"

class LiginView(LoginView):
    """ログインページ"""
    form_class = forms.LoginForm
    template_name = "myapp/login.html"

class LogoutView(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = "myapp/login.html"



