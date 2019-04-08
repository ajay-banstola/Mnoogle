# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.http import HttpRequest, HttpResponseRedirect
# from shop.models import 
from .models import *
from jobs.models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

@login_required(login_url="/account/login")
def products(request):
    obj = products.objects.all().order_by('name')

    if request.method == 'POST':
        form = products_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product Added successfully.')
            return HttpResponseRedirect('/prodform/')

    else:
        form = products_form()
    return render(request, 'jobs/product/list.html', {'form': form})



def custreg(request):
    if request.method == 'POST':
        form = cust_reg_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,
                                     password=password)
            usr = auth.authenticate(username=username, password=password)
            auth.login(request, usr)
            return HttpResponseRedirect('/')

    else:
        form = cust_reg_form()
    return render(request, 'cust_reg.html', {'form': form})


def login(request):
    if request.method == "POST":
        username = request.POST['user']
        password = request.POST['psk']
        try:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect('/')
            else:
                messages.error(request, 'Username or password didn\'t match.')

        except ObjectDoesNotExist:
            print("invalid user")

    return render(request, 'login.html')


# # Views to add product from user
@login_required(login_url="/account/login")
def add_product(request):
    Title =request.POST.get("Title")
    URL =request.POST.get("URL")
    #description = request.POST.get("description")
    #price =request.POST.get("price")
    #available =request.POST.get("available")
    #stock =request.POST.get("stock")
    #created_at =request.POST.get("created_at")
    #updated_at =request.POST.get("updated_at")
    products = Mix(Title=Title, URL = URL)
    #price = price, stock=stock)
    products.save()

    return render(request, 'add_product.html')
    if request.method == 'POST':
        form = products_form(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, 'Product Added successfully.')
            return HttpResponseRedirect('/account/add_product')

        else:
            messages.error(request, 'Invalid entry. Please check the fields')

    else:
        form = products_form()

    return render(request, 'add_product.html', {'form': form})


@login_required(login_url="/account/login")
def profile(request):
    #mixtures = Mix.objects.filter(author=request.user).order_by('-Title')
    jobsprofile = Jobs.objects.filter(flag=True)
    context = {
        'jobsprofile':jobsprofile,
    }
    return render(request, 'profile.html', context)

# @login_required(login_url="/account/login")
# def message(request):
#    # mixtures = Mixture.objects.filter(author=request.user)
#     messages = Message.objects.filter(recipient=request.user)
#     context = {
#      #   'mixtures': mixtures,
#         'messages':messages,
#     }
#     return render(request, '..\directmessages\templates\directmessage\message.html', context)

@login_required(login_url="/account/login")
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


# def pinned(request):
#     if request.GET.get('myModal'):
#         profil = get_object_or_404(Jobs)
#         profil.flag = True
#         profil.save(update_fields=["flag"])
#     return HttpResponseRedirect('/account/profile/')

    

# # This is the view for changing user profile information like description,profile_picture,etc
@login_required(login_url="/account/login")
def edit_profile(request):
    if request.method == 'POST':
        form = UserForm(request.POST or None, request.FILES or None, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/account/profile/')
            messages.success(request, "Successfully Changed")
        else:
            messages.error(request, "Invalid Changes")

    else:
        form = UserForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})


# # This is the view for changing user info

def user_info(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/account/profile')

        else:
            messages.error(request, 'Invalid changes. Please check the fields')

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_info.html', args)


# # View for changing the password
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile')

        else:
            return redirect('/account/profile')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'change_password.html', args)
