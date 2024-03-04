from django.forms import modelform_factory
from django.urls import reverse_lazy
from django.views import generic as views

from common.profile_helpers import get_profile
from world_of_speed.cars.models import Car


class CarFormMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['type'].widget.attrs['placeholder'] = 'Type'
        form.fields['model'].widget.attrs['placeholder'] = 'Model'
        form.fields['year'].widget.attrs['placeholder'] = 'Year'
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


class CreateCarView(CarFormMixin, views.CreateView):
    queryset = Car.objects.all()
    fields = ('type', 'model', 'year', 'image_url', 'price')
    template_name = 'cars/car-create.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        form.instance.owner_id = get_profile().pk
        return super().form_valid(form)


class DetailCarView(views.DetailView):
    queryset = Car.objects.all()
    template_name = 'cars/car-details.html'


class EditCarView(CarFormMixin, views.UpdateView):
    queryset = Car.objects.all()
    fields = ('type', 'model', 'year', 'image_url', 'price')
    template_name = 'cars/car-edit.html'
    success_url = reverse_lazy('catalogue')


class DeleteCarView(ReadonlyViewMixin, views.DeleteView):
    queryset = Car.objects.all()
    fields = ('type', 'model', 'year', 'image_url', 'price')

    template_name = 'cars/car-delete.html'
    success_url = reverse_lazy('catalogue')
    form_class = modelform_factory(Car, fields=('type', 'model', 'year', 'image_url', 'price'))

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs
