import imp
from multiprocessing import AuthenticationError
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.forms import ValidationError
from django.shortcuts import redirect, render, get_object_or_404

from .forms import *

# Create your views here.
def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        password = form.cleaned_data.get('password')
        username = form.cleaned_data.get('username')
        user = authenticate(
            username=username,
            password=password
        )
        if user :
            login(request=request,user= user)
            url = request.GET.get('next')
            if url:
                return redirect(url)
            else:
                return redirect('project:list_view')
        else:
            form.add_error(field=None, error= AuthenticationError("Incorrect username or password"))


    context ={
        'form':form
    }
    return render(request,'account/login.html',context)

def logout_view(request):
    logout(request)
    return redirect('project:list_view')


def profile_create_view(request):
    form = ProfileCreateForm(request.POST or None)
    user = request.user
    qs = Profile.objects.filter(user_id = user.id)
    # qs = Profile.objects.get(user_id = user.id)
    # print(qs.first_name)
    if qs:
        print('redirecting')
        return redirect ('account:detail_view')
        # return render(request,'account/detail.html',{'object':qs})

    if form.is_valid():
        form.save(commit=False)
        profile = form.instance
        profile.user =request.user
        # profile.save()
        form.save()
        redirect('account:detail_view')

    context ={
        'form':form
    }
    return render(request,'account/create_profile.html',context)

def user_create_view(request):
    form = UserCreateForm(request.POST or None)
    if request.POST.get('password') != request.POST.get('password1'):
            form.add_error(field=None,error=ValidationError('Password should match.'))
    if form.is_valid():
        
        form.save(commit=False)

        user = form.instance
        user.is_staff = True
        print (form.cleaned_data['password'])
        user.set_password(form.cleaned_data['password'])
        form.save()
        login(request=request,user= user)
        return redirect("account:create_view")

    
    context ={
        'form':form

    }
    return render(request, 'account/create.html',context)

def profile_detail_view(request, *args, **kwargs):
    id = request.user.id
    profile= get_object_or_404(klass=Profile, user_id = id)
    print(profile)
    context = {
        'object' : profile
    }
    return render(request, 'account/detail.html', context= context)



