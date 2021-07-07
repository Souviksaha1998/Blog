from django import http
from django.http.response import HttpResponse 
from django.shortcuts import render , redirect
from django.http import HttpResponse
import random
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage

# Create your views here.

r1 = random.randint(164772 , 975643)
def home(request): 
    if request.method =="POST":
        email = request.POST.get("email")
        print(email)
        subject = 'Your otp verification'
        message = f'your otp number is : {r1}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(
        subject,
        message,
        email_from,
        recipient_list , 
        fail_silently=False,)         
        return redirect('otp')
    


    return render(request , 'email.html')

def otp(request):
    if request.method == "POST":
        otp = request.POST.get("otp")
        print(otp)
        print(r1)
        if int(otp) == int(r1):
            return redirect('home')
        else:
            return HttpResponse('bad otp')

        
        
    return render(request , 'otp.html')
