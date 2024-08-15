from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, DeleteView, UpdateView
from .models import product, Collection
from django.contrib.auth import authenticate, login, logout
from petstore.urls import *
from .forms import *
from django.contrib import messages

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            return redirect('homepage')
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('homepage')



def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            user = authenticate(username=username, password=password, email=email, )
            login(request, user)
            messages.success(request, ("Registartion Successful"))
            return render(request, 'homepage.html')
    else:
        form = RegisterUserForm()
    return render(request,'authentication/customeraccountregister.html', {'form':form})



def examplelogins(request):
    return render(request,'authentication/examplelogins.html')


def customerdashboard(request):
    return render(request, 'customerdashboard.html')

def customerprofilemyorders(request):
    return render(request, 'customerorders.html')

def customerprofileaddresses(request):
    return render(request, 'customeraddresses.html')

def customerprofilewishlist(request):
    return render(request, 'customerwishlist.html')



def home(request):
    return render(request, 'homepage.html')

def detailpage(request, product_id):
    products = get_object_or_404(product, id=product_id)
    return render(request, 'detailpg.html', {'product': products})

def productsfordogs(request):
    return render(request, 'pets/dogs.html')


def productsforcats(request):
    return render(request, 'pets/cats.html')

def cartpage(request):
    return render(request, 'cartpage.html')

def aboutus(request):
    return render(request, 'aboutus.html')


#PRODUCTS FOR DOGS

def dogfood(request):
    dogfood = product.objects.filter(collection__id=1)
    return render(request, 'collectionpages/dogcollections/dogfood.html', {'dogfood':dogfood})


def dogtoys(request):
    dogtoys = product.objects.filter(collection__id=2)
    return render(request, 'collectionpages/dogcollections/dogtoys.html', {'dogtoys':dogtoys})



def dogbed(request):
    dogbeds = product.objects.filter(collection__id=3)
    return render(request, 'collectionpages/dogcollections/dogbeds.html', {'dogbeds':dogbeds})

def dogbowl(request):
    dogbowls = product.objects.filter(collection__id=4)
    return render(request, 'collectionpages/dogcollections/dogbowls.html', {'dogbowls':dogbowls})

#----------------------------------------------------


def catfood(request):
    catfoods = product.objects.filter(collection_id=5)
    return render(request, 'collectionpages/catcollections/catfood.html', {'catfoods':catfoods})



def cattoy(request):
    cattoys = product.objects.filter(collection_id=6)
    return render(request, 'collectionpages/catcollections/cattoys.html', {'cattoys':cattoys})

def catbed(request):
    catbeds = product.objects.filter(collection_id=7)
    return render(request, 'collectionpages/catcollections/catbeds.html', {'catbeds':catbeds})


def catbowl(request):
    catbowls = product.objects.filter(collection_id=8)
    return render(request, 'collectionpages/catcollections/catbowls.html', {'catbowls':catbowls})


def booking(request):
    return render(request, 'booking/groomingcalendar.html')