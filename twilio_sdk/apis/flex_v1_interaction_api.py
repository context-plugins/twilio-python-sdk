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
from ..models.flex_v1_interaction import FlexV1Interaction
from ..server.server import Server


class FlexV1InteractionApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FlexV1InteractionApiWithRawResponse(client, server, auth)

    def create_interaction(
        self,
        channel: Any,
        *,
        routing: Any | None = None,
        interaction_context_sid: str | None = None,
        webhook_ttid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1Interaction:
        """Create a new Interaction.

        Args:
            channel: The Interaction's channel.
            routing: The Interaction's routing logic.
            interaction_context_sid: The Interaction context sid is used for adding a context lookup sid
            webhook_ttid: The unique identifier for Interaction level webhook
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_interaction(
            channel,
            routing=routing,
            interaction_context_sid=interaction_context_sid,
            webhook_ttid=webhook_ttid,
            request_options=request_options,
        ).unwrap()

    def fetch_interaction2(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> FlexV1Interaction:
        """Send a ``GET`` request.

        Args:
            sid: The SID of the Interaction resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_interaction2(sid, request_options=request_options).unwrap()

    def update_interaction(
        self, sid: str, *, webhook_ttid: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> FlexV1Interaction:
        """Updates an interaction.

        Args:
            sid: The SID of the Interaction resource to fetch.
            webhook_ttid: The unique identifier for Interaction level webhook
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_interaction(
            sid, webhook_ttid=webhook_ttid, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> FlexV1InteractionApiWithRawResponse:
        return self._with_raw_response


class AsyncFlexV1InteractionApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFlexV1InteractionApiWithRawResponse(client, server, auth)

    async def create_interaction(
        self,
        channel: Any,
        *,
        routing: Any | None = None,
        interaction_context_sid: str | None = None,
        webhook_ttid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1Interaction:
        """Create a new Interaction.

        Args:
            channel: The Interaction's channel.
            routing: The Interaction's routing logic.
            interaction_context_sid: The Interaction context sid is used for adding a context lookup sid
            webhook_ttid: The unique identifier for Interaction level webhook
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_interaction(
                channel,
                routing=routing,
                interaction_context_sid=interaction_context_sid,
                webhook_ttid=webhook_ttid,
                request_options=request_options,
            )
        ).unwrap()

    async def fetch_interaction2(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FlexV1Interaction:
        """Send a ``GET`` request.

        Args:
            sid: The SID of the Interaction resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_interaction2(sid, request_options=request_options)).unwrap()

    async def update_interaction(
        self, sid: str, *, webhook_ttid: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> FlexV1Interaction:
        """Updates an interaction.

        Args:
            sid: The SID of the Interaction resource to fetch.
            webhook_ttid: The unique identifier for Interaction level webhook
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_interaction(
                sid, webhook_ttid=webhook_ttid, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncFlexV1InteractionApiWithRawResponse:
        return self._with_raw_response


class FlexV1InteractionApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_interaction(
        self,
        channel: Any,
        *,
        routing: Any | None = None,
        interaction_context_sid: str | None = None,
        webhook_ttid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1Interaction, RawError]:
        """Create a new Interaction.

        Args:
            channel: The Interaction's channel.
            routing: The Interaction's routing logic.
            interaction_context_sid: The Interaction context sid is used for adding a context lookup sid
            webhook_ttid: The unique identifier for Interaction level webhook
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/Interactions"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[Any]("Channel", channel),
                    param[Any | None]("Routing", routing),
                    param[str | None]("InteractionContextSid", interaction_context_sid),
                    param[str | None]("WebhookTtid", webhook_ttid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1Interaction],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_interaction2(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FlexV1Interaction, RawError]:
        """Send a ``GET`` request.

        Args:
            sid: The SID of the Interaction resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/Interactions/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1Interaction],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_interaction(
        self, sid: str, *, webhook_ttid: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FlexV1Interaction, RawError]:
        """Updates an interaction.

        Args:
            sid: The SID of the Interaction resource to fetch.
            webhook_ttid: The unique identifier for Interaction level webhook
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/Interactions/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str | None]("WebhookTtid", webhook_ttid)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1Interaction],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncFlexV1InteractionApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_interaction(
        self,
        channel: Any,
        *,
        routing: Any | None = None,
        interaction_context_sid: str | None = None,
        webhook_ttid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1Interaction, RawError]:
        """Create a new Interaction.

        Args:
            channel: The Interaction's channel.
            routing: The Interaction's routing logic.
            interaction_context_sid: The Interaction context sid is used for adding a context lookup sid
            webhook_ttid: The unique identifier for Interaction level webhook
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/Interactions"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[Any]("Channel", channel),
                    param[Any | None]("Routing", routing),
                    param[str | None]("InteractionContextSid", interaction_context_sid),
                    param[str | None]("WebhookTtid", webhook_ttid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1Interaction],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_interaction2(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FlexV1Interaction, RawError]:
        """Send a ``GET`` request.

        Args:
            sid: The SID of the Interaction resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/Interactions/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1Interaction],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_interaction(
        self, sid: str, *, webhook_ttid: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FlexV1Interaction, RawError]:
        """Updates an interaction.

        Args:
            sid: The SID of the Interaction resource to fetch.
            webhook_ttid: The unique identifier for Interaction level webhook
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/Interactions/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str | None]("WebhookTtid", webhook_ttid)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1Interaction],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
