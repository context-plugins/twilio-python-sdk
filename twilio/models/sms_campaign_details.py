from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.campaign_frequency import CampaignFrequencyOrStr
from .enums.customer_care_channel import CustomerCareChannelOrStr
from .enums.tollfree_verification_enum_use_case_category import TollfreeVerificationEnumUseCaseCategoryOrStr


class SmsCampaignDetails(SdkBaseModel):
    """SMS campaign details for the application."""

    campaign_name: Optional[str] = UNSET
    campaign_brand_website: Optional[str] = UNSET
    customer_care_channel: Optional[CustomerCareChannelOrStr] = UNSET
    customer_care_value: Optional[str] = UNSET
    campaign_frequency: Optional[list[CampaignFrequencyOrStr]] = UNSET
    sc_use_case_categories: Optional[list[TollfreeVerificationEnumUseCaseCategoryOrStr]] = UNSET
    sms_terms_of_service_url: Optional[str] = UNSET
    sms_privacy_policy_url: Optional[str] = UNSET
    monthly_outbound_volume_expected: Optional[str] = UNSET
    monthly_inbound_volume_expected: Optional[str] = UNSET
    avg_monthly_messages_sent_to_each_subscriber: Optional[str] = UNSET
    avg_monthly_messages_received_from_subscribers: Optional[str] = UNSET
    estimated_total_subscribers: Optional[str] = UNSET
    duration_of_the_campaign: Optional[str] = UNSET
    planned_traffic_spikes: Optional[str] = UNSET
    spike_details: Optional[str] = UNSET
    expected_traffic_start_date: Optional[str] = UNSET


class SmsCampaignDetailsDict(TypedDict):
    campaign_name: NotRequired[str]
    campaign_brand_website: NotRequired[str]
    customer_care_channel: NotRequired[CustomerCareChannelOrStr]
    customer_care_value: NotRequired[str]
    campaign_frequency: NotRequired[list[CampaignFrequencyOrStr]]
    sc_use_case_categories: NotRequired[list[TollfreeVerificationEnumUseCaseCategoryOrStr]]
    sms_terms_of_service_url: NotRequired[str]
    sms_privacy_policy_url: NotRequired[str]
    monthly_outbound_volume_expected: NotRequired[str]
    monthly_inbound_volume_expected: NotRequired[str]
    avg_monthly_messages_sent_to_each_subscriber: NotRequired[str]
    avg_monthly_messages_received_from_subscribers: NotRequired[str]
    estimated_total_subscribers: NotRequired[str]
    duration_of_the_campaign: NotRequired[str]
    planned_traffic_spikes: NotRequired[str]
    spike_details: NotRequired[str]
    expected_traffic_start_date: NotRequired[str]
