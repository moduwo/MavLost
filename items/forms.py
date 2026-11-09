from django import forms
from .models import Item

# form for Item model
class ItemForm(forms.ModelForm):
    # define form fields and widgets
    class Meta:
        model = Item
        fields = [
            'name',
            'description',
            'report_type',
            'location',
            'date_lost_or_found',
            'time_lost_or_found',
            'photo',
        ]

    # get time and date from browser
    widgets = {
        "date_lost_or_found": forms.DateInput(attrs={"type":"date"}), 
        "time_found": forms.TimeInput(attrs={"type":"time"}),
    }

