from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .filter import Filter, FilterDict
from .order_by import OrderBy, OrderByDict


class QueryDefinition(SdkBaseModel):
    """Structured query definition that specifies what data to retrieve and how to filter, group, and order it"""

    measures: Optional[list[str]] = UNSET
    """Array of measures to retrieve, representing quantitative values or metrics to be calculated"""

    dimensions: Optional[list[str]] = UNSET
    """Array of dimensions to retrieve, representing categorical attributes for grouping and organizing data"""

    filters: Optional[list[Filter]] = UNSET
    """Nested filter conditions. Always use ``op`` and ``expressions``."""

    order_by: Optional[list[OrderBy]] = Field(default=UNSET, alias="orderBy")
    """Specifications for sorting the query results by specific fields in ascending or descending order"""


class QueryDefinitionDict(TypedDict):
    measures: NotRequired[list[str]]
    dimensions: NotRequired[list[str]]
    filters: NotRequired[list[Filter | FilterDict]]
    order_by: NotRequired[list[OrderBy | OrderByDict]]
