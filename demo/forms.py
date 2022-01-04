from django import forms
from . import models


class CreateNumberList(forms.ModelForm):
    class Meta:
        model = models.Demo
        fields = ['number_list']
