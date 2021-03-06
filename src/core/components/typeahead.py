from django_unicorn.components import UnicornView

from core.models import User


class TypeaheadView(UnicornView):
    state = ""

    ALL_STATES = (
        "Alabama",
        "Alaska",
        "Arizona",
        "Arkansas",
        "California",
        "Colorado",
        "Connecticut",
        "Delaware",
        "Florida",
        "Georgia",
        "Hawaii",
        "Idaho",
        "Illinois",
        "Indiana",
        "Iowa",
        "Kansas",
        "Kentucky",
        "Louisiana",
        "Maine",
        "Maryland",
        "Massachusetts",
        "Michigan",
        "Minnesota",
        "Mississippi",
        "Missouri",
        "Montana",
        "Nebraska",
        "Nevada",
        "New Hampshire",
        "New Jersey",
        "New Mexico",
        "New York",
        "North Carolina",
        "North Dakota",
        "Ohio",
        "Oklahoma",
        "Oregon",
        "Pennsylvania",
        "Rhode Island",
        "South Carolina",
        "South Dakota",
        "Tennessee",
        "Texas",
        "Utah",
        "Vermont",
        "Virginia",
        "Washington",
        "West Virginia",
        "Wisconsin",
        "Wyoming",
    )

    def clear_states(self):
        self.state = ""

    def states(self):
        if not self.state:
            return []
        return User.objects.filter(username__icontains=self.state.lower()).values('username', 'email')
        return [u.username for u in User.objects.all() if u.username.startswith(self.state.lower())]
        return [s for s in self.ALL_STATES if s.lower().startswith(self.state.lower())]

    class Meta:
        exclude = ("ALL_STATES",)
