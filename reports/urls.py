from django.urls import path
from reports import views

urlpatterns = [
    path('', views.index),
    path('ticket_sales/', views.ticket_sales),
    path('passages_through_turnstiles/', views.passages_through_turnstiles),
    path('export_stat_bill/', views.export_stat_bill, name='export-stat-bill')
]
