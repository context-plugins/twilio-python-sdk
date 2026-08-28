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
from ..models.studio_v1_flow_execution_execution_context import StudioV1FlowExecutionExecutionContext
from ..server.server import Server


class StudioV1ExecutionContext:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = StudioV1ExecutionContextWithRawResponse(client, server, auth)

    def fetch_execution_context(
        self, flow_sid: str, execution_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> StudioV1FlowExecutionExecutionContext:
        """Retrieve the most recent context for an Execution.

        Args:
            flow_sid: The SID of the Flow with the Execution context to fetch.
            execution_sid: The SID of the Execution context to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_execution_context(
            flow_sid, execution_sid, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> StudioV1ExecutionContextWithRawResponse:
        return self._with_raw_response


class AsyncStudioV1ExecutionContext:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncStudioV1ExecutionContextWithRawResponse(client, server, auth)

    async def fetch_execution_context(
        self, flow_sid: str, execution_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> StudioV1FlowExecutionExecutionContext:
        """Retrieve the most recent context for an Execution.

        Args:
            flow_sid: The SID of the Flow with the Execution context to fetch.
            execution_sid: The SID of the Execution context to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_execution_context(
                flow_sid, execution_sid, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncStudioV1ExecutionContextWithRawResponse:
        return self._with_raw_response


class StudioV1ExecutionContextWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_execution_context(
        self, flow_sid: str, execution_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[StudioV1FlowExecutionExecutionContext, RawError]:
        """Retrieve the most recent context for an Execution.

        Args:
            flow_sid: The SID of the Flow with the Execution context to fetch.
            execution_sid: The SID of the Execution context to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default11("/v1/Flows/{FlowSid}/Executions/{ExecutionSid}/Context"),
            path_params=[param[str]("FlowSid", flow_sid), param[str]("ExecutionSid", execution_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[StudioV1FlowExecutionExecutionContext],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncStudioV1ExecutionContextWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_execution_context(
        self, flow_sid: str, execution_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[StudioV1FlowExecutionExecutionContext, RawError]:
        """Retrieve the most recent context for an Execution.

        Args:
            flow_sid: The SID of the Flow with the Execution context to fetch.
            execution_sid: The SID of the Execution context to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default11("/v1/Flows/{FlowSid}/Executions/{ExecutionSid}/Context"),
            path_params=[param[str]("FlowSid", flow_sid), param[str]("ExecutionSid", execution_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[StudioV1FlowExecutionExecutionContext],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
