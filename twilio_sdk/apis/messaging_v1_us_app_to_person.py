from __future__ import annotations

from pydantic import AnyUrl

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    empty_response,
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.list_us_app_to_person_response import ListUsAppToPersonResponse
from ..models.unions.messaging_v1_service_us_app_to_person_response import MessagingV1ServiceUsAppToPersonResponse
from ..server.server import Server


class MessagingV1UsAppToPerson:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MessagingV1UsAppToPersonWithRawResponse(client, server, auth)

    def create_us_app_to_person(
        self,
        messaging_service_sid: str,
        brand_registration_sid: str,
        description: str,
        message_flow: str,
        message_samples: list[str],
        us_app_to_person_usecase: str,
        has_embedded_links: bool,
        has_embedded_phone: bool,
        *,
        x_twilio_api_version: str | None = None,
        opt_in_message: str | None = None,
        opt_out_message: str | None = None,
        help_message: str | None = None,
        opt_in_keywords: list[str] | None = None,
        opt_out_keywords: list[str] | None = None,
        help_keywords: list[str] | None = None,
        subscriber_opt_in: bool | None = None,
        age_gated: bool | None = None,
        direct_lending: bool | None = None,
        privacy_policy_url: AnyUrl | None = None,
        terms_and_conditions_url: AnyUrl | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MessagingV1ServiceUsAppToPersonResponse:
        """A service for (fetch/create/delete) A2P Campaign for a Messaging Service

        Args:
            messaging_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ to create the resources from.
            brand_registration_sid: A2P Brand Registration SID
            description: A short description of what this SMS campaign does. Min length: 40 characters. Max length: 4096
                characters.
            message_flow: Required for all Campaigns. Details around how a consumer opts-in to their campaign, therefore
                giving consent to receive their messages. If multiple opt-in methods can be used for the same campaign,
                they must all be listed. 40 character minimum. 2048 character maximum.
            message_samples: An array of sample message strings, min two and max five. Min length for each sample: 20
                chars. Max length for each sample: 1024 chars.
            us_app_to_person_usecase: A2P Campaign Use Case. Examples: [ 2FA, EMERGENCY, MARKETING..]
            has_embedded_links: Indicates that this SMS campaign will send messages that contain links.
            has_embedded_phone: Indicates that this SMS campaign will send messages that contain phone numbers.
            x_twilio_api_version: The version of the Messaging API to use for this request
            opt_in_message: If end users can text in a keyword to start receiving messages from this campaign, the
                auto-reply messages sent to the end users must be provided. The opt-in response should include the Brand
                name, confirmation of opt-in enrollment to a recurring message campaign, how to get help, and clear
                description of how to opt-out. This field is required if end users can text in a keyword to start
                receiving messages from this campaign. 20 character minimum. 320 character maximum.
            opt_out_message: Upon receiving the opt-out keywords from the end users, Twilio customers are expected to
                send back an auto-generated response, which must provide acknowledgment of the opt-out request and
                confirmation that no further messages will be sent. It is also recommended that these opt-out messages
                include the brand name. This field is required if managing opt out keywords yourself (i.e. not using
                Twilio's Default or Advanced Opt Out features). 20 character minimum. 320 character maximum.
            help_message: When customers receive the help keywords from their end users, Twilio customers are expected
                to send back an auto-generated response; this may include the brand name and additional support contact
                information. This field is required if managing help keywords yourself (i.e. not using Twilio's Default
                or Advanced Opt Out features). 20 character minimum. 320 character maximum.
            opt_in_keywords: If end users can text in a keyword to start receiving messages from this campaign, those
                keywords must be provided. This field is required if end users can text in a keyword to start receiving
                messages from this campaign. Values must be alphanumeric. 255 character maximum.
            opt_out_keywords: End users should be able to text in a keyword to stop receiving messages from this
                campaign. Those keywords must be provided. This field is required if managing opt out keywords yourself
                (i.e. not using Twilio's Default or Advanced Opt Out features). Values must be alphanumeric. 255
                character maximum.
            help_keywords: End users should be able to text in a keyword to receive help. Those keywords must be
                provided as part of the campaign registration request. This field is required if managing help keywords
                yourself (i.e. not using Twilio's Default or Advanced Opt Out features). Values must be alphanumeric.
                255 character maximum.
            subscriber_opt_in: A boolean that specifies whether campaign has Subscriber Optin or not.
            age_gated: A boolean that specifies whether campaign is age gated or not.
            direct_lending: A boolean that specifies whether campaign allows direct lending or not.
            privacy_policy_url: The URL of the privacy policy for the campaign.
            terms_and_conditions_url: The URL of the terms and conditions for the campaign.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_us_app_to_person(
            messaging_service_sid,
            brand_registration_sid,
            description,
            message_flow,
            message_samples,
            us_app_to_person_usecase,
            has_embedded_links,
            has_embedded_phone,
            x_twilio_api_version=x_twilio_api_version,
            opt_in_message=opt_in_message,
            opt_out_message=opt_out_message,
            help_message=help_message,
            opt_in_keywords=opt_in_keywords,
            opt_out_keywords=opt_out_keywords,
            help_keywords=help_keywords,
            subscriber_opt_in=subscriber_opt_in,
            age_gated=age_gated,
            direct_lending=direct_lending,
            privacy_policy_url=privacy_policy_url,
            terms_and_conditions_url=terms_and_conditions_url,
            request_options=request_options,
        ).unwrap()

    def delete_us_app_to_person(
        self, messaging_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """A service for (fetch/create/delete) A2P Campaign for a Messaging Service

        Args:
            messaging_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ to delete the resource from.
            sid: The SID of the US A2P Compliance resource to delete ``QE2c6890da8086d771620e9b13fadeba0b``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_us_app_to_person(
            messaging_service_sid, sid, request_options=request_options
        ).unwrap()

    def fetch_us_app_to_person(
        self,
        messaging_service_sid: str,
        sid: str,
        *,
        x_twilio_api_version: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MessagingV1ServiceUsAppToPersonResponse:
        """A service for (fetch/create/delete) A2P Campaign for a Messaging Service

        Args:
            messaging_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ to fetch the resource from.
            sid: The SID of the US A2P Compliance resource to fetch ``QE2c6890da8086d771620e9b13fadeba0b``.
            x_twilio_api_version: The version of the Messaging API to use for this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_us_app_to_person(
            messaging_service_sid, sid, x_twilio_api_version=x_twilio_api_version, request_options=request_options
        ).unwrap()

    def list_us_app_to_person(
        self,
        messaging_service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        x_twilio_api_version: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListUsAppToPersonResponse:
        """A service for (fetch/create/delete) A2P Campaign for a Messaging Service

        Args:
            messaging_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ to fetch the resource from.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            x_twilio_api_version: The version of the Messaging API to use for this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_us_app_to_person(
            messaging_service_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            x_twilio_api_version=x_twilio_api_version,
            request_options=request_options,
        ).unwrap()

    def update_us_app_to_person(
        self,
        messaging_service_sid: str,
        sid: str,
        has_embedded_links: bool,
        has_embedded_phone: bool,
        message_samples: list[str],
        message_flow: str,
        description: str,
        age_gated: bool,
        direct_lending: bool,
        *,
        x_twilio_api_version: str | None = None,
        privacy_policy_url: AnyUrl | None = None,
        terms_and_conditions_url: AnyUrl | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MessagingV1ServiceUsAppToPersonResponse:
        """A service for (fetch/create/delete) A2P Campaign for a Messaging Service

        Args:
            messaging_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/services/api>`__ to update the resource from.
            sid: The SID of the US A2P Compliance resource to update ``QE2c6890da8086d771620e9b13fadeba0b``.
            has_embedded_links: Indicates that this SMS campaign will send messages that contain links.
            has_embedded_phone: Indicates that this SMS campaign will send messages that contain phone numbers.
            message_samples: An array of sample message strings, min two and max five. Min length for each sample: 20
                chars. Max length for each sample: 1024 chars.
            message_flow: Required for all Campaigns. Details around how a consumer opts-in to their campaign, therefore
                giving consent to receive their messages. If multiple opt-in methods can be used for the same campaign,
                they must all be listed. 40 character minimum. 2048 character maximum.
            description: A short description of what this SMS campaign does. Min length: 40 characters. Max length: 4096
                characters.
            age_gated: A boolean that specifies whether campaign requires age gate for federally legal content.
            direct_lending: A boolean that specifies whether campaign allows direct lending or not.
            x_twilio_api_version: The version of the Messaging API to use for this request
            privacy_policy_url: The URL of the privacy policy for the campaign.
            terms_and_conditions_url: The URL of the terms and conditions for the campaign.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_us_app_to_person(
            messaging_service_sid,
            sid,
            has_embedded_links,
            has_embedded_phone,
            message_samples,
            message_flow,
            description,
            age_gated,
            direct_lending,
            x_twilio_api_version=x_twilio_api_version,
            privacy_policy_url=privacy_policy_url,
            terms_and_conditions_url=terms_and_conditions_url,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> MessagingV1UsAppToPersonWithRawResponse:
        return self._with_raw_response


class AsyncMessagingV1UsAppToPerson:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMessagingV1UsAppToPersonWithRawResponse(client, server, auth)

    async def create_us_app_to_person(
        self,
        messaging_service_sid: str,
        brand_registration_sid: str,
        description: str,
        message_flow: str,
        message_samples: list[str],
        us_app_to_person_usecase: str,
        has_embedded_links: bool,
        has_embedded_phone: bool,
        *,
        x_twilio_api_version: str | None = None,
        opt_in_message: str | None = None,
        opt_out_message: str | None = None,
        help_message: str | None = None,
        opt_in_keywords: list[str] | None = None,
        opt_out_keywords: list[str] | None = None,
        help_keywords: list[str] | None = None,
        subscriber_opt_in: bool | None = None,
        age_gated: bool | None = None,
        direct_lending: bool | None = None,
        privacy_policy_url: AnyUrl | None = None,
        terms_and_conditions_url: AnyUrl | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MessagingV1ServiceUsAppToPersonResponse:
        """A service for (fetch/create/delete) A2P Campaign for a Messaging Service

        Args:
            messaging_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ to create the resources from.
            brand_registration_sid: A2P Brand Registration SID
            description: A short description of what this SMS campaign does. Min length: 40 characters. Max length: 4096
                characters.
            message_flow: Required for all Campaigns. Details around how a consumer opts-in to their campaign, therefore
                giving consent to receive their messages. If multiple opt-in methods can be used for the same campaign,
                they must all be listed. 40 character minimum. 2048 character maximum.
            message_samples: An array of sample message strings, min two and max five. Min length for each sample: 20
                chars. Max length for each sample: 1024 chars.
            us_app_to_person_usecase: A2P Campaign Use Case. Examples: [ 2FA, EMERGENCY, MARKETING..]
            has_embedded_links: Indicates that this SMS campaign will send messages that contain links.
            has_embedded_phone: Indicates that this SMS campaign will send messages that contain phone numbers.
            x_twilio_api_version: The version of the Messaging API to use for this request
            opt_in_message: If end users can text in a keyword to start receiving messages from this campaign, the
                auto-reply messages sent to the end users must be provided. The opt-in response should include the Brand
                name, confirmation of opt-in enrollment to a recurring message campaign, how to get help, and clear
                description of how to opt-out. This field is required if end users can text in a keyword to start
                receiving messages from this campaign. 20 character minimum. 320 character maximum.
            opt_out_message: Upon receiving the opt-out keywords from the end users, Twilio customers are expected to
                send back an auto-generated response, which must provide acknowledgment of the opt-out request and
                confirmation that no further messages will be sent. It is also recommended that these opt-out messages
                include the brand name. This field is required if managing opt out keywords yourself (i.e. not using
                Twilio's Default or Advanced Opt Out features). 20 character minimum. 320 character maximum.
            help_message: When customers receive the help keywords from their end users, Twilio customers are expected
                to send back an auto-generated response; this may include the brand name and additional support contact
                information. This field is required if managing help keywords yourself (i.e. not using Twilio's Default
                or Advanced Opt Out features). 20 character minimum. 320 character maximum.
            opt_in_keywords: If end users can text in a keyword to start receiving messages from this campaign, those
                keywords must be provided. This field is required if end users can text in a keyword to start receiving
                messages from this campaign. Values must be alphanumeric. 255 character maximum.
            opt_out_keywords: End users should be able to text in a keyword to stop receiving messages from this
                campaign. Those keywords must be provided. This field is required if managing opt out keywords yourself
                (i.e. not using Twilio's Default or Advanced Opt Out features). Values must be alphanumeric. 255
                character maximum.
            help_keywords: End users should be able to text in a keyword to receive help. Those keywords must be
                provided as part of the campaign registration request. This field is required if managing help keywords
                yourself (i.e. not using Twilio's Default or Advanced Opt Out features). Values must be alphanumeric.
                255 character maximum.
            subscriber_opt_in: A boolean that specifies whether campaign has Subscriber Optin or not.
            age_gated: A boolean that specifies whether campaign is age gated or not.
            direct_lending: A boolean that specifies whether campaign allows direct lending or not.
            privacy_policy_url: The URL of the privacy policy for the campaign.
            terms_and_conditions_url: The URL of the terms and conditions for the campaign.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_us_app_to_person(
                messaging_service_sid,
                brand_registration_sid,
                description,
                message_flow,
                message_samples,
                us_app_to_person_usecase,
                has_embedded_links,
                has_embedded_phone,
                x_twilio_api_version=x_twilio_api_version,
                opt_in_message=opt_in_message,
                opt_out_message=opt_out_message,
                help_message=help_message,
                opt_in_keywords=opt_in_keywords,
                opt_out_keywords=opt_out_keywords,
                help_keywords=help_keywords,
                subscriber_opt_in=subscriber_opt_in,
                age_gated=age_gated,
                direct_lending=direct_lending,
                privacy_policy_url=privacy_policy_url,
                terms_and_conditions_url=terms_and_conditions_url,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_us_app_to_person(
        self, messaging_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """A service for (fetch/create/delete) A2P Campaign for a Messaging Service

        Args:
            messaging_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ to delete the resource from.
            sid: The SID of the US A2P Compliance resource to delete ``QE2c6890da8086d771620e9b13fadeba0b``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_us_app_to_person(
                messaging_service_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def fetch_us_app_to_person(
        self,
        messaging_service_sid: str,
        sid: str,
        *,
        x_twilio_api_version: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MessagingV1ServiceUsAppToPersonResponse:
        """A service for (fetch/create/delete) A2P Campaign for a Messaging Service

        Args:
            messaging_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ to fetch the resource from.
            sid: The SID of the US A2P Compliance resource to fetch ``QE2c6890da8086d771620e9b13fadeba0b``.
            x_twilio_api_version: The version of the Messaging API to use for this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_us_app_to_person(
                messaging_service_sid, sid, x_twilio_api_version=x_twilio_api_version, request_options=request_options
            )
        ).unwrap()

    async def list_us_app_to_person(
        self,
        messaging_service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        x_twilio_api_version: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListUsAppToPersonResponse:
        """A service for (fetch/create/delete) A2P Campaign for a Messaging Service

        Args:
            messaging_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ to fetch the resource from.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            x_twilio_api_version: The version of the Messaging API to use for this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_us_app_to_person(
                messaging_service_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                x_twilio_api_version=x_twilio_api_version,
                request_options=request_options,
            )
        ).unwrap()

    async def update_us_app_to_person(
        self,
        messaging_service_sid: str,
        sid: str,
        has_embedded_links: bool,
        has_embedded_phone: bool,
        message_samples: list[str],
        message_flow: str,
        description: str,
        age_gated: bool,
        direct_lending: bool,
        *,
        x_twilio_api_version: str | None = None,
        privacy_policy_url: AnyUrl | None = None,
        terms_and_conditions_url: AnyUrl | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MessagingV1ServiceUsAppToPersonResponse:
        """A service for (fetch/create/delete) A2P Campaign for a Messaging Service

        Args:
            messaging_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/services/api>`__ to update the resource from.
            sid: The SID of the US A2P Compliance resource to update ``QE2c6890da8086d771620e9b13fadeba0b``.
            has_embedded_links: Indicates that this SMS campaign will send messages that contain links.
            has_embedded_phone: Indicates that this SMS campaign will send messages that contain phone numbers.
            message_samples: An array of sample message strings, min two and max five. Min length for each sample: 20
                chars. Max length for each sample: 1024 chars.
            message_flow: Required for all Campaigns. Details around how a consumer opts-in to their campaign, therefore
                giving consent to receive their messages. If multiple opt-in methods can be used for the same campaign,
                they must all be listed. 40 character minimum. 2048 character maximum.
            description: A short description of what this SMS campaign does. Min length: 40 characters. Max length: 4096
                characters.
            age_gated: A boolean that specifies whether campaign requires age gate for federally legal content.
            direct_lending: A boolean that specifies whether campaign allows direct lending or not.
            x_twilio_api_version: The version of the Messaging API to use for this request
            privacy_policy_url: The URL of the privacy policy for the campaign.
            terms_and_conditions_url: The URL of the terms and conditions for the campaign.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_us_app_to_person(
                messaging_service_sid,
                sid,
                has_embedded_links,
                has_embedded_phone,
                message_samples,
                message_flow,
                description,
                age_gated,
                direct_lending,
                x_twilio_api_version=x_twilio_api_version,
                privacy_policy_url=privacy_policy_url,
                terms_and_conditions_url=terms_and_conditions_url,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncMessagingV1UsAppToPersonWithRawResponse:
        return self._with_raw_response


class MessagingV1UsAppToPersonWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_us_app_to_person(
        self,
        messaging_service_sid: str,
        brand_registration_sid: str,
        description: str,
        message_flow: str,
        message_samples: list[str],
        us_app_to_person_usecase: str,
        has_embedded_links: bool,
        has_embedded_phone: bool,
        *,
        x_twilio_api_version: str | None = None,
        opt_in_message: str | None = None,
        opt_out_message: str | None = None,
        help_message: str | None = None,
        opt_in_keywords: list[str] | None = None,
        opt_out_keywords: list[str] | None = None,
        help_keywords: list[str] | None = None,
        subscriber_opt_in: bool | None = None,
        age_gated: bool | None = None,
        direct_lending: bool | None = None,
        privacy_policy_url: AnyUrl | None = None,
        terms_and_conditions_url: AnyUrl | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MessagingV1ServiceUsAppToPersonResponse, RawError]:
        """A service for (fetch/create/delete) A2P Campaign for a Messaging Service

        Args:
            messaging_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ to create the resources from.
            brand_registration_sid: A2P Brand Registration SID
            description: A short description of what this SMS campaign does. Min length: 40 characters. Max length: 4096
                characters.
            message_flow: Required for all Campaigns. Details around how a consumer opts-in to their campaign, therefore
                giving consent to receive their messages. If multiple opt-in methods can be used for the same campaign,
                they must all be listed. 40 character minimum. 2048 character maximum.
            message_samples: An array of sample message strings, min two and max five. Min length for each sample: 20
                chars. Max length for each sample: 1024 chars.
            us_app_to_person_usecase: A2P Campaign Use Case. Examples: [ 2FA, EMERGENCY, MARKETING..]
            has_embedded_links: Indicates that this SMS campaign will send messages that contain links.
            has_embedded_phone: Indicates that this SMS campaign will send messages that contain phone numbers.
            x_twilio_api_version: The version of the Messaging API to use for this request
            opt_in_message: If end users can text in a keyword to start receiving messages from this campaign, the
                auto-reply messages sent to the end users must be provided. The opt-in response should include the Brand
                name, confirmation of opt-in enrollment to a recurring message campaign, how to get help, and clear
                description of how to opt-out. This field is required if end users can text in a keyword to start
                receiving messages from this campaign. 20 character minimum. 320 character maximum.
            opt_out_message: Upon receiving the opt-out keywords from the end users, Twilio customers are expected to
                send back an auto-generated response, which must provide acknowledgment of the opt-out request and
                confirmation that no further messages will be sent. It is also recommended that these opt-out messages
                include the brand name. This field is required if managing opt out keywords yourself (i.e. not using
                Twilio's Default or Advanced Opt Out features). 20 character minimum. 320 character maximum.
            help_message: When customers receive the help keywords from their end users, Twilio customers are expected
                to send back an auto-generated response; this may include the brand name and additional support contact
                information. This field is required if managing help keywords yourself (i.e. not using Twilio's Default
                or Advanced Opt Out features). 20 character minimum. 320 character maximum.
            opt_in_keywords: If end users can text in a keyword to start receiving messages from this campaign, those
                keywords must be provided. This field is required if end users can text in a keyword to start receiving
                messages from this campaign. Values must be alphanumeric. 255 character maximum.
            opt_out_keywords: End users should be able to text in a keyword to stop receiving messages from this
                campaign. Those keywords must be provided. This field is required if managing opt out keywords yourself
                (i.e. not using Twilio's Default or Advanced Opt Out features). Values must be alphanumeric. 255
                character maximum.
            help_keywords: End users should be able to text in a keyword to receive help. Those keywords must be
                provided as part of the campaign registration request. This field is required if managing help keywords
                yourself (i.e. not using Twilio's Default or Advanced Opt Out features). Values must be alphanumeric.
                255 character maximum.
            subscriber_opt_in: A boolean that specifies whether campaign has Subscriber Optin or not.
            age_gated: A boolean that specifies whether campaign is age gated or not.
            direct_lending: A boolean that specifies whether campaign allows direct lending or not.
            privacy_policy_url: The URL of the privacy policy for the campaign.
            terms_and_conditions_url: The URL of the terms and conditions for the campaign.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v1/Services/{MessagingServiceSid}/Compliance/Usa2p"),
            path_params=[param[str]("MessagingServiceSid", messaging_service_sid)],
            headers=[param[str | None]("X-Twilio-Api-Version", x_twilio_api_version)],
            body=form_body(
                [
                    param[str]("BrandRegistrationSid", brand_registration_sid),
                    param[str]("Description", description),
                    param[str]("MessageFlow", message_flow),
                    param[list[str]]("MessageSamples", message_samples),
                    param[str]("UsAppToPersonUsecase", us_app_to_person_usecase),
                    param[bool]("HasEmbeddedLinks", has_embedded_links),
                    param[bool]("HasEmbeddedPhone", has_embedded_phone),
                    param[str | None]("OptInMessage", opt_in_message),
                    param[str | None]("OptOutMessage", opt_out_message),
                    param[str | None]("HelpMessage", help_message),
                    param[list[str] | None]("OptInKeywords", opt_in_keywords),
                    param[list[str] | None]("OptOutKeywords", opt_out_keywords),
                    param[list[str] | None]("HelpKeywords", help_keywords),
                    param[bool | None]("SubscriberOptIn", subscriber_opt_in),
                    param[bool | None]("AgeGated", age_gated),
                    param[bool | None]("DirectLending", direct_lending),
                    param[AnyUrl | None]("PrivacyPolicyUrl", privacy_policy_url),
                    param[AnyUrl | None]("TermsAndConditionsUrl", terms_and_conditions_url),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1ServiceUsAppToPersonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_us_app_to_person(
        self, messaging_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """A service for (fetch/create/delete) A2P Campaign for a Messaging Service

        Args:
            messaging_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ to delete the resource from.
            sid: The SID of the US A2P Compliance resource to delete ``QE2c6890da8086d771620e9b13fadeba0b``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default1("/v1/Services/{MessagingServiceSid}/Compliance/Usa2p/{Sid}"),
            path_params=[param[str]("MessagingServiceSid", messaging_service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_us_app_to_person(
        self,
        messaging_service_sid: str,
        sid: str,
        *,
        x_twilio_api_version: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MessagingV1ServiceUsAppToPersonResponse, RawError]:
        """A service for (fetch/create/delete) A2P Campaign for a Messaging Service

        Args:
            messaging_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ to fetch the resource from.
            sid: The SID of the US A2P Compliance resource to fetch ``QE2c6890da8086d771620e9b13fadeba0b``.
            x_twilio_api_version: The version of the Messaging API to use for this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/Services/{MessagingServiceSid}/Compliance/Usa2p/{Sid}"),
            path_params=[param[str]("MessagingServiceSid", messaging_service_sid), param[str]("Sid", sid)],
            headers=[param[str | None]("X-Twilio-Api-Version", x_twilio_api_version)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1ServiceUsAppToPersonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_us_app_to_person(
        self,
        messaging_service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        x_twilio_api_version: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListUsAppToPersonResponse, RawError]:
        """A service for (fetch/create/delete) A2P Campaign for a Messaging Service

        Args:
            messaging_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ to fetch the resource from.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            x_twilio_api_version: The version of the Messaging API to use for this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/Services/{MessagingServiceSid}/Compliance/Usa2p"),
            path_params=[param[str]("MessagingServiceSid", messaging_service_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            headers=[param[str | None]("X-Twilio-Api-Version", x_twilio_api_version)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListUsAppToPersonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_us_app_to_person(
        self,
        messaging_service_sid: str,
        sid: str,
        has_embedded_links: bool,
        has_embedded_phone: bool,
        message_samples: list[str],
        message_flow: str,
        description: str,
        age_gated: bool,
        direct_lending: bool,
        *,
        x_twilio_api_version: str | None = None,
        privacy_policy_url: AnyUrl | None = None,
        terms_and_conditions_url: AnyUrl | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MessagingV1ServiceUsAppToPersonResponse, RawError]:
        """A service for (fetch/create/delete) A2P Campaign for a Messaging Service

        Args:
            messaging_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/services/api>`__ to update the resource from.
            sid: The SID of the US A2P Compliance resource to update ``QE2c6890da8086d771620e9b13fadeba0b``.
            has_embedded_links: Indicates that this SMS campaign will send messages that contain links.
            has_embedded_phone: Indicates that this SMS campaign will send messages that contain phone numbers.
            message_samples: An array of sample message strings, min two and max five. Min length for each sample: 20
                chars. Max length for each sample: 1024 chars.
            message_flow: Required for all Campaigns. Details around how a consumer opts-in to their campaign, therefore
                giving consent to receive their messages. If multiple opt-in methods can be used for the same campaign,
                they must all be listed. 40 character minimum. 2048 character maximum.
            description: A short description of what this SMS campaign does. Min length: 40 characters. Max length: 4096
                characters.
            age_gated: A boolean that specifies whether campaign requires age gate for federally legal content.
            direct_lending: A boolean that specifies whether campaign allows direct lending or not.
            x_twilio_api_version: The version of the Messaging API to use for this request
            privacy_policy_url: The URL of the privacy policy for the campaign.
            terms_and_conditions_url: The URL of the terms and conditions for the campaign.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v1/Services/{MessagingServiceSid}/Compliance/Usa2p/{Sid}"),
            path_params=[param[str]("MessagingServiceSid", messaging_service_sid), param[str]("Sid", sid)],
            headers=[param[str | None]("X-Twilio-Api-Version", x_twilio_api_version)],
            body=form_body(
                [
                    param[bool]("HasEmbeddedLinks", has_embedded_links),
                    param[bool]("HasEmbeddedPhone", has_embedded_phone),
                    param[list[str]]("MessageSamples", message_samples),
                    param[str]("MessageFlow", message_flow),
                    param[str]("Description", description),
                    param[bool]("AgeGated", age_gated),
                    param[bool]("DirectLending", direct_lending),
                    param[AnyUrl | None]("PrivacyPolicyUrl", privacy_policy_url),
                    param[AnyUrl | None]("TermsAndConditionsUrl", terms_and_conditions_url),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1ServiceUsAppToPersonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncMessagingV1UsAppToPersonWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_us_app_to_person(
        self,
        messaging_service_sid: str,
        brand_registration_sid: str,
        description: str,
        message_flow: str,
        message_samples: list[str],
        us_app_to_person_usecase: str,
        has_embedded_links: bool,
        has_embedded_phone: bool,
        *,
        x_twilio_api_version: str | None = None,
        opt_in_message: str | None = None,
        opt_out_message: str | None = None,
        help_message: str | None = None,
        opt_in_keywords: list[str] | None = None,
        opt_out_keywords: list[str] | None = None,
        help_keywords: list[str] | None = None,
        subscriber_opt_in: bool | None = None,
        age_gated: bool | None = None,
        direct_lending: bool | None = None,
        privacy_policy_url: AnyUrl | None = None,
        terms_and_conditions_url: AnyUrl | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MessagingV1ServiceUsAppToPersonResponse, RawError]:
        """A service for (fetch/create/delete) A2P Campaign for a Messaging Service

        Args:
            messaging_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ to create the resources from.
            brand_registration_sid: A2P Brand Registration SID
            description: A short description of what this SMS campaign does. Min length: 40 characters. Max length: 4096
                characters.
            message_flow: Required for all Campaigns. Details around how a consumer opts-in to their campaign, therefore
                giving consent to receive their messages. If multiple opt-in methods can be used for the same campaign,
                they must all be listed. 40 character minimum. 2048 character maximum.
            message_samples: An array of sample message strings, min two and max five. Min length for each sample: 20
                chars. Max length for each sample: 1024 chars.
            us_app_to_person_usecase: A2P Campaign Use Case. Examples: [ 2FA, EMERGENCY, MARKETING..]
            has_embedded_links: Indicates that this SMS campaign will send messages that contain links.
            has_embedded_phone: Indicates that this SMS campaign will send messages that contain phone numbers.
            x_twilio_api_version: The version of the Messaging API to use for this request
            opt_in_message: If end users can text in a keyword to start receiving messages from this campaign, the
                auto-reply messages sent to the end users must be provided. The opt-in response should include the Brand
                name, confirmation of opt-in enrollment to a recurring message campaign, how to get help, and clear
                description of how to opt-out. This field is required if end users can text in a keyword to start
                receiving messages from this campaign. 20 character minimum. 320 character maximum.
            opt_out_message: Upon receiving the opt-out keywords from the end users, Twilio customers are expected to
                send back an auto-generated response, which must provide acknowledgment of the opt-out request and
                confirmation that no further messages will be sent. It is also recommended that these opt-out messages
                include the brand name. This field is required if managing opt out keywords yourself (i.e. not using
                Twilio's Default or Advanced Opt Out features). 20 character minimum. 320 character maximum.
            help_message: When customers receive the help keywords from their end users, Twilio customers are expected
                to send back an auto-generated response; this may include the brand name and additional support contact
                information. This field is required if managing help keywords yourself (i.e. not using Twilio's Default
                or Advanced Opt Out features). 20 character minimum. 320 character maximum.
            opt_in_keywords: If end users can text in a keyword to start receiving messages from this campaign, those
                keywords must be provided. This field is required if end users can text in a keyword to start receiving
                messages from this campaign. Values must be alphanumeric. 255 character maximum.
            opt_out_keywords: End users should be able to text in a keyword to stop receiving messages from this
                campaign. Those keywords must be provided. This field is required if managing opt out keywords yourself
                (i.e. not using Twilio's Default or Advanced Opt Out features). Values must be alphanumeric. 255
                character maximum.
            help_keywords: End users should be able to text in a keyword to receive help. Those keywords must be
                provided as part of the campaign registration request. This field is required if managing help keywords
                yourself (i.e. not using Twilio's Default or Advanced Opt Out features). Values must be alphanumeric.
                255 character maximum.
            subscriber_opt_in: A boolean that specifies whether campaign has Subscriber Optin or not.
            age_gated: A boolean that specifies whether campaign is age gated or not.
            direct_lending: A boolean that specifies whether campaign allows direct lending or not.
            privacy_policy_url: The URL of the privacy policy for the campaign.
            terms_and_conditions_url: The URL of the terms and conditions for the campaign.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v1/Services/{MessagingServiceSid}/Compliance/Usa2p"),
            path_params=[param[str]("MessagingServiceSid", messaging_service_sid)],
            headers=[param[str | None]("X-Twilio-Api-Version", x_twilio_api_version)],
            body=form_body(
                [
                    param[str]("BrandRegistrationSid", brand_registration_sid),
                    param[str]("Description", description),
                    param[str]("MessageFlow", message_flow),
                    param[list[str]]("MessageSamples", message_samples),
                    param[str]("UsAppToPersonUsecase", us_app_to_person_usecase),
                    param[bool]("HasEmbeddedLinks", has_embedded_links),
                    param[bool]("HasEmbeddedPhone", has_embedded_phone),
                    param[str | None]("OptInMessage", opt_in_message),
                    param[str | None]("OptOutMessage", opt_out_message),
                    param[str | None]("HelpMessage", help_message),
                    param[list[str] | None]("OptInKeywords", opt_in_keywords),
                    param[list[str] | None]("OptOutKeywords", opt_out_keywords),
                    param[list[str] | None]("HelpKeywords", help_keywords),
                    param[bool | None]("SubscriberOptIn", subscriber_opt_in),
                    param[bool | None]("AgeGated", age_gated),
                    param[bool | None]("DirectLending", direct_lending),
                    param[AnyUrl | None]("PrivacyPolicyUrl", privacy_policy_url),
                    param[AnyUrl | None]("TermsAndConditionsUrl", terms_and_conditions_url),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1ServiceUsAppToPersonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_us_app_to_person(
        self, messaging_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """A service for (fetch/create/delete) A2P Campaign for a Messaging Service

        Args:
            messaging_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ to delete the resource from.
            sid: The SID of the US A2P Compliance resource to delete ``QE2c6890da8086d771620e9b13fadeba0b``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default1("/v1/Services/{MessagingServiceSid}/Compliance/Usa2p/{Sid}"),
            path_params=[param[str]("MessagingServiceSid", messaging_service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_us_app_to_person(
        self,
        messaging_service_sid: str,
        sid: str,
        *,
        x_twilio_api_version: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MessagingV1ServiceUsAppToPersonResponse, RawError]:
        """A service for (fetch/create/delete) A2P Campaign for a Messaging Service

        Args:
            messaging_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ to fetch the resource from.
            sid: The SID of the US A2P Compliance resource to fetch ``QE2c6890da8086d771620e9b13fadeba0b``.
            x_twilio_api_version: The version of the Messaging API to use for this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/Services/{MessagingServiceSid}/Compliance/Usa2p/{Sid}"),
            path_params=[param[str]("MessagingServiceSid", messaging_service_sid), param[str]("Sid", sid)],
            headers=[param[str | None]("X-Twilio-Api-Version", x_twilio_api_version)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1ServiceUsAppToPersonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_us_app_to_person(
        self,
        messaging_service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        x_twilio_api_version: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListUsAppToPersonResponse, RawError]:
        """A service for (fetch/create/delete) A2P Campaign for a Messaging Service

        Args:
            messaging_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ to fetch the resource from.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            x_twilio_api_version: The version of the Messaging API to use for this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/Services/{MessagingServiceSid}/Compliance/Usa2p"),
            path_params=[param[str]("MessagingServiceSid", messaging_service_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            headers=[param[str | None]("X-Twilio-Api-Version", x_twilio_api_version)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListUsAppToPersonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_us_app_to_person(
        self,
        messaging_service_sid: str,
        sid: str,
        has_embedded_links: bool,
        has_embedded_phone: bool,
        message_samples: list[str],
        message_flow: str,
        description: str,
        age_gated: bool,
        direct_lending: bool,
        *,
        x_twilio_api_version: str | None = None,
        privacy_policy_url: AnyUrl | None = None,
        terms_and_conditions_url: AnyUrl | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MessagingV1ServiceUsAppToPersonResponse, RawError]:
        """A service for (fetch/create/delete) A2P Campaign for a Messaging Service

        Args:
            messaging_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/services/api>`__ to update the resource from.
            sid: The SID of the US A2P Compliance resource to update ``QE2c6890da8086d771620e9b13fadeba0b``.
            has_embedded_links: Indicates that this SMS campaign will send messages that contain links.
            has_embedded_phone: Indicates that this SMS campaign will send messages that contain phone numbers.
            message_samples: An array of sample message strings, min two and max five. Min length for each sample: 20
                chars. Max length for each sample: 1024 chars.
            message_flow: Required for all Campaigns. Details around how a consumer opts-in to their campaign, therefore
                giving consent to receive their messages. If multiple opt-in methods can be used for the same campaign,
                they must all be listed. 40 character minimum. 2048 character maximum.
            description: A short description of what this SMS campaign does. Min length: 40 characters. Max length: 4096
                characters.
            age_gated: A boolean that specifies whether campaign requires age gate for federally legal content.
            direct_lending: A boolean that specifies whether campaign allows direct lending or not.
            x_twilio_api_version: The version of the Messaging API to use for this request
            privacy_policy_url: The URL of the privacy policy for the campaign.
            terms_and_conditions_url: The URL of the terms and conditions for the campaign.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v1/Services/{MessagingServiceSid}/Compliance/Usa2p/{Sid}"),
            path_params=[param[str]("MessagingServiceSid", messaging_service_sid), param[str]("Sid", sid)],
            headers=[param[str | None]("X-Twilio-Api-Version", x_twilio_api_version)],
            body=form_body(
                [
                    param[bool]("HasEmbeddedLinks", has_embedded_links),
                    param[bool]("HasEmbeddedPhone", has_embedded_phone),
                    param[list[str]]("MessageSamples", message_samples),
                    param[str]("MessageFlow", message_flow),
                    param[str]("Description", description),
                    param[bool]("AgeGated", age_gated),
                    param[bool]("DirectLending", direct_lending),
                    param[AnyUrl | None]("PrivacyPolicyUrl", privacy_policy_url),
                    param[AnyUrl | None]("TermsAndConditionsUrl", terms_and_conditions_url),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1ServiceUsAppToPersonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
