import dataclasses

import pytest

from tallyhold.domain.models.definition_field import DefinitionField
from tallyhold.domain.models.type_field import TypeField


def create_field(name="tax_number", label="Vergi No"):
    return DefinitionField(name=name, label=label, type_field=TypeField.TAX_NUMBER_TR)


def test_valid_field_is_created():
    field = create_field()
    assert field.name == "tax_number"
    assert field.label == "Vergi No"
    assert field.is_required is False


@pytest.mark.parametrize("name", ["a", "tax_number", "phone_2", "a" * 63])
def test_valid_names_are_accepted(name):
    assert create_field(name=name).name == name


@pytest.mark.parametrize(
    "name",
    [
        "",
        "Vergi No",
        "TaxNumber",
        "tax number",
        "tax-number",
        "1phone",
        "_id",
        "vergi_no_ş",
        "a" * 64,
    ],
)
def test_invalid_names_are_rejected(name):
    with pytest.raises(ValueError, match="Invalid field name"):
        create_field(name=name)


@pytest.mark.parametrize("label", ["", "   "])
def test_empty_label_is_rejected(label):
    with pytest.raises(ValueError, match="label cannot be empty"):
        create_field(label=label)


def test_field_is_immutable():
    field = create_field()
    with pytest.raises(dataclasses.FrozenInstanceError):
        field.label = "Başka"