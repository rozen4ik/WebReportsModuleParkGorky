class ReportXLS:
    def get_stat_bill(self, kontur):
        return kontur.values_list(
            "date_bill",
            "id_ticket",
            "tariff",
            "ticket_validity_date",
            "date_of_ticket_passage",
        )
