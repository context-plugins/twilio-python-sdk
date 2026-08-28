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
from ..models.list_item_assignment_response import ListItemAssignmentResponse
from ..models.numbers_v2_regulatory_compliance_bundle_item_assignment import (
    NumbersV2RegulatoryComplianceBundleItemAssignment,
)
from ..server.server import Server


class NumbersV2ItemAssignment:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NumbersV2ItemAssignmentWithRawResponse(client, server, auth)

    def create_item_assignment(
        self, bundle_sid: str, object_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV2RegulatoryComplianceBundleItemAssignment:
        """Create a new Assigned Item.

        Args:
            bundle_sid: The unique string that we created to identify the Bundle resource.
            object_sid: The SID of an object bag that holds information of the different items.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_item_assignment(
            bundle_sid, object_sid, request_options=request_options
        ).unwrap()

    def delete_item_assignment(
        self, bundle_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Remove an Assignment Item Instance.

        Args:
            bundle_sid: The unique string that we created to identify the Bundle resource.
            sid: The unique string that we created to identify the Identity resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_item_assignment(bundle_sid, sid, request_options=request_options).unwrap()

    def fetch_item_assignment(
        self, bundle_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV2RegulatoryComplianceBundleItemAssignment:
        """Fetch specific Assigned Item Instance.

        Args:
            bundle_sid: The unique string that we created to identify the Bundle resource.
            sid: The unique string that we created to identify the Identity resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_item_assignment(bundle_sid, sid, request_options=request_options).unwrap()

    def list_item_assignment(
        self,
        bundle_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListItemAssignmentResponse:
        """Retrieve a list of all Assigned Items for an account.

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
        return self._with_raw_response.list_item_assignment(
            bundle_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> NumbersV2ItemAssignmentWithRawResponse:
        return self._with_raw_response


class AsyncNumbersV2ItemAssignment:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNumbersV2ItemAssignmentWithRawResponse(client, server, auth)

    async def create_item_assignment(
        self, bundle_sid: str, object_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV2RegulatoryComplianceBundleItemAssignment:
        """Create a new Assigned Item.

        Args:
            bundle_sid: The unique string that we created to identify the Bundle resource.
            object_sid: The SID of an object bag that holds information of the different items.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_item_assignment(
                bundle_sid, object_sid, request_options=request_options
            )
        ).unwrap()

    async def delete_item_assignment(
        self, bundle_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Remove an Assignment Item Instance.

        Args:
            bundle_sid: The unique string that we created to identify the Bundle resource.
            sid: The unique string that we created to identify the Identity resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_item_assignment(bundle_sid, sid, request_options=request_options)
        ).unwrap()

    async def fetch_item_assignment(
        self, bundle_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV2RegulatoryComplianceBundleItemAssignment:
        """Fetch specific Assigned Item Instance.

        Args:
            bundle_sid: The unique string that we created to identify the Bundle resource.
            sid: The unique string that we created to identify the Identity resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_item_assignment(bundle_sid, sid, request_options=request_options)
        ).unwrap()

    async def list_item_assignment(
        self,
        bundle_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListItemAssignmentResponse:
        """Retrieve a list of all Assigned Items for an account.

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
            await self._with_raw_response.list_item_assignment(
                bundle_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncNumbersV2ItemAssignmentWithRawResponse:
        return self._with_raw_response


class NumbersV2ItemAssignmentWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_item_assignment(
        self, bundle_sid: str, object_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV2RegulatoryComplianceBundleItemAssignment, RawError]:
        """Create a new Assigned Item.

        Args:
            bundle_sid: The unique string that we created to identify the Bundle resource.
            object_sid: The SID of an object bag that holds information of the different items.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v2/RegulatoryCompliance/Bundles/{BundleSid}/ItemAssignments"),
            path_params=[param[str]("BundleSid", bundle_sid)],
            body=form_body([param[str]("ObjectSid", object_sid)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2RegulatoryComplianceBundleItemAssignment],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_item_assignment(
        self, bundle_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Remove an Assignment Item Instance.

        Args:
            bundle_sid: The unique string that we created to identify the Bundle resource.
            sid: The unique string that we created to identify the Identity resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default5("/v2/RegulatoryCompliance/Bundles/{BundleSid}/ItemAssignments/{Sid}"),
            path_params=[param[str]("BundleSid", bundle_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_item_assignment(
        self, bundle_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV2RegulatoryComplianceBundleItemAssignment, RawError]:
        """Fetch specific Assigned Item Instance.

        Args:
            bundle_sid: The unique string that we created to identify the Bundle resource.
            sid: The unique string that we created to identify the Identity resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/RegulatoryCompliance/Bundles/{BundleSid}/ItemAssignments/{Sid}"),
            path_params=[param[str]("BundleSid", bundle_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2RegulatoryComplianceBundleItemAssignment],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_item_assignment(
        self,
        bundle_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListItemAssignmentResponse, RawError]:
        """Retrieve a list of all Assigned Items for an account.

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
            url_template=self._server.default5("/v2/RegulatoryCompliance/Bundles/{BundleSid}/ItemAssignments"),
            path_params=[param[str]("BundleSid", bundle_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListItemAssignmentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncNumbersV2ItemAssignmentWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_item_assignment(
        self, bundle_sid: str, object_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV2RegulatoryComplianceBundleItemAssignment, RawError]:
        """Create a new Assigned Item.

        Args:
            bundle_sid: The unique string that we created to identify the Bundle resource.
            object_sid: The SID of an object bag that holds information of the different items.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v2/RegulatoryCompliance/Bundles/{BundleSid}/ItemAssignments"),
            path_params=[param[str]("BundleSid", bundle_sid)],
            body=form_body([param[str]("ObjectSid", object_sid)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2RegulatoryComplianceBundleItemAssignment],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_item_assignment(
        self, bundle_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Remove an Assignment Item Instance.

        Args:
            bundle_sid: The unique string that we created to identify the Bundle resource.
            sid: The unique string that we created to identify the Identity resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default5("/v2/RegulatoryCompliance/Bundles/{BundleSid}/ItemAssignments/{Sid}"),
            path_params=[param[str]("BundleSid", bundle_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_item_assignment(
        self, bundle_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV2RegulatoryComplianceBundleItemAssignment, RawError]:
        """Fetch specific Assigned Item Instance.

        Args:
            bundle_sid: The unique string that we created to identify the Bundle resource.
            sid: The unique string that we created to identify the Identity resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/RegulatoryCompliance/Bundles/{BundleSid}/ItemAssignments/{Sid}"),
            path_params=[param[str]("BundleSid", bundle_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2RegulatoryComplianceBundleItemAssignment],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_item_assignment(
        self,
        bundle_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListItemAssignmentResponse, RawError]:
        """Retrieve a list of all Assigned Items for an account.

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
            url_template=self._server.default5("/v2/RegulatoryCompliance/Bundles/{BundleSid}/ItemAssignments"),
            path_params=[param[str]("BundleSid", bundle_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListItemAssignmentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
