from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from django.views import View
from accounts.models import User
from main_module.forms import RegisterForm, LoginForm
from django.contrib.auth import login, logout


def main_page(request):
    return render(request, 'main_module/main_page.html')


def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user_name = register_form.cleaned_data.get('username')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'The entered Email is duplicate.')
            else:
                new_user = User(email=user_email,
                                username=user_name,
                                email_active_code=get_random_string(72))
                new_user.set_password(user_password)
                new_user.save()

        context = {
            'register_form': register_form
        }
        return render(request, 'shared/register.html', context)

    if request.method == 'GET':
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }
        return render(request, 'shared/register.html', context)


def log_in(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        print("1")
        if login_form.is_valid():
            print("2")
            user_email = login_form.cleaned_data.get('email')
            user_pass = login_form.cleaned_data.get('password')

            user: User = User.objects.filter(email__exact=user_email).first()

            if user is not None:
                print("3")
                if not user.is_active:
                    print("4")
                    login_form.add_error('email', "your account has not been activated!")
                else:
                    print("5")
                    pass_validation = user.check_password(user_pass)
                    if pass_validation:
                        print("yesssssssss")
                        login(request, user)
                        return redirect('main_page')
                    else:
                        login_form.add_error('email', "password is wrong!")
                        print("noooo")
            else:
                login_form.add_error('email', "user with the entered profile was not found!")
        return render(request, 'shared\log_in.html', {'login_form': login_form})

    if request.method == 'GET':
        login_form = LoginForm(request.GET)
        return render(request, 'shared\log_in.html', {'login_form': login_form})


def log_out(request):
    logout(request)
    return redirect('main_page')


def footer(request):
    return render(request, 'shared/footer.html')


def otp(request):
    return render(request, 'shared/otp.html')


def successful(request):
    return render(request, 'shared/successful.html')


def header(request):
    return render(request, 'shared/header.html')


def cart(request):
    return render(request, 'shared/cart.html')
