from django.urls import path

from world_of_speed.profiles.views import DetailProfileView, DeleteProfileView, CreateProfileView, UpdateProfileView

urlpatterns = (
    path('create/', CreateProfileView.as_view(), name='create_profile'),
    path('details/', DetailProfileView.as_view(), name='details_profile'),
    path('<int:pk>/edit/', UpdateProfileView.as_view(), name='edit_profile'),
    path('<int:pk>/delete/', DeleteProfileView.as_view(), name='delete_profile'),
)
