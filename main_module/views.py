from django.db.models.functions import Coalesce
from django.utils import timezone
from django.db.models import Q, F, DecimalField
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from accounts.models import User
from products.models import Product
from .forms import RegisterForm, LoginForm
from django.utils.crypto import get_random_string
from django.contrib.auth import login, logout
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def main_page(request):
    return render(request, 'main_module/main_page.html')


def activate_account(request, email_active_code):
    if request.method == 'GET':
        user: User = User.objects.filter(email_active_code__exact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                return redirect(reverse('main_page'))
        raise Http404


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
                                email_active_code=get_random_string(72),
                                is_active=False)
                new_user.set_password(user_password)
                new_user.save()
                subject = 'activate account'
                sender = 'mailtrap@demomailtrap.com'
                to = [new_user.email]
                context = {'user': new_user}
                html_message = render_to_string("emails/activate_account.html", context)
                plain_message = strip_tags(html_message)
                email = EmailMultiAlternatives(subject, plain_message, sender, to)
                email.attach_alternative(html_message, "text/html")
                email.send()

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
