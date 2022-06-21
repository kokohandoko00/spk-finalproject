from django.urls import path
from . import views
#build index path
urlpatterns = [
    path('', views.index, name="index"),
]
