__author__ = 'mehmet'

from django import forms
from tenGag.models import CommentInfo
from tenGag.models import Gag


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentInfo
        fields = ['commentContent']


class GagForm(forms.ModelForm):
    class Meta:
        model = Gag
        fields = ['title', 'image']