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
from ..models.api_v2010_account_sip_sip_domain_sip_credential_list_mapping import (
    ApiV2010AccountSipSipDomainSipCredentialListMapping,
)
from ..models.list_sip_credential_list_mapping_response import ListSipCredentialListMappingResponse
from ..server.server import Server


class Api20100401CredentialListMapping:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401CredentialListMappingWithRawResponse(client, server, auth)

    def create_sip_credential_list_mapping(
        self,
        account_sid: str,
        domain_sid: str,
        credential_list_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountSipSipDomainSipCredentialListMapping:
        """Create a CredentialListMapping resource for an account.

        Args:
            account_sid: The unique id of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for
                this resource.
            domain_sid: A 34 character string that uniquely identifies the SIP Domain for which the CredentialList
                resource will be mapped.
            credential_list_sid: A 34 character string that uniquely identifies the CredentialList resource to map to
                the SIP domain.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_sip_credential_list_mapping(
            account_sid, domain_sid, credential_list_sid, request_options=request_options
        ).unwrap()

    def delete_sip_credential_list_mapping(
        self, account_sid: str, domain_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a CredentialListMapping resource from an account.

        Args:
            account_sid: The unique id of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for
                this resource.
            domain_sid: A 34 character string that uniquely identifies the SIP Domain that includes the resource to
                delete.
            sid: A 34 character string that uniquely identifies the resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_sip_credential_list_mapping(
            account_sid, domain_sid, sid, request_options=request_options
        ).unwrap()

    def fetch_sip_credential_list_mapping(
        self, account_sid: str, domain_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountSipSipDomainSipCredentialListMapping:
        """Fetch a single CredentialListMapping resource from an account.

        Args:
            account_sid: The unique id of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for
                this resource.
            domain_sid: A 34 character string that uniquely identifies the SIP Domain that includes the resource to
                fetch.
            sid: A 34 character string that uniquely identifies the resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_sip_credential_list_mapping(
            account_sid, domain_sid, sid, request_options=request_options
        ).unwrap()

    def list_sip_credential_list_mapping(
        self,
        account_sid: str,
        domain_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSipCredentialListMappingResponse:
        """Read multiple CredentialListMapping resources from an account.

        Args:
            account_sid: The unique id of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for
                this resource.
            domain_sid: A 34 character string that uniquely identifies the SIP Domain that includes the resource to
                read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_sip_credential_list_mapping(
            account_sid,
            domain_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401CredentialListMappingWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401CredentialListMapping:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401CredentialListMappingWithRawResponse(client, server, auth)

    async def create_sip_credential_list_mapping(
        self,
        account_sid: str,
        domain_sid: str,
        credential_list_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountSipSipDomainSipCredentialListMapping:
        """Create a CredentialListMapping resource for an account.

        Args:
            account_sid: The unique id of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for
                this resource.
            domain_sid: A 34 character string that uniquely identifies the SIP Domain for which the CredentialList
                resource will be mapped.
            credential_list_sid: A 34 character string that uniquely identifies the CredentialList resource to map to
                the SIP domain.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_sip_credential_list_mapping(
                account_sid, domain_sid, credential_list_sid, request_options=request_options
            )
        ).unwrap()

    async def delete_sip_credential_list_mapping(
        self, account_sid: str, domain_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a CredentialListMapping resource from an account.

        Args:
            account_sid: The unique id of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for
                this resource.
            domain_sid: A 34 character string that uniquely identifies the SIP Domain that includes the resource to
                delete.
            sid: A 34 character string that uniquely identifies the resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_sip_credential_list_mapping(
                account_sid, domain_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def fetch_sip_credential_list_mapping(
        self, account_sid: str, domain_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountSipSipDomainSipCredentialListMapping:
        """Fetch a single CredentialListMapping resource from an account.

        Args:
            account_sid: The unique id of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for
                this resource.
            domain_sid: A 34 character string that uniquely identifies the SIP Domain that includes the resource to
                fetch.
            sid: A 34 character string that uniquely identifies the resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_sip_credential_list_mapping(
                account_sid, domain_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def list_sip_credential_list_mapping(
        self,
        account_sid: str,
        domain_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSipCredentialListMappingResponse:
        """Read multiple CredentialListMapping resources from an account.

        Args:
            account_sid: The unique id of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for
                this resource.
            domain_sid: A 34 character string that uniquely identifies the SIP Domain that includes the resource to
                read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_sip_credential_list_mapping(
                account_sid,
                domain_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401CredentialListMappingWithRawResponse:
        return self._with_raw_response


class Api20100401CredentialListMappingWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_sip_credential_list_mapping(
        self,
        account_sid: str,
        domain_sid: str,
        credential_list_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountSipSipDomainSipCredentialListMapping, RawError]:
        """Create a CredentialListMapping resource for an account.

        Args:
            account_sid: The unique id of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for
                this resource.
            domain_sid: A 34 character string that uniquely identifies the SIP Domain for which the CredentialList
                resource will be mapped.
            credential_list_sid: A 34 character string that uniquely identifies the CredentialList resource to map to
                the SIP domain.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/CredentialListMappings.json"
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("DomainSid", domain_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str]("CredentialListSid", credential_list_sid)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountSipSipDomainSipCredentialListMapping],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_sip_credential_list_mapping(
        self, account_sid: str, domain_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a CredentialListMapping resource from an account.

        Args:
            account_sid: The unique id of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for
                this resource.
            domain_sid: A 34 character string that uniquely identifies the SIP Domain that includes the resource to
                delete.
            sid: A 34 character string that uniquely identifies the resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/CredentialListMappings/{Sid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid), param[str]("DomainSid", domain_sid), param[str]("Sid", sid)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_sip_credential_list_mapping(
        self, account_sid: str, domain_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountSipSipDomainSipCredentialListMapping, RawError]:
        """Fetch a single CredentialListMapping resource from an account.

        Args:
            account_sid: The unique id of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for
                this resource.
            domain_sid: A 34 character string that uniquely identifies the SIP Domain that includes the resource to
                fetch.
            sid: A 34 character string that uniquely identifies the resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/CredentialListMappings/{Sid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid), param[str]("DomainSid", domain_sid), param[str]("Sid", sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountSipSipDomainSipCredentialListMapping],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_sip_credential_list_mapping(
        self,
        account_sid: str,
        domain_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSipCredentialListMappingResponse, RawError]:
        """Read multiple CredentialListMapping resources from an account.

        Args:
            account_sid: The unique id of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for
                this resource.
            domain_sid: A 34 character string that uniquely identifies the SIP Domain that includes the resource to
                read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/CredentialListMappings.json"
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("DomainSid", domain_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListSipCredentialListMappingResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401CredentialListMappingWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def create_sip_credential_list_mapping(
        self,
        account_sid: str,
        domain_sid: str,
        credential_list_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountSipSipDomainSipCredentialListMapping, RawError]:
        """Create a CredentialListMapping resource for an account.

        Args:
            account_sid: The unique id of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for
                this resource.
            domain_sid: A 34 character string that uniquely identifies the SIP Domain for which the CredentialList
                resource will be mapped.
            credential_list_sid: A 34 character string that uniquely identifies the CredentialList resource to map to
                the SIP domain.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/CredentialListMappings.json"
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("DomainSid", domain_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str]("CredentialListSid", credential_list_sid)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountSipSipDomainSipCredentialListMapping],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_sip_credential_list_mapping(
        self, account_sid: str, domain_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a CredentialListMapping resource from an account.

        Args:
            account_sid: The unique id of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for
                this resource.
            domain_sid: A 34 character string that uniquely identifies the SIP Domain that includes the resource to
                delete.
            sid: A 34 character string that uniquely identifies the resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/CredentialListMappings/{Sid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid), param[str]("DomainSid", domain_sid), param[str]("Sid", sid)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_sip_credential_list_mapping(
        self, account_sid: str, domain_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountSipSipDomainSipCredentialListMapping, RawError]:
        """Fetch a single CredentialListMapping resource from an account.

        Args:
            account_sid: The unique id of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for
                this resource.
            domain_sid: A 34 character string that uniquely identifies the SIP Domain that includes the resource to
                fetch.
            sid: A 34 character string that uniquely identifies the resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/CredentialListMappings/{Sid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid), param[str]("DomainSid", domain_sid), param[str]("Sid", sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountSipSipDomainSipCredentialListMapping],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_sip_credential_list_mapping(
        self,
        account_sid: str,
        domain_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSipCredentialListMappingResponse, RawError]:
        """Read multiple CredentialListMapping resources from an account.

        Args:
            account_sid: The unique id of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for
                this resource.
            domain_sid: A 34 character string that uniquely identifies the SIP Domain that includes the resource to
                read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/CredentialListMappings.json"
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("DomainSid", domain_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListSipCredentialListMappingResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
