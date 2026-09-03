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
    empty_response,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.api_v2010_account_message_media import ApiV2010AccountMessageMedia
from ..server.server import Server


class Api20100401MediaInstance:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401MediaInstanceWithRawResponse(client, server, auth)

    def delete_media(
        self, account_sid: str, message_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete the Media resource.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that is associated
                with the Media resource.
            message_sid: The SID of the Message resource that is associated with the Media resource.
            sid: The unique identifier of the to-be-deleted Media resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_media(
            account_sid, message_sid, sid, request_options=request_options
        ).unwrap()

    def fetch_media(
        self, account_sid: str, message_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountMessageMedia:
        """Fetch a single Media resource associated with a specific Message resource

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ associated with the
                Media resource.
            message_sid: The SID of the Message resource that is associated with the Media resource.
            sid: The Twilio-provided string that uniquely identifies the Media resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_media(
            account_sid, message_sid, sid, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401MediaInstanceWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401MediaInstance:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401MediaInstanceWithRawResponse(client, server, auth)

    async def delete_media(
        self, account_sid: str, message_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete the Media resource.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that is associated
                with the Media resource.
            message_sid: The SID of the Message resource that is associated with the Media resource.
            sid: The unique identifier of the to-be-deleted Media resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_media(account_sid, message_sid, sid, request_options=request_options)
        ).unwrap()

    async def fetch_media(
        self, account_sid: str, message_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountMessageMedia:
        """Fetch a single Media resource associated with a specific Message resource

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ associated with the
                Media resource.
            message_sid: The SID of the Message resource that is associated with the Media resource.
            sid: The Twilio-provided string that uniquely identifies the Media resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_media(account_sid, message_sid, sid, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401MediaInstanceWithRawResponse:
        return self._with_raw_response


class Api20100401MediaInstanceWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_media(
        self, account_sid: str, message_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete the Media resource.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that is associated
                with the Media resource.
            message_sid: The SID of the Message resource that is associated with the Media resource.
            sid: The unique identifier of the to-be-deleted Media resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Messages/{MessageSid}/Media/{Sid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid), param[str]("MessageSid", message_sid), param[str]("Sid", sid)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_media(
        self, account_sid: str, message_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountMessageMedia, RawError]:
        """Fetch a single Media resource associated with a specific Message resource

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ associated with the
                Media resource.
            message_sid: The SID of the Message resource that is associated with the Media resource.
            sid: The Twilio-provided string that uniquely identifies the Media resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Messages/{MessageSid}/Media/{Sid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid), param[str]("MessageSid", message_sid), param[str]("Sid", sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountMessageMedia],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401MediaInstanceWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_media(
        self, account_sid: str, message_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete the Media resource.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that is associated
                with the Media resource.
            message_sid: The SID of the Message resource that is associated with the Media resource.
            sid: The unique identifier of the to-be-deleted Media resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Messages/{MessageSid}/Media/{Sid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid), param[str]("MessageSid", message_sid), param[str]("Sid", sid)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_media(
        self, account_sid: str, message_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountMessageMedia, RawError]:
        """Fetch a single Media resource associated with a specific Message resource

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ associated with the
                Media resource.
            message_sid: The SID of the Message resource that is associated with the Media resource.
            sid: The Twilio-provided string that uniquely identifies the Media resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Messages/{MessageSid}/Media/{Sid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid), param[str]("MessageSid", message_sid), param[str]("Sid", sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountMessageMedia],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
