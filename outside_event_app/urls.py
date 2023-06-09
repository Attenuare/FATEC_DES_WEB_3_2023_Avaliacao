from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("listar", views.presences, name="presences"),
]

urlpatterns += staticfiles_urlpatterns()