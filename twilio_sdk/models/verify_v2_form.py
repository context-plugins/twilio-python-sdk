from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.form_enum_form_types import FormEnumFormTypesOrStr


class VerifyV2Form(SdkBaseModel):
    form_type: Optional[FormEnumFormTypesOrStr] = UNSET
    """The Type of this Form. Currently only ``form-push`` is supported."""

    forms: OptionalNullable[Any] = UNSET
    """Object that contains the available forms for this type. This available forms are given in the standard `JSON
    Schema <https://json-schema.org/>`__ format"""

    form_meta: OptionalNullable[Any] = UNSET
    """Additional information for the available forms for this type. E.g. The separator string used for ``binding`` in a
    Factor push."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The URL to access the forms for this type."""


class VerifyV2FormDict(TypedDict):
    form_type: NotRequired[FormEnumFormTypesOrStr]
    forms: NotRequired[Any | None]
    form_meta: NotRequired[Any | None]
    url: NotRequired[AnyUrl | None]
