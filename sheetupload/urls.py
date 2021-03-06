"""sheetupload URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from projectapp import views
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indexPage, name='index'),
    path('contact/', views.contactPage, name='contact'),
    path('uploadfile/', views.uploadfile, name='uploadfile'),
    path('reviewfiles/', views.reviewfiles, name='reviewfiles'),
    path('alldata/', views.alldata, name='alldata'),
    path('profile/<int:id>/', views.profilePage, name='profile'),
    path('allprofiles/', views.allprofiles, name='allprofiles'),
    path('edit/<int:id>/', views.EditView.as_view(), name='edit'),
    path('delete/<int:id>/', views.DeleteView.as_view(), name='delete'),
    path('login/', views.handleLogin, name='handleLogin'),
    path('logout/', views.handleLogout, name='handleLogout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
