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
from ..models.list_flow_revision_response import ListFlowRevisionResponse
from ..models.studio_v2_flow_flow_revision import StudioV2FlowFlowRevision
from ..server.server import Server


class StudioV2FlowRevision:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = StudioV2FlowRevisionWithRawResponse(client, server, auth)

    def fetch_flow_revision(
        self, sid: str, revision: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> StudioV2FlowFlowRevision:
        """Retrieve a specific Flow revision.

        Args:
            sid: The SID of the Flow resource to fetch.
            revision: Specific Revision number or can be ``LatestPublished`` and ``LatestRevision``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_flow_revision(sid, revision, request_options=request_options).unwrap()

    def list_flow_revision(
        self,
        sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListFlowRevisionResponse:
        """Retrieve a list of all Flows revisions.

        Args:
            sid: The SID of the Flow resource to fetch.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_flow_revision(
            sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> StudioV2FlowRevisionWithRawResponse:
        return self._with_raw_response


class AsyncStudioV2FlowRevision:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncStudioV2FlowRevisionWithRawResponse(client, server, auth)

    async def fetch_flow_revision(
        self, sid: str, revision: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> StudioV2FlowFlowRevision:
        """Retrieve a specific Flow revision.

        Args:
            sid: The SID of the Flow resource to fetch.
            revision: Specific Revision number or can be ``LatestPublished`` and ``LatestRevision``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_flow_revision(sid, revision, request_options=request_options)
        ).unwrap()

    async def list_flow_revision(
        self,
        sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListFlowRevisionResponse:
        """Retrieve a list of all Flows revisions.

        Args:
            sid: The SID of the Flow resource to fetch.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_flow_revision(
                sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncStudioV2FlowRevisionWithRawResponse:
        return self._with_raw_response


class StudioV2FlowRevisionWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_flow_revision(
        self, sid: str, revision: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[StudioV2FlowFlowRevision, RawError]:
        """Retrieve a specific Flow revision.

        Args:
            sid: The SID of the Flow resource to fetch.
            revision: Specific Revision number or can be ``LatestPublished`` and ``LatestRevision``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default11("/v2/Flows/{Sid}/Revisions/{Revision}"),
            path_params=[param[str]("Sid", sid), param[str]("Revision", revision)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[StudioV2FlowFlowRevision],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_flow_revision(
        self,
        sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListFlowRevisionResponse, RawError]:
        """Retrieve a list of all Flows revisions.

        Args:
            sid: The SID of the Flow resource to fetch.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default11("/v2/Flows/{Sid}/Revisions"),
            path_params=[param[str]("Sid", sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListFlowRevisionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncStudioV2FlowRevisionWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_flow_revision(
        self, sid: str, revision: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[StudioV2FlowFlowRevision, RawError]:
        """Retrieve a specific Flow revision.

        Args:
            sid: The SID of the Flow resource to fetch.
            revision: Specific Revision number or can be ``LatestPublished`` and ``LatestRevision``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default11("/v2/Flows/{Sid}/Revisions/{Revision}"),
            path_params=[param[str]("Sid", sid), param[str]("Revision", revision)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[StudioV2FlowFlowRevision],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_flow_revision(
        self,
        sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListFlowRevisionResponse, RawError]:
        """Retrieve a list of all Flows revisions.

        Args:
            sid: The SID of the Flow resource to fetch.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default11("/v2/Flows/{Sid}/Revisions"),
            path_params=[param[str]("Sid", sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListFlowRevisionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
