from django.contrib import admin

from reports.models import Kontur, Baloon


@admin.register(Kontur)
class KonturAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "date_bill",
        "id_ticket",
        "tariff",
        "ticket_validity_date",
        "date_of_ticket_passage"
    )
    list_display_links = (
        "id",
        "date_bill",
        "id_ticket",
        "tariff",
        "ticket_validity_date",
        "date_of_ticket_passage"
    )


@admin.register(Baloon)
class KonturAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "date_bill",
        "id_ticket",
        "tariff"
    )
    list_display_links = (
        "id",
        "date_bill",
        "id_ticket",
        "tariff"
    )
