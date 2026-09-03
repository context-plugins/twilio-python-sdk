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
    RFC3339DateTime,
    SecuredRawResponse,
    empty_response,
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.enums.session_enum_mode import SessionEnumModeOrStr
from ..models.enums.session_enum_status import SessionEnumStatusOrStr
from ..models.list_session_response import ListSessionResponse
from ..models.proxy_v1_service_session import ProxyV1ServiceSession
from ..server.server import Server


class ProxyV1Session:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ProxyV1SessionWithRawResponse(client, server, auth)

    def create_session(
        self,
        service_sid: str,
        *,
        unique_name: str | None = None,
        date_expiry: RFC3339DateTime | None = None,
        ttl: int | None = None,
        mode: SessionEnumModeOrStr | None = None,
        status: SessionEnumStatusOrStr | None = None,
        participants: list[Any] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProxyV1ServiceSession:
        """Create a new Session

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ resource.
            unique_name: An application-defined string that uniquely identifies the resource. This value must be 191
                characters or fewer in length and be unique. **This value should not have PII.**
            date_expiry: The `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ date when the Session should expire.
                If this is value is present, it overrides the ``ttl`` value.
            ttl: The time, in seconds, when the session will expire. The time is measured from the last Session create
                or the Session's last Interaction.
            mode: The Mode of the Session. Can be: ``message-only``, ``voice-only``, or ``voice-and-message``.
            status: The status of the Session. Can be: ``open``, ``in-progress``, ``closed``, ``failed``, or
                ``unknown``.
            participants: The Participant objects to include in the new session.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_session(
            service_sid,
            unique_name=unique_name,
            date_expiry=date_expiry,
            ttl=ttl,
            mode=mode,
            status=status,
            participants=participants,
            request_options=request_options,
        ).unwrap()

    def delete_session(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a specific Session.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resource to delete.
            sid: The Twilio-provided string that uniquely identifies the Session resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_session(service_sid, sid, request_options=request_options).unwrap()

    def fetch_session(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ProxyV1ServiceSession:
        """Fetch a specific Session.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the Session resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_session(service_sid, sid, request_options=request_options).unwrap()

    def list_session(
        self,
        service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSessionResponse:
        """Retrieve a list of all Sessions for the Service. A maximum of 100 records will be returned per page.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resource to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_session(
            service_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    def update_session(
        self,
        service_sid: str,
        sid: str,
        *,
        date_expiry: RFC3339DateTime | None = None,
        ttl: int | None = None,
        status: SessionEnumStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProxyV1ServiceSession:
        """Update a specific Session.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resource to update.
            sid: The Twilio-provided string that uniquely identifies the Session resource to update.
            date_expiry: The `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ date when the Session should expire.
                If this is value is present, it overrides the ``ttl`` value.
            ttl: The time, in seconds, when the session will expire. The time is measured from the last Session create
                or the Session's last Interaction.
            status: The status of the Session. Can be: ``open``, ``in-progress``, ``closed``, ``failed``, or
                ``unknown``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_session(
            service_sid, sid, date_expiry=date_expiry, ttl=ttl, status=status, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ProxyV1SessionWithRawResponse:
        return self._with_raw_response


class AsyncProxyV1Session:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncProxyV1SessionWithRawResponse(client, server, auth)

    async def create_session(
        self,
        service_sid: str,
        *,
        unique_name: str | None = None,
        date_expiry: RFC3339DateTime | None = None,
        ttl: int | None = None,
        mode: SessionEnumModeOrStr | None = None,
        status: SessionEnumStatusOrStr | None = None,
        participants: list[Any] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProxyV1ServiceSession:
        """Create a new Session

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ resource.
            unique_name: An application-defined string that uniquely identifies the resource. This value must be 191
                characters or fewer in length and be unique. **This value should not have PII.**
            date_expiry: The `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ date when the Session should expire.
                If this is value is present, it overrides the ``ttl`` value.
            ttl: The time, in seconds, when the session will expire. The time is measured from the last Session create
                or the Session's last Interaction.
            mode: The Mode of the Session. Can be: ``message-only``, ``voice-only``, or ``voice-and-message``.
            status: The status of the Session. Can be: ``open``, ``in-progress``, ``closed``, ``failed``, or
                ``unknown``.
            participants: The Participant objects to include in the new session.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_session(
                service_sid,
                unique_name=unique_name,
                date_expiry=date_expiry,
                ttl=ttl,
                mode=mode,
                status=status,
                participants=participants,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_session(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a specific Session.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resource to delete.
            sid: The Twilio-provided string that uniquely identifies the Session resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_session(service_sid, sid, request_options=request_options)
        ).unwrap()

    async def fetch_session(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ProxyV1ServiceSession:
        """Fetch a specific Session.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the Session resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_session(service_sid, sid, request_options=request_options)).unwrap()

    async def list_session(
        self,
        service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSessionResponse:
        """Retrieve a list of all Sessions for the Service. A maximum of 100 records will be returned per page.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resource to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_session(
                service_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    async def update_session(
        self,
        service_sid: str,
        sid: str,
        *,
        date_expiry: RFC3339DateTime | None = None,
        ttl: int | None = None,
        status: SessionEnumStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProxyV1ServiceSession:
        """Update a specific Session.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resource to update.
            sid: The Twilio-provided string that uniquely identifies the Session resource to update.
            date_expiry: The `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ date when the Session should expire.
                If this is value is present, it overrides the ``ttl`` value.
            ttl: The time, in seconds, when the session will expire. The time is measured from the last Session create
                or the Session's last Interaction.
            status: The status of the Session. Can be: ``open``, ``in-progress``, ``closed``, ``failed``, or
                ``unknown``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_session(
                service_sid, sid, date_expiry=date_expiry, ttl=ttl, status=status, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncProxyV1SessionWithRawResponse:
        return self._with_raw_response


class ProxyV1SessionWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_session(
        self,
        service_sid: str,
        *,
        unique_name: str | None = None,
        date_expiry: RFC3339DateTime | None = None,
        ttl: int | None = None,
        mode: SessionEnumModeOrStr | None = None,
        status: SessionEnumStatusOrStr | None = None,
        participants: list[Any] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProxyV1ServiceSession, RawError]:
        """Create a new Session

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ resource.
            unique_name: An application-defined string that uniquely identifies the resource. This value must be 191
                characters or fewer in length and be unique. **This value should not have PII.**
            date_expiry: The `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ date when the Session should expire.
                If this is value is present, it overrides the ``ttl`` value.
            ttl: The time, in seconds, when the session will expire. The time is measured from the last Session create
                or the Session's last Interaction.
            mode: The Mode of the Session. Can be: ``message-only``, ``voice-only``, or ``voice-and-message``.
            status: The status of the Session. Can be: ``open``, ``in-progress``, ``closed``, ``failed``, or
                ``unknown``.
            participants: The Participant objects to include in the new session.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/v1/Services/{ServiceSid}/Sessions"),
            path_params=[param[str]("ServiceSid", service_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("UniqueName", unique_name),
                    param[RFC3339DateTime | None]("DateExpiry", date_expiry),
                    param[int | None]("Ttl", ttl),
                    param[SessionEnumModeOrStr | None]("Mode", mode),
                    param[SessionEnumStatusOrStr | None]("Status", status),
                    param[list[Any] | None]("Participants", participants),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ProxyV1ServiceSession],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_session(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Session.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resource to delete.
            sid: The Twilio-provided string that uniquely identifies the Session resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default10("/v1/Services/{ServiceSid}/Sessions/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_session(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ProxyV1ServiceSession, RawError]:
        """Fetch a specific Session.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the Session resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default10("/v1/Services/{ServiceSid}/Sessions/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ProxyV1ServiceSession],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_session(
        self,
        service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSessionResponse, RawError]:
        """Retrieve a list of all Sessions for the Service. A maximum of 100 records will be returned per page.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resource to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default10("/v1/Services/{ServiceSid}/Sessions"),
            path_params=[param[str]("ServiceSid", service_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListSessionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_session(
        self,
        service_sid: str,
        sid: str,
        *,
        date_expiry: RFC3339DateTime | None = None,
        ttl: int | None = None,
        status: SessionEnumStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProxyV1ServiceSession, RawError]:
        """Update a specific Session.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resource to update.
            sid: The Twilio-provided string that uniquely identifies the Session resource to update.
            date_expiry: The `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ date when the Session should expire.
                If this is value is present, it overrides the ``ttl`` value.
            ttl: The time, in seconds, when the session will expire. The time is measured from the last Session create
                or the Session's last Interaction.
            status: The status of the Session. Can be: ``open``, ``in-progress``, ``closed``, ``failed``, or
                ``unknown``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/v1/Services/{ServiceSid}/Sessions/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[RFC3339DateTime | None]("DateExpiry", date_expiry),
                    param[int | None]("Ttl", ttl),
                    param[SessionEnumStatusOrStr | None]("Status", status),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ProxyV1ServiceSession],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncProxyV1SessionWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_session(
        self,
        service_sid: str,
        *,
        unique_name: str | None = None,
        date_expiry: RFC3339DateTime | None = None,
        ttl: int | None = None,
        mode: SessionEnumModeOrStr | None = None,
        status: SessionEnumStatusOrStr | None = None,
        participants: list[Any] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProxyV1ServiceSession, RawError]:
        """Create a new Session

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ resource.
            unique_name: An application-defined string that uniquely identifies the resource. This value must be 191
                characters or fewer in length and be unique. **This value should not have PII.**
            date_expiry: The `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ date when the Session should expire.
                If this is value is present, it overrides the ``ttl`` value.
            ttl: The time, in seconds, when the session will expire. The time is measured from the last Session create
                or the Session's last Interaction.
            mode: The Mode of the Session. Can be: ``message-only``, ``voice-only``, or ``voice-and-message``.
            status: The status of the Session. Can be: ``open``, ``in-progress``, ``closed``, ``failed``, or
                ``unknown``.
            participants: The Participant objects to include in the new session.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/v1/Services/{ServiceSid}/Sessions"),
            path_params=[param[str]("ServiceSid", service_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("UniqueName", unique_name),
                    param[RFC3339DateTime | None]("DateExpiry", date_expiry),
                    param[int | None]("Ttl", ttl),
                    param[SessionEnumModeOrStr | None]("Mode", mode),
                    param[SessionEnumStatusOrStr | None]("Status", status),
                    param[list[Any] | None]("Participants", participants),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ProxyV1ServiceSession],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_session(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Session.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resource to delete.
            sid: The Twilio-provided string that uniquely identifies the Session resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default10("/v1/Services/{ServiceSid}/Sessions/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_session(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ProxyV1ServiceSession, RawError]:
        """Fetch a specific Session.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the Session resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default10("/v1/Services/{ServiceSid}/Sessions/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ProxyV1ServiceSession],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_session(
        self,
        service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSessionResponse, RawError]:
        """Retrieve a list of all Sessions for the Service. A maximum of 100 records will be returned per page.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resource to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default10("/v1/Services/{ServiceSid}/Sessions"),
            path_params=[param[str]("ServiceSid", service_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListSessionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_session(
        self,
        service_sid: str,
        sid: str,
        *,
        date_expiry: RFC3339DateTime | None = None,
        ttl: int | None = None,
        status: SessionEnumStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProxyV1ServiceSession, RawError]:
        """Update a specific Session.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resource to update.
            sid: The Twilio-provided string that uniquely identifies the Session resource to update.
            date_expiry: The `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ date when the Session should expire.
                If this is value is present, it overrides the ``ttl`` value.
            ttl: The time, in seconds, when the session will expire. The time is measured from the last Session create
                or the Session's last Interaction.
            status: The status of the Session. Can be: ``open``, ``in-progress``, ``closed``, ``failed``, or
                ``unknown``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/v1/Services/{ServiceSid}/Sessions/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[RFC3339DateTime | None]("DateExpiry", date_expiry),
                    param[int | None]("Ttl", ttl),
                    param[SessionEnumStatusOrStr | None]("Status", status),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ProxyV1ServiceSession],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
