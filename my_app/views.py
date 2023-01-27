from django.shortcuts import render, redirect 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from django.contrib.auth.views import PasswordChangeView


  
  
########### register user here #####################################

@unauthenticated_user
def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')

            messages.success(request,"account created successfully for "+ user)


            return redirect('login')
        
        
    context = {'form':form}
    return render(request, 'my_app/register.html',context)

###logout the user
def logoutUser(request):
    logout(request)

    return redirect('login')
  
################ login forms###################################################

def loginPage(request):
    
    
    if request.method == 'POST':
        
        # AuthenticationForm_can_also_be_used__
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password = password)
        if user is not None:
            if user.is_active:

                login(request, user)
            
                return redirect('home')
            else:
                messages.info(request, 'Account not available')
        else:
            messages.info(request, 'username of password is incorrect!! ')
    
    return render(request, 'my_app/login.html')

@login_required(login_url='login')
def Home(request):
    context = {}

    return render(request, 'my_app/main.html', context)


def userPage(request):

    return render( request,'my_app/user.html')






