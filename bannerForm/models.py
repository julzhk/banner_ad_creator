from django.db import models
from django.urls import reverse
from django.utils.text import slugify

import bannerResult
import asyncio
from pyppeteer import launch
from requests_html import HTMLSession


async def get_webpage_content():
    # launch chromium browser in the background
    browser = await launch({'headless': True, 'args': ['--no-sandbox']})
    # open a new tab in the browser
    page = await browser.newPage()
    # add URL to a new page and then open it
    await page.goto("https://www.python.org/")
    # create a screenshot of the page and save it
    await page.screenshot({"path": "python.png"})
    c = await page.content()
    await browser.close()
    return c

# print("Starting...")
# asyncio.get_event_loop().run_until_complete(get_webpage_content())
# print("Screenshot has been taken")


class bannerAd(models.Model):
    # Relationships
    emotion = models.ManyToManyField("bannerForm.Emotion")

    # Fields
    websiteURL = models.URLField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    size = models.CharField(max_length=8)
    webpage_raw_content = models.TextField(blank=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.websiteURL)

    def get_absolute_url(self):
        return reverse("bannerForm_bannerAd_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("bannerForm_bannerAd_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("bannerForm_bannerAd_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("bannerForm_bannerAd_htmx_delete", args=(self.pk,))

    def get_webpage_content(self):
        session = HTMLSession()
        r = session.get(self.websiteURL)



class Emotion(models.Model):
    Name = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    slug = models.SlugField(blank=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.Name)

    def get_absolute_url(self):
        return reverse("bannerForm_Emotion_detail", args=(self.slug,))

    def get_update_url(self):
        return reverse("bannerForm_Emotion_update", args=(self.slug,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("bannerForm_Emotion_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("bannerForm_Emotion_htmx_delete", args=(self.slug,))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.Name)
        super(Emotion, self).save(*args, **kwargs)
