import replicate
import requests
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.db import models
from django.urls import reverse


class Result(models.Model):
    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    image = models.ImageField(upload_to="upload/images/",
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
        self.image.save(f"image_{url[:-16]}.jpg", img_file_object, save=False)

    def generate(self, debug=False):
        if debug:
            img_url = 'https://replicate.delivery/pbxt/15LlJeqLI1zHHS1axIW5F4YGNJ8dVMVxjOG7KAfcSJ4AnmIQA/out-0.png'
        else:
            model = replicate.models.get("stability-ai/stable-diffusion")
            version = model.versions.get("27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478")
            img_url = version.predict(prompt="a 19th century portrait of a wombat gentleman")[0]
        self.save_image_from_url(img_url)
