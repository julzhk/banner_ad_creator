from django import forms
from bannerForm.models import Emotion
from . import models


class bannerAdForm(forms.ModelForm):
    class Meta:
        model = models.bannerAd
        fields = [
            "websiteURL",
            "size",
            "emotion",
        ]

    def __init__(self, *args, **kwargs):
        super(bannerAdForm, self).__init__(*args, **kwargs)
        self.fields["emotion"].queryset = Emotion.objects.all()



class EmotionForm(forms.ModelForm):
    class Meta:
        model = models.Emotion
        fields = [
            "Name",
            "slug",
        ]
