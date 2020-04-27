"""bae URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from .views import index, blog, post, search, post_by_category, post_by_tags

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('blog/', blog, name='post-list'),
    path('post/<id>/', post, name='post-detail'),
    path('category/<name>/', post_by_category, name = 'post_by_category'),
    path('tags/<name>/', post_by_tags, name = 'post_by_tags'),
    path('search/', search, name='search'),
    path('accounts/', include('accounts.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
