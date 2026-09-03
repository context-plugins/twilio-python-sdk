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
    empty_response,
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.flex_v1_insights_questionnaires import FlexV1InsightsQuestionnaires
from ..models.list_insights_questionnaires_response import ListInsightsQuestionnairesResponse
from ..server.server import Server


class FlexV1InsightsQuestionnairesApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FlexV1InsightsQuestionnairesApiWithRawResponse(client, server, auth)

    def create_insights_questionnaires(
        self,
        name: str,
        *,
        authorization: str | None = None,
        description: str | None = None,
        active: bool | None = None,
        question_sids: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1InsightsQuestionnaires:
        """To create a Questionnaire

        Args:
            name: The name of this questionnaire
            authorization: The Authorization HTTP request header
            description: The description of this questionnaire
            active: The flag to enable or disable questionnaire
            question_sids: The list of questions sids under a questionnaire
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_insights_questionnaires(
            name,
            authorization=authorization,
            description=description,
            active=active,
            question_sids=question_sids,
            request_options=request_options,
        ).unwrap()

    def delete_insights_questionnaires(
        self,
        questionnaire_sid: str,
        *,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """To delete the questionnaire

        Args:
            questionnaire_sid: The SID of the questionnaire
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_insights_questionnaires(
            questionnaire_sid, authorization=authorization, request_options=request_options
        ).unwrap()

    def fetch_insights_questionnaires(
        self,
        questionnaire_sid: str,
        *,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1InsightsQuestionnaires:
        """To get the Questionnaire Detail

        Args:
            questionnaire_sid: The SID of the questionnaire
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_insights_questionnaires(
            questionnaire_sid, authorization=authorization, request_options=request_options
        ).unwrap()

    def list_insights_questionnaires(
        self,
        *,
        include_inactive: bool | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInsightsQuestionnairesResponse:
        """To get all questionnaires with questions

        Args:
            include_inactive: Flag indicating whether to include inactive questionnaires or not
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_insights_questionnaires(
            include_inactive=include_inactive,
            page_size=page_size,
            page=page,
            page_token=page_token,
            authorization=authorization,
            request_options=request_options,
        ).unwrap()

    def update_insights_questionnaires(
        self,
        questionnaire_sid: str,
        active: bool,
        *,
        authorization: str | None = None,
        name: str | None = None,
        description: str | None = None,
        question_sids: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1InsightsQuestionnaires:
        """To update the questionnaire

        Args:
            questionnaire_sid: The SID of the questionnaire
            active: The flag to enable or disable questionnaire
            authorization: The Authorization HTTP request header
            name: The name of this questionnaire
            description: The description of this questionnaire
            question_sids: The list of questions sids under a questionnaire
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_insights_questionnaires(
            questionnaire_sid,
            active,
            authorization=authorization,
            name=name,
            description=description,
            question_sids=question_sids,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> FlexV1InsightsQuestionnairesApiWithRawResponse:
        return self._with_raw_response


class AsyncFlexV1InsightsQuestionnairesApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFlexV1InsightsQuestionnairesApiWithRawResponse(client, server, auth)

    async def create_insights_questionnaires(
        self,
        name: str,
        *,
        authorization: str | None = None,
        description: str | None = None,
        active: bool | None = None,
        question_sids: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1InsightsQuestionnaires:
        """To create a Questionnaire

        Args:
            name: The name of this questionnaire
            authorization: The Authorization HTTP request header
            description: The description of this questionnaire
            active: The flag to enable or disable questionnaire
            question_sids: The list of questions sids under a questionnaire
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_insights_questionnaires(
                name,
                authorization=authorization,
                description=description,
                active=active,
                question_sids=question_sids,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_insights_questionnaires(
        self,
        questionnaire_sid: str,
        *,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """To delete the questionnaire

        Args:
            questionnaire_sid: The SID of the questionnaire
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_insights_questionnaires(
                questionnaire_sid, authorization=authorization, request_options=request_options
            )
        ).unwrap()

    async def fetch_insights_questionnaires(
        self,
        questionnaire_sid: str,
        *,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1InsightsQuestionnaires:
        """To get the Questionnaire Detail

        Args:
            questionnaire_sid: The SID of the questionnaire
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_insights_questionnaires(
                questionnaire_sid, authorization=authorization, request_options=request_options
            )
        ).unwrap()

    async def list_insights_questionnaires(
        self,
        *,
        include_inactive: bool | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInsightsQuestionnairesResponse:
        """To get all questionnaires with questions

        Args:
            include_inactive: Flag indicating whether to include inactive questionnaires or not
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
            await self._with_raw_response.list_insights_questionnaires(
                include_inactive=include_inactive,
                page_size=page_size,
                page=page,
                page_token=page_token,
                authorization=authorization,
                request_options=request_options,
            )
        ).unwrap()

    async def update_insights_questionnaires(
        self,
        questionnaire_sid: str,
        active: bool,
        *,
        authorization: str | None = None,
        name: str | None = None,
        description: str | None = None,
        question_sids: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1InsightsQuestionnaires:
        """To update the questionnaire

        Args:
            questionnaire_sid: The SID of the questionnaire
            active: The flag to enable or disable questionnaire
            authorization: The Authorization HTTP request header
            name: The name of this questionnaire
            description: The description of this questionnaire
            question_sids: The list of questions sids under a questionnaire
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_insights_questionnaires(
                questionnaire_sid,
                active,
                authorization=authorization,
                name=name,
                description=description,
                question_sids=question_sids,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncFlexV1InsightsQuestionnairesApiWithRawResponse:
        return self._with_raw_response


class FlexV1InsightsQuestionnairesApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_insights_questionnaires(
        self,
        name: str,
        *,
        authorization: str | None = None,
        description: str | None = None,
        active: bool | None = None,
        question_sids: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1InsightsQuestionnaires, RawError]:
        """To create a Questionnaire

        Args:
            name: The name of this questionnaire
            authorization: The Authorization HTTP request header
            description: The description of this questionnaire
            active: The flag to enable or disable questionnaire
            question_sids: The list of questions sids under a questionnaire
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/Insights/QualityManagement/Questionnaires"),
            headers=[param[str | None]("Authorization", authorization), param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("Name", name),
                    param[str | None]("Description", description),
                    param[bool | None]("Active", active),
                    param[list[str] | None]("QuestionSids", question_sids),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InsightsQuestionnaires],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_insights_questionnaires(
        self,
        questionnaire_sid: str,
        *,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """To delete the questionnaire

        Args:
            questionnaire_sid: The SID of the questionnaire
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default13("/v1/Insights/QualityManagement/Questionnaires/{QuestionnaireSid}"),
            path_params=[param[str]("QuestionnaireSid", questionnaire_sid)],
            headers=[param[str | None]("Authorization", authorization), param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_insights_questionnaires(
        self,
        questionnaire_sid: str,
        *,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1InsightsQuestionnaires, RawError]:
        """To get the Questionnaire Detail

        Args:
            questionnaire_sid: The SID of the questionnaire
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/Insights/QualityManagement/Questionnaires/{QuestionnaireSid}"),
            path_params=[param[str]("QuestionnaireSid", questionnaire_sid)],
            headers=[param[str | None]("Authorization", authorization)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InsightsQuestionnaires],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_insights_questionnaires(
        self,
        *,
        include_inactive: bool | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInsightsQuestionnairesResponse, RawError]:
        """To get all questionnaires with questions

        Args:
            include_inactive: Flag indicating whether to include inactive questionnaires or not
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/Insights/QualityManagement/Questionnaires"),
            query_params=[
                param[bool | None]("IncludeInactive", include_inactive),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            headers=[param[str | None]("Authorization", authorization)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListInsightsQuestionnairesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_insights_questionnaires(
        self,
        questionnaire_sid: str,
        active: bool,
        *,
        authorization: str | None = None,
        name: str | None = None,
        description: str | None = None,
        question_sids: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1InsightsQuestionnaires, RawError]:
        """To update the questionnaire

        Args:
            questionnaire_sid: The SID of the questionnaire
            active: The flag to enable or disable questionnaire
            authorization: The Authorization HTTP request header
            name: The name of this questionnaire
            description: The description of this questionnaire
            question_sids: The list of questions sids under a questionnaire
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/Insights/QualityManagement/Questionnaires/{QuestionnaireSid}"),
            path_params=[param[str]("QuestionnaireSid", questionnaire_sid)],
            headers=[param[str | None]("Authorization", authorization), param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[bool]("Active", active),
                    param[str | None]("Name", name),
                    param[str | None]("Description", description),
                    param[list[str] | None]("QuestionSids", question_sids),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InsightsQuestionnaires],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncFlexV1InsightsQuestionnairesApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_insights_questionnaires(
        self,
        name: str,
        *,
        authorization: str | None = None,
        description: str | None = None,
        active: bool | None = None,
        question_sids: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1InsightsQuestionnaires, RawError]:
        """To create a Questionnaire

        Args:
            name: The name of this questionnaire
            authorization: The Authorization HTTP request header
            description: The description of this questionnaire
            active: The flag to enable or disable questionnaire
            question_sids: The list of questions sids under a questionnaire
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/Insights/QualityManagement/Questionnaires"),
            headers=[param[str | None]("Authorization", authorization), param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("Name", name),
                    param[str | None]("Description", description),
                    param[bool | None]("Active", active),
                    param[list[str] | None]("QuestionSids", question_sids),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InsightsQuestionnaires],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_insights_questionnaires(
        self,
        questionnaire_sid: str,
        *,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """To delete the questionnaire

        Args:
            questionnaire_sid: The SID of the questionnaire
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default13("/v1/Insights/QualityManagement/Questionnaires/{QuestionnaireSid}"),
            path_params=[param[str]("QuestionnaireSid", questionnaire_sid)],
            headers=[param[str | None]("Authorization", authorization), param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_insights_questionnaires(
        self,
        questionnaire_sid: str,
        *,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1InsightsQuestionnaires, RawError]:
        """To get the Questionnaire Detail

        Args:
            questionnaire_sid: The SID of the questionnaire
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/Insights/QualityManagement/Questionnaires/{QuestionnaireSid}"),
            path_params=[param[str]("QuestionnaireSid", questionnaire_sid)],
            headers=[param[str | None]("Authorization", authorization)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InsightsQuestionnaires],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_insights_questionnaires(
        self,
        *,
        include_inactive: bool | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInsightsQuestionnairesResponse, RawError]:
        """To get all questionnaires with questions

        Args:
            include_inactive: Flag indicating whether to include inactive questionnaires or not
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/Insights/QualityManagement/Questionnaires"),
            query_params=[
                param[bool | None]("IncludeInactive", include_inactive),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            headers=[param[str | None]("Authorization", authorization)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListInsightsQuestionnairesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_insights_questionnaires(
        self,
        questionnaire_sid: str,
        active: bool,
        *,
        authorization: str | None = None,
        name: str | None = None,
        description: str | None = None,
        question_sids: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1InsightsQuestionnaires, RawError]:
        """To update the questionnaire

        Args:
            questionnaire_sid: The SID of the questionnaire
            active: The flag to enable or disable questionnaire
            authorization: The Authorization HTTP request header
            name: The name of this questionnaire
            description: The description of this questionnaire
            question_sids: The list of questions sids under a questionnaire
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/Insights/QualityManagement/Questionnaires/{QuestionnaireSid}"),
            path_params=[param[str]("QuestionnaireSid", questionnaire_sid)],
            headers=[param[str | None]("Authorization", authorization), param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[bool]("Active", active),
                    param[str | None]("Name", name),
                    param[str | None]("Description", description),
                    param[list[str] | None]("QuestionSids", question_sids),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InsightsQuestionnaires],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
