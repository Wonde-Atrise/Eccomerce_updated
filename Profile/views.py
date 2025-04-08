from django.shortcuts import render,redirect, HttpResponseRedirect,get_object_or_404
from django.core.mail import send_mail
from django.contrib.auth.views import PasswordResetView


from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import get_user_model
from .models import Profile



import os

# Create your views here.
Is_user_logged = ""
def Signin(request):
    
    if request.method == "POST":
       First_name = request.POST.get('fname')
       Last_name = request.POST.get('lname')
       username = request.POST.get('username')
       email = request.POST.get('email')
       password = request.POST.get('password')
       confrim_pass = request.POST.get('cpassword')
       if User.objects.filter(username = username):
         messages.error(request, "Username Already taken, Please choose other one ")
         redirect('signin')
       elif User.objects.filter(email =email):
         messages.error(request, "Email Already taken, please choose other one ")
         redirect('signin')
       elif password != confrim_pass:
        messages.error(request, "Password is not match")
       else:
        User.objects.create_user(
           first_name =First_name,
           last_name = Last_name,
           email=email,
           username= username,
           password=password
           
       )
        phone_number = request.POST.get('phone'),
        birth_date = request.POST.get('birth_date')
        user_fetch = User.objects.get(username = username)
        print(user_fetch.username)
        print(request.POST.get('phone'))
        Profile_Detail = Profile.objects.create(user = user_fetch,
                                               
                                                            
                 
            )
        Profile_Detail.save()

         
        authenticate(request, username=username, password = password)
        messages.success(request,"Account Created ")
        return render(request, 'signin.html')

    return render(request, 'signin.html')
def Login(request):
    
   if request.user.is_authenticated:
        return redirect('home')

   if request.method == 'POST':
        username = request.POST.get('username')
       
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exit')
            return render(request, 'login.html')

    
    
   
   return render(request, 'login.html')
  
def Password_Reset(request):
    return render(request, 'forget-password.html') 


def Logout(request):
     if request.user.is_authenticated:
         logout(request)
         return redirect('home')
     else:  
          return redirect('login') 
     
def DashBoard(request,username):
     
    
     if username != request.user.is_authenticated:
        profiles = User.objects.filter(username = username)
        if profiles.exists():
         user = profiles.first()
        return render(request, 'dashboard.html',{'profiles':user,'username':user.username})  
     else:
        
        profiles = User.objects.filter(username =  request.user)
        if profiles.exists():
         user = profiles.first()
         return render(request, 'dashboard.html',{'profiles':user,'username':user.username})   
       
      
     
     
     return render(request, 'dashboard.html')   

def Profile_Details(request,username):
   
    if username != request.user.is_authenticated:
     print("i")
     profiles = User.objects.filter(username = username )
     
     if profiles.exists():
      user = profiles.first()
     
      return render(request, 'profile-details.html',{'profiles':user,'username':user.username})  
    else:
      print("ii")
      userPro =request.user
      profiles = User.objects.filter(username = userPro)
      if profiles.exists():
        user = profiles.first()
        return render(request, 'profile-details.html',{'profiles':user,'username':user.username}) 

        
    return render(request, 'profile-details.html',{'username':username})       

    return render(request, 'profile-details.html')       
def  Addres(request, username):
 if request.user.is_authenticated:
    userPro = username
    if userPro != request.user:
        return render(request, 'address.html',{'username':userPro})
    else: 
        userPro =request.user
        return render(request, 'address.html',{'username':userPro})
 else:
    return render(request, 'address.html',{'username':username})

 return render(request, 'address.html')


def My_order(request, username):
   
   userPro =username 
   if request.user.is_authenticated:
      
    if userPro != request.user:
            return render(request, 'order.html',{'username':userPro})
    else: 
        userPro =request.user
        return render(request, 'address.html',{'username':userPro})
   else:
              return render(request, 'address.html',{'username':username})
 # Get your custom user model
User = get_user_model()   
def Edit_Profiles(request, username):


    user_value = get_object_or_404(User, username=username)
    try:
     user_profile = Profile.objects.get(user=user_value)
    except Profile.DoesNotExist:
     user_value = get_object_or_404(User, username=username)
     user_profile = Profile.objects.create(user=user_value)
    # Optionally, you might want to set other default profile fields here
    # user_profile.date_birth = ...
    # user_profile.phone = ...
     user_profile.save() # Important to save the newly created profile

# Now you can work
    if request.method == "POST":
        user_value.first_name = request.POST.get('first_name')
        user_value.last_name = request.POST.get('last_name')
        user_value.email = request.POST.get('email')
        user_value.username = request.POST.get('username')  # Be cautious about changing username
        user_profile.phone_number = request.POST.get('phone')
        user_profile.birth_date = request.POST.get('birth_date')
         
        # Handle photo upload if you have a file field
        user_profile.save()
        user_value.save()
        if request.FILES['image']:
           user_profile.profile_image= request.FILES['image']
           user_profile.save()
           
           return redirect('profile_details', username=user_value.username)  # Redirect to the user's profile page
        else:
          return redirect('profile_details', username=user_value.username)  # Redirect to the user's profile page

    return render(request, 'Edit-profile.html', {'profiles': user_value,'user_det':user_profile})

def Edit_Photo(request, username):
   list_user = User.objects.get(username =username)
   user = list_user.id
   filter_user = Profile.objects.get(user = user)
   if request.method == "POST":
      if request.FILES['image']:
         filter_user.profile_image = request.FILES['image']
         filter_user.save()
      return redirect('profile_details', username=list_user.username)  # Redirect to the user's profile page
   return redirect('profile_details', username=list_user.username)


   