from django_unicorn.components import UnicornView
from django_unicorn.components.typing import QuerySetType
from core.models import User


class UserListView(UnicornView):
    users : QuerySetType
    steps = (
        '1_first',
        '2_second',
        '3_third',
        '4_forth',
    )

    def mount(self):
        self.users = User.objects.all()
