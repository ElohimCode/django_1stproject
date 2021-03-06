from django.shortcuts import render
from django.contrib.auth.decorators import login_required # To secure the backend
from django.views.decorators.cache import cache_control # To clear the login registry after user logout

# My imports
from App.models import Patient # Import the class patient from app.models
from django.contrib import messages # import the messages from contrib
from django.http import HttpResponseRedirect # To redirect the webpages
from django.db.models import Q # This allows us to query the db
from django.core.paginator import Paginator # To paginate the items

# Function to render the frontend
def frontend(request):
    return render(request, 'frontend.html')

# ---------------------------------------------------
# BACKEND FUNCTIONS
# ---------------------------------------------------
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def backend(request):
    
    if 'q' in request.GET:
        q = request.GET['q']
        all_patients_list = Patient.objects.filter(
            Q(name__icontains=q) | Q(phone__icontains=q) | Q(email__icontains=q) | Q(age__icontains=q) | Q(gender__icontains=q) | Q(note__icontains=q)
        ).order_by('-created_at')

    else:
        all_patients_list = Patient.objects.all().order_by('-created_at')

    # To call the paginator and send it to the backend page 
    paginator = Paginator(all_patients_list, 10)
    page = request.GET.get('page')
    all_patients = paginator.get_page(page)

    return render(request, "backend.html", {"patients":all_patients})

# Function to render page for add patient
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def addpatient(request):
    if request.method == "POST":
        if request.POST.get('name') and request.POST.get('phone') and request.POST.get('email') and request.POST.get('age') and request.POST.get('gender') or request.POST.get('note'):
            patient = Patient()
            patient.name = request.POST.get('name')
            patient.phone = request.POST.get('phone')
            patient.email = request.POST.get('email')
            patient.age = request.POST.get('age')
            patient.gender = request.POST.get('gender')
            patient.note = request.POST.get('note')
            patient.save()
            # Message to show successful patient added
            messages.success(request, "Patient added successfully")
            return HttpResponseRedirect('/backend')
    
    else:
        return render(request, 'add.html')


# Function to render access patient individually
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def patient(request, patient_id):
    patient = Patient.objects.get(id = patient_id)
    # check if patient is not none 
    if patient != None:
        return render(request, "edit.html", {'patient':patient})

# Function to render edit page for patient individually
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def editpatient(request):
    if request.method == "POST":
        patient = Patient.objects.get(id = request.POST.get('id'))
        if patient != None:
            patient.name =request.POST.get('name')
            patient.phone =request.POST.get('phone')
            patient.email =request.POST.get('email')
            patient.age =request.POST.get('age')
            patient.gender =request.POST.get('gender')
            patient.note =request.POST.get('note')
            patient.save()

            messages.success(request, "Patient info updated successfully!")
            return HttpResponseRedirect('/backend')

# Function to delete the patient
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def deletepatient(request, patient_id):
    patient = Patient.objects.get(id = patient_id)
    patient.delete()

    messages.success(request, "Patient removed successfully!")
    return HttpResponseRedirect('/backend')