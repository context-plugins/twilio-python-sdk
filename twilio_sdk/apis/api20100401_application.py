from __future__ import annotations

from uuid import UUID, uuid4

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
from ..models.api_v2010_account_application import ApiV2010AccountApplication
from ..models.enums.sms_fallback_method7 import SmsFallbackMethod7OrStr
from ..models.enums.sms_method7 import SmsMethod7OrStr
from ..models.enums.status_callback_method6 import StatusCallbackMethod6OrStr
from ..models.enums.voice_fallback_method7 import VoiceFallbackMethod7OrStr
from ..models.enums.voice_method7 import VoiceMethod7OrStr
from ..models.list_application_response import ListApplicationResponse
from ..server.server import Server


class Api20100401Application:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401ApplicationWithRawResponse(client, server, auth)

    def create_application(
        self,
        account_sid: str,
        *,
        api_version: str | None = None,
        voice_url: str | None = None,
        voice_method: VoiceMethod7OrStr | None = None,
        voice_fallback_url: str | None = None,
        voice_fallback_method: VoiceFallbackMethod7OrStr | None = None,
        status_callback: str | None = None,
        status_callback_method: StatusCallbackMethod6OrStr | None = None,
        voice_caller_id_lookup: bool | None = None,
        sms_url: str | None = None,
        sms_method: SmsMethod7OrStr | None = None,
        sms_fallback_url: str | None = None,
        sms_fallback_method: SmsFallbackMethod7OrStr | None = None,
        sms_status_callback: str | None = None,
        message_status_callback: str | None = None,
        friendly_name: str | None = None,
        public_application_connect_enabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountApplication:
        """Create a new application within your account

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            api_version: The API version to use to start a new TwiML session. Can be: ``2010-04-01`` or ``2008-08-01``.
                The default value is the account's default API version.
            voice_url: The URL we should call when the phone number assigned to this application receives a call.
            voice_method: The HTTP method we should use to call ``voice_url``. Can be: ``GET`` or ``POST``.
            voice_fallback_url: The URL that we should call when an error occurs retrieving or executing the TwiML
                requested by ``url``.
            voice_fallback_method: The HTTP method we should use to call ``voice_fallback_url``. Can be: ``GET`` or
                ``POST``.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``GET`` or
                ``POST``.
            voice_caller_id_lookup: Whether we should look up the caller's caller-ID name from the CNAM database
                (additional charges apply). Can be: ``true`` or ``false``.
            sms_url: The URL we should call when the phone number receives an incoming SMS message.
            sms_method: The HTTP method we should use to call ``sms_url``. Can be: ``GET`` or ``POST``.
            sms_fallback_url: The URL that we should call when an error occurs while retrieving or executing the TwiML
                from ``sms_url``.
            sms_fallback_method: The HTTP method we should use to call ``sms_fallback_url``. Can be: ``GET`` or
                ``POST``.
            sms_status_callback: The URL we should call using a POST method to send status information about SMS
                messages sent by the application.
            message_status_callback: The URL we should call using a POST method to send message status information to
                your application.
            friendly_name: A descriptive string that you create to describe the new application. It can be up to 64
                characters long.
            public_application_connect_enabled: Whether to allow other Twilio accounts to dial this applicaton using
                Dial verb. Can be: ``true`` or ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_application(
            account_sid,
            api_version=api_version,
            voice_url=voice_url,
            voice_method=voice_method,
            voice_fallback_url=voice_fallback_url,
            voice_fallback_method=voice_fallback_method,
            status_callback=status_callback,
            status_callback_method=status_callback_method,
            voice_caller_id_lookup=voice_caller_id_lookup,
            sms_url=sms_url,
            sms_method=sms_method,
            sms_fallback_url=sms_fallback_url,
            sms_fallback_method=sms_fallback_method,
            sms_status_callback=sms_status_callback,
            message_status_callback=message_status_callback,
            friendly_name=friendly_name,
            public_application_connect_enabled=public_application_connect_enabled,
            request_options=request_options,
        ).unwrap()

    def delete_application(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete the application by the specified application sid

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Application resources to delete.
            sid: The Twilio-provided string that uniquely identifies the Application resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_application(account_sid, sid, request_options=request_options).unwrap()

    def fetch_application(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountApplication:
        """Fetch the application specified by the provided sid

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Application resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the Application resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_application(account_sid, sid, request_options=request_options).unwrap()

    def list_application(
        self,
        account_sid: str,
        *,
        friendly_name: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListApplicationResponse:
        """Retrieve a list of applications representing an application within the requesting account

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Application resources to read.
            friendly_name: The string that identifies the Application resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_application(
            account_sid,
            friendly_name=friendly_name,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_application(
        self,
        account_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        api_version: str | None = None,
        voice_url: str | None = None,
        voice_method: VoiceMethod7OrStr | None = None,
        voice_fallback_url: str | None = None,
        voice_fallback_method: VoiceFallbackMethod7OrStr | None = None,
        status_callback: str | None = None,
        status_callback_method: StatusCallbackMethod6OrStr | None = None,
        voice_caller_id_lookup: bool | None = None,
        sms_url: str | None = None,
        sms_method: SmsMethod7OrStr | None = None,
        sms_fallback_url: str | None = None,
        sms_fallback_method: SmsFallbackMethod7OrStr | None = None,
        sms_status_callback: str | None = None,
        message_status_callback: str | None = None,
        public_application_connect_enabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountApplication:
        """Updates the application's properties

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Application resources to update.
            sid: The Twilio-provided string that uniquely identifies the Application resource to update.
            friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters
                long.
            api_version: The API version to use to start a new TwiML session. Can be: ``2010-04-01`` or ``2008-08-01``.
                The default value is your account's default API version.
            voice_url: The URL we should call when the phone number assigned to this application receives a call.
            voice_method: The HTTP method we should use to call ``voice_url``. Can be: ``GET`` or ``POST``.
            voice_fallback_url: The URL that we should call when an error occurs retrieving or executing the TwiML
                requested by ``url``.
            voice_fallback_method: The HTTP method we should use to call ``voice_fallback_url``. Can be: ``GET`` or
                ``POST``.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``GET`` or
                ``POST``.
            voice_caller_id_lookup: Whether we should look up the caller's caller-ID name from the CNAM database
                (additional charges apply). Can be: ``true`` or ``false``.
            sms_url: The URL we should call when the phone number receives an incoming SMS message.
            sms_method: The HTTP method we should use to call ``sms_url``. Can be: ``GET`` or ``POST``.
            sms_fallback_url: The URL that we should call when an error occurs while retrieving or executing the TwiML
                from ``sms_url``.
            sms_fallback_method: The HTTP method we should use to call ``sms_fallback_url``. Can be: ``GET`` or
                ``POST``.
            sms_status_callback: Same as message_status_callback: The URL we should call using a POST method to send
                status information about SMS messages sent by the application. Deprecated, included for backwards
                compatibility.
            message_status_callback: The URL we should call using a POST method to send message status information to
                your application.
            public_application_connect_enabled: Whether to allow other Twilio accounts to dial this applicaton using
                Dial verb. Can be: ``true`` or ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_application(
            account_sid,
            sid,
            friendly_name=friendly_name,
            api_version=api_version,
            voice_url=voice_url,
            voice_method=voice_method,
            voice_fallback_url=voice_fallback_url,
            voice_fallback_method=voice_fallback_method,
            status_callback=status_callback,
            status_callback_method=status_callback_method,
            voice_caller_id_lookup=voice_caller_id_lookup,
            sms_url=sms_url,
            sms_method=sms_method,
            sms_fallback_url=sms_fallback_url,
            sms_fallback_method=sms_fallback_method,
            sms_status_callback=sms_status_callback,
            message_status_callback=message_status_callback,
            public_application_connect_enabled=public_application_connect_enabled,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401ApplicationWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401Application:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401ApplicationWithRawResponse(client, server, auth)

    async def create_application(
        self,
        account_sid: str,
        *,
        api_version: str | None = None,
        voice_url: str | None = None,
        voice_method: VoiceMethod7OrStr | None = None,
        voice_fallback_url: str | None = None,
        voice_fallback_method: VoiceFallbackMethod7OrStr | None = None,
        status_callback: str | None = None,
        status_callback_method: StatusCallbackMethod6OrStr | None = None,
        voice_caller_id_lookup: bool | None = None,
        sms_url: str | None = None,
        sms_method: SmsMethod7OrStr | None = None,
        sms_fallback_url: str | None = None,
        sms_fallback_method: SmsFallbackMethod7OrStr | None = None,
        sms_status_callback: str | None = None,
        message_status_callback: str | None = None,
        friendly_name: str | None = None,
        public_application_connect_enabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountApplication:
        """Create a new application within your account

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            api_version: The API version to use to start a new TwiML session. Can be: ``2010-04-01`` or ``2008-08-01``.
                The default value is the account's default API version.
            voice_url: The URL we should call when the phone number assigned to this application receives a call.
            voice_method: The HTTP method we should use to call ``voice_url``. Can be: ``GET`` or ``POST``.
            voice_fallback_url: The URL that we should call when an error occurs retrieving or executing the TwiML
                requested by ``url``.
            voice_fallback_method: The HTTP method we should use to call ``voice_fallback_url``. Can be: ``GET`` or
                ``POST``.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``GET`` or
                ``POST``.
            voice_caller_id_lookup: Whether we should look up the caller's caller-ID name from the CNAM database
                (additional charges apply). Can be: ``true`` or ``false``.
            sms_url: The URL we should call when the phone number receives an incoming SMS message.
            sms_method: The HTTP method we should use to call ``sms_url``. Can be: ``GET`` or ``POST``.
            sms_fallback_url: The URL that we should call when an error occurs while retrieving or executing the TwiML
                from ``sms_url``.
            sms_fallback_method: The HTTP method we should use to call ``sms_fallback_url``. Can be: ``GET`` or
                ``POST``.
            sms_status_callback: The URL we should call using a POST method to send status information about SMS
                messages sent by the application.
            message_status_callback: The URL we should call using a POST method to send message status information to
                your application.
            friendly_name: A descriptive string that you create to describe the new application. It can be up to 64
                characters long.
            public_application_connect_enabled: Whether to allow other Twilio accounts to dial this applicaton using
                Dial verb. Can be: ``true`` or ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_application(
                account_sid,
                api_version=api_version,
                voice_url=voice_url,
                voice_method=voice_method,
                voice_fallback_url=voice_fallback_url,
                voice_fallback_method=voice_fallback_method,
                status_callback=status_callback,
                status_callback_method=status_callback_method,
                voice_caller_id_lookup=voice_caller_id_lookup,
                sms_url=sms_url,
                sms_method=sms_method,
                sms_fallback_url=sms_fallback_url,
                sms_fallback_method=sms_fallback_method,
                sms_status_callback=sms_status_callback,
                message_status_callback=message_status_callback,
                friendly_name=friendly_name,
                public_application_connect_enabled=public_application_connect_enabled,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_application(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete the application by the specified application sid

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Application resources to delete.
            sid: The Twilio-provided string that uniquely identifies the Application resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_application(account_sid, sid, request_options=request_options)
        ).unwrap()

    async def fetch_application(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountApplication:
        """Fetch the application specified by the provided sid

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Application resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the Application resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_application(account_sid, sid, request_options=request_options)
        ).unwrap()

    async def list_application(
        self,
        account_sid: str,
        *,
        friendly_name: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListApplicationResponse:
        """Retrieve a list of applications representing an application within the requesting account

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Application resources to read.
            friendly_name: The string that identifies the Application resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_application(
                account_sid,
                friendly_name=friendly_name,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_application(
        self,
        account_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        api_version: str | None = None,
        voice_url: str | None = None,
        voice_method: VoiceMethod7OrStr | None = None,
        voice_fallback_url: str | None = None,
        voice_fallback_method: VoiceFallbackMethod7OrStr | None = None,
        status_callback: str | None = None,
        status_callback_method: StatusCallbackMethod6OrStr | None = None,
        voice_caller_id_lookup: bool | None = None,
        sms_url: str | None = None,
        sms_method: SmsMethod7OrStr | None = None,
        sms_fallback_url: str | None = None,
        sms_fallback_method: SmsFallbackMethod7OrStr | None = None,
        sms_status_callback: str | None = None,
        message_status_callback: str | None = None,
        public_application_connect_enabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountApplication:
        """Updates the application's properties

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Application resources to update.
            sid: The Twilio-provided string that uniquely identifies the Application resource to update.
            friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters
                long.
            api_version: The API version to use to start a new TwiML session. Can be: ``2010-04-01`` or ``2008-08-01``.
                The default value is your account's default API version.
            voice_url: The URL we should call when the phone number assigned to this application receives a call.
            voice_method: The HTTP method we should use to call ``voice_url``. Can be: ``GET`` or ``POST``.
            voice_fallback_url: The URL that we should call when an error occurs retrieving or executing the TwiML
                requested by ``url``.
            voice_fallback_method: The HTTP method we should use to call ``voice_fallback_url``. Can be: ``GET`` or
                ``POST``.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``GET`` or
                ``POST``.
            voice_caller_id_lookup: Whether we should look up the caller's caller-ID name from the CNAM database
                (additional charges apply). Can be: ``true`` or ``false``.
            sms_url: The URL we should call when the phone number receives an incoming SMS message.
            sms_method: The HTTP method we should use to call ``sms_url``. Can be: ``GET`` or ``POST``.
            sms_fallback_url: The URL that we should call when an error occurs while retrieving or executing the TwiML
                from ``sms_url``.
            sms_fallback_method: The HTTP method we should use to call ``sms_fallback_url``. Can be: ``GET`` or
                ``POST``.
            sms_status_callback: Same as message_status_callback: The URL we should call using a POST method to send
                status information about SMS messages sent by the application. Deprecated, included for backwards
                compatibility.
            message_status_callback: The URL we should call using a POST method to send message status information to
                your application.
            public_application_connect_enabled: Whether to allow other Twilio accounts to dial this applicaton using
                Dial verb. Can be: ``true`` or ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_application(
                account_sid,
                sid,
                friendly_name=friendly_name,
                api_version=api_version,
                voice_url=voice_url,
                voice_method=voice_method,
                voice_fallback_url=voice_fallback_url,
                voice_fallback_method=voice_fallback_method,
                status_callback=status_callback,
                status_callback_method=status_callback_method,
                voice_caller_id_lookup=voice_caller_id_lookup,
                sms_url=sms_url,
                sms_method=sms_method,
                sms_fallback_url=sms_fallback_url,
                sms_fallback_method=sms_fallback_method,
                sms_status_callback=sms_status_callback,
                message_status_callback=message_status_callback,
                public_application_connect_enabled=public_application_connect_enabled,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401ApplicationWithRawResponse:
        return self._with_raw_response


class Api20100401ApplicationWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_application(
        self,
        account_sid: str,
        *,
        api_version: str | None = None,
        voice_url: str | None = None,
        voice_method: VoiceMethod7OrStr | None = None,
        voice_fallback_url: str | None = None,
        voice_fallback_method: VoiceFallbackMethod7OrStr | None = None,
        status_callback: str | None = None,
        status_callback_method: StatusCallbackMethod6OrStr | None = None,
        voice_caller_id_lookup: bool | None = None,
        sms_url: str | None = None,
        sms_method: SmsMethod7OrStr | None = None,
        sms_fallback_url: str | None = None,
        sms_fallback_method: SmsFallbackMethod7OrStr | None = None,
        sms_status_callback: str | None = None,
        message_status_callback: str | None = None,
        friendly_name: str | None = None,
        public_application_connect_enabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountApplication, RawError]:
        """Create a new application within your account

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            api_version: The API version to use to start a new TwiML session. Can be: ``2010-04-01`` or ``2008-08-01``.
                The default value is the account's default API version.
            voice_url: The URL we should call when the phone number assigned to this application receives a call.
            voice_method: The HTTP method we should use to call ``voice_url``. Can be: ``GET`` or ``POST``.
            voice_fallback_url: The URL that we should call when an error occurs retrieving or executing the TwiML
                requested by ``url``.
            voice_fallback_method: The HTTP method we should use to call ``voice_fallback_url``. Can be: ``GET`` or
                ``POST``.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``GET`` or
                ``POST``.
            voice_caller_id_lookup: Whether we should look up the caller's caller-ID name from the CNAM database
                (additional charges apply). Can be: ``true`` or ``false``.
            sms_url: The URL we should call when the phone number receives an incoming SMS message.
            sms_method: The HTTP method we should use to call ``sms_url``. Can be: ``GET`` or ``POST``.
            sms_fallback_url: The URL that we should call when an error occurs while retrieving or executing the TwiML
                from ``sms_url``.
            sms_fallback_method: The HTTP method we should use to call ``sms_fallback_url``. Can be: ``GET`` or
                ``POST``.
            sms_status_callback: The URL we should call using a POST method to send status information about SMS
                messages sent by the application.
            message_status_callback: The URL we should call using a POST method to send message status information to
                your application.
            friendly_name: A descriptive string that you create to describe the new application. It can be up to 64
                characters long.
            public_application_connect_enabled: Whether to allow other Twilio accounts to dial this applicaton using
                Dial verb. Can be: ``true`` or ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Applications.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("ApiVersion", api_version),
                    param[str | None]("VoiceUrl", voice_url),
                    param[VoiceMethod7OrStr | None]("VoiceMethod", voice_method),
                    param[str | None]("VoiceFallbackUrl", voice_fallback_url),
                    param[VoiceFallbackMethod7OrStr | None]("VoiceFallbackMethod", voice_fallback_method),
                    param[str | None]("StatusCallback", status_callback),
                    param[StatusCallbackMethod6OrStr | None]("StatusCallbackMethod", status_callback_method),
                    param[bool | None]("VoiceCallerIdLookup", voice_caller_id_lookup),
                    param[str | None]("SmsUrl", sms_url),
                    param[SmsMethod7OrStr | None]("SmsMethod", sms_method),
                    param[str | None]("SmsFallbackUrl", sms_fallback_url),
                    param[SmsFallbackMethod7OrStr | None]("SmsFallbackMethod", sms_fallback_method),
                    param[str | None]("SmsStatusCallback", sms_status_callback),
                    param[str | None]("MessageStatusCallback", message_status_callback),
                    param[str | None]("FriendlyName", friendly_name),
                    param[bool | None]("PublicApplicationConnectEnabled", public_application_connect_enabled),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountApplication],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_application(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete the application by the specified application sid

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Application resources to delete.
            sid: The Twilio-provided string that uniquely identifies the Application resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Applications/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_application(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountApplication, RawError]:
        """Fetch the application specified by the provided sid

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Application resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the Application resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Applications/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountApplication],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_application(
        self,
        account_sid: str,
        *,
        friendly_name: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListApplicationResponse, RawError]:
        """Retrieve a list of applications representing an application within the requesting account

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Application resources to read.
            friendly_name: The string that identifies the Application resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Applications.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            query_params=[
                param[str | None]("FriendlyName", friendly_name),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListApplicationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_application(
        self,
        account_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        api_version: str | None = None,
        voice_url: str | None = None,
        voice_method: VoiceMethod7OrStr | None = None,
        voice_fallback_url: str | None = None,
        voice_fallback_method: VoiceFallbackMethod7OrStr | None = None,
        status_callback: str | None = None,
        status_callback_method: StatusCallbackMethod6OrStr | None = None,
        voice_caller_id_lookup: bool | None = None,
        sms_url: str | None = None,
        sms_method: SmsMethod7OrStr | None = None,
        sms_fallback_url: str | None = None,
        sms_fallback_method: SmsFallbackMethod7OrStr | None = None,
        sms_status_callback: str | None = None,
        message_status_callback: str | None = None,
        public_application_connect_enabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountApplication, RawError]:
        """Updates the application's properties

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Application resources to update.
            sid: The Twilio-provided string that uniquely identifies the Application resource to update.
            friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters
                long.
            api_version: The API version to use to start a new TwiML session. Can be: ``2010-04-01`` or ``2008-08-01``.
                The default value is your account's default API version.
            voice_url: The URL we should call when the phone number assigned to this application receives a call.
            voice_method: The HTTP method we should use to call ``voice_url``. Can be: ``GET`` or ``POST``.
            voice_fallback_url: The URL that we should call when an error occurs retrieving or executing the TwiML
                requested by ``url``.
            voice_fallback_method: The HTTP method we should use to call ``voice_fallback_url``. Can be: ``GET`` or
                ``POST``.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``GET`` or
                ``POST``.
            voice_caller_id_lookup: Whether we should look up the caller's caller-ID name from the CNAM database
                (additional charges apply). Can be: ``true`` or ``false``.
            sms_url: The URL we should call when the phone number receives an incoming SMS message.
            sms_method: The HTTP method we should use to call ``sms_url``. Can be: ``GET`` or ``POST``.
            sms_fallback_url: The URL that we should call when an error occurs while retrieving or executing the TwiML
                from ``sms_url``.
            sms_fallback_method: The HTTP method we should use to call ``sms_fallback_url``. Can be: ``GET`` or
                ``POST``.
            sms_status_callback: Same as message_status_callback: The URL we should call using a POST method to send
                status information about SMS messages sent by the application. Deprecated, included for backwards
                compatibility.
            message_status_callback: The URL we should call using a POST method to send message status information to
                your application.
            public_application_connect_enabled: Whether to allow other Twilio accounts to dial this applicaton using
                Dial verb. Can be: ``true`` or ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Applications/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("ApiVersion", api_version),
                    param[str | None]("VoiceUrl", voice_url),
                    param[VoiceMethod7OrStr | None]("VoiceMethod", voice_method),
                    param[str | None]("VoiceFallbackUrl", voice_fallback_url),
                    param[VoiceFallbackMethod7OrStr | None]("VoiceFallbackMethod", voice_fallback_method),
                    param[str | None]("StatusCallback", status_callback),
                    param[StatusCallbackMethod6OrStr | None]("StatusCallbackMethod", status_callback_method),
                    param[bool | None]("VoiceCallerIdLookup", voice_caller_id_lookup),
                    param[str | None]("SmsUrl", sms_url),
                    param[SmsMethod7OrStr | None]("SmsMethod", sms_method),
                    param[str | None]("SmsFallbackUrl", sms_fallback_url),
                    param[SmsFallbackMethod7OrStr | None]("SmsFallbackMethod", sms_fallback_method),
                    param[str | None]("SmsStatusCallback", sms_status_callback),
                    param[str | None]("MessageStatusCallback", message_status_callback),
                    param[bool | None]("PublicApplicationConnectEnabled", public_application_connect_enabled),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountApplication],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401ApplicationWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_application(
        self,
        account_sid: str,
        *,
        api_version: str | None = None,
        voice_url: str | None = None,
        voice_method: VoiceMethod7OrStr | None = None,
        voice_fallback_url: str | None = None,
        voice_fallback_method: VoiceFallbackMethod7OrStr | None = None,
        status_callback: str | None = None,
        status_callback_method: StatusCallbackMethod6OrStr | None = None,
        voice_caller_id_lookup: bool | None = None,
        sms_url: str | None = None,
        sms_method: SmsMethod7OrStr | None = None,
        sms_fallback_url: str | None = None,
        sms_fallback_method: SmsFallbackMethod7OrStr | None = None,
        sms_status_callback: str | None = None,
        message_status_callback: str | None = None,
        friendly_name: str | None = None,
        public_application_connect_enabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountApplication, RawError]:
        """Create a new application within your account

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            api_version: The API version to use to start a new TwiML session. Can be: ``2010-04-01`` or ``2008-08-01``.
                The default value is the account's default API version.
            voice_url: The URL we should call when the phone number assigned to this application receives a call.
            voice_method: The HTTP method we should use to call ``voice_url``. Can be: ``GET`` or ``POST``.
            voice_fallback_url: The URL that we should call when an error occurs retrieving or executing the TwiML
                requested by ``url``.
            voice_fallback_method: The HTTP method we should use to call ``voice_fallback_url``. Can be: ``GET`` or
                ``POST``.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``GET`` or
                ``POST``.
            voice_caller_id_lookup: Whether we should look up the caller's caller-ID name from the CNAM database
                (additional charges apply). Can be: ``true`` or ``false``.
            sms_url: The URL we should call when the phone number receives an incoming SMS message.
            sms_method: The HTTP method we should use to call ``sms_url``. Can be: ``GET`` or ``POST``.
            sms_fallback_url: The URL that we should call when an error occurs while retrieving or executing the TwiML
                from ``sms_url``.
            sms_fallback_method: The HTTP method we should use to call ``sms_fallback_url``. Can be: ``GET`` or
                ``POST``.
            sms_status_callback: The URL we should call using a POST method to send status information about SMS
                messages sent by the application.
            message_status_callback: The URL we should call using a POST method to send message status information to
                your application.
            friendly_name: A descriptive string that you create to describe the new application. It can be up to 64
                characters long.
            public_application_connect_enabled: Whether to allow other Twilio accounts to dial this applicaton using
                Dial verb. Can be: ``true`` or ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Applications.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("ApiVersion", api_version),
                    param[str | None]("VoiceUrl", voice_url),
                    param[VoiceMethod7OrStr | None]("VoiceMethod", voice_method),
                    param[str | None]("VoiceFallbackUrl", voice_fallback_url),
                    param[VoiceFallbackMethod7OrStr | None]("VoiceFallbackMethod", voice_fallback_method),
                    param[str | None]("StatusCallback", status_callback),
                    param[StatusCallbackMethod6OrStr | None]("StatusCallbackMethod", status_callback_method),
                    param[bool | None]("VoiceCallerIdLookup", voice_caller_id_lookup),
                    param[str | None]("SmsUrl", sms_url),
                    param[SmsMethod7OrStr | None]("SmsMethod", sms_method),
                    param[str | None]("SmsFallbackUrl", sms_fallback_url),
                    param[SmsFallbackMethod7OrStr | None]("SmsFallbackMethod", sms_fallback_method),
                    param[str | None]("SmsStatusCallback", sms_status_callback),
                    param[str | None]("MessageStatusCallback", message_status_callback),
                    param[str | None]("FriendlyName", friendly_name),
                    param[bool | None]("PublicApplicationConnectEnabled", public_application_connect_enabled),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountApplication],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_application(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete the application by the specified application sid

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Application resources to delete.
            sid: The Twilio-provided string that uniquely identifies the Application resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Applications/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_application(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountApplication, RawError]:
        """Fetch the application specified by the provided sid

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Application resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the Application resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Applications/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountApplication],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_application(
        self,
        account_sid: str,
        *,
        friendly_name: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListApplicationResponse, RawError]:
        """Retrieve a list of applications representing an application within the requesting account

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Application resources to read.
            friendly_name: The string that identifies the Application resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Applications.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            query_params=[
                param[str | None]("FriendlyName", friendly_name),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListApplicationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_application(
        self,
        account_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        api_version: str | None = None,
        voice_url: str | None = None,
        voice_method: VoiceMethod7OrStr | None = None,
        voice_fallback_url: str | None = None,
        voice_fallback_method: VoiceFallbackMethod7OrStr | None = None,
        status_callback: str | None = None,
        status_callback_method: StatusCallbackMethod6OrStr | None = None,
        voice_caller_id_lookup: bool | None = None,
        sms_url: str | None = None,
        sms_method: SmsMethod7OrStr | None = None,
        sms_fallback_url: str | None = None,
        sms_fallback_method: SmsFallbackMethod7OrStr | None = None,
        sms_status_callback: str | None = None,
        message_status_callback: str | None = None,
        public_application_connect_enabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountApplication, RawError]:
        """Updates the application's properties

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Application resources to update.
            sid: The Twilio-provided string that uniquely identifies the Application resource to update.
            friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters
                long.
            api_version: The API version to use to start a new TwiML session. Can be: ``2010-04-01`` or ``2008-08-01``.
                The default value is your account's default API version.
            voice_url: The URL we should call when the phone number assigned to this application receives a call.
            voice_method: The HTTP method we should use to call ``voice_url``. Can be: ``GET`` or ``POST``.
            voice_fallback_url: The URL that we should call when an error occurs retrieving or executing the TwiML
                requested by ``url``.
            voice_fallback_method: The HTTP method we should use to call ``voice_fallback_url``. Can be: ``GET`` or
                ``POST``.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``GET`` or
                ``POST``.
            voice_caller_id_lookup: Whether we should look up the caller's caller-ID name from the CNAM database
                (additional charges apply). Can be: ``true`` or ``false``.
            sms_url: The URL we should call when the phone number receives an incoming SMS message.
            sms_method: The HTTP method we should use to call ``sms_url``. Can be: ``GET`` or ``POST``.
            sms_fallback_url: The URL that we should call when an error occurs while retrieving or executing the TwiML
                from ``sms_url``.
            sms_fallback_method: The HTTP method we should use to call ``sms_fallback_url``. Can be: ``GET`` or
                ``POST``.
            sms_status_callback: Same as message_status_callback: The URL we should call using a POST method to send
                status information about SMS messages sent by the application. Deprecated, included for backwards
                compatibility.
            message_status_callback: The URL we should call using a POST method to send message status information to
                your application.
            public_application_connect_enabled: Whether to allow other Twilio accounts to dial this applicaton using
                Dial verb. Can be: ``true`` or ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Applications/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("ApiVersion", api_version),
                    param[str | None]("VoiceUrl", voice_url),
                    param[VoiceMethod7OrStr | None]("VoiceMethod", voice_method),
                    param[str | None]("VoiceFallbackUrl", voice_fallback_url),
                    param[VoiceFallbackMethod7OrStr | None]("VoiceFallbackMethod", voice_fallback_method),
                    param[str | None]("StatusCallback", status_callback),
                    param[StatusCallbackMethod6OrStr | None]("StatusCallbackMethod", status_callback_method),
                    param[bool | None]("VoiceCallerIdLookup", voice_caller_id_lookup),
                    param[str | None]("SmsUrl", sms_url),
                    param[SmsMethod7OrStr | None]("SmsMethod", sms_method),
                    param[str | None]("SmsFallbackUrl", sms_fallback_url),
                    param[SmsFallbackMethod7OrStr | None]("SmsFallbackMethod", sms_fallback_method),
                    param[str | None]("SmsStatusCallback", sms_status_callback),
                    param[str | None]("MessageStatusCallback", message_status_callback),
                    param[bool | None]("PublicApplicationConnectEnabled", public_application_connect_enabled),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountApplication],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
