from django_unicorn.components import UnicornView

from .. import forms, models


class AddUserView(UnicornView):
    form_class = forms.UserAddForm

    email = ''
    username = ''
    password = ''
    password_confirm = ''

    class Meta:
        javascript_exclude = (
            'save_user',
        )

    def save_user(self):
        if self.is_valid():
            user = models.User.objects.create(
                username=self.username,
                email=self.email,
                )
            user.set_password(self.password)
            user.save()

            self.email = ''
            self.username = ''
            self.password = ''
            self.password_confirm = ''

