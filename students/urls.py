from django.contrib import admin
from django.urls import path, include
from .views import StudentsListView
from rest_framework.routers import DefaultRouter

r = DefaultRouter()

r.register('info', StudentsListView)

urlpatterns = [
    path('api/all_list/', include(r.urls)),
]