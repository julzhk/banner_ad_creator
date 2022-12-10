import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType

from bannerForm import models as bannerForm_models
from bannerResult import models as bannerResult_models


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_User(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_AbstractUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractUser.objects.create(**defaults)


def create_AbstractBaseUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractBaseUser.objects.create(**defaults)


def create_Group(**kwargs):
    defaults = {
        "name": "%s_group" % random_string(5),
    }
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_ContentType(**kwargs):
    defaults = {
    }
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_bannerForm_Emotion(**kwargs):
    defaults = {}
    defaults["Name"] = ""
    defaults["slug"] = ""
    defaults.update(**kwargs)
    return bannerForm_models.Emotion.objects.create(**defaults)
def create_bannerForm_bannerAd(**kwargs):
    defaults = {}
    defaults["size"] = ""
    defaults["websiteURL"] = ""
    if "emotion" not in kwargs:
        defaults["emotion"] = create_bannerForm_Emotion()
    defaults.update(**kwargs)
    return bannerForm_models.bannerAd.objects.create(**defaults)
def create_bannerResult_Result(**kwargs):
    defaults = {}
    defaults["image"] = ""
    defaults.update(**kwargs)
    return bannerResult_models.Result.objects.create(**defaults)
