from django.urls import path
from .views import ClassesListView, ClassesDetailView

urlpatterns = [
    path("Classes/", ClassesListView.as_view(), name="classes-list"),
    path("Classes/<int:pk>", ClassesDetailView.as_view(), name="classes-detail"),
 
]