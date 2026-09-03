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
from ..models.list_end_user_type_response import ListEndUserTypeResponse
from ..models.numbers_v2_regulatory_compliance_end_user_type import NumbersV2RegulatoryComplianceEndUserType
from ..server.server import Server


class NumbersV2EndUserType:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NumbersV2EndUserTypeWithRawResponse(client, server, auth)

    def fetch_end_user_type(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV2RegulatoryComplianceEndUserType:
        """Fetch a specific End-User Type Instance.

        Args:
            sid: The unique string that identifies the End-User Type resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_end_user_type(sid, request_options=request_options).unwrap()

    def list_end_user_type(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListEndUserTypeResponse:
        """Retrieve a list of all End-User Types.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_end_user_type(
            page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> NumbersV2EndUserTypeWithRawResponse:
        return self._with_raw_response


class AsyncNumbersV2EndUserType:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNumbersV2EndUserTypeWithRawResponse(client, server, auth)

    async def fetch_end_user_type(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV2RegulatoryComplianceEndUserType:
        """Fetch a specific End-User Type Instance.

        Args:
            sid: The unique string that identifies the End-User Type resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_end_user_type(sid, request_options=request_options)).unwrap()

    async def list_end_user_type(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListEndUserTypeResponse:
        """Retrieve a list of all End-User Types.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_end_user_type(
                page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncNumbersV2EndUserTypeWithRawResponse:
        return self._with_raw_response


class NumbersV2EndUserTypeWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_end_user_type(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV2RegulatoryComplianceEndUserType, RawError]:
        """Fetch a specific End-User Type Instance.

        Args:
            sid: The unique string that identifies the End-User Type resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/RegulatoryCompliance/EndUserTypes/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2RegulatoryComplianceEndUserType],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_end_user_type(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListEndUserTypeResponse, RawError]:
        """Retrieve a list of all End-User Types.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/RegulatoryCompliance/EndUserTypes"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListEndUserTypeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncNumbersV2EndUserTypeWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_end_user_type(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV2RegulatoryComplianceEndUserType, RawError]:
        """Fetch a specific End-User Type Instance.

        Args:
            sid: The unique string that identifies the End-User Type resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/RegulatoryCompliance/EndUserTypes/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2RegulatoryComplianceEndUserType],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_end_user_type(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListEndUserTypeResponse, RawError]:
        """Retrieve a list of all End-User Types.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/RegulatoryCompliance/EndUserTypes"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListEndUserTypeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
