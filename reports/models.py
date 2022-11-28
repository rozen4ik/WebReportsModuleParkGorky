from django.db import models


# Отчёт по продажам мест
class Kontur(models.Model):
    date_bill = models.CharField(max_length=250, blank=True, null=True)
    id_ticket = models.CharField(max_length=200, blank=True, null=True)
    tariff = models.CharField(max_length=200, blank=True, null=True)
    ticket_validity_date = models.CharField(max_length=250, blank=True, null=True)
    date_of_ticket_passage = models.CharField(max_length=250, blank=True, null=True)


class Baloon(models.Model):
    date_bill = models.CharField(max_length=250, blank=True, null=True)
    id_ticket = models.CharField(max_length=200, blank=True, null=True)
    tariff = models.CharField(max_length=200, blank=True, null=True)


# Отчёт по проходам через турникет
class PassagesTurnstile(models.Model):
    resolution_timestamp = models.CharField(max_length=250, blank=True, null=True)
    id_point = models.CharField(max_length=250, blank=True, null=True)
    id_ter_from = models.CharField(max_length=250, blank=True, null=True)
    id_ter_to = models.CharField(max_length=250, blank=True, null=True)
    identifier_value = models.CharField(max_length=250, blank=True, null=True)


class RuleList(models.Model):
    rule_use = models.CharField(max_length=250, blank=True, null=True)


class ServiceList(models.Model):
    service = models.CharField(max_length=250, blank=True, null=True)


class DeskItems(models.Model):
    id_desk = models.CharField(max_length=250, blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)


class ReportZDesk(models.Model):
    number = models.CharField(max_length=250, blank=True, null=True)
    condition = models.CharField(max_length=250, blank=True, null=True)
    desk = models.CharField(max_length=250, blank=True, null=True)
    type = models.CharField(max_length=250, blank=True, null=True)
    number_fr = models.CharField(max_length=250, blank=True, null=True)
    open_sm = models.CharField(max_length=250, blank=True, null=True)
    operator_open = models.CharField(max_length=250, blank=True, null=True)
    close_sm = models.CharField(max_length=250, blank=True, null=True)
    operator_close = models.CharField(max_length=250, blank=True, null=True)


class SummaryReportDesk(models.Model):
    operation_desk = models.CharField(max_length=250, blank=True, null=True)
    operation_reg = models.CharField(max_length=250, blank=True, null=True)
    view_pay = models.CharField(max_length=250, blank=True, null=True)
    count_operation = models.CharField(max_length=250, blank=True, null=True)
    summ = models.CharField(max_length=250, blank=True, null=True)


class ErroneousOperations(models.Model):
    bill = models.CharField(max_length=250, blank=True, null=True)
    date_e = models.CharField(max_length=250, blank=True, null=True)
    summ = models.CharField(max_length=250, blank=True, null=True)
    number_doc = models.CharField(max_length=250, blank=True, null=True)
    condition = models.CharField(max_length=250, blank=True, null=True)
    operation_desk = models.CharField(max_length=250, blank=True, null=True)
    operation_reg = models.CharField(max_length=250, blank=True, null=True)
    type_pay = models.CharField(max_length=250, blank=True, null=True)
    comment = models.CharField(max_length=250, blank=True, null=True)


class SummMoney(models.Model):
    cash_amount = models.CharField(max_length=250, blank=True, null=True)
    the_amount_of_corrective_operations = models.CharField(max_length=250, blank=True, null=True)


class ViewPay(models.Model):
    view = models.CharField(max_length=250, blank=True, null=True)
    pay = models.CharField(max_length=250, blank=True, null=True)


class DecodingOfDeskSectionsAndTaxGroups(models.Model):
    tax_group = models.CharField(max_length=250, blank=True, null=True)
    desk_sections = models.CharField(max_length=250, blank=True, null=True)
    taxation_system = models.CharField(max_length=250, blank=True, null=True)
    count_operation = models.CharField(max_length=250, blank=True, null=True)
    summ = models.CharField(max_length=250, blank=True, null=True)


class AdditionalInformationAboutTheDeskRegister(models.Model):
    date_a = models.CharField(max_length=250, blank=True, null=True)
    comment = models.CharField(max_length=250, blank=True, null=True)


class IdentTypes(models.Model):
    id_ident_type = models.CharField(max_length=250, blank=True, null=True)
    caption = models.CharField(max_length=250, blank=True, null=True)


class SaleIdent(models.Model):
    date_s = models.CharField(max_length=250, blank=True, null=True)
    type_s = models.CharField(max_length=250, blank=True, null=True)
    hardware_code = models.CharField(max_length=250, blank=True, null=True)
    user_code = models.CharField(max_length=250, blank=True, null=True)
    condition = models.CharField(max_length=250, blank=True, null=True)
    desk = models.CharField(max_length=250, blank=True, null=True)
    bill = models.CharField(max_length=250, blank=True, null=True)
    service = models.CharField(max_length=250, blank=True, null=True)
    price = models.CharField(max_length=250, blank=True, null=True)
