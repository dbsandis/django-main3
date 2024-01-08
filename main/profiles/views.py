from django.shortcuts import render
from .forms import ResidentForm, StaffForm
from .models import Resident, Staff

def profiles_list(request):
    residents = Resident.objects.all()
    staff = Staff.objects.all()
    return render(request, 'profiles_list.html', {'residents': residents, 'staff': staff})

def add_resident(request):
    if request.method == 'POST':
        form = ResidentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ResidentForm()
    return render(request, 'add_resident.html', {'form': form})

def add_staff(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StaffForm()
    return render(request, 'add_staff.html', {'form': form})


# add other views here