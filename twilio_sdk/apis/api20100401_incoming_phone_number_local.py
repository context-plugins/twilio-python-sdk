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
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.api_v2010_account_incoming_phone_number_incoming_phone_number_local import (
    ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberLocal,
)
from ..models.enums.incoming_phone_number_local_enum_emergency_status import (
    IncomingPhoneNumberLocalEnumEmergencyStatusOrStr,
)
from ..models.enums.incoming_phone_number_local_enum_voice_receive_mode import (
    IncomingPhoneNumberLocalEnumVoiceReceiveModeOrStr,
)
from ..models.enums.sms_fallback_method9 import SmsFallbackMethod9OrStr
from ..models.enums.sms_method9 import SmsMethod9OrStr
from ..models.enums.status_callback_method10 import StatusCallbackMethod10OrStr
from ..models.enums.voice_fallback_method9 import VoiceFallbackMethod9OrStr
from ..models.enums.voice_method9 import VoiceMethod9OrStr
from ..models.list_incoming_phone_number_local_response import ListIncomingPhoneNumberLocalResponse
from ..server.server import Server


class Api20100401IncomingPhoneNumberLocal:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401IncomingPhoneNumberLocalWithRawResponse(client, server, auth)

    def create_incoming_phone_number_local(
        self,
        account_sid: str,
        phone_number: str,
        *,
        api_version: str | None = None,
        friendly_name: str | None = None,
        sms_application_sid: str | None = None,
        sms_fallback_method: SmsFallbackMethod9OrStr | None = None,
        sms_fallback_url: AnyUrl | None = None,
        sms_method: SmsMethod9OrStr | None = None,
        sms_url: AnyUrl | None = None,
        status_callback: AnyUrl | None = None,
        status_callback_method: StatusCallbackMethod10OrStr | None = None,
        voice_application_sid: str | None = None,
        voice_caller_id_lookup: bool | None = None,
        voice_fallback_method: VoiceFallbackMethod9OrStr | None = None,
        voice_fallback_url: AnyUrl | None = None,
        voice_method: VoiceMethod9OrStr | None = None,
        voice_url: AnyUrl | None = None,
        identity_sid: str | None = None,
        address_sid: str | None = None,
        emergency_status: IncomingPhoneNumberLocalEnumEmergencyStatusOrStr | None = None,
        emergency_address_sid: str | None = None,
        trunk_sid: str | None = None,
        voice_receive_mode: IncomingPhoneNumberLocalEnumVoiceReceiveModeOrStr | None = None,
        bundle_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberLocal:
        """Incoming local phone numbers on a Twilio account/project

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            phone_number: The phone number to purchase specified in `E.164
                <https://www.twilio.com/docs/glossary/what-e164>`__ format. E.164 phone numbers consist of a + followed
                by the country code and subscriber number without punctuation characters. For example, +14155551234.
            api_version: The API version to use for incoming calls made to the new phone number. The default is
                ``2010-04-01``.
            friendly_name: A descriptive string that you created to describe the new phone number. It can be up to 64
                characters long. By default, this is a formatted version of the phone number.
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
            identity_sid: The SID of the Identity resource that we should associate with the new phone number. Some
                regions require an identity to meet local regulations.
            address_sid: The SID of the Address resource we should associate with the new phone number. Some regions
                require addresses to meet local regulations.
            emergency_status: The parameter displays if emergency calling is enabled for this number. Active numbers may
                place emergency calls by dialing valid emergency numbers for the country.
            emergency_address_sid: The SID of the emergency address configuration to use for emergency calling from the
                new phone number.
            trunk_sid: The SID of the Trunk we should use to handle calls to the new phone number. If a ``trunk_sid`` is
                present, we ignore all of the voice urls and voice applications and use only those set on the Trunk.
                Setting a ``trunk_sid`` will automatically delete your ``voice_application_sid`` and vice versa.
            voice_receive_mode: Value sent with the request.
            bundle_sid: The SID of the Bundle resource that you associate with the phone number. Some regions require a
                Bundle to meet local Regulations.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_incoming_phone_number_local(
            account_sid,
            phone_number,
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
            identity_sid=identity_sid,
            address_sid=address_sid,
            emergency_status=emergency_status,
            emergency_address_sid=emergency_address_sid,
            trunk_sid=trunk_sid,
            voice_receive_mode=voice_receive_mode,
            bundle_sid=bundle_sid,
            request_options=request_options,
        ).unwrap()

    def list_incoming_phone_number_local(
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
    ) -> ListIncomingPhoneNumberLocalResponse:
        """Incoming local phone numbers on a Twilio account/project

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                resources to read.
            beta: Whether to include phone numbers new to the Twilio platform. Can be: ``true`` or ``false`` and the
                default is ``true``.
            friendly_name: A string that identifies the resources to read.
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
        return self._with_raw_response.list_incoming_phone_number_local(
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

    @property
    def with_raw_response(self) -> Api20100401IncomingPhoneNumberLocalWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401IncomingPhoneNumberLocal:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401IncomingPhoneNumberLocalWithRawResponse(client, server, auth)

    async def create_incoming_phone_number_local(
        self,
        account_sid: str,
        phone_number: str,
        *,
        api_version: str | None = None,
        friendly_name: str | None = None,
        sms_application_sid: str | None = None,
        sms_fallback_method: SmsFallbackMethod9OrStr | None = None,
        sms_fallback_url: AnyUrl | None = None,
        sms_method: SmsMethod9OrStr | None = None,
        sms_url: AnyUrl | None = None,
        status_callback: AnyUrl | None = None,
        status_callback_method: StatusCallbackMethod10OrStr | None = None,
        voice_application_sid: str | None = None,
        voice_caller_id_lookup: bool | None = None,
        voice_fallback_method: VoiceFallbackMethod9OrStr | None = None,
        voice_fallback_url: AnyUrl | None = None,
        voice_method: VoiceMethod9OrStr | None = None,
        voice_url: AnyUrl | None = None,
        identity_sid: str | None = None,
        address_sid: str | None = None,
        emergency_status: IncomingPhoneNumberLocalEnumEmergencyStatusOrStr | None = None,
        emergency_address_sid: str | None = None,
        trunk_sid: str | None = None,
        voice_receive_mode: IncomingPhoneNumberLocalEnumVoiceReceiveModeOrStr | None = None,
        bundle_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberLocal:
        """Incoming local phone numbers on a Twilio account/project

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            phone_number: The phone number to purchase specified in `E.164
                <https://www.twilio.com/docs/glossary/what-e164>`__ format. E.164 phone numbers consist of a + followed
                by the country code and subscriber number without punctuation characters. For example, +14155551234.
            api_version: The API version to use for incoming calls made to the new phone number. The default is
                ``2010-04-01``.
            friendly_name: A descriptive string that you created to describe the new phone number. It can be up to 64
                characters long. By default, this is a formatted version of the phone number.
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
            identity_sid: The SID of the Identity resource that we should associate with the new phone number. Some
                regions require an identity to meet local regulations.
            address_sid: The SID of the Address resource we should associate with the new phone number. Some regions
                require addresses to meet local regulations.
            emergency_status: The parameter displays if emergency calling is enabled for this number. Active numbers may
                place emergency calls by dialing valid emergency numbers for the country.
            emergency_address_sid: The SID of the emergency address configuration to use for emergency calling from the
                new phone number.
            trunk_sid: The SID of the Trunk we should use to handle calls to the new phone number. If a ``trunk_sid`` is
                present, we ignore all of the voice urls and voice applications and use only those set on the Trunk.
                Setting a ``trunk_sid`` will automatically delete your ``voice_application_sid`` and vice versa.
            voice_receive_mode: Value sent with the request.
            bundle_sid: The SID of the Bundle resource that you associate with the phone number. Some regions require a
                Bundle to meet local Regulations.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_incoming_phone_number_local(
                account_sid,
                phone_number,
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
                identity_sid=identity_sid,
                address_sid=address_sid,
                emergency_status=emergency_status,
                emergency_address_sid=emergency_address_sid,
                trunk_sid=trunk_sid,
                voice_receive_mode=voice_receive_mode,
                bundle_sid=bundle_sid,
                request_options=request_options,
            )
        ).unwrap()

    async def list_incoming_phone_number_local(
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
    ) -> ListIncomingPhoneNumberLocalResponse:
        """Incoming local phone numbers on a Twilio account/project

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                resources to read.
            beta: Whether to include phone numbers new to the Twilio platform. Can be: ``true`` or ``false`` and the
                default is ``true``.
            friendly_name: A string that identifies the resources to read.
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
            await self._with_raw_response.list_incoming_phone_number_local(
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

    @property
    def with_raw_response(self) -> AsyncApi20100401IncomingPhoneNumberLocalWithRawResponse:
        return self._with_raw_response


class Api20100401IncomingPhoneNumberLocalWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_incoming_phone_number_local(
        self,
        account_sid: str,
        phone_number: str,
        *,
        api_version: str | None = None,
        friendly_name: str | None = None,
        sms_application_sid: str | None = None,
        sms_fallback_method: SmsFallbackMethod9OrStr | None = None,
        sms_fallback_url: AnyUrl | None = None,
        sms_method: SmsMethod9OrStr | None = None,
        sms_url: AnyUrl | None = None,
        status_callback: AnyUrl | None = None,
        status_callback_method: StatusCallbackMethod10OrStr | None = None,
        voice_application_sid: str | None = None,
        voice_caller_id_lookup: bool | None = None,
        voice_fallback_method: VoiceFallbackMethod9OrStr | None = None,
        voice_fallback_url: AnyUrl | None = None,
        voice_method: VoiceMethod9OrStr | None = None,
        voice_url: AnyUrl | None = None,
        identity_sid: str | None = None,
        address_sid: str | None = None,
        emergency_status: IncomingPhoneNumberLocalEnumEmergencyStatusOrStr | None = None,
        emergency_address_sid: str | None = None,
        trunk_sid: str | None = None,
        voice_receive_mode: IncomingPhoneNumberLocalEnumVoiceReceiveModeOrStr | None = None,
        bundle_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberLocal, RawError]:
        """Incoming local phone numbers on a Twilio account/project

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            phone_number: The phone number to purchase specified in `E.164
                <https://www.twilio.com/docs/glossary/what-e164>`__ format. E.164 phone numbers consist of a + followed
                by the country code and subscriber number without punctuation characters. For example, +14155551234.
            api_version: The API version to use for incoming calls made to the new phone number. The default is
                ``2010-04-01``.
            friendly_name: A descriptive string that you created to describe the new phone number. It can be up to 64
                characters long. By default, this is a formatted version of the phone number.
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
            identity_sid: The SID of the Identity resource that we should associate with the new phone number. Some
                regions require an identity to meet local regulations.
            address_sid: The SID of the Address resource we should associate with the new phone number. Some regions
                require addresses to meet local regulations.
            emergency_status: The parameter displays if emergency calling is enabled for this number. Active numbers may
                place emergency calls by dialing valid emergency numbers for the country.
            emergency_address_sid: The SID of the emergency address configuration to use for emergency calling from the
                new phone number.
            trunk_sid: The SID of the Trunk we should use to handle calls to the new phone number. If a ``trunk_sid`` is
                present, we ignore all of the voice urls and voice applications and use only those set on the Trunk.
                Setting a ``trunk_sid`` will automatically delete your ``voice_application_sid`` and vice versa.
            voice_receive_mode: Value sent with the request.
            bundle_sid: The SID of the Bundle resource that you associate with the phone number. Some regions require a
                Bundle to meet local Regulations.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/Local.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            body=form_body(
                [
                    param[str]("PhoneNumber", phone_number),
                    param[str | None]("ApiVersion", api_version),
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("SmsApplicationSid", sms_application_sid),
                    param[SmsFallbackMethod9OrStr | None]("SmsFallbackMethod", sms_fallback_method),
                    param[AnyUrl | None]("SmsFallbackUrl", sms_fallback_url),
                    param[SmsMethod9OrStr | None]("SmsMethod", sms_method),
                    param[AnyUrl | None]("SmsUrl", sms_url),
                    param[AnyUrl | None]("StatusCallback", status_callback),
                    param[StatusCallbackMethod10OrStr | None]("StatusCallbackMethod", status_callback_method),
                    param[str | None]("VoiceApplicationSid", voice_application_sid),
                    param[bool | None]("VoiceCallerIdLookup", voice_caller_id_lookup),
                    param[VoiceFallbackMethod9OrStr | None]("VoiceFallbackMethod", voice_fallback_method),
                    param[AnyUrl | None]("VoiceFallbackUrl", voice_fallback_url),
                    param[VoiceMethod9OrStr | None]("VoiceMethod", voice_method),
                    param[AnyUrl | None]("VoiceUrl", voice_url),
                    param[str | None]("IdentitySid", identity_sid),
                    param[str | None]("AddressSid", address_sid),
                    param[IncomingPhoneNumberLocalEnumEmergencyStatusOrStr | None]("EmergencyStatus", emergency_status),
                    param[str | None]("EmergencyAddressSid", emergency_address_sid),
                    param[str | None]("TrunkSid", trunk_sid),
                    param[IncomingPhoneNumberLocalEnumVoiceReceiveModeOrStr | None](
                        "VoiceReceiveMode", voice_receive_mode
                    ),
                    param[str | None]("BundleSid", bundle_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberLocal],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_incoming_phone_number_local(
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
    ) -> ApiResult[ListIncomingPhoneNumberLocalResponse, RawError]:
        """Incoming local phone numbers on a Twilio account/project

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                resources to read.
            beta: Whether to include phone numbers new to the Twilio platform. Can be: ``true`` or ``false`` and the
                default is ``true``.
            friendly_name: A string that identifies the resources to read.
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
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/Local.json"),
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
            decoder=json_decoder[ListIncomingPhoneNumberLocalResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401IncomingPhoneNumberLocalWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def create_incoming_phone_number_local(
        self,
        account_sid: str,
        phone_number: str,
        *,
        api_version: str | None = None,
        friendly_name: str | None = None,
        sms_application_sid: str | None = None,
        sms_fallback_method: SmsFallbackMethod9OrStr | None = None,
        sms_fallback_url: AnyUrl | None = None,
        sms_method: SmsMethod9OrStr | None = None,
        sms_url: AnyUrl | None = None,
        status_callback: AnyUrl | None = None,
        status_callback_method: StatusCallbackMethod10OrStr | None = None,
        voice_application_sid: str | None = None,
        voice_caller_id_lookup: bool | None = None,
        voice_fallback_method: VoiceFallbackMethod9OrStr | None = None,
        voice_fallback_url: AnyUrl | None = None,
        voice_method: VoiceMethod9OrStr | None = None,
        voice_url: AnyUrl | None = None,
        identity_sid: str | None = None,
        address_sid: str | None = None,
        emergency_status: IncomingPhoneNumberLocalEnumEmergencyStatusOrStr | None = None,
        emergency_address_sid: str | None = None,
        trunk_sid: str | None = None,
        voice_receive_mode: IncomingPhoneNumberLocalEnumVoiceReceiveModeOrStr | None = None,
        bundle_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberLocal, RawError]:
        """Incoming local phone numbers on a Twilio account/project

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            phone_number: The phone number to purchase specified in `E.164
                <https://www.twilio.com/docs/glossary/what-e164>`__ format. E.164 phone numbers consist of a + followed
                by the country code and subscriber number without punctuation characters. For example, +14155551234.
            api_version: The API version to use for incoming calls made to the new phone number. The default is
                ``2010-04-01``.
            friendly_name: A descriptive string that you created to describe the new phone number. It can be up to 64
                characters long. By default, this is a formatted version of the phone number.
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
            identity_sid: The SID of the Identity resource that we should associate with the new phone number. Some
                regions require an identity to meet local regulations.
            address_sid: The SID of the Address resource we should associate with the new phone number. Some regions
                require addresses to meet local regulations.
            emergency_status: The parameter displays if emergency calling is enabled for this number. Active numbers may
                place emergency calls by dialing valid emergency numbers for the country.
            emergency_address_sid: The SID of the emergency address configuration to use for emergency calling from the
                new phone number.
            trunk_sid: The SID of the Trunk we should use to handle calls to the new phone number. If a ``trunk_sid`` is
                present, we ignore all of the voice urls and voice applications and use only those set on the Trunk.
                Setting a ``trunk_sid`` will automatically delete your ``voice_application_sid`` and vice versa.
            voice_receive_mode: Value sent with the request.
            bundle_sid: The SID of the Bundle resource that you associate with the phone number. Some regions require a
                Bundle to meet local Regulations.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/Local.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            body=form_body(
                [
                    param[str]("PhoneNumber", phone_number),
                    param[str | None]("ApiVersion", api_version),
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("SmsApplicationSid", sms_application_sid),
                    param[SmsFallbackMethod9OrStr | None]("SmsFallbackMethod", sms_fallback_method),
                    param[AnyUrl | None]("SmsFallbackUrl", sms_fallback_url),
                    param[SmsMethod9OrStr | None]("SmsMethod", sms_method),
                    param[AnyUrl | None]("SmsUrl", sms_url),
                    param[AnyUrl | None]("StatusCallback", status_callback),
                    param[StatusCallbackMethod10OrStr | None]("StatusCallbackMethod", status_callback_method),
                    param[str | None]("VoiceApplicationSid", voice_application_sid),
                    param[bool | None]("VoiceCallerIdLookup", voice_caller_id_lookup),
                    param[VoiceFallbackMethod9OrStr | None]("VoiceFallbackMethod", voice_fallback_method),
                    param[AnyUrl | None]("VoiceFallbackUrl", voice_fallback_url),
                    param[VoiceMethod9OrStr | None]("VoiceMethod", voice_method),
                    param[AnyUrl | None]("VoiceUrl", voice_url),
                    param[str | None]("IdentitySid", identity_sid),
                    param[str | None]("AddressSid", address_sid),
                    param[IncomingPhoneNumberLocalEnumEmergencyStatusOrStr | None]("EmergencyStatus", emergency_status),
                    param[str | None]("EmergencyAddressSid", emergency_address_sid),
                    param[str | None]("TrunkSid", trunk_sid),
                    param[IncomingPhoneNumberLocalEnumVoiceReceiveModeOrStr | None](
                        "VoiceReceiveMode", voice_receive_mode
                    ),
                    param[str | None]("BundleSid", bundle_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberLocal],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_incoming_phone_number_local(
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
    ) -> ApiResult[ListIncomingPhoneNumberLocalResponse, RawError]:
        """Incoming local phone numbers on a Twilio account/project

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                resources to read.
            beta: Whether to include phone numbers new to the Twilio platform. Can be: ``true`` or ``false`` and the
                default is ``true``.
            friendly_name: A string that identifies the resources to read.
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
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/Local.json"),
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
            decoder=json_decoder[ListIncomingPhoneNumberLocalResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
