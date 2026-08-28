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
from ..models.flex_v1_insights_questionnaires_question import FlexV1InsightsQuestionnairesQuestion
from ..models.list_insights_questionnaires_question_response import ListInsightsQuestionnairesQuestionResponse
from ..server.server import Server


class FlexV1InsightsQuestionnairesQuestionApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FlexV1InsightsQuestionnairesQuestionApiWithRawResponse(client, server, auth)

    def create_insights_questionnaires_question(
        self,
        category_sid: str,
        question: str,
        answer_set_id: str,
        allow_na: bool,
        *,
        authorization: str | None = None,
        description: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1InsightsQuestionnairesQuestion:
        """To create a question for a Category

        Args:
            category_sid: The SID of the category
            question: The question.
            answer_set_id: The answer_set for the question.
            allow_na: The flag to enable for disable NA for answer.
            authorization: The Authorization HTTP request header
            description: The description for the question.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_insights_questionnaires_question(
            category_sid,
            question,
            answer_set_id,
            allow_na,
            authorization=authorization,
            description=description,
            request_options=request_options,
        ).unwrap()

    def delete_insights_questionnaires_question(
        self,
        question_sid: str,
        *,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``DELETE`` request.

        Args:
            question_sid: The SID of the question
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_insights_questionnaires_question(
            question_sid, authorization=authorization, request_options=request_options
        ).unwrap()

    def list_insights_questionnaires_question(
        self,
        *,
        category_sid: list[str] | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInsightsQuestionnairesQuestionResponse:
        """To get all the question for the given categories

        Args:
            category_sid: The list of category SIDs
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_insights_questionnaires_question(
            category_sid=category_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            authorization=authorization,
            request_options=request_options,
        ).unwrap()

    def update_insights_questionnaires_question(
        self,
        question_sid: str,
        allow_na: bool,
        *,
        authorization: str | None = None,
        category_sid: str | None = None,
        question: str | None = None,
        description: str | None = None,
        answer_set_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1InsightsQuestionnairesQuestion:
        """To update the question

        Args:
            question_sid: The SID of the question
            allow_na: The flag to enable for disable NA for answer.
            authorization: The Authorization HTTP request header
            category_sid: The SID of the category
            question: The question.
            description: The description for the question.
            answer_set_id: The answer_set for the question.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_insights_questionnaires_question(
            question_sid,
            allow_na,
            authorization=authorization,
            category_sid=category_sid,
            question=question,
            description=description,
            answer_set_id=answer_set_id,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> FlexV1InsightsQuestionnairesQuestionApiWithRawResponse:
        return self._with_raw_response


class AsyncFlexV1InsightsQuestionnairesQuestionApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFlexV1InsightsQuestionnairesQuestionApiWithRawResponse(client, server, auth)

    async def create_insights_questionnaires_question(
        self,
        category_sid: str,
        question: str,
        answer_set_id: str,
        allow_na: bool,
        *,
        authorization: str | None = None,
        description: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1InsightsQuestionnairesQuestion:
        """To create a question for a Category

        Args:
            category_sid: The SID of the category
            question: The question.
            answer_set_id: The answer_set for the question.
            allow_na: The flag to enable for disable NA for answer.
            authorization: The Authorization HTTP request header
            description: The description for the question.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_insights_questionnaires_question(
                category_sid,
                question,
                answer_set_id,
                allow_na,
                authorization=authorization,
                description=description,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_insights_questionnaires_question(
        self,
        question_sid: str,
        *,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``DELETE`` request.

        Args:
            question_sid: The SID of the question
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_insights_questionnaires_question(
                question_sid, authorization=authorization, request_options=request_options
            )
        ).unwrap()

    async def list_insights_questionnaires_question(
        self,
        *,
        category_sid: list[str] | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInsightsQuestionnairesQuestionResponse:
        """To get all the question for the given categories

        Args:
            category_sid: The list of category SIDs
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
            await self._with_raw_response.list_insights_questionnaires_question(
                category_sid=category_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                authorization=authorization,
                request_options=request_options,
            )
        ).unwrap()

    async def update_insights_questionnaires_question(
        self,
        question_sid: str,
        allow_na: bool,
        *,
        authorization: str | None = None,
        category_sid: str | None = None,
        question: str | None = None,
        description: str | None = None,
        answer_set_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1InsightsQuestionnairesQuestion:
        """To update the question

        Args:
            question_sid: The SID of the question
            allow_na: The flag to enable for disable NA for answer.
            authorization: The Authorization HTTP request header
            category_sid: The SID of the category
            question: The question.
            description: The description for the question.
            answer_set_id: The answer_set for the question.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_insights_questionnaires_question(
                question_sid,
                allow_na,
                authorization=authorization,
                category_sid=category_sid,
                question=question,
                description=description,
                answer_set_id=answer_set_id,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncFlexV1InsightsQuestionnairesQuestionApiWithRawResponse:
        return self._with_raw_response


class FlexV1InsightsQuestionnairesQuestionApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_insights_questionnaires_question(
        self,
        category_sid: str,
        question: str,
        answer_set_id: str,
        allow_na: bool,
        *,
        authorization: str | None = None,
        description: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1InsightsQuestionnairesQuestion, RawError]:
        """To create a question for a Category

        Args:
            category_sid: The SID of the category
            question: The question.
            answer_set_id: The answer_set for the question.
            allow_na: The flag to enable for disable NA for answer.
            authorization: The Authorization HTTP request header
            description: The description for the question.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/Insights/QualityManagement/Questions"),
            headers=[param[str | None]("Authorization", authorization)],
            body=form_body(
                [
                    param[str]("CategorySid", category_sid),
                    param[str]("Question", question),
                    param[str]("AnswerSetId", answer_set_id),
                    param[bool]("AllowNa", allow_na),
                    param[str | None]("Description", description),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InsightsQuestionnairesQuestion],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_insights_questionnaires_question(
        self,
        question_sid: str,
        *,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Send a ``DELETE`` request.

        Args:
            question_sid: The SID of the question
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default13("/v1/Insights/QualityManagement/Questions/{QuestionSid}"),
            path_params=[param[str]("QuestionSid", question_sid)],
            headers=[param[str | None]("Authorization", authorization)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_insights_questionnaires_question(
        self,
        *,
        category_sid: list[str] | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInsightsQuestionnairesQuestionResponse, RawError]:
        """To get all the question for the given categories

        Args:
            category_sid: The list of category SIDs
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/Insights/QualityManagement/Questions"),
            query_params=[
                param[list[str] | None]("CategorySid", category_sid),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            headers=[param[str | None]("Authorization", authorization)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListInsightsQuestionnairesQuestionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_insights_questionnaires_question(
        self,
        question_sid: str,
        allow_na: bool,
        *,
        authorization: str | None = None,
        category_sid: str | None = None,
        question: str | None = None,
        description: str | None = None,
        answer_set_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1InsightsQuestionnairesQuestion, RawError]:
        """To update the question

        Args:
            question_sid: The SID of the question
            allow_na: The flag to enable for disable NA for answer.
            authorization: The Authorization HTTP request header
            category_sid: The SID of the category
            question: The question.
            description: The description for the question.
            answer_set_id: The answer_set for the question.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/Insights/QualityManagement/Questions/{QuestionSid}"),
            path_params=[param[str]("QuestionSid", question_sid)],
            headers=[param[str | None]("Authorization", authorization)],
            body=form_body(
                [
                    param[bool]("AllowNa", allow_na),
                    param[str | None]("CategorySid", category_sid),
                    param[str | None]("Question", question),
                    param[str | None]("Description", description),
                    param[str | None]("AnswerSetId", answer_set_id),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InsightsQuestionnairesQuestion],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncFlexV1InsightsQuestionnairesQuestionApiWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def create_insights_questionnaires_question(
        self,
        category_sid: str,
        question: str,
        answer_set_id: str,
        allow_na: bool,
        *,
        authorization: str | None = None,
        description: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1InsightsQuestionnairesQuestion, RawError]:
        """To create a question for a Category

        Args:
            category_sid: The SID of the category
            question: The question.
            answer_set_id: The answer_set for the question.
            allow_na: The flag to enable for disable NA for answer.
            authorization: The Authorization HTTP request header
            description: The description for the question.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/Insights/QualityManagement/Questions"),
            headers=[param[str | None]("Authorization", authorization)],
            body=form_body(
                [
                    param[str]("CategorySid", category_sid),
                    param[str]("Question", question),
                    param[str]("AnswerSetId", answer_set_id),
                    param[bool]("AllowNa", allow_na),
                    param[str | None]("Description", description),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InsightsQuestionnairesQuestion],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_insights_questionnaires_question(
        self,
        question_sid: str,
        *,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Send a ``DELETE`` request.

        Args:
            question_sid: The SID of the question
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default13("/v1/Insights/QualityManagement/Questions/{QuestionSid}"),
            path_params=[param[str]("QuestionSid", question_sid)],
            headers=[param[str | None]("Authorization", authorization)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_insights_questionnaires_question(
        self,
        *,
        category_sid: list[str] | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInsightsQuestionnairesQuestionResponse, RawError]:
        """To get all the question for the given categories

        Args:
            category_sid: The list of category SIDs
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/Insights/QualityManagement/Questions"),
            query_params=[
                param[list[str] | None]("CategorySid", category_sid),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            headers=[param[str | None]("Authorization", authorization)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListInsightsQuestionnairesQuestionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_insights_questionnaires_question(
        self,
        question_sid: str,
        allow_na: bool,
        *,
        authorization: str | None = None,
        category_sid: str | None = None,
        question: str | None = None,
        description: str | None = None,
        answer_set_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1InsightsQuestionnairesQuestion, RawError]:
        """To update the question

        Args:
            question_sid: The SID of the question
            allow_na: The flag to enable for disable NA for answer.
            authorization: The Authorization HTTP request header
            category_sid: The SID of the category
            question: The question.
            description: The description for the question.
            answer_set_id: The answer_set for the question.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/Insights/QualityManagement/Questions/{QuestionSid}"),
            path_params=[param[str]("QuestionSid", question_sid)],
            headers=[param[str | None]("Authorization", authorization)],
            body=form_body(
                [
                    param[bool]("AllowNa", allow_na),
                    param[str | None]("CategorySid", category_sid),
                    param[str | None]("Question", question),
                    param[str | None]("Description", description),
                    param[str | None]("AnswerSetId", answer_set_id),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InsightsQuestionnairesQuestion],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
