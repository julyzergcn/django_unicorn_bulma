from django import forms

from . import models


class UserAddForm(forms.ModelForm):
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = models.User
        fields = ('username', 'email', 'password')

    def clean_password_confirm(self):
        pwd = self.cleaned_data['password_confirm']
        if pwd != self.cleaned_data['password']:
            raise forms.ValidationError('Password mismatch.')
        return pwd


class UserEditForm(forms.ModelForm):

    class Meta:
        model = models.User
        fields = ('email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
