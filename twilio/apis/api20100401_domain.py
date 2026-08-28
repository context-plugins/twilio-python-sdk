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
from ..models.api_v2010_account_sip_sip_domain import ApiV2010AccountSipSipDomain
from ..models.enums.voice_fallback_method7 import VoiceFallbackMethod7OrStr
from ..models.enums.voice_method7 import VoiceMethod7OrStr
from ..models.enums.voice_method15 import VoiceMethod15OrStr
from ..models.enums.voice_status_callback_method1 import VoiceStatusCallbackMethod1OrStr
from ..models.list_sip_domain_response import ListSipDomainResponse
from ..server.server import Server


class Api20100401Domain:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401DomainWithRawResponse(client, server, auth)

    def create_sip_domain(
        self,
        account_sid: str,
        domain_name: str,
        *,
        friendly_name: str | None = None,
        voice_url: str | None = None,
        voice_method: VoiceMethod7OrStr | None = None,
        voice_fallback_url: str | None = None,
        voice_fallback_method: VoiceFallbackMethod7OrStr | None = None,
        voice_status_callback_url: str | None = None,
        voice_status_callback_method: VoiceStatusCallbackMethod1OrStr | None = None,
        sip_registration: bool | None = None,
        emergency_calling_enabled: bool | None = None,
        secure: bool | None = None,
        byoc_trunk_sid: str | None = None,
        emergency_caller_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountSipSipDomain:
        """Create a new Domain

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            domain_name: The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can
                contain letters, digits, and "-" and must end with ``sip.twilio.com``.
            friendly_name: A descriptive string that you created to describe the resource. It can be up to 64 characters
                long.
            voice_url: The URL we should when the domain receives a call.
            voice_method: The HTTP method we should use to call ``voice_url``. Can be: ``GET`` or ``POST``.
            voice_fallback_url: The URL that we should call when an error occurs while retrieving or executing the TwiML
                from ``voice_url``.
            voice_fallback_method: The HTTP method we should use to call ``voice_fallback_url``. Can be: ``GET`` or
                ``POST``.
            voice_status_callback_url: The URL that we should call to pass status parameters (such as call ended) to
                your application.
            voice_status_callback_method: The HTTP method we should use to call ``voice_status_callback_url``. Can be:
                ``GET`` or ``POST``.
            sip_registration: Whether to allow SIP Endpoints to register with the domain to receive calls. Can be
                ``true`` or ``false``. ``true`` allows SIP Endpoints to register with the domain to receive calls,
                ``false`` does not.
            emergency_calling_enabled: Whether emergency calling is enabled for the domain. If enabled, allows emergency
                calls on the domain from phone numbers with validated addresses.
            secure: Whether secure SIP is enabled for the domain. If enabled, TLS will be enforced and SRTP will be
                negotiated on all incoming calls to this sip domain.
            byoc_trunk_sid: The SID of the BYOC Trunk(Bring Your Own Carrier) resource that the Sip Domain will be
                associated with.
            emergency_caller_sid: Whether an emergency caller sid is configured for the domain. If present, this phone
                number will be used as the callback for the emergency call.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_sip_domain(
            account_sid,
            domain_name,
            friendly_name=friendly_name,
            voice_url=voice_url,
            voice_method=voice_method,
            voice_fallback_url=voice_fallback_url,
            voice_fallback_method=voice_fallback_method,
            voice_status_callback_url=voice_status_callback_url,
            voice_status_callback_method=voice_status_callback_method,
            sip_registration=sip_registration,
            emergency_calling_enabled=emergency_calling_enabled,
            secure=secure,
            byoc_trunk_sid=byoc_trunk_sid,
            emergency_caller_sid=emergency_caller_sid,
            request_options=request_options,
        ).unwrap()

    def delete_sip_domain(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete an instance of a Domain

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                SipDomain resources to delete.
            sid: The Twilio-provided string that uniquely identifies the SipDomain resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_sip_domain(account_sid, sid, request_options=request_options).unwrap()

    def fetch_sip_domain(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountSipSipDomain:
        """Fetch an instance of a Domain

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                SipDomain resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the SipDomain resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_sip_domain(account_sid, sid, request_options=request_options).unwrap()

    def list_sip_domain(
        self,
        account_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSipDomainResponse:
        """Retrieve a list of domains belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                SipDomain resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_sip_domain(
            account_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    def update_sip_domain(
        self,
        account_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        voice_fallback_method: VoiceFallbackMethod7OrStr | None = None,
        voice_fallback_url: str | None = None,
        voice_method: VoiceMethod15OrStr | None = None,
        voice_status_callback_method: VoiceStatusCallbackMethod1OrStr | None = None,
        voice_status_callback_url: str | None = None,
        voice_url: str | None = None,
        sip_registration: bool | None = None,
        domain_name: str | None = None,
        emergency_calling_enabled: bool | None = None,
        secure: bool | None = None,
        byoc_trunk_sid: str | None = None,
        emergency_caller_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountSipSipDomain:
        """Update the attributes of a domain

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                SipDomain resource to update.
            sid: The Twilio-provided string that uniquely identifies the SipDomain resource to update.
            friendly_name: A descriptive string that you created to describe the resource. It can be up to 64 characters
                long.
            voice_fallback_method: The HTTP method we should use to call ``voice_fallback_url``. Can be: ``GET`` or
                ``POST``.
            voice_fallback_url: The URL that we should call when an error occurs while retrieving or executing the TwiML
                requested by ``voice_url``.
            voice_method: The HTTP method we should use to call ``voice_url``
            voice_status_callback_method: The HTTP method we should use to call ``voice_status_callback_url``. Can be:
                ``GET`` or ``POST``.
            voice_status_callback_url: The URL that we should call to pass status parameters (such as call ended) to
                your application.
            voice_url: The URL we should call when the domain receives a call.
            sip_registration: Whether to allow SIP Endpoints to register with the domain to receive calls. Can be
                ``true`` or ``false``. ``true`` allows SIP Endpoints to register with the domain to receive calls,
                ``false`` does not.
            domain_name: The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can
                contain letters, digits, and "-" and must end with ``sip.twilio.com``.
            emergency_calling_enabled: Whether emergency calling is enabled for the domain. If enabled, allows emergency
                calls on the domain from phone numbers with validated addresses.
            secure: Whether secure SIP is enabled for the domain. If enabled, TLS will be enforced and SRTP will be
                negotiated on all incoming calls to this sip domain.
            byoc_trunk_sid: The SID of the BYOC Trunk(Bring Your Own Carrier) resource that the Sip Domain will be
                associated with.
            emergency_caller_sid: Whether an emergency caller sid is configured for the domain. If present, this phone
                number will be used as the callback for the emergency call.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_sip_domain(
            account_sid,
            sid,
            friendly_name=friendly_name,
            voice_fallback_method=voice_fallback_method,
            voice_fallback_url=voice_fallback_url,
            voice_method=voice_method,
            voice_status_callback_method=voice_status_callback_method,
            voice_status_callback_url=voice_status_callback_url,
            voice_url=voice_url,
            sip_registration=sip_registration,
            domain_name=domain_name,
            emergency_calling_enabled=emergency_calling_enabled,
            secure=secure,
            byoc_trunk_sid=byoc_trunk_sid,
            emergency_caller_sid=emergency_caller_sid,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401DomainWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401Domain:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401DomainWithRawResponse(client, server, auth)

    async def create_sip_domain(
        self,
        account_sid: str,
        domain_name: str,
        *,
        friendly_name: str | None = None,
        voice_url: str | None = None,
        voice_method: VoiceMethod7OrStr | None = None,
        voice_fallback_url: str | None = None,
        voice_fallback_method: VoiceFallbackMethod7OrStr | None = None,
        voice_status_callback_url: str | None = None,
        voice_status_callback_method: VoiceStatusCallbackMethod1OrStr | None = None,
        sip_registration: bool | None = None,
        emergency_calling_enabled: bool | None = None,
        secure: bool | None = None,
        byoc_trunk_sid: str | None = None,
        emergency_caller_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountSipSipDomain:
        """Create a new Domain

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            domain_name: The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can
                contain letters, digits, and "-" and must end with ``sip.twilio.com``.
            friendly_name: A descriptive string that you created to describe the resource. It can be up to 64 characters
                long.
            voice_url: The URL we should when the domain receives a call.
            voice_method: The HTTP method we should use to call ``voice_url``. Can be: ``GET`` or ``POST``.
            voice_fallback_url: The URL that we should call when an error occurs while retrieving or executing the TwiML
                from ``voice_url``.
            voice_fallback_method: The HTTP method we should use to call ``voice_fallback_url``. Can be: ``GET`` or
                ``POST``.
            voice_status_callback_url: The URL that we should call to pass status parameters (such as call ended) to
                your application.
            voice_status_callback_method: The HTTP method we should use to call ``voice_status_callback_url``. Can be:
                ``GET`` or ``POST``.
            sip_registration: Whether to allow SIP Endpoints to register with the domain to receive calls. Can be
                ``true`` or ``false``. ``true`` allows SIP Endpoints to register with the domain to receive calls,
                ``false`` does not.
            emergency_calling_enabled: Whether emergency calling is enabled for the domain. If enabled, allows emergency
                calls on the domain from phone numbers with validated addresses.
            secure: Whether secure SIP is enabled for the domain. If enabled, TLS will be enforced and SRTP will be
                negotiated on all incoming calls to this sip domain.
            byoc_trunk_sid: The SID of the BYOC Trunk(Bring Your Own Carrier) resource that the Sip Domain will be
                associated with.
            emergency_caller_sid: Whether an emergency caller sid is configured for the domain. If present, this phone
                number will be used as the callback for the emergency call.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_sip_domain(
                account_sid,
                domain_name,
                friendly_name=friendly_name,
                voice_url=voice_url,
                voice_method=voice_method,
                voice_fallback_url=voice_fallback_url,
                voice_fallback_method=voice_fallback_method,
                voice_status_callback_url=voice_status_callback_url,
                voice_status_callback_method=voice_status_callback_method,
                sip_registration=sip_registration,
                emergency_calling_enabled=emergency_calling_enabled,
                secure=secure,
                byoc_trunk_sid=byoc_trunk_sid,
                emergency_caller_sid=emergency_caller_sid,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_sip_domain(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete an instance of a Domain

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                SipDomain resources to delete.
            sid: The Twilio-provided string that uniquely identifies the SipDomain resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_sip_domain(account_sid, sid, request_options=request_options)
        ).unwrap()

    async def fetch_sip_domain(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountSipSipDomain:
        """Fetch an instance of a Domain

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                SipDomain resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the SipDomain resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_sip_domain(account_sid, sid, request_options=request_options)
        ).unwrap()

    async def list_sip_domain(
        self,
        account_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSipDomainResponse:
        """Retrieve a list of domains belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                SipDomain resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_sip_domain(
                account_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    async def update_sip_domain(
        self,
        account_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        voice_fallback_method: VoiceFallbackMethod7OrStr | None = None,
        voice_fallback_url: str | None = None,
        voice_method: VoiceMethod15OrStr | None = None,
        voice_status_callback_method: VoiceStatusCallbackMethod1OrStr | None = None,
        voice_status_callback_url: str | None = None,
        voice_url: str | None = None,
        sip_registration: bool | None = None,
        domain_name: str | None = None,
        emergency_calling_enabled: bool | None = None,
        secure: bool | None = None,
        byoc_trunk_sid: str | None = None,
        emergency_caller_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountSipSipDomain:
        """Update the attributes of a domain

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                SipDomain resource to update.
            sid: The Twilio-provided string that uniquely identifies the SipDomain resource to update.
            friendly_name: A descriptive string that you created to describe the resource. It can be up to 64 characters
                long.
            voice_fallback_method: The HTTP method we should use to call ``voice_fallback_url``. Can be: ``GET`` or
                ``POST``.
            voice_fallback_url: The URL that we should call when an error occurs while retrieving or executing the TwiML
                requested by ``voice_url``.
            voice_method: The HTTP method we should use to call ``voice_url``
            voice_status_callback_method: The HTTP method we should use to call ``voice_status_callback_url``. Can be:
                ``GET`` or ``POST``.
            voice_status_callback_url: The URL that we should call to pass status parameters (such as call ended) to
                your application.
            voice_url: The URL we should call when the domain receives a call.
            sip_registration: Whether to allow SIP Endpoints to register with the domain to receive calls. Can be
                ``true`` or ``false``. ``true`` allows SIP Endpoints to register with the domain to receive calls,
                ``false`` does not.
            domain_name: The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can
                contain letters, digits, and "-" and must end with ``sip.twilio.com``.
            emergency_calling_enabled: Whether emergency calling is enabled for the domain. If enabled, allows emergency
                calls on the domain from phone numbers with validated addresses.
            secure: Whether secure SIP is enabled for the domain. If enabled, TLS will be enforced and SRTP will be
                negotiated on all incoming calls to this sip domain.
            byoc_trunk_sid: The SID of the BYOC Trunk(Bring Your Own Carrier) resource that the Sip Domain will be
                associated with.
            emergency_caller_sid: Whether an emergency caller sid is configured for the domain. If present, this phone
                number will be used as the callback for the emergency call.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_sip_domain(
                account_sid,
                sid,
                friendly_name=friendly_name,
                voice_fallback_method=voice_fallback_method,
                voice_fallback_url=voice_fallback_url,
                voice_method=voice_method,
                voice_status_callback_method=voice_status_callback_method,
                voice_status_callback_url=voice_status_callback_url,
                voice_url=voice_url,
                sip_registration=sip_registration,
                domain_name=domain_name,
                emergency_calling_enabled=emergency_calling_enabled,
                secure=secure,
                byoc_trunk_sid=byoc_trunk_sid,
                emergency_caller_sid=emergency_caller_sid,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401DomainWithRawResponse:
        return self._with_raw_response


class Api20100401DomainWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_sip_domain(
        self,
        account_sid: str,
        domain_name: str,
        *,
        friendly_name: str | None = None,
        voice_url: str | None = None,
        voice_method: VoiceMethod7OrStr | None = None,
        voice_fallback_url: str | None = None,
        voice_fallback_method: VoiceFallbackMethod7OrStr | None = None,
        voice_status_callback_url: str | None = None,
        voice_status_callback_method: VoiceStatusCallbackMethod1OrStr | None = None,
        sip_registration: bool | None = None,
        emergency_calling_enabled: bool | None = None,
        secure: bool | None = None,
        byoc_trunk_sid: str | None = None,
        emergency_caller_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountSipSipDomain, RawError]:
        """Create a new Domain

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            domain_name: The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can
                contain letters, digits, and "-" and must end with ``sip.twilio.com``.
            friendly_name: A descriptive string that you created to describe the resource. It can be up to 64 characters
                long.
            voice_url: The URL we should when the domain receives a call.
            voice_method: The HTTP method we should use to call ``voice_url``. Can be: ``GET`` or ``POST``.
            voice_fallback_url: The URL that we should call when an error occurs while retrieving or executing the TwiML
                from ``voice_url``.
            voice_fallback_method: The HTTP method we should use to call ``voice_fallback_url``. Can be: ``GET`` or
                ``POST``.
            voice_status_callback_url: The URL that we should call to pass status parameters (such as call ended) to
                your application.
            voice_status_callback_method: The HTTP method we should use to call ``voice_status_callback_url``. Can be:
                ``GET`` or ``POST``.
            sip_registration: Whether to allow SIP Endpoints to register with the domain to receive calls. Can be
                ``true`` or ``false``. ``true`` allows SIP Endpoints to register with the domain to receive calls,
                ``false`` does not.
            emergency_calling_enabled: Whether emergency calling is enabled for the domain. If enabled, allows emergency
                calls on the domain from phone numbers with validated addresses.
            secure: Whether secure SIP is enabled for the domain. If enabled, TLS will be enforced and SRTP will be
                negotiated on all incoming calls to this sip domain.
            byoc_trunk_sid: The SID of the BYOC Trunk(Bring Your Own Carrier) resource that the Sip Domain will be
                associated with.
            emergency_caller_sid: Whether an emergency caller sid is configured for the domain. If present, this phone
                number will be used as the callback for the emergency call.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/SIP/Domains.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            body=form_body(
                [
                    param[str]("DomainName", domain_name),
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("VoiceUrl", voice_url),
                    param[VoiceMethod7OrStr | None]("VoiceMethod", voice_method),
                    param[str | None]("VoiceFallbackUrl", voice_fallback_url),
                    param[VoiceFallbackMethod7OrStr | None]("VoiceFallbackMethod", voice_fallback_method),
                    param[str | None]("VoiceStatusCallbackUrl", voice_status_callback_url),
                    param[VoiceStatusCallbackMethod1OrStr | None](
                        "VoiceStatusCallbackMethod", voice_status_callback_method
                    ),
                    param[bool | None]("SipRegistration", sip_registration),
                    param[bool | None]("EmergencyCallingEnabled", emergency_calling_enabled),
                    param[bool | None]("Secure", secure),
                    param[str | None]("ByocTrunkSid", byoc_trunk_sid),
                    param[str | None]("EmergencyCallerSid", emergency_caller_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountSipSipDomain],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_sip_domain(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete an instance of a Domain

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                SipDomain resources to delete.
            sid: The Twilio-provided string that uniquely identifies the SipDomain resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_sip_domain(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountSipSipDomain, RawError]:
        """Fetch an instance of a Domain

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                SipDomain resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the SipDomain resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountSipSipDomain],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_sip_domain(
        self,
        account_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSipDomainResponse, RawError]:
        """Retrieve a list of domains belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                SipDomain resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/SIP/Domains.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListSipDomainResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_sip_domain(
        self,
        account_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        voice_fallback_method: VoiceFallbackMethod7OrStr | None = None,
        voice_fallback_url: str | None = None,
        voice_method: VoiceMethod15OrStr | None = None,
        voice_status_callback_method: VoiceStatusCallbackMethod1OrStr | None = None,
        voice_status_callback_url: str | None = None,
        voice_url: str | None = None,
        sip_registration: bool | None = None,
        domain_name: str | None = None,
        emergency_calling_enabled: bool | None = None,
        secure: bool | None = None,
        byoc_trunk_sid: str | None = None,
        emergency_caller_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountSipSipDomain, RawError]:
        """Update the attributes of a domain

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                SipDomain resource to update.
            sid: The Twilio-provided string that uniquely identifies the SipDomain resource to update.
            friendly_name: A descriptive string that you created to describe the resource. It can be up to 64 characters
                long.
            voice_fallback_method: The HTTP method we should use to call ``voice_fallback_url``. Can be: ``GET`` or
                ``POST``.
            voice_fallback_url: The URL that we should call when an error occurs while retrieving or executing the TwiML
                requested by ``voice_url``.
            voice_method: The HTTP method we should use to call ``voice_url``
            voice_status_callback_method: The HTTP method we should use to call ``voice_status_callback_url``. Can be:
                ``GET`` or ``POST``.
            voice_status_callback_url: The URL that we should call to pass status parameters (such as call ended) to
                your application.
            voice_url: The URL we should call when the domain receives a call.
            sip_registration: Whether to allow SIP Endpoints to register with the domain to receive calls. Can be
                ``true`` or ``false``. ``true`` allows SIP Endpoints to register with the domain to receive calls,
                ``false`` does not.
            domain_name: The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can
                contain letters, digits, and "-" and must end with ``sip.twilio.com``.
            emergency_calling_enabled: Whether emergency calling is enabled for the domain. If enabled, allows emergency
                calls on the domain from phone numbers with validated addresses.
            secure: Whether secure SIP is enabled for the domain. If enabled, TLS will be enforced and SRTP will be
                negotiated on all incoming calls to this sip domain.
            byoc_trunk_sid: The SID of the BYOC Trunk(Bring Your Own Carrier) resource that the Sip Domain will be
                associated with.
            emergency_caller_sid: Whether an emergency caller sid is configured for the domain. If present, this phone
                number will be used as the callback for the emergency call.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[VoiceFallbackMethod7OrStr | None]("VoiceFallbackMethod", voice_fallback_method),
                    param[str | None]("VoiceFallbackUrl", voice_fallback_url),
                    param[VoiceMethod15OrStr | None]("VoiceMethod", voice_method),
                    param[VoiceStatusCallbackMethod1OrStr | None](
                        "VoiceStatusCallbackMethod", voice_status_callback_method
                    ),
                    param[str | None]("VoiceStatusCallbackUrl", voice_status_callback_url),
                    param[str | None]("VoiceUrl", voice_url),
                    param[bool | None]("SipRegistration", sip_registration),
                    param[str | None]("DomainName", domain_name),
                    param[bool | None]("EmergencyCallingEnabled", emergency_calling_enabled),
                    param[bool | None]("Secure", secure),
                    param[str | None]("ByocTrunkSid", byoc_trunk_sid),
                    param[str | None]("EmergencyCallerSid", emergency_caller_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountSipSipDomain],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401DomainWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_sip_domain(
        self,
        account_sid: str,
        domain_name: str,
        *,
        friendly_name: str | None = None,
        voice_url: str | None = None,
        voice_method: VoiceMethod7OrStr | None = None,
        voice_fallback_url: str | None = None,
        voice_fallback_method: VoiceFallbackMethod7OrStr | None = None,
        voice_status_callback_url: str | None = None,
        voice_status_callback_method: VoiceStatusCallbackMethod1OrStr | None = None,
        sip_registration: bool | None = None,
        emergency_calling_enabled: bool | None = None,
        secure: bool | None = None,
        byoc_trunk_sid: str | None = None,
        emergency_caller_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountSipSipDomain, RawError]:
        """Create a new Domain

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            domain_name: The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can
                contain letters, digits, and "-" and must end with ``sip.twilio.com``.
            friendly_name: A descriptive string that you created to describe the resource. It can be up to 64 characters
                long.
            voice_url: The URL we should when the domain receives a call.
            voice_method: The HTTP method we should use to call ``voice_url``. Can be: ``GET`` or ``POST``.
            voice_fallback_url: The URL that we should call when an error occurs while retrieving or executing the TwiML
                from ``voice_url``.
            voice_fallback_method: The HTTP method we should use to call ``voice_fallback_url``. Can be: ``GET`` or
                ``POST``.
            voice_status_callback_url: The URL that we should call to pass status parameters (such as call ended) to
                your application.
            voice_status_callback_method: The HTTP method we should use to call ``voice_status_callback_url``. Can be:
                ``GET`` or ``POST``.
            sip_registration: Whether to allow SIP Endpoints to register with the domain to receive calls. Can be
                ``true`` or ``false``. ``true`` allows SIP Endpoints to register with the domain to receive calls,
                ``false`` does not.
            emergency_calling_enabled: Whether emergency calling is enabled for the domain. If enabled, allows emergency
                calls on the domain from phone numbers with validated addresses.
            secure: Whether secure SIP is enabled for the domain. If enabled, TLS will be enforced and SRTP will be
                negotiated on all incoming calls to this sip domain.
            byoc_trunk_sid: The SID of the BYOC Trunk(Bring Your Own Carrier) resource that the Sip Domain will be
                associated with.
            emergency_caller_sid: Whether an emergency caller sid is configured for the domain. If present, this phone
                number will be used as the callback for the emergency call.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/SIP/Domains.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            body=form_body(
                [
                    param[str]("DomainName", domain_name),
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("VoiceUrl", voice_url),
                    param[VoiceMethod7OrStr | None]("VoiceMethod", voice_method),
                    param[str | None]("VoiceFallbackUrl", voice_fallback_url),
                    param[VoiceFallbackMethod7OrStr | None]("VoiceFallbackMethod", voice_fallback_method),
                    param[str | None]("VoiceStatusCallbackUrl", voice_status_callback_url),
                    param[VoiceStatusCallbackMethod1OrStr | None](
                        "VoiceStatusCallbackMethod", voice_status_callback_method
                    ),
                    param[bool | None]("SipRegistration", sip_registration),
                    param[bool | None]("EmergencyCallingEnabled", emergency_calling_enabled),
                    param[bool | None]("Secure", secure),
                    param[str | None]("ByocTrunkSid", byoc_trunk_sid),
                    param[str | None]("EmergencyCallerSid", emergency_caller_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountSipSipDomain],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_sip_domain(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete an instance of a Domain

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                SipDomain resources to delete.
            sid: The Twilio-provided string that uniquely identifies the SipDomain resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_sip_domain(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountSipSipDomain, RawError]:
        """Fetch an instance of a Domain

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                SipDomain resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the SipDomain resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountSipSipDomain],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_sip_domain(
        self,
        account_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSipDomainResponse, RawError]:
        """Retrieve a list of domains belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                SipDomain resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/SIP/Domains.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListSipDomainResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_sip_domain(
        self,
        account_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        voice_fallback_method: VoiceFallbackMethod7OrStr | None = None,
        voice_fallback_url: str | None = None,
        voice_method: VoiceMethod15OrStr | None = None,
        voice_status_callback_method: VoiceStatusCallbackMethod1OrStr | None = None,
        voice_status_callback_url: str | None = None,
        voice_url: str | None = None,
        sip_registration: bool | None = None,
        domain_name: str | None = None,
        emergency_calling_enabled: bool | None = None,
        secure: bool | None = None,
        byoc_trunk_sid: str | None = None,
        emergency_caller_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountSipSipDomain, RawError]:
        """Update the attributes of a domain

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                SipDomain resource to update.
            sid: The Twilio-provided string that uniquely identifies the SipDomain resource to update.
            friendly_name: A descriptive string that you created to describe the resource. It can be up to 64 characters
                long.
            voice_fallback_method: The HTTP method we should use to call ``voice_fallback_url``. Can be: ``GET`` or
                ``POST``.
            voice_fallback_url: The URL that we should call when an error occurs while retrieving or executing the TwiML
                requested by ``voice_url``.
            voice_method: The HTTP method we should use to call ``voice_url``
            voice_status_callback_method: The HTTP method we should use to call ``voice_status_callback_url``. Can be:
                ``GET`` or ``POST``.
            voice_status_callback_url: The URL that we should call to pass status parameters (such as call ended) to
                your application.
            voice_url: The URL we should call when the domain receives a call.
            sip_registration: Whether to allow SIP Endpoints to register with the domain to receive calls. Can be
                ``true`` or ``false``. ``true`` allows SIP Endpoints to register with the domain to receive calls,
                ``false`` does not.
            domain_name: The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can
                contain letters, digits, and "-" and must end with ``sip.twilio.com``.
            emergency_calling_enabled: Whether emergency calling is enabled for the domain. If enabled, allows emergency
                calls on the domain from phone numbers with validated addresses.
            secure: Whether secure SIP is enabled for the domain. If enabled, TLS will be enforced and SRTP will be
                negotiated on all incoming calls to this sip domain.
            byoc_trunk_sid: The SID of the BYOC Trunk(Bring Your Own Carrier) resource that the Sip Domain will be
                associated with.
            emergency_caller_sid: Whether an emergency caller sid is configured for the domain. If present, this phone
                number will be used as the callback for the emergency call.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[VoiceFallbackMethod7OrStr | None]("VoiceFallbackMethod", voice_fallback_method),
                    param[str | None]("VoiceFallbackUrl", voice_fallback_url),
                    param[VoiceMethod15OrStr | None]("VoiceMethod", voice_method),
                    param[VoiceStatusCallbackMethod1OrStr | None](
                        "VoiceStatusCallbackMethod", voice_status_callback_method
                    ),
                    param[str | None]("VoiceStatusCallbackUrl", voice_status_callback_url),
                    param[str | None]("VoiceUrl", voice_url),
                    param[bool | None]("SipRegistration", sip_registration),
                    param[str | None]("DomainName", domain_name),
                    param[bool | None]("EmergencyCallingEnabled", emergency_calling_enabled),
                    param[bool | None]("Secure", secure),
                    param[str | None]("ByocTrunkSid", byoc_trunk_sid),
                    param[str | None]("EmergencyCallerSid", emergency_caller_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountSipSipDomain],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
