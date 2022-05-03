import imp
from django.contrib import admin
from App.models import Patient

# Register your models here. 
'''
    The model under models.py is registered here and the search technique is applied here.
'''

class PatientAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'age', 'gender', 'created_at']
    search_fields = ['name', 'phone', 'email', 'gender']
    list_filter = ['gender']
    list_per_page = 10

admin.site.register(Patient, PatientAdmin)

