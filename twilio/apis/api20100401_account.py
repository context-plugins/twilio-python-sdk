from __future__ import annotations

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
from ..models.api_v2010_account import ApiV2010Account
from ..models.enums.account_enum_status import AccountEnumStatusOrStr
from ..models.list_account_response import ListAccountResponse
from ..server.server import Server


class Api20100401Account:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401AccountWithRawResponse(client, server, auth)

    def create_account(
        self, *, friendly_name: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010Account:
        """Create a new Twilio Subaccount from the account making the request

        Args:
            friendly_name: A human readable description of the account to create, defaults to ``SubAccount Created at
                {YYYY-MM-DD HH:MM meridian}``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_account(
            friendly_name=friendly_name, request_options=request_options
        ).unwrap()

    def fetch_account(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiV2010Account:
        """Fetch the account specified by the provided Account Sid

        Args:
            sid: The Account Sid that uniquely identifies the account to fetch
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_account(sid, request_options=request_options).unwrap()

    def list_account(
        self,
        *,
        friendly_name: str | None = None,
        status: AccountEnumStatusOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListAccountResponse:
        """Retrieves a collection of Accounts belonging to the account used to make the request

        Args:
            friendly_name: Only return the Account resources with friendly names that exactly match this name.
            status: Only return Account resources with the given status. Can be ``closed``, ``suspended`` or ``active``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_account(
            friendly_name=friendly_name,
            status=status,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_account(
        self,
        sid: str,
        *,
        friendly_name: str | None = None,
        status: AccountEnumStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010Account:
        """Modify the properties of a given Account

        Args:
            sid: The Account Sid that uniquely identifies the account to update
            friendly_name: Update the human-readable description of this Account
            status: The status of this account. Usually ``active``, but can be ``suspended`` or ``closed``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_account(
            sid, friendly_name=friendly_name, status=status, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401AccountWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401Account:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401AccountWithRawResponse(client, server, auth)

    async def create_account(
        self, *, friendly_name: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010Account:
        """Create a new Twilio Subaccount from the account making the request

        Args:
            friendly_name: A human readable description of the account to create, defaults to ``SubAccount Created at
                {YYYY-MM-DD HH:MM meridian}``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_account(friendly_name=friendly_name, request_options=request_options)
        ).unwrap()

    async def fetch_account(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiV2010Account:
        """Fetch the account specified by the provided Account Sid

        Args:
            sid: The Account Sid that uniquely identifies the account to fetch
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_account(sid, request_options=request_options)).unwrap()

    async def list_account(
        self,
        *,
        friendly_name: str | None = None,
        status: AccountEnumStatusOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListAccountResponse:
        """Retrieves a collection of Accounts belonging to the account used to make the request

        Args:
            friendly_name: Only return the Account resources with friendly names that exactly match this name.
            status: Only return Account resources with the given status. Can be ``closed``, ``suspended`` or ``active``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_account(
                friendly_name=friendly_name,
                status=status,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_account(
        self,
        sid: str,
        *,
        friendly_name: str | None = None,
        status: AccountEnumStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010Account:
        """Modify the properties of a given Account

        Args:
            sid: The Account Sid that uniquely identifies the account to update
            friendly_name: Update the human-readable description of this Account
            status: The status of this account. Usually ``active``, but can be ``suspended`` or ``closed``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_account(
                sid, friendly_name=friendly_name, status=status, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401AccountWithRawResponse:
        return self._with_raw_response


class Api20100401AccountWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_account(
        self, *, friendly_name: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010Account, RawError]:
        """Create a new Twilio Subaccount from the account making the request

        Args:
            friendly_name: A human readable description of the account to create, defaults to ``SubAccount Created at
                {YYYY-MM-DD HH:MM meridian}``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts.json"),
            body=form_body([param[str | None]("FriendlyName", friendly_name)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010Account],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_account(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010Account, RawError]:
        """Fetch the account specified by the provided Account Sid

        Args:
            sid: The Account Sid that uniquely identifies the account to fetch
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{Sid}.json"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010Account],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_account(
        self,
        *,
        friendly_name: str | None = None,
        status: AccountEnumStatusOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListAccountResponse, RawError]:
        """Retrieves a collection of Accounts belonging to the account used to make the request

        Args:
            friendly_name: Only return the Account resources with friendly names that exactly match this name.
            status: Only return Account resources with the given status. Can be ``closed``, ``suspended`` or ``active``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts.json"),
            query_params=[
                param[str | None]("FriendlyName", friendly_name),
                param[AccountEnumStatusOrStr | None]("Status", status),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListAccountResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_account(
        self,
        sid: str,
        *,
        friendly_name: str | None = None,
        status: AccountEnumStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010Account, RawError]:
        """Modify the properties of a given Account

        Args:
            sid: The Account Sid that uniquely identifies the account to update
            friendly_name: Update the human-readable description of this Account
            status: The status of this account. Usually ``active``, but can be ``suspended`` or ``closed``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{Sid}.json"),
            path_params=[param[str]("Sid", sid)],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[AccountEnumStatusOrStr | None]("Status", status),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010Account],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401AccountWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_account(
        self, *, friendly_name: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010Account, RawError]:
        """Create a new Twilio Subaccount from the account making the request

        Args:
            friendly_name: A human readable description of the account to create, defaults to ``SubAccount Created at
                {YYYY-MM-DD HH:MM meridian}``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts.json"),
            body=form_body([param[str | None]("FriendlyName", friendly_name)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010Account],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_account(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010Account, RawError]:
        """Fetch the account specified by the provided Account Sid

        Args:
            sid: The Account Sid that uniquely identifies the account to fetch
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{Sid}.json"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010Account],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_account(
        self,
        *,
        friendly_name: str | None = None,
        status: AccountEnumStatusOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListAccountResponse, RawError]:
        """Retrieves a collection of Accounts belonging to the account used to make the request

        Args:
            friendly_name: Only return the Account resources with friendly names that exactly match this name.
            status: Only return Account resources with the given status. Can be ``closed``, ``suspended`` or ``active``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts.json"),
            query_params=[
                param[str | None]("FriendlyName", friendly_name),
                param[AccountEnumStatusOrStr | None]("Status", status),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListAccountResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_account(
        self,
        sid: str,
        *,
        friendly_name: str | None = None,
        status: AccountEnumStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010Account, RawError]:
        """Modify the properties of a given Account

        Args:
            sid: The Account Sid that uniquely identifies the account to update
            friendly_name: Update the human-readable description of this Account
            status: The status of this account. Usually ``active``, but can be ``suspended`` or ``closed``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{Sid}.json"),
            path_params=[param[str]("Sid", sid)],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[AccountEnumStatusOrStr | None]("Status", status),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010Account],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
