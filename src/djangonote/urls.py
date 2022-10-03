"""djangonote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, path
from kunden import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.list_kunde, name='list_kunde'),
    path('kundelist/',views.list_kunde, name='list_kunde'),
    path('add_kunde/', views.add_kunde, name='add_kunde'),
    path('update_kundenlists/<str:pk>/', views.update_kundenlists, name="update_kundenlists"),
    path('delete_kunde/<str:pk>/', views.delete_kunde, name="delete_kunde"),
    path('add_notiz/', views.add_notiz, name="add_notiz"),
    path('gespreachsverlauf/',views.gespreachsverlauf, name='gespreachsverlauf'),
    path('delete_verlauf/<str:pk>/', views.delete_verlauf, name="delete_verlauf"),
    path('show_comments/<str:pk>/', views.show_comments, name="show_comments"),


    path('accounts/', include('registration.backends.default.urls')),

]
