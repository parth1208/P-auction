from imp import is_builtin
from django.shortcuts import render
from django.contrib.auth import authenticate, login as dj_login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.db import IntegrityError
from .models import *

import datetime
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from django.utils.datastructures import MultiValueDictKeyError
from django.urls import reverse
import imghdr


# Create your views here.
def index(request):
    return render(request, "index.html")

def login(request):
    if request.method == "POST":

        # sign user 
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        # Check authentication 
        if user is not None:
            dj_login(request, user)
            return HttpResponseRedirect(reverse("index"))

        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password.", 
            })
    else:
        return render(request, "login.html")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def signup(request):
    if request.method == "POST":
        first = request.POST["first"]
        last = request.POST["last"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        city = request.POST["City"]
        state = request.POST["State"]
        country = request.POST["Country"]
        Sellect=request.POST["usertype"]
        print(Sellect)
        try:
            image = request.FILES["images"]
        except MultiValueDictKeyError:
            image = ''
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if not first.isalpha():
            return render(request, "signup.html", {
                "message": "First Name contains only letters.",
            })
    
        if password != confirmation:
            return render(request, "signup.html", {
                "message": "Passwords must match.",
            })

        if not image=='':
            check_image = imghdr.what(image)
            if not (check_image== "jpg" or check_image== "jpeg" or check_image== "png"):
                return render(request, "auctions/register.html", {
                    "message": "jpg or png files are accepted.",
                })  

        # Attempt to create new user
        try:
            if Sellect=='bidder':
                user = User.objects.create_user(username=email , email=email, password=password,first_name = first, last_name=last, phone=phone, city=city, state=state, country=country,image=image,is_Budder=True)
                user = authenticate(request, username=email, password=password)
                dj_login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                user = User.objects.create_user(username=email , email=email, password=password,first_name = first, last_name=last, phone=phone, city=city, state=state, country=country,image=image,is_seller=True)
                user = authenticate(request, username=email, password=password)
                dj_login(request, user)
                return HttpResponseRedirect(reverse("index"))

        except IntegrityError:
            return render(request, "signup.html", {
                "message": "Username already taken.",
            })
        return render(request, "login.html")
    else:
        return render(request, "signup.html")
    


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})    
    
def Add_Product(request):
    if not request.user.is_authenticated:
        return redirect('login_user')
    data = 0
    user = User.objects.get(username=request.user.username)
    error = ""
    try:
        data = Bidder.objects.get(user=user)
        if data:
            error = "pat"
    except:
        data = User.objects.get(username=user)
    date1 = datetime.date.today()
    sed = Session_date.objects.all()
    sell = User.objects.get(username=user)
    terror = False
    if request.method == "POST":
        p = request.POST['product_name']
        pr = request.POST['ex_price']
        i = request.FILES['images']
        st_date = request.POST['start_date']
        end_date = request.POST['end_date']
        fr_ct = request.POST['from_city']
        to_ct = request.POST['to_city']
        weight = request.POST['weight']
        p_type = request.POST['parcel_type']
        ses = Session_date.objects.create(date=st_date)
        sta = Status.objects.create(status="pending")
        pro1=Product.objects.create(status=sta,session=ses,name=p, min_price=pr, images=i,from_city=fr_ct,to_city=to_ct,weight=weight,parcel_type=p_type)
        auc=Aucted_Product.objects.create(product=pro1,user=sell)
        terror = True
        
    d = {'sed': sed,'date1': date1,'terror':terror,'error':error}
    return render(request, 'add_product.html', d)    

def profile(request,pk):
    username = User.objects.get(pk = pk)
    context = {
            "username": username,
        }
    return render(request,"profile.html", context)