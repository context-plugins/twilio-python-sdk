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
from ..models.api_v2010_account_sip_sip_ip_access_control_list_sip_ip_address import (
    ApiV2010AccountSipSipIpAccessControlListSipIpAddress,
)
from ..models.list_sip_ip_address_response import ListSipIpAddressResponse
from ..server.server import Server


class Api20100401SipIpAddress:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401SipIpAddressWithRawResponse(client, server, auth)

    def create_sip_ip_address(
        self,
        account_sid: str,
        ip_access_control_list_sid: str,
        friendly_name: str,
        ip_address: str,
        *,
        cidr_prefix_length: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountSipSipIpAccessControlListSipIpAddress:
        """Create a new IpAddress resource.

        Args:
            account_sid: The unique id of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for
                this resource.
            ip_access_control_list_sid: The IpAccessControlList Sid with which to associate the created IpAddress
                resource.
            friendly_name: A human readable descriptive text for this resource, up to 255 characters long.
            ip_address: An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests
                from this IP address will be allowed by Twilio. IPv4 only supported today.
            cidr_prefix_length: An integer representing the length of the CIDR prefix to use with this IP address when
                accepting traffic. By default the entire IP address is used.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_sip_ip_address(
            account_sid,
            ip_access_control_list_sid,
            friendly_name,
            ip_address,
            cidr_prefix_length=cidr_prefix_length,
            request_options=request_options,
        ).unwrap()

    def delete_sip_ip_address(
        self,
        account_sid: str,
        ip_access_control_list_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Delete an IpAddress resource.

        Args:
            account_sid: The unique id of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for
                this resource.
            ip_access_control_list_sid: The IpAccessControlList Sid that identifies the IpAddress resources to delete.
            sid: A 34 character string that uniquely identifies the resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_sip_ip_address(
            account_sid, ip_access_control_list_sid, sid, request_options=request_options
        ).unwrap()

    def fetch_sip_ip_address(
        self,
        account_sid: str,
        ip_access_control_list_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountSipSipIpAccessControlListSipIpAddress:
        """Read one IpAddress resource.

        Args:
            account_sid: The unique id of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for
                this resource.
            ip_access_control_list_sid: The IpAccessControlList Sid that identifies the IpAddress resources to fetch.
            sid: A 34 character string that uniquely identifies the IpAddress resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_sip_ip_address(
            account_sid, ip_access_control_list_sid, sid, request_options=request_options
        ).unwrap()

    def list_sip_ip_address(
        self,
        account_sid: str,
        ip_access_control_list_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSipIpAddressResponse:
        """Read multiple IpAddress resources.

        Args:
            account_sid: The unique id of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for
                this resource.
            ip_access_control_list_sid: The IpAccessControlList Sid that identifies the IpAddress resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_sip_ip_address(
            account_sid,
            ip_access_control_list_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_sip_ip_address(
        self,
        account_sid: str,
        ip_access_control_list_sid: str,
        sid: str,
        *,
        ip_address: str | None = None,
        friendly_name: str | None = None,
        cidr_prefix_length: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountSipSipIpAccessControlListSipIpAddress:
        """Update an IpAddress resource.

        Args:
            account_sid: The unique id of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for
                this resource.
            ip_access_control_list_sid: The IpAccessControlList Sid that identifies the IpAddress resources to update.
            sid: A 34 character string that identifies the IpAddress resource to update.
            ip_address: An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests
                from this IP address will be allowed by Twilio. IPv4 only supported today.
            friendly_name: A human readable descriptive text for this resource, up to 255 characters long.
            cidr_prefix_length: An integer representing the length of the CIDR prefix to use with this IP address when
                accepting traffic. By default the entire IP address is used.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_sip_ip_address(
            account_sid,
            ip_access_control_list_sid,
            sid,
            ip_address=ip_address,
            friendly_name=friendly_name,
            cidr_prefix_length=cidr_prefix_length,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401SipIpAddressWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401SipIpAddress:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401SipIpAddressWithRawResponse(client, server, auth)

    async def create_sip_ip_address(
        self,
        account_sid: str,
        ip_access_control_list_sid: str,
        friendly_name: str,
        ip_address: str,
        *,
        cidr_prefix_length: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountSipSipIpAccessControlListSipIpAddress:
        """Create a new IpAddress resource.

        Args:
            account_sid: The unique id of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for
                this resource.
            ip_access_control_list_sid: The IpAccessControlList Sid with which to associate the created IpAddress
                resource.
            friendly_name: A human readable descriptive text for this resource, up to 255 characters long.
            ip_address: An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests
                from this IP address will be allowed by Twilio. IPv4 only supported today.
            cidr_prefix_length: An integer representing the length of the CIDR prefix to use with this IP address when
                accepting traffic. By default the entire IP address is used.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_sip_ip_address(
                account_sid,
                ip_access_control_list_sid,
                friendly_name,
                ip_address,
                cidr_prefix_length=cidr_prefix_length,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_sip_ip_address(
        self,
        account_sid: str,
        ip_access_control_list_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Delete an IpAddress resource.

        Args:
            account_sid: The unique id of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for
                this resource.
            ip_access_control_list_sid: The IpAccessControlList Sid that identifies the IpAddress resources to delete.
            sid: A 34 character string that uniquely identifies the resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_sip_ip_address(
                account_sid, ip_access_control_list_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def fetch_sip_ip_address(
        self,
        account_sid: str,
        ip_access_control_list_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountSipSipIpAccessControlListSipIpAddress:
        """Read one IpAddress resource.

        Args:
            account_sid: The unique id of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for
                this resource.
            ip_access_control_list_sid: The IpAccessControlList Sid that identifies the IpAddress resources to fetch.
            sid: A 34 character string that uniquely identifies the IpAddress resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_sip_ip_address(
                account_sid, ip_access_control_list_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def list_sip_ip_address(
        self,
        account_sid: str,
        ip_access_control_list_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSipIpAddressResponse:
        """Read multiple IpAddress resources.

        Args:
            account_sid: The unique id of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for
                this resource.
            ip_access_control_list_sid: The IpAccessControlList Sid that identifies the IpAddress resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_sip_ip_address(
                account_sid,
                ip_access_control_list_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_sip_ip_address(
        self,
        account_sid: str,
        ip_access_control_list_sid: str,
        sid: str,
        *,
        ip_address: str | None = None,
        friendly_name: str | None = None,
        cidr_prefix_length: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountSipSipIpAccessControlListSipIpAddress:
        """Update an IpAddress resource.

        Args:
            account_sid: The unique id of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for
                this resource.
            ip_access_control_list_sid: The IpAccessControlList Sid that identifies the IpAddress resources to update.
            sid: A 34 character string that identifies the IpAddress resource to update.
            ip_address: An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests
                from this IP address will be allowed by Twilio. IPv4 only supported today.
            friendly_name: A human readable descriptive text for this resource, up to 255 characters long.
            cidr_prefix_length: An integer representing the length of the CIDR prefix to use with this IP address when
                accepting traffic. By default the entire IP address is used.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_sip_ip_address(
                account_sid,
                ip_access_control_list_sid,
                sid,
                ip_address=ip_address,
                friendly_name=friendly_name,
                cidr_prefix_length=cidr_prefix_length,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401SipIpAddressWithRawResponse:
        return self._with_raw_response


class Api20100401SipIpAddressWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_sip_ip_address(
        self,
        account_sid: str,
        ip_access_control_list_sid: str,
        friendly_name: str,
        ip_address: str,
        *,
        cidr_prefix_length: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountSipSipIpAccessControlListSipIpAddress, RawError]:
        """Create a new IpAddress resource.

        Args:
            account_sid: The unique id of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for
                this resource.
            ip_access_control_list_sid: The IpAccessControlList Sid with which to associate the created IpAddress
                resource.
            friendly_name: A human readable descriptive text for this resource, up to 255 characters long.
            ip_address: An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests
                from this IP address will be allowed by Twilio. IPv4 only supported today.
            cidr_prefix_length: An integer representing the length of the CIDR prefix to use with this IP address when
                accepting traffic. By default the entire IP address is used.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{IpAccessControlListSid}/IpAddresses.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid), param[str]("IpAccessControlListSid", ip_access_control_list_sid)
            ],
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[str]("IpAddress", ip_address),
                    param[int | None]("CidrPrefixLength", cidr_prefix_length),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountSipSipIpAccessControlListSipIpAddress],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_sip_ip_address(
        self,
        account_sid: str,
        ip_access_control_list_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Delete an IpAddress resource.

        Args:
            account_sid: The unique id of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for
                this resource.
            ip_access_control_list_sid: The IpAccessControlList Sid that identifies the IpAddress resources to delete.
            sid: A 34 character string that uniquely identifies the resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{IpAccessControlListSid}/IpAddresses/{Sid}.json",
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("IpAccessControlListSid", ip_access_control_list_sid),
                param[str]("Sid", sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_sip_ip_address(
        self,
        account_sid: str,
        ip_access_control_list_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountSipSipIpAccessControlListSipIpAddress, RawError]:
        """Read one IpAddress resource.

        Args:
            account_sid: The unique id of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for
                this resource.
            ip_access_control_list_sid: The IpAccessControlList Sid that identifies the IpAddress resources to fetch.
            sid: A 34 character string that uniquely identifies the IpAddress resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{IpAccessControlListSid}/IpAddresses/{Sid}.json",
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("IpAccessControlListSid", ip_access_control_list_sid),
                param[str]("Sid", sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountSipSipIpAccessControlListSipIpAddress],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_sip_ip_address(
        self,
        account_sid: str,
        ip_access_control_list_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSipIpAddressResponse, RawError]:
        """Read multiple IpAddress resources.

        Args:
            account_sid: The unique id of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for
                this resource.
            ip_access_control_list_sid: The IpAccessControlList Sid that identifies the IpAddress resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{IpAccessControlListSid}/IpAddresses.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid), param[str]("IpAccessControlListSid", ip_access_control_list_sid)
            ],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListSipIpAddressResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_sip_ip_address(
        self,
        account_sid: str,
        ip_access_control_list_sid: str,
        sid: str,
        *,
        ip_address: str | None = None,
        friendly_name: str | None = None,
        cidr_prefix_length: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountSipSipIpAccessControlListSipIpAddress, RawError]:
        """Update an IpAddress resource.

        Args:
            account_sid: The unique id of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for
                this resource.
            ip_access_control_list_sid: The IpAccessControlList Sid that identifies the IpAddress resources to update.
            sid: A 34 character string that identifies the IpAddress resource to update.
            ip_address: An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests
                from this IP address will be allowed by Twilio. IPv4 only supported today.
            friendly_name: A human readable descriptive text for this resource, up to 255 characters long.
            cidr_prefix_length: An integer representing the length of the CIDR prefix to use with this IP address when
                accepting traffic. By default the entire IP address is used.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{IpAccessControlListSid}/IpAddresses/{Sid}.json",
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("IpAccessControlListSid", ip_access_control_list_sid),
                param[str]("Sid", sid),
            ],
            body=form_body(
                [
                    param[str | None]("IpAddress", ip_address),
                    param[str | None]("FriendlyName", friendly_name),
                    param[int | None]("CidrPrefixLength", cidr_prefix_length),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountSipSipIpAccessControlListSipIpAddress],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401SipIpAddressWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_sip_ip_address(
        self,
        account_sid: str,
        ip_access_control_list_sid: str,
        friendly_name: str,
        ip_address: str,
        *,
        cidr_prefix_length: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountSipSipIpAccessControlListSipIpAddress, RawError]:
        """Create a new IpAddress resource.

        Args:
            account_sid: The unique id of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for
                this resource.
            ip_access_control_list_sid: The IpAccessControlList Sid with which to associate the created IpAddress
                resource.
            friendly_name: A human readable descriptive text for this resource, up to 255 characters long.
            ip_address: An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests
                from this IP address will be allowed by Twilio. IPv4 only supported today.
            cidr_prefix_length: An integer representing the length of the CIDR prefix to use with this IP address when
                accepting traffic. By default the entire IP address is used.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{IpAccessControlListSid}/IpAddresses.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid), param[str]("IpAccessControlListSid", ip_access_control_list_sid)
            ],
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[str]("IpAddress", ip_address),
                    param[int | None]("CidrPrefixLength", cidr_prefix_length),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountSipSipIpAccessControlListSipIpAddress],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_sip_ip_address(
        self,
        account_sid: str,
        ip_access_control_list_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Delete an IpAddress resource.

        Args:
            account_sid: The unique id of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for
                this resource.
            ip_access_control_list_sid: The IpAccessControlList Sid that identifies the IpAddress resources to delete.
            sid: A 34 character string that uniquely identifies the resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{IpAccessControlListSid}/IpAddresses/{Sid}.json",
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("IpAccessControlListSid", ip_access_control_list_sid),
                param[str]("Sid", sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_sip_ip_address(
        self,
        account_sid: str,
        ip_access_control_list_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountSipSipIpAccessControlListSipIpAddress, RawError]:
        """Read one IpAddress resource.

        Args:
            account_sid: The unique id of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for
                this resource.
            ip_access_control_list_sid: The IpAccessControlList Sid that identifies the IpAddress resources to fetch.
            sid: A 34 character string that uniquely identifies the IpAddress resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{IpAccessControlListSid}/IpAddresses/{Sid}.json",
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("IpAccessControlListSid", ip_access_control_list_sid),
                param[str]("Sid", sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountSipSipIpAccessControlListSipIpAddress],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_sip_ip_address(
        self,
        account_sid: str,
        ip_access_control_list_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSipIpAddressResponse, RawError]:
        """Read multiple IpAddress resources.

        Args:
            account_sid: The unique id of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for
                this resource.
            ip_access_control_list_sid: The IpAccessControlList Sid that identifies the IpAddress resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{IpAccessControlListSid}/IpAddresses.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid), param[str]("IpAccessControlListSid", ip_access_control_list_sid)
            ],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListSipIpAddressResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_sip_ip_address(
        self,
        account_sid: str,
        ip_access_control_list_sid: str,
        sid: str,
        *,
        ip_address: str | None = None,
        friendly_name: str | None = None,
        cidr_prefix_length: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountSipSipIpAccessControlListSipIpAddress, RawError]:
        """Update an IpAddress resource.

        Args:
            account_sid: The unique id of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for
                this resource.
            ip_access_control_list_sid: The IpAccessControlList Sid that identifies the IpAddress resources to update.
            sid: A 34 character string that identifies the IpAddress resource to update.
            ip_address: An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests
                from this IP address will be allowed by Twilio. IPv4 only supported today.
            friendly_name: A human readable descriptive text for this resource, up to 255 characters long.
            cidr_prefix_length: An integer representing the length of the CIDR prefix to use with this IP address when
                accepting traffic. By default the entire IP address is used.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{IpAccessControlListSid}/IpAddresses/{Sid}.json",
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("IpAccessControlListSid", ip_access_control_list_sid),
                param[str]("Sid", sid),
            ],
            body=form_body(
                [
                    param[str | None]("IpAddress", ip_address),
                    param[str | None]("FriendlyName", friendly_name),
                    param[int | None]("CidrPrefixLength", cidr_prefix_length),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountSipSipIpAccessControlListSipIpAddress],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
