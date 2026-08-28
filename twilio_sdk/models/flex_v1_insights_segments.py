from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class FlexV1InsightsSegments(SdkBaseModel):
    segment_id: OptionalNullable[str] = UNSET
    """To unique id of the segment"""

    external_id: OptionalNullable[str] = UNSET
    """The unique id for the conversation."""

    queue: OptionalNullable[str] = UNSET
    external_contact: OptionalNullable[str] = UNSET
    external_segment_link_id: OptionalNullable[str] = UNSET
    """The uuid for the external_segment_link."""

    date: OptionalNullable[str] = UNSET
    """The date of the conversation."""

    account_id: OptionalNullable[str] = UNSET
    """The unique id for the account."""

    external_segment_link: OptionalNullable[str] = UNSET
    """The hyperlink to recording of the task event."""

    agent_id: OptionalNullable[str] = UNSET
    """The unique id for the agent."""

    agent_phone: OptionalNullable[str] = UNSET
    """The phone number of the agent."""

    agent_name: OptionalNullable[str] = UNSET
    """The name of the agent."""

    agent_team_name: OptionalNullable[str] = UNSET
    """The team name to which agent belongs."""

    agent_team_name_in_hierarchy: OptionalNullable[str] = UNSET
    """he team name to which agent belongs."""

    agent_link: OptionalNullable[str] = UNSET
    """The link to the agent conversation."""

    customer_phone: OptionalNullable[str] = UNSET
    """The phone number of the customer."""

    customer_name: OptionalNullable[str] = UNSET
    """The name of the customer."""

    customer_link: OptionalNullable[str] = UNSET
    """The link to the customer conversation."""

    segment_recording_offset: OptionalNullable[str] = UNSET
    """The offset value for the recording."""

    media: OptionalNullable[Any] = UNSET
    """The media identifiers of the conversation."""

    assessment_type: OptionalNullable[Any] = UNSET
    """The type of the assessment."""

    assessment_percentage: OptionalNullable[Any] = UNSET
    """The percentage scored on the Assessments."""

    url: OptionalNullable[AnyUrl] = UNSET


class FlexV1InsightsSegmentsDict(TypedDict):
    segment_id: NotRequired[str | None]
    external_id: NotRequired[str | None]
    queue: NotRequired[str | None]
    external_contact: NotRequired[str | None]
    external_segment_link_id: NotRequired[str | None]
    date: NotRequired[str | None]
    account_id: NotRequired[str | None]
    external_segment_link: NotRequired[str | None]
    agent_id: NotRequired[str | None]
    agent_phone: NotRequired[str | None]
    agent_name: NotRequired[str | None]
    agent_team_name: NotRequired[str | None]
    agent_team_name_in_hierarchy: NotRequired[str | None]
    agent_link: NotRequired[str | None]
    customer_phone: NotRequired[str | None]
    customer_name: NotRequired[str | None]
    customer_link: NotRequired[str | None]
    segment_recording_offset: NotRequired[str | None]
    media: NotRequired[Any | None]
    assessment_type: NotRequired[Any | None]
    assessment_percentage: NotRequired[Any | None]
    url: NotRequired[AnyUrl | None]
