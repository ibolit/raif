from django.contrib import admin
from django.urls import path, include

from vectors.views import VectorsView

urlpatterns = [
    path('', VectorsView.as_view())
]
