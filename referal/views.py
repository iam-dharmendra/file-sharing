from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from referal.models import Profile

# Create your views here.

def hello(self):
    return render(self,'base.html')


def my_reccomendation(self):
    print('---------------------')
    profile=Profile.objects.get(user=self.user)
    print(profile)
    my_recs=profile.get_recommend_profiles()
    print(my_recs)
    context={'my_recs':my_recs}
    return render(self,'main1.html',context)

def any_recommendations_view(request,*args,**kwargs):
    code = str(kwargs.get('ref_code'))
    profile = Profile.objects.get(code = code)
    request.session['ref_profile'] = profile.id
    print('id',profile.id)
    # profile = Profile.objects.get(user=request.user)
    my_recs =  profile.get_recommend_profiles()
    context = {'my_recs':my_recs}
    return render(request, 'main1.html',context)

def all(self):
    a=User.objects.all()
    l=[]
    l2=[]
    for i in a:
        b=Profile.objects.filter(recomend_by=i.id)
        # print(i.user,end='------------')
        l.append(i.username)      
        l2.append(b)
        
    
    
    return render(self,'new.html',{'l':l,'l1':l2})
    # for i in l:
    #     print(i,end='  --- ')
    #     for j in l1:
    #         for k in j:
    #             print('ref=',k)

            