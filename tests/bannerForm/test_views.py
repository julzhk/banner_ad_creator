import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_bannerAd_list_view(client):
    instance1 = test_helpers.create_bannerForm_bannerAd()
    instance2 = test_helpers.create_bannerForm_bannerAd()
    url = reverse("bannerForm_bannerAd_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_bannerAd_create_view(client):
    emotion = test_helpers.create_bannerForm_Emotion()
    url = reverse("bannerForm_bannerAd_create")
    data = {
        "websiteURL": http://127.0.0.1,
        "size": "text",
        "emotion": emotion.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_bannerAd_detail_view(client):
    instance = test_helpers.create_bannerForm_bannerAd()
    url = reverse("bannerForm_bannerAd_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_bannerAd_update_view(client):
    emotion = test_helpers.create_bannerForm_Emotion()
    instance = test_helpers.create_bannerForm_bannerAd()
    url = reverse("bannerForm_bannerAd_update", args=[instance.pk, ])
    data = {
        "websiteURL": http://127.0.0.1,
        "size": "text",
        "emotion": emotion.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Emotion_list_view(client):
    instance1 = test_helpers.create_bannerForm_Emotion()
    instance2 = test_helpers.create_bannerForm_Emotion()
    url = reverse("bannerForm_Emotion_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Emotion_create_view(client):
    url = reverse("bannerForm_Emotion_create")
    data = {
        "Name": "text",
        "slug": "slug",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Emotion_detail_view(client):
    instance = test_helpers.create_bannerForm_Emotion()
    url = reverse("bannerForm_Emotion_detail", args=[instance.slug, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Emotion_update_view(client):
    instance = test_helpers.create_bannerForm_Emotion()
    url = reverse("bannerForm_Emotion_update", args=[instance.slug, ])
    data = {
        "Name": "text",
        "slug": "slug",
    }
    response = client.post(url, data)
    assert response.status_code == 302
