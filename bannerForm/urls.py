from django.urls import path, include
from rest_framework import routers

from . import api
from . import views
from . import htmx


router = routers.DefaultRouter()
router.register("bannerAd", api.bannerAdViewSet)
router.register("Emotion", api.EmotionViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("bannerForm/bannerAd/", views.bannerAdListView.as_view(), name="bannerForm_bannerAd_list"),
    path("bannerForm/bannerAd/create/", views.bannerAdCreateView.as_view(), name="bannerForm_bannerAd_create"),
    path("bannerForm/bannerAd/detail/<int:pk>/", views.bannerAdDetailView.as_view(), name="bannerForm_bannerAd_detail"),
    path("bannerForm/bannerAd/update/<int:pk>/", views.bannerAdUpdateView.as_view(), name="bannerForm_bannerAd_update"),
    path("bannerForm/bannerAd/delete/<int:pk>/", views.bannerAdDeleteView.as_view(), name="bannerForm_bannerAd_delete"),
    path("bannerForm/Emotion/", views.EmotionListView.as_view(), name="bannerForm_Emotion_list"),
    path("bannerForm/Emotion/create/", views.EmotionCreateView.as_view(), name="bannerForm_Emotion_create"),
    path("bannerForm/Emotion/detail/<slug:slug>/", views.EmotionDetailView.as_view(), name="bannerForm_Emotion_detail"),
    path("bannerForm/Emotion/update/<slug:slug>/", views.EmotionUpdateView.as_view(), name="bannerForm_Emotion_update"),
    path("bannerForm/Emotion/delete/<slug:slug>/", views.EmotionDeleteView.as_view(), name="bannerForm_Emotion_delete"),

    path("bannerForm/htmx/bannerAd/", htmx.HTMXbannerAdListView.as_view(), name="bannerForm_bannerAd_htmx_list"),
    path("bannerForm/htmx/bannerAd/create/", htmx.HTMXbannerAdCreateView.as_view(), name="bannerForm_bannerAd_htmx_create"),
    path("bannerForm/htmx/bannerAd/delete/<int:pk>/", htmx.HTMXbannerAdDeleteView.as_view(), name="bannerForm_bannerAd_htmx_delete"),
    path("bannerForm/htmx/Emotion/", htmx.HTMXEmotionListView.as_view(), name="bannerForm_Emotion_htmx_list"),
    path("bannerForm/htmx/Emotion/create/", htmx.HTMXEmotionCreateView.as_view(), name="bannerForm_Emotion_htmx_create"),
    path("bannerForm/htmx/Emotion/delete/<slug:slug>/", htmx.HTMXEmotionDeleteView.as_view(), name="bannerForm_Emotion_htmx_delete"),
)
