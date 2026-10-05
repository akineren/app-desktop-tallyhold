import re

_PATTERN_IDENTIFIER = re.compile(r"[a-z][a-z0-9_]{0,62}")


def is_valid_identifier(value: str) -> bool:
    return _PATTERN_IDENTIFIER.fullmatch(value) is not None