import fdb
import pymysql
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render
from sshtunnel import SSHTunnelForwarder
from bs4 import BeautifulSoup
from reports.forms import TicketSales
from reports.models import Kontur, Baloon


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
        access = get_access(request)
        page_number = request.GET.get("page")
        ticket_form = TicketSales(request.GET)
        start_d = "01.01.01"
        end_d = "01.01.01"
        fo = ""

        if ticket_form.is_valid():
            filter_ticket = ticket_form.cleaned_data
            start_d = ticket_form.cleaned_data["start_date"]
            end_d = ticket_form.cleaned_data["end_date"]

            if filter_ticket != {'start_date': None, 'end_date': None}:
                fo = "yes"
                con = fdb.connect(dsn='213.208.176.194/43050:spd_showmaket', user='sysdba', password='masterkey',
                                  charset="win1251")
                cur = con.cursor()

                tables = cur.execute(
                    "select "
                    "* "
                    "from "
                    f"HTML2$ARN_SALE_STATS('{start_d}', '{end_d}') "
                ).fetchall()

                con.commit()
                con.close()

                st = ""
                for i in tables:
                    st += f"{i[0]}"

                st = st.replace("charset=windows-1251", "charset=utf-8")
                with open('result_scan_req.html', 'w') as output_file:
                    output_file.write(st)

                with open("result_scan_req.html") as fp:
                    soup = BeautifulSoup(fp, "lxml")

                trs = soup.find_all('table')[1].find_all('tr')

                pars_table(trs, 'td')

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

                    cur.execute(
                        "SELECT "
                        "DateArc, code, permanent_rulename "
                        "FROM "
                        "Identifier "
                        f"WHERE DateArc >= '{start_d}' and DateArc <= '{end_d}'"
                    )

                    result = cur.fetchall()
                    con.close()

                    baloon = Baloon.objects.all().delete()

                    for i in result:
                        baloon = Baloon()
                        dt = i[0].strftime("%d.%m.%Y %H:%M")
                        baloon.date_bill = dt
                        baloon.id_ticket = i[1]
                        baloon.tariff = f"{i[2]} [C]"
                        baloon.save()

                    baloon = Baloon.objects.all().order_by("date_bill")
                    kontur = Kontur.objects.all().order_by("date_bill")

                    for b in baloon:
                        filt = kontur.filter(id_ticket=b.id_ticket)
                        if not filt:
                            kor = Kontur()
                            kor.date_bill = b.date_bill
                            kor.id_ticket = b.id_ticket
                            kor.tariff = b.tariff
                            kor.ticket_validity_date = ""
                            kor.date_of_ticket_passage = ""
                            kor.save()
                        else:
                            continue

            kontur = Kontur.objects.all().order_by("date_bill")
            page_model = Paginator(kontur, 20)
            page_m = page_model.get_page(page_number)

            data = {
                "ticket_form": ticket_form,
                "fo": fo,
                "page_m": page_m,
                "access": access
            }
        else:
            data = {}
        return render(request, "reports/result_ticket_sales.html", data)


def passages_through_turnstiles(request):
    if request.user.is_authenticated:
        access = get_access(request)
        data = {
            "access": access
        }
    else:
        data = {}
    return render(request, "reports/passages_throw_turnstiles.html", data)


def get_access(request):
    if request.user.is_authenticated:
        user = User.objects.all().select_related('profile')
        access = ""
        if request.user.profile.position_id_id == 1:
            access = "yes"
        else:
            access = "no"
        return access


def pars_table(trs, tag):
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
