from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.home , name="home"),
    path('findJobs/', views.findJobs, name="findJobs"),
    path('findFreelancer/', views.findFreelancer , name="findFreelancer"),
    path('resources/', views.resources, name="resources"),
    path('login/',views.loginpage , name="login"),
    path('signup/',views.signup, name="signup"),

]