from django.shortcuts import render,HttpResponse

# Create your views here.
def vlogin(request):
    # return HttpResponse ("login")
    return render (request,'login.html')
def vsignup(request):
    # return HttpResponse ("signup")
    return render (request,'signup.html')


def vhome(request):
    # return HttpResponse ("home page")
    return render (request,'home.html')


def vuserdata(request):
    # return HttpResponse ("home page")
    return render (request,'userdata.html')
def vuserdata_form(request):
    # return HttpResponse ("home page")
    return render (request,'userdata_form.html')

def vhrdata(request):
    # return HttpResponse ("home page")
    return render (request,'hrdata.html')
def vhrdata_form(request):
    # return HttpResponse ("home page")
    return render (request,'hrdata_form.html')

def vaccounts(request):
    # return HttpResponse ("home page")
    return render (request,'accounts.html')
def vaccounts_form(request):
    # return HttpResponse ("home page")
    return render (request,'accounts_form.html')

