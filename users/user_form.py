from django import forms

import users


class user_form(forms.ModelForm):
    class Meta:
        model = users
        fields = "__all__"
