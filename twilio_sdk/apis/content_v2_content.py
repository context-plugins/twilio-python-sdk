from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    RFC3339DateTime,
    SecuredRawResponse,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.list_content_response import ListContentResponse
from ..server.server import Server


class ContentV2Content:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ContentV2ContentWithRawResponse(client, server, auth)

    def list_content2(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        sort_by_date: str | None = None,
        sort_by_content_name: str | None = None,
        date_created_after: RFC3339DateTime | None = None,
        date_created_before: RFC3339DateTime | None = None,
        content_name: str | None = None,
        content: str | None = None,
        language: list[str] | None = None,
        content_type: list[str] | None = None,
        channel_eligibility: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListContentResponse:
        """Retrieve a list of Contents belonging to the account used to make the request

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            sort_by_date: Whether to sort by ascending or descending date updated
            sort_by_content_name: Whether to sort by ascending or descending content name
            date_created_after: Filter by >=[date-time]
            date_created_before: Filter by <=[date-time]
            content_name: Filter by Regex Pattern in content name
            content: Filter by Regex Pattern in template content
            language: Filter by array of valid language(s)
            content_type: Filter by array of contentType(s)
            channel_eligibility: Filter by array of ChannelEligibility(s), where ChannelEligibility=<channel>:<status>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_content2(
            page_size=page_size,
            page=page,
            page_token=page_token,
            sort_by_date=sort_by_date,
            sort_by_content_name=sort_by_content_name,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            content_name=content_name,
            content=content,
            language=language,
            content_type=content_type,
            channel_eligibility=channel_eligibility,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> ContentV2ContentWithRawResponse:
        return self._with_raw_response


class AsyncContentV2Content:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncContentV2ContentWithRawResponse(client, server, auth)

    async def list_content2(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        sort_by_date: str | None = None,
        sort_by_content_name: str | None = None,
        date_created_after: RFC3339DateTime | None = None,
        date_created_before: RFC3339DateTime | None = None,
        content_name: str | None = None,
        content: str | None = None,
        language: list[str] | None = None,
        content_type: list[str] | None = None,
        channel_eligibility: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListContentResponse:
        """Retrieve a list of Contents belonging to the account used to make the request

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            sort_by_date: Whether to sort by ascending or descending date updated
            sort_by_content_name: Whether to sort by ascending or descending content name
            date_created_after: Filter by >=[date-time]
            date_created_before: Filter by <=[date-time]
            content_name: Filter by Regex Pattern in content name
            content: Filter by Regex Pattern in template content
            language: Filter by array of valid language(s)
            content_type: Filter by array of contentType(s)
            channel_eligibility: Filter by array of ChannelEligibility(s), where ChannelEligibility=<channel>:<status>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_content2(
                page_size=page_size,
                page=page,
                page_token=page_token,
                sort_by_date=sort_by_date,
                sort_by_content_name=sort_by_content_name,
                date_created_after=date_created_after,
                date_created_before=date_created_before,
                content_name=content_name,
                content=content,
                language=language,
                content_type=content_type,
                channel_eligibility=channel_eligibility,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncContentV2ContentWithRawResponse:
        return self._with_raw_response


class ContentV2ContentWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def list_content2(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        sort_by_date: str | None = None,
        sort_by_content_name: str | None = None,
        date_created_after: RFC3339DateTime | None = None,
        date_created_before: RFC3339DateTime | None = None,
        content_name: str | None = None,
        content: str | None = None,
        language: list[str] | None = None,
        content_type: list[str] | None = None,
        channel_eligibility: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListContentResponse, RawError]:
        """Retrieve a list of Contents belonging to the account used to make the request

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            sort_by_date: Whether to sort by ascending or descending date updated
            sort_by_content_name: Whether to sort by ascending or descending content name
            date_created_after: Filter by >=[date-time]
            date_created_before: Filter by <=[date-time]
            content_name: Filter by Regex Pattern in content name
            content: Filter by Regex Pattern in template content
            language: Filter by array of valid language(s)
            content_type: Filter by array of contentType(s)
            channel_eligibility: Filter by array of ChannelEligibility(s), where ChannelEligibility=<channel>:<status>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default2("/v2/Content"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
                param[str | None]("SortByDate", sort_by_date),
                param[str | None]("SortByContentName", sort_by_content_name),
                param[RFC3339DateTime | None]("DateCreatedAfter", date_created_after),
                param[RFC3339DateTime | None]("DateCreatedBefore", date_created_before),
                param[str | None]("ContentName", content_name),
                param[str | None]("Content", content),
                param[list[str] | None]("Language", language),
                param[list[str] | None]("ContentType", content_type),
                param[list[str] | None]("ChannelEligibility", channel_eligibility),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListContentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncContentV2ContentWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def list_content2(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        sort_by_date: str | None = None,
        sort_by_content_name: str | None = None,
        date_created_after: RFC3339DateTime | None = None,
        date_created_before: RFC3339DateTime | None = None,
        content_name: str | None = None,
        content: str | None = None,
        language: list[str] | None = None,
        content_type: list[str] | None = None,
        channel_eligibility: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListContentResponse, RawError]:
        """Retrieve a list of Contents belonging to the account used to make the request

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            sort_by_date: Whether to sort by ascending or descending date updated
            sort_by_content_name: Whether to sort by ascending or descending content name
            date_created_after: Filter by >=[date-time]
            date_created_before: Filter by <=[date-time]
            content_name: Filter by Regex Pattern in content name
            content: Filter by Regex Pattern in template content
            language: Filter by array of valid language(s)
            content_type: Filter by array of contentType(s)
            channel_eligibility: Filter by array of ChannelEligibility(s), where ChannelEligibility=<channel>:<status>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default2("/v2/Content"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
                param[str | None]("SortByDate", sort_by_date),
                param[str | None]("SortByContentName", sort_by_content_name),
                param[RFC3339DateTime | None]("DateCreatedAfter", date_created_after),
                param[RFC3339DateTime | None]("DateCreatedBefore", date_created_before),
                param[str | None]("ContentName", content_name),
                param[str | None]("Content", content),
                param[list[str] | None]("Language", language),
                param[list[str] | None]("ContentType", content_type),
                param[list[str] | None]("ChannelEligibility", channel_eligibility),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListContentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
