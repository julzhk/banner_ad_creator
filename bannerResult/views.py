import asyncio
import math
import os
import textwrap

import cairo
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


class BannerSvg:
    WIDTH, HEIGHT = 512, 512

    def __init__(self):
        self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.WIDTH, self.HEIGHT)
        self.ctx = cairo.Context(self.surface)
        self.ctx.scale(self.WIDTH, self.HEIGHT)  # Normalizing the canvas

    def add_gradient(self):
        pat = cairo.LinearGradient(0.0, 0.0, 0.0, 1.0)
        pat.add_color_stop_rgba(1, 0.7, 0, 0, 0.5)  # First stop, 50% opacity
        pat.add_color_stop_rgba(0, 0.9, 0.7, 0.2, 1)  # Last stop, 100% opacity
        self.ctx.rectangle(0, 0, 1, 1)  # Rectangle(x0, y0, x1, y1)
        self.ctx.set_source(pat)
        self.ctx.fill()

    def vector(self):
        self.ctx.translate(0.1, 0.1)  # Changing the current transformation matrix
        self.ctx.move_to(0, 0)
        self.ctx.arc(0.2, 0.1, 0.1, -math.pi / 2, 0)
        self.ctx.line_to(0.5, 0.1)  # Line to (x,y)
        self.ctx.curve_to(0.5, 0.2, 0.5, 0.4, 0.2, 0.8)
        self.ctx.close_path()
        self.ctx.set_source_rgb(0.3, 0.2, 0.5)  # Solid color
        self.ctx.set_line_width(0.02)
        self.ctx.stroke()

    def write_text(self,
                   text="1Hello2Hello3Hello",
                   red=0.6, green=0.1, blue=0.1,
                   size=0.1,
                   x=0.075, y=0.75):
        self.ctx.select_font_face("Sans",
                                  cairo.FONT_SLANT_NORMAL,
                                  cairo.FONT_WEIGHT_BOLD)
        self.ctx.set_font_size(size)
        self.ctx.move_to(x, y)
        self.ctx.set_source_rgb(red, green, blue)
        self.ctx.show_text(text)

    def output(self, fn="example.png"):
        self.surface.write_to_png(fn)  # Output to PNG

    def add_background_img(self, fn='sample.png'):
        self.surface = cairo.ImageSurface.create_from_png(fn)
        self.ctx = cairo.Context(self.surface)
        self.ctx.scale(self.WIDTH, self.HEIGHT)


async def process_submission(request):
    # result = await sync_to_async(Result.objects.last, thread_sensitive=True)()
    # banner = await sync_to_async(bannerAd.objects.last, thread_sensitive=True)()
    # return render(request,
    #               context={'slogan': 'test slogan',
    #                        'banner': banner,
    #                        'result': result},
    #               template_name="bannerResult/process_submission.html")

    url = request.POST.get("url", '')
    slogan = get_slogan(banner.webpage_raw_content)
    webpage_content = await get_website_contents(url)
    banner, result = await write_data(result, url, webpage_content)
    await write_slogan(result.image_full_path, slogan)


    return render(request,
                  context={'slogan': slogan,
                           'banner': banner,
                           'result': result},
                  template_name="bannerResult/process_submission.html")


async def write_data(result, url, webpage_content):
    banner = await sync_to_async(bannerAd.objects.create, thread_sensitive=True)(websiteURL=url, webpage_raw_content=webpage_content)
    result = await sync_to_async(Result.objects.create, thread_sensitive=True)(banner=banner)
    return banner, result


async def get_website_contents(url):
    new_loop = asyncio.new_event_loop()
    if asyncio.get_event_loop().is_running():
        nest_asyncio.apply()
    asyncio.set_event_loop(new_loop)
    webpage_content = new_loop.run_until_complete(get_url_page_contents(url=url))
    return webpage_content


async def write_slogan_to_results(result, slogan, webpage_content):
    slogan = get_slogan(webpage_content)
    await sync_to_async(Result.generate, thread_sensitive=True)(result, slogan=slogan)
    return slogan


async def write_slogan(image_full_path: str, slogan: str):
    c = BannerSvg()
    c.add_background_img(fn=image_full_path)
    MAX_LINELENGTH = 25
    SLOGAN_Y_START = 0.5  # the middle of the image, vertically
    SLOGAN_Y_END = 0.95  # the end of the image, with a little padding
    slogan_lines = textwrap.wrap(slogan, MAX_LINELENGTH, break_long_words=False)
    no_of_lines = len(slogan_lines)
    line_height = 0.07
    for i, line in enumerate(slogan_lines):
        c.write_text(text=line,
                     y=SLOGAN_Y_START + i * line_height,
                     size=line_height)
    c.output(fn=image_full_path)
