from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .api_v2010_account_sip_sip_domain_sip_credential_list_mapping import (
    ApiV2010AccountSipSipDomainSipCredentialListMapping,
    ApiV2010AccountSipSipDomainSipCredentialListMappingDict,
)


class ListSipCredentialListMappingResponse(SdkBaseModel):
    end: Optional[int] = UNSET
    first_page_uri: Optional[str] = UNSET
    next_page_uri: OptionalNullable[str] = UNSET
    page: Optional[int] = UNSET
    page_size: Optional[int] = UNSET
    previous_page_uri: OptionalNullable[str] = UNSET
    start: Optional[int] = UNSET
    uri: Optional[str] = UNSET
    credential_list_mappings: Optional[list[ApiV2010AccountSipSipDomainSipCredentialListMapping]] = UNSET


class ListSipCredentialListMappingResponseDict(TypedDict):
    end: NotRequired[int]
    first_page_uri: NotRequired[str]
    next_page_uri: NotRequired[str | None]
    page: NotRequired[int]
    page_size: NotRequired[int]
    previous_page_uri: NotRequired[str | None]
    start: NotRequired[int]
    uri: NotRequired[str]
    credential_list_mappings: NotRequired[
        list[
            (
                ApiV2010AccountSipSipDomainSipCredentialListMapping
                | ApiV2010AccountSipSipDomainSipCredentialListMappingDict
            )
        ]
    ]
