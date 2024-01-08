from django import forms
from .models import Resident, Staff

class ResidentForm(forms.ModelForm):
    class Meta:
        model = Resident
        fields = '__all__'

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'

# add other forms here