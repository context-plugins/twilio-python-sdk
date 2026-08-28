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
from ..models.api_v2010_account_sip_sip_domain_sip_ip_access_control_list_mapping import (
    ApiV2010AccountSipSipDomainSipIpAccessControlListMapping,
)
from ..models.list_sip_ip_access_control_list_mapping_response import ListSipIpAccessControlListMappingResponse
from ..server.server import Server


class Api20100401IpAccessControlListMapping:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401IpAccessControlListMappingWithRawResponse(client, server, auth)

    def create_sip_ip_access_control_list_mapping(
        self,
        account_sid: str,
        domain_sid: str,
        ip_access_control_list_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountSipSipDomainSipIpAccessControlListMapping:
        """Create a new IpAccessControlListMapping resource.

        Args:
            account_sid: The unique id of the Account that is responsible for this resource.
            domain_sid: A 34 character string that uniquely identifies the SIP domain.
            ip_access_control_list_sid: The unique id of the IP access control list to map to the SIP domain.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_sip_ip_access_control_list_mapping(
            account_sid, domain_sid, ip_access_control_list_sid, request_options=request_options
        ).unwrap()

    def delete_sip_ip_access_control_list_mapping(
        self, account_sid: str, domain_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete an IpAccessControlListMapping resource.

        Args:
            account_sid: The unique id of the Account that is responsible for this resource.
            domain_sid: A 34 character string that uniquely identifies the SIP domain.
            sid: A 34 character string that uniquely identifies the resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_sip_ip_access_control_list_mapping(
            account_sid, domain_sid, sid, request_options=request_options
        ).unwrap()

    def fetch_sip_ip_access_control_list_mapping(
        self, account_sid: str, domain_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountSipSipDomainSipIpAccessControlListMapping:
        """Fetch an IpAccessControlListMapping resource.

        Args:
            account_sid: The unique id of the Account that is responsible for this resource.
            domain_sid: A 34 character string that uniquely identifies the SIP domain.
            sid: A 34 character string that uniquely identifies the resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_sip_ip_access_control_list_mapping(
            account_sid, domain_sid, sid, request_options=request_options
        ).unwrap()

    def list_sip_ip_access_control_list_mapping(
        self,
        account_sid: str,
        domain_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSipIpAccessControlListMappingResponse:
        """Retrieve a list of IpAccessControlListMapping resources.

        Args:
            account_sid: The unique id of the Account that is responsible for this resource.
            domain_sid: A 34 character string that uniquely identifies the SIP domain.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_sip_ip_access_control_list_mapping(
            account_sid,
            domain_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401IpAccessControlListMappingWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401IpAccessControlListMapping:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401IpAccessControlListMappingWithRawResponse(client, server, auth)

    async def create_sip_ip_access_control_list_mapping(
        self,
        account_sid: str,
        domain_sid: str,
        ip_access_control_list_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountSipSipDomainSipIpAccessControlListMapping:
        """Create a new IpAccessControlListMapping resource.

        Args:
            account_sid: The unique id of the Account that is responsible for this resource.
            domain_sid: A 34 character string that uniquely identifies the SIP domain.
            ip_access_control_list_sid: The unique id of the IP access control list to map to the SIP domain.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_sip_ip_access_control_list_mapping(
                account_sid, domain_sid, ip_access_control_list_sid, request_options=request_options
            )
        ).unwrap()

    async def delete_sip_ip_access_control_list_mapping(
        self, account_sid: str, domain_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete an IpAccessControlListMapping resource.

        Args:
            account_sid: The unique id of the Account that is responsible for this resource.
            domain_sid: A 34 character string that uniquely identifies the SIP domain.
            sid: A 34 character string that uniquely identifies the resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_sip_ip_access_control_list_mapping(
                account_sid, domain_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def fetch_sip_ip_access_control_list_mapping(
        self, account_sid: str, domain_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountSipSipDomainSipIpAccessControlListMapping:
        """Fetch an IpAccessControlListMapping resource.

        Args:
            account_sid: The unique id of the Account that is responsible for this resource.
            domain_sid: A 34 character string that uniquely identifies the SIP domain.
            sid: A 34 character string that uniquely identifies the resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_sip_ip_access_control_list_mapping(
                account_sid, domain_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def list_sip_ip_access_control_list_mapping(
        self,
        account_sid: str,
        domain_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSipIpAccessControlListMappingResponse:
        """Retrieve a list of IpAccessControlListMapping resources.

        Args:
            account_sid: The unique id of the Account that is responsible for this resource.
            domain_sid: A 34 character string that uniquely identifies the SIP domain.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_sip_ip_access_control_list_mapping(
                account_sid,
                domain_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401IpAccessControlListMappingWithRawResponse:
        return self._with_raw_response


class Api20100401IpAccessControlListMappingWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_sip_ip_access_control_list_mapping(
        self,
        account_sid: str,
        domain_sid: str,
        ip_access_control_list_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountSipSipDomainSipIpAccessControlListMapping, RawError]:
        """Create a new IpAccessControlListMapping resource.

        Args:
            account_sid: The unique id of the Account that is responsible for this resource.
            domain_sid: A 34 character string that uniquely identifies the SIP domain.
            ip_access_control_list_sid: The unique id of the IP access control list to map to the SIP domain.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/IpAccessControlListMappings.json"
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("DomainSid", domain_sid)],
            body=form_body([param[str]("IpAccessControlListSid", ip_access_control_list_sid)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountSipSipDomainSipIpAccessControlListMapping],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_sip_ip_access_control_list_mapping(
        self, account_sid: str, domain_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete an IpAccessControlListMapping resource.

        Args:
            account_sid: The unique id of the Account that is responsible for this resource.
            domain_sid: A 34 character string that uniquely identifies the SIP domain.
            sid: A 34 character string that uniquely identifies the resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/IpAccessControlListMappings/{Sid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid), param[str]("DomainSid", domain_sid), param[str]("Sid", sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_sip_ip_access_control_list_mapping(
        self, account_sid: str, domain_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountSipSipDomainSipIpAccessControlListMapping, RawError]:
        """Fetch an IpAccessControlListMapping resource.

        Args:
            account_sid: The unique id of the Account that is responsible for this resource.
            domain_sid: A 34 character string that uniquely identifies the SIP domain.
            sid: A 34 character string that uniquely identifies the resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/IpAccessControlListMappings/{Sid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid), param[str]("DomainSid", domain_sid), param[str]("Sid", sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountSipSipDomainSipIpAccessControlListMapping],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_sip_ip_access_control_list_mapping(
        self,
        account_sid: str,
        domain_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSipIpAccessControlListMappingResponse, RawError]:
        """Retrieve a list of IpAccessControlListMapping resources.

        Args:
            account_sid: The unique id of the Account that is responsible for this resource.
            domain_sid: A 34 character string that uniquely identifies the SIP domain.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/IpAccessControlListMappings.json"
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("DomainSid", domain_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListSipIpAccessControlListMappingResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401IpAccessControlListMappingWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def create_sip_ip_access_control_list_mapping(
        self,
        account_sid: str,
        domain_sid: str,
        ip_access_control_list_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountSipSipDomainSipIpAccessControlListMapping, RawError]:
        """Create a new IpAccessControlListMapping resource.

        Args:
            account_sid: The unique id of the Account that is responsible for this resource.
            domain_sid: A 34 character string that uniquely identifies the SIP domain.
            ip_access_control_list_sid: The unique id of the IP access control list to map to the SIP domain.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/IpAccessControlListMappings.json"
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("DomainSid", domain_sid)],
            body=form_body([param[str]("IpAccessControlListSid", ip_access_control_list_sid)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountSipSipDomainSipIpAccessControlListMapping],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_sip_ip_access_control_list_mapping(
        self, account_sid: str, domain_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete an IpAccessControlListMapping resource.

        Args:
            account_sid: The unique id of the Account that is responsible for this resource.
            domain_sid: A 34 character string that uniquely identifies the SIP domain.
            sid: A 34 character string that uniquely identifies the resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/IpAccessControlListMappings/{Sid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid), param[str]("DomainSid", domain_sid), param[str]("Sid", sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_sip_ip_access_control_list_mapping(
        self, account_sid: str, domain_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountSipSipDomainSipIpAccessControlListMapping, RawError]:
        """Fetch an IpAccessControlListMapping resource.

        Args:
            account_sid: The unique id of the Account that is responsible for this resource.
            domain_sid: A 34 character string that uniquely identifies the SIP domain.
            sid: A 34 character string that uniquely identifies the resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/IpAccessControlListMappings/{Sid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid), param[str]("DomainSid", domain_sid), param[str]("Sid", sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountSipSipDomainSipIpAccessControlListMapping],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_sip_ip_access_control_list_mapping(
        self,
        account_sid: str,
        domain_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSipIpAccessControlListMappingResponse, RawError]:
        """Retrieve a list of IpAccessControlListMapping resources.

        Args:
            account_sid: The unique id of the Account that is responsible for this resource.
            domain_sid: A 34 character string that uniquely identifies the SIP domain.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/IpAccessControlListMappings.json"
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("DomainSid", domain_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListSipIpAccessControlListMappingResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
