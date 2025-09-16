from django.urls import path

from . import views

urlpatterns = [
    path("", views.process_email, name="process_email"),
]
