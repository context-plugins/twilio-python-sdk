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
from ..models.flex_v1_interaction_interaction_channel_interaction_channel_invite import (
    FlexV1InteractionInteractionChannelInteractionChannelInvite,
)
from ..models.list_interaction_channel_invite_response import ListInteractionChannelInviteResponse
from ..server.server import Server


class FlexV1InteractionChannelInvite:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FlexV1InteractionChannelInviteWithRawResponse(client, server, auth)

    def create_interaction_channel_invite(
        self,
        interaction_sid: str,
        channel_sid: str,
        routing: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1InteractionInteractionChannelInteractionChannelInvite:
        """Invite an Agent or a TaskQueue to a Channel.

        Args:
            interaction_sid: The Interaction SID for this Channel.
            channel_sid: The Channel SID for this Invite.
            routing: The Interaction's routing logic.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_interaction_channel_invite(
            interaction_sid, channel_sid, routing, request_options=request_options
        ).unwrap()

    def list_interaction_channel_invite(
        self,
        interaction_sid: str,
        channel_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInteractionChannelInviteResponse:
        """List all Invites for a Channel.

        Args:
            interaction_sid: The Interaction SID for this Channel.
            channel_sid: The Channel SID for this Participant.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_interaction_channel_invite(
            interaction_sid,
            channel_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> FlexV1InteractionChannelInviteWithRawResponse:
        return self._with_raw_response


class AsyncFlexV1InteractionChannelInvite:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFlexV1InteractionChannelInviteWithRawResponse(client, server, auth)

    async def create_interaction_channel_invite(
        self,
        interaction_sid: str,
        channel_sid: str,
        routing: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1InteractionInteractionChannelInteractionChannelInvite:
        """Invite an Agent or a TaskQueue to a Channel.

        Args:
            interaction_sid: The Interaction SID for this Channel.
            channel_sid: The Channel SID for this Invite.
            routing: The Interaction's routing logic.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_interaction_channel_invite(
                interaction_sid, channel_sid, routing, request_options=request_options
            )
        ).unwrap()

    async def list_interaction_channel_invite(
        self,
        interaction_sid: str,
        channel_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInteractionChannelInviteResponse:
        """List all Invites for a Channel.

        Args:
            interaction_sid: The Interaction SID for this Channel.
            channel_sid: The Channel SID for this Participant.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_interaction_channel_invite(
                interaction_sid,
                channel_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncFlexV1InteractionChannelInviteWithRawResponse:
        return self._with_raw_response


class FlexV1InteractionChannelInviteWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_interaction_channel_invite(
        self,
        interaction_sid: str,
        channel_sid: str,
        routing: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1InteractionInteractionChannelInteractionChannelInvite, RawError]:
        """Invite an Agent or a TaskQueue to a Channel.

        Args:
            interaction_sid: The Interaction SID for this Channel.
            channel_sid: The Channel SID for this Invite.
            routing: The Interaction's routing logic.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/Interactions/{InteractionSid}/Channels/{ChannelSid}/Invites"),
            path_params=[param[str]("InteractionSid", interaction_sid), param[str]("ChannelSid", channel_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[Any]("Routing", routing)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InteractionInteractionChannelInteractionChannelInvite],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_interaction_channel_invite(
        self,
        interaction_sid: str,
        channel_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInteractionChannelInviteResponse, RawError]:
        """List all Invites for a Channel.

        Args:
            interaction_sid: The Interaction SID for this Channel.
            channel_sid: The Channel SID for this Participant.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/Interactions/{InteractionSid}/Channels/{ChannelSid}/Invites"),
            path_params=[param[str]("InteractionSid", interaction_sid), param[str]("ChannelSid", channel_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListInteractionChannelInviteResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncFlexV1InteractionChannelInviteWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_interaction_channel_invite(
        self,
        interaction_sid: str,
        channel_sid: str,
        routing: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1InteractionInteractionChannelInteractionChannelInvite, RawError]:
        """Invite an Agent or a TaskQueue to a Channel.

        Args:
            interaction_sid: The Interaction SID for this Channel.
            channel_sid: The Channel SID for this Invite.
            routing: The Interaction's routing logic.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/Interactions/{InteractionSid}/Channels/{ChannelSid}/Invites"),
            path_params=[param[str]("InteractionSid", interaction_sid), param[str]("ChannelSid", channel_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[Any]("Routing", routing)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InteractionInteractionChannelInteractionChannelInvite],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_interaction_channel_invite(
        self,
        interaction_sid: str,
        channel_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInteractionChannelInviteResponse, RawError]:
        """List all Invites for a Channel.

        Args:
            interaction_sid: The Interaction SID for this Channel.
            channel_sid: The Channel SID for this Participant.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/Interactions/{InteractionSid}/Channels/{ChannelSid}/Invites"),
            path_params=[param[str]("InteractionSid", interaction_sid), param[str]("ChannelSid", channel_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListInteractionChannelInviteResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
