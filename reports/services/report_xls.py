import datetime
import xlwt
from django.http import HttpResponse
from reports.models import *


class ReportXLS:
    def __get_stat_bill(self, kontur):
        return kontur.values_list(
            "date_bill",
            "id_ticket",
            "tariff",
            "ticket_validity_date",
            "date_of_ticket_passage",
        )

    def get_export_stat_bill(self, request):
        response = HttpResponse(content_type="applications/ms-excel")
        date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
        response["Content-Disposition"] = "attachment; filename=StatBill " + str(date) + ".xls"

        wb = xlwt.Workbook(encoding="utf-8")
        ws = wb.add_sheet("report")
        row_num = 1
        font_title = xlwt.XFStyle()
        font_title.font.name = "Times New Roman"
        font_title.font.height = 20 * 14
        font_title.font.bold = True
        font_title.alignment.vert = font_title.alignment.VERT_BOTTOM
        font_title.alignment.horz = font_title.alignment.HORZ_CENTER
        col_pat = xlwt.Pattern()
        col_pat.pattern = col_pat.SOLID_PATTERN
        col_pat.pattern_fore_colour = 22
        col_pat.pattern_back_colour = 4
        font_title.pattern = col_pat
        font_title.borders.top = font_title.borders.THIN
        font_title.borders.bottom = font_title.borders.THIN
        font_title.borders.left = font_title.borders.THIN
        font_title.borders.right = font_title.borders.THIN

        ws.write_merge(0, 0, 0, 4, "Отчёт по продажам билетов", font_title)

        font_zag = xlwt.XFStyle()
        font_zag.font.name = "Times New Roman"
        font_zag.alignment.vert = font_title.alignment.VERT_BOTTOM
        font_zag.alignment.horz = font_title.alignment.HORZ_CENTER
        font_zag.font.bold = False
        font_zag.borders.top = font_zag.borders.THIN
        font_zag.borders.bottom = font_zag.borders.THIN
        font_zag.borders.left = font_zag.borders.THIN
        font_zag.borders.right = font_zag.borders.THIN
        font_zag.font.height = 20 * 12

        columns = [
            "Дата продажи",
            "ID билета",
            "Тариф",
            "Дата действия билета",
            "Дата прохода по билету"
        ]

        len_date_bill = len(columns[0])
        len_id_ticket = len(columns[1])
        len_tariff = len(columns[2])
        len_ticket_validity_date = len(columns[3])
        len_date_of_ticket_passage = len(columns[4])

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_zag)

        font_style = xlwt.XFStyle()
        font_style.font.name = "Times New Roman"
        font_style.font.bold = False
        font_style.borders.top = font_zag.borders.THIN
        font_style.borders.bottom = font_zag.borders.THIN
        font_style.borders.left = font_zag.borders.THIN
        font_style.borders.right = font_zag.borders.THIN
        font_style.font.height = 20 * 12

        kontur = self.__get_stat_bill(Kontur.objects.all().order_by("date_bill"))
        rows = kontur

        for i in kontur:
            if len_date_bill < len(i[0]):
                len_date_bill = len(i[0])
            if len_id_ticket < len(i[1]):
                len_id_ticket = len(i[1])
            if len_tariff < len(i[2]):
                len_tariff = len(i[2])
            if len_ticket_validity_date < len(i[3]):
                len_ticket_validity_date = len(i[3])
            if len_date_of_ticket_passage < len(i[4]):
                len_date_of_ticket_passage = len(i[4])

        width_col = [
            len_date_bill,
            len_id_ticket,
            len_tariff,
            len_ticket_validity_date,
            len_date_of_ticket_passage
        ]

        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.col(col_num).width = 256 * (int(width_col[col_num]) + 1)
                ws.write(row_num, col_num, str(row[col_num]), font_style)

        wb.save(response)

        return response

    def __get_passage(self, passages_turnstile):
        return passages_turnstile.values_list(
            'resolution_timestamp',
            'id_point',
            'id_ter_from',
            'id_ter_to',
            'identifier_value',
        )

    def get_export_passage(self, request):
        response = HttpResponse(content_type="applications/ms-excel")
        date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
        response["Content-Disposition"] = "attachment; filename=Passage " + str(date) + ".xls"

        wb = xlwt.Workbook(encoding="utf-8")
        ws = wb.add_sheet("report")
        row_num = 1
        font_title = xlwt.XFStyle()
        font_title.font.name = "Times New Roman"
        font_title.font.height = 20 * 14
        font_title.font.bold = True
        font_title.alignment.vert = font_title.alignment.VERT_BOTTOM
        font_title.alignment.horz = font_title.alignment.HORZ_CENTER
        col_pat = xlwt.Pattern()
        col_pat.pattern = col_pat.SOLID_PATTERN
        col_pat.pattern_fore_colour = 22
        col_pat.pattern_back_colour = 4
        font_title.pattern = col_pat
        font_title.borders.top = font_title.borders.THIN
        font_title.borders.bottom = font_title.borders.THIN
        font_title.borders.left = font_title.borders.THIN
        font_title.borders.right = font_title.borders.THIN

        ws.write_merge(0, 0, 0, 4, "Отчёт по проходам через турникеты", font_title)

        font_zag = xlwt.XFStyle()
        font_zag.font.name = "Times New Roman"
        font_zag.alignment.vert = font_title.alignment.VERT_BOTTOM
        font_zag.alignment.horz = font_title.alignment.HORZ_CENTER
        font_zag.font.bold = False
        font_zag.borders.top = font_zag.borders.THIN
        font_zag.borders.bottom = font_zag.borders.THIN
        font_zag.borders.left = font_zag.borders.THIN
        font_zag.borders.right = font_zag.borders.THIN
        font_zag.font.height = 20 * 12

        columns = [
            "Дата прохода",
            "Устройство",
            "Откуда",
            "Куда",
            "Индификатор"
        ]

        len_resolution_timestamp = len(columns[0])
        len_id_point = len(columns[1])
        len_id_ter_from = len(columns[2])
        len_id_ter_to = len(columns[3])
        len_identifier_value = len(columns[4])

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_zag)

        font_style = xlwt.XFStyle()
        font_style.font.name = "Times New Roman"
        font_style.font.bold = False
        font_style.borders.top = font_zag.borders.THIN
        font_style.borders.bottom = font_zag.borders.THIN
        font_style.borders.left = font_zag.borders.THIN
        font_style.borders.right = font_zag.borders.THIN
        font_style.font.height = 20 * 12

        passages_turnstiles = self.__get_passage(PassagesTurnstile.objects.all().order_by('resolution_timestamp'))
        rows = passages_turnstiles

        for i in passages_turnstiles:
            if len_resolution_timestamp < len(i[0]):
                len_resolution_timestamp = len(i[0])
            if len_id_point < len(i[1]):
                len_id_point = len(i[1])
            if len_id_ter_from < len(i[2]):
                len_id_ter_from = len(i[2])
            if len_id_ter_to < len(i[3]):
                len_id_ter_to = len(i[3])
            if len_identifier_value < len(i[4]):
                len_identifier_value = len(i[4])

        width_col = [
            len_resolution_timestamp,
            len_id_point,
            len_id_ter_to,
            len_id_ter_from,
            len_identifier_value
        ]

        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.col(col_num).width = 256 * (int(width_col[col_num]) + 1)
                ws.write(row_num, col_num, str(row[col_num]), font_style)

        wb.save(response)

        return response

    def __get_rule_list(self, rule_list):
        return rule_list.values_list(
            'rule_use',
        )

    def get_export_rule_list(self, request):
        response = HttpResponse(content_type="applications/ms-excel")
        date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
        response["Content-Disposition"] = "attachment; filename=RuleList " + str(date) + ".xls"

        wb = xlwt.Workbook(encoding="utf-8")
        ws = wb.add_sheet("report")
        row_num = 1
        font_title = xlwt.XFStyle()
        font_title.font.name = "Times New Roman"
        font_title.font.height = 20 * 14
        font_title.font.bold = True
        font_title.alignment.vert = font_title.alignment.VERT_BOTTOM
        font_title.alignment.horz = font_title.alignment.HORZ_CENTER
        col_pat = xlwt.Pattern()
        col_pat.pattern = col_pat.SOLID_PATTERN
        col_pat.pattern_fore_colour = 22
        col_pat.pattern_back_colour = 4
        font_title.pattern = col_pat
        font_title.borders.top = font_title.borders.THIN
        font_title.borders.bottom = font_title.borders.THIN
        font_title.borders.left = font_title.borders.THIN
        font_title.borders.right = font_title.borders.THIN

        font_zag = xlwt.XFStyle()
        font_zag.font.name = "Times New Roman"
        font_zag.alignment.vert = font_title.alignment.VERT_BOTTOM
        font_zag.alignment.horz = font_title.alignment.HORZ_CENTER
        font_zag.font.bold = False
        font_zag.borders.top = font_zag.borders.THIN
        font_zag.borders.bottom = font_zag.borders.THIN
        font_zag.borders.left = font_zag.borders.THIN
        font_zag.borders.right = font_zag.borders.THIN
        font_zag.font.height = 20 * 12

        columns = [
            "Отчёт по правилам пользования",
            "Правила пользования"
        ]

        len_rule_use = len(columns[0])

        ws.write(0, 0, columns[0], font_title)
        ws.write(row_num, 0, columns[1], font_zag)

        font_style = xlwt.XFStyle()
        font_style.font.name = "Times New Roman"
        font_style.font.bold = False
        font_style.borders.top = font_zag.borders.THIN
        font_style.borders.bottom = font_zag.borders.THIN
        font_style.borders.left = font_zag.borders.THIN
        font_style.borders.right = font_zag.borders.THIN
        font_style.font.height = 20 * 12

        r_list = self.__get_rule_list(RuleList.objects.all())
        rows = r_list

        for i in r_list:
            if len_rule_use < len(i[0]):
                len_rule_use = len(i[0])

        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.col(col_num).width = 256 * (len_rule_use + 7)
                ws.write(row_num, col_num, str(row[col_num]), font_style)

        wb.save(response)

        return response

    def __get_service_list(self, service_list):
        return service_list.values_list(
            'service',
        )

    def get_export_service_list(self, request):
        response = HttpResponse(content_type="applications/ms-excel")
        date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
        response["Content-Disposition"] = "attachment; filename=ServiceList " + str(date) + ".xls"

        wb = xlwt.Workbook(encoding="utf-8")
        ws = wb.add_sheet("report")
        row_num = 1
        font_title = xlwt.XFStyle()
        font_title.font.name = "Times New Roman"
        font_title.font.height = 20 * 14
        font_title.font.bold = True
        font_title.alignment.vert = font_title.alignment.VERT_BOTTOM
        font_title.alignment.horz = font_title.alignment.HORZ_CENTER
        col_pat = xlwt.Pattern()
        col_pat.pattern = col_pat.SOLID_PATTERN
        col_pat.pattern_fore_colour = 22
        col_pat.pattern_back_colour = 4
        font_title.pattern = col_pat
        font_title.borders.top = font_title.borders.THIN
        font_title.borders.bottom = font_title.borders.THIN
        font_title.borders.left = font_title.borders.THIN
        font_title.borders.right = font_title.borders.THIN

        font_zag = xlwt.XFStyle()
        font_zag.font.name = "Times New Roman"
        font_zag.alignment.vert = font_title.alignment.VERT_BOTTOM
        font_zag.alignment.horz = font_title.alignment.HORZ_CENTER
        font_zag.font.bold = False
        font_zag.borders.top = font_zag.borders.THIN
        font_zag.borders.bottom = font_zag.borders.THIN
        font_zag.borders.left = font_zag.borders.THIN
        font_zag.borders.right = font_zag.borders.THIN
        font_zag.font.height = 20 * 12

        columns = [
            "Отчёт по услугам",
            "Услуги"
        ]

        len_service_use = len(columns[0])

        ws.write(0, 0, columns[0], font_title)
        ws.write(row_num, 0, columns[1], font_zag)

        font_style = xlwt.XFStyle()
        font_style.font.name = "Times New Roman"
        font_style.font.bold = False
        font_style.borders.top = font_zag.borders.THIN
        font_style.borders.bottom = font_zag.borders.THIN
        font_style.borders.left = font_zag.borders.THIN
        font_style.borders.right = font_zag.borders.THIN
        font_style.font.height = 20 * 12

        s_list = self.__get_service_list(ServiceList.objects.all())
        rows = s_list

        for i in s_list:
            if len_service_use < len(i[0]):
                len_service_use = len(i[0])

        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.col(col_num).width = 256 * (len_service_use + 1)
                ws.write(row_num, col_num, str(row[col_num]), font_style)

        wb.save(response)

        return response

    def __get_report_z_desk(self, report_z_desk):
        return report_z_desk.values_list(
            'number',
            'condition',
            'desk',
            'type',
            'number_fr',
            'open_sm',
            'operator_open',
            'close_sm',
            'operator_close'
        )

    def __get_summary_report_desk(self, summary_report_desk):
        return summary_report_desk.values_list(
            'operation_desk',
            'operation_reg',
            'view_pay',
            'count_operation',
            'summ'
        )

    def get_export_desk_shift(self, request):
        response = HttpResponse(content_type="applications/ms-excel")
        date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
        response["Content-Disposition"] = "attachment; filename=DeskShift " + str(date) + ".xls"

        wb = xlwt.Workbook(encoding="utf-8")
        ws = wb.add_sheet("report")
        row_num = 1
        font_title = xlwt.XFStyle()
        font_title.font.name = "Times New Roman"
        font_title.font.height = 20 * 14
        font_title.font.bold = True
        font_title.alignment.vert = font_title.alignment.VERT_BOTTOM
        font_title.alignment.horz = font_title.alignment.HORZ_CENTER
        col_pat = xlwt.Pattern()
        col_pat.pattern = col_pat.SOLID_PATTERN
        col_pat.pattern_fore_colour = 22
        col_pat.pattern_back_colour = 4
        font_title.pattern = col_pat
        font_title.borders.top = font_title.borders.THIN
        font_title.borders.bottom = font_title.borders.THIN
        font_title.borders.left = font_title.borders.THIN
        font_title.borders.right = font_title.borders.THIN

        ws.write_merge(0, 0, 0, 8, "Z-Отчёт по кассе", font_title)

        font_zag = xlwt.XFStyle()
        font_zag.font.name = "Times New Roman"
        font_zag.alignment.vert = font_title.alignment.VERT_BOTTOM
        font_zag.alignment.horz = font_title.alignment.HORZ_CENTER
        font_zag.font.bold = False
        font_zag.borders.top = font_zag.borders.THIN
        font_zag.borders.bottom = font_zag.borders.THIN
        font_zag.borders.left = font_zag.borders.THIN
        font_zag.borders.right = font_zag.borders.THIN
        font_zag.font.height = 20 * 12

        columns = [
            "Номер смены",
            "Состояние",
            "Касса",
            "Тип смены",
            "Номер ФР",
            "Открытие смены",
            "Оператор, открывший смену",
            "Закрытие смены",
            "Оператор, закрывший смену"
        ]

        len_number = len(columns[0])
        len_condition = len(columns[1])
        len_desk = len(columns[2])
        len_type = len(columns[3])
        len_number_fr = len(columns[4])
        len_open_sm = len(columns[5])
        len_operator_open = len(columns[6])
        len_close_sm = len(columns[7])
        len_operator_close = len(columns[8])

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_zag)

        font_style = xlwt.XFStyle()
        font_style.font.name = "Times New Roman"
        font_style.font.bold = False
        font_style.borders.top = font_zag.borders.THIN
        font_style.borders.bottom = font_zag.borders.THIN
        font_style.borders.left = font_zag.borders.THIN
        font_style.borders.right = font_zag.borders.THIN
        font_style.font.height = 20 * 12

        report_z_desk = self.__get_report_z_desk(ReportZDesk.objects.all())
        rows = report_z_desk

        for i in report_z_desk:
            if len_number < len(i[0]):
                len_number = len(i[0])
            if len_condition < len(i[1]):
                len_condition = len(i[1])
            if len_desk < len(i[2]):
                len_desk = len(i[2])
            if len_type < len(i[3]):
                len_type = len(i[3])
            if len_number_fr < len(i[4]):
                len_number_fr = len(i[4])
            if len_open_sm < len(i[5]):
                len_open_sm = len(i[5])
            if len_operator_open < len(i[6]):
                len_operator_open = len(i[6])
            if len_close_sm < len(i[7]):
                len_close_sm = len(i[7])
            if len_operator_close < len(i[8]):
                len_operator_close = len(i[8])

        width_col = [
            len_number,
            len_condition,
            len_desk,
            len_type,
            len_number_fr,
            len_open_sm,
            len_operator_open,
            len_close_sm,
            len_operator_close
        ]

        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.col(col_num).width = 256 * (int(width_col[col_num]) + 2)
                ws.write(row_num, col_num, str(row[col_num]), font_style)

        font_title.font.height = 20 * 12

        row_num += 1
        ws.write_merge(row_num, row_num, 0, 8, "Сводный отчёт по кассе", font_title)

        columns_2 = [
            "Операция кассы",
            "Операция регистратора",
            "Вид оплаты",
            "Кол-во операций",
            "Сумма"
        ]

        len_operation_desk = len(columns[0])
        len_operation_reg = len(columns[1])
        len_view_pay = len(columns[2])
        len_count_operation = len(columns[3])
        len_summ = len(columns[4])

        row_num += 1
        i = 0
        for col_num in range(len(columns_2)):
            i = col_num + 2
            ws.write(row_num, i, columns_2[col_num], font_zag)

        summary_report_desk = self.__get_summary_report_desk(SummaryReportDesk.objects.all())
        rows = summary_report_desk

        for i in summary_report_desk:
            if len_operation_desk < len(i[0]):
                len_operation_desk = len(i[0])
            if len_operation_reg < len(i[1]):
                len_operation_reg = len(i[1])
            if len_view_pay < len(i[2]):
                len_view_pay = len(i[2])
            if len_count_operation < len(i[3]):
                len_count_operation = len(i[3])
            if len_summ < len(i[4]):
                len_summ = len(i[4])

        width_col_2 = [
            len_operation_desk,
            len_operation_reg,
            len_view_pay,
            len_count_operation,
            len_summ
        ]

        for row in rows:
            row_num += 1
            i = 0
            for col_num in range(len(row)):
                i = col_num + 2
                ws.col(i).width = 256 * (int(width_col_2[col_num]) + 18)
                ws.write(row_num, i, str(row[col_num]), font_style)

        wb.save(response)

        return response
