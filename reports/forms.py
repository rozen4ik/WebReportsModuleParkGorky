from django import forms
from reports.models import *

d = DeskItems.objects.all()
desk_l = []

for i in d:
    desk_l.append((f"{i.name}", f"{i.name}"))

desk_l = tuple(desk_l)

i_t = IdentTypes.objects.all()
ident_type_l = []

for i in i_t:
    ident_type_l.append((f"{i.caption}", f"{i.caption}"))

ident_type_l = tuple(ident_type_l)

tariff = TariffTypes.objects.all()
tariff_l = []

for i in tariff:
    tariff_l.append((f"{i.name}", f"{i.name}"))

tariff_l = tuple(tariff_l)


class TicketSales(forms.Form):
    start_date = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                "class": "form-control datetimepicker-input",
                "type": "date"
            },
        )
    )

    end_date = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                "class": "form-control datetimepicker-input",
                "type": "date"
            },
        )
    )


class DeskForms(forms.Form):
    desk = forms.ChoiceField(
        required=False,
        widget=forms.Select(
            attrs={
                "class": "form-select"
            }
        ),
        choices=desk_l,
    )


class IdentTypesForms(forms.Form):
    ident_types = forms.ChoiceField(
        required=False,
        widget=forms.Select(
            attrs={
                "class": "form-select"
            }
        ),
        choices=ident_type_l
    )

    start_date = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                "class": "form-control datetimepicker-input",
                "type": "date"
            },
        )
    )

    end_date = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                "class": "form-control datetimepicker-input",
                "type": "date"
            },
        )
    )


class TariffTypesForms(forms.Form):
    tariff_types = forms.ChoiceField(
        required=False,
        widget=forms.Select(
            attrs={
                "class": "form-select"
            }
        ),
        choices=tariff_l
    )

    start_date = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                "class": "form-control datetimepicker-input",
                "type": "date"
            },
        )
    )

    end_date = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                "class": "form-control datetimepicker-input",
                "type": "date"
            },
        )
    )


class TariffTimesForm(forms.Form):
    tariff_start = forms.ChoiceField(
        required=False,
        widget=forms.Select(
            attrs={
                "class": "form-select"
            }
        ),
        choices=tariff_l
    )

    tariff_stop = forms.ChoiceField(
        required=False,
        widget=forms.Select(
            attrs={
                "class": "form-select"
            }
        ),
        choices=tariff_l
    )

    start_date = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                "class": "form-control datetimepicker-input",
                "type": "date"
            },
        )
    )

    end_date = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                "class": "form-control datetimepicker-input",
                "type": "date"
            },
        )
    )
