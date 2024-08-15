from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'page'

urlpatterns = [

    #------------STORE URLS------------------
    path('<int:product_id>', views.detailpage, name="detailpg"),
    path('cart/', views.cartpage, name="cartpage"),

    #------------DOG URLS------------------
    path('dogs/', views.productsfordogs, name="dogproducts"),
    path('dogfood/', views.dogfood, name="dogfood"),
    path('dogtoys/', views.dogtoys, name="dogtoys"),
    path('dogbeds/', views.dogbed, name="dogbeds"),
    path('dogbowls/', views.dogbowl, name="dogbowls"),

    #------------CAT URLS------------------
    path('cats/', views.productsforcats, name="catproducts"),
    path('catfood/', views.catfood, name="catfood"),
    path('cattoys/', views.cattoy, name="cattoys"),
    path('catbeds/', views.catbed, name="catbeds"),
    path('catbowls/', views.catbowl, name="catbowls"),

    #------Authentication---------------
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    path('password/', auth_views.PasswordChangeView.as_view(), name="password"),
    path('example_logins/', views.examplelogins, name="examplelogins"),

    #--------------BOOKING PAGE-----------------------------
    path('booking/', views.booking, name="booking"),

    #--------------Customer Dashboard-----------------------------
    path('dash/', views.customerdashboard, name="customerdashboard"),
    path('customerprofilemyorders/', views.customerprofilemyorders, name="customerprofilemyorders"),
    path('customerprofileaddresses/', views.customerprofileaddresses, name="customerprofileaddresses"),
    path('customerprofilewishlist/', views.customerprofilewishlist, name="customerprofilewishlist"),


    #--------------Customer Dashboard-----------------------------
    path('about-us/', views.aboutus, name="aboutus"),
]