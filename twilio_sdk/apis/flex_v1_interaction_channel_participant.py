from __future__ import annotations

from typing import Any

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
from ..models.enums.interaction_channel_participant_enum_status import InteractionChannelParticipantEnumStatusOrStr
from ..models.enums.interaction_channel_participant_enum_type import InteractionChannelParticipantEnumTypeOrStr
from ..models.flex_v1_interaction_interaction_channel_interaction_channel_participant import (
    FlexV1InteractionInteractionChannelInteractionChannelParticipant,
)
from ..models.list_interaction_channel_participant_response import ListInteractionChannelParticipantResponse
from ..server.server import Server


class FlexV1InteractionChannelParticipant:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FlexV1InteractionChannelParticipantWithRawResponse(client, server, auth)

    def create_interaction_channel_participant(
        self,
        interaction_sid: str,
        channel_sid: str,
        type_: InteractionChannelParticipantEnumTypeOrStr,
        media_properties: Any,
        *,
        routing_properties: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1InteractionInteractionChannelInteractionChannelParticipant:
        """Add a Participant to a Channel.

        Args:
            interaction_sid: The Interaction Sid for the new Channel Participant.
            channel_sid: The Channel Sid for the new Channel Participant.
            type_: Participant type. Can be: ``agent``, ``customer``, ``supervisor``, ``external``, ``unknown``
            media_properties: JSON representing the Media Properties for the new Participant.
            routing_properties: Object representing the Routing Properties for the new Participant.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_interaction_channel_participant(
            interaction_sid,
            channel_sid,
            type_,
            media_properties,
            routing_properties=routing_properties,
            request_options=request_options,
        ).unwrap()

    def list_interaction_channel_participant(
        self,
        interaction_sid: str,
        channel_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInteractionChannelParticipantResponse:
        """List all Participants for a Channel.

        Args:
            interaction_sid: The Interaction Sid for this channel.
            channel_sid: The Channel Sid for this Participant.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_interaction_channel_participant(
            interaction_sid,
            channel_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_interaction_channel_participant(
        self,
        interaction_sid: str,
        channel_sid: str,
        sid: str,
        status: InteractionChannelParticipantEnumStatusOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1InteractionInteractionChannelInteractionChannelParticipant:
        """Update an existing Channel Participant.

        Args:
            interaction_sid: The Interaction Sid for this channel.
            channel_sid: The Channel Sid for this Participant.
            sid: The unique string created by Twilio to identify an Interaction Channel resource.
            status: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_interaction_channel_participant(
            interaction_sid, channel_sid, sid, status, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> FlexV1InteractionChannelParticipantWithRawResponse:
        return self._with_raw_response


class AsyncFlexV1InteractionChannelParticipant:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFlexV1InteractionChannelParticipantWithRawResponse(client, server, auth)

    async def create_interaction_channel_participant(
        self,
        interaction_sid: str,
        channel_sid: str,
        type_: InteractionChannelParticipantEnumTypeOrStr,
        media_properties: Any,
        *,
        routing_properties: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1InteractionInteractionChannelInteractionChannelParticipant:
        """Add a Participant to a Channel.

        Args:
            interaction_sid: The Interaction Sid for the new Channel Participant.
            channel_sid: The Channel Sid for the new Channel Participant.
            type_: Participant type. Can be: ``agent``, ``customer``, ``supervisor``, ``external``, ``unknown``
            media_properties: JSON representing the Media Properties for the new Participant.
            routing_properties: Object representing the Routing Properties for the new Participant.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_interaction_channel_participant(
                interaction_sid,
                channel_sid,
                type_,
                media_properties,
                routing_properties=routing_properties,
                request_options=request_options,
            )
        ).unwrap()

    async def list_interaction_channel_participant(
        self,
        interaction_sid: str,
        channel_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInteractionChannelParticipantResponse:
        """List all Participants for a Channel.

        Args:
            interaction_sid: The Interaction Sid for this channel.
            channel_sid: The Channel Sid for this Participant.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_interaction_channel_participant(
                interaction_sid,
                channel_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_interaction_channel_participant(
        self,
        interaction_sid: str,
        channel_sid: str,
        sid: str,
        status: InteractionChannelParticipantEnumStatusOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1InteractionInteractionChannelInteractionChannelParticipant:
        """Update an existing Channel Participant.

        Args:
            interaction_sid: The Interaction Sid for this channel.
            channel_sid: The Channel Sid for this Participant.
            sid: The unique string created by Twilio to identify an Interaction Channel resource.
            status: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_interaction_channel_participant(
                interaction_sid, channel_sid, sid, status, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncFlexV1InteractionChannelParticipantWithRawResponse:
        return self._with_raw_response


class FlexV1InteractionChannelParticipantWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_interaction_channel_participant(
        self,
        interaction_sid: str,
        channel_sid: str,
        type_: InteractionChannelParticipantEnumTypeOrStr,
        media_properties: Any,
        *,
        routing_properties: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1InteractionInteractionChannelInteractionChannelParticipant, RawError]:
        """Add a Participant to a Channel.

        Args:
            interaction_sid: The Interaction Sid for the new Channel Participant.
            channel_sid: The Channel Sid for the new Channel Participant.
            type_: Participant type. Can be: ``agent``, ``customer``, ``supervisor``, ``external``, ``unknown``
            media_properties: JSON representing the Media Properties for the new Participant.
            routing_properties: Object representing the Routing Properties for the new Participant.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/Interactions/{InteractionSid}/Channels/{ChannelSid}/Participants"),
            path_params=[param[str]("InteractionSid", interaction_sid), param[str]("ChannelSid", channel_sid)],
            body=form_body(
                [
                    param[InteractionChannelParticipantEnumTypeOrStr]("Type", type_),
                    param[Any]("MediaProperties", media_properties),
                    param[Any | None]("RoutingProperties", routing_properties),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InteractionInteractionChannelInteractionChannelParticipant],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_interaction_channel_participant(
        self,
        interaction_sid: str,
        channel_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInteractionChannelParticipantResponse, RawError]:
        """List all Participants for a Channel.

        Args:
            interaction_sid: The Interaction Sid for this channel.
            channel_sid: The Channel Sid for this Participant.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/Interactions/{InteractionSid}/Channels/{ChannelSid}/Participants"),
            path_params=[param[str]("InteractionSid", interaction_sid), param[str]("ChannelSid", channel_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListInteractionChannelParticipantResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_interaction_channel_participant(
        self,
        interaction_sid: str,
        channel_sid: str,
        sid: str,
        status: InteractionChannelParticipantEnumStatusOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1InteractionInteractionChannelInteractionChannelParticipant, RawError]:
        """Update an existing Channel Participant.

        Args:
            interaction_sid: The Interaction Sid for this channel.
            channel_sid: The Channel Sid for this Participant.
            sid: The unique string created by Twilio to identify an Interaction Channel resource.
            status: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13(
                "/v1/Interactions/{InteractionSid}/Channels/{ChannelSid}/Participants/{Sid}"
            ),
            path_params=[
                param[str]("InteractionSid", interaction_sid),
                param[str]("ChannelSid", channel_sid),
                param[str]("Sid", sid),
            ],
            body=form_body([param[InteractionChannelParticipantEnumStatusOrStr]("Status", status)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InteractionInteractionChannelInteractionChannelParticipant],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncFlexV1InteractionChannelParticipantWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def create_interaction_channel_participant(
        self,
        interaction_sid: str,
        channel_sid: str,
        type_: InteractionChannelParticipantEnumTypeOrStr,
        media_properties: Any,
        *,
        routing_properties: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1InteractionInteractionChannelInteractionChannelParticipant, RawError]:
        """Add a Participant to a Channel.

        Args:
            interaction_sid: The Interaction Sid for the new Channel Participant.
            channel_sid: The Channel Sid for the new Channel Participant.
            type_: Participant type. Can be: ``agent``, ``customer``, ``supervisor``, ``external``, ``unknown``
            media_properties: JSON representing the Media Properties for the new Participant.
            routing_properties: Object representing the Routing Properties for the new Participant.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/Interactions/{InteractionSid}/Channels/{ChannelSid}/Participants"),
            path_params=[param[str]("InteractionSid", interaction_sid), param[str]("ChannelSid", channel_sid)],
            body=form_body(
                [
                    param[InteractionChannelParticipantEnumTypeOrStr]("Type", type_),
                    param[Any]("MediaProperties", media_properties),
                    param[Any | None]("RoutingProperties", routing_properties),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InteractionInteractionChannelInteractionChannelParticipant],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_interaction_channel_participant(
        self,
        interaction_sid: str,
        channel_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInteractionChannelParticipantResponse, RawError]:
        """List all Participants for a Channel.

        Args:
            interaction_sid: The Interaction Sid for this channel.
            channel_sid: The Channel Sid for this Participant.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/Interactions/{InteractionSid}/Channels/{ChannelSid}/Participants"),
            path_params=[param[str]("InteractionSid", interaction_sid), param[str]("ChannelSid", channel_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListInteractionChannelParticipantResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_interaction_channel_participant(
        self,
        interaction_sid: str,
        channel_sid: str,
        sid: str,
        status: InteractionChannelParticipantEnumStatusOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1InteractionInteractionChannelInteractionChannelParticipant, RawError]:
        """Update an existing Channel Participant.

        Args:
            interaction_sid: The Interaction Sid for this channel.
            channel_sid: The Channel Sid for this Participant.
            sid: The unique string created by Twilio to identify an Interaction Channel resource.
            status: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13(
                "/v1/Interactions/{InteractionSid}/Channels/{ChannelSid}/Participants/{Sid}"
            ),
            path_params=[
                param[str]("InteractionSid", interaction_sid),
                param[str]("ChannelSid", channel_sid),
                param[str]("Sid", sid),
            ],
            body=form_body([param[InteractionChannelParticipantEnumStatusOrStr]("Status", status)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InteractionInteractionChannelInteractionChannelParticipant],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
