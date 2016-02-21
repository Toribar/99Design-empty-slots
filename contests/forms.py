from django import forms
from contests.models import Contest
from django.utils import timezone
from datetime import timedelta

class ContestForm(forms.ModelForm):

    class Meta:
        model = Contest
        fields = ['name']






