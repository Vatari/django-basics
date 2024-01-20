from django.urls import path

from urls_and_views.core.views import new_index

urlpatterns = [
    path('', new_index),
    path('<int:id>', new_index),
    path('<slug:slug>', new_index),
    path('<int:id>/<slug:slug>', new_index),
]
