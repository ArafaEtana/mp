from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserCreationForm , SignUpForm
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages


from .forms import SignUpForm

# Create your views here.
def home(request):
    return render(request, 'index.html')


def findFreelancer(request):
    return render (request,'findFreelancer.html')

def findJobs(request):
    return render(request, 'findJobs.html')

def resources(request):
    return render(request, 'resources.html')

def signup(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'HI'+ ' ' + user +', ' +' Account Created successfully! ')
            return redirect('login')
   
    context={'form':form}
    return render(request,'signup.html', context)

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user= authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('buyerDash')
        else:
            messages.info(request,'Username Or password is incorrect')
            return render(request,'login.html')

    context={}
    return render(request,'login.html',context)

