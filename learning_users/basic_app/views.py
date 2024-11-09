from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from .forms import UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from . import views
from .models import UserProfileInfo




# Create your views here.



def index(request):
    user = request.user  # Get the authenticated user
    return render(request, 'index.html', {'user': user})



def register(request):

    registered = False

    if request.method =='POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if  user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()


            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        
        else:

            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'registration.html',
                  {'user_form':user_form,'profile_form':profile_form,'registered':registered})




'''
View --> Login  View Function
'''

def userlogin(request):

    if request.method == 'POST':
        username_1 = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(username=username_1,password=pwd)

        if user:
            if user.is_active:
                login(request,user)
                Userinfo=UserProfileInfo.objects.get(user=user)
                print(Userinfo)
                context={"userinfo":Userinfo}
                return render(request,"index.html",context)
            
            else:
                return HttpResponse('User Not Active')
        
        else:
            print('Login Failed due to Wrong User Login')
            return HttpResponse("Invalid Login Details")
        
    else:
        return render(request,'login.html')



''' 
Logout User
'''
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))





