from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class ResultListView(generic.ListView):
    model = models.Result
    form_class = forms.ResultForm


class ResultCreateView(generic.CreateView):
    model = models.Result
    form_class = forms.ResultForm


class ResultDetailView(generic.DetailView):
    model = models.Result
    form_class = forms.ResultForm


class ResultUpdateView(generic.UpdateView):
    model = models.Result
    form_class = forms.ResultForm
    pk_url_kwarg = "pk"


class ResultDeleteView(generic.DeleteView):
    model = models.Result
    success_url = reverse_lazy("bannerResult_Result_list")
