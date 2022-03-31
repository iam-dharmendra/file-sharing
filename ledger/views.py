from asyncio import events
from xmlrpc.client import Server
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
# from grpc import server
import requests 
import  json
import xml.etree.ElementTree as ET
import asyncio
from websockets import connect
from websockets import serve
from django.contrib import messages
import websockets 
import os

import json
# import redis

from websocket import create_connection

from .models import *
# # ==============================
# from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseServerError
# from django.views.decorators.csrf import csrf_exempt
# from django.contrib.sessions.models import Session
# from django.contrib.auth.decorators import login_required
# ===================================
# Create your views here.

def my(self):
    

  
    # postlegder = requests.get('http://127.0.0.1:8000/postlegder/')
    # datas=postlegder.json()
    # data = ' <ENVELOPE><HEADER><VERSION>1</VERSION><REQVERSION>1</REQVERSION><TALLYREQUEST>Export</TALLYREQUEST><TYPE>DATA</TYPE><ID>List Of Companies</ID></HEADER><BODY><DESC><STATICVARIABLES><SVINCLUDE>Connected</SVINCLUDE></STATICVARIABLES></DESC></BODY></ENVELOPE> '
    data = '<ENVELOPE><HEADER><VERSION>1</VERSION><TALLYREQUEST>EXPORT</TALLYREQUEST><TYPE>COLLECTION</TYPE>'
    data += '<ID>ListOfCompanies</ID></HEADER><BODY><DESC><STATICVARIABLES><SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>'
    data += '</STATICVARIABLES><TDL><TDLMESSAGE><COLLECTION Name="ListOfCompanies"><TYPE>Company</TYPE>'
    data += '<FETCH>Name,CompanyNumber</FETCH></COLLECTION></TDLMESSAGE></TDL></DESC></BODY></ENVELOPE>'
    IPAddr='192.168.29.102'
    url='http://'+IPAddr+':'+'9000'
    request1=requests.post(url=url,data=data)
    response1=request1.text.strip().replace("&amp;","and")
    responseXML1 = ET.fromstring(response1)
    # print(response1)


    for data in responseXML1.findall('./BODY/DATA/COLLECTION/COMPANY'):
        getdata=(data.get('NAME'))
        data1=getdata
        print("======================================================",data1,'===============================================')
        url='http://'+IPAddr+':'+'9000'
        data='<ENVELOPE><HEADER><VERSION>1</VERSION><TALLYREQUEST>EXPORT</TALLYREQUEST><TYPE>COLLECTION</TYPE><ID>List of Ledgers</ID>'
        data+='</HEADER><BODY><DESC><STATICVARIABLES><SVCurrentCompany>'+data1+'</SVCurrentCompany><SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT></STATICVARIABLES></DESC></BODY></ENVELOPE>'
        request=requests.post(url=url,data=data)
        response=request.text.strip().replace("&amp;","and")
        responseXML = ET.fromstring(response)
        # print(response)
        d2 = []


        
        for j in responseXML.findall('./BODY/DATA/COLLECTION/LEDGER'):
            get = (j.get('NAME'))
            d1 = get
            # print(d1)
            
            d2.append(d1)
        main_dict = {data1 : d2}
    


        for i,j in main_dict.items():
            for k in range(0,len(j)):
                try:
                    obj1=my_company.objects.get(comp=i)
                    obj=my_ledger.objects.get(company_name=obj1,ledger_list=j[k],lcreated_by=obj1.created_by)
                    if obj:
                        pass
                except:
                    obj1=my_company.objects.get(comp=i)
                    m=my_ledger()
                    m.lcreated_by=obj1.created_by
                    m.company_name=obj1
                    # m.comp=i
                    m.ledger_list=j[k]
                    m.save()
                
            
        # print(main_dict)


    return HttpResponse(d2)
        


async def hello(uri):
    async with connect(uri) as websocket:
        await websocket.send("Hello world!")
        await websocket.recv()

async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)


def lSignup(self):
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
            data=lUser.objects.filter(email=Email)
            if data:
                msg = 'Email already taken'
                return render(self , 'signup.html',{'msg':msg})

            elif ConfirmPassword == Password:
                v = lUser()
                v.name = Name
                v.email = Email
                v.number = Number
                v.password = Password
                v.save()
                return redirect('llogin')

            else:
                msg = 'Enter Same Password'
                return render(self , 'signup.html',{'msg':msg}) 
                
        finally:
            messages.success(self, 'Signup Successfully Done...')

    return render(self,'signup.html')
# ca login
def llogin(request):
    if request.POST:
        em = request.POST.get('email')
        pass1 = request.POST.get('password')
        try:
            print("Inside first try block", em)
            check = lUser.objects.get(email = em)      
            print("Email is ",em)
            if check.password == pass1:
                request.session['email'] = check.email
                print(f'CA {check.name} Successfully logged in')
                return redirect('web')
            else:
                return HttpResponse('Invalid Password')
        except:
            print("Inside first except block")
            return HttpResponse('Invalid Email ID')
    return render(request,'login.html')

def llogout(request):
    
        del request.session['email']
        print('User logged out')
        # ws = create_connection("ws://localhost:8000/ws/some_url/")
        # ws.close()
        return redirect('llogin')



def web(self):

    # # Copy the web brower header and input as a dictionary
    # headers = json.dumps({
    #     'Accept-Encoding': 'gzip, deflate, br',
    #     'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    #     'Cache-Control': 'no-cache',
    #     'Connection': 'Upgrade',
    #     'Pragma': 'no-cache',
    #     'Upgrade': 'websocket',
    #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    # })
    # # Launch the connection to the server.
    # ws = create_connection('ws://localhost:8000/ws/some_url/',headers=headers)
    # # # Perform the handshake.
    # # ws.send(json.dumps({"action": "SubAdd", "subs": ["11~BTC", "21~BTC", "5~CCCAGG~BTC~USD", "11~ETH", "21~ETH", "5~CCCAGG~ETH~USD", "11~BCH", "21~BCH", "5~CCCAGG~BCH~USD",
    # #                     "11~EOS", "21~EOS", "5~CCCAGG~EOS~USD", "11~XRP", "21~XRP","5~CCCAGG~XRP~USD", "11~LTC", "21~LTC", "5~CCCAGG~LTC~USD",
    # #                     "11~ETC", "21~ETC", "5~CCCAGG~ETC~USD", "11~BSV", "21~BSV", "5~CCCAGG~BSV~USD", "11~LINK", "21~LINK", "5~CCCAGG~LINK~USD", "11~ATOM", "21~ATOM", "5~CCCAGG~ATOM~USD"]}))
    # # # Printing all the result
    # while True:
    #     try:
    #         result = ws.recv()
    #         print(result)
    #     except Exception as e:
    #         print(e)
    #         break

    # # async def listen():
    # #     async with websockets.connect('ws://localhost:8000/ws/some_url/') as ws:
    # #         while True:
    # #             msg=await ws.recv()
    # #             print("my message is",msg)

    # # asyncio.get_event_loop().run_until_complete(listen())


    return render(self,'index.html',context = {'text' : 'result'})






# @login_required
# def home(request):
#     comments = Comments.objects.select_related().all()[0:100]
#     return render(request, 'indexcopy.html', locals())

# @csrf_exempt
# def node_api(request):
#     try:
#         #Get User from sessionid
#         session = Session.objects.get(session_key=request.POST.get('sessionid'))
#         user_id = session.get_decoded().get('_auth_user_id')
#         user = lUser.objects.get(id=user_id)

#         #Create comment
#         Comments.objects.create(user=user, text=request.POST.get('comment'))
        
#         #Once comment has been created post it to the chat channel
#         r = redis.StrictRedis(host='localhost', port=6379, db=0)
#         r.publish('chat', user.username + ': ' + request.POST.get('comment'))
        
#         return HttpResponse("Everything worked :)")
#     except Exception as  e:
#         return HttpResponseServerError(str(e))