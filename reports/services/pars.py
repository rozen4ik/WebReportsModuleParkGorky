import datetime
import re
from bs4 import BeautifulSoup
from reports.models import *
from datetime import timedelta


class Pars:
    def pars_ticket(self, trs, tag):
        count = 0
        kontur = Kontur.objects.all().delete()
        for tr in trs:
            cap = tr.find_all(tag)
            kontur = Kontur()
            for i in cap:
                caps = i.text.replace('\n', '')
                if count == 0:
                    kontur.date_bill = caps
                elif count == 1:
                    kontur.id_ticket = caps
                elif count == 3:
                    kontur.tariff = caps
                elif count == 6:
                    kontur.ticket_validity_date = caps
                elif count == 7:
                    kontur.date_of_ticket_passage = caps
                count += 1
            kontur.save()
            count = 0
        kontur = Kontur.objects.all()
        kontur = kontur[0].delete()

    def pars_rule_list(self, trs):
        soup = BeautifulSoup(str(trs))
        r_list = soup.get_text()
        rule_use = RuleList.objects.all().delete()
        r_list = r_list.replace("[", "").replace("]", "").split(", ")
        for i in r_list:
            rule_use = RuleList()
            rule_use.rule_use = i
            rule_use.save()

    def pars_service_list(self, trs):
        soup = BeautifulSoup(str(trs))
        s_list = soup.get_text()
        service_use = ServiceList.objects.all().delete()
        s_list = s_list.replace("[", "").replace("]", "").split(", ")
        for i in s_list:
            res = re.sub("[A-Za-z]+", lambda ele: " " + ele[0] + " ", i)
            res = re.sub("[А-Яа-я]+", lambda ele: " " + ele[0] + " ", res)
            res = re.sub(r"\B([А-Я])", r" \1", res)
            res = res.replace("  ", " ")
            service_use = ServiceList()
            service_use.service = res.lstrip()
            service_use.save()

    def pars_desk_shift_1(self, trs, tag):
        report_z_desk = ReportZDesk.objects.all().delete()
        report_z_desk = ReportZDesk()
        report_z_desk.number = trs[0].find(tag).text.replace('\n', '')
        report_z_desk.condition = trs[1].find(tag).text.replace('\n', '')
        report_z_desk.desk = trs[2].find(tag).text.replace('\n', '')
        report_z_desk.type = trs[3].find(tag).text.replace('\n', '')
        report_z_desk.number_fr = trs[4].find(tag).text.replace('\n', '')
        report_z_desk.open_sm = trs[5].find(tag).text.replace('\n', '')
        report_z_desk.operator_open = trs[6].find(tag).text.replace('\n', '')
        report_z_desk.close_sm = trs[7].find(tag).text.replace('\n', '')
        report_z_desk.operator_close = trs[8].find(tag).text.replace('\n', '')
        report_z_desk.save()

    def pars_desk_shift_2(self, trs, tag):
        count = 0
        summary_report_desk = SummaryReportDesk.objects.all().delete()
        for tr in trs:
            cap = tr.find_all(tag)
            summary_report_desk = SummaryReportDesk()
            for i in cap:
                caps = i.text.replace('\n', '')
                if count == 0:
                    summary_report_desk.operation_desk = caps
                elif count == 1:
                    summary_report_desk.operation_reg = caps
                elif count == 2:
                    summary_report_desk.view_pay = caps
                elif count == 3:
                    summary_report_desk.count_operation = caps
                elif count == 4:
                    summary_report_desk.summ = caps
                count += 1
            summary_report_desk.save()
            count = 0
        summary_report_desk = SummaryReportDesk.objects.all()
        summary_report_desk = summary_report_desk[0].delete()

    def pars_desk_shift_3(self, trs, tag):
        count = 0
        erroneous_operations = ErroneousOperations.objects.all().delete()
        for tr in trs:
            cap = tr.find_all(tag)
            erroneous_operations = ErroneousOperations()
            for i in cap:
                caps = i.text.replace('\n', '')
                if count == 0:
                    erroneous_operations.bill = caps
                elif count == 1:
                    erroneous_operations.date_e = caps
                elif count == 2:
                    erroneous_operations.summ = caps
                elif count == 3:
                    erroneous_operations.number_doc = caps
                elif count == 4:
                    erroneous_operations.condition = caps
                elif count == 5:
                    erroneous_operations.operation_desk = caps
                elif count == 6:
                    erroneous_operations.operation_reg = caps
                elif count == 7:
                    erroneous_operations.type_pay = caps
                elif count == 8:
                    erroneous_operations.comment = caps
                count += 1
            erroneous_operations.save()
            count = 0
        erroneous_operations = ErroneousOperations.objects.all()
        erroneous_operations = erroneous_operations[0].delete()

    def pars_desk_shift_4(self, trs, tag):
        summ_money = SummMoney.objects.all().delete()
        summ_money = SummMoney()
        summ_money.cash_amount = trs[0].find(tag).text.replace('\n', '')
        summ_money.the_amount_of_corrective_operations = trs[1].find(tag).text.replace('\n', '')
        summ_money.save()

    def pars_desk_shift_5(self, trs, tag):
        count = 0
        view_pay = ViewPay.objects.all().delete()
        for tr in trs:
            cap = tr.find_all(tag)
            view_pay = ViewPay()
            for i in cap:
                caps = i.text.replace('\n', '')
                if count == 0:
                    view_pay.view = caps
                elif count == 1:
                    view_pay.pay = caps
                count += 1
            view_pay.save()
            count = 0
        view_pay = ViewPay.objects.all()
        view_pay = view_pay[0].delete()

    def pars_desk_shift_6(self, trs, tag):
        count = 0
        decoding_of_desk_sections_and_tax_groups = DecodingOfDeskSectionsAndTaxGroups.objects.all().delete()
        for tr in trs:
            cap = tr.find_all(tag)
            decoding_of_desk_sections_and_tax_groups = DecodingOfDeskSectionsAndTaxGroups()
            for i in cap:
                caps = i.text.replace('\n', '')
                if count == 0:
                    decoding_of_desk_sections_and_tax_groups.tax_group = caps
                elif count == 1:
                    decoding_of_desk_sections_and_tax_groups.desk_sections = caps
                elif count == 2:
                    decoding_of_desk_sections_and_tax_groups.taxation_system = caps
                elif count == 3:
                    decoding_of_desk_sections_and_tax_groups.count_operation = caps
                elif count == 4:
                    decoding_of_desk_sections_and_tax_groups.summ = caps
                count += 1
            decoding_of_desk_sections_and_tax_groups.save()
            count = 0
        decoding_of_desk_sections_and_tax_groups = DecodingOfDeskSectionsAndTaxGroups.objects.all()
        decoding_of_desk_sections_and_tax_groups = decoding_of_desk_sections_and_tax_groups[0].delete()

    def pars_desk_shift_7(self, trs, tag):
        count = 0
        additional_information_about_the_desk_register = AdditionalInformationAboutTheDeskRegister.objects.all().delete()
        for tr in trs:
            cap = tr.find_all(tag)
            additional_information_about_the_desk_register = AdditionalInformationAboutTheDeskRegister()
            for i in cap:
                caps = i.text.replace('\n', '')
                if count == 0:
                    additional_information_about_the_desk_register.date_a = caps
                elif count == 1:
                    additional_information_about_the_desk_register.comment = caps
                count += 1
            additional_information_about_the_desk_register.save()
            count = 0

    def pars_sale_ident(self, trs, tag):
        count = 0
        sale_ident = SaleIdent.objects.all().delete()
        for tr in trs:
            cap = tr.find_all(tag)
            sale_ident = SaleIdent()
            for i in cap:
                caps = i.text.replace('\n', '')
                if count == 1:
                    sale_ident.date_s = caps
                elif count == 2:
                    sale_ident.type_s = caps
                elif count == 3:
                    sale_ident.hardware_code = caps
                elif count == 4:
                    sale_ident.user_code = caps
                elif count == 5:
                    sale_ident.condition = caps
                elif count == 6:
                    sale_ident.desk = caps
                elif count == 7:
                    sale_ident.bill = caps
                elif count == 8:
                    sale_ident.service = caps
                elif count == 9:
                    sale_ident.price = caps
                count += 1
            sale_ident.save()
            count = 0
        sale_ident = SaleIdent.objects.all()
        sale_ident = sale_ident[0].delete()

    def pars_sales_by_cat(self, trs, tag):
        count = 0
        sales_by_cat = SalesByCat.objects.all().delete()
        for tr in trs:
            cap = tr.find_all(tag)
            sales_by_cat = SalesByCat()
            for i in cap:
                caps = i.text.replace('\n', '')
                if count == 0:
                    sales_by_cat.code_name = caps
                elif count == 1:
                    sales_by_cat.count = caps
                elif count == 2:
                    sales_by_cat.summ = caps
                elif count == 3:
                    sales_by_cat.discount = caps
                elif count == 4:
                    sales_by_cat.all_s = caps
                count += 1
            sales_by_cat.save()
            count = 0
        sales_by_cat = SalesByCat.objects.all()
        sales_by_cat = sales_by_cat[0].delete()

    def pars_sales_by_positions_stat(self, trs, tag):
        count = 0
        sales_by_positions_stat = SalesByPositionsStat.objects.all().delete()
        for tr in trs:
            cap = tr.find_all(tag)
            sales_by_positions_stat = SalesByPositionsStat()
            for i in cap:
                caps = i.text.replace('\n', '')
                if count == 0:
                    sales_by_positions_stat.service = caps
                elif count == 1:
                    sales_by_positions_stat.position = caps
                elif count == 2:
                    sales_by_positions_stat.price = caps
                elif count == 3:
                    sales_by_positions_stat.count = caps
                elif count == 4:
                    sales_by_positions_stat.summ = caps
                count += 1
            sales_by_positions_stat.save()
            count = 0
        sales_by_positions_stat = SalesByPositionsStat.objects.all()
        sales_by_positions_stat = sales_by_positions_stat[0].delete()

    def pars_sales_by_sno(self, trs, tag):
        count = 0
        sales_by_sno = SalesBySno.objects.all().delete()
        for tr in trs:
            cap = tr.find_all(tag)
            sales_by_sno = SalesBySno()
            for i in cap:
                caps = i.text.replace('\n', '')
                if count == 0:
                    sales_by_sno.code = caps
                elif count == 1:
                    sales_by_sno.caption = caps
                elif count == 2:
                    sales_by_sno.count = caps
                elif count == 3:
                    sales_by_sno.summ = caps
                elif count == 4:
                    sales_by_sno.discount = caps
                count += 1
            sales_by_sno.save()
            count = 0
        sales_by_sno = SalesBySno.objects.all()
        sales_by_sno = sales_by_sno[0].delete()

    def pars_ident_sales_stat(self, trs, tag):
        count = 0
        ident_sales_stat = IdentSalesStat.objects.all().delete()
        for tr in trs:
            cap = tr.find_all(tag)
            ident_sales_stat = IdentSalesStat()
            for i in cap:
                caps = i.text.replace('\n', '')
                if count == 0:
                    ident_sales_stat.price = caps
                elif count == 1:
                    ident_sales_stat.count = caps
                elif count == 2:
                    ident_sales_stat.summ = caps
                count += 1
            ident_sales_stat.save()
            count = 0
        ident_sales_stat = IdentSalesStat.objects.all()
        ident_sales_stat = ident_sales_stat[0].delete()

    def pars_ident_sales_by_tariff(self, trs, tag, date_cash):
        day = timedelta(days=1)
        count = 0
        ident_sales_by_tariff = IdentSalesByTariff.objects.all().delete()
        for tr in trs:
            cap = tr.find_all(tag)
            ident_sales_by_tariff = IdentSalesByTariff()
            for i in cap:
                caps = i.text.replace('\n', '')
                if count == 0:
                    ident_sales_by_tariff.tariff = f"{date_cash} {caps}"
                    if caps == "19:30":
                        date_cash += day
                elif count == 1:
                    ident_sales_by_tariff.limit = caps
                elif count == 2:
                    ident_sales_by_tariff.used = caps
                elif count == 3:
                    ident_sales_by_tariff.remains = caps
                count += 1
            ident_sales_by_tariff.save()
            count = 0
        ident_sales_by_tariff = IdentSalesByTariff.objects.all()
        ident_sales_by_tariff = ident_sales_by_tariff.filter(tariff=None).delete()
