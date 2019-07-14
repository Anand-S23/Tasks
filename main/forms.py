from django import forms
from .models import Task, Category

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task 
        fields = ['description', 'category', 'due']
        widgets = {
            'description': forms.TextInput(attrs={"placeholder":"Ex: 'Go to the store'"}),
            'due': forms.DateInput(attrs={'placeholder':'mm/dd/yy'})
        }