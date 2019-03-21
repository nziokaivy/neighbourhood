from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Business, Profile, Neighbourhood
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files.storage import FileSystemStorage


# Create your views here.

def home(request):
    current_user = request.user
    businesses = Business.objects.order_by('-pub_date')
    return render(request, 'index.html', {'businesses':businesses})

def profile(request):
    user = request.user    
    business = Business.objects.all().filter(poster_id = user.id)
    return render(request, 'profile.html', {'business':business, "user":user, "current_user":request.user })
