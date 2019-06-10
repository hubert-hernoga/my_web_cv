"""CV URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from cv_maker.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$', TitlePage.as_view(), name='title_page'),
    url('cover_letter/', CoverLatter.as_view(), name='cover_latter'),
    url('projects/', Projects.as_view(), name='blog'),
    url('projects/lasante', LaSante.as_view(), name='lasante'),
    url('projects/interdrinks/', InterDrinks.as_view(), name='interdrinks'),
    url('projects/frenchtouch/', FrenchTouch.as_view(), name='frenchtouch'),
    url('projects/project_cv', LaSante.as_view(), name='project_cv'),
    url('projects/project_shop/', InterDrinks.as_view(), name='project_shop'),
    # url('contact/', Contact.as_view(), name='contact'),
    url('portfolio/', Portfolio.as_view(), name='portfolio'),
]
