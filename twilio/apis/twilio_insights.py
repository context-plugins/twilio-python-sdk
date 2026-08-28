from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_body,
    json_decoder,
    param,
)
from ..errors.create_query_results_error import CreateQueryResultsErrorBody, create_query_results_error_mapper
from ..errors.fetch_metadata_error import FetchMetadataErrorBody, fetch_metadata_error_mapper
from ..errors.fetch_query_results_error import FetchQueryResultsErrorBody, fetch_query_results_error_mapper
from ..models.insights_metadata_response import InsightsMetadataResponse
from ..models.insights_query_request import InsightsQueryRequest, InsightsQueryRequestDict
from ..models.insights_query_response import InsightsQueryResponse
from ..server.server import Server


class TwilioInsights:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TwilioInsightsWithRawResponse(client, server, auth)

    def create_query_results(
        self,
        body: InsightsQueryRequest | InsightsQueryRequestDict,
        *,
        page_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> InsightsQueryResponse:
        """Execute a semantic query against the Conversations domain.

        Args:
            body: The request body.
            page_size: Number of items per page
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful query response

        Raises:
            ApiError: Bad request Too Many requests (rate limit exceeded for request originating from public API)
                Internal server error ``error`` is ``V3InsightsDomainsConversationsQuery400Error1 |
                V3InsightsDomainsConversationsQuery429Error1 | V3InsightsDomainsConversationsQuery500Error1 |
                RawError``."""
        return self._with_raw_response.create_query_results(
            body, page_size=page_size, request_options=request_options
        ).unwrap()

    def fetch_metadata(self, *, request_options: RequestOptionsOrDict | None = None) -> InsightsMetadataResponse:
        """Fetch Metadata for the Conversations domain.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: Bad request Too Many requests (rate limit exceeded for request originating from public API)
                Internal server error ``error`` is ``V3InsightsDomainsConversationsMetadata400Error1 |
                V3InsightsDomainsConversationsMetadata429Error1 | V3InsightsDomainsConversationsMetadata500Error1 |
                RawError``."""
        return self._with_raw_response.fetch_metadata(request_options=request_options).unwrap()

    def fetch_query_results(
        self, page_token: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> InsightsQueryResponse:
        """Send a ``GET`` request.

        Args:
            page_token: Pagination token
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful query response

        Raises:
            ApiError: Bad request Too Many requests (rate limit exceeded for request originating from public API)
                Internal server error ``error`` is ``V3InsightsDomainsConversationsQuery400Error1 |
                V3InsightsDomainsConversationsQuery429Error1 | V3InsightsDomainsConversationsQuery500Error1 |
                RawError``."""
        return self._with_raw_response.fetch_query_results(page_token, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> TwilioInsightsWithRawResponse:
        return self._with_raw_response


class AsyncTwilioInsights:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTwilioInsightsWithRawResponse(client, server, auth)

    async def create_query_results(
        self,
        body: InsightsQueryRequest | InsightsQueryRequestDict,
        *,
        page_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> InsightsQueryResponse:
        """Execute a semantic query against the Conversations domain.

        Args:
            body: The request body.
            page_size: Number of items per page
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful query response

        Raises:
            ApiError: Bad request Too Many requests (rate limit exceeded for request originating from public API)
                Internal server error ``error`` is ``V3InsightsDomainsConversationsQuery400Error1 |
                V3InsightsDomainsConversationsQuery429Error1 | V3InsightsDomainsConversationsQuery500Error1 |
                RawError``."""
        return (
            await self._with_raw_response.create_query_results(
                body, page_size=page_size, request_options=request_options
            )
        ).unwrap()

    async def fetch_metadata(self, *, request_options: RequestOptionsOrDict | None = None) -> InsightsMetadataResponse:
        """Fetch Metadata for the Conversations domain.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: Bad request Too Many requests (rate limit exceeded for request originating from public API)
                Internal server error ``error`` is ``V3InsightsDomainsConversationsMetadata400Error1 |
                V3InsightsDomainsConversationsMetadata429Error1 | V3InsightsDomainsConversationsMetadata500Error1 |
                RawError``."""
        return (await self._with_raw_response.fetch_metadata(request_options=request_options)).unwrap()

    async def fetch_query_results(
        self, page_token: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> InsightsQueryResponse:
        """Send a ``GET`` request.

        Args:
            page_token: Pagination token
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful query response

        Raises:
            ApiError: Bad request Too Many requests (rate limit exceeded for request originating from public API)
                Internal server error ``error`` is ``V3InsightsDomainsConversationsQuery400Error1 |
                V3InsightsDomainsConversationsQuery429Error1 | V3InsightsDomainsConversationsQuery500Error1 |
                RawError``."""
        return (await self._with_raw_response.fetch_query_results(page_token, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncTwilioInsightsWithRawResponse:
        return self._with_raw_response


class TwilioInsightsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_query_results(
        self,
        body: InsightsQueryRequest | InsightsQueryRequestDict,
        *,
        page_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[InsightsQueryResponse, CreateQueryResultsErrorBody]:
        """Execute a semantic query against the Conversations domain.

        Args:
            body: The request body.
            page_size: Number of items per page
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default14("/v3/InsightsDomains/Conversations/Query"),
            query_params=[param[int | None]("pageSize", page_size)],
            body=json_body[InsightsQueryRequest | InsightsQueryRequestDict](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[InsightsQueryResponse],
            error_mapper=create_query_results_error_mapper,
            request_options=request_options,
        )

    def fetch_metadata(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InsightsMetadataResponse, FetchMetadataErrorBody]:
        """Fetch Metadata for the Conversations domain.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/v3/InsightsDomains/Conversations/Metadata"),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[InsightsMetadataResponse],
            error_mapper=fetch_metadata_error_mapper,
            request_options=request_options,
        )

    def fetch_query_results(
        self, page_token: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InsightsQueryResponse, FetchQueryResultsErrorBody]:
        """Send a ``GET`` request.

        Args:
            page_token: Pagination token
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/v3/InsightsDomains/Conversations/Query"),
            query_params=[param[str]("pageToken", page_token)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[InsightsQueryResponse],
            error_mapper=fetch_query_results_error_mapper,
            request_options=request_options,
        )


class AsyncTwilioInsightsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_query_results(
        self,
        body: InsightsQueryRequest | InsightsQueryRequestDict,
        *,
        page_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[InsightsQueryResponse, CreateQueryResultsErrorBody]:
        """Execute a semantic query against the Conversations domain.

        Args:
            body: The request body.
            page_size: Number of items per page
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default14("/v3/InsightsDomains/Conversations/Query"),
            query_params=[param[int | None]("pageSize", page_size)],
            body=json_body[InsightsQueryRequest | InsightsQueryRequestDict](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[InsightsQueryResponse],
            error_mapper=create_query_results_error_mapper,
            request_options=request_options,
        )

    async def fetch_metadata(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InsightsMetadataResponse, FetchMetadataErrorBody]:
        """Fetch Metadata for the Conversations domain.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/v3/InsightsDomains/Conversations/Metadata"),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[InsightsMetadataResponse],
            error_mapper=fetch_metadata_error_mapper,
            request_options=request_options,
        )

    async def fetch_query_results(
        self, page_token: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InsightsQueryResponse, FetchQueryResultsErrorBody]:
        """Send a ``GET`` request.

        Args:
            page_token: Pagination token
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/v3/InsightsDomains/Conversations/Query"),
            query_params=[param[str]("pageToken", page_token)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[InsightsQueryResponse],
            error_mapper=fetch_query_results_error_mapper,
            request_options=request_options,
        )
