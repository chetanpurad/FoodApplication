from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from . models import Profile
# Create your views here.

def register(request):
    form=UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request,'users/register.html',{'form':form})

def profile(request):
    profile_instance = Profile.objects.get(user_instance=request.user)
 
    return render(request, 'users/profile.html', {'profile_instance': profile_instance})