from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('exam_prep.web.urls')),
    path('album/', include('exam_prep.albums.urls')),
    path('profile/', include('exam_prep.profiles.urls')),
]
