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
from ..models.api_v2010_account_connect_app import ApiV2010AccountConnectApp
from ..models.enums.connect_app_enum_permission import ConnectAppEnumPermissionOrStr
from ..models.enums.deauthorize_callback_method1 import DeauthorizeCallbackMethod1OrStr
from ..models.list_connect_app_response import ListConnectAppResponse
from ..server.server import Server


class Api20100401ConnectApp:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401ConnectAppWithRawResponse(client, server, auth)

    def delete_connect_app(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete an instance of a connect-app

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                ConnectApp resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the ConnectApp resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_connect_app(account_sid, sid, request_options=request_options).unwrap()

    def fetch_connect_app(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountConnectApp:
        """Fetch an instance of a connect-app

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                ConnectApp resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the ConnectApp resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_connect_app(account_sid, sid, request_options=request_options).unwrap()

    def list_connect_app(
        self,
        account_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListConnectAppResponse:
        """Retrieve a list of connect-apps belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                ConnectApp resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_connect_app(
            account_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    def update_connect_app(
        self,
        account_sid: str,
        sid: str,
        *,
        authorize_redirect_url: str | None = None,
        company_name: str | None = None,
        deauthorize_callback_method: DeauthorizeCallbackMethod1OrStr | None = None,
        deauthorize_callback_url: str | None = None,
        description: str | None = None,
        friendly_name: str | None = None,
        homepage_url: str | None = None,
        permissions: list[ConnectAppEnumPermissionOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountConnectApp:
        """Update a connect-app with the specified parameters

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                ConnectApp resources to update.
            sid: The Twilio-provided string that uniquely identifies the ConnectApp resource to update.
            authorize_redirect_url: The URL to redirect the user to after we authenticate the user and obtain
                authorization to access the Connect App.
            company_name: The company name to set for the Connect App.
            deauthorize_callback_method: The HTTP method to use when calling ``deauthorize_callback_url``.
            deauthorize_callback_url: The URL to call using the ``deauthorize_callback_method`` to de-authorize the
                Connect App.
            description: A description of the Connect App.
            friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters
                long.
            homepage_url: A public URL where users can obtain more information about this Connect App.
            permissions: A comma-separated list of the permissions you will request from the users of this ConnectApp.
                Can include: ``get-all`` and ``post-all``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_connect_app(
            account_sid,
            sid,
            authorize_redirect_url=authorize_redirect_url,
            company_name=company_name,
            deauthorize_callback_method=deauthorize_callback_method,
            deauthorize_callback_url=deauthorize_callback_url,
            description=description,
            friendly_name=friendly_name,
            homepage_url=homepage_url,
            permissions=permissions,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401ConnectAppWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401ConnectApp:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401ConnectAppWithRawResponse(client, server, auth)

    async def delete_connect_app(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete an instance of a connect-app

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                ConnectApp resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the ConnectApp resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_connect_app(account_sid, sid, request_options=request_options)
        ).unwrap()

    async def fetch_connect_app(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountConnectApp:
        """Fetch an instance of a connect-app

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                ConnectApp resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the ConnectApp resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_connect_app(account_sid, sid, request_options=request_options)
        ).unwrap()

    async def list_connect_app(
        self,
        account_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListConnectAppResponse:
        """Retrieve a list of connect-apps belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                ConnectApp resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_connect_app(
                account_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    async def update_connect_app(
        self,
        account_sid: str,
        sid: str,
        *,
        authorize_redirect_url: str | None = None,
        company_name: str | None = None,
        deauthorize_callback_method: DeauthorizeCallbackMethod1OrStr | None = None,
        deauthorize_callback_url: str | None = None,
        description: str | None = None,
        friendly_name: str | None = None,
        homepage_url: str | None = None,
        permissions: list[ConnectAppEnumPermissionOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountConnectApp:
        """Update a connect-app with the specified parameters

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                ConnectApp resources to update.
            sid: The Twilio-provided string that uniquely identifies the ConnectApp resource to update.
            authorize_redirect_url: The URL to redirect the user to after we authenticate the user and obtain
                authorization to access the Connect App.
            company_name: The company name to set for the Connect App.
            deauthorize_callback_method: The HTTP method to use when calling ``deauthorize_callback_url``.
            deauthorize_callback_url: The URL to call using the ``deauthorize_callback_method`` to de-authorize the
                Connect App.
            description: A description of the Connect App.
            friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters
                long.
            homepage_url: A public URL where users can obtain more information about this Connect App.
            permissions: A comma-separated list of the permissions you will request from the users of this ConnectApp.
                Can include: ``get-all`` and ``post-all``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_connect_app(
                account_sid,
                sid,
                authorize_redirect_url=authorize_redirect_url,
                company_name=company_name,
                deauthorize_callback_method=deauthorize_callback_method,
                deauthorize_callback_url=deauthorize_callback_url,
                description=description,
                friendly_name=friendly_name,
                homepage_url=homepage_url,
                permissions=permissions,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401ConnectAppWithRawResponse:
        return self._with_raw_response


class Api20100401ConnectAppWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_connect_app(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete an instance of a connect-app

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                ConnectApp resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the ConnectApp resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/ConnectApps/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_connect_app(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountConnectApp, RawError]:
        """Fetch an instance of a connect-app

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                ConnectApp resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the ConnectApp resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/ConnectApps/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountConnectApp],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_connect_app(
        self,
        account_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListConnectAppResponse, RawError]:
        """Retrieve a list of connect-apps belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                ConnectApp resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/ConnectApps.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListConnectAppResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_connect_app(
        self,
        account_sid: str,
        sid: str,
        *,
        authorize_redirect_url: str | None = None,
        company_name: str | None = None,
        deauthorize_callback_method: DeauthorizeCallbackMethod1OrStr | None = None,
        deauthorize_callback_url: str | None = None,
        description: str | None = None,
        friendly_name: str | None = None,
        homepage_url: str | None = None,
        permissions: list[ConnectAppEnumPermissionOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountConnectApp, RawError]:
        """Update a connect-app with the specified parameters

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                ConnectApp resources to update.
            sid: The Twilio-provided string that uniquely identifies the ConnectApp resource to update.
            authorize_redirect_url: The URL to redirect the user to after we authenticate the user and obtain
                authorization to access the Connect App.
            company_name: The company name to set for the Connect App.
            deauthorize_callback_method: The HTTP method to use when calling ``deauthorize_callback_url``.
            deauthorize_callback_url: The URL to call using the ``deauthorize_callback_method`` to de-authorize the
                Connect App.
            description: A description of the Connect App.
            friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters
                long.
            homepage_url: A public URL where users can obtain more information about this Connect App.
            permissions: A comma-separated list of the permissions you will request from the users of this ConnectApp.
                Can include: ``get-all`` and ``post-all``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/ConnectApps/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("AuthorizeRedirectUrl", authorize_redirect_url),
                    param[str | None]("CompanyName", company_name),
                    param[DeauthorizeCallbackMethod1OrStr | None](
                        "DeauthorizeCallbackMethod", deauthorize_callback_method
                    ),
                    param[str | None]("DeauthorizeCallbackUrl", deauthorize_callback_url),
                    param[str | None]("Description", description),
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("HomepageUrl", homepage_url),
                    param[list[ConnectAppEnumPermissionOrStr] | None]("Permissions", permissions),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountConnectApp],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401ConnectAppWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_connect_app(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete an instance of a connect-app

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                ConnectApp resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the ConnectApp resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/ConnectApps/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_connect_app(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountConnectApp, RawError]:
        """Fetch an instance of a connect-app

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                ConnectApp resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the ConnectApp resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/ConnectApps/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountConnectApp],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_connect_app(
        self,
        account_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListConnectAppResponse, RawError]:
        """Retrieve a list of connect-apps belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                ConnectApp resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/ConnectApps.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListConnectAppResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_connect_app(
        self,
        account_sid: str,
        sid: str,
        *,
        authorize_redirect_url: str | None = None,
        company_name: str | None = None,
        deauthorize_callback_method: DeauthorizeCallbackMethod1OrStr | None = None,
        deauthorize_callback_url: str | None = None,
        description: str | None = None,
        friendly_name: str | None = None,
        homepage_url: str | None = None,
        permissions: list[ConnectAppEnumPermissionOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountConnectApp, RawError]:
        """Update a connect-app with the specified parameters

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                ConnectApp resources to update.
            sid: The Twilio-provided string that uniquely identifies the ConnectApp resource to update.
            authorize_redirect_url: The URL to redirect the user to after we authenticate the user and obtain
                authorization to access the Connect App.
            company_name: The company name to set for the Connect App.
            deauthorize_callback_method: The HTTP method to use when calling ``deauthorize_callback_url``.
            deauthorize_callback_url: The URL to call using the ``deauthorize_callback_method`` to de-authorize the
                Connect App.
            description: A description of the Connect App.
            friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters
                long.
            homepage_url: A public URL where users can obtain more information about this Connect App.
            permissions: A comma-separated list of the permissions you will request from the users of this ConnectApp.
                Can include: ``get-all`` and ``post-all``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/ConnectApps/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("AuthorizeRedirectUrl", authorize_redirect_url),
                    param[str | None]("CompanyName", company_name),
                    param[DeauthorizeCallbackMethod1OrStr | None](
                        "DeauthorizeCallbackMethod", deauthorize_callback_method
                    ),
                    param[str | None]("DeauthorizeCallbackUrl", deauthorize_callback_url),
                    param[str | None]("Description", description),
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("HomepageUrl", homepage_url),
                    param[list[ConnectAppEnumPermissionOrStr] | None]("Permissions", permissions),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountConnectApp],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
