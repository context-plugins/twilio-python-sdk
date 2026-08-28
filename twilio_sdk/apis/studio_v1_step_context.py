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
from ..models.studio_v1_flow_engagement_step_step_context import StudioV1FlowEngagementStepStepContext
from ..server.server import Server


class StudioV1StepContext:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = StudioV1StepContextWithRawResponse(client, server, auth)

    def fetch_step_context(
        self, flow_sid: str, engagement_sid: str, step_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> StudioV1FlowEngagementStepStepContext:
        """Retrieve the context for an Engagement Step.

        Args:
            flow_sid: The SID of the Flow with the Step to fetch.
            engagement_sid: The SID of the Engagement with the Step to fetch.
            step_sid: The SID of the Step to fetch
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_step_context(
            flow_sid, engagement_sid, step_sid, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> StudioV1StepContextWithRawResponse:
        return self._with_raw_response


class AsyncStudioV1StepContext:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncStudioV1StepContextWithRawResponse(client, server, auth)

    async def fetch_step_context(
        self, flow_sid: str, engagement_sid: str, step_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> StudioV1FlowEngagementStepStepContext:
        """Retrieve the context for an Engagement Step.

        Args:
            flow_sid: The SID of the Flow with the Step to fetch.
            engagement_sid: The SID of the Engagement with the Step to fetch.
            step_sid: The SID of the Step to fetch
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_step_context(
                flow_sid, engagement_sid, step_sid, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncStudioV1StepContextWithRawResponse:
        return self._with_raw_response


class StudioV1StepContextWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_step_context(
        self, flow_sid: str, engagement_sid: str, step_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[StudioV1FlowEngagementStepStepContext, RawError]:
        """Retrieve the context for an Engagement Step.

        Args:
            flow_sid: The SID of the Flow with the Step to fetch.
            engagement_sid: The SID of the Engagement with the Step to fetch.
            step_sid: The SID of the Step to fetch
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default11(
                "/v1/Flows/{FlowSid}/Engagements/{EngagementSid}/Steps/{StepSid}/Context"
            ),
            path_params=[
                param[str]("FlowSid", flow_sid),
                param[str]("EngagementSid", engagement_sid),
                param[str]("StepSid", step_sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[StudioV1FlowEngagementStepStepContext],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncStudioV1StepContextWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_step_context(
        self, flow_sid: str, engagement_sid: str, step_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[StudioV1FlowEngagementStepStepContext, RawError]:
        """Retrieve the context for an Engagement Step.

        Args:
            flow_sid: The SID of the Flow with the Step to fetch.
            engagement_sid: The SID of the Engagement with the Step to fetch.
            step_sid: The SID of the Step to fetch
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default11(
                "/v1/Flows/{FlowSid}/Engagements/{EngagementSid}/Steps/{StepSid}/Context"
            ),
            path_params=[
                param[str]("FlowSid", flow_sid),
                param[str]("EngagementSid", engagement_sid),
                param[str]("StepSid", step_sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[StudioV1FlowEngagementStepStepContext],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
