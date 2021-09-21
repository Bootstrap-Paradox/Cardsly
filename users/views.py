from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
import datetime

from django.template import RequestContext

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages, sessions

from .models import Users, username_validation

from .forms import SignupForm, LoginForm

from django.core.mail import send_mail
from . import auth

from beautifulCards.backend.mail import Mailing_system


import sys
sys.path.append("..")

# from backend.mail import welcome_email


def logged_in(function):
    def wrapper(*args, **kwargs):
        request, *data = args
        logged = request.COOKIES.get("logged_in", False)
        print(logged)
        if not logged:
            return function(*args, **kwargs)

        else:
            return redirect('/')

    return wrapper


def set_cookie(response: HttpResponseRedirect, content: dict):
    def get_expiry(days=1):
        max_age = days * 24 * 60 * 60
        expires = datetime.datetime.strftime(
            datetime.datetime.utcnow() +
            datetime.timedelta(seconds=max_age),

        )
        return (max_age, expires)

    try:
        keys = content.keys()

        for key in keys:
            max_age, expires = get_expiry(content[key][1])
            response.set_cookie(key, content[key][0], max_age, expires)

    except Exception as error:
        print(error)

    return response

# Create your views here.


def signup(response):

    if response.method == "POST":
        form = SignupForm(response.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            signed_in, user_data, message = auth.sign_up_user(
                username, email, password)
            if signed_in:
                new_response = redirect("/")
                return set_cookie(new_response, {"logged_in": [True, 15]})

    else:
        form = SignupForm()
        # welcome_email()
        # print(form)

    return render(response, "users/signup.html", {"form": form})


@logged_in
def login(response):
    if response.method == "POST":
        form = LoginForm(response.POST)

        if form.is_valid():
            login_text = form.cleaned_data['login_text']

            # user_data = Users.objects.filter(username=login_text).first() if Users.objects.filter(username=login_text).first() else Users.objects.filter(email=login_text).first()
            logged_in, user_data, message = auth.login_user(
                login_text, form.cleaned_data['password'])
            if logged_in:
                messages.success(response, message)
                new_response = redirect('/')
                return set_cookie(
                    new_response,
                    {
                        "logged_in": [True, 15]
                    }
                )

            else:
                messages.error(response, message)

    else:
        form = LoginForm()

    # if response.method == 'POST':
    #     print(response.POST["email"])
    #     # welcome_email()
    #     return redirect('/')
    return render(response, "users/login.html", {"form": form})
