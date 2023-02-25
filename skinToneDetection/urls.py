"""skinToneDetection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls import include, url
from django.urls import include, re_path
from webApp import views
from django.conf.urls import include

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^uploadImg/', views.uploadImg, name='upload'),
    re_path(r'^webCam/', views.webcam, name='webCam'),
    re_path(r'^skinToneProcess/', views.skinToneProcessing, name='skinTone'),
    re_path(r'^webApp/', include('webApp.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^logout/$', views.user_logout, name='logout'),
    re_path(r'^dummyCard/', views.dmyCrd, name="card"),
    re_path(r'^delAll/', views.deleteAll, name="delete"),
    re_path(r'content/', views.content, name='content')
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)