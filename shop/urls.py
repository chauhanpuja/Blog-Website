from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('quickview/<int:id>',views.quickview,name="quickview"),
    path('userlogin',views.userlogin,name="userlogin"),
    path('userlogout',views.userlogout,name="logoutuser"),
    path('register',views.register,name="register"),
    path('checkout',views.checkout,name="checkout"),
    path('contact',views.contact,name="contact"),
    path('comment',views.comments,name="comment"),
    

]