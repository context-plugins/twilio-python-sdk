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
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.list_message_interaction_response import ListMessageInteractionResponse
from ..models.proxy_v1_service_session_participant_message_interaction import (
    ProxyV1ServiceSessionParticipantMessageInteraction,
)
from ..server.server import Server


class ProxyV1MessageInteraction:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ProxyV1MessageInteractionWithRawResponse(client, server, auth)

    def create_message_interaction(
        self,
        service_sid: str,
        session_sid: str,
        participant_sid: str,
        *,
        body: str | None = None,
        media_url: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProxyV1ServiceSessionParticipantMessageInteraction:
        """Create a new message Interaction to send directly from your system to one `Participant
        <https://www.twilio.com/docs/proxy/api/participant>`__. The ``inbound`` properties for the Interaction will
        always be empty.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ resource.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ resource.
            participant_sid: The SID of the `Participant <https://www.twilio.com/docs/proxy/api/participant>`__
                resource.
            body: The message to send to the participant
            media_url: Reserved. Not currently supported.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_message_interaction(
            service_sid, session_sid, participant_sid, body=body, media_url=media_url, request_options=request_options
        ).unwrap()

    def fetch_message_interaction(
        self,
        service_sid: str,
        session_sid: str,
        participant_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProxyV1ServiceSessionParticipantMessageInteraction:
        """Send a ``GET`` request.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resource to fetch.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ of the
                resource to fetch.
            participant_sid: The SID of the `Participant <https://www.twilio.com/docs/proxy/api/participant>`__
                resource.
            sid: The Twilio-provided string that uniquely identifies the MessageInteraction resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_message_interaction(
            service_sid, session_sid, participant_sid, sid, request_options=request_options
        ).unwrap()

    def list_message_interaction(
        self,
        service_sid: str,
        session_sid: str,
        participant_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListMessageInteractionResponse:
        """Send a ``GET`` request.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ to read the
                resources from.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ to read the
                resources from.
            participant_sid: The SID of the `Participant <https://www.twilio.com/docs/proxy/api/participant>`__ to read
                the resources from.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_message_interaction(
            service_sid,
            session_sid,
            participant_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> ProxyV1MessageInteractionWithRawResponse:
        return self._with_raw_response


class AsyncProxyV1MessageInteraction:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncProxyV1MessageInteractionWithRawResponse(client, server, auth)

    async def create_message_interaction(
        self,
        service_sid: str,
        session_sid: str,
        participant_sid: str,
        *,
        body: str | None = None,
        media_url: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProxyV1ServiceSessionParticipantMessageInteraction:
        """Create a new message Interaction to send directly from your system to one `Participant
        <https://www.twilio.com/docs/proxy/api/participant>`__. The ``inbound`` properties for the Interaction will
        always be empty.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ resource.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ resource.
            participant_sid: The SID of the `Participant <https://www.twilio.com/docs/proxy/api/participant>`__
                resource.
            body: The message to send to the participant
            media_url: Reserved. Not currently supported.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_message_interaction(
                service_sid,
                session_sid,
                participant_sid,
                body=body,
                media_url=media_url,
                request_options=request_options,
            )
        ).unwrap()

    async def fetch_message_interaction(
        self,
        service_sid: str,
        session_sid: str,
        participant_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProxyV1ServiceSessionParticipantMessageInteraction:
        """Send a ``GET`` request.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resource to fetch.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ of the
                resource to fetch.
            participant_sid: The SID of the `Participant <https://www.twilio.com/docs/proxy/api/participant>`__
                resource.
            sid: The Twilio-provided string that uniquely identifies the MessageInteraction resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_message_interaction(
                service_sid, session_sid, participant_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def list_message_interaction(
        self,
        service_sid: str,
        session_sid: str,
        participant_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListMessageInteractionResponse:
        """Send a ``GET`` request.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ to read the
                resources from.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ to read the
                resources from.
            participant_sid: The SID of the `Participant <https://www.twilio.com/docs/proxy/api/participant>`__ to read
                the resources from.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_message_interaction(
                service_sid,
                session_sid,
                participant_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncProxyV1MessageInteractionWithRawResponse:
        return self._with_raw_response


class ProxyV1MessageInteractionWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_message_interaction(
        self,
        service_sid: str,
        session_sid: str,
        participant_sid: str,
        *,
        body: str | None = None,
        media_url: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProxyV1ServiceSessionParticipantMessageInteraction, RawError]:
        """Create a new message Interaction to send directly from your system to one `Participant
        <https://www.twilio.com/docs/proxy/api/participant>`__. The ``inbound`` properties for the Interaction will
        always be empty.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ resource.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ resource.
            participant_sid: The SID of the `Participant <https://www.twilio.com/docs/proxy/api/participant>`__
                resource.
            body: The message to send to the participant
            media_url: Reserved. Not currently supported.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default10(
                "/v1/Services/{ServiceSid}/Sessions/{SessionSid}/Participants/{ParticipantSid}/MessageInteractions"
            ),
            path_params=[
                param[str]("ServiceSid", service_sid),
                param[str]("SessionSid", session_sid),
                param[str]("ParticipantSid", participant_sid),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str | None]("Body", body), param[list[str] | None]("MediaUrl", media_url)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ProxyV1ServiceSessionParticipantMessageInteraction],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_message_interaction(
        self,
        service_sid: str,
        session_sid: str,
        participant_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProxyV1ServiceSessionParticipantMessageInteraction, RawError]:
        """Send a ``GET`` request.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resource to fetch.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ of the
                resource to fetch.
            participant_sid: The SID of the `Participant <https://www.twilio.com/docs/proxy/api/participant>`__
                resource.
            sid: The Twilio-provided string that uniquely identifies the MessageInteraction resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default10(
                "/v1/Services/{ServiceSid}/Sessions/{SessionSid}/Participants/{ParticipantSid}/MessageInteractions/{Sid}",
            ),
            path_params=[
                param[str]("ServiceSid", service_sid),
                param[str]("SessionSid", session_sid),
                param[str]("ParticipantSid", participant_sid),
                param[str]("Sid", sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ProxyV1ServiceSessionParticipantMessageInteraction],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_message_interaction(
        self,
        service_sid: str,
        session_sid: str,
        participant_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListMessageInteractionResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ to read the
                resources from.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ to read the
                resources from.
            participant_sid: The SID of the `Participant <https://www.twilio.com/docs/proxy/api/participant>`__ to read
                the resources from.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default10(
                "/v1/Services/{ServiceSid}/Sessions/{SessionSid}/Participants/{ParticipantSid}/MessageInteractions"
            ),
            path_params=[
                param[str]("ServiceSid", service_sid),
                param[str]("SessionSid", session_sid),
                param[str]("ParticipantSid", participant_sid),
            ],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListMessageInteractionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncProxyV1MessageInteractionWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_message_interaction(
        self,
        service_sid: str,
        session_sid: str,
        participant_sid: str,
        *,
        body: str | None = None,
        media_url: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProxyV1ServiceSessionParticipantMessageInteraction, RawError]:
        """Create a new message Interaction to send directly from your system to one `Participant
        <https://www.twilio.com/docs/proxy/api/participant>`__. The ``inbound`` properties for the Interaction will
        always be empty.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ resource.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ resource.
            participant_sid: The SID of the `Participant <https://www.twilio.com/docs/proxy/api/participant>`__
                resource.
            body: The message to send to the participant
            media_url: Reserved. Not currently supported.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default10(
                "/v1/Services/{ServiceSid}/Sessions/{SessionSid}/Participants/{ParticipantSid}/MessageInteractions"
            ),
            path_params=[
                param[str]("ServiceSid", service_sid),
                param[str]("SessionSid", session_sid),
                param[str]("ParticipantSid", participant_sid),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str | None]("Body", body), param[list[str] | None]("MediaUrl", media_url)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ProxyV1ServiceSessionParticipantMessageInteraction],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_message_interaction(
        self,
        service_sid: str,
        session_sid: str,
        participant_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProxyV1ServiceSessionParticipantMessageInteraction, RawError]:
        """Send a ``GET`` request.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resource to fetch.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ of the
                resource to fetch.
            participant_sid: The SID of the `Participant <https://www.twilio.com/docs/proxy/api/participant>`__
                resource.
            sid: The Twilio-provided string that uniquely identifies the MessageInteraction resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default10(
                "/v1/Services/{ServiceSid}/Sessions/{SessionSid}/Participants/{ParticipantSid}/MessageInteractions/{Sid}",
            ),
            path_params=[
                param[str]("ServiceSid", service_sid),
                param[str]("SessionSid", session_sid),
                param[str]("ParticipantSid", participant_sid),
                param[str]("Sid", sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ProxyV1ServiceSessionParticipantMessageInteraction],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_message_interaction(
        self,
        service_sid: str,
        session_sid: str,
        participant_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListMessageInteractionResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ to read the
                resources from.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ to read the
                resources from.
            participant_sid: The SID of the `Participant <https://www.twilio.com/docs/proxy/api/participant>`__ to read
                the resources from.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default10(
                "/v1/Services/{ServiceSid}/Sessions/{SessionSid}/Participants/{ParticipantSid}/MessageInteractions"
            ),
            path_params=[
                param[str]("ServiceSid", service_sid),
                param[str]("SessionSid", session_sid),
                param[str]("ParticipantSid", participant_sid),
            ],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListMessageInteractionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
