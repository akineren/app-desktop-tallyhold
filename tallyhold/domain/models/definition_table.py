from collections import Counter
from dataclasses import dataclass

from tallyhold.domain.models.definition_field import DefinitionField
from tallyhold.domain.models.identifier import is_valid_identifier

_PREFIX_RESERVED = "sqlite_"


@dataclass(frozen=True)
class DefinitionTable:
    name: str
    label: str
    fields: tuple[DefinitionField, ...]

    def __post_init__(self) -> None:
        if not is_valid_identifier(self.name):
            raise ValueError(
                f"Invalid table name '{self.name}'. Use lowercase letters, digits "
                "and underscores, start with a letter, max 63 characters."
            )
        if self.name.startswith(_PREFIX_RESERVED):
            raise ValueError(
                f"Invalid table name '{self.name}'. Names starting with "
                f"'{_PREFIX_RESERVED}' are reserved."
            )
        if not self.label.strip():
            raise ValueError("Table label cannot be empty.")
        if not self.fields:
            raise ValueError(f"Table '{self.name}' must have at least one field.")

        counts = Counter(field.name for field in self.fields)
        duplicates = sorted(name for name, count in counts.items() if count > 1)
        if duplicates:
            raise ValueError(
                f"Table '{self.name}' has duplicate field names: "
                f"{', '.join(duplicates)}."
            )