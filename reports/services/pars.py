import re
from bs4 import BeautifulSoup
from reports.models import Kontur, RuleList, ServiceList


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
