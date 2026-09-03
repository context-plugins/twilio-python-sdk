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
from ..models.flex_v1_insights_assessments import FlexV1InsightsAssessments
from ..models.list_insights_assessments_response import ListInsightsAssessmentsResponse
from ..server.server import Server


class FlexV1Assessments:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FlexV1AssessmentsWithRawResponse(client, server, auth)

    def create_insights_assessments(
        self,
        category_sid: str,
        category_name: str,
        segment_id: str,
        agent_id: str,
        offset: float,
        metric_id: str,
        metric_name: str,
        answer_text: str,
        answer_id: str,
        questionnaire_sid: str,
        *,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1InsightsAssessments:
        """Add assessments against conversation to dynamo db. Used in assessments screen by user. Users can select the
        questionnaire and pick up answers for each and every question.

        Args:
            category_sid: The SID of the category
            category_name: The name of the category
            segment_id: Segment Id of the conversation
            agent_id: The id of the Agent
            offset: The offset of the conversation.
            metric_id: The question SID selected for assessment
            metric_name: The question name of the assessment
            answer_text: The answer text selected by user
            answer_id: The id of the answer selected by user
            questionnaire_sid: Questionnaire SID of the associated question
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_insights_assessments(
            category_sid,
            category_name,
            segment_id,
            agent_id,
            offset,
            metric_id,
            metric_name,
            answer_text,
            answer_id,
            questionnaire_sid,
            authorization=authorization,
            request_options=request_options,
        ).unwrap()

    def list_insights_assessments(
        self,
        *,
        segment_id: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInsightsAssessmentsResponse:
        """Get assessments done for a conversation by logged in user

        Args:
            segment_id: The id of the segment.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_insights_assessments(
            segment_id=segment_id,
            page_size=page_size,
            page=page,
            page_token=page_token,
            authorization=authorization,
            request_options=request_options,
        ).unwrap()

    def update_insights_assessments(
        self,
        assessment_sid: str,
        offset: float,
        answer_text: str,
        answer_id: str,
        *,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1InsightsAssessments:
        """Update a specific Assessment assessed earlier

        Args:
            assessment_sid: The SID of the assessment to be modified
            offset: The offset of the conversation
            answer_text: The answer text selected by user
            answer_id: The id of the answer selected by user
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_insights_assessments(
            assessment_sid, offset, answer_text, answer_id, authorization=authorization, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> FlexV1AssessmentsWithRawResponse:
        return self._with_raw_response


class AsyncFlexV1Assessments:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFlexV1AssessmentsWithRawResponse(client, server, auth)

    async def create_insights_assessments(
        self,
        category_sid: str,
        category_name: str,
        segment_id: str,
        agent_id: str,
        offset: float,
        metric_id: str,
        metric_name: str,
        answer_text: str,
        answer_id: str,
        questionnaire_sid: str,
        *,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1InsightsAssessments:
        """Add assessments against conversation to dynamo db. Used in assessments screen by user. Users can select the
        questionnaire and pick up answers for each and every question.

        Args:
            category_sid: The SID of the category
            category_name: The name of the category
            segment_id: Segment Id of the conversation
            agent_id: The id of the Agent
            offset: The offset of the conversation.
            metric_id: The question SID selected for assessment
            metric_name: The question name of the assessment
            answer_text: The answer text selected by user
            answer_id: The id of the answer selected by user
            questionnaire_sid: Questionnaire SID of the associated question
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_insights_assessments(
                category_sid,
                category_name,
                segment_id,
                agent_id,
                offset,
                metric_id,
                metric_name,
                answer_text,
                answer_id,
                questionnaire_sid,
                authorization=authorization,
                request_options=request_options,
            )
        ).unwrap()

    async def list_insights_assessments(
        self,
        *,
        segment_id: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInsightsAssessmentsResponse:
        """Get assessments done for a conversation by logged in user

        Args:
            segment_id: The id of the segment.
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
            await self._with_raw_response.list_insights_assessments(
                segment_id=segment_id,
                page_size=page_size,
                page=page,
                page_token=page_token,
                authorization=authorization,
                request_options=request_options,
            )
        ).unwrap()

    async def update_insights_assessments(
        self,
        assessment_sid: str,
        offset: float,
        answer_text: str,
        answer_id: str,
        *,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1InsightsAssessments:
        """Update a specific Assessment assessed earlier

        Args:
            assessment_sid: The SID of the assessment to be modified
            offset: The offset of the conversation
            answer_text: The answer text selected by user
            answer_id: The id of the answer selected by user
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_insights_assessments(
                assessment_sid,
                offset,
                answer_text,
                answer_id,
                authorization=authorization,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncFlexV1AssessmentsWithRawResponse:
        return self._with_raw_response


class FlexV1AssessmentsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_insights_assessments(
        self,
        category_sid: str,
        category_name: str,
        segment_id: str,
        agent_id: str,
        offset: float,
        metric_id: str,
        metric_name: str,
        answer_text: str,
        answer_id: str,
        questionnaire_sid: str,
        *,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1InsightsAssessments, RawError]:
        """Add assessments against conversation to dynamo db. Used in assessments screen by user. Users can select the
        questionnaire and pick up answers for each and every question.

        Args:
            category_sid: The SID of the category
            category_name: The name of the category
            segment_id: Segment Id of the conversation
            agent_id: The id of the Agent
            offset: The offset of the conversation.
            metric_id: The question SID selected for assessment
            metric_name: The question name of the assessment
            answer_text: The answer text selected by user
            answer_id: The id of the answer selected by user
            questionnaire_sid: Questionnaire SID of the associated question
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/Insights/QualityManagement/Assessments"),
            headers=[param[str | None]("Authorization", authorization), param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("CategorySid", category_sid),
                    param[str]("CategoryName", category_name),
                    param[str]("SegmentId", segment_id),
                    param[str]("AgentId", agent_id),
                    param[float]("Offset", offset),
                    param[str]("MetricId", metric_id),
                    param[str]("MetricName", metric_name),
                    param[str]("AnswerText", answer_text),
                    param[str]("AnswerId", answer_id),
                    param[str]("QuestionnaireSid", questionnaire_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InsightsAssessments],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_insights_assessments(
        self,
        *,
        segment_id: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInsightsAssessmentsResponse, RawError]:
        """Get assessments done for a conversation by logged in user

        Args:
            segment_id: The id of the segment.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/Insights/QualityManagement/Assessments"),
            query_params=[
                param[str | None]("SegmentId", segment_id),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            headers=[param[str | None]("Authorization", authorization)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListInsightsAssessmentsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_insights_assessments(
        self,
        assessment_sid: str,
        offset: float,
        answer_text: str,
        answer_id: str,
        *,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1InsightsAssessments, RawError]:
        """Update a specific Assessment assessed earlier

        Args:
            assessment_sid: The SID of the assessment to be modified
            offset: The offset of the conversation
            answer_text: The answer text selected by user
            answer_id: The id of the answer selected by user
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/Insights/QualityManagement/Assessments/{AssessmentSid}"),
            path_params=[param[str]("AssessmentSid", assessment_sid)],
            headers=[param[str | None]("Authorization", authorization), param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[float]("Offset", offset),
                    param[str]("AnswerText", answer_text),
                    param[str]("AnswerId", answer_id),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InsightsAssessments],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncFlexV1AssessmentsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_insights_assessments(
        self,
        category_sid: str,
        category_name: str,
        segment_id: str,
        agent_id: str,
        offset: float,
        metric_id: str,
        metric_name: str,
        answer_text: str,
        answer_id: str,
        questionnaire_sid: str,
        *,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1InsightsAssessments, RawError]:
        """Add assessments against conversation to dynamo db. Used in assessments screen by user. Users can select the
        questionnaire and pick up answers for each and every question.

        Args:
            category_sid: The SID of the category
            category_name: The name of the category
            segment_id: Segment Id of the conversation
            agent_id: The id of the Agent
            offset: The offset of the conversation.
            metric_id: The question SID selected for assessment
            metric_name: The question name of the assessment
            answer_text: The answer text selected by user
            answer_id: The id of the answer selected by user
            questionnaire_sid: Questionnaire SID of the associated question
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/Insights/QualityManagement/Assessments"),
            headers=[param[str | None]("Authorization", authorization), param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("CategorySid", category_sid),
                    param[str]("CategoryName", category_name),
                    param[str]("SegmentId", segment_id),
                    param[str]("AgentId", agent_id),
                    param[float]("Offset", offset),
                    param[str]("MetricId", metric_id),
                    param[str]("MetricName", metric_name),
                    param[str]("AnswerText", answer_text),
                    param[str]("AnswerId", answer_id),
                    param[str]("QuestionnaireSid", questionnaire_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InsightsAssessments],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_insights_assessments(
        self,
        *,
        segment_id: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInsightsAssessmentsResponse, RawError]:
        """Get assessments done for a conversation by logged in user

        Args:
            segment_id: The id of the segment.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/Insights/QualityManagement/Assessments"),
            query_params=[
                param[str | None]("SegmentId", segment_id),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            headers=[param[str | None]("Authorization", authorization)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListInsightsAssessmentsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_insights_assessments(
        self,
        assessment_sid: str,
        offset: float,
        answer_text: str,
        answer_id: str,
        *,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1InsightsAssessments, RawError]:
        """Update a specific Assessment assessed earlier

        Args:
            assessment_sid: The SID of the assessment to be modified
            offset: The offset of the conversation
            answer_text: The answer text selected by user
            answer_id: The id of the answer selected by user
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/Insights/QualityManagement/Assessments/{AssessmentSid}"),
            path_params=[param[str]("AssessmentSid", assessment_sid)],
            headers=[param[str | None]("Authorization", authorization), param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[float]("Offset", offset),
                    param[str]("AnswerText", answer_text),
                    param[str]("AnswerId", answer_id),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InsightsAssessments],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
