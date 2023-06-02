from django.contrib import admin
from django.urls import path
from .views import infer_facts


urlpatterns = [
    path('', infer_facts, name='infer_facts'),
]
