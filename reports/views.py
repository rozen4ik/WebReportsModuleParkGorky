import fdb
from django.core.paginator import Paginator
from django.shortcuts import render


def index(request):
    page_number = request.GET.get("page")
    con = fdb.connect(dsn='213.208.176.194/43050:volen', user='sysdba', password='masterkey',
                      charset="win1251")
    cur = con.cursor()
    tables = cur.execute('select ID_DESK, ID_BILL, DATE_CHANGE, OPERATION_SUM from "DESK$OPERATIONS"').fetchall()
    page_model = Paginator(tables, 10)
    page_m = page_model.get_page(page_number)


    # for t in tables:
    #     print(t)

    con.commit()

    con.close()
    data = {
        "tables": tables,
        "page_m": page_m
    }

    return render(request, "reports/index.html", data)


def get_table_desk_items(cur):
    return cur.execute('select * from "DESK$ITEMS"')
