from django.db import models
from django.urls import reverse
from django.utils.text import slugify

import bannerResult


class bannerAd(models.Model):
    # Relationships
    emotion = models.ManyToManyField("bannerForm.Emotion")

    # Fields
    websiteURL = models.URLField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    size = models.CharField(max_length=8)

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
