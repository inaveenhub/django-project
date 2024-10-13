"""Wisefox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/

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
import debug_toolbar

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from core.sitemaps import *
from core.helpers import urlpatterns as urls

# ----------------------------------------------------------
 

urlpatterns = [
    path( "robots.txt", TemplateView.as_view(template_name="misc/robots.txt", content_type="text/plain"), ),
    path( "webmanifest.json", TemplateView.as_view(template_name="misc/webmanifest.json", content_type="application/json"), name = 'webmanifest_url' ),

    path( 'about/', TemplateView.as_view(template_name="pages/about.html"), name = 'about_url' ),
    path( 'contact/', TemplateView.as_view(template_name="pages/contact.html"), name = 'contact_url' ),
    path( 'privacy-policy/', TemplateView.as_view(template_name="pages/privacy.html"), name = 'privacy_url' ),
    path( 'terms/', TemplateView.as_view(template_name="pages/terms.html"), name = 'terms_url' ),

    path( 'dj/', admin.site.urls ),
    path( 'debug/', include(debug_toolbar.urls) ),

    path( '', include('core.urls') ),
    path( '', include('auth_user.urls') ),

    path( 'trix-editor/', include('trix_editor.urls')),

] + urls

if settings.DEBUG:
    urlpatterns += static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )
