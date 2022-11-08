import fdb
import pymysql
from django.core.paginator import Paginator
from django.shortcuts import render
from sshtunnel import SSHTunnelForwarder

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
    r = ""

    if ticket_form.is_valid():
        filter_ticket = ticket_form.cleaned_data
        start_d = ticket_form.cleaned_data["start_date"]
        end_d = ticket_form.cleaned_data["end_date"]

        print(filter_ticket)
        print(start_d)
        print(end_d)

        if filter_ticket != {'start_date': None, 'end_date': None}:
            fo = "yes"
            con = fdb.connect(dsn='213.208.176.194/43050:spd_showmaket', user='sysdba', password='masterkey',
                              charset="win1251")
            cur = con.cursor()

            # Вывод всех таблиц

            # r = cur.execute('SELECT '
            #                 'a.RDB$RELATION_NAME '
            #                 'FROM RDB$RELATIONS a '
            #                 'WHERE COALESCE(RDB$SYSTEM_FLAG, 0) = 0 AND RDB$RELATION_TYPE = 0'
            #                 ).fetchall()

            tables = cur.execute(
                "select "
                "* "
                "from EMP$TIMESHEETS "
                # "where OPERATION_TIMESTAMP >= '2022-10-27 00:00:00';"
            ).fetchall()

            # Вывод всех столбцов

            r = cur.execute(
                "select "
                "rdb$field_name "
                "from rdb$relation_fields "
                "where rdb$relation_name = 'EMP$TIMESHEETS ';"
            ).fetchall()

            for i in tables:
                print(i)

            for i in r:
                print(i)

            con.commit()
            con.close()

        page_model = Paginator(tables, 10)
        page_m = page_model.get_page(page_number)

        data = {
            "ticket_form": ticket_form,
            "fo": fo,
            "page_m": page_m,
            "r": r
        }

        return render(request, "reports/result_ticket_sales.html", data)


def passages_through_turnstiles(request):
    page_number = request.GET.get("page")
    result = ""
    with SSHTunnelForwarder(
            ('5.253.62.211', 22),
            ssh_password="5hz2Q6Z5RX82YfqlnS",
            ssh_username="root",
            remote_bind_address=('127.0.0.1', 3306)) as server:
        con = None

        con = pymysql.connect(
            user='mikhailrozenberg',
            passwd='Rozen_9635352',
            db='baloon',
            host='127.0.0.1',
            port=server.local_bind_port
        )

        cur = con.cursor()

        cur.execute("SELECT personid, name, permanent_rulename, clientoid, status, comment, DateArc FROM Identifier")
        result = cur.fetchall()

        con.close()

    page_model = Paginator(result, 10)
    page_m = page_model.get_page(page_number)

    data = {
        "page_m": page_m
    }

    return render(request, "reports/passages_throw_turnstiles.html", data)
