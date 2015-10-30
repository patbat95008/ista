from __future__ import print_function
from __future__ import unicode_literals

from django import forms

from tc.models import TestSession

class TestInfoForm(forms.ModelForm):
    required_css_class = 'required'
    class Meta:
        model = TestSession
        fields = ['item_name', 'user', 'package_type', 'id']
        labels = {
            'item_name': ('Item Name'),
            'user': ('Your Name')
        }
        widgets = {
            'package_type': forms.RadioSelect(),
            'id': forms.TextInput(attrs={'hidden': True})
        }
