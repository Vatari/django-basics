from django.shortcuts import render, redirect

from common.profile_helpers import get_profile
from world_of_speed.cars.models import Car
from world_of_speed.web.forms import CreateProfileForm


def create_profile(request):
    form = CreateProfileForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("catalogue")

    context = {
        "form": form,
        "user": True
    }
    return render(request, "web/catalogue.html", context)


def index(request):
    context = {
        "user": get_profile()
    }
    return render(request, "web/index.html", context)


def catalogue(request):
    profile = get_profile()

    if profile is None:
        return create_profile(request)

    context = {
        "cars": Car.objects.all(),
        "user": True,
    }
    return render(request, "web/catalogue.html", context)
