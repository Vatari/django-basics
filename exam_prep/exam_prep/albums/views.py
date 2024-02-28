from django.forms import modelform_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from exam_prep.albums.models import Album
from exam_prep.web.views import get_profile


class AlbumFormMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['name'].widget.attrs['placeholder'] = 'Album Name'
        form.fields['artist_name'].widget.attrs['placeholder'] = 'Artist'
        form.fields['description'].widget.attrs['placeholder'] = 'Description'
        form.fields['image_url'].widget.attrs['placeholder'] = 'Image URL'
        form.fields['price'].widget.attrs['placeholder'] = 'Price'

        return form


class ReadonlyViewMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        for field in form.fields.values():
            field.widget.attrs['readonly'] = True
            # field.widget.attrs['disabled'] = True
        return form


class CreateAlbumView(AlbumFormMixin, views.CreateView):
    queryset = Album.objects.all()
    fields = ('name', 'artist_name', 'genre', 'description', 'image_url', 'price')
    template_name = 'albums/album-add.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.owner_id = get_profile().pk
        return super().form_valid(form)


class DetailAlbumView(views.DetailView):
    queryset = Album.objects.all()
    template_name = 'albums/album-details.html'


class EditAlbumView(AlbumFormMixin, views.UpdateView):
    queryset = Album.objects.all()
    fields = ('name', 'artist_name', 'genre', 'description', 'image_url', 'price')
    template_name = 'albums/album-edit.html'
    success_url = reverse_lazy('index')


class DeleteAlbumView(ReadonlyViewMixin, views.DeleteView):
    queryset = Album.objects.all()
    fields = ('name', 'artist_name', 'genre', 'description', 'image_url', 'price')
    template_name = 'albums/album-delete.html'
    success_url = reverse_lazy('index')
    form_class = modelform_factory(Album, fields=('name', 'artist_name', 'genre', 'description', 'image_url', 'price'))

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs
