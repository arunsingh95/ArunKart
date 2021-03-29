from django.forms import forms
from mykart.models import UserDetail


class UserDetailsForm(forms.Form):

    class Meta:
        model = UserDetail
        fields = "__all__"
