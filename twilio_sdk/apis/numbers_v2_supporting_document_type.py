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
from ..models.list_supporting_document_type_response import ListSupportingDocumentTypeResponse
from ..models.numbers_v2_regulatory_compliance_supporting_document_type import (
    NumbersV2RegulatoryComplianceSupportingDocumentType,
)
from ..server.server import Server


class NumbersV2SupportingDocumentType:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NumbersV2SupportingDocumentTypeWithRawResponse(client, server, auth)

    def fetch_supporting_document_type(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV2RegulatoryComplianceSupportingDocumentType:
        """Fetch a specific Supporting Document Type Instance.

        Args:
            sid: The unique string that identifies the Supporting Document Type resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_supporting_document_type(sid, request_options=request_options).unwrap()

    def list_supporting_document_type(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSupportingDocumentTypeResponse:
        """Retrieve a list of all Supporting Document Types.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_supporting_document_type(
            page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> NumbersV2SupportingDocumentTypeWithRawResponse:
        return self._with_raw_response


class AsyncNumbersV2SupportingDocumentType:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNumbersV2SupportingDocumentTypeWithRawResponse(client, server, auth)

    async def fetch_supporting_document_type(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV2RegulatoryComplianceSupportingDocumentType:
        """Fetch a specific Supporting Document Type Instance.

        Args:
            sid: The unique string that identifies the Supporting Document Type resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_supporting_document_type(sid, request_options=request_options)
        ).unwrap()

    async def list_supporting_document_type(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSupportingDocumentTypeResponse:
        """Retrieve a list of all Supporting Document Types.

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
            await self._with_raw_response.list_supporting_document_type(
                page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncNumbersV2SupportingDocumentTypeWithRawResponse:
        return self._with_raw_response


class NumbersV2SupportingDocumentTypeWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_supporting_document_type(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV2RegulatoryComplianceSupportingDocumentType, RawError]:
        """Fetch a specific Supporting Document Type Instance.

        Args:
            sid: The unique string that identifies the Supporting Document Type resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/RegulatoryCompliance/SupportingDocumentTypes/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2RegulatoryComplianceSupportingDocumentType],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_supporting_document_type(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSupportingDocumentTypeResponse, RawError]:
        """Retrieve a list of all Supporting Document Types.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/RegulatoryCompliance/SupportingDocumentTypes"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListSupportingDocumentTypeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncNumbersV2SupportingDocumentTypeWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_supporting_document_type(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV2RegulatoryComplianceSupportingDocumentType, RawError]:
        """Fetch a specific Supporting Document Type Instance.

        Args:
            sid: The unique string that identifies the Supporting Document Type resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/RegulatoryCompliance/SupportingDocumentTypes/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2RegulatoryComplianceSupportingDocumentType],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_supporting_document_type(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSupportingDocumentTypeResponse, RawError]:
        """Retrieve a list of all Supporting Document Types.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/RegulatoryCompliance/SupportingDocumentTypes"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListSupportingDocumentTypeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
