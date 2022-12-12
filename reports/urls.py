from django.urls import path
from reports import views

urlpatterns = [
    path('', views.index),
    path('ticket_sales/', views.ticket_sales),
    path('passages_through_turnstiles/', views.passages_through_turnstiles),
    path('rule_list/', views.rule_list),
    path('service_list/', views.service_list),
    path('desk_shift/', views.desk_shift),
    path('sale_ident/', views.sale_ident),
    path('sales_by_cat/', views.sales_by_cat),
    path('sales_by_positions_stat/', views.sales_by_positions_stat),
    path('sales_by_sno/', views.sales_by_sno),
    path('ident_sales_stat/', views.ident_sales_stat),
    path('export_stat_bill/', views.export_stat_bill, name='export-stat-bill'),
    path('export_passage/', views.export_passage, name='export-passage'),
    path('export_rule_list/', views.export_rule_list, name='export-rule-list'),
    path('export_service_list/', views.export_service_list, name='export-service-list'),
    path('export_desk_shift/', views.export_desk_shift, name='export-desk-shift'),
    path('export_sale_ident/', views.export_sale_ident, name='export-sale-ident'),
    path('export_sales_by_cat/', views.export_sales_by_cat, name='export-sales-by-cat'),
    path('export_sales_by_positions_stat/', views.export_sales_by_positions_stat,
         name='export-sales-by-positions-stat'),
    path('export_sales_by_sno/', views.export_sales_by_sno, name='export-sales-by-sno'),
    path('export_ident_sales_stat/', views.export_ident_sales_stat, name='export-ident-sales-stat')
]
