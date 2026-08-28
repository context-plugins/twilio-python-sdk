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
from ..models.list_execution_step_response import ListExecutionStepResponse
from ..models.studio_v1_flow_execution_execution_step import StudioV1FlowExecutionExecutionStep
from ..server.server import Server


class StudioV1ExecutionStep:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = StudioV1ExecutionStepWithRawResponse(client, server, auth)

    def fetch_execution_step(
        self, flow_sid: str, execution_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> StudioV1FlowExecutionExecutionStep:
        """Retrieve a Step.

        Args:
            flow_sid: The SID of the Flow with the Step to fetch.
            execution_sid: The SID of the Execution resource with the Step to fetch.
            sid: The SID of the ExecutionStep resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_execution_step(
            flow_sid, execution_sid, sid, request_options=request_options
        ).unwrap()

    def list_execution_step(
        self,
        flow_sid: str,
        execution_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListExecutionStepResponse:
        """Retrieve a list of all Steps for an Execution.

        Args:
            flow_sid: The SID of the Flow with the Steps to read.
            execution_sid: The SID of the Execution with the Steps to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_execution_step(
            flow_sid,
            execution_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> StudioV1ExecutionStepWithRawResponse:
        return self._with_raw_response


class AsyncStudioV1ExecutionStep:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncStudioV1ExecutionStepWithRawResponse(client, server, auth)

    async def fetch_execution_step(
        self, flow_sid: str, execution_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> StudioV1FlowExecutionExecutionStep:
        """Retrieve a Step.

        Args:
            flow_sid: The SID of the Flow with the Step to fetch.
            execution_sid: The SID of the Execution resource with the Step to fetch.
            sid: The SID of the ExecutionStep resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_execution_step(
                flow_sid, execution_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def list_execution_step(
        self,
        flow_sid: str,
        execution_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListExecutionStepResponse:
        """Retrieve a list of all Steps for an Execution.

        Args:
            flow_sid: The SID of the Flow with the Steps to read.
            execution_sid: The SID of the Execution with the Steps to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_execution_step(
                flow_sid,
                execution_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncStudioV1ExecutionStepWithRawResponse:
        return self._with_raw_response


class StudioV1ExecutionStepWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_execution_step(
        self, flow_sid: str, execution_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[StudioV1FlowExecutionExecutionStep, RawError]:
        """Retrieve a Step.

        Args:
            flow_sid: The SID of the Flow with the Step to fetch.
            execution_sid: The SID of the Execution resource with the Step to fetch.
            sid: The SID of the ExecutionStep resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default11("/v1/Flows/{FlowSid}/Executions/{ExecutionSid}/Steps/{Sid}"),
            path_params=[
                param[str]("FlowSid", flow_sid), param[str]("ExecutionSid", execution_sid), param[str]("Sid", sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[StudioV1FlowExecutionExecutionStep],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_execution_step(
        self,
        flow_sid: str,
        execution_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListExecutionStepResponse, RawError]:
        """Retrieve a list of all Steps for an Execution.

        Args:
            flow_sid: The SID of the Flow with the Steps to read.
            execution_sid: The SID of the Execution with the Steps to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default11("/v1/Flows/{FlowSid}/Executions/{ExecutionSid}/Steps"),
            path_params=[param[str]("FlowSid", flow_sid), param[str]("ExecutionSid", execution_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListExecutionStepResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncStudioV1ExecutionStepWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_execution_step(
        self, flow_sid: str, execution_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[StudioV1FlowExecutionExecutionStep, RawError]:
        """Retrieve a Step.

        Args:
            flow_sid: The SID of the Flow with the Step to fetch.
            execution_sid: The SID of the Execution resource with the Step to fetch.
            sid: The SID of the ExecutionStep resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default11("/v1/Flows/{FlowSid}/Executions/{ExecutionSid}/Steps/{Sid}"),
            path_params=[
                param[str]("FlowSid", flow_sid), param[str]("ExecutionSid", execution_sid), param[str]("Sid", sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[StudioV1FlowExecutionExecutionStep],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_execution_step(
        self,
        flow_sid: str,
        execution_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListExecutionStepResponse, RawError]:
        """Retrieve a list of all Steps for an Execution.

        Args:
            flow_sid: The SID of the Flow with the Steps to read.
            execution_sid: The SID of the Execution with the Steps to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default11("/v1/Flows/{FlowSid}/Executions/{ExecutionSid}/Steps"),
            path_params=[param[str]("FlowSid", flow_sid), param[str]("ExecutionSid", execution_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListExecutionStepResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
