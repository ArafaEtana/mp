from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.buyerDash,name="buyerDash" ),
    path('projects/', views.projects,name="buyerProject" ),
    path('projects/postProjects/', views.postProjects,name="buyerPostProject" ),
    path('projects/allProjects/', views.allProjects,name="buyerAllProject" ),

   
]