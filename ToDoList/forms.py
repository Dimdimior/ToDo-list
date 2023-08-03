from django import forms
from django.utils import timezone

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "deadline": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        deadline = cleaned_data.get("deadline")
        if deadline:
            task_datetime = timezone.now()
            if task_datetime and deadline < task_datetime:
                raise forms.ValidationError("The deadline can't be in the past")
        return cleaned_data
