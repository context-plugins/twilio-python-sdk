from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BrandRegistrationsEnumBrandFeedback(str, Enum):
    """DEPRECATED. Feedback on how to improve brand score"""

    TAX_ID = "TAX_ID"
    STOCK_SYMBOL = "STOCK_SYMBOL"
    NONPROFIT = "NONPROFIT"
    GOVERNMENT_ENTITY = "GOVERNMENT_ENTITY"
    OTHERS = "OTHERS"

    __str__ = str.__str__


BrandRegistrationsEnumBrandFeedbackOrStr: TypeAlias = Annotated[
    BrandRegistrationsEnumBrandFeedback | str, open_enum_validator(BrandRegistrationsEnumBrandFeedback)
]
