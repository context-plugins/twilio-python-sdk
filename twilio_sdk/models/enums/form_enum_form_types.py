from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FormEnumFormTypes(str, Enum):
    """The Type of this Form. Currently only ``form-push`` is supported."""

    FORM_PUSH = "form-push"

    __str__ = str.__str__


FormEnumFormTypesOrStr: TypeAlias = Annotated[FormEnumFormTypes | str, open_enum_validator(FormEnumFormTypes)]
