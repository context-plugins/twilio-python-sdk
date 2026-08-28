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
from ..models.list_sip_auth_registrations_credential_list_mapping_response import (
    ListSipAuthRegistrationsCredentialListMappingResponse,
)
from ..models.sip_auth_registrations_credential_list_mapping import SipAuthRegistrationsCredentialListMapping
from ..server.server import Server


class Api20100401AuthRegistrationsCredentialListMapping:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401AuthRegistrationsCredentialListMappingWithRawResponse(client, server, auth)

    def create_sip_auth_registrations_credential_list_mapping(
        self,
        account_sid: str,
        domain_sid: str,
        credential_list_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SipAuthRegistrationsCredentialListMapping:
        """Create a new credential list mapping resource

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            domain_sid: The SID of the SIP domain that will contain the new resource.
            credential_list_sid: The SID of the CredentialList resource to map to the SIP domain.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_sip_auth_registrations_credential_list_mapping(
            account_sid, domain_sid, credential_list_sid, request_options=request_options
        ).unwrap()

    def delete_sip_auth_registrations_credential_list_mapping(
        self, account_sid: str, domain_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a credential list mapping from the requested domain

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                CredentialListMapping resources to delete.
            domain_sid: The SID of the SIP domain that contains the resources to delete.
            sid: The Twilio-provided string that uniquely identifies the CredentialListMapping resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_sip_auth_registrations_credential_list_mapping(
            account_sid, domain_sid, sid, request_options=request_options
        ).unwrap()

    def fetch_sip_auth_registrations_credential_list_mapping(
        self, account_sid: str, domain_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SipAuthRegistrationsCredentialListMapping:
        """Fetch a specific instance of a credential list mapping

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                CredentialListMapping resource to fetch.
            domain_sid: The SID of the SIP domain that contains the resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the CredentialListMapping resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_sip_auth_registrations_credential_list_mapping(
            account_sid, domain_sid, sid, request_options=request_options
        ).unwrap()

    def list_sip_auth_registrations_credential_list_mapping(
        self,
        account_sid: str,
        domain_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSipAuthRegistrationsCredentialListMappingResponse:
        """Retrieve a list of credential list mappings belonging to the domain used in the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                CredentialListMapping resources to read.
            domain_sid: The SID of the SIP domain that contains the resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_sip_auth_registrations_credential_list_mapping(
            account_sid,
            domain_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401AuthRegistrationsCredentialListMappingWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401AuthRegistrationsCredentialListMapping:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401AuthRegistrationsCredentialListMappingWithRawResponse(
            client, server, auth
        )

    async def create_sip_auth_registrations_credential_list_mapping(
        self,
        account_sid: str,
        domain_sid: str,
        credential_list_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SipAuthRegistrationsCredentialListMapping:
        """Create a new credential list mapping resource

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            domain_sid: The SID of the SIP domain that will contain the new resource.
            credential_list_sid: The SID of the CredentialList resource to map to the SIP domain.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_sip_auth_registrations_credential_list_mapping(
                account_sid, domain_sid, credential_list_sid, request_options=request_options
            )
        ).unwrap()

    async def delete_sip_auth_registrations_credential_list_mapping(
        self, account_sid: str, domain_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a credential list mapping from the requested domain

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                CredentialListMapping resources to delete.
            domain_sid: The SID of the SIP domain that contains the resources to delete.
            sid: The Twilio-provided string that uniquely identifies the CredentialListMapping resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_sip_auth_registrations_credential_list_mapping(
                account_sid, domain_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def fetch_sip_auth_registrations_credential_list_mapping(
        self, account_sid: str, domain_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SipAuthRegistrationsCredentialListMapping:
        """Fetch a specific instance of a credential list mapping

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                CredentialListMapping resource to fetch.
            domain_sid: The SID of the SIP domain that contains the resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the CredentialListMapping resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_sip_auth_registrations_credential_list_mapping(
                account_sid, domain_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def list_sip_auth_registrations_credential_list_mapping(
        self,
        account_sid: str,
        domain_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSipAuthRegistrationsCredentialListMappingResponse:
        """Retrieve a list of credential list mappings belonging to the domain used in the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                CredentialListMapping resources to read.
            domain_sid: The SID of the SIP domain that contains the resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_sip_auth_registrations_credential_list_mapping(
                account_sid,
                domain_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401AuthRegistrationsCredentialListMappingWithRawResponse:
        return self._with_raw_response


class Api20100401AuthRegistrationsCredentialListMappingWithRawResponse(
    SecuredRawResponse[RawClient, Server, AuthSchemes]
):
    def create_sip_auth_registrations_credential_list_mapping(
        self,
        account_sid: str,
        domain_sid: str,
        credential_list_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SipAuthRegistrationsCredentialListMapping, RawError]:
        """Create a new credential list mapping resource

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            domain_sid: The SID of the SIP domain that will contain the new resource.
            credential_list_sid: The SID of the CredentialList resource to map to the SIP domain.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Registrations/CredentialListMappings.json",
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("DomainSid", domain_sid)],
            body=form_body([param[str]("CredentialListSid", credential_list_sid)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SipAuthRegistrationsCredentialListMapping],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_sip_auth_registrations_credential_list_mapping(
        self, account_sid: str, domain_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a credential list mapping from the requested domain

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                CredentialListMapping resources to delete.
            domain_sid: The SID of the SIP domain that contains the resources to delete.
            sid: The Twilio-provided string that uniquely identifies the CredentialListMapping resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Registrations/CredentialListMappings/{Sid}.json",
            ),
            path_params=[
                param[str]("AccountSid", account_sid), param[str]("DomainSid", domain_sid), param[str]("Sid", sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_sip_auth_registrations_credential_list_mapping(
        self, account_sid: str, domain_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SipAuthRegistrationsCredentialListMapping, RawError]:
        """Fetch a specific instance of a credential list mapping

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                CredentialListMapping resource to fetch.
            domain_sid: The SID of the SIP domain that contains the resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the CredentialListMapping resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Registrations/CredentialListMappings/{Sid}.json",
            ),
            path_params=[
                param[str]("AccountSid", account_sid), param[str]("DomainSid", domain_sid), param[str]("Sid", sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SipAuthRegistrationsCredentialListMapping],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_sip_auth_registrations_credential_list_mapping(
        self,
        account_sid: str,
        domain_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSipAuthRegistrationsCredentialListMappingResponse, RawError]:
        """Retrieve a list of credential list mappings belonging to the domain used in the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                CredentialListMapping resources to read.
            domain_sid: The SID of the SIP domain that contains the resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Registrations/CredentialListMappings.json",
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("DomainSid", domain_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListSipAuthRegistrationsCredentialListMappingResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401AuthRegistrationsCredentialListMappingWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def create_sip_auth_registrations_credential_list_mapping(
        self,
        account_sid: str,
        domain_sid: str,
        credential_list_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SipAuthRegistrationsCredentialListMapping, RawError]:
        """Create a new credential list mapping resource

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            domain_sid: The SID of the SIP domain that will contain the new resource.
            credential_list_sid: The SID of the CredentialList resource to map to the SIP domain.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Registrations/CredentialListMappings.json",
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("DomainSid", domain_sid)],
            body=form_body([param[str]("CredentialListSid", credential_list_sid)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SipAuthRegistrationsCredentialListMapping],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_sip_auth_registrations_credential_list_mapping(
        self, account_sid: str, domain_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a credential list mapping from the requested domain

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                CredentialListMapping resources to delete.
            domain_sid: The SID of the SIP domain that contains the resources to delete.
            sid: The Twilio-provided string that uniquely identifies the CredentialListMapping resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Registrations/CredentialListMappings/{Sid}.json",
            ),
            path_params=[
                param[str]("AccountSid", account_sid), param[str]("DomainSid", domain_sid), param[str]("Sid", sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_sip_auth_registrations_credential_list_mapping(
        self, account_sid: str, domain_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SipAuthRegistrationsCredentialListMapping, RawError]:
        """Fetch a specific instance of a credential list mapping

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                CredentialListMapping resource to fetch.
            domain_sid: The SID of the SIP domain that contains the resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the CredentialListMapping resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Registrations/CredentialListMappings/{Sid}.json",
            ),
            path_params=[
                param[str]("AccountSid", account_sid), param[str]("DomainSid", domain_sid), param[str]("Sid", sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SipAuthRegistrationsCredentialListMapping],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_sip_auth_registrations_credential_list_mapping(
        self,
        account_sid: str,
        domain_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSipAuthRegistrationsCredentialListMappingResponse, RawError]:
        """Retrieve a list of credential list mappings belonging to the domain used in the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                CredentialListMapping resources to read.
            domain_sid: The SID of the SIP domain that contains the resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Registrations/CredentialListMappings.json",
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("DomainSid", domain_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListSipAuthRegistrationsCredentialListMappingResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
