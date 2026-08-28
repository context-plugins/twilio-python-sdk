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
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.list_channels_sender_response import ListChannelsSenderResponse
from ..models.messaging_v2_channels_sender_requests_create import (
    MessagingV2ChannelsSenderRequestsCreate,
    MessagingV2ChannelsSenderRequestsCreateDict,
)
from ..models.messaging_v2_channels_sender_requests_update import (
    MessagingV2ChannelsSenderRequestsUpdate,
    MessagingV2ChannelsSenderRequestsUpdateDict,
)
from ..models.messaging_v2_channels_sender_response import MessagingV2ChannelsSenderResponse
from ..server.server import Server


class MessagingV2ChannelsSender:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MessagingV2ChannelsSenderWithRawResponse(client, server, auth)

    def create_channels_sender(
        self,
        body: MessagingV2ChannelsSenderRequestsCreate | MessagingV2ChannelsSenderRequestsCreateDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MessagingV2ChannelsSenderResponse:
        """Create a Sender.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Accepted

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_channels_sender(body, request_options=request_options).unwrap()

    def delete_channels_sender(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """(WhatsApp only) Delete a Sender.

        Args:
            sid: The SID of the sender.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_channels_sender(sid, request_options=request_options).unwrap()

    def fetch_channels_sender(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MessagingV2ChannelsSenderResponse:
        """Retrieve a Sender.

        Args:
            sid: The SID of the sender.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_channels_sender(sid, request_options=request_options).unwrap()

    def list_channels_sender(
        self,
        channel: str,
        *,
        page_size: int | None = 50,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListChannelsSenderResponse:
        """Retrieve a list of Senders for an account.

        Args:
            channel: Value sent with the request.
            page_size: The number of items to return per page. For WhatsApp, the default is ``20``.
            page: The page index. Use only for client state.
            page_token: The page token provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_channels_sender(
            channel, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    def update_channels_sender(
        self,
        sid: str,
        *,
        body: MessagingV2ChannelsSenderRequestsUpdate | MessagingV2ChannelsSenderRequestsUpdateDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MessagingV2ChannelsSenderResponse:
        """(WhatsApp only) Update a Sender. You can update a sender's information, including ``profile``, ``webhook``,
        and ``configuration``. To verify a phone number, set ``configuration.verification_code`` to the One-time
        Password (OTP) that you received.

        Args:
            sid: The SID of the sender.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Accepted

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_channels_sender(sid, body=body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> MessagingV2ChannelsSenderWithRawResponse:
        return self._with_raw_response


class AsyncMessagingV2ChannelsSender:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMessagingV2ChannelsSenderWithRawResponse(client, server, auth)

    async def create_channels_sender(
        self,
        body: MessagingV2ChannelsSenderRequestsCreate | MessagingV2ChannelsSenderRequestsCreateDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MessagingV2ChannelsSenderResponse:
        """Create a Sender.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Accepted

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_channels_sender(body, request_options=request_options)).unwrap()

    async def delete_channels_sender(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """(WhatsApp only) Delete a Sender.

        Args:
            sid: The SID of the sender.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_channels_sender(sid, request_options=request_options)).unwrap()

    async def fetch_channels_sender(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MessagingV2ChannelsSenderResponse:
        """Retrieve a Sender.

        Args:
            sid: The SID of the sender.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_channels_sender(sid, request_options=request_options)).unwrap()

    async def list_channels_sender(
        self,
        channel: str,
        *,
        page_size: int | None = 50,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListChannelsSenderResponse:
        """Retrieve a list of Senders for an account.

        Args:
            channel: Value sent with the request.
            page_size: The number of items to return per page. For WhatsApp, the default is ``20``.
            page: The page index. Use only for client state.
            page_token: The page token provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_channels_sender(
                channel, page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    async def update_channels_sender(
        self,
        sid: str,
        *,
        body: MessagingV2ChannelsSenderRequestsUpdate | MessagingV2ChannelsSenderRequestsUpdateDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MessagingV2ChannelsSenderResponse:
        """(WhatsApp only) Update a Sender. You can update a sender's information, including ``profile``, ``webhook``,
        and ``configuration``. To verify a phone number, set ``configuration.verification_code`` to the One-time
        Password (OTP) that you received.

        Args:
            sid: The SID of the sender.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Accepted

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_channels_sender(sid, body=body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncMessagingV2ChannelsSenderWithRawResponse:
        return self._with_raw_response


class MessagingV2ChannelsSenderWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_channels_sender(
        self,
        body: MessagingV2ChannelsSenderRequestsCreate | MessagingV2ChannelsSenderRequestsCreateDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MessagingV2ChannelsSenderResponse, RawError]:
        """Create a Sender.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v2/Channels/Senders"),
            body=json_body[MessagingV2ChannelsSenderRequestsCreate | MessagingV2ChannelsSenderRequestsCreateDict](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV2ChannelsSenderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_channels_sender(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """(WhatsApp only) Delete a Sender.

        Args:
            sid: The SID of the sender.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default1("/v2/Channels/Senders/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_channels_sender(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV2ChannelsSenderResponse, RawError]:
        """Retrieve a Sender.

        Args:
            sid: The SID of the sender.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v2/Channels/Senders/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV2ChannelsSenderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_channels_sender(
        self,
        channel: str,
        *,
        page_size: int | None = 50,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListChannelsSenderResponse, RawError]:
        """Retrieve a list of Senders for an account.

        Args:
            channel: Value sent with the request.
            page_size: The number of items to return per page. For WhatsApp, the default is ``20``.
            page: The page index. Use only for client state.
            page_token: The page token provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v2/Channels/Senders"),
            query_params=[
                param[str]("Channel", channel),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListChannelsSenderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_channels_sender(
        self,
        sid: str,
        *,
        body: MessagingV2ChannelsSenderRequestsUpdate | MessagingV2ChannelsSenderRequestsUpdateDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MessagingV2ChannelsSenderResponse, RawError]:
        """(WhatsApp only) Update a Sender. You can update a sender's information, including ``profile``, ``webhook``,
        and ``configuration``. To verify a phone number, set ``configuration.verification_code`` to the One-time
        Password (OTP) that you received.

        Args:
            sid: The SID of the sender.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v2/Channels/Senders/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            body=json_body[
                MessagingV2ChannelsSenderRequestsUpdate | MessagingV2ChannelsSenderRequestsUpdateDict | None
            ](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV2ChannelsSenderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncMessagingV2ChannelsSenderWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_channels_sender(
        self,
        body: MessagingV2ChannelsSenderRequestsCreate | MessagingV2ChannelsSenderRequestsCreateDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MessagingV2ChannelsSenderResponse, RawError]:
        """Create a Sender.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v2/Channels/Senders"),
            body=json_body[MessagingV2ChannelsSenderRequestsCreate | MessagingV2ChannelsSenderRequestsCreateDict](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV2ChannelsSenderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_channels_sender(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """(WhatsApp only) Delete a Sender.

        Args:
            sid: The SID of the sender.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default1("/v2/Channels/Senders/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_channels_sender(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV2ChannelsSenderResponse, RawError]:
        """Retrieve a Sender.

        Args:
            sid: The SID of the sender.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v2/Channels/Senders/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV2ChannelsSenderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_channels_sender(
        self,
        channel: str,
        *,
        page_size: int | None = 50,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListChannelsSenderResponse, RawError]:
        """Retrieve a list of Senders for an account.

        Args:
            channel: Value sent with the request.
            page_size: The number of items to return per page. For WhatsApp, the default is ``20``.
            page: The page index. Use only for client state.
            page_token: The page token provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v2/Channels/Senders"),
            query_params=[
                param[str]("Channel", channel),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListChannelsSenderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_channels_sender(
        self,
        sid: str,
        *,
        body: MessagingV2ChannelsSenderRequestsUpdate | MessagingV2ChannelsSenderRequestsUpdateDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MessagingV2ChannelsSenderResponse, RawError]:
        """(WhatsApp only) Update a Sender. You can update a sender's information, including ``profile``, ``webhook``,
        and ``configuration``. To verify a phone number, set ``configuration.verification_code`` to the One-time
        Password (OTP) that you received.

        Args:
            sid: The SID of the sender.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v2/Channels/Senders/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            body=json_body[
                MessagingV2ChannelsSenderRequestsUpdate | MessagingV2ChannelsSenderRequestsUpdateDict | None
            ](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV2ChannelsSenderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
