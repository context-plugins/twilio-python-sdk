from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v3_insights_domains_conversations_metadata400_error1 import (
    V3InsightsDomainsConversationsMetadata400Error1,
)
from ..models.v3_insights_domains_conversations_metadata429_error1 import (
    V3InsightsDomainsConversationsMetadata429Error1,
)
from ..models.v3_insights_domains_conversations_metadata500_error1 import (
    V3InsightsDomainsConversationsMetadata500Error1,
)

FetchMetadataErrorBody: TypeAlias = (
    V3InsightsDomainsConversationsMetadata400Error1
    | V3InsightsDomainsConversationsMetadata429Error1
    | V3InsightsDomainsConversationsMetadata500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _FetchMetadataError:
    def map(self, response: HttpResponse) -> FetchMetadataErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V3InsightsDomainsConversationsMetadata400Error1](response)
            case 429:
                return decode_json[V3InsightsDomainsConversationsMetadata429Error1](response)
            case 500:
                return decode_json[V3InsightsDomainsConversationsMetadata500Error1](response)
            case _:
                return RawError(response)


fetch_metadata_error_mapper: Final[ErrorMapper[FetchMetadataErrorBody]] = _FetchMetadataError()
