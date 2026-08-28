from __future__ import annotations

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
from ..models.list_participant_response1 import ListParticipantResponse1
from ..models.proxy_v1_service_session_participant import ProxyV1ServiceSessionParticipant
from ..server.server import Server


class ProxyV1Participant:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ProxyV1ParticipantWithRawResponse(client, server, auth)

    def create_participant2(
        self,
        service_sid: str,
        session_sid: str,
        identifier: str,
        *,
        friendly_name: str | None = None,
        proxy_identifier: str | None = None,
        proxy_identifier_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProxyV1ServiceSessionParticipant:
        """Add a new Participant to the Session

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ resource.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ resource.
            identifier: The phone number of the Participant.
            friendly_name: The string that you assigned to describe the participant. This value must be 255 characters
                or fewer. **This value should not have PII.**
            proxy_identifier: The proxy phone number to use for the Participant. If not specified, Proxy will select a
                number from the pool.
            proxy_identifier_sid: The SID of the Proxy Identifier to assign to the Participant.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_participant2(
            service_sid,
            session_sid,
            identifier,
            friendly_name=friendly_name,
            proxy_identifier=proxy_identifier,
            proxy_identifier_sid=proxy_identifier_sid,
            request_options=request_options,
        ).unwrap()

    def delete_participant2(
        self, service_sid: str, session_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a specific Participant. This is a soft-delete. The participant remains associated with the session and
        cannot be re-added. Participants are only permanently deleted when the `Session
        <https://www.twilio.com/docs/proxy/api/session>`__ is deleted.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resource to delete.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ of the
                resource to delete.
            sid: The Twilio-provided string that uniquely identifies the Participant resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_participant2(
            service_sid, session_sid, sid, request_options=request_options
        ).unwrap()

    def fetch_participant3(
        self, service_sid: str, session_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ProxyV1ServiceSessionParticipant:
        """Fetch a specific Participant.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resource to fetch.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ of the
                resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the Participant resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_participant3(
            service_sid, session_sid, sid, request_options=request_options
        ).unwrap()

    def list_participant2(
        self,
        service_sid: str,
        session_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListParticipantResponse1:
        """Retrieve a list of all Participants in a Session.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resources to read.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ of the
                resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_participant2(
            service_sid,
            session_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> ProxyV1ParticipantWithRawResponse:
        return self._with_raw_response


class AsyncProxyV1Participant:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncProxyV1ParticipantWithRawResponse(client, server, auth)

    async def create_participant2(
        self,
        service_sid: str,
        session_sid: str,
        identifier: str,
        *,
        friendly_name: str | None = None,
        proxy_identifier: str | None = None,
        proxy_identifier_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProxyV1ServiceSessionParticipant:
        """Add a new Participant to the Session

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ resource.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ resource.
            identifier: The phone number of the Participant.
            friendly_name: The string that you assigned to describe the participant. This value must be 255 characters
                or fewer. **This value should not have PII.**
            proxy_identifier: The proxy phone number to use for the Participant. If not specified, Proxy will select a
                number from the pool.
            proxy_identifier_sid: The SID of the Proxy Identifier to assign to the Participant.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_participant2(
                service_sid,
                session_sid,
                identifier,
                friendly_name=friendly_name,
                proxy_identifier=proxy_identifier,
                proxy_identifier_sid=proxy_identifier_sid,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_participant2(
        self, service_sid: str, session_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a specific Participant. This is a soft-delete. The participant remains associated with the session and
        cannot be re-added. Participants are only permanently deleted when the `Session
        <https://www.twilio.com/docs/proxy/api/session>`__ is deleted.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resource to delete.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ of the
                resource to delete.
            sid: The Twilio-provided string that uniquely identifies the Participant resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_participant2(
                service_sid, session_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def fetch_participant3(
        self, service_sid: str, session_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ProxyV1ServiceSessionParticipant:
        """Fetch a specific Participant.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resource to fetch.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ of the
                resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the Participant resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_participant3(
                service_sid, session_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def list_participant2(
        self,
        service_sid: str,
        session_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListParticipantResponse1:
        """Retrieve a list of all Participants in a Session.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resources to read.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ of the
                resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_participant2(
                service_sid,
                session_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncProxyV1ParticipantWithRawResponse:
        return self._with_raw_response


class ProxyV1ParticipantWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_participant2(
        self,
        service_sid: str,
        session_sid: str,
        identifier: str,
        *,
        friendly_name: str | None = None,
        proxy_identifier: str | None = None,
        proxy_identifier_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProxyV1ServiceSessionParticipant, RawError]:
        """Add a new Participant to the Session

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ resource.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ resource.
            identifier: The phone number of the Participant.
            friendly_name: The string that you assigned to describe the participant. This value must be 255 characters
                or fewer. **This value should not have PII.**
            proxy_identifier: The proxy phone number to use for the Participant. If not specified, Proxy will select a
                number from the pool.
            proxy_identifier_sid: The SID of the Proxy Identifier to assign to the Participant.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/v1/Services/{ServiceSid}/Sessions/{SessionSid}/Participants"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("SessionSid", session_sid)],
            body=form_body(
                [
                    param[str]("Identifier", identifier),
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("ProxyIdentifier", proxy_identifier),
                    param[str | None]("ProxyIdentifierSid", proxy_identifier_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ProxyV1ServiceSessionParticipant],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_participant2(
        self, service_sid: str, session_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Participant. This is a soft-delete. The participant remains associated with the session and
        cannot be re-added. Participants are only permanently deleted when the `Session
        <https://www.twilio.com/docs/proxy/api/session>`__ is deleted.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resource to delete.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ of the
                resource to delete.
            sid: The Twilio-provided string that uniquely identifies the Participant resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default10("/v1/Services/{ServiceSid}/Sessions/{SessionSid}/Participants/{Sid}"),
            path_params=[
                param[str]("ServiceSid", service_sid), param[str]("SessionSid", session_sid), param[str]("Sid", sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_participant3(
        self, service_sid: str, session_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ProxyV1ServiceSessionParticipant, RawError]:
        """Fetch a specific Participant.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resource to fetch.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ of the
                resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the Participant resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default10("/v1/Services/{ServiceSid}/Sessions/{SessionSid}/Participants/{Sid}"),
            path_params=[
                param[str]("ServiceSid", service_sid), param[str]("SessionSid", session_sid), param[str]("Sid", sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ProxyV1ServiceSessionParticipant],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_participant2(
        self,
        service_sid: str,
        session_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListParticipantResponse1, RawError]:
        """Retrieve a list of all Participants in a Session.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resources to read.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ of the
                resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default10("/v1/Services/{ServiceSid}/Sessions/{SessionSid}/Participants"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("SessionSid", session_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListParticipantResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncProxyV1ParticipantWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_participant2(
        self,
        service_sid: str,
        session_sid: str,
        identifier: str,
        *,
        friendly_name: str | None = None,
        proxy_identifier: str | None = None,
        proxy_identifier_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProxyV1ServiceSessionParticipant, RawError]:
        """Add a new Participant to the Session

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ resource.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ resource.
            identifier: The phone number of the Participant.
            friendly_name: The string that you assigned to describe the participant. This value must be 255 characters
                or fewer. **This value should not have PII.**
            proxy_identifier: The proxy phone number to use for the Participant. If not specified, Proxy will select a
                number from the pool.
            proxy_identifier_sid: The SID of the Proxy Identifier to assign to the Participant.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/v1/Services/{ServiceSid}/Sessions/{SessionSid}/Participants"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("SessionSid", session_sid)],
            body=form_body(
                [
                    param[str]("Identifier", identifier),
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("ProxyIdentifier", proxy_identifier),
                    param[str | None]("ProxyIdentifierSid", proxy_identifier_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ProxyV1ServiceSessionParticipant],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_participant2(
        self, service_sid: str, session_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Participant. This is a soft-delete. The participant remains associated with the session and
        cannot be re-added. Participants are only permanently deleted when the `Session
        <https://www.twilio.com/docs/proxy/api/session>`__ is deleted.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resource to delete.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ of the
                resource to delete.
            sid: The Twilio-provided string that uniquely identifies the Participant resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default10("/v1/Services/{ServiceSid}/Sessions/{SessionSid}/Participants/{Sid}"),
            path_params=[
                param[str]("ServiceSid", service_sid), param[str]("SessionSid", session_sid), param[str]("Sid", sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_participant3(
        self, service_sid: str, session_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ProxyV1ServiceSessionParticipant, RawError]:
        """Fetch a specific Participant.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resource to fetch.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ of the
                resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the Participant resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default10("/v1/Services/{ServiceSid}/Sessions/{SessionSid}/Participants/{Sid}"),
            path_params=[
                param[str]("ServiceSid", service_sid), param[str]("SessionSid", session_sid), param[str]("Sid", sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ProxyV1ServiceSessionParticipant],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_participant2(
        self,
        service_sid: str,
        session_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListParticipantResponse1, RawError]:
        """Retrieve a list of all Participants in a Session.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resources to read.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ of the
                resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default10("/v1/Services/{ServiceSid}/Sessions/{SessionSid}/Participants"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("SessionSid", session_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListParticipantResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
