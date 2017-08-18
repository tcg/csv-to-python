from django import forms


class CsvPasteForm(forms.Form):
    csv_data = forms.CharField(widget=forms.Textarea, label='CSV Data', max_length=5000)
    has_headers = forms.BooleanField(label="First row of data is headers?", required=False)
