from os import name
from pickle import FALSE
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.

def SignupView(self):
    if self.POST:
        Name = self.POST['name']
        print(Name)
        Email = self.POST['email']
        print(Email)
        Number = self.POST['number']
        print(Number)
        Password = self.POST['password']
        print(Password)
        ConfirmPassword = self.POST['confirmPassword']
        print(ConfirmPassword)

        try:
            data=UserDetails.objects.filter(email=Email)
            if data:
                msg = 'Email already taken'
                return render(self , 'signup.html',{'msg':msg})

            elif ConfirmPassword == Password:
                v = UserDetails()
                v.name = Name
                v.email = Email
                v.number = Number
                v.password = Password
                v.save()
                return redirect('LOGIN')

            else:
                msg = 'Enter Same Password'
                return render(self , 'signup.html',{'msg':msg}) 
                
        finally:
            messages.success(self, 'Signup Successfully Done...')

    return render(self,'signup.html')
# ca login
def userLogin(request):
    if request.POST:
        em = request.POST.get('email')
        pass1 = request.POST.get('password')
        try:
            print("Inside first try block", em)
            check = UserDetails.objects.filter(email = em)
            check1=check[0]        
            print("Email is ",em)
            if check1.password == pass1:
                request.session['email'] = check1.email
                print(f'CA {check1.name} Successfully logged in')
                return redirect('DASHBOARD')
            else:
                return HttpResponse('Invalid Password')
        except:
            print("Inside first except block")
            return HttpResponse('Invalid Email ID')
    return render(request,'login.html')

#ca dashboard
def dashboard(request):
   
    if 'email' in request.session:
        # try:
            nameMsg = UserDetails.objects.filter(email = request.session['email'])
            nameMsg1=nameMsg[0]
            if request.POST.get('upload')=='upload':
                multiplefile=request.POST.getlist('file')
                print(multiplefile)
                k=0
                b=False
                for i in multiplefile: 
                    for k in nameMsg:
                        if i==k.file:
                            b=True
                            break
                    if b:
                        continue
                    print(type(i))
                    u=UserDetails()
                    u.file=i
                    u.name=nameMsg1.name
                    u.email=nameMsg1.email
                    u.number=nameMsg1.number
                    u.password=nameMsg1.password
                    u.save()
                    print('inside for1')
                return(HttpResponseRedirect('http://127.0.0.1:8000/share/dash/'))

            if request.POST.get('send')=='send':

                email = request.POST['reciever_email']
                rfile= request.POST.get('ofile')
                
                try:
                    obj=UserDetails.objects.filter(email=email)
                    obj1=obj[0]
                except:
                    return HttpResponse(('wrong email id'))
                v=UserDetails()

                v.name=obj1.name
                v.email=obj1.email
                v.password=obj1.password
                v.number=obj1.number
                v.received_From=nameMsg1.name
                v.recieved_file=rfile
                v.save()
                print('123456')
                return(HttpResponseRedirect('http://127.0.0.1:8000/share/dash/'))
                    
            return render(request, 'dashboard.html', {'key':nameMsg1,'files':nameMsg})
        # except:
        #     return redirect('LOGIN')
        
    # return redirect('LOGIN')

def userLogOut(request):
    del request.session['email']
    print('User logged out')
    return redirect('LOGIN')

  