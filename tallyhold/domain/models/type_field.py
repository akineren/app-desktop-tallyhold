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