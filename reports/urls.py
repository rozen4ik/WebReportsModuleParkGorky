from django.urls import path
from reports import views

urlpatterns = [
    path('', views.index),
    path('ticket_sales/', views.ticket_sales),
    path('passages_through_turnstiles/', views.passages_through_turnstiles)
    # path('ticket_sales/show_result_ticket_sales/', views.show_result)
]
