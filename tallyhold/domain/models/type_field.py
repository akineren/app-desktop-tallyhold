from enum import Enum


class TypeField(str, Enum):
    TEXT = "text"
    INTEGER = "integer"
    DECIMAL = "decimal"
    DATE = "date"
    BOOLEAN = "boolean"
    PHONE = "phone"
    EMAIL = "email"
    TAX_NUMBER_TR = "tax_number_tr"
    NATIONAL_ID_TR = "national_id_tr"

    @property
    def base_type(self) -> "TypeField":
        return _BASE_TYPES.get(self, self)


_BASE_TYPES = {
    TypeField.PHONE: TypeField.TEXT,
    TypeField.EMAIL: TypeField.TEXT,
    TypeField.TAX_NUMBER_TR: TypeField.TEXT,
    TypeField.NATIONAL_ID_TR: TypeField.TEXT,
}