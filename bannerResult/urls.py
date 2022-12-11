from django.urls import path, include
from rest_framework import routers

from . import api
from . import views
from . import htmx


router = routers.DefaultRouter()
router.register("Result", api.ResultViewSet)
urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("bannerResult/Result/", views.ResultListView.as_view(), name="bannerResult_Result_list"),
    path("bannerResult/Result/create/", views.ResultCreateView.as_view(), name="bannerResult_Result_create"),
    path("bannerResult/Result/detail/<int:pk>/", views.ResultDetailView.as_view(), name="bannerResult_Result_detail"),
    path("bannerResult/Result/update/<int:pk>/", views.ResultUpdateView.as_view(), name="bannerResult_Result_update"),
    path("bannerResult/Result/delete/<int:pk>/", views.ResultDeleteView.as_view(), name="bannerResult_Result_delete"),

    path("bannerResult/htmx/Result/", htmx.HTMXResultListView.as_view(), name="bannerResult_Result_htmx_list"),
    path("bannerResult/htmx/Result/create/", htmx.HTMXResultCreateView.as_view(), name="bannerResult_Result_htmx_create"),
    path("bannerResult/htmx/Result/delete/<int:pk>/", htmx.HTMXResultDeleteView.as_view(), name="bannerResult_Result_htmx_delete"),
)
