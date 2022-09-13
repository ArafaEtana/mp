from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import postJobForm
from .models import postJob


# Create your views here.
def buyerDash(request):
    return render(request, 'dashboardBuyer.html')


def projects(request):
    return render(request, 'project.html')

def postProjects(request):
    form=postJobForm()
    if request.method=="POST":
        form=postJobForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form has been submitted.')
            return redirect('buyerPostProject')
    context={'form': form}
    return render(request,'postProject.html',context)

def allProjects(request):
    project_list=postJob.objects.all()

    context={'project_list':project_list}
    return render(request,"buyerAllProject.html",context)