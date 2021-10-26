from django.utils.functional import cached_property
from django.http import HttpResponseRedirect
from django_unicorn.components import UnicornView, LocationUpdate


class StepperView(UnicornView):
    steps = (
        'step_1',
        'step_2',
        'step_3',
        'step_4',
        'step_5',
    )
    current_step_index = 0

    class Meta:
        javascript_exclude = (
            'steps', 'current_step_index',
            'has_next_step', 'has_previous_step', 'total_steps',
        )

    def mount(self):
        s = self.request.GET.get('s', '1')
        if s.isdigit() and 0 < int(s) < self.total_steps + 1:
            self.current_step_index = int(s) - 1

    @cached_property
    def total_steps(self):
        return len(self.steps)

    @property
    def has_next_step(self):
        return self.current_step_index < self.total_steps - 1

    @property
    def has_previous_step(self):
        return self.current_step_index > 0

    def get_current_step(self):
        return self.steps[self.current_step_index]


    def get_current_step_location_update(self):
        return LocationUpdate(
                HttpResponseRedirect(
                    f'?s={self.current_step_index+1}'))

    def goto_next_step(self):
        if self.has_next_step:
            self.current_step_index += 1
            return self.get_current_step_location_update()

    def goto_previous_step(self):
        if self.has_previous_step:
            self.current_step_index -= 1
            return self.get_current_step_location_update()

    def set_step_index(self, index: int):
        if 0 <= index < self.total_steps:
            self.current_step_index = index
            return self.get_current_step_location_update()
