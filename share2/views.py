from django.shortcuts import render

# Create your views here.
from os import name
from pickle import FALSE
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
import socket
import requests
import netifaces
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
            data=UserDetails2.objects.filter(email=Email)
            if data:
                msg = 'Email already taken'
                return render(self , 'signup.html',{'msg':msg})

            elif ConfirmPassword == Password:
                v = UserDetails2()
                v.name = Name
                v.email = Email
                v.number = Number
                v.password = Password
                v.save()
                return redirect('LOGIN2')

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
            check = UserDetails2.objects.get(email = em)      
            print("Email is ",em)
            if check.password == pass1:
                request.session['email'] = check.email
                print(f'CA {check.name} Successfully logged in')
                return redirect('DASHBOARD2')
            else:
                return HttpResponse('Invalid Password')
        except:
            print("Inside first except block")
            return HttpResponse('Invalid Email ID')
    return render(request,'login.html')
import os
#ca dashboard
def dashboard(request):
   
    if 'email' in request.session:
        # try:
            nameMsg = UserDetails2.objects.get(email = request.session['email'])
            fi=FileList.objects.filter(uploaded_by=nameMsg.email,recieved_from='')

            if request.POST.get('upload')=='upload':
                multiplefile=request.POST.getlist('file')
                print(multiplefile)

                for i in multiplefile:
                    # ext = os.path.splitext(i)[-1].lower()
                    # print(ext)
                    # i=i.replace('.pdf','')+'123'+ext
                    print(i)
                    b=False 
                    for k in fi:
                        if i==k.files and k.uploaded_by==nameMsg.email:
                            print('inside duplicate')
                            b=True
                            break
                    if b:
                        continue
                    f=FileList()
                    f.uploaded_by=nameMsg.email
                    f.recieved_from=''
                    f.files=i
                    f.save()      
                    print('inside for1')
                # return render(request, 'dashboard.html', {'key':nameMsg,'files':fi})    
                return(HttpResponseRedirect('http://127.0.0.1:8000/share2/dash/'))

            if request.POST.get('send')=='send':
                email = request.POST['reciever_email']
                try:
                    obj=UserDetails2.objects.get(email=email)
                    
                except:
                    return HttpResponse(('wrong email id'))
                
                rfile= request.POST.get('ofile')
                if email==nameMsg.email:
                   return HttpResponse(('you canot send pdf to yourself'))
                else:
                    f=FileList()
                    f.recieved_from=nameMsg.email
                    f.uploaded_by=email
                    f.files=rfile
                    f.save()
                    
                return(HttpResponseRedirect('http://127.0.0.1:8000/share2/dash/'))   

            person=FileList.objects.filter(uploaded_by=nameMsg.email)
            print(person)
            return render(request, 'dashboard.html', {'key':nameMsg,'files':fi,'person':person})
        # except:
        #     return redirect('LOGIN')
        
    # return redirect('LOGIN')

def userLogOut(request):
    del request.session['email']
    print('User logged out')
    return redirect('LOGIN2')


def getip(self):
  ## importing socket module

    ## getting the hostname by socket.gethostname() method
    hostname = socket.gethostname()
    ## getting the IP address using socket.gethostbyname() method
    ip_address = socket.gethostbyname(hostname)
    ## printing the hostname and ip_address
    print(f"Hostname: {hostname}")
    print(f"IP Address: {ip_address}")
    
   

def getip2(self):

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('mysite.com', 80))
    print(s.getsockname()[0])
    a = s.getsockname()[0]
    return HttpResponse(a)
       
def getip1(request):
    """Get the current external IPv6 address or return None if no connection to the IPify service is possible"""
    try:
        print(requests.get("https://api6.ipify.org", timeout=5).text)
        print(requests.get("https://api6.ipify.org", timeout=5).text)
        return HttpResponse(requests.get("https://api6.ipify.org", timeout=5).text)
    except requests.exceptions.ConnectionError as ex:
        print(None)
        return HttpResponse(None)       

def getip(self):

    # print(netifaces.interfaces())
    # addrs = netifaces.ifaddresses('enp8s0')
    # # print(addrs)
    # x = addrs.get(10)
    # # (x[0])
    # global_add = x[0].get('addr')
    # print(global_add)
    # link_local = x[2].get('addr')
    # link_local = link_local.replace("%enp8s0","" )
    # print(link_local)      

    # print(netifaces.interfaces())
    addrs = netifaces.ifaddresses(netifaces.interfaces()[1])
    # print(addrs)
    x = addrs.get(10)
    # # (x[0])
    global_add = x[0].get('addr')
    print(global_add)
    link_local = x[2].get('addr')
    print(link_local)

    i=Ip()
    i.ipaddress= global_add+':'+link_local 
    i.save()    

    return (HttpResponse('your ip address saved')) 