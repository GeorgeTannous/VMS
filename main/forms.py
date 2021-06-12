from django import forms
from django.forms import HiddenInput

from .models import vacations

class VacationForm(forms.ModelForm):

    user_name = forms.CharField(widget=forms.TextInput(
        attrs={'id': 'user', 'type': 'hidden', 'value': 'user'
               })
        , required=True)

    from_date_time = forms.CharField(widget=forms.TextInput(
        attrs={ 'id': 'fdate', 'type': 'text', 'class': 'form-control', 'placeholder': 'From Date & Time', 'data-parsley-required': 'true', 'data-parsley-required-message': 'Date is required'})
        , required=True)

    to_date_time = forms.CharField(widget=forms.TextInput(
        attrs={'id': 'tdate', 'type': 'text', 'class': 'form-control', 'placeholder': 'To Date & Time',
               'data-parsley-required': 'true', 'data-parsley-required-message': 'Date is required', 'data-parsley-mindate': '2015/01/01', 'data-date-format': 'YYYY/MM/DD'})
        , required=True)

    description = forms.ChoiceField(widget=forms.Select(
        attrs={ 'data-parsley-required': 'true', 'data-parsley-required-message': 'Vacation Type is required.'}),
        choices=([('', 'Select Value'), ('Annual Leave', 'Annual Leave'), ('Bereavement Leave', 'Bereavement Leave'), ('Medical Leave', 'Medical Leave'), ]), initial='', required=True, )

    class Meta:
        model = vacations
        fields = ('user_name', 'from_date_time', 'to_date_time', 'description')
        widgets = {
            # 'user_name': HiddenInput(),
        }
