import datetime
import xlwt
from django.http import HttpResponse
from reports.models import *


class ReportXLS:
    def __settings_font(self, name, height, bold, center, cap):
        font = xlwt.XFStyle()
        font.font.name = name
        font.font.height = height
        font.font.bold = bold
        font.borders.top = font.borders.THIN
        font.borders.bottom = font.borders.THIN
        font.borders.left = font.borders.THIN
        font.borders.right = font.borders.THIN
        if center == "yes":
            font.alignment.vert = font.alignment.VERT_BOTTOM
            font.alignment.horz = font.alignment.HORZ_CENTER
        if cap == "yes":
            col_pat = xlwt.Pattern()
            col_pat.pattern = col_pat.SOLID_PATTERN
            col_pat.pattern_fore_colour = 22
            col_pat.pattern_back_colour = 4
            font.pattern = col_pat
        return font


    def __get_stat_bill(self, kontur):
        return kontur.values_list(
            "date_bill",
            "id_ticket",
            "tariff",
            "ticket_validity_date",
            "date_of_ticket_passage",
        )

    def get_export_stat_bill(self):
        response = HttpResponse(content_type="applications/ms-excel")
        date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
        response["Content-Disposition"] = "attachment; filename=StatBill " + str(date) + ".xls"

        wb = xlwt.Workbook(encoding="utf-8")
        ws = wb.add_sheet("report")
        row_num = 1
        font_title = self.__settings_font("Times New Roman", 20 * 14, True, "yes", "yes")

        ws.write_merge(0, 0, 0, 4, "Отчёт по статистике продаж по местам", font_title)

        font_zag = self.__settings_font("Times New Roman", 20 * 12, False, "yes", "no")

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

        font_style = self.__settings_font("Times New Roman", 20 * 12, False, "no", "no")

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

    def get_export_passage(self):
        response = HttpResponse(content_type="applications/ms-excel")
        date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
        response["Content-Disposition"] = "attachment; filename=Passage " + str(date) + ".xls"

        wb = xlwt.Workbook(encoding="utf-8")
        ws = wb.add_sheet("report")
        row_num = 1
        font_title = self.__settings_font("Times New Roman", 20 * 14, True, "yes", "yes")

        ws.write_merge(0, 0, 0, 4, "Отчёт по проходам через турникеты", font_title)

        font_zag = self.__settings_font("Times New Roman", 20 * 12, False, "yes", "no")

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

        font_style = self.__settings_font("Times New Roman", 20 * 12, False, "no", "no")

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

    def get_export_rule_list(self):
        response = HttpResponse(content_type="applications/ms-excel")
        date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
        response["Content-Disposition"] = "attachment; filename=RuleList " + str(date) + ".xls"

        wb = xlwt.Workbook(encoding="utf-8")
        ws = wb.add_sheet("report")
        row_num = 1
        font_title = self.__settings_font("Times New Roman", 20 * 14, True, "yes", "yes")
        font_zag = self.__settings_font("Times New Roman", 20 * 12, False, "yes", "no")

        columns = [
            "Отчёт по правилам пользования",
            "Правила пользования"
        ]

        len_rule_use = len(columns[0])

        ws.write(0, 0, columns[0], font_title)
        ws.write(row_num, 0, columns[1], font_zag)

        font_style = self.__settings_font("Times New Roman", 20 * 12, False, "no", "no")

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

    def get_export_service_list(self):
        response = HttpResponse(content_type="applications/ms-excel")
        date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
        response["Content-Disposition"] = "attachment; filename=ServiceList " + str(date) + ".xls"

        wb = xlwt.Workbook(encoding="utf-8")
        ws = wb.add_sheet("report")
        row_num = 1
        font_title = self.__settings_font("Times New Roman", 20 * 14, True, "yes", "yes")
        font_zag = self.__settings_font("Times New Roman", 20 * 12, False, "yes", "no")

        columns = [
            "Отчёт по услугам",
            "Услуги"
        ]

        len_service_use = len(columns[0])

        ws.write(0, 0, columns[0], font_title)
        ws.write(row_num, 0, columns[1], font_zag)

        font_style = self.__settings_font("Times New Roman", 20 * 12, False, "no", "no")

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

    def __get_erroneous_operations(self, erroneous_operations):
        return erroneous_operations.values_list(
            'bill',
            'date_e',
            'summ',
            'number_doc',
            'condition',
            'operation_desk',
            'operation_reg',
            'type_pay',
            'comment'
        )

    def __get_summ_money(self, summ_money):
        return summ_money.values_list(
            'cash_amount',
            'the_amount_of_corrective_operations'
        )

    def __get_view_pay(self, view_pay):
        return view_pay.values_list(
            'view',
            'pay'
        )

    def __get_decoding_of_desk_sections_and_tax_groups(self, decoding_of_desk_sections_and_tax_groups):
        return decoding_of_desk_sections_and_tax_groups.values_list(
            'tax_group',
            'desk_sections',
            'taxation_system',
            'count_operation',
            'summ'
        )

    def __get_additional_information_about_the_desk_register(self, additional_information_about_the_desk_register):
        return additional_information_about_the_desk_register.values_list(
            'date_a',
            'comment'
        )

    def get_export_desk_shift(self):
        response = HttpResponse(content_type="applications/ms-excel")
        date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
        response["Content-Disposition"] = "attachment; filename=DeskShift " + str(date) + ".xls"

        wb = xlwt.Workbook(encoding="utf-8")
        ws = wb.add_sheet("report")
        row_num = 1
        font_title = self.__settings_font("Times New Roman", 20 * 14, True, "yes", "yes")

        ws.write_merge(0, 0, 0, 8, "Z-Отчёт по кассе", font_title)

        font_zag = self.__settings_font("Times New Roman", 20 * 12, False, "yes", "no")

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

        font_style = self.__settings_font("Times New Roman", 20 * 12, False, "no", "no")

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

        row_num += 1
        ws.write_merge(row_num, row_num, 0, 8, "Ошибочные операции ФР", font_title)

        columns_3 = [
            "Счет",
            "Дата",
            "Сумма",
            "Номер док-та ФР",
            "Состояние",
            "Операция кассы",
            "Операция регистратора",
            "Тип оплаты",
            "Примечание"
        ]

        row_num += 1
        for col_num in range(len(columns_3)):
            ws.write(row_num, col_num, columns_3[col_num], font_zag)

        erroneous_operations = self.__get_erroneous_operations(ErroneousOperations.objects.all())
        rows = erroneous_operations

        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, str(row[col_num]), font_style)

        row_num += 1
        ws.write_merge(row_num, row_num, 0, 8, "", font_title)

        columns_4 = [
            "Сумма наличных",
            "Сумма исправительных операций"
        ]

        row_num += 1
        i = 0
        for col_num in range(len(columns_4)):
            i = col_num + 2
            ws.write(row_num, i, columns_4[col_num], font_zag)

        summ_money = self.__get_summ_money(SummMoney.objects.all())
        rows = summ_money

        for row in rows:
            row_num += 1
            i = 0
            for col_num in range(len(row)):
                i = col_num + 2
                ws.write(row_num, i, str(row[col_num]), font_style)

        row_num += 1
        ws.write_merge(row_num, row_num, 0, 8, "Оплаты (баланс)", font_title)

        columns_5 = [
            "Вид оплаты",
            "Сумма"
        ]

        row_num += 1
        i = 0
        for col_num in range(len(columns_5)):
            i = col_num + 2
            ws.write(row_num, i, columns_5[col_num], font_zag)

        view_pay = self.__get_view_pay(ViewPay.objects.all())
        rows = view_pay

        for row in rows:
            row_num += 1
            i = 0
            for col_num in range(len(row)):
                i = col_num + 2
                ws.write(row_num, i, str(row[col_num]), font_style)

        row_num += 1
        ws.write_merge(row_num, row_num, 0, 8, "Расшифровка кассовых секций и налоговых групп", font_title)

        columns_6 = [
            "Налоговая группа",
            "Кассовая секция",
            "Система налогообложения",
            "Кол-во операций",
            "Сумма"
        ]

        row_num += 1
        i = 0
        for col_num in range(len(columns_6)):
            i = col_num + 2
            ws.write(row_num, i, columns_6[col_num], font_zag)

        get_decoding_of_desk_sections_and_tax_groups = self.__get_decoding_of_desk_sections_and_tax_groups(
            DecodingOfDeskSectionsAndTaxGroups.objects.all())
        rows = get_decoding_of_desk_sections_and_tax_groups

        for row in rows:
            row_num += 1
            i = 0
            for col_num in range(len(row)):
                i = col_num + 2
                ws.write(row_num, i, str(row[col_num]), font_style)

        row_num += 1
        ws.write_merge(row_num, row_num, 0, 8, "Дополнительная информация о кассовом аппарате", font_title)

        additional_information_about_the_desk_register = self.__get_additional_information_about_the_desk_register(
            AdditionalInformationAboutTheDeskRegister.objects.all())
        rows = additional_information_about_the_desk_register

        for row in rows:
            row_num += 1
            ws.write_merge(row_num, row_num, 0, 1, str(row[0]), font_style)
            ws.write_merge(row_num, row_num, 2, 8, str(row[1]), font_style)

        wb.save(response)

        return response

    def __get_sale_ident(self, sale_ident):
        return sale_ident.values_list(
            'date_s',
            'type_s',
            'hardware_code',
            'user_code',
            'condition',
            'desk',
            'bill',
            'service',
            'price'
        )

    def get_export_sale_ident(self):
        response = HttpResponse(content_type="applications/ms-excel")
        date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
        response["Content-Disposition"] = "attachment; filename=SaleIdent " + str(date) + ".xls"

        wb = xlwt.Workbook(encoding="utf-8")
        ws = wb.add_sheet("report")
        row_num = 1
        font_title = self.__settings_font("Times New Roman", 20 * 14, True, "yes", "yes")

        ws.write_merge(0, 0, 0, 8, "Продажи идентификаторов за период", font_title)

        font_zag = self.__settings_font("Times New Roman", 20 * 12, False, "yes", "no")

        columns = [
            "Дата",
            "Тип",
            "Аппаратный код",
            "Пользовательский код",
            "Состояние",
            "Касса",
            "Счет",
            "Услуга",
            "Стоимость"
        ]

        len_date_s = len(columns[0])
        len_type_s = len(columns[1])
        len_hardware_code = len(columns[2])
        len_user_code = len(columns[3])
        len_condition = len(columns[4])
        len_desk = len(columns[5])
        len_bill = len(columns[6])
        len_service = len(columns[7])
        len_price = len(columns[8])

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_zag)

        font_style = self.__settings_font("Times New Roman", 20 * 12, False, "no", "no")

        sale_ident = self.__get_sale_ident(SaleIdent.objects.all())
        rows = sale_ident

        for i in sale_ident:
            if len_date_s < len(i[0]):
                len_date_s = len(i[0])
            if len_type_s < len(i[1]):
                len_type_s = len(i[1])
            if len_hardware_code < len(i[2]):
                len_hardware_code = len(i[2])
            if len_user_code < len(i[3]):
                len_user_code = len(i[3])
            if len_condition < len(i[4]):
                len_condition = len(i[4])
            if len_desk < len(i[5]):
                len_desk = len(i[5])
            if len_bill < len(i[6]):
                len_bill = len(i[6])
            if len_service < len(i[7]):
                len_service = len(i[7])
            if len_price < len(i[8]):
                len_price = len(i[8])

        width_col = [
            len_date_s,
            len_type_s,
            len_hardware_code,
            len_user_code,
            len_condition,
            len_desk,
            len_bill,
            len_service,
            len_price
        ]

        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.col(col_num).width = 256 * (int(width_col[col_num]) + 3)
                ws.write(row_num, col_num, str(row[col_num]), font_style)

        wb.save(response)

        return response

    def __get_sales_by_cat(self, sales_by_cat):
        return sales_by_cat.values_list(
            'code_name',
            'count',
            'summ',
            'discount',
            'all_s'
        )

    def get_export_sales_by_cat(self):
        response = HttpResponse(content_type="applications/ms-excel")
        date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
        response["Content-Disposition"] = "attachment; filename=SalesByCat " + str(date) + ".xls"

        wb = xlwt.Workbook(encoding="utf-8")
        ws = wb.add_sheet("report")
        row_num = 1
        font_title = self.__settings_font("Times New Roman", 20 * 14, True, "yes", "yes")

        ws.write_merge(0, 0, 0, 5, "Продажи с разбивкой по категориям", font_title)

        font_zag = self.__settings_font("Times New Roman", 20 * 12, False, "yes", "no")

        columns = [
            "Код",
            "Наименование",
            "Кол-во",
            "Сумма",
            "Скидка",
            "Всего"
        ]

        len_code_name = len(columns[0])
        len_count = len(columns[1])
        len_summ = len(columns[2])
        len_discount = len(columns[3])
        len_all_s = len(columns[4])

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_zag)

        font_style = self.__settings_font("Times New Roman", 20 * 12, False, "no", "no")

        sales_by_cat = self.__get_sales_by_cat(SalesByCat.objects.all())
        rows = sales_by_cat

        for i in sales_by_cat:
            if len_code_name < len(i[0]):
                len_code_name = len(i[0])
            if len_count < len(i[1]):
                len_count = len(i[1])
            if len_summ < len(i[2]):
                len_summ = len(i[2])
            if len_discount < len(i[3]):
                len_discount = len(i[3])
            if len_all_s < len(i[4]):
                len_all_s = len(i[4])

        width_col = [
            len_code_name,
            len_count,
            len_summ,
            len_discount,
            len_all_s
        ]

        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.col(col_num).width = 256 * (int(width_col[col_num]) + 3)
                ws.write(row_num, col_num+1, str(row[col_num]), font_style)

        wb.save(response)

        return response

    def __get_sales_by_positions_stat(self, sales_by_positions_stat):
        return sales_by_positions_stat.values_list(
            'service',
            'position',
            'price',
            'count',
            'summ'
        )

    def __get_in_total(self, in_total):
        return in_total.values_list(
            'count',
            'summ'
        )

    def get_export_sales_by_positions_stat(self):
        response = HttpResponse(content_type="applications/ms-excel")
        date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
        response["Content-Disposition"] = "attachment; filename=SalesByPositionsStat " + str(date) + ".xls"

        wb = xlwt.Workbook(encoding="utf-8")
        ws = wb.add_sheet("report")
        row_num = 1
        font_title = self.__settings_font("Times New Roman", 20 * 14, True, "yes", "yes")

        ws.write_merge(0, 0, 0, 4, "Продажи в разбивке по позициям в чеке", font_title)

        font_zag = self.__settings_font("Times New Roman", 20 * 12, False, "yes", "no")

        columns = [
            "Услуга",
            "Позиция",
            "Цена",
            "Кол-во",
            "Сумма",
        ]

        len_service = len(columns[0])
        len_position = len(columns[1])
        len_price = len(columns[2])
        len_count = len(columns[3])
        len_summ = len(columns[4])

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_zag)

        font_style = self.__settings_font("Times New Roman", 20 * 12, False, "no", "no")

        sales_by_positions_stat = self.__get_sales_by_positions_stat(SalesByPositionsStat.objects.all())
        rows = sales_by_positions_stat

        for i in sales_by_positions_stat:
            if len_service < len(i[0]):
                len_service = len(i[0])
            if len_position < len(i[1]):
                len_position = len(i[1])
            if len_price < len(i[2]):
                len_price = len(i[2])
            if len_count < len(i[3]):
                len_count = len(i[3])
            if len_summ < len(i[4]):
                len_summ = len(i[4])

        width_col = [
            len_service,
            len_position,
            len_price,
            len_count,
            len_summ
        ]

        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.col(col_num).width = 256 * (int(width_col[col_num]) + 3)
                ws.write(row_num, col_num, str(row[col_num]), font_style)

        in_total = self.__get_in_total(InTotal.objects.all())
        rows = in_total

        row_num += 1
        ws.write_merge(row_num, row_num, 0, 2, "ВСЕГО", font_style)

        for row in rows:
            for col_num in range(len(row)):
                ws.col(col_num).width = 256 * (int(width_col[col_num]) + 6)
                ws.write(row_num, col_num+3, str(row[col_num]), font_style)

        wb.save(response)

        return response

    def __get_sales_by_sno(self, sales_by_sno):
        return sales_by_sno.values_list(
            'code',
            'caption',
            'count',
            'summ',
            'discount'
        )

    def get_export_sales_by_sno(self):
        response = HttpResponse(content_type="applications/ms-excel")
        date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
        response["Content-Disposition"] = "attachment; filename=SalesBySNO " + str(date) + ".xls"

        wb = xlwt.Workbook(encoding="utf-8")
        ws = wb.add_sheet("report")
        row_num = 1
        font_title = self.__settings_font("Times New Roman", 20 * 14, True, "yes", "yes")

        ws.write_merge(0, 0, 0, 5, "Продажи с разбивкой по СНО", font_title)

        font_zag = self.__settings_font("Times New Roman", 20 * 12, False, "yes", "no")

        columns = [
            "Код",
            "Наименование",
            "Кол-во",
            "Сумма",
            "Скидка",
            "Всего"
        ]

        len_code = len(columns[0])
        len_caption = len(columns[1])
        len_count = len(columns[2])
        len_summ = len(columns[3])
        len_discount = len(columns[4])
        len_all_s = len(columns[5])

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_zag)

        font_style = self.__settings_font("Times New Roman", 20 * 12, False, "no", "no")

        sales_by_sno = self.__get_sales_by_sno(SalesBySno.objects.all())
        rows = sales_by_sno

        for i in sales_by_sno:
            if len_code < len(i[0]):
                len_code = len(i[0])
            if len_caption < len(i[1]):
                len_caption = len(i[1])
            if len_count < len(i[2]):
                len_count = len(i[2])
            if len_summ < len(i[3]):
                len_summ = len(i[3])
            if len_discount < len(i[4]):
                len_discount = len(i[4])

        width_col = [
            len_code,
            len_caption,
            len_count,
            len_summ,
            len_discount,
            len_all_s
        ]

        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.col(col_num).width = 256 * (int(width_col[col_num]) + 3)
                ws.write(row_num, col_num+1, str(row[col_num]), font_style)

        wb.save(response)

        return response

    def __get_ident_sales_stat(self, ident_sales_stat):
        return ident_sales_stat.values_list(
            'price',
            'count',
            'summ'
        )

    def get_export_ident_sales_stat(self):
        response = HttpResponse(content_type="applications/ms-excel")
        date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
        response["Content-Disposition"] = "attachment; filename=IdentSalesStat " + str(date) + ".xls"

        wb = xlwt.Workbook(encoding="utf-8")
        ws = wb.add_sheet("report")
        row_num = 1
        font_title = self.__settings_font("Times New Roman", 20 * 14, True, "yes", "yes")

        ws.write_merge(0, 0, 0, 5, "Продажи идентификаторов по тарифам", font_title)

        font_zag = self.__settings_font("Times New Roman", 20 * 12, False, "yes", "no")

        columns = [
            "Код",
            "Наименование",
            "Тариф",
            "Цена",
            "Кол-во",
            "Сумма"
        ]

        len_price = len(columns[3])
        len_count = len(columns[4])
        len_summ = len(columns[5])

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_zag)

        font_style = self.__settings_font("Times New Roman", 20 * 12, False, "no", "no")

        ident_sales_stat = self.__get_ident_sales_stat(IdentSalesStat.objects.all())
        rows = ident_sales_stat

        for i in ident_sales_stat:
            if len_price < len(i[0]):
                len_price = len(i[0])
            if len_count < len(i[1]):
                len_count = len(i[1])
            if len_summ < len(i[2]):
                len_summ = len(i[2])

        width_col = [
            len_price,
            len_count,
            len_summ
        ]

        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.col(col_num).width = 256 * (int(width_col[col_num]) + 12)
                ws.write(row_num, col_num + 3, str(row[col_num]), font_style)

        wb.save(response)

        return response

    def __get_ident_sales_by_tariff(self, ident_sales_by_tariff):
        return ident_sales_by_tariff.values_list(
            'tariff',
            'limit',
            'used',
            'remains'
        )

    def get_export_ident_sales_by_tariff(self):
        response = HttpResponse(content_type="applications/ms-excel")
        date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
        response["Content-Disposition"] = "attachment; filename=IdentSalesByTariff " + str(date) + ".xls"

        wb = xlwt.Workbook(encoding="utf-8")
        ws = wb.add_sheet("report")
        row_num = 1
        font_title = self.__settings_font("Times New Roman", 20 * 14, True, "yes", "yes")

        ws.write_merge(0, 0, 0, 3, "Количество проданных карт", font_title)

        font_zag = self.__settings_font("Times New Roman", 20 * 12, False, "yes", "no")

        columns = [
            "Тариф",
            "Лимит",
            "Использовано",
            "Остаток"
        ]

        len_tariff = len(columns[0])
        len_limit = len(columns[1])
        len_used = len(columns[2])
        len_remains = len(columns[3])

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_zag)

        font_style = self.__settings_font("Times New Roman", 20 * 12, False, "no", "no")

        ident_sales_by_tariff = self.__get_ident_sales_by_tariff(IdentSalesByTariff.objects.all())
        rows = ident_sales_by_tariff

        for i in ident_sales_by_tariff:
            if len_tariff < len(i[0]):
                len_tariff = len(i[0])
            if len_limit < len(i[1]):
                len_limit = len(i[1])
            if len_used < len(i[2]):
                len_used = len(i[2])
            if len_remains < len(i[3]):
                len_remains = len(i[3])

        width_col = [
            len_tariff,
            len_limit,
            len_used,
            len_remains
        ]

        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.col(col_num).width = 256 * (int(width_col[col_num]) + 3)
                ws.write(row_num, col_num, str(row[col_num]), font_style)

        wb.save(response)

        return response
