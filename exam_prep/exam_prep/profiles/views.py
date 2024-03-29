from django.urls import reverse_lazy
from django.views import generic as views

from common.profile_helpers import get_profile
from exam_prep.profiles.models import Profile


class DetailProfileView(views.DetailView):
    queryset = Profile.objects.all()
    template_name = 'profiles/profile-details.html'

    def get_object(self, queryset=None):
        return get_profile()


class DeleteProfileView(views.DeleteView):
    template_name = 'profiles/profile-delete.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_profile()
