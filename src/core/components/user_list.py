from django_unicorn.components import UnicornView
from django.utils import timezone

from core.models import User


class UserListView(UnicornView):
    current_time = timezone.now()
    users = User.objects.none()
    steps = (
        '1_first',
        '2_second',
        '3_third',
        '4_forth',
    )

    # def mount(self):
    #     self.users = User.objects.all()

    def hydrate(self):
        self.users = User.objects.all().values('username', 'email')
        self.current_time = timezone.now()
