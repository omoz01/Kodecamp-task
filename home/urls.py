from django.urls import path
from . import views


#app_name = "home"

urlpatterns = [
    path('', views.home, name= 'home'),
    path('about', views.about, name= 'about'),
    path('contact', views.contact, name= 'contact'),
    path('login', views.login, name= 'login'),
    path('register', views.register, name= 'register'),
    path('single', views.single, name= 'single'),
    path('blog1', views.blog1, name= 'blog1'),
    path('blog2', views.blog2, name= 'blog2'),
    path('blog3', views.blog3, name= 'blog3'),
    path('signup', views.signup, name='signup'),
]