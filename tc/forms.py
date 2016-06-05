# Copyright 2016 by Dane Collins
from __future__ import print_function
from __future__ import unicode_literals

from django import forms

from tc.models import TestSession, Comment


class TestInfoForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = TestSession
        fields = ['item_name', 'user', 'package_type', 'id']
        labels = {
            'item_name': 'Test Item Name',
            'user': 'Your Name'
        }
        widgets = {
            'package_type': forms.RadioSelect(attrs={'onchange': "change_image(1)"}),
            'id': forms.TextInput(attrs={'hidden': True})
        }


class MediaForm(forms.Form):
    docfile = forms.FileField(label='Select a file')


class CommentForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Comment
        fields = ['comment']
        labels = {
            'comment': 'Enter a comment'
        }
        widgets = {
            'comment': forms.Textarea(attrs={'cols': '50', 'rows': '4'}),
        }
