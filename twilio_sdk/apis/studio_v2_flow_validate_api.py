from __future__ import annotations

from typing import Any
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
from ..models.enums.flow_enum_status import FlowEnumStatusOrStr
from ..models.studio_v2_flow_validate import StudioV2FlowValidate
from ..server.server import Server


class StudioV2FlowValidateApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = StudioV2FlowValidateApiWithRawResponse(client, server, auth)

    def update_flow_validate(
        self,
        friendly_name: str,
        status: FlowEnumStatusOrStr,
        definition: Any,
        *,
        commit_message: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StudioV2FlowValidate:
        """Validate flow JSON definition

        Args:
            friendly_name: The string that you assigned to describe the Flow.
            status: The status of the Flow. Can be: ``draft`` or ``published``.
            definition: JSON representation of flow definition.
            commit_message: Description of change made in the revision.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_flow_validate(
            friendly_name, status, definition, commit_message=commit_message, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> StudioV2FlowValidateApiWithRawResponse:
        return self._with_raw_response


class AsyncStudioV2FlowValidateApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncStudioV2FlowValidateApiWithRawResponse(client, server, auth)

    async def update_flow_validate(
        self,
        friendly_name: str,
        status: FlowEnumStatusOrStr,
        definition: Any,
        *,
        commit_message: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StudioV2FlowValidate:
        """Validate flow JSON definition

        Args:
            friendly_name: The string that you assigned to describe the Flow.
            status: The status of the Flow. Can be: ``draft`` or ``published``.
            definition: JSON representation of flow definition.
            commit_message: Description of change made in the revision.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_flow_validate(
                friendly_name, status, definition, commit_message=commit_message, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncStudioV2FlowValidateApiWithRawResponse:
        return self._with_raw_response


class StudioV2FlowValidateApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def update_flow_validate(
        self,
        friendly_name: str,
        status: FlowEnumStatusOrStr,
        definition: Any,
        *,
        commit_message: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StudioV2FlowValidate, RawError]:
        """Validate flow JSON definition

        Args:
            friendly_name: The string that you assigned to describe the Flow.
            status: The status of the Flow. Can be: ``draft`` or ``published``.
            definition: JSON representation of flow definition.
            commit_message: Description of change made in the revision.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default11("/v2/Flows/Validate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[FlowEnumStatusOrStr]("Status", status),
                    param[Any]("Definition", definition),
                    param[str | None]("CommitMessage", commit_message),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[StudioV2FlowValidate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncStudioV2FlowValidateApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def update_flow_validate(
        self,
        friendly_name: str,
        status: FlowEnumStatusOrStr,
        definition: Any,
        *,
        commit_message: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StudioV2FlowValidate, RawError]:
        """Validate flow JSON definition

        Args:
            friendly_name: The string that you assigned to describe the Flow.
            status: The status of the Flow. Can be: ``draft`` or ``published``.
            definition: JSON representation of flow definition.
            commit_message: Description of change made in the revision.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default11("/v2/Flows/Validate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[FlowEnumStatusOrStr]("Status", status),
                    param[Any]("Definition", definition),
                    param[str | None]("CommitMessage", commit_message),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[StudioV2FlowValidate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
