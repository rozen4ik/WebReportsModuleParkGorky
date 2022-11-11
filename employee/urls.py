from django.urls import path
from reports import views

urlpatterns = [
    path('', views.index)
]
