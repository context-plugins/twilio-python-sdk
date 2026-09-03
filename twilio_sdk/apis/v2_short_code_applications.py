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
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.create_short_code_application_request import (
    CreateShortCodeApplicationRequest,
    CreateShortCodeApplicationRequestDict,
)
from ..models.create_short_code_application_response import CreateShortCodeApplicationResponse
from ..models.short_code_application import ShortCodeApplication
from ..models.short_code_application_response_page import ShortCodeApplicationResponsePage
from ..server.server import Server


class V2ShortCodeApplications:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = V2ShortCodeApplicationsWithRawResponse(client, server, auth)

    def create_short_code_application(
        self,
        body: CreateShortCodeApplicationRequest | CreateShortCodeApplicationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateShortCodeApplicationResponse:
        """Create a new short code application for an account

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Response schema for creating a Short Code Application.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_short_code_application(body, request_options=request_options).unwrap()

    def fetch_short_code_application(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ShortCodeApplication:
        """Fetch a specific Short Code Application instance.

        Args:
            sid: The unique string that identifies the Short Code Application resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Response schema for a single Short Code Application instance.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_short_code_application(sid, request_options=request_options).unwrap()

    def list_short_code_applications(
        self,
        *,
        account_sid: str | None = None,
        iso_country: str | None = None,
        status: str | None = None,
        friendly_name: str | None = None,
        sid: str | None = None,
        page_size: int | None = None,
        page: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ShortCodeApplicationResponsePage:
        """list of all short code applications for an account

        Args:
            account_sid: The Account SID to filter by.
            iso_country: The ISO country to filter by.
            status: The application status to filter by.
            friendly_name: The friendly name to filter by.
            sid: The application SID to filter by.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The current page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Response schema for listing Short Code Applications.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_short_code_applications(
            account_sid=account_sid,
            iso_country=iso_country,
            status=status,
            friendly_name=friendly_name,
            sid=sid,
            page_size=page_size,
            page=page,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> V2ShortCodeApplicationsWithRawResponse:
        return self._with_raw_response


class AsyncV2ShortCodeApplications:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncV2ShortCodeApplicationsWithRawResponse(client, server, auth)

    async def create_short_code_application(
        self,
        body: CreateShortCodeApplicationRequest | CreateShortCodeApplicationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateShortCodeApplicationResponse:
        """Create a new short code application for an account

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Response schema for creating a Short Code Application.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_short_code_application(body, request_options=request_options)
        ).unwrap()

    async def fetch_short_code_application(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ShortCodeApplication:
        """Fetch a specific Short Code Application instance.

        Args:
            sid: The unique string that identifies the Short Code Application resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Response schema for a single Short Code Application instance.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_short_code_application(sid, request_options=request_options)
        ).unwrap()

    async def list_short_code_applications(
        self,
        *,
        account_sid: str | None = None,
        iso_country: str | None = None,
        status: str | None = None,
        friendly_name: str | None = None,
        sid: str | None = None,
        page_size: int | None = None,
        page: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ShortCodeApplicationResponsePage:
        """list of all short code applications for an account

        Args:
            account_sid: The Account SID to filter by.
            iso_country: The ISO country to filter by.
            status: The application status to filter by.
            friendly_name: The friendly name to filter by.
            sid: The application SID to filter by.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The current page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Response schema for listing Short Code Applications.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_short_code_applications(
                account_sid=account_sid,
                iso_country=iso_country,
                status=status,
                friendly_name=friendly_name,
                sid=sid,
                page_size=page_size,
                page=page,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncV2ShortCodeApplicationsWithRawResponse:
        return self._with_raw_response


class V2ShortCodeApplicationsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_short_code_application(
        self,
        body: CreateShortCodeApplicationRequest | CreateShortCodeApplicationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateShortCodeApplicationResponse, RawError]:
        """Create a new short code application for an account

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v2/ShortCodes/Applications"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateShortCodeApplicationRequest | CreateShortCodeApplicationRequestDict](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[CreateShortCodeApplicationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_short_code_application(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ShortCodeApplication, RawError]:
        """Fetch a specific Short Code Application instance.

        Args:
            sid: The unique string that identifies the Short Code Application resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/ShortCodes/Applications/{sid}"),
            path_params=[param[str]("sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ShortCodeApplication],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_short_code_applications(
        self,
        *,
        account_sid: str | None = None,
        iso_country: str | None = None,
        status: str | None = None,
        friendly_name: str | None = None,
        sid: str | None = None,
        page_size: int | None = None,
        page: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ShortCodeApplicationResponsePage, RawError]:
        """list of all short code applications for an account

        Args:
            account_sid: The Account SID to filter by.
            iso_country: The ISO country to filter by.
            status: The application status to filter by.
            friendly_name: The friendly name to filter by.
            sid: The application SID to filter by.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The current page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/ShortCodes/Applications"),
            query_params=[
                param[str | None]("AccountSid", account_sid),
                param[str | None]("IsoCountry", iso_country),
                param[str | None]("Status", status),
                param[str | None]("FriendlyName", friendly_name),
                param[str | None]("Sid", sid),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ShortCodeApplicationResponsePage],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncV2ShortCodeApplicationsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_short_code_application(
        self,
        body: CreateShortCodeApplicationRequest | CreateShortCodeApplicationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateShortCodeApplicationResponse, RawError]:
        """Create a new short code application for an account

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v2/ShortCodes/Applications"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateShortCodeApplicationRequest | CreateShortCodeApplicationRequestDict](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[CreateShortCodeApplicationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_short_code_application(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ShortCodeApplication, RawError]:
        """Fetch a specific Short Code Application instance.

        Args:
            sid: The unique string that identifies the Short Code Application resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/ShortCodes/Applications/{sid}"),
            path_params=[param[str]("sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ShortCodeApplication],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_short_code_applications(
        self,
        *,
        account_sid: str | None = None,
        iso_country: str | None = None,
        status: str | None = None,
        friendly_name: str | None = None,
        sid: str | None = None,
        page_size: int | None = None,
        page: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ShortCodeApplicationResponsePage, RawError]:
        """list of all short code applications for an account

        Args:
            account_sid: The Account SID to filter by.
            iso_country: The ISO country to filter by.
            status: The application status to filter by.
            friendly_name: The friendly name to filter by.
            sid: The application SID to filter by.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The current page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/ShortCodes/Applications"),
            query_params=[
                param[str | None]("AccountSid", account_sid),
                param[str | None]("IsoCountry", iso_country),
                param[str | None]("Status", status),
                param[str | None]("FriendlyName", friendly_name),
                param[str | None]("Sid", sid),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ShortCodeApplicationResponsePage],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
