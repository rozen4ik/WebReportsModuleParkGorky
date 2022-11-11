from django.urls import path
from configuration import views

urlpatterns = [
    path('edit/<int:id>/', views.edit)
]
