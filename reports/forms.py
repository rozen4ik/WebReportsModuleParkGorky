from django import forms


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
