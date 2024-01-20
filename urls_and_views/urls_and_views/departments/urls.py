from django.urls import path, include

import urls_and_views
from urls_and_views.departments.views import department_details, department_details_by_name, index

urlpatterns = [
    path('', index),
    path('index/', index),
    path("<int:pk>", department_details),
    path('<str:name>', department_details_by_name),

]
