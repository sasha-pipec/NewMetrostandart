from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View


# Create your views here.

class HomePageRenderView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'metrostandart/index.html')


class AuthorizationPageRenderView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'metrostandart/login.html')

    # def post(self, request, *args, **kwargs):
    #     user = authenticate(request, username=request.POST["login"], password=request.POST["password"])
    #     if user is not None:
    #         login(request, user)
    #         return redirect('home')
    #     return render(request, 'metrostandart/login.html', context={
    #         'error': 'Не верный логин или пароль'
    #     })


class RegistrationPageRenderView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'metrostandart/register.html')

    # def post(self, request, *args, **kwargs):
    #     User.objects.create_user(
    #         username=request.POST['login'],
    #         password=request.POST['password'],
    #         email=request.POST['email']
    #     )
    #     return redirect('login')
