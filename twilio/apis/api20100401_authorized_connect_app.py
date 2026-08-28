from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.api_v2010_account_authorized_connect_app import ApiV2010AccountAuthorizedConnectApp
from ..models.list_authorized_connect_app_response import ListAuthorizedConnectAppResponse
from ..server.server import Server


class Api20100401AuthorizedConnectApp:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401AuthorizedConnectAppWithRawResponse(client, server, auth)

    def fetch_authorized_connect_app(
        self, account_sid: str, connect_app_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountAuthorizedConnectApp:
        """Fetch an instance of an authorized-connect-app

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                AuthorizedConnectApp resource to fetch.
            connect_app_sid: The SID of the Connect App to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_authorized_connect_app(
            account_sid, connect_app_sid, request_options=request_options
        ).unwrap()

    def list_authorized_connect_app(
        self,
        account_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListAuthorizedConnectAppResponse:
        """Retrieve a list of authorized-connect-apps belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                AuthorizedConnectApp resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_authorized_connect_app(
            account_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401AuthorizedConnectAppWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401AuthorizedConnectApp:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401AuthorizedConnectAppWithRawResponse(client, server, auth)

    async def fetch_authorized_connect_app(
        self, account_sid: str, connect_app_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountAuthorizedConnectApp:
        """Fetch an instance of an authorized-connect-app

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                AuthorizedConnectApp resource to fetch.
            connect_app_sid: The SID of the Connect App to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_authorized_connect_app(
                account_sid, connect_app_sid, request_options=request_options
            )
        ).unwrap()

    async def list_authorized_connect_app(
        self,
        account_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListAuthorizedConnectAppResponse:
        """Retrieve a list of authorized-connect-apps belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                AuthorizedConnectApp resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_authorized_connect_app(
                account_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401AuthorizedConnectAppWithRawResponse:
        return self._with_raw_response


class Api20100401AuthorizedConnectAppWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_authorized_connect_app(
        self, account_sid: str, connect_app_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountAuthorizedConnectApp, RawError]:
        """Fetch an instance of an authorized-connect-app

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                AuthorizedConnectApp resource to fetch.
            connect_app_sid: The SID of the Connect App to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/AuthorizedConnectApps/{ConnectAppSid}.json"
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("ConnectAppSid", connect_app_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountAuthorizedConnectApp],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_authorized_connect_app(
        self,
        account_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListAuthorizedConnectAppResponse, RawError]:
        """Retrieve a list of authorized-connect-apps belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                AuthorizedConnectApp resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/AuthorizedConnectApps.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListAuthorizedConnectAppResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401AuthorizedConnectAppWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_authorized_connect_app(
        self, account_sid: str, connect_app_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountAuthorizedConnectApp, RawError]:
        """Fetch an instance of an authorized-connect-app

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                AuthorizedConnectApp resource to fetch.
            connect_app_sid: The SID of the Connect App to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/AuthorizedConnectApps/{ConnectAppSid}.json"
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("ConnectAppSid", connect_app_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountAuthorizedConnectApp],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_authorized_connect_app(
        self,
        account_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListAuthorizedConnectAppResponse, RawError]:
        """Retrieve a list of authorized-connect-apps belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                AuthorizedConnectApp resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/AuthorizedConnectApps.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListAuthorizedConnectAppResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
