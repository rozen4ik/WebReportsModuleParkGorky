class ReportXLS:
    def get_stat_bill(self, kontur):
        return kontur.values_list(
            "date_bill",
            "id_ticket",
            "tariff",
            "ticket_validity_date",
            "date_of_ticket_passage",
        )

    def get_passage(self, passages_turnstile):
        return passages_turnstile.values_list(
            'resolution_timestamp',
            'id_point',
            'id_ter_from',
            'id_ter_to',
            'identifier_value',
        )

    def get_rule_list(self, rule_list):
        return rule_list.values_list(
            'rule_use',
        )