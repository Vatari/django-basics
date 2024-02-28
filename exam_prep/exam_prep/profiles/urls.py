from django.urls import path

from exam_prep.profiles.views import DetailProfileView, DeleteProfileView

urlpatterns = (
    path('details/', DetailProfileView.as_view(), name='details_profile'),
    path('delete/', DeleteProfileView.as_view(), name='delete_profile'),
)