from django_unicorn.components import UnicornView

from core.models import User


class UserDetailView(UnicornView):
    user: User = None

    # def mount(self):
    #     self.user = 1
