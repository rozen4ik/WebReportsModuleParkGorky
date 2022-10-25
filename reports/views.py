import fdb
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render

from reports.forms import TicketSales


def index(request):
    data = {
    }

    return render(request, "reports/index.html", data)


def ticket_sales(request):
    page_number = request.GET.get("page")
    ticket_form = TicketSales(request.GET)
    start_d = "01.01.01"
    end_d = "01.01.01"
    fo = ""
    tables = ""

    if ticket_form.is_valid():
        filter_ticket = ticket_form.cleaned_data
        start_d = ticket_form.cleaned_data["start_date"]
        end_d = ticket_form.cleaned_data["end_date"]

        print(filter_ticket)
        print(start_d)
        print(end_d)

        if filter_ticket != {'start_date': None, 'end_date': None}:
            fo = "yes"
            con = fdb.connect(dsn='213.208.176.194/43050:volen', user='sysdba', password='masterkey',
                              charset="win1251")
            cur = con.cursor()
            tables = cur.execute('select ID_DESK, ID_BILL, DATE_CHANGE, OPERATION_SUM from "DESK$OPERATIONS" where DATE_CHANGE >= (?) and DATE_CHANGE <= (?)',(start_d, end_d)).fetchall()
            con.commit()
            con.close()

        page_model = Paginator(tables, 10)
        page_m = page_model.get_page(page_number)

        data = {
            "ticket_form": ticket_form,
            "tables": tables,
            "fo": fo,
            "page_m": page_m
        }

        return render(request, "reports/result_ticket_sales.html", data)


def passages_through_turnstiles(request):
    pass
