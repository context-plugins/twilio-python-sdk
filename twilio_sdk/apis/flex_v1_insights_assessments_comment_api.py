from __future__ import annotations

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
from ..models.flex_v1_insights_assessments_comment import FlexV1InsightsAssessmentsComment
from ..models.list_insights_assessments_comment_response import ListInsightsAssessmentsCommentResponse
from ..server.server import Server


class FlexV1InsightsAssessmentsCommentApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FlexV1InsightsAssessmentsCommentApiWithRawResponse(client, server, auth)

    def create_insights_assessments_comment(
        self,
        category_id: str,
        category_name: str,
        comment: str,
        segment_id: str,
        agent_id: str,
        offset: float,
        *,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1InsightsAssessmentsComment:
        """To create a comment assessment for a conversation

        Args:
            category_id: The ID of the category
            category_name: The name of the category
            comment: The Assessment comment.
            segment_id: The id of the segment.
            agent_id: The id of the agent.
            offset: The offset
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_insights_assessments_comment(
            category_id,
            category_name,
            comment,
            segment_id,
            agent_id,
            offset,
            authorization=authorization,
            request_options=request_options,
        ).unwrap()

    def list_insights_assessments_comment(
        self,
        *,
        segment_id: str | None = None,
        agent_id: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInsightsAssessmentsCommentResponse:
        """To create a comment assessment for a conversation

        Args:
            segment_id: The id of the segment.
            agent_id: The id of the agent.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_insights_assessments_comment(
            segment_id=segment_id,
            agent_id=agent_id,
            page_size=page_size,
            page=page,
            page_token=page_token,
            authorization=authorization,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> FlexV1InsightsAssessmentsCommentApiWithRawResponse:
        return self._with_raw_response


class AsyncFlexV1InsightsAssessmentsCommentApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFlexV1InsightsAssessmentsCommentApiWithRawResponse(client, server, auth)

    async def create_insights_assessments_comment(
        self,
        category_id: str,
        category_name: str,
        comment: str,
        segment_id: str,
        agent_id: str,
        offset: float,
        *,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1InsightsAssessmentsComment:
        """To create a comment assessment for a conversation

        Args:
            category_id: The ID of the category
            category_name: The name of the category
            comment: The Assessment comment.
            segment_id: The id of the segment.
            agent_id: The id of the agent.
            offset: The offset
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_insights_assessments_comment(
                category_id,
                category_name,
                comment,
                segment_id,
                agent_id,
                offset,
                authorization=authorization,
                request_options=request_options,
            )
        ).unwrap()

    async def list_insights_assessments_comment(
        self,
        *,
        segment_id: str | None = None,
        agent_id: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInsightsAssessmentsCommentResponse:
        """To create a comment assessment for a conversation

        Args:
            segment_id: The id of the segment.
            agent_id: The id of the agent.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_insights_assessments_comment(
                segment_id=segment_id,
                agent_id=agent_id,
                page_size=page_size,
                page=page,
                page_token=page_token,
                authorization=authorization,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncFlexV1InsightsAssessmentsCommentApiWithRawResponse:
        return self._with_raw_response


class FlexV1InsightsAssessmentsCommentApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_insights_assessments_comment(
        self,
        category_id: str,
        category_name: str,
        comment: str,
        segment_id: str,
        agent_id: str,
        offset: float,
        *,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1InsightsAssessmentsComment, RawError]:
        """To create a comment assessment for a conversation

        Args:
            category_id: The ID of the category
            category_name: The name of the category
            comment: The Assessment comment.
            segment_id: The id of the segment.
            agent_id: The id of the agent.
            offset: The offset
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/Insights/QualityManagement/Assessments/Comments"),
            headers=[param[str | None]("Authorization", authorization)],
            body=form_body(
                [
                    param[str]("CategoryId", category_id),
                    param[str]("CategoryName", category_name),
                    param[str]("Comment", comment),
                    param[str]("SegmentId", segment_id),
                    param[str]("AgentId", agent_id),
                    param[float]("Offset", offset),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InsightsAssessmentsComment],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_insights_assessments_comment(
        self,
        *,
        segment_id: str | None = None,
        agent_id: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInsightsAssessmentsCommentResponse, RawError]:
        """To create a comment assessment for a conversation

        Args:
            segment_id: The id of the segment.
            agent_id: The id of the agent.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/Insights/QualityManagement/Assessments/Comments"),
            query_params=[
                param[str | None]("SegmentId", segment_id),
                param[str | None]("AgentId", agent_id),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            headers=[param[str | None]("Authorization", authorization)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListInsightsAssessmentsCommentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncFlexV1InsightsAssessmentsCommentApiWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def create_insights_assessments_comment(
        self,
        category_id: str,
        category_name: str,
        comment: str,
        segment_id: str,
        agent_id: str,
        offset: float,
        *,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1InsightsAssessmentsComment, RawError]:
        """To create a comment assessment for a conversation

        Args:
            category_id: The ID of the category
            category_name: The name of the category
            comment: The Assessment comment.
            segment_id: The id of the segment.
            agent_id: The id of the agent.
            offset: The offset
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/Insights/QualityManagement/Assessments/Comments"),
            headers=[param[str | None]("Authorization", authorization)],
            body=form_body(
                [
                    param[str]("CategoryId", category_id),
                    param[str]("CategoryName", category_name),
                    param[str]("Comment", comment),
                    param[str]("SegmentId", segment_id),
                    param[str]("AgentId", agent_id),
                    param[float]("Offset", offset),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InsightsAssessmentsComment],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_insights_assessments_comment(
        self,
        *,
        segment_id: str | None = None,
        agent_id: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInsightsAssessmentsCommentResponse, RawError]:
        """To create a comment assessment for a conversation

        Args:
            segment_id: The id of the segment.
            agent_id: The id of the agent.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/Insights/QualityManagement/Assessments/Comments"),
            query_params=[
                param[str | None]("SegmentId", segment_id),
                param[str | None]("AgentId", agent_id),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            headers=[param[str | None]("Authorization", authorization)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListInsightsAssessmentsCommentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
