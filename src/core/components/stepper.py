from django.utils.functional import cached_property
from django_unicorn.components import UnicornView


class StepperView(UnicornView):
    steps = (
        'step_1',
        'step_2',
        'step_3',
        'step_4',
    )
    current_step_index = 0

    class Meta:
        javascript_exclude = (
            'has_next_step', 'has_previous_step',
        )

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

    def goto_next_step(self):
        if self.has_next_step:
            self.current_step_index += 1

    def goto_previous_step(self):
        if self.has_previous_step:
            self.current_step_index -= 1

    def set_step_index(self, index: int):
        if 0 <= index < self.total_steps:
            self.current_step_index = index
