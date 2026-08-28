from __future__ import annotations

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
from ..models.api_v2010_account_incoming_phone_number import ApiV2010AccountIncomingPhoneNumber
from ..models.enums.incoming_phone_number_enum_emergency_status import IncomingPhoneNumberEnumEmergencyStatusOrStr
from ..models.enums.incoming_phone_number_enum_voice_receive_mode import IncomingPhoneNumberEnumVoiceReceiveModeOrStr
from ..models.enums.sms_fallback_method9 import SmsFallbackMethod9OrStr
from ..models.enums.sms_method9 import SmsMethod9OrStr
from ..models.enums.status_callback_method10 import StatusCallbackMethod10OrStr
from ..models.enums.voice_fallback_method9 import VoiceFallbackMethod9OrStr
from ..models.enums.voice_method9 import VoiceMethod9OrStr
from ..models.list_incoming_phone_number_response import ListIncomingPhoneNumberResponse
from ..server.server import Server


class Api20100401IncomingPhoneNumber:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401IncomingPhoneNumberWithRawResponse(client, server, auth)

    def create_incoming_phone_number(
        self,
        account_sid: str,
        *,
        api_version: str | None = None,
        friendly_name: str | None = None,
        sms_application_sid: str | None = None,
        sms_fallback_method: SmsFallbackMethod9OrStr | None = None,
        sms_fallback_url: str | None = None,
        sms_method: SmsMethod9OrStr | None = None,
        sms_url: str | None = None,
        status_callback: str | None = None,
        status_callback_method: StatusCallbackMethod10OrStr | None = None,
        voice_application_sid: str | None = None,
        voice_caller_id_lookup: bool | None = None,
        voice_fallback_method: VoiceFallbackMethod9OrStr | None = None,
        voice_fallback_url: str | None = None,
        voice_method: VoiceMethod9OrStr | None = None,
        voice_url: str | None = None,
        emergency_status: IncomingPhoneNumberEnumEmergencyStatusOrStr | None = None,
        emergency_address_sid: str | None = None,
        trunk_sid: str | None = None,
        identity_sid: str | None = None,
        address_sid: str | None = None,
        voice_receive_mode: IncomingPhoneNumberEnumVoiceReceiveModeOrStr | None = None,
        bundle_sid: str | None = None,
        phone_number: str | None = None,
        area_code: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountIncomingPhoneNumber:
        """Purchase a phone-number for the account.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            api_version: The API version to use for incoming calls made to the new phone number. The default is
                ``2010-04-01``.
            friendly_name: A descriptive string that you created to describe the new phone number. It can be up to 64
                characters long. By default, this is a formatted version of the new phone number.
            sms_application_sid: The SID of the application that should handle SMS messages sent to the new phone
                number. If an ``sms_application_sid`` is present, we ignore all of the ``sms_*_url`` urls and use those
                set on the application.
            sms_fallback_method: The HTTP method that we should use to call ``sms_fallback_url``. Can be: ``GET`` or
                ``POST`` and defaults to ``POST``.
            sms_fallback_url: The URL that we should call when an error occurs while requesting or executing the TwiML
                defined by ``sms_url``.
            sms_method: The HTTP method that we should use to call ``sms_url``. Can be: ``GET`` or ``POST`` and defaults
                to ``POST``.
            sms_url: The URL we should call when the new phone number receives an incoming SMS message.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``GET`` or
                ``POST`` and defaults to ``POST``.
            voice_application_sid: The SID of the application we should use to handle calls to the new phone number. If
                a ``voice_application_sid`` is present, we ignore all of the voice urls and use only those set on the
                application. Setting a ``voice_application_sid`` will automatically delete your ``trunk_sid`` and vice
                versa.
            voice_caller_id_lookup: Whether to lookup the caller's name from the CNAM database and post it to your app.
                Can be: ``true`` or ``false`` and defaults to ``false``.
            voice_fallback_method: The HTTP method that we should use to call ``voice_fallback_url``. Can be: ``GET`` or
                ``POST`` and defaults to ``POST``.
            voice_fallback_url: The URL that we should call when an error occurs retrieving or executing the TwiML
                requested by ``url``.
            voice_method: The HTTP method that we should use to call ``voice_url``. Can be: ``GET`` or ``POST`` and
                defaults to ``POST``.
            voice_url: The URL that we should call to answer a call to the new phone number. The ``voice_url`` will not
                be called if a ``voice_application_sid`` or a ``trunk_sid`` is set.
            emergency_status: The parameter displays if emergency calling is enabled for this number. Active numbers may
                place emergency calls by dialing valid emergency numbers for the country.
            emergency_address_sid: The SID of the emergency address configuration to use for emergency calling from the
                new phone number.
            trunk_sid: The SID of the Trunk we should use to handle calls to the new phone number. If a ``trunk_sid`` is
                present, we ignore all of the voice urls and voice applications and use only those set on the Trunk.
                Setting a ``trunk_sid`` will automatically delete your ``voice_application_sid`` and vice versa.
            identity_sid: The SID of the Identity resource that we should associate with the new phone number. Some
                regions require an identity to meet local regulations.
            address_sid: The SID of the Address resource we should associate with the new phone number. Some regions
                require addresses to meet local regulations.
            voice_receive_mode: Value sent with the request.
            bundle_sid: The SID of the Bundle resource that you associate with the phone number. Some regions require a
                Bundle to meet local Regulations.
            phone_number: The phone number to purchase specified in `E.164
                <https://www.twilio.com/docs/glossary/what-e164>`__ format. E.164 phone numbers consist of a + followed
                by the country code and subscriber number without punctuation characters. For example, +14155551234.
            area_code: The desired area code for your new incoming phone number. Can be any three-digit, US or Canada
                area code. We will provision an available phone number within this area code for you. **You must provide
                an ``area_code`` or a ``phone_number``.** (US and Canada only).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_incoming_phone_number(
            account_sid,
            api_version=api_version,
            friendly_name=friendly_name,
            sms_application_sid=sms_application_sid,
            sms_fallback_method=sms_fallback_method,
            sms_fallback_url=sms_fallback_url,
            sms_method=sms_method,
            sms_url=sms_url,
            status_callback=status_callback,
            status_callback_method=status_callback_method,
            voice_application_sid=voice_application_sid,
            voice_caller_id_lookup=voice_caller_id_lookup,
            voice_fallback_method=voice_fallback_method,
            voice_fallback_url=voice_fallback_url,
            voice_method=voice_method,
            voice_url=voice_url,
            emergency_status=emergency_status,
            emergency_address_sid=emergency_address_sid,
            trunk_sid=trunk_sid,
            identity_sid=identity_sid,
            address_sid=address_sid,
            voice_receive_mode=voice_receive_mode,
            bundle_sid=bundle_sid,
            phone_number=phone_number,
            area_code=area_code,
            request_options=request_options,
        ).unwrap()

    def delete_incoming_phone_number(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a phone-numbers belonging to the account used to make the request.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                IncomingPhoneNumber resources to delete.
            sid: The Twilio-provided string that uniquely identifies the IncomingPhoneNumber resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_incoming_phone_number(
            account_sid, sid, request_options=request_options
        ).unwrap()

    def fetch_incoming_phone_number(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountIncomingPhoneNumber:
        """Fetch an incoming-phone-number belonging to the account used to make the request.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                IncomingPhoneNumber resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the IncomingPhoneNumber resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_incoming_phone_number(
            account_sid, sid, request_options=request_options
        ).unwrap()

    def list_incoming_phone_number(
        self,
        account_sid: str,
        *,
        beta: bool | None = None,
        friendly_name: str | None = None,
        phone_number: str | None = None,
        origin: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListIncomingPhoneNumberResponse:
        """Retrieve a list of incoming-phone-numbers belonging to the account used to make the request.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                IncomingPhoneNumber resources to read.
            beta: Whether to include phone numbers new to the Twilio platform. Can be: ``true`` or ``false`` and the
                default is ``true``.
            friendly_name: A string that identifies the IncomingPhoneNumber resources to read.
            phone_number: The phone numbers of the IncomingPhoneNumber resources to read. You can specify partial
                numbers and use '*' as a wildcard for any digit.
            origin: Whether to include phone numbers based on their origin. Can be: ``twilio`` or ``hosted``. By
                default, phone numbers of all origin are included.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_incoming_phone_number(
            account_sid,
            beta=beta,
            friendly_name=friendly_name,
            phone_number=phone_number,
            origin=origin,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_incoming_phone_number(
        self,
        account_sid_template: str,
        sid: str,
        *,
        account_sid: str | None = None,
        api_version: str | None = None,
        friendly_name: str | None = None,
        sms_application_sid: str | None = None,
        sms_fallback_method: SmsFallbackMethod9OrStr | None = None,
        sms_fallback_url: str | None = None,
        sms_method: SmsMethod9OrStr | None = None,
        sms_url: str | None = None,
        status_callback: str | None = None,
        status_callback_method: StatusCallbackMethod10OrStr | None = None,
        voice_application_sid: str | None = None,
        voice_caller_id_lookup: bool | None = None,
        voice_fallback_method: VoiceFallbackMethod9OrStr | None = None,
        voice_fallback_url: str | None = None,
        voice_method: VoiceMethod9OrStr | None = None,
        voice_url: str | None = None,
        emergency_status: IncomingPhoneNumberEnumEmergencyStatusOrStr | None = None,
        emergency_address_sid: str | None = None,
        trunk_sid: str | None = None,
        voice_receive_mode: IncomingPhoneNumberEnumVoiceReceiveModeOrStr | None = None,
        identity_sid: str | None = None,
        address_sid: str | None = None,
        bundle_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountIncomingPhoneNumber:
        """Update an incoming-phone-number instance.

        Args:
            account_sid_template: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created
                the IncomingPhoneNumber resource to update. For more information, see `Exchanging Numbers Between
                Subaccounts <https://www.twilio.com/docs/iam/api/subaccounts#exchanging-numbers>`__.
            sid: The Twilio-provided string that uniquely identifies the IncomingPhoneNumber resource to update.
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                IncomingPhoneNumber resource to update. For more information, see `Exchanging Numbers Between
                Subaccounts <https://www.twilio.com/docs/iam/api/subaccounts#exchanging-numbers>`__.
            api_version: The API version to use for incoming calls made to the phone number. The default is
                ``2010-04-01``.
            friendly_name: A descriptive string that you created to describe this phone number. It can be up to 64
                characters long. By default, this is a formatted version of the phone number.
            sms_application_sid: The SID of the application that should handle SMS messages sent to the number. If an
                ``sms_application_sid`` is present, we ignore all of the ``sms_*_url`` urls and use those set on the
                application.
            sms_fallback_method: The HTTP method that we should use to call ``sms_fallback_url``. Can be: ``GET`` or
                ``POST`` and defaults to ``POST``.
            sms_fallback_url: The URL that we should call when an error occurs while requesting or executing the TwiML
                defined by ``sms_url``.
            sms_method: The HTTP method that we should use to call ``sms_url``. Can be: ``GET`` or ``POST`` and defaults
                to ``POST``.
            sms_url: The URL we should call when the phone number receives an incoming SMS message.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``GET`` or
                ``POST`` and defaults to ``POST``.
            voice_application_sid: The SID of the application we should use to handle phone calls to the phone number.
                If a ``voice_application_sid`` is present, we ignore all of the voice urls and use only those set on the
                application. Setting a ``voice_application_sid`` will automatically delete your ``trunk_sid`` and vice
                versa.
            voice_caller_id_lookup: Whether to lookup the caller's name from the CNAM database and post it to your app.
                Can be: ``true`` or ``false`` and defaults to ``false``.
            voice_fallback_method: The HTTP method that we should use to call ``voice_fallback_url``. Can be: ``GET`` or
                ``POST`` and defaults to ``POST``.
            voice_fallback_url: The URL that we should call when an error occurs retrieving or executing the TwiML
                requested by ``url``.
            voice_method: The HTTP method that we should use to call ``voice_url``. Can be: ``GET`` or ``POST`` and
                defaults to ``POST``.
            voice_url: The URL that we should call to answer a call to the phone number. The ``voice_url`` will not be
                called if a ``voice_application_sid`` or a ``trunk_sid`` is set.
            emergency_status: The parameter displays if emergency calling is enabled for this number. Active numbers may
                place emergency calls by dialing valid emergency numbers for the country.
            emergency_address_sid: The SID of the emergency address configuration to use for emergency calling from this
                phone number.
            trunk_sid: The SID of the Trunk we should use to handle phone calls to the phone number. If a ``trunk_sid``
                is present, we ignore all of the voice urls and voice applications and use only those set on the Trunk.
                Setting a ``trunk_sid`` will automatically delete your ``voice_application_sid`` and vice versa.
            voice_receive_mode: Value sent with the request.
            identity_sid: The SID of the Identity resource that we should associate with the phone number. Some regions
                require an identity to meet local regulations.
            address_sid: The SID of the Address resource we should associate with the phone number. Some regions require
                addresses to meet local regulations.
            bundle_sid: The SID of the Bundle resource that you associate with the phone number. Some regions require a
                Bundle to meet local Regulations.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_incoming_phone_number(
            account_sid_template,
            sid,
            account_sid=account_sid,
            api_version=api_version,
            friendly_name=friendly_name,
            sms_application_sid=sms_application_sid,
            sms_fallback_method=sms_fallback_method,
            sms_fallback_url=sms_fallback_url,
            sms_method=sms_method,
            sms_url=sms_url,
            status_callback=status_callback,
            status_callback_method=status_callback_method,
            voice_application_sid=voice_application_sid,
            voice_caller_id_lookup=voice_caller_id_lookup,
            voice_fallback_method=voice_fallback_method,
            voice_fallback_url=voice_fallback_url,
            voice_method=voice_method,
            voice_url=voice_url,
            emergency_status=emergency_status,
            emergency_address_sid=emergency_address_sid,
            trunk_sid=trunk_sid,
            voice_receive_mode=voice_receive_mode,
            identity_sid=identity_sid,
            address_sid=address_sid,
            bundle_sid=bundle_sid,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401IncomingPhoneNumberWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401IncomingPhoneNumber:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401IncomingPhoneNumberWithRawResponse(client, server, auth)

    async def create_incoming_phone_number(
        self,
        account_sid: str,
        *,
        api_version: str | None = None,
        friendly_name: str | None = None,
        sms_application_sid: str | None = None,
        sms_fallback_method: SmsFallbackMethod9OrStr | None = None,
        sms_fallback_url: str | None = None,
        sms_method: SmsMethod9OrStr | None = None,
        sms_url: str | None = None,
        status_callback: str | None = None,
        status_callback_method: StatusCallbackMethod10OrStr | None = None,
        voice_application_sid: str | None = None,
        voice_caller_id_lookup: bool | None = None,
        voice_fallback_method: VoiceFallbackMethod9OrStr | None = None,
        voice_fallback_url: str | None = None,
        voice_method: VoiceMethod9OrStr | None = None,
        voice_url: str | None = None,
        emergency_status: IncomingPhoneNumberEnumEmergencyStatusOrStr | None = None,
        emergency_address_sid: str | None = None,
        trunk_sid: str | None = None,
        identity_sid: str | None = None,
        address_sid: str | None = None,
        voice_receive_mode: IncomingPhoneNumberEnumVoiceReceiveModeOrStr | None = None,
        bundle_sid: str | None = None,
        phone_number: str | None = None,
        area_code: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountIncomingPhoneNumber:
        """Purchase a phone-number for the account.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            api_version: The API version to use for incoming calls made to the new phone number. The default is
                ``2010-04-01``.
            friendly_name: A descriptive string that you created to describe the new phone number. It can be up to 64
                characters long. By default, this is a formatted version of the new phone number.
            sms_application_sid: The SID of the application that should handle SMS messages sent to the new phone
                number. If an ``sms_application_sid`` is present, we ignore all of the ``sms_*_url`` urls and use those
                set on the application.
            sms_fallback_method: The HTTP method that we should use to call ``sms_fallback_url``. Can be: ``GET`` or
                ``POST`` and defaults to ``POST``.
            sms_fallback_url: The URL that we should call when an error occurs while requesting or executing the TwiML
                defined by ``sms_url``.
            sms_method: The HTTP method that we should use to call ``sms_url``. Can be: ``GET`` or ``POST`` and defaults
                to ``POST``.
            sms_url: The URL we should call when the new phone number receives an incoming SMS message.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``GET`` or
                ``POST`` and defaults to ``POST``.
            voice_application_sid: The SID of the application we should use to handle calls to the new phone number. If
                a ``voice_application_sid`` is present, we ignore all of the voice urls and use only those set on the
                application. Setting a ``voice_application_sid`` will automatically delete your ``trunk_sid`` and vice
                versa.
            voice_caller_id_lookup: Whether to lookup the caller's name from the CNAM database and post it to your app.
                Can be: ``true`` or ``false`` and defaults to ``false``.
            voice_fallback_method: The HTTP method that we should use to call ``voice_fallback_url``. Can be: ``GET`` or
                ``POST`` and defaults to ``POST``.
            voice_fallback_url: The URL that we should call when an error occurs retrieving or executing the TwiML
                requested by ``url``.
            voice_method: The HTTP method that we should use to call ``voice_url``. Can be: ``GET`` or ``POST`` and
                defaults to ``POST``.
            voice_url: The URL that we should call to answer a call to the new phone number. The ``voice_url`` will not
                be called if a ``voice_application_sid`` or a ``trunk_sid`` is set.
            emergency_status: The parameter displays if emergency calling is enabled for this number. Active numbers may
                place emergency calls by dialing valid emergency numbers for the country.
            emergency_address_sid: The SID of the emergency address configuration to use for emergency calling from the
                new phone number.
            trunk_sid: The SID of the Trunk we should use to handle calls to the new phone number. If a ``trunk_sid`` is
                present, we ignore all of the voice urls and voice applications and use only those set on the Trunk.
                Setting a ``trunk_sid`` will automatically delete your ``voice_application_sid`` and vice versa.
            identity_sid: The SID of the Identity resource that we should associate with the new phone number. Some
                regions require an identity to meet local regulations.
            address_sid: The SID of the Address resource we should associate with the new phone number. Some regions
                require addresses to meet local regulations.
            voice_receive_mode: Value sent with the request.
            bundle_sid: The SID of the Bundle resource that you associate with the phone number. Some regions require a
                Bundle to meet local Regulations.
            phone_number: The phone number to purchase specified in `E.164
                <https://www.twilio.com/docs/glossary/what-e164>`__ format. E.164 phone numbers consist of a + followed
                by the country code and subscriber number without punctuation characters. For example, +14155551234.
            area_code: The desired area code for your new incoming phone number. Can be any three-digit, US or Canada
                area code. We will provision an available phone number within this area code for you. **You must provide
                an ``area_code`` or a ``phone_number``.** (US and Canada only).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_incoming_phone_number(
                account_sid,
                api_version=api_version,
                friendly_name=friendly_name,
                sms_application_sid=sms_application_sid,
                sms_fallback_method=sms_fallback_method,
                sms_fallback_url=sms_fallback_url,
                sms_method=sms_method,
                sms_url=sms_url,
                status_callback=status_callback,
                status_callback_method=status_callback_method,
                voice_application_sid=voice_application_sid,
                voice_caller_id_lookup=voice_caller_id_lookup,
                voice_fallback_method=voice_fallback_method,
                voice_fallback_url=voice_fallback_url,
                voice_method=voice_method,
                voice_url=voice_url,
                emergency_status=emergency_status,
                emergency_address_sid=emergency_address_sid,
                trunk_sid=trunk_sid,
                identity_sid=identity_sid,
                address_sid=address_sid,
                voice_receive_mode=voice_receive_mode,
                bundle_sid=bundle_sid,
                phone_number=phone_number,
                area_code=area_code,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_incoming_phone_number(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a phone-numbers belonging to the account used to make the request.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                IncomingPhoneNumber resources to delete.
            sid: The Twilio-provided string that uniquely identifies the IncomingPhoneNumber resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_incoming_phone_number(
                account_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def fetch_incoming_phone_number(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountIncomingPhoneNumber:
        """Fetch an incoming-phone-number belonging to the account used to make the request.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                IncomingPhoneNumber resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the IncomingPhoneNumber resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_incoming_phone_number(account_sid, sid, request_options=request_options)
        ).unwrap()

    async def list_incoming_phone_number(
        self,
        account_sid: str,
        *,
        beta: bool | None = None,
        friendly_name: str | None = None,
        phone_number: str | None = None,
        origin: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListIncomingPhoneNumberResponse:
        """Retrieve a list of incoming-phone-numbers belonging to the account used to make the request.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                IncomingPhoneNumber resources to read.
            beta: Whether to include phone numbers new to the Twilio platform. Can be: ``true`` or ``false`` and the
                default is ``true``.
            friendly_name: A string that identifies the IncomingPhoneNumber resources to read.
            phone_number: The phone numbers of the IncomingPhoneNumber resources to read. You can specify partial
                numbers and use '*' as a wildcard for any digit.
            origin: Whether to include phone numbers based on their origin. Can be: ``twilio`` or ``hosted``. By
                default, phone numbers of all origin are included.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_incoming_phone_number(
                account_sid,
                beta=beta,
                friendly_name=friendly_name,
                phone_number=phone_number,
                origin=origin,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_incoming_phone_number(
        self,
        account_sid_template: str,
        sid: str,
        *,
        account_sid: str | None = None,
        api_version: str | None = None,
        friendly_name: str | None = None,
        sms_application_sid: str | None = None,
        sms_fallback_method: SmsFallbackMethod9OrStr | None = None,
        sms_fallback_url: str | None = None,
        sms_method: SmsMethod9OrStr | None = None,
        sms_url: str | None = None,
        status_callback: str | None = None,
        status_callback_method: StatusCallbackMethod10OrStr | None = None,
        voice_application_sid: str | None = None,
        voice_caller_id_lookup: bool | None = None,
        voice_fallback_method: VoiceFallbackMethod9OrStr | None = None,
        voice_fallback_url: str | None = None,
        voice_method: VoiceMethod9OrStr | None = None,
        voice_url: str | None = None,
        emergency_status: IncomingPhoneNumberEnumEmergencyStatusOrStr | None = None,
        emergency_address_sid: str | None = None,
        trunk_sid: str | None = None,
        voice_receive_mode: IncomingPhoneNumberEnumVoiceReceiveModeOrStr | None = None,
        identity_sid: str | None = None,
        address_sid: str | None = None,
        bundle_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountIncomingPhoneNumber:
        """Update an incoming-phone-number instance.

        Args:
            account_sid_template: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created
                the IncomingPhoneNumber resource to update. For more information, see `Exchanging Numbers Between
                Subaccounts <https://www.twilio.com/docs/iam/api/subaccounts#exchanging-numbers>`__.
            sid: The Twilio-provided string that uniquely identifies the IncomingPhoneNumber resource to update.
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                IncomingPhoneNumber resource to update. For more information, see `Exchanging Numbers Between
                Subaccounts <https://www.twilio.com/docs/iam/api/subaccounts#exchanging-numbers>`__.
            api_version: The API version to use for incoming calls made to the phone number. The default is
                ``2010-04-01``.
            friendly_name: A descriptive string that you created to describe this phone number. It can be up to 64
                characters long. By default, this is a formatted version of the phone number.
            sms_application_sid: The SID of the application that should handle SMS messages sent to the number. If an
                ``sms_application_sid`` is present, we ignore all of the ``sms_*_url`` urls and use those set on the
                application.
            sms_fallback_method: The HTTP method that we should use to call ``sms_fallback_url``. Can be: ``GET`` or
                ``POST`` and defaults to ``POST``.
            sms_fallback_url: The URL that we should call when an error occurs while requesting or executing the TwiML
                defined by ``sms_url``.
            sms_method: The HTTP method that we should use to call ``sms_url``. Can be: ``GET`` or ``POST`` and defaults
                to ``POST``.
            sms_url: The URL we should call when the phone number receives an incoming SMS message.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``GET`` or
                ``POST`` and defaults to ``POST``.
            voice_application_sid: The SID of the application we should use to handle phone calls to the phone number.
                If a ``voice_application_sid`` is present, we ignore all of the voice urls and use only those set on the
                application. Setting a ``voice_application_sid`` will automatically delete your ``trunk_sid`` and vice
                versa.
            voice_caller_id_lookup: Whether to lookup the caller's name from the CNAM database and post it to your app.
                Can be: ``true`` or ``false`` and defaults to ``false``.
            voice_fallback_method: The HTTP method that we should use to call ``voice_fallback_url``. Can be: ``GET`` or
                ``POST`` and defaults to ``POST``.
            voice_fallback_url: The URL that we should call when an error occurs retrieving or executing the TwiML
                requested by ``url``.
            voice_method: The HTTP method that we should use to call ``voice_url``. Can be: ``GET`` or ``POST`` and
                defaults to ``POST``.
            voice_url: The URL that we should call to answer a call to the phone number. The ``voice_url`` will not be
                called if a ``voice_application_sid`` or a ``trunk_sid`` is set.
            emergency_status: The parameter displays if emergency calling is enabled for this number. Active numbers may
                place emergency calls by dialing valid emergency numbers for the country.
            emergency_address_sid: The SID of the emergency address configuration to use for emergency calling from this
                phone number.
            trunk_sid: The SID of the Trunk we should use to handle phone calls to the phone number. If a ``trunk_sid``
                is present, we ignore all of the voice urls and voice applications and use only those set on the Trunk.
                Setting a ``trunk_sid`` will automatically delete your ``voice_application_sid`` and vice versa.
            voice_receive_mode: Value sent with the request.
            identity_sid: The SID of the Identity resource that we should associate with the phone number. Some regions
                require an identity to meet local regulations.
            address_sid: The SID of the Address resource we should associate with the phone number. Some regions require
                addresses to meet local regulations.
            bundle_sid: The SID of the Bundle resource that you associate with the phone number. Some regions require a
                Bundle to meet local Regulations.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_incoming_phone_number(
                account_sid_template,
                sid,
                account_sid=account_sid,
                api_version=api_version,
                friendly_name=friendly_name,
                sms_application_sid=sms_application_sid,
                sms_fallback_method=sms_fallback_method,
                sms_fallback_url=sms_fallback_url,
                sms_method=sms_method,
                sms_url=sms_url,
                status_callback=status_callback,
                status_callback_method=status_callback_method,
                voice_application_sid=voice_application_sid,
                voice_caller_id_lookup=voice_caller_id_lookup,
                voice_fallback_method=voice_fallback_method,
                voice_fallback_url=voice_fallback_url,
                voice_method=voice_method,
                voice_url=voice_url,
                emergency_status=emergency_status,
                emergency_address_sid=emergency_address_sid,
                trunk_sid=trunk_sid,
                voice_receive_mode=voice_receive_mode,
                identity_sid=identity_sid,
                address_sid=address_sid,
                bundle_sid=bundle_sid,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401IncomingPhoneNumberWithRawResponse:
        return self._with_raw_response


class Api20100401IncomingPhoneNumberWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_incoming_phone_number(
        self,
        account_sid: str,
        *,
        api_version: str | None = None,
        friendly_name: str | None = None,
        sms_application_sid: str | None = None,
        sms_fallback_method: SmsFallbackMethod9OrStr | None = None,
        sms_fallback_url: str | None = None,
        sms_method: SmsMethod9OrStr | None = None,
        sms_url: str | None = None,
        status_callback: str | None = None,
        status_callback_method: StatusCallbackMethod10OrStr | None = None,
        voice_application_sid: str | None = None,
        voice_caller_id_lookup: bool | None = None,
        voice_fallback_method: VoiceFallbackMethod9OrStr | None = None,
        voice_fallback_url: str | None = None,
        voice_method: VoiceMethod9OrStr | None = None,
        voice_url: str | None = None,
        emergency_status: IncomingPhoneNumberEnumEmergencyStatusOrStr | None = None,
        emergency_address_sid: str | None = None,
        trunk_sid: str | None = None,
        identity_sid: str | None = None,
        address_sid: str | None = None,
        voice_receive_mode: IncomingPhoneNumberEnumVoiceReceiveModeOrStr | None = None,
        bundle_sid: str | None = None,
        phone_number: str | None = None,
        area_code: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountIncomingPhoneNumber, RawError]:
        """Purchase a phone-number for the account.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            api_version: The API version to use for incoming calls made to the new phone number. The default is
                ``2010-04-01``.
            friendly_name: A descriptive string that you created to describe the new phone number. It can be up to 64
                characters long. By default, this is a formatted version of the new phone number.
            sms_application_sid: The SID of the application that should handle SMS messages sent to the new phone
                number. If an ``sms_application_sid`` is present, we ignore all of the ``sms_*_url`` urls and use those
                set on the application.
            sms_fallback_method: The HTTP method that we should use to call ``sms_fallback_url``. Can be: ``GET`` or
                ``POST`` and defaults to ``POST``.
            sms_fallback_url: The URL that we should call when an error occurs while requesting or executing the TwiML
                defined by ``sms_url``.
            sms_method: The HTTP method that we should use to call ``sms_url``. Can be: ``GET`` or ``POST`` and defaults
                to ``POST``.
            sms_url: The URL we should call when the new phone number receives an incoming SMS message.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``GET`` or
                ``POST`` and defaults to ``POST``.
            voice_application_sid: The SID of the application we should use to handle calls to the new phone number. If
                a ``voice_application_sid`` is present, we ignore all of the voice urls and use only those set on the
                application. Setting a ``voice_application_sid`` will automatically delete your ``trunk_sid`` and vice
                versa.
            voice_caller_id_lookup: Whether to lookup the caller's name from the CNAM database and post it to your app.
                Can be: ``true`` or ``false`` and defaults to ``false``.
            voice_fallback_method: The HTTP method that we should use to call ``voice_fallback_url``. Can be: ``GET`` or
                ``POST`` and defaults to ``POST``.
            voice_fallback_url: The URL that we should call when an error occurs retrieving or executing the TwiML
                requested by ``url``.
            voice_method: The HTTP method that we should use to call ``voice_url``. Can be: ``GET`` or ``POST`` and
                defaults to ``POST``.
            voice_url: The URL that we should call to answer a call to the new phone number. The ``voice_url`` will not
                be called if a ``voice_application_sid`` or a ``trunk_sid`` is set.
            emergency_status: The parameter displays if emergency calling is enabled for this number. Active numbers may
                place emergency calls by dialing valid emergency numbers for the country.
            emergency_address_sid: The SID of the emergency address configuration to use for emergency calling from the
                new phone number.
            trunk_sid: The SID of the Trunk we should use to handle calls to the new phone number. If a ``trunk_sid`` is
                present, we ignore all of the voice urls and voice applications and use only those set on the Trunk.
                Setting a ``trunk_sid`` will automatically delete your ``voice_application_sid`` and vice versa.
            identity_sid: The SID of the Identity resource that we should associate with the new phone number. Some
                regions require an identity to meet local regulations.
            address_sid: The SID of the Address resource we should associate with the new phone number. Some regions
                require addresses to meet local regulations.
            voice_receive_mode: Value sent with the request.
            bundle_sid: The SID of the Bundle resource that you associate with the phone number. Some regions require a
                Bundle to meet local Regulations.
            phone_number: The phone number to purchase specified in `E.164
                <https://www.twilio.com/docs/glossary/what-e164>`__ format. E.164 phone numbers consist of a + followed
                by the country code and subscriber number without punctuation characters. For example, +14155551234.
            area_code: The desired area code for your new incoming phone number. Can be any three-digit, US or Canada
                area code. We will provision an available phone number within this area code for you. **You must provide
                an ``area_code`` or a ``phone_number``.** (US and Canada only).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            body=form_body(
                [
                    param[str | None]("ApiVersion", api_version),
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("SmsApplicationSid", sms_application_sid),
                    param[SmsFallbackMethod9OrStr | None]("SmsFallbackMethod", sms_fallback_method),
                    param[str | None]("SmsFallbackUrl", sms_fallback_url),
                    param[SmsMethod9OrStr | None]("SmsMethod", sms_method),
                    param[str | None]("SmsUrl", sms_url),
                    param[str | None]("StatusCallback", status_callback),
                    param[StatusCallbackMethod10OrStr | None]("StatusCallbackMethod", status_callback_method),
                    param[str | None]("VoiceApplicationSid", voice_application_sid),
                    param[bool | None]("VoiceCallerIdLookup", voice_caller_id_lookup),
                    param[VoiceFallbackMethod9OrStr | None]("VoiceFallbackMethod", voice_fallback_method),
                    param[str | None]("VoiceFallbackUrl", voice_fallback_url),
                    param[VoiceMethod9OrStr | None]("VoiceMethod", voice_method),
                    param[str | None]("VoiceUrl", voice_url),
                    param[IncomingPhoneNumberEnumEmergencyStatusOrStr | None]("EmergencyStatus", emergency_status),
                    param[str | None]("EmergencyAddressSid", emergency_address_sid),
                    param[str | None]("TrunkSid", trunk_sid),
                    param[str | None]("IdentitySid", identity_sid),
                    param[str | None]("AddressSid", address_sid),
                    param[IncomingPhoneNumberEnumVoiceReceiveModeOrStr | None]("VoiceReceiveMode", voice_receive_mode),
                    param[str | None]("BundleSid", bundle_sid),
                    param[str | None]("PhoneNumber", phone_number),
                    param[str | None]("AreaCode", area_code),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountIncomingPhoneNumber],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_incoming_phone_number(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a phone-numbers belonging to the account used to make the request.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                IncomingPhoneNumber resources to delete.
            sid: The Twilio-provided string that uniquely identifies the IncomingPhoneNumber resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_incoming_phone_number(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountIncomingPhoneNumber, RawError]:
        """Fetch an incoming-phone-number belonging to the account used to make the request.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                IncomingPhoneNumber resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the IncomingPhoneNumber resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountIncomingPhoneNumber],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_incoming_phone_number(
        self,
        account_sid: str,
        *,
        beta: bool | None = None,
        friendly_name: str | None = None,
        phone_number: str | None = None,
        origin: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListIncomingPhoneNumberResponse, RawError]:
        """Retrieve a list of incoming-phone-numbers belonging to the account used to make the request.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                IncomingPhoneNumber resources to read.
            beta: Whether to include phone numbers new to the Twilio platform. Can be: ``true`` or ``false`` and the
                default is ``true``.
            friendly_name: A string that identifies the IncomingPhoneNumber resources to read.
            phone_number: The phone numbers of the IncomingPhoneNumber resources to read. You can specify partial
                numbers and use '*' as a wildcard for any digit.
            origin: Whether to include phone numbers based on their origin. Can be: ``twilio`` or ``hosted``. By
                default, phone numbers of all origin are included.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            query_params=[
                param[bool | None]("Beta", beta),
                param[str | None]("FriendlyName", friendly_name),
                param[str | None]("PhoneNumber", phone_number),
                param[str | None]("Origin", origin),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListIncomingPhoneNumberResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_incoming_phone_number(
        self,
        account_sid_template: str,
        sid: str,
        *,
        account_sid: str | None = None,
        api_version: str | None = None,
        friendly_name: str | None = None,
        sms_application_sid: str | None = None,
        sms_fallback_method: SmsFallbackMethod9OrStr | None = None,
        sms_fallback_url: str | None = None,
        sms_method: SmsMethod9OrStr | None = None,
        sms_url: str | None = None,
        status_callback: str | None = None,
        status_callback_method: StatusCallbackMethod10OrStr | None = None,
        voice_application_sid: str | None = None,
        voice_caller_id_lookup: bool | None = None,
        voice_fallback_method: VoiceFallbackMethod9OrStr | None = None,
        voice_fallback_url: str | None = None,
        voice_method: VoiceMethod9OrStr | None = None,
        voice_url: str | None = None,
        emergency_status: IncomingPhoneNumberEnumEmergencyStatusOrStr | None = None,
        emergency_address_sid: str | None = None,
        trunk_sid: str | None = None,
        voice_receive_mode: IncomingPhoneNumberEnumVoiceReceiveModeOrStr | None = None,
        identity_sid: str | None = None,
        address_sid: str | None = None,
        bundle_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountIncomingPhoneNumber, RawError]:
        """Update an incoming-phone-number instance.

        Args:
            account_sid_template: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created
                the IncomingPhoneNumber resource to update. For more information, see `Exchanging Numbers Between
                Subaccounts <https://www.twilio.com/docs/iam/api/subaccounts#exchanging-numbers>`__.
            sid: The Twilio-provided string that uniquely identifies the IncomingPhoneNumber resource to update.
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                IncomingPhoneNumber resource to update. For more information, see `Exchanging Numbers Between
                Subaccounts <https://www.twilio.com/docs/iam/api/subaccounts#exchanging-numbers>`__.
            api_version: The API version to use for incoming calls made to the phone number. The default is
                ``2010-04-01``.
            friendly_name: A descriptive string that you created to describe this phone number. It can be up to 64
                characters long. By default, this is a formatted version of the phone number.
            sms_application_sid: The SID of the application that should handle SMS messages sent to the number. If an
                ``sms_application_sid`` is present, we ignore all of the ``sms_*_url`` urls and use those set on the
                application.
            sms_fallback_method: The HTTP method that we should use to call ``sms_fallback_url``. Can be: ``GET`` or
                ``POST`` and defaults to ``POST``.
            sms_fallback_url: The URL that we should call when an error occurs while requesting or executing the TwiML
                defined by ``sms_url``.
            sms_method: The HTTP method that we should use to call ``sms_url``. Can be: ``GET`` or ``POST`` and defaults
                to ``POST``.
            sms_url: The URL we should call when the phone number receives an incoming SMS message.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``GET`` or
                ``POST`` and defaults to ``POST``.
            voice_application_sid: The SID of the application we should use to handle phone calls to the phone number.
                If a ``voice_application_sid`` is present, we ignore all of the voice urls and use only those set on the
                application. Setting a ``voice_application_sid`` will automatically delete your ``trunk_sid`` and vice
                versa.
            voice_caller_id_lookup: Whether to lookup the caller's name from the CNAM database and post it to your app.
                Can be: ``true`` or ``false`` and defaults to ``false``.
            voice_fallback_method: The HTTP method that we should use to call ``voice_fallback_url``. Can be: ``GET`` or
                ``POST`` and defaults to ``POST``.
            voice_fallback_url: The URL that we should call when an error occurs retrieving or executing the TwiML
                requested by ``url``.
            voice_method: The HTTP method that we should use to call ``voice_url``. Can be: ``GET`` or ``POST`` and
                defaults to ``POST``.
            voice_url: The URL that we should call to answer a call to the phone number. The ``voice_url`` will not be
                called if a ``voice_application_sid`` or a ``trunk_sid`` is set.
            emergency_status: The parameter displays if emergency calling is enabled for this number. Active numbers may
                place emergency calls by dialing valid emergency numbers for the country.
            emergency_address_sid: The SID of the emergency address configuration to use for emergency calling from this
                phone number.
            trunk_sid: The SID of the Trunk we should use to handle phone calls to the phone number. If a ``trunk_sid``
                is present, we ignore all of the voice urls and voice applications and use only those set on the Trunk.
                Setting a ``trunk_sid`` will automatically delete your ``voice_application_sid`` and vice versa.
            voice_receive_mode: Value sent with the request.
            identity_sid: The SID of the Identity resource that we should associate with the phone number. Some regions
                require an identity to meet local regulations.
            address_sid: The SID of the Address resource we should associate with the phone number. Some regions require
                addresses to meet local regulations.
            bundle_sid: The SID of the Bundle resource that you associate with the phone number. Some regions require a
                Bundle to meet local Regulations.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid_template), param[str]("Sid", sid)],
            body=form_body(
                [
                    param[str | None]("AccountSid", account_sid),
                    param[str | None]("ApiVersion", api_version),
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("SmsApplicationSid", sms_application_sid),
                    param[SmsFallbackMethod9OrStr | None]("SmsFallbackMethod", sms_fallback_method),
                    param[str | None]("SmsFallbackUrl", sms_fallback_url),
                    param[SmsMethod9OrStr | None]("SmsMethod", sms_method),
                    param[str | None]("SmsUrl", sms_url),
                    param[str | None]("StatusCallback", status_callback),
                    param[StatusCallbackMethod10OrStr | None]("StatusCallbackMethod", status_callback_method),
                    param[str | None]("VoiceApplicationSid", voice_application_sid),
                    param[bool | None]("VoiceCallerIdLookup", voice_caller_id_lookup),
                    param[VoiceFallbackMethod9OrStr | None]("VoiceFallbackMethod", voice_fallback_method),
                    param[str | None]("VoiceFallbackUrl", voice_fallback_url),
                    param[VoiceMethod9OrStr | None]("VoiceMethod", voice_method),
                    param[str | None]("VoiceUrl", voice_url),
                    param[IncomingPhoneNumberEnumEmergencyStatusOrStr | None]("EmergencyStatus", emergency_status),
                    param[str | None]("EmergencyAddressSid", emergency_address_sid),
                    param[str | None]("TrunkSid", trunk_sid),
                    param[IncomingPhoneNumberEnumVoiceReceiveModeOrStr | None]("VoiceReceiveMode", voice_receive_mode),
                    param[str | None]("IdentitySid", identity_sid),
                    param[str | None]("AddressSid", address_sid),
                    param[str | None]("BundleSid", bundle_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountIncomingPhoneNumber],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401IncomingPhoneNumberWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_incoming_phone_number(
        self,
        account_sid: str,
        *,
        api_version: str | None = None,
        friendly_name: str | None = None,
        sms_application_sid: str | None = None,
        sms_fallback_method: SmsFallbackMethod9OrStr | None = None,
        sms_fallback_url: str | None = None,
        sms_method: SmsMethod9OrStr | None = None,
        sms_url: str | None = None,
        status_callback: str | None = None,
        status_callback_method: StatusCallbackMethod10OrStr | None = None,
        voice_application_sid: str | None = None,
        voice_caller_id_lookup: bool | None = None,
        voice_fallback_method: VoiceFallbackMethod9OrStr | None = None,
        voice_fallback_url: str | None = None,
        voice_method: VoiceMethod9OrStr | None = None,
        voice_url: str | None = None,
        emergency_status: IncomingPhoneNumberEnumEmergencyStatusOrStr | None = None,
        emergency_address_sid: str | None = None,
        trunk_sid: str | None = None,
        identity_sid: str | None = None,
        address_sid: str | None = None,
        voice_receive_mode: IncomingPhoneNumberEnumVoiceReceiveModeOrStr | None = None,
        bundle_sid: str | None = None,
        phone_number: str | None = None,
        area_code: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountIncomingPhoneNumber, RawError]:
        """Purchase a phone-number for the account.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            api_version: The API version to use for incoming calls made to the new phone number. The default is
                ``2010-04-01``.
            friendly_name: A descriptive string that you created to describe the new phone number. It can be up to 64
                characters long. By default, this is a formatted version of the new phone number.
            sms_application_sid: The SID of the application that should handle SMS messages sent to the new phone
                number. If an ``sms_application_sid`` is present, we ignore all of the ``sms_*_url`` urls and use those
                set on the application.
            sms_fallback_method: The HTTP method that we should use to call ``sms_fallback_url``. Can be: ``GET`` or
                ``POST`` and defaults to ``POST``.
            sms_fallback_url: The URL that we should call when an error occurs while requesting or executing the TwiML
                defined by ``sms_url``.
            sms_method: The HTTP method that we should use to call ``sms_url``. Can be: ``GET`` or ``POST`` and defaults
                to ``POST``.
            sms_url: The URL we should call when the new phone number receives an incoming SMS message.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``GET`` or
                ``POST`` and defaults to ``POST``.
            voice_application_sid: The SID of the application we should use to handle calls to the new phone number. If
                a ``voice_application_sid`` is present, we ignore all of the voice urls and use only those set on the
                application. Setting a ``voice_application_sid`` will automatically delete your ``trunk_sid`` and vice
                versa.
            voice_caller_id_lookup: Whether to lookup the caller's name from the CNAM database and post it to your app.
                Can be: ``true`` or ``false`` and defaults to ``false``.
            voice_fallback_method: The HTTP method that we should use to call ``voice_fallback_url``. Can be: ``GET`` or
                ``POST`` and defaults to ``POST``.
            voice_fallback_url: The URL that we should call when an error occurs retrieving or executing the TwiML
                requested by ``url``.
            voice_method: The HTTP method that we should use to call ``voice_url``. Can be: ``GET`` or ``POST`` and
                defaults to ``POST``.
            voice_url: The URL that we should call to answer a call to the new phone number. The ``voice_url`` will not
                be called if a ``voice_application_sid`` or a ``trunk_sid`` is set.
            emergency_status: The parameter displays if emergency calling is enabled for this number. Active numbers may
                place emergency calls by dialing valid emergency numbers for the country.
            emergency_address_sid: The SID of the emergency address configuration to use for emergency calling from the
                new phone number.
            trunk_sid: The SID of the Trunk we should use to handle calls to the new phone number. If a ``trunk_sid`` is
                present, we ignore all of the voice urls and voice applications and use only those set on the Trunk.
                Setting a ``trunk_sid`` will automatically delete your ``voice_application_sid`` and vice versa.
            identity_sid: The SID of the Identity resource that we should associate with the new phone number. Some
                regions require an identity to meet local regulations.
            address_sid: The SID of the Address resource we should associate with the new phone number. Some regions
                require addresses to meet local regulations.
            voice_receive_mode: Value sent with the request.
            bundle_sid: The SID of the Bundle resource that you associate with the phone number. Some regions require a
                Bundle to meet local Regulations.
            phone_number: The phone number to purchase specified in `E.164
                <https://www.twilio.com/docs/glossary/what-e164>`__ format. E.164 phone numbers consist of a + followed
                by the country code and subscriber number without punctuation characters. For example, +14155551234.
            area_code: The desired area code for your new incoming phone number. Can be any three-digit, US or Canada
                area code. We will provision an available phone number within this area code for you. **You must provide
                an ``area_code`` or a ``phone_number``.** (US and Canada only).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            body=form_body(
                [
                    param[str | None]("ApiVersion", api_version),
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("SmsApplicationSid", sms_application_sid),
                    param[SmsFallbackMethod9OrStr | None]("SmsFallbackMethod", sms_fallback_method),
                    param[str | None]("SmsFallbackUrl", sms_fallback_url),
                    param[SmsMethod9OrStr | None]("SmsMethod", sms_method),
                    param[str | None]("SmsUrl", sms_url),
                    param[str | None]("StatusCallback", status_callback),
                    param[StatusCallbackMethod10OrStr | None]("StatusCallbackMethod", status_callback_method),
                    param[str | None]("VoiceApplicationSid", voice_application_sid),
                    param[bool | None]("VoiceCallerIdLookup", voice_caller_id_lookup),
                    param[VoiceFallbackMethod9OrStr | None]("VoiceFallbackMethod", voice_fallback_method),
                    param[str | None]("VoiceFallbackUrl", voice_fallback_url),
                    param[VoiceMethod9OrStr | None]("VoiceMethod", voice_method),
                    param[str | None]("VoiceUrl", voice_url),
                    param[IncomingPhoneNumberEnumEmergencyStatusOrStr | None]("EmergencyStatus", emergency_status),
                    param[str | None]("EmergencyAddressSid", emergency_address_sid),
                    param[str | None]("TrunkSid", trunk_sid),
                    param[str | None]("IdentitySid", identity_sid),
                    param[str | None]("AddressSid", address_sid),
                    param[IncomingPhoneNumberEnumVoiceReceiveModeOrStr | None]("VoiceReceiveMode", voice_receive_mode),
                    param[str | None]("BundleSid", bundle_sid),
                    param[str | None]("PhoneNumber", phone_number),
                    param[str | None]("AreaCode", area_code),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountIncomingPhoneNumber],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_incoming_phone_number(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a phone-numbers belonging to the account used to make the request.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                IncomingPhoneNumber resources to delete.
            sid: The Twilio-provided string that uniquely identifies the IncomingPhoneNumber resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_incoming_phone_number(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountIncomingPhoneNumber, RawError]:
        """Fetch an incoming-phone-number belonging to the account used to make the request.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                IncomingPhoneNumber resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the IncomingPhoneNumber resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountIncomingPhoneNumber],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_incoming_phone_number(
        self,
        account_sid: str,
        *,
        beta: bool | None = None,
        friendly_name: str | None = None,
        phone_number: str | None = None,
        origin: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListIncomingPhoneNumberResponse, RawError]:
        """Retrieve a list of incoming-phone-numbers belonging to the account used to make the request.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                IncomingPhoneNumber resources to read.
            beta: Whether to include phone numbers new to the Twilio platform. Can be: ``true`` or ``false`` and the
                default is ``true``.
            friendly_name: A string that identifies the IncomingPhoneNumber resources to read.
            phone_number: The phone numbers of the IncomingPhoneNumber resources to read. You can specify partial
                numbers and use '*' as a wildcard for any digit.
            origin: Whether to include phone numbers based on their origin. Can be: ``twilio`` or ``hosted``. By
                default, phone numbers of all origin are included.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            query_params=[
                param[bool | None]("Beta", beta),
                param[str | None]("FriendlyName", friendly_name),
                param[str | None]("PhoneNumber", phone_number),
                param[str | None]("Origin", origin),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListIncomingPhoneNumberResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_incoming_phone_number(
        self,
        account_sid_template: str,
        sid: str,
        *,
        account_sid: str | None = None,
        api_version: str | None = None,
        friendly_name: str | None = None,
        sms_application_sid: str | None = None,
        sms_fallback_method: SmsFallbackMethod9OrStr | None = None,
        sms_fallback_url: str | None = None,
        sms_method: SmsMethod9OrStr | None = None,
        sms_url: str | None = None,
        status_callback: str | None = None,
        status_callback_method: StatusCallbackMethod10OrStr | None = None,
        voice_application_sid: str | None = None,
        voice_caller_id_lookup: bool | None = None,
        voice_fallback_method: VoiceFallbackMethod9OrStr | None = None,
        voice_fallback_url: str | None = None,
        voice_method: VoiceMethod9OrStr | None = None,
        voice_url: str | None = None,
        emergency_status: IncomingPhoneNumberEnumEmergencyStatusOrStr | None = None,
        emergency_address_sid: str | None = None,
        trunk_sid: str | None = None,
        voice_receive_mode: IncomingPhoneNumberEnumVoiceReceiveModeOrStr | None = None,
        identity_sid: str | None = None,
        address_sid: str | None = None,
        bundle_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountIncomingPhoneNumber, RawError]:
        """Update an incoming-phone-number instance.

        Args:
            account_sid_template: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created
                the IncomingPhoneNumber resource to update. For more information, see `Exchanging Numbers Between
                Subaccounts <https://www.twilio.com/docs/iam/api/subaccounts#exchanging-numbers>`__.
            sid: The Twilio-provided string that uniquely identifies the IncomingPhoneNumber resource to update.
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                IncomingPhoneNumber resource to update. For more information, see `Exchanging Numbers Between
                Subaccounts <https://www.twilio.com/docs/iam/api/subaccounts#exchanging-numbers>`__.
            api_version: The API version to use for incoming calls made to the phone number. The default is
                ``2010-04-01``.
            friendly_name: A descriptive string that you created to describe this phone number. It can be up to 64
                characters long. By default, this is a formatted version of the phone number.
            sms_application_sid: The SID of the application that should handle SMS messages sent to the number. If an
                ``sms_application_sid`` is present, we ignore all of the ``sms_*_url`` urls and use those set on the
                application.
            sms_fallback_method: The HTTP method that we should use to call ``sms_fallback_url``. Can be: ``GET`` or
                ``POST`` and defaults to ``POST``.
            sms_fallback_url: The URL that we should call when an error occurs while requesting or executing the TwiML
                defined by ``sms_url``.
            sms_method: The HTTP method that we should use to call ``sms_url``. Can be: ``GET`` or ``POST`` and defaults
                to ``POST``.
            sms_url: The URL we should call when the phone number receives an incoming SMS message.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``GET`` or
                ``POST`` and defaults to ``POST``.
            voice_application_sid: The SID of the application we should use to handle phone calls to the phone number.
                If a ``voice_application_sid`` is present, we ignore all of the voice urls and use only those set on the
                application. Setting a ``voice_application_sid`` will automatically delete your ``trunk_sid`` and vice
                versa.
            voice_caller_id_lookup: Whether to lookup the caller's name from the CNAM database and post it to your app.
                Can be: ``true`` or ``false`` and defaults to ``false``.
            voice_fallback_method: The HTTP method that we should use to call ``voice_fallback_url``. Can be: ``GET`` or
                ``POST`` and defaults to ``POST``.
            voice_fallback_url: The URL that we should call when an error occurs retrieving or executing the TwiML
                requested by ``url``.
            voice_method: The HTTP method that we should use to call ``voice_url``. Can be: ``GET`` or ``POST`` and
                defaults to ``POST``.
            voice_url: The URL that we should call to answer a call to the phone number. The ``voice_url`` will not be
                called if a ``voice_application_sid`` or a ``trunk_sid`` is set.
            emergency_status: The parameter displays if emergency calling is enabled for this number. Active numbers may
                place emergency calls by dialing valid emergency numbers for the country.
            emergency_address_sid: The SID of the emergency address configuration to use for emergency calling from this
                phone number.
            trunk_sid: The SID of the Trunk we should use to handle phone calls to the phone number. If a ``trunk_sid``
                is present, we ignore all of the voice urls and voice applications and use only those set on the Trunk.
                Setting a ``trunk_sid`` will automatically delete your ``voice_application_sid`` and vice versa.
            voice_receive_mode: Value sent with the request.
            identity_sid: The SID of the Identity resource that we should associate with the phone number. Some regions
                require an identity to meet local regulations.
            address_sid: The SID of the Address resource we should associate with the phone number. Some regions require
                addresses to meet local regulations.
            bundle_sid: The SID of the Bundle resource that you associate with the phone number. Some regions require a
                Bundle to meet local Regulations.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid_template), param[str]("Sid", sid)],
            body=form_body(
                [
                    param[str | None]("AccountSid", account_sid),
                    param[str | None]("ApiVersion", api_version),
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("SmsApplicationSid", sms_application_sid),
                    param[SmsFallbackMethod9OrStr | None]("SmsFallbackMethod", sms_fallback_method),
                    param[str | None]("SmsFallbackUrl", sms_fallback_url),
                    param[SmsMethod9OrStr | None]("SmsMethod", sms_method),
                    param[str | None]("SmsUrl", sms_url),
                    param[str | None]("StatusCallback", status_callback),
                    param[StatusCallbackMethod10OrStr | None]("StatusCallbackMethod", status_callback_method),
                    param[str | None]("VoiceApplicationSid", voice_application_sid),
                    param[bool | None]("VoiceCallerIdLookup", voice_caller_id_lookup),
                    param[VoiceFallbackMethod9OrStr | None]("VoiceFallbackMethod", voice_fallback_method),
                    param[str | None]("VoiceFallbackUrl", voice_fallback_url),
                    param[VoiceMethod9OrStr | None]("VoiceMethod", voice_method),
                    param[str | None]("VoiceUrl", voice_url),
                    param[IncomingPhoneNumberEnumEmergencyStatusOrStr | None]("EmergencyStatus", emergency_status),
                    param[str | None]("EmergencyAddressSid", emergency_address_sid),
                    param[str | None]("TrunkSid", trunk_sid),
                    param[IncomingPhoneNumberEnumVoiceReceiveModeOrStr | None]("VoiceReceiveMode", voice_receive_mode),
                    param[str | None]("IdentitySid", identity_sid),
                    param[str | None]("AddressSid", address_sid),
                    param[str | None]("BundleSid", bundle_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountIncomingPhoneNumber],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
