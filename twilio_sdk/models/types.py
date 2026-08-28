from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .twilio_call_to_action import TwilioCallToAction, TwilioCallToActionDict
from .twilio_card import TwilioCard, TwilioCardDict
from .twilio_carousel import TwilioCarousel, TwilioCarouselDict
from .twilio_catalog import TwilioCatalog, TwilioCatalogDict
from .twilio_flows import TwilioFlows, TwilioFlowsDict
from .twilio_list_picker import TwilioListPicker, TwilioListPickerDict
from .twilio_location import TwilioLocation, TwilioLocationDict
from .twilio_media import TwilioMedia, TwilioMediaDict
from .twilio_quick_reply import TwilioQuickReply, TwilioQuickReplyDict
from .twilio_schedule import TwilioSchedule, TwilioScheduleDict
from .twilio_text import TwilioText, TwilioTextDict
from .whatsapp_authentication import WhatsappAuthentication, WhatsappAuthenticationDict
from .whatsapp_card import WhatsappCard, WhatsappCardDict
from .whatsapp_flows import WhatsappFlows, WhatsappFlowsDict


class Types(SdkBaseModel):
    """Content types"""

    twilio_text: OptionalNullable[TwilioText] = Field(default=UNSET, alias="twilio/text")
    """Type containing only plain text-based content"""

    twilio_media: OptionalNullable[TwilioMedia] = Field(default=UNSET, alias="twilio/media")
    """twilio/media is used to send file attachments, or to send long text via MMS in the US and Canada. As such, the
    twilio/media type must contain at least ONE of text or media content."""

    twilio_location: OptionalNullable[TwilioLocation] = Field(default=UNSET, alias="twilio/location")
    """twilio/location type contains a location pin and an optional label, which can be used to enhance delivery
    notifications or connect recipients to physical experiences you offer."""

    twilio_list_picker: OptionalNullable[TwilioListPicker] = Field(default=UNSET, alias="twilio/list-picker")
    """twilio/list-picker includes a menu of up to 10 options, which offers a simple way for users to make a
    selection."""

    twilio_call_to_action: OptionalNullable[TwilioCallToAction] = Field(default=UNSET, alias="twilio/call-to-action")
    """twilio/call-to-action buttons let recipients tap to trigger actions such as launching a website or making a phone
    call."""

    twilio_quick_reply: OptionalNullable[TwilioQuickReply] = Field(default=UNSET, alias="twilio/quick-reply")
    """twilio/quick-reply templates let recipients tap, rather than type, to respond to the message."""

    twilio_card: OptionalNullable[TwilioCard] = Field(default=UNSET, alias="twilio/card")
    """twilio/card is a structured template which can be used to send a series of related information. It must include a
    title and at least one additional field."""

    twilio_catalog: OptionalNullable[TwilioCatalog] = Field(default=UNSET, alias="twilio/catalog")
    """twilio/catalog type lets recipients view list of catalog products, ask questions about products, order
    products."""

    twilio_carousel: OptionalNullable[TwilioCarousel] = Field(default=UNSET, alias="twilio/carousel")
    """twilio/carousel templates allow you to send a single text message accompanied by a set of up to 10 carousel cards
    in a horizontally scrollable view"""

    twilio_flows: OptionalNullable[TwilioFlows] = Field(default=UNSET, alias="twilio/flows")
    """twilio/flows templates allow you to send multiple messages in a set order with text or select options"""

    twilio_schedule: OptionalNullable[TwilioSchedule] = Field(default=UNSET, alias="twilio/schedule")
    """twilio/schedule templates allow us to send a message with a schedule with different time slots"""

    whatsapp_card: OptionalNullable[WhatsappCard] = Field(default=UNSET, alias="whatsapp/card")
    """whatsapp/card is a structured template which can be used to send a series of related information. It must include
    a body and at least one additional field."""

    whatsapp_authentication: OptionalNullable[WhatsappAuthentication] = Field(
        default=UNSET, alias="whatsapp/authentication"
    )
    """whatsApp/authentication templates let companies deliver WA approved one-time-password button."""

    whatsapp_flows: OptionalNullable[WhatsappFlows] = Field(default=UNSET, alias="whatsapp/flows")
    """whatsapp/flows templates allow you to send multiple messages in a set order with text or select options"""


class TypesDict(TypedDict):
    twilio_text: NotRequired[TwilioText | TwilioTextDict | None]
    twilio_media: NotRequired[TwilioMedia | TwilioMediaDict | None]
    twilio_location: NotRequired[TwilioLocation | TwilioLocationDict | None]
    twilio_list_picker: NotRequired[TwilioListPicker | TwilioListPickerDict | None]
    twilio_call_to_action: NotRequired[TwilioCallToAction | TwilioCallToActionDict | None]
    twilio_quick_reply: NotRequired[TwilioQuickReply | TwilioQuickReplyDict | None]
    twilio_card: NotRequired[TwilioCard | TwilioCardDict | None]
    twilio_catalog: NotRequired[TwilioCatalog | TwilioCatalogDict | None]
    twilio_carousel: NotRequired[TwilioCarousel | TwilioCarouselDict | None]
    twilio_flows: NotRequired[TwilioFlows | TwilioFlowsDict | None]
    twilio_schedule: NotRequired[TwilioSchedule | TwilioScheduleDict | None]
    whatsapp_card: NotRequired[WhatsappCard | WhatsappCardDict | None]
    whatsapp_authentication: NotRequired[WhatsappAuthentication | WhatsappAuthenticationDict | None]
    whatsapp_flows: NotRequired[WhatsappFlows | WhatsappFlowsDict | None]
