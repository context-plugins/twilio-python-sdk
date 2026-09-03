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
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.list_bundle_copy_response import ListBundleCopyResponse
from ..models.numbers_v2_regulatory_compliance_bundle_bundle_copy import NumbersV2RegulatoryComplianceBundleBundleCopy
from ..server.server import Server


class NumbersV2BundleCopy:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NumbersV2BundleCopyWithRawResponse(client, server, auth)

    def create_bundle_copy(
        self, bundle_sid: str, *, friendly_name: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV2RegulatoryComplianceBundleBundleCopy:
        """Creates a new copy of a Bundle. It will internally create copies of all the bundle items (identities and
        documents) of the original bundle

        Args:
            bundle_sid: The unique string that identifies the Bundle to be copied.
            friendly_name: The string that you assigned to describe the copied bundle.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_bundle_copy(
            bundle_sid, friendly_name=friendly_name, request_options=request_options
        ).unwrap()

    def list_bundle_copy(
        self,
        bundle_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListBundleCopyResponse:
        """Retrieve a list of all Bundles Copies for a Bundle.

        Args:
            bundle_sid: The unique string that we created to identify the Bundle resource.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_bundle_copy(
            bundle_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> NumbersV2BundleCopyWithRawResponse:
        return self._with_raw_response


class AsyncNumbersV2BundleCopy:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNumbersV2BundleCopyWithRawResponse(client, server, auth)

    async def create_bundle_copy(
        self, bundle_sid: str, *, friendly_name: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV2RegulatoryComplianceBundleBundleCopy:
        """Creates a new copy of a Bundle. It will internally create copies of all the bundle items (identities and
        documents) of the original bundle

        Args:
            bundle_sid: The unique string that identifies the Bundle to be copied.
            friendly_name: The string that you assigned to describe the copied bundle.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_bundle_copy(
                bundle_sid, friendly_name=friendly_name, request_options=request_options
            )
        ).unwrap()

    async def list_bundle_copy(
        self,
        bundle_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListBundleCopyResponse:
        """Retrieve a list of all Bundles Copies for a Bundle.

        Args:
            bundle_sid: The unique string that we created to identify the Bundle resource.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_bundle_copy(
                bundle_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncNumbersV2BundleCopyWithRawResponse:
        return self._with_raw_response


class NumbersV2BundleCopyWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_bundle_copy(
        self, bundle_sid: str, *, friendly_name: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV2RegulatoryComplianceBundleBundleCopy, RawError]:
        """Creates a new copy of a Bundle. It will internally create copies of all the bundle items (identities and
        documents) of the original bundle

        Args:
            bundle_sid: The unique string that identifies the Bundle to be copied.
            friendly_name: The string that you assigned to describe the copied bundle.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v2/RegulatoryCompliance/Bundles/{BundleSid}/Copies"),
            path_params=[param[str]("BundleSid", bundle_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str | None]("FriendlyName", friendly_name)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2RegulatoryComplianceBundleBundleCopy],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_bundle_copy(
        self,
        bundle_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListBundleCopyResponse, RawError]:
        """Retrieve a list of all Bundles Copies for a Bundle.

        Args:
            bundle_sid: The unique string that we created to identify the Bundle resource.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/RegulatoryCompliance/Bundles/{BundleSid}/Copies"),
            path_params=[param[str]("BundleSid", bundle_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListBundleCopyResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncNumbersV2BundleCopyWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_bundle_copy(
        self, bundle_sid: str, *, friendly_name: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV2RegulatoryComplianceBundleBundleCopy, RawError]:
        """Creates a new copy of a Bundle. It will internally create copies of all the bundle items (identities and
        documents) of the original bundle

        Args:
            bundle_sid: The unique string that identifies the Bundle to be copied.
            friendly_name: The string that you assigned to describe the copied bundle.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v2/RegulatoryCompliance/Bundles/{BundleSid}/Copies"),
            path_params=[param[str]("BundleSid", bundle_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str | None]("FriendlyName", friendly_name)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2RegulatoryComplianceBundleBundleCopy],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_bundle_copy(
        self,
        bundle_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListBundleCopyResponse, RawError]:
        """Retrieve a list of all Bundles Copies for a Bundle.

        Args:
            bundle_sid: The unique string that we created to identify the Bundle resource.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/RegulatoryCompliance/Bundles/{BundleSid}/Copies"),
            path_params=[param[str]("BundleSid", bundle_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListBundleCopyResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
