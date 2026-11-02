from dataclasses import dataclass

from .tea import Tea


@dataclass
class Catalog:
    teas: list[Tea]

    def filter(self, tea_type, profile):
        return [
            tea
            for tea in self.teas
            if (tea_type is None or tea.type == tea_type)
            and (profile is None or tea.profile == profile)
        ]

    def find(self, tea_id):
        return next((tea for tea in self.teas if tea.tea_id == tea_id), None)
