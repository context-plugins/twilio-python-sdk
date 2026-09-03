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
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.content_approval_request import ContentApprovalRequest, ContentApprovalRequestDict
from ..models.content_v1_content_approval_create import ContentV1ContentApprovalCreate
from ..server.server import Server


class Contentv1ApprovalCreate:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Contentv1ApprovalCreateWithRawResponse(client, server, auth)

    def create_approval_create(
        self,
        content_sid: str,
        body: ContentApprovalRequest | ContentApprovalRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ContentV1ContentApprovalCreate:
        """Create a ContentApprovalRequest for a content item

        Args:
            content_sid: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_approval_create(
            content_sid, body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> Contentv1ApprovalCreateWithRawResponse:
        return self._with_raw_response


class AsyncContentv1ApprovalCreate:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncContentv1ApprovalCreateWithRawResponse(client, server, auth)

    async def create_approval_create(
        self,
        content_sid: str,
        body: ContentApprovalRequest | ContentApprovalRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ContentV1ContentApprovalCreate:
        """Create a ContentApprovalRequest for a content item

        Args:
            content_sid: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_approval_create(content_sid, body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncContentv1ApprovalCreateWithRawResponse:
        return self._with_raw_response


class Contentv1ApprovalCreateWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_approval_create(
        self,
        content_sid: str,
        body: ContentApprovalRequest | ContentApprovalRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ContentV1ContentApprovalCreate, RawError]:
        """Create a ContentApprovalRequest for a content item

        Args:
            content_sid: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default2("/v1/Content/{ContentSid}/ApprovalRequests/whatsapp"),
            path_params=[param[str]("ContentSid", content_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ContentApprovalRequest | ContentApprovalRequestDict](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ContentV1ContentApprovalCreate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncContentv1ApprovalCreateWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_approval_create(
        self,
        content_sid: str,
        body: ContentApprovalRequest | ContentApprovalRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ContentV1ContentApprovalCreate, RawError]:
        """Create a ContentApprovalRequest for a content item

        Args:
            content_sid: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default2("/v1/Content/{ContentSid}/ApprovalRequests/whatsapp"),
            path_params=[param[str]("ContentSid", content_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ContentApprovalRequest | ContentApprovalRequestDict](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ContentV1ContentApprovalCreate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
