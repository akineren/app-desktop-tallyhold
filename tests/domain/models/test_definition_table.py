import dataclasses

import pytest

from tallyhold.domain.models.definition_field import DefinitionField
from tallyhold.domain.models.definition_table import DefinitionTable
from tallyhold.domain.models.type_field import TypeField

FIELD_TAX_NUMBER = DefinitionField(
    name="tax_number", label="Vergi No", type_field=TypeField.TAX_NUMBER_TR
)


def create_table(name="customers", label="Müşteriler", fields=(FIELD_TAX_NUMBER,)):
    return DefinitionTable(name=name, label=label, fields=fields)


def test_valid_table_is_created():
    table = create_table()
    assert table.name == "customers"
    assert table.label == "Müşteriler"
    assert table.fields == (FIELD_TAX_NUMBER,)


@pytest.mark.parametrize(
    "name", ["", "Customers", "1customers", "_meta", "müşteriler"]
)
def test_invalid_names_are_rejected(name):
    with pytest.raises(ValueError, match="Invalid table name"):
        create_table(name=name)


def test_reserved_prefix_is_rejected():
    with pytest.raises(ValueError, match="reserved"):
        create_table(name="sqlite_customers")


@pytest.mark.parametrize("label", ["", "   "])
def test_empty_label_is_rejected(label):
    with pytest.raises(ValueError, match="Table label cannot be empty"):
        create_table(label=label)


def test_table_is_immutable():
    table = create_table()
    with pytest.raises(dataclasses.FrozenInstanceError):
        table.label = "Başka"

def test_table_without_fields_is_rejected():
    with pytest.raises(ValueError, match="at least one field"):
        create_table(fields=())


def test_duplicate_field_names_are_rejected():
    field_copy = DefinitionField(
        name="tax_number", label="VKN", type_field=TypeField.TEXT
    )
    with pytest.raises(ValueError, match="duplicate field names: tax_number"):
        create_table(fields=(FIELD_TAX_NUMBER, field_copy))


def test_fields_with_different_names_are_accepted():
    field_title = DefinitionField(name="title", label="Ünvan", type_field=TypeField.TEXT)
    table = create_table(fields=(FIELD_TAX_NUMBER, field_title))
    assert len(table.fields) == 2