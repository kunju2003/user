
from django.shortcuts import render,redirect
from  django.http import HttpResponse
from django.contrib.auth.models import User,auth

# Create your views here.


def userreg(request):
    if request.method=='POST':
        name=request.POST['name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        data=User.objects.create_user(first_name=name,username=username,email=email,password=password)
        data.save()
        return redirect(userlog)
    return render(request,'user/userreg.html')

def userlog(request):
    if request.method=='POST':
        username=request.POST['username']
        userpassword=request.POST['password']
        user=auth.authenticate(username=username,password=userpassword)
        if user is not None:
            auth.login(request,user)
            return redirect(userhome)
        else:
            return redirect(userlog)
    return render(request,'user/userlog.html')

admname="adm123"
admpassword="adm@123"
def adminlog(request):
    if request.method=='POST':
       username=request.POST['name']
       password=request.POST['password']
       if username==admname and password==admpassword:
           print("logged in")
           request.session['adm']=admname
           return redirect(adminhome)
    return render(request,'admin/adminlog.html')
            
def adminhome(request):
    
    if 'adm' in request.session:
    #   user=User.objects.all()
        user=User.objects.filter(username__startswith="n")
        print(user)
        return render(request,'admin/adminhome.html',{'user':user})
      
    else:
        return redirect(adminlog)

def userhome(request):
    if '_auth_user_id' in request.session:
        user=User.objects.get(pk=request.session['_auth_user_id'])
        return render(request,'user/userhome.html',{'user':user})
    else:
        return redirect(userlog)


def userlogout(request):
    if '_auth_user_id' in request.session:
        auth.logout(request)
        return redirect(userlog)
    else:
        return redirect(userlog)
    
def adminlogout(request):
    if 'adm' in request.session:
        del request.session['adm']
        return redirect(adminlog)
    else:
        return redirect(adminlog)    