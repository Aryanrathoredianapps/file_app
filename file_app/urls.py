
from .views import FileView
from django.urls import path

urlpatterns = [
    path('upload/', FileView.as_view()),
]