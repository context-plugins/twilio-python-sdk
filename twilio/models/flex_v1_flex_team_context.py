from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class FlexV1FlexTeamContext(SdkBaseModel):
    team_setup_complete: OptionalNullable[bool] = UNSET
    conversational_insights_enabled: OptionalNullable[bool] = UNSET
    historical_reporting_enabled: OptionalNullable[bool] = UNSET


class FlexV1FlexTeamContextDict(TypedDict):
    team_setup_complete: NotRequired[bool | None]
    conversational_insights_enabled: NotRequired[bool | None]
    historical_reporting_enabled: NotRequired[bool | None]
