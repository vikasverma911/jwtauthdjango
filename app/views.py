import imp
from rest_framework import viewsets
from django.shortcuts import render
from app.forms import LoginForm, SignUpForm
from .models import User
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
import requests
import json


URL_reg = "http://127.0.0.1:8000/dj-rest-auth/registration/"
URL_log = "http://127.0.0.1:8000/dj-rest-auth/login/"

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()   


@csrf_exempt
def SignUpView(request):
    form = SignUpForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            data = {
                'username' : form.cleaned_data['username'],
                'email' : form.cleaned_data['email'],
                'password1' : form.cleaned_data['password1'],
                'password2' : form.cleaned_data['password2'],
                'is_student' : form.cleaned_data['is_student'],
                'is_teacher': form.cleaned_data['is_teacher'],
            }
            json_data = json.dumps(data)
            headers = {'Content-type': 'application/json'}
            r = requests.post(url=URL_reg, data=json_data, headers=headers)
            print(r.text)
            

            return render(request, 'app/signup.html', {'form': form})
    else:
        print('error')
    return render(request, 'app/signup.html', {'form': form})


@csrf_exempt
def LoginView(request):
    form = LoginForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            data = {
                'username': form.cleaned_data['username'],
                'email': form.cleaned_data['email'],
                'password': form.cleaned_data['password'],
            }
            json_data = json.dumps(data)
            headers = {'Content-type': 'application/json'}
            r = requests.post(url=URL_log, data=json_data, headers=headers)
            print(r.cookies.set_cookie)
            r.cookies.add_cookie_header
            return render(request, 'app/login.html', {'form': form})
    else:
        print("error")
    return render(request, 'app/login.html', {'form': form})
