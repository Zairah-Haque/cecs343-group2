from dataclasses import dataclass, field

from .tea import Tea


@dataclass
class ShoppingCart:
    teas: list[Tea] = field(default_factory=list)

    def add(self, tea):
        self.teas.append(tea)

    def remove(self, tea_id):
        for index, tea in enumerate(self.teas):
            if tea.tea_id == tea_id:
                del self.teas[index]
                return
