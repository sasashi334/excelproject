from django.urls import path, include
from . import views

app_name = "excel"

urlpatterns = [
    path("", views.index, name="index"),
    path("edit/", views.edit_file, name="edit"),
    path("<int:pk>/delete/", views.delete_func, name="delete"),
]
