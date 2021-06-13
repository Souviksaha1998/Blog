from django import http
from django.http.response import Http404
from django.shortcuts import redirect, render , HttpResponse
from post import urls 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_new
from django.contrib.auth import logout as logout_new
from post.models import Blog
from django.db.models import Q
from django.contrib import messages

# Create your views here.
def home(request):
    post = Blog.objects.all()
    context = {'post' : post}
    
    return render(request , 'home.html' , context)
def login(request):
    if request.method == "POST":
        username = request.POST['user']
        password= request.POST['pass']
        user = authenticate(request , username=username, password=password)
        if user is not None:
            login_new(request, user)
            messages.success(request, 'Successfully logged in....')
            return redirect('home')
        
        else:
            messages.warning(request, 'please check your password or username..')
            return redirect('login')
    return render(request, 'login.html')
    # return HttpResponse('404- not found')

def sign(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        pass1= request.POST['pass1']
        pass2 = request.POST['pass2']
        if pass1 != pass2:
            messages.warning(request, 'Password doesn"t match...')
            return redirect('signup')
        elif lname =='' or fname=="":
            messages.warning(request, 'Enter your name...')
            return redirect('signup')
        elif len(fname)<3 or len(lname)<3 or len(username)<3:
            messages.warning(request, 'Names are too short...')
            return redirect('signup')
        
        else:
            user = User.objects.create_user(username=username , email=email , password=pass1)
            user.first_name =fname
            user.last_name =lname
            user.save()
            messages.success(request, 'Successfully signed up')
            return redirect('login')
    return render(request, 'signup.html')
def blog(request):
    try:
        if request.user.is_authenticated==True:
            if request.method == 'POST':
                name = request.POST.get('name')
                name2 = request.POST.get('name2')
                desc = request.POST.get('text')
                date = request.POST.get('date')
                new_blog = Blog(name=name , subtitle=name2 , desc=desc , date=date)
                new_blog.save()
                messages.success(request, 'Successfully Post')
                return redirect('home')
        else:
            messages.warning(request, 'Signup to continue...')
            return redirect('signup')
    except:
        return HttpResponse('error go-back')
        
    return render(request , 'blog.html')

def logout_view(request):
    logout_new(request)
    messages.success(request, 'Successfully logged out...')
    return redirect('home')

def query(request):
    if request.method == "GET":
        try:
            query1 = request.GET.get("query")
            if len(query1) > 50:
                messages.warning(request, 'Error, try minimum words')
                return redirect('home')
            else:
                results = Blog.objects.filter(Q(name__icontains=query1) | Q(desc__icontains=query1))
                param = {'results' : results , 'query1' : query1}
        except:
            messages.warning(request, 'Couldn"t find...')
            return redirect('home')
                
            # else:
            #     return HttpResponse('error-cant find')
                
          
    return render(request , 'query.html', param)
    # return HttpResponse('hi')
    
def blogfull(request , posts):
    try:
        blog3 = Blog.objects.filter(id = posts)
        context = {'blog1' : blog3}
        return render( request , 'blogfull.html' , context)
    except:
        return redirect(request , 'signup')
        
    # return render( request , 'blogfull.html' , context)
