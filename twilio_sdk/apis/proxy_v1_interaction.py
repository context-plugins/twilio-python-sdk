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
    json_decoder,
    param,
    raw_error_response,
)
from ..models.list_interaction_response import ListInteractionResponse
from ..models.proxy_v1_service_session_interaction import ProxyV1ServiceSessionInteraction
from ..server.server import Server


class ProxyV1Interaction:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ProxyV1InteractionWithRawResponse(client, server, auth)

    def delete_interaction(
        self, service_sid: str, session_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a specific Interaction.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resource to delete.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ of the
                resource to delete.
            sid: The Twilio-provided string that uniquely identifies the Interaction resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_interaction(
            service_sid, session_sid, sid, request_options=request_options
        ).unwrap()

    def fetch_interaction(
        self, service_sid: str, session_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ProxyV1ServiceSessionInteraction:
        """Retrieve a list of Interactions for a given `Session <https://www.twilio.com/docs/proxy/api/session>`__.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resource to fetch.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ of the
                resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the Interaction resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_interaction(
            service_sid, session_sid, sid, request_options=request_options
        ).unwrap()

    def list_interaction(
        self,
        service_sid: str,
        session_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInteractionResponse:
        """Retrieve a list of all Interactions for a Session. A maximum of 100 records will be returned per page.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ to read the
                resources from.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ to read the
                resources from.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_interaction(
            service_sid,
            session_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> ProxyV1InteractionWithRawResponse:
        return self._with_raw_response


class AsyncProxyV1Interaction:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncProxyV1InteractionWithRawResponse(client, server, auth)

    async def delete_interaction(
        self, service_sid: str, session_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a specific Interaction.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resource to delete.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ of the
                resource to delete.
            sid: The Twilio-provided string that uniquely identifies the Interaction resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_interaction(
                service_sid, session_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def fetch_interaction(
        self, service_sid: str, session_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ProxyV1ServiceSessionInteraction:
        """Retrieve a list of Interactions for a given `Session <https://www.twilio.com/docs/proxy/api/session>`__.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resource to fetch.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ of the
                resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the Interaction resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_interaction(
                service_sid, session_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def list_interaction(
        self,
        service_sid: str,
        session_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInteractionResponse:
        """Retrieve a list of all Interactions for a Session. A maximum of 100 records will be returned per page.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ to read the
                resources from.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ to read the
                resources from.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_interaction(
                service_sid,
                session_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncProxyV1InteractionWithRawResponse:
        return self._with_raw_response


class ProxyV1InteractionWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_interaction(
        self, service_sid: str, session_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Interaction.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resource to delete.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ of the
                resource to delete.
            sid: The Twilio-provided string that uniquely identifies the Interaction resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default10("/v1/Services/{ServiceSid}/Sessions/{SessionSid}/Interactions/{Sid}"),
            path_params=[
                param[str]("ServiceSid", service_sid), param[str]("SessionSid", session_sid), param[str]("Sid", sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_interaction(
        self, service_sid: str, session_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ProxyV1ServiceSessionInteraction, RawError]:
        """Retrieve a list of Interactions for a given `Session <https://www.twilio.com/docs/proxy/api/session>`__.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resource to fetch.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ of the
                resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the Interaction resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default10("/v1/Services/{ServiceSid}/Sessions/{SessionSid}/Interactions/{Sid}"),
            path_params=[
                param[str]("ServiceSid", service_sid), param[str]("SessionSid", session_sid), param[str]("Sid", sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ProxyV1ServiceSessionInteraction],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_interaction(
        self,
        service_sid: str,
        session_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInteractionResponse, RawError]:
        """Retrieve a list of all Interactions for a Session. A maximum of 100 records will be returned per page.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ to read the
                resources from.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ to read the
                resources from.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default10("/v1/Services/{ServiceSid}/Sessions/{SessionSid}/Interactions"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("SessionSid", session_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListInteractionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncProxyV1InteractionWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_interaction(
        self, service_sid: str, session_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Interaction.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resource to delete.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ of the
                resource to delete.
            sid: The Twilio-provided string that uniquely identifies the Interaction resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default10("/v1/Services/{ServiceSid}/Sessions/{SessionSid}/Interactions/{Sid}"),
            path_params=[
                param[str]("ServiceSid", service_sid), param[str]("SessionSid", session_sid), param[str]("Sid", sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_interaction(
        self, service_sid: str, session_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ProxyV1ServiceSessionInteraction, RawError]:
        """Retrieve a list of Interactions for a given `Session <https://www.twilio.com/docs/proxy/api/session>`__.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                resource to fetch.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ of the
                resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the Interaction resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default10("/v1/Services/{ServiceSid}/Sessions/{SessionSid}/Interactions/{Sid}"),
            path_params=[
                param[str]("ServiceSid", service_sid), param[str]("SessionSid", session_sid), param[str]("Sid", sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ProxyV1ServiceSessionInteraction],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_interaction(
        self,
        service_sid: str,
        session_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInteractionResponse, RawError]:
        """Retrieve a list of all Interactions for a Session. A maximum of 100 records will be returned per page.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ to read the
                resources from.
            session_sid: The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ to read the
                resources from.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default10("/v1/Services/{ServiceSid}/Sessions/{SessionSid}/Interactions"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("SessionSid", session_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListInteractionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
