"""patients URL Configuration

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
import imp
from unicodedata import name
from django import views
from django.contrib import admin
from django.urls import path, include
from App import views

urlpatterns = [
    # Path to access the admin
    path('admin/', admin.site.urls),

    # Path to access the frontend
    path('', views.frontend, name="frontend"),

    # --------------------------------------------
    # BACKEND ROUTES
    #---------------------------------------------
    
    # Path for login / logout 
    path('login/', include('django.contrib.auth.urls')),

    # Path to acess the backend
    path('backend/', views.backend, name="backend"),

    # Path to add patient
    path('addpatient', views.addpatient, name="addpatient"),

    # Path to access patient individually
    path('patient/<str:patient_id>', views.patient, name="patient"),

    # Path to edit patient
    path('editpatient', views.editpatient, name="editpatient"),

    # Path to Delete patient
    path('deletepatient/<str:patient_id>', views.deletepatient, name="deletepatient"),
]
