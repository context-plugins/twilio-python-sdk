from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .business_information1 import BusinessInformation1, BusinessInformation1Dict
from .compliance_keywords import ComplianceKeywords, ComplianceKeywordsDict
from .content_examples import ContentExamples, ContentExamplesDict
from .enums.state import StateOrStr
from .setup1 import Setup1, Setup1Dict
from .sms_campaign_details import SmsCampaignDetails, SmsCampaignDetailsDict
from .user_sign_up import UserSignUp, UserSignUpDict


class CreateShortCodeApplicationResponse(SdkBaseModel):
    sid: Optional[str] = UNSET
    """The unique identifier of the Short Code Application."""

    application_requirements_sid: Optional[str] = UNSET
    """The Application Requirements SID."""

    application_requirements_version: Optional[int] = UNSET
    """The version of the application requirements."""

    account_sid: Optional[str] = UNSET
    """The Account SID associated with the application."""

    bundle_sid: Optional[str] = UNSET
    """The Bundle SID for regulatory compliance."""

    reviewer: Optional[str] = UNSET
    """The reviewer of the application."""

    zendesk_ticket_id: Optional[str] = UNSET
    """The Zendesk ticket ID associated with the application."""

    friendly_name: Optional[str] = UNSET
    """The friendly name of the application."""

    notification_emails: Optional[list[str]] = UNSET
    """The notification emails for the application."""

    iso_country: Optional[str] = UNSET
    """The ISO country code."""

    state: Optional[StateOrStr] = UNSET
    """The state of the application."""

    setup: Optional[Setup1] = UNSET
    """Setup configuration for the application."""

    business_information: Optional[BusinessInformation1] = UNSET
    """Business information associated with the application."""

    user_sign_up: Optional[UserSignUp] = UNSET
    """User sign-up configuration for the application."""

    compliance_keywords: Optional[ComplianceKeywords] = UNSET
    """Compliance keywords for the application."""

    content_examples: Optional[ContentExamples] = UNSET
    """Content examples for the application."""

    sms_campaign_details: Optional[SmsCampaignDetails] = UNSET
    """SMS campaign details for the application."""

    date_created: Optional[RFC3339DateTime] = UNSET
    """The date and time the application was created."""

    date_updated: Optional[RFC3339DateTime] = UNSET
    """The date and time the application was last updated."""

    created_by: Optional[str] = UNSET
    """The identity of the user who created the application."""

    updated_by: Optional[str] = UNSET
    """The identity of the user who last updated the application."""


class CreateShortCodeApplicationResponseDict(TypedDict):
    sid: NotRequired[str]
    application_requirements_sid: NotRequired[str]
    application_requirements_version: NotRequired[int]
    account_sid: NotRequired[str]
    bundle_sid: NotRequired[str]
    reviewer: NotRequired[str]
    zendesk_ticket_id: NotRequired[str]
    friendly_name: NotRequired[str]
    notification_emails: NotRequired[list[str]]
    iso_country: NotRequired[str]
    state: NotRequired[StateOrStr]
    setup: NotRequired[Setup1 | Setup1Dict]
    business_information: NotRequired[BusinessInformation1 | BusinessInformation1Dict]
    user_sign_up: NotRequired[UserSignUp | UserSignUpDict]
    compliance_keywords: NotRequired[ComplianceKeywords | ComplianceKeywordsDict]
    content_examples: NotRequired[ContentExamples | ContentExamplesDict]
    sms_campaign_details: NotRequired[SmsCampaignDetails | SmsCampaignDetailsDict]
    date_created: NotRequired[RFC3339DateTime]
    date_updated: NotRequired[RFC3339DateTime]
    created_by: NotRequired[str]
    updated_by: NotRequired[str]
