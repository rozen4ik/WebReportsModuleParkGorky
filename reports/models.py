from django.db import models


# Create your models here.
class Kontur(models.Model):
    date_bill = models.CharField(max_length=250, blank=True, null=True)
    id_ticket = models.CharField(max_length=200, blank=True, null=True)
    tariff = models.CharField(max_length=200, blank=True, null=True)
    ticket_validity_date = models.CharField(max_length=250, blank=True, null=True)
    date_of_ticket_passage = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return f"id: {self.id} date bill: {self.date_bill} id ticket: {self.id_ticket}"

    class Meta:
        verbose_name = "таблица контур"
        verbose_name_plural = "таблицы контура"


class Baloon(models.Model):
    date_bill = models.CharField(max_length=250, blank=True, null=True)
    id_ticket = models.CharField(max_length=200, blank=True, null=True)
    tariff = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"id: {self.id} date bill: {self.date_bill} id ticket: {self.id_ticket} tariff: {self.tariff}"

    class Meta:
        verbose_name = "таблица балона"
        verbose_name_plural = "таблицы балона"
