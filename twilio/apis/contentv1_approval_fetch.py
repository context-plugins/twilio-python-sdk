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
from ..models.content_v1_content_approval_fetch import ContentV1ContentApprovalFetch
from ..server.server import Server


class Contentv1ApprovalFetch:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Contentv1ApprovalFetchWithRawResponse(client, server, auth)

    def fetch_approval_fetch(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ContentV1ContentApprovalFetch:
        """Fetch a Content resource's approval status by its unique Content Sid

        Args:
            sid: The Twilio-provided string that uniquely identifies the Content resource whose approval information to
                fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_approval_fetch(sid, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> Contentv1ApprovalFetchWithRawResponse:
        return self._with_raw_response


class AsyncContentv1ApprovalFetch:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncContentv1ApprovalFetchWithRawResponse(client, server, auth)

    async def fetch_approval_fetch(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ContentV1ContentApprovalFetch:
        """Fetch a Content resource's approval status by its unique Content Sid

        Args:
            sid: The Twilio-provided string that uniquely identifies the Content resource whose approval information to
                fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_approval_fetch(sid, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncContentv1ApprovalFetchWithRawResponse:
        return self._with_raw_response


class Contentv1ApprovalFetchWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_approval_fetch(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ContentV1ContentApprovalFetch, RawError]:
        """Fetch a Content resource's approval status by its unique Content Sid

        Args:
            sid: The Twilio-provided string that uniquely identifies the Content resource whose approval information to
                fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default2("/v1/Content/{Sid}/ApprovalRequests"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ContentV1ContentApprovalFetch],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncContentv1ApprovalFetchWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_approval_fetch(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ContentV1ContentApprovalFetch, RawError]:
        """Fetch a Content resource's approval status by its unique Content Sid

        Args:
            sid: The Twilio-provided string that uniquely identifies the Content resource whose approval information to
                fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default2("/v1/Content/{Sid}/ApprovalRequests"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ContentV1ContentApprovalFetch],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
