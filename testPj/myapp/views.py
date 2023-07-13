from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from . import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .models import UserProfile
from django.views.decorators.http import require_http_methods

class TopView(TemplateView):
    template_name = "myapp/top.html"

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "myapp/home.html"

class LoginView(LoginView):
    """ログインページ"""
    form_class = forms.LoginForm
    template_name = "myapp/login.html"

@require_http_methods(['POST'])
def my_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            day = form.cleaned_data['day']
            # データベースに保存するためのモデルインスタンスを作成
            my_model = UserProfile(name=name, day=day)
            my_model.save()
            return redirect('home')  # 成功時のリダイレクト先URLを指定
            #return render(request, 'home.html', {'form': form})
    else:
        form = UserProfileForm()
    return render(request, 'home.html', {'form': form})

'''
@require_http_methods(['POST'])
@login_required(login_url='login')  # ログインが必要な場合はこのデコレータを追加します
def my_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            day = form.cleaned_data['day']
            # データベースに保存するためのモデルインスタンスを作成
            my_model = UserProfile(name=name, day=day)
            my_model.save()
            return redirect('home')  # 成功時のリダイレクト先URLを指定
    else:
        form = UserProfileForm()
    return render(request, 'home.html', {'form': form})
'''

class LogoutView(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = "myapp/login.html"
