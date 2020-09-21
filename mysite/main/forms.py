from django import forms
from myapp.models import Form  # models.py


class Form(forms.ModelForm):
    class Meta:
        model = Form
        fields = "__all__"
