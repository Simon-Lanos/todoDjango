from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    content = forms.CharField(max_length=100, help_text = "Renseignez un intitulé")

    class Meta:
        model = Task
        fields = ('content',)