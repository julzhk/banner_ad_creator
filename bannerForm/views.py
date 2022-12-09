from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class bannerAdListView(generic.ListView):
    model = models.bannerAd
    form_class = forms.bannerAdForm


class bannerAdCreateView(generic.CreateView):
    model = models.bannerAd
    form_class = forms.bannerAdForm


class bannerAdDetailView(generic.DetailView):
    model = models.bannerAd
    form_class = forms.bannerAdForm


class bannerAdUpdateView(generic.UpdateView):
    model = models.bannerAd
    form_class = forms.bannerAdForm
    pk_url_kwarg = "pk"


class bannerAdDeleteView(generic.DeleteView):
    model = models.bannerAd
    success_url = reverse_lazy("bannerForm_bannerAd_list")


class EmotionListView(generic.ListView):
    model = models.Emotion
    form_class = forms.EmotionForm


class EmotionCreateView(generic.CreateView):
    model = models.Emotion
    form_class = forms.EmotionForm


class EmotionDetailView(generic.DetailView):
    model = models.Emotion
    form_class = forms.EmotionForm
    slug_url_kwarg = "slug"


class EmotionUpdateView(generic.UpdateView):
    model = models.Emotion
    form_class = forms.EmotionForm
    slug_url_kwarg = "slug"


class EmotionDeleteView(generic.DeleteView):
    model = models.Emotion
    success_url = reverse_lazy("bannerForm_Emotion_list")
