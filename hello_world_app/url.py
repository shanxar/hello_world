from django.urls import path
from .views import Hello_World

urlpatterns = [
    path('hello/',Hello_World.as_view())
]
