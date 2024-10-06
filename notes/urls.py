from django.urls import path
from . import views

urlpatterns = [
    path("",views.base,name="base"),
    path("Add",views.add,name="add"),
    path("View",views.viewc,name="view"),
    path("Edit/<int:param>",views.edit,name="edit"),
    path("Delete/<int:param>",views.delete,name="delete")
]