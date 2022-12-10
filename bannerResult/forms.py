from django import forms
from . import models


class ResultForm(forms.ModelForm):
    class Meta:
        model = models.Result
        fields = [
            "image",
        ]
