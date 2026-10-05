from dataclasses import dataclass

from tallyhold.domain.models.identifier import is_valid_identifier
from tallyhold.domain.models.type_field import TypeField


@dataclass(frozen=True)
class DefinitionField:
    name: str
    label: str
    type_field: TypeField
    is_required: bool = False

    def __post_init__(self) -> None:
        if not is_valid_identifier(self.name):
            raise ValueError(
                f"Invalid field name '{self.name}'. Use lowercase letters, digits "
                "and underscores, start with a letter, max 63 characters."
            )
        if not self.label.strip():
            raise ValueError("Field label cannot be empty.")