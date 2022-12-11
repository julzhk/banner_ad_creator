from random import choice

import replicate
import requests
from django.conf import settings
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Result(models.Model):
    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    image_src = models.URLField(blank=True)
    image = models.ImageField(upload_to="images/",
                              height_field=None,
                              width_field=None,
                              max_length=None,
                              blank=True,
                              )
    banner = models.ForeignKey("bannerForm.bannerAd",
                               on_delete=models.CASCADE,
                               related_name="results")

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    @property
    def image_full_path(self):
        return f'{settings.BASE_DIR_PATH}{settings.MEDIA_URL}{self.image.name}'

    def get_absolute_url(self):
        return reverse("bannerResult_Result_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("bannerResult_Result_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("bannerResult_Result_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("bannerResult_Result_htmx_delete", args=(self.pk,))

    def save_image_from_url(self, url):
        r = requests.get(url)
        img_temp = NamedTemporaryFile(delete=True)
        img_temp.write(r.content)
        img_temp.flush()
        img_file_object = File(img_temp)
        fn = slugify(url.split("/")[-2])[:16]
        self.image.save(name=f'{fn}.png', content=img_file_object, save=False)

    def generate(self, slogan):
        model = replicate.models.get("stability-ai/stable-diffusion")
        version = model.versions.get("27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478")
        prompts = [
            f"glossy photo-montage interesting palette on the concept of: {slogan}",
            f"mdjrny-v4 style banner advert for the concept of: {slogan} showing no words and without text"
            f"sophisticated illustration on the concept of: {slogan} showing just pictures and without text"
            f"abstract commercial illustration on the concept of: {slogan} showing just pictures and without text"
        ]
        prompt = choice(prompts)
        self.image_src = version.predict(prompt=prompt)[0]
        self.save_image_from_url(self.image_src)
        self.save()
