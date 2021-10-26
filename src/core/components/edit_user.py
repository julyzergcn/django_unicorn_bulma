from django.shortcuts import get_object_or_404
from django_unicorn.components import UnicornView

from .. import forms, models


class EditUserView(UnicornView):
    form_class = forms.UserEditForm

    email = ''
    first_name = ''
    last_name = ''

    class Meta:
        javascript_exclude = (
            'save_user',
        )

    def mount(self):
        if getattr(self, 'user_id', ''):
            self.user = get_object_or_404(models.User, id=self.user_id)
            self.email = self.user.email
            self.first_name = self.user.first_name
            self.last_name = self.user.last_name

    def save_user(self):
        # self.validate()
        if self.is_valid() and getattr(self, 'user', ''):
            self.user.email = self.email
            self.user.first_name = self.first_name
            self.user.last_name = self.last_name
            self.user.save()
