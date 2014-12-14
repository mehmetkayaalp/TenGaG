__author__ = 'mehmet'

from django import forms
from tenGag.models import CommentInfo


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentInfo
        fields = ['commentName']