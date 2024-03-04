from django.urls import path

from world_of_speed.web.views import index, create_profile

urlpatterns = (
    path("", index, name='index'),
    path("profile/", create_profile, name='create_profile')
)