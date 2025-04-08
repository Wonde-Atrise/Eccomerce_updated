from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   
    path('signin/',views.Signin, name='signin' ),
        path('login/',views.Login, name='login' ),
        path('pass_foget/',views.Password_Reset,name='pass_reset'),
        path('dashboard/<str:username>',views.DashBoard, name = 'user-interface'),
        path('profile-details/<str:username>', views.Profile_Details, name ="profile_details"),
         path('Edit-profiles/<str:username>', views.Edit_Profiles, name ="edit-profile"),
        path('address/<str:username>', views.Addres, name ="adres"),
          path('my_order/<str:username>', views.My_order, name ="order"),
          path('edit-photo/<str:username>', views.Edit_Photo, name = 'edit-photo'),

        path('logout/',views.Logout, name='logout'),

    

]
