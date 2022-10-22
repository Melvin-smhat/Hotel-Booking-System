from django.urls import path
from.views import *

urlpatterns = [
 path('',dashboard,name='dashboard'),
    path('about',about,name='about'),
    path('service',service,name='service'),
    path('pricing',pricing,name='pricing'),
    path('blog',blog,name='blog'),
    path('blog_single',blog_single,name='blog_single'),
    path('testimonials',testimonials,name='testimonials'),
    path('register',register,name='register'),
    path('homepage',homepage,name='index'),
    path('login',log_in,name='login'),
    path('logout',log,name='logout')
]
