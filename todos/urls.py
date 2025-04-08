from django.urls import path
from . import views

urlpatterns = [
    # Like so, now the index view is mapped to the root URL of this app
    # If I want to access this from the project, I need to include this app in the project's urls.py too
    path("", views.index, name="index")
]
