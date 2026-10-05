from tallyhold.domain.models.type_field import TypeField

BASE_TYPES = {
    TypeField.TEXT,
    TypeField.INTEGER,
    TypeField.DECIMAL,
    TypeField.DATE,
    TypeField.BOOLEAN,
}


def test_base_types_map_to_themselves():
    for type_field in BASE_TYPES:
        assert type_field.base_type is type_field


def test_every_type_maps_to_a_base_type():
    for type_field in TypeField:
        assert type_field.base_type in BASE_TYPES


def test_tax_number_is_stored_as_text():
    assert TypeField.TAX_NUMBER_TR.base_type is TypeField.TEXT