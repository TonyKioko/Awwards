from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.

# @login_required(login_url='/accounts/login/')
def index(request):

    message = "Hello World"

    # context ={"images":images,"comments":comments,"profiles":profiles}

    return render(request,'index.html',{"message":message})
