import re
from bs4 import BeautifulSoup
from reports.models import *


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
