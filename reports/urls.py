from django.urls import path
from reports import views

urlpatterns = [
    path('', views.index),
    path('ticket_sales/', views.ticket_sales),
    path('passages_through_turnstiles/', views.passages_through_turnstiles),
    path('rule_list/', views.rule_list),
    path('export_stat_bill/', views.export_stat_bill, name='export-stat-bill'),
    path('export_passage/', views.export_passage, name='export-passage'),
    path('export_rule_list/', views.export_rule_list, name='export-rule-list')
]
