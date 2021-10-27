from django_unicorn.components import UnicornView

from core.models import User


class UserListView(UnicornView):
    users = User.objects.none()

    # def mount(self):
    #     self.users = User.objects.all()

    def hydrate(self):
        self.users = User.objects.all().values(
            'id', 'username', 'email', 'first_name', 'last_name')

