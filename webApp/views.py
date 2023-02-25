from django.shortcuts import render
from webApp.forms import ImageForm
from django.http import HttpResponseRedirect
from .models import ImageModel
from webApp.forms import UserForm
from webApp import skin_tone_2


from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import base64
from PIL import Image
from io import BytesIO



import os


# Create your views here.

def deleteImg():
    count = ImageModel.objects.all().count()

    if(count > 2):
        imgs = ImageModel.objects.last()
        imgs.delete()

def index(request):
    return render(request, "webApp/index.html")

def uploadImg(request):
    form = ImageForm()

    if request.method == 'POST':
        deleteImg()
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect("/uploadImg/")
        else:
            print("Error")
    
    image = ImageModel.objects.last()

    return render(request, "webApp/uploadImage.html", {
        'form': form,
        'image': image, 
        'skinT': image.tone
        })



def deleteAll(request):
    count = ImageModel.objects.all().count()

    if(count > 2):
        imgs = ImageModel.objects.last()
        imgs.delete()
    return HttpResponseRedirect(reverse('upload'))




@login_required
def content(request):
    return render(request, 'webApp/content.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request, 'webApp/register.html', {'user_form': user_form, 'registered': registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('ACCOUNT NOT  ACTIVE')

        else:
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("INVALID LOGIN DETAILS SUPPLIED")
    
    else:
        return render(request, 'webApp/login.html', {})


def skinToneProcessing(request):
    obj = ImageModel.objects.last()
    name = obj.name
    output = skin_tone_2.skinToneProcess()
    ImageModel.objects.filter(name=name).update(tone=output)
    return render(request, 'webApp/output.html', {"imgf": obj.cover, 'skinT': obj.tone})


	

def webcam(request):
    return render(request, 'webApp/webcam.html')


def dmyCrd(request):
    return render(request, 'webApp/card.html')
        
    