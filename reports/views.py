from django.contrib.auth.models import User
from django.shortcuts import render
from reports.services.report import Report
from reports.services.report_xls import ReportXLS


def index(request):
    if request.user.is_authenticated:
        access = get_access(request)
        data = {
            "access": access
        }
    else:
        data = {}
    return render(request, "reports/index.html", data)


def ticket_sales(request):
    if request.user.is_authenticated:
        report = Report()
        data = report.get_ticket(request)
    else:
        data = {}
    return render(request, "reports/result_ticket_sales.html", data)


def passages_through_turnstiles(request):
    if request.user.is_authenticated:
        report = Report()
        data = report.get_passages_through_turnstiles(request)
    else:
        data = {}
    return render(request, "reports/result_passage.html", data)


def rule_list(request):
    if request.user.is_authenticated:
        report = Report()
        data = report.get_rule_list(request)
    else:
        data = {}
    return render(request, "reports/rule_list.html", data)


def service_list(request):
    if request.user.is_authenticated:
        report = Report()
        data = report.get_service_list(request)
    else:
        data = {}
    return render(request, "reports/service_list.html", data)


def desk_shift(request):
    if request.user.is_authenticated:
        report = Report()
        data = report.get_desk_shift(request)
    else:
        data = {}
    return render(request, "reports/result_desk_shift.html", data)


def sale_ident(request):
    if request.user.is_authenticated:
        report = Report()
        data = report.get_sale_ident(request)
    else:
        data = {}
    return render(request, "reports/result_sale_ident.html", data)


def sales_by_cat(request):
    if request.user.is_authenticated:
        report = Report()
        data = report.get_sales_by_cat(request)
    else:
        data = {}
    return render(request, "reports/result_sales_by_cat.html", data)


def sales_by_positions_stat(request):
    if request.user.is_authenticated:
        report = Report()
        data = report.get_sales_by_positions_stat(request)
    else:
        data = {}
    return render(request, "reports/result_sales_by_positions_stat.html", data)


def sales_by_sno(request):
    if request.user.is_authenticated:
        report = Report()
        data = report.get_sales_by_sno(request)
    else:
        data = {}
    return render(request, "reports/result_sales_by_sno.html", data)


def ident_sales_stat(request):
    if request.user.is_authenticated:
        report = Report()
        data = report.get_ident_sales_stat(request)
    else:
        data = {}
    return render(request, "reports/result_ident_sales_stat.html", data)


def ident_sales_by_tariff(request):
    if request.user.is_authenticated:
        report = Report()
        data = report.get_ident_sales_by_tariff(request)
    else:
        data = {}
    return render(request, "reports/result_ident_sales_by_tariff.html", data)


def get_access(request):
    if request.user.is_authenticated:
        user = User.objects.all().select_related('profile')
        access = ""
        if request.user.profile.position_id_id == 1:
            access = "yes"
        else:
            access = "no"
        return access


def export_stat_bill(request):
    report_xls = ReportXLS()
    response = report_xls.get_export_stat_bill()
    return response


def export_passage(request):
    report_xls = ReportXLS()
    response = report_xls.get_export_passage()
    return response


def export_rule_list(request):
    report_xls = ReportXLS()
    response = report_xls.get_export_rule_list()
    return response


def export_service_list(request):
    report_xls = ReportXLS()
    response = report_xls.get_export_service_list()
    return response


def export_desk_shift(request):
    report_xls = ReportXLS()
    response = report_xls.get_export_desk_shift()
    return response


def export_sale_ident(request):
    report_xls = ReportXLS()
    response = report_xls.get_export_sale_ident()
    return response


def export_sales_by_cat(request):
    report_xls = ReportXLS()
    response = report_xls.get_export_sales_by_cat()
    return response


def export_sales_by_positions_stat(request):
    report_xls = ReportXLS()
    response = report_xls.get_export_sales_by_positions_stat()
    return response


def export_sales_by_sno(request):
    report_xls = ReportXLS()
    response = report_xls.get_export_sales_by_sno()
    return response


def export_ident_sales_stat(request):
    report_xls = ReportXLS()
    response = report_xls.get_export_ident_sales_stat()
    return response


def export_ident_sales_by_tariff(request):
    report_xls = ReportXLS()
    response = report_xls.get_export_ident_sales_by_tariff()
    return response
