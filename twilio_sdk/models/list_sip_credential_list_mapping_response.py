from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .api_v2010_account_sip_sip_domain_sip_credential_list_mapping import (
    ApiV2010AccountSipSipDomainSipCredentialListMapping,
    ApiV2010AccountSipSipDomainSipCredentialListMappingDict,
)


class ListSipCredentialListMappingResponse(SdkBaseModel):
    end: Optional[int] = UNSET
    first_page_uri: Optional[AnyUrl] = UNSET
    next_page_uri: OptionalNullable[AnyUrl] = UNSET
    page: Optional[int] = UNSET
    page_size: Optional[int] = UNSET
    previous_page_uri: OptionalNullable[AnyUrl] = UNSET
    start: Optional[int] = UNSET
    uri: Optional[AnyUrl] = UNSET
    credential_list_mappings: Optional[list[ApiV2010AccountSipSipDomainSipCredentialListMapping]] = UNSET


class ListSipCredentialListMappingResponseDict(TypedDict):
    end: NotRequired[int]
    first_page_uri: NotRequired[AnyUrl]
    next_page_uri: NotRequired[AnyUrl | None]
    page: NotRequired[int]
    page_size: NotRequired[int]
    previous_page_uri: NotRequired[AnyUrl | None]
    start: NotRequired[int]
    uri: NotRequired[AnyUrl]
    credential_list_mappings: NotRequired[
        list[
            (
                ApiV2010AccountSipSipDomainSipCredentialListMapping
                | ApiV2010AccountSipSipDomainSipCredentialListMappingDict
            )
        ]
    ]
