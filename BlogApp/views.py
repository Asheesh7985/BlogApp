from django.shortcuts import render,HttpResponseRedirect
from .forms import SignupForm,LoginForm,PostForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required
from .models import Post
from django.contrib.auth.models import Group

# Create your views here.

def HomeView(request):
    post = Post.objects.all()
    return render(request, 'home.html',{'post':post})


def AboutView(request):
    return render(request, 'about.html')

@login_required(login_url='/login/')
def DashboardView(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request, 'dashboard.html',{'posts':posts,'group':gps,'full_name':full_name})
    else:
        return HttpResponseRedirect('/login/')


def SignupView(request):
    if request.method == "POST":
        fm = SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Your Account Created Successfully')
            user = fm.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
    else:
        fm = SignupForm()
    return render(request, 'signup.html',{'form':fm})


def LoginView(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = LoginForm(request = request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/dashboard/')
            else:
                messages.warning(request, 'Please Enter Correct username and Password')
    
        else:
            fm = LoginForm()
        return render(request, 'login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/dashboard/')


@login_required(login_url='/login/')
def Logout(request):
    logout(request)
    return HttpResponseRedirect('/signup/')

def ContactView(request):
    return render(request, 'contact.html')


def AddPostView(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PostForm(request.POST)
            if fm.is_valid():
               title = fm.cleaned_data['title']
               descrption = fm.cleaned_data['descrption']
               pst = Post(title=title, descrption=descrption)
               messages.success(request, 'New Post Create Successfully!!!')
               pst.save()
        else:
            fm = PostForm()
        return render(request, 'addpost.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')

def UpdatePostPage(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            fm = PostForm(request.POST, instance=pi)
            if fm.is_valid():
                messages.success(request, 'Post Updated Successfully!!!')
                fm.save()
        else:
            pi = Post.objects.get(pk=id)
            fm = PostForm(instance=pi)
        return render(request, 'updatepost.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')
    

def DeletePostView(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect('/dashboard/')