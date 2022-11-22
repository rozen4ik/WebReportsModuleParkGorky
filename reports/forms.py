from django import forms
from reports.models import DeskItems

d = DeskItems.objects.all()
desk_l = []

for i in d:
    desk_l.append((f"{i.name}", f"{i.name}"))

desk_l = tuple(desk_l)



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
