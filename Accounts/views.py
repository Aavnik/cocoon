from django.shortcuts import render,redirect, HttpResponse
from .models import *

import uuid
from .threads import *
from django.contrib.auth import authenticate, login , logout
# Create your views here.
def signup(request):
    try:
        if request.method == "POST":
            name = request.POST.get("inputName")
            email = request.POST.get("inputEmail")
            password = request.POST.get("inputPassword")
            if usersignup.objects.filter(email=email).filter():
                return redirect('signup')
            email_tok = str(uuid.uuid4())   
            usersignup_obj = usersignup.objects.create(username=email,
                email= email,
                first_name= name,
                email_token=email_tok
            ) 
            usersignup_obj.set_password(password)
            usersignup_obj.save()
            thread_obj = Send_mail(email, email_tok)
            thread_obj.start()
            return redirect('./verify')
            print("account create")
        
    except Exception as e:
        print(e)     
    

    return render(request ,'accounts/sign-up.html')
def verify(request):
     

    return render(request ,'accounts/verify.html')    
def verifysuccess(request):
     

    return render(request ,'accounts/verfiysucces.html')    
def loginauth(request):
    try:
        if request.method == "POST":
            email = request.POST.get("inputEmail")
            password = request.POST.get("inputPassword")
            try:
                userlogin_obj = usersignup.objects.filter(email=email).first()
                if userlogin_obj is None:
                    return HttpResponse("Please Register First")
                if not userlogin_obj.email_verified:
                    return HttpResponse("Please Register First")
                user=authenticate(username=email, password=password)  
                if user is None:
                    print("user in non")
                    return HttpResponse('Incorrect')
                            
                login(request, user)
                print("user logined")
                try:
                    return redirect('/')
                except Exception as e:
                    print(e)

            except Exception as e:
                print(e)    
         
        
    except Exception as e:
        print(e)     
    
     

    return render(request ,'accounts/sign-in.html')    

def verifyemail(request, email_tok):
    try:
        usersignup_obj = usersignup.objects.get(email_token = email_tok)
        usersignup_obj.email_verified = True
        usersignup_obj.save()
        
        return redirect('/')
    except Exception as e:
        print(e)
    return HttpResponse('Invalid Token')

def logout_attempt(request):
    logout(request)
    return redirect('/')     