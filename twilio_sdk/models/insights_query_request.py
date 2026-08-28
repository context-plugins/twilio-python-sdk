from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .query_definition import QueryDefinition, QueryDefinitionDict


class InsightsQueryRequest(SdkBaseModel):
    domain: Optional[str] = UNSET
    """The business domain to execute the query against"""

    query: QueryDefinition
    """Structured query definition that specifies what data to retrieve and how to filter, group, and order it"""


class InsightsQueryRequestDict(TypedDict):
    domain: NotRequired[str]
    query: QueryDefinition | QueryDefinitionDict
