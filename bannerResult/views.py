import asyncio
import os

import html_text
import nest_asyncio
import openai
from asgiref.sync import sync_to_async
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from requests_html import AsyncHTMLSession

from bannerForm.models import bannerAd
from . import forms, models
from .models import Result


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


async def get_url_page_contents(url):
    session = AsyncHTMLSession()
    r = await session.get(url, verify=False, timeout=10)
    r.html.arender()
    if maindiv := r.html.find('main'):
        html_txt = maindiv[0].html
    else:
        html_txt = r.html.html
    webpage_content = html_text.extract_text(html_txt)
    await session.close()
    return webpage_content


def get_slogan(msg):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f'turn this into a slogan: {msg}',
        temperature=0.7,
        max_tokens=64,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    cleanedtxt = [clean_up(r.text) for r in response.choices]
    return cleanedtxt[0]


def clean_up(txt):
    for dingbat in ['"', "'", '\n', '\r', '\t']:
        txt = txt.replace(dingbat, '')
    return txt


def generate_image(slogan: str):
    pass


async def process_submission(request):
    url = request.POST.get("url", '')
    new_loop = asyncio.new_event_loop()
    if asyncio.get_event_loop().is_running():
        nest_asyncio.apply()
    asyncio.set_event_loop(new_loop)
    webpage_content = new_loop.run_until_complete(get_url_page_contents(url=url))
    banner = await sync_to_async(bannerAd.objects.create, thread_sensitive=True)(websiteURL=url, webpage_raw_content=webpage_content)
    result = await sync_to_async(Result.objects.create, thread_sensitive=True)(banner=banner)
    slogan = get_slogan(webpage_content)
    await sync_to_async(Result.generate, thread_sensitive=True)(result, slogan=slogan)
    return render(request,
                  context={'slogan': slogan,
                           'banner': banner,
                           'result': result},
                  template_name="bannerResult/process_submission.html")
