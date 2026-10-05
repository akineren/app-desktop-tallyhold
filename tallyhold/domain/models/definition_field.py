from dataclasses import dataclass

from tallyhold.domain.models.type_field import TypeField


@dataclass(frozen=True)
class DefinitionField:
    name: str
    label: str
    type_field: TypeField
    is_required: bool = False