from django.shortcuts import render

from django.urls import reverse_lazy
from django.views import generic as views

from common.profile_helpers import get_profile
from world_of_speed.profiles.models import Profile


class CreateProfileView(views.CreateView):
    queryset = Profile.objects.all()
    fields = ('username', 'email', 'age', 'password', 'first_name', 'last_name', 'profile_picture')
    template_name = 'profiles/profile-create.html'
    success_url = reverse_lazy('catalogue')


class UpdateProfileView(views.UpdateView):
    queryset = Profile.objects.all()
    fields = ('username', 'email', 'age', 'password', 'first_name', 'last_name', 'profile_picture')
    template_name = 'profiles/profile-edit.html'
    success_url = reverse_lazy('details_profile')


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

