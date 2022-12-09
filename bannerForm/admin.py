from django.contrib import admin
from django import forms

from . import models


class bannerAdAdminForm(forms.ModelForm):

    class Meta:
        model = models.bannerAd
        fields = "__all__"


class bannerAdAdmin(admin.ModelAdmin):
    form = bannerAdAdminForm
    list_display = [
        "websiteURL",
        "created",
        "last_updated",
        "size",
    ]
    readonly_fields = [
        "websiteURL",
        "created",
        "last_updated",
        "size",
    ]


class EmotionAdminForm(forms.ModelForm):

    class Meta:
        model = models.Emotion
        fields = "__all__"


class EmotionAdmin(admin.ModelAdmin):
    form = EmotionAdminForm
    list_display = [
        "Name",
        "last_updated",
        "created",
        "slug",
    ]
    readonly_fields = [
        "Name",
        "last_updated",
        "created",
        "slug",
    ]


admin.site.register(models.bannerAd, bannerAdAdmin)
admin.site.register(models.Emotion, EmotionAdmin)
