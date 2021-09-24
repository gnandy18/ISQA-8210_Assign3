from django import forms
from .models import Request


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request

        fields = ('category_type', 'location_type', 'full_description', 'request_date')