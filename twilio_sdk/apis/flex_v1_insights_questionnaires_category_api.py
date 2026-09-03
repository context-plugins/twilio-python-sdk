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
from ..models.flex_v1_insights_questionnaires_category import FlexV1InsightsQuestionnairesCategory
from ..models.list_insights_questionnaires_category_response import ListInsightsQuestionnairesCategoryResponse
from ..server.server import Server


class FlexV1InsightsQuestionnairesCategoryApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FlexV1InsightsQuestionnairesCategoryApiWithRawResponse(client, server, auth)

    def create_insights_questionnaires_category(
        self, name: str, *, authorization: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> FlexV1InsightsQuestionnairesCategory:
        """To create a category for Questions

        Args:
            name: The name of this category.
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_insights_questionnaires_category(
            name, authorization=authorization, request_options=request_options
        ).unwrap()

    def delete_insights_questionnaires_category(
        self,
        category_sid: str,
        *,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``DELETE`` request.

        Args:
            category_sid: The SID of the category to be deleted
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_insights_questionnaires_category(
            category_sid, authorization=authorization, request_options=request_options
        ).unwrap()

    def list_insights_questionnaires_category(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInsightsQuestionnairesCategoryResponse:
        """To get all the categories

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_insights_questionnaires_category(
            page_size=page_size,
            page=page,
            page_token=page_token,
            authorization=authorization,
            request_options=request_options,
        ).unwrap()

    def update_insights_questionnaires_category(
        self,
        category_sid: str,
        name: str,
        *,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1InsightsQuestionnairesCategory:
        """To update the category for Questions

        Args:
            category_sid: The SID of the category to be updated
            name: The name of this category.
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_insights_questionnaires_category(
            category_sid, name, authorization=authorization, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> FlexV1InsightsQuestionnairesCategoryApiWithRawResponse:
        return self._with_raw_response


class AsyncFlexV1InsightsQuestionnairesCategoryApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFlexV1InsightsQuestionnairesCategoryApiWithRawResponse(client, server, auth)

    async def create_insights_questionnaires_category(
        self, name: str, *, authorization: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> FlexV1InsightsQuestionnairesCategory:
        """To create a category for Questions

        Args:
            name: The name of this category.
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_insights_questionnaires_category(
                name, authorization=authorization, request_options=request_options
            )
        ).unwrap()

    async def delete_insights_questionnaires_category(
        self,
        category_sid: str,
        *,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``DELETE`` request.

        Args:
            category_sid: The SID of the category to be deleted
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_insights_questionnaires_category(
                category_sid, authorization=authorization, request_options=request_options
            )
        ).unwrap()

    async def list_insights_questionnaires_category(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInsightsQuestionnairesCategoryResponse:
        """To get all the categories

        Args:
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
            await self._with_raw_response.list_insights_questionnaires_category(
                page_size=page_size,
                page=page,
                page_token=page_token,
                authorization=authorization,
                request_options=request_options,
            )
        ).unwrap()

    async def update_insights_questionnaires_category(
        self,
        category_sid: str,
        name: str,
        *,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1InsightsQuestionnairesCategory:
        """To update the category for Questions

        Args:
            category_sid: The SID of the category to be updated
            name: The name of this category.
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_insights_questionnaires_category(
                category_sid, name, authorization=authorization, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncFlexV1InsightsQuestionnairesCategoryApiWithRawResponse:
        return self._with_raw_response


class FlexV1InsightsQuestionnairesCategoryApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_insights_questionnaires_category(
        self, name: str, *, authorization: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FlexV1InsightsQuestionnairesCategory, RawError]:
        """To create a category for Questions

        Args:
            name: The name of this category.
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/Insights/QualityManagement/Categories"),
            headers=[param[str | None]("Authorization", authorization), param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str]("Name", name)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InsightsQuestionnairesCategory],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_insights_questionnaires_category(
        self,
        category_sid: str,
        *,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Send a ``DELETE`` request.

        Args:
            category_sid: The SID of the category to be deleted
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default13("/v1/Insights/QualityManagement/Categories/{CategorySid}"),
            path_params=[param[str]("CategorySid", category_sid)],
            headers=[param[str | None]("Authorization", authorization), param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_insights_questionnaires_category(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInsightsQuestionnairesCategoryResponse, RawError]:
        """To get all the categories

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/Insights/QualityManagement/Categories"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            headers=[param[str | None]("Authorization", authorization)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListInsightsQuestionnairesCategoryResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_insights_questionnaires_category(
        self,
        category_sid: str,
        name: str,
        *,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1InsightsQuestionnairesCategory, RawError]:
        """To update the category for Questions

        Args:
            category_sid: The SID of the category to be updated
            name: The name of this category.
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/Insights/QualityManagement/Categories/{CategorySid}"),
            path_params=[param[str]("CategorySid", category_sid)],
            headers=[param[str | None]("Authorization", authorization), param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str]("Name", name)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InsightsQuestionnairesCategory],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncFlexV1InsightsQuestionnairesCategoryApiWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def create_insights_questionnaires_category(
        self, name: str, *, authorization: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FlexV1InsightsQuestionnairesCategory, RawError]:
        """To create a category for Questions

        Args:
            name: The name of this category.
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/Insights/QualityManagement/Categories"),
            headers=[param[str | None]("Authorization", authorization), param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str]("Name", name)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InsightsQuestionnairesCategory],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_insights_questionnaires_category(
        self,
        category_sid: str,
        *,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Send a ``DELETE`` request.

        Args:
            category_sid: The SID of the category to be deleted
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default13("/v1/Insights/QualityManagement/Categories/{CategorySid}"),
            path_params=[param[str]("CategorySid", category_sid)],
            headers=[param[str | None]("Authorization", authorization), param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_insights_questionnaires_category(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInsightsQuestionnairesCategoryResponse, RawError]:
        """To get all the categories

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/Insights/QualityManagement/Categories"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            headers=[param[str | None]("Authorization", authorization)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListInsightsQuestionnairesCategoryResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_insights_questionnaires_category(
        self,
        category_sid: str,
        name: str,
        *,
        authorization: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1InsightsQuestionnairesCategory, RawError]:
        """To update the category for Questions

        Args:
            category_sid: The SID of the category to be updated
            name: The name of this category.
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/Insights/QualityManagement/Categories/{CategorySid}"),
            path_params=[param[str]("CategorySid", category_sid)],
            headers=[param[str | None]("Authorization", authorization), param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str]("Name", name)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InsightsQuestionnairesCategory],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
