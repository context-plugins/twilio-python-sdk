from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v3_insights_domains_conversations_query400_error1 import V3InsightsDomainsConversationsQuery400Error1
from ..models.v3_insights_domains_conversations_query429_error1 import V3InsightsDomainsConversationsQuery429Error1
from ..models.v3_insights_domains_conversations_query500_error1 import V3InsightsDomainsConversationsQuery500Error1

FetchQueryResultsErrorBody: TypeAlias = (
    V3InsightsDomainsConversationsQuery400Error1
    | V3InsightsDomainsConversationsQuery429Error1
    | V3InsightsDomainsConversationsQuery500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _FetchQueryResultsError:
    def map(self, response: HttpResponse) -> FetchQueryResultsErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V3InsightsDomainsConversationsQuery400Error1](response)
            case 429:
                return decode_json[V3InsightsDomainsConversationsQuery429Error1](response)
            case 500:
                return decode_json[V3InsightsDomainsConversationsQuery500Error1](response)
            case _:
                return RawError(response)


fetch_query_results_error_mapper: Final[ErrorMapper[FetchQueryResultsErrorBody]] = _FetchQueryResultsError()
