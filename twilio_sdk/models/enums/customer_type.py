from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CustomerType(str, Enum):
    """The type of customer account in the losing carrier. This should either be: 'Individual' or 'Business'., The type
    of End User the regulation requires - can be ``Individual`` or ``Business``."""

    BUSINESS = "Business"
    INDIVIDUAL = "Individual"

    __str__ = str.__str__


CustomerTypeOrStr: TypeAlias = Annotated[CustomerType | str, open_enum_validator(CustomerType)]
