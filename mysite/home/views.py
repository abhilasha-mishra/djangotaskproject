from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import auth
from django.contrib.auth.models import User
from .models import BlogPost,Task,ApplyTask
# Create your views here.

def task_list(request):
    data=Task.objects.all()
    return render(request,'task_list.html',{'data':data})

def task_detail(request,dtid):
    data=Task.objects.filter(id=dtid)
    request.session["dtid"] = dtid
    return render(request,'task_details.html',{'data':data})


def apply(request):
    task=request.session["dtid"]
    if request.method=='POST':
        ans=request.POST.get('ans')
        status='True'
        user_id = User.objects.get(username=request.user)
        ApplyTask.objects.create(ans=ans,status=status,task_id=task,created_user_id=user_id.id)
    return render(request,'apply.html')

def mysiteinfo(request):
    return render(request,'mysiteinfo.html')


def dashbord(request):
    data= BlogPost.objects.filter(created_user_id=request.user)
    count=data.count()
    print(count)
    applydata=ApplyTask.objects.filter(created_user_id=request.user)
    return render(request,'dashbortd.html',{'data':data,'applydata':applydata})

def details(request,sid):
    details = BlogPost.objects.get(pk=sid)
    print(details)
    return render(request,'details.html', {'details':details})


def edit(request,id):
    data=BlogPost.objects.get(id=id)
    if request.method=='POST' and request.POST:
        title = request.POST.get('title')
        hed1 = request.POST.get('hed1')
        hed2 = request.POST.get('hed2')
        hed3 = request.POST.get('hed3')
        p1 = request.POST.get('p1')
        p2 = request.POST.get('p2')
        p3 = request.POST.get('p3')
        image=request.FILES.get('image')
        if title==None:
            title=data.title
        if hed1==None:
            hed1=data.hed1
        if hed2==None:
            hed2=data.hed2
        if hed3==None:
            hed3=data.hed3
        if p1==None:
            p1=data.p1
        if p2==None:
            p2=data.p2
        if p3==None:
            p3=data.p3
        if image==None:
            image=data.image
        data.title = title
        data.hed1 = hed1
        data.hed2 = hed2
        data.hed3 = hed3
        data.p1 = p1
        data.p2 =p2
        data.p3 = p3
        data.image = image
        data.save()
    return render(request,'edit_post.html',{'data':data})

def delete(request,did):
    data=BlogPost.objects.get(id=did)
    data.delete()
    return redirect('home:dashbord')


def home(request):
    post = BlogPost.objects.all()
    print(post)
    return render(request,'index.html', {'post':post})

def blogpost(request ,id):
    post=BlogPost.objects.filter(id=id)
    print(post)
    return render(request,'blogpost.html',{'post':post})

# title,hed1,p1,hed2,p2,hed3,p3,image
def create_blog(request):
    if request.method=='POST' and request.FILES:
        title=request.POST.get('title')
        hed1=request.POST.get('hed1')
        hed2=request.POST.get('hed2')
        hed3 = request.POST.get('hed3')
        p1=request.POST.get('p1')
        p2=request.POST.get('p2')
        p3 = request.POST.get('p3')
        image = request.FILES.get('image')
        user_id = User.objects.get(username=request.user)
        BlogPost.objects.create(title=title,hed1=hed1,hed2=hed2,hed3=hed3,p1=p1,p2=p2,p3=p3,image=image,created_user_id=user_id.id)
        return redirect('home:blogpage')
    else:
        return render(request,'create_blog.html')


def Register(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        x=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
        x.save()
        return redirect('home:home')
    else:
        return render(request,'index.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home:home')
        else:
            return redirect('home:home')
    else:
        return render(request, 'home.html')

def UserLogout(request):
    logout(request)
    return redirect('home:home')

def blogpage(request):
    bpost = BlogPost.objects.filter(created_user_id=request.user)
    print(bpost)
    return render(request,'blog.html',{'bpost':bpost})