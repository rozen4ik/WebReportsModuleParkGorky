import fdb
from django.shortcuts import render


def index(request):
    # con = fdb.connect(dsn='213.208.176.194:55577:/path/db_asterisk.fdb', user='sysdba', password='masterkey',
    #                   charset='UTF8')
    # cur = con.cursor()
    #
    # tables = get_tables_fir(cur)
    #
    # con.closed()

    data = {
        # "tables": tables
    }

    return render(request, "reports/index.html", data)


def get_tables_fir(cur):
    return cur.execute("show table")
