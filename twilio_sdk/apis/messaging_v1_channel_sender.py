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
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.list_channel_sender_response import ListChannelSenderResponse
from ..models.messaging_v1_service_channel_sender import MessagingV1ServiceChannelSender
from ..server.server import Server


class MessagingV1ChannelSender:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MessagingV1ChannelSenderWithRawResponse(client, server, auth)

    def create_channel_sender(
        self, messaging_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MessagingV1ServiceChannelSender:
        """A Messaging Service resource to read, fetch all Channel Senders associated with a Messaging Service.

        Args:
            messaging_service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__
                to create the resource under.
            sid: The SID of the Channel Sender being added to the Service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_channel_sender(
            messaging_service_sid, sid, request_options=request_options
        ).unwrap()

    def delete_channel_sender(
        self, messaging_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """A Messaging Service resource to read, fetch all Channel Senders associated with a Messaging Service.

        Args:
            messaging_service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__
                to delete the resource from.
            sid: The SID of the Channel Sender resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_channel_sender(
            messaging_service_sid, sid, request_options=request_options
        ).unwrap()

    def fetch_channel_sender(
        self, messaging_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MessagingV1ServiceChannelSender:
        """A Messaging Service resource to read, fetch all Channel Senders associated with a Messaging Service.

        Args:
            messaging_service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__
                to fetch the resource from.
            sid: The SID of the ChannelSender resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_channel_sender(
            messaging_service_sid, sid, request_options=request_options
        ).unwrap()

    def list_channel_sender(
        self,
        messaging_service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListChannelSenderResponse:
        """A Messaging Service resource to read, fetch all Channel Senders associated with a Messaging Service.

        Args:
            messaging_service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__
                to read the resources from.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_channel_sender(
            messaging_service_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> MessagingV1ChannelSenderWithRawResponse:
        return self._with_raw_response


class AsyncMessagingV1ChannelSender:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMessagingV1ChannelSenderWithRawResponse(client, server, auth)

    async def create_channel_sender(
        self, messaging_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MessagingV1ServiceChannelSender:
        """A Messaging Service resource to read, fetch all Channel Senders associated with a Messaging Service.

        Args:
            messaging_service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__
                to create the resource under.
            sid: The SID of the Channel Sender being added to the Service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_channel_sender(
                messaging_service_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def delete_channel_sender(
        self, messaging_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """A Messaging Service resource to read, fetch all Channel Senders associated with a Messaging Service.

        Args:
            messaging_service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__
                to delete the resource from.
            sid: The SID of the Channel Sender resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_channel_sender(
                messaging_service_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def fetch_channel_sender(
        self, messaging_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MessagingV1ServiceChannelSender:
        """A Messaging Service resource to read, fetch all Channel Senders associated with a Messaging Service.

        Args:
            messaging_service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__
                to fetch the resource from.
            sid: The SID of the ChannelSender resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_channel_sender(
                messaging_service_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def list_channel_sender(
        self,
        messaging_service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListChannelSenderResponse:
        """A Messaging Service resource to read, fetch all Channel Senders associated with a Messaging Service.

        Args:
            messaging_service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__
                to read the resources from.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_channel_sender(
                messaging_service_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncMessagingV1ChannelSenderWithRawResponse:
        return self._with_raw_response


class MessagingV1ChannelSenderWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_channel_sender(
        self, messaging_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV1ServiceChannelSender, RawError]:
        """A Messaging Service resource to read, fetch all Channel Senders associated with a Messaging Service.

        Args:
            messaging_service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__
                to create the resource under.
            sid: The SID of the Channel Sender being added to the Service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v1/Services/{MessagingServiceSid}/ChannelSenders"),
            path_params=[param[str]("MessagingServiceSid", messaging_service_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str]("Sid", sid)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1ServiceChannelSender],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_channel_sender(
        self, messaging_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """A Messaging Service resource to read, fetch all Channel Senders associated with a Messaging Service.

        Args:
            messaging_service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__
                to delete the resource from.
            sid: The SID of the Channel Sender resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default1("/v1/Services/{MessagingServiceSid}/ChannelSenders/{Sid}"),
            path_params=[param[str]("MessagingServiceSid", messaging_service_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_channel_sender(
        self, messaging_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV1ServiceChannelSender, RawError]:
        """A Messaging Service resource to read, fetch all Channel Senders associated with a Messaging Service.

        Args:
            messaging_service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__
                to fetch the resource from.
            sid: The SID of the ChannelSender resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/Services/{MessagingServiceSid}/ChannelSenders/{Sid}"),
            path_params=[param[str]("MessagingServiceSid", messaging_service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1ServiceChannelSender],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_channel_sender(
        self,
        messaging_service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListChannelSenderResponse, RawError]:
        """A Messaging Service resource to read, fetch all Channel Senders associated with a Messaging Service.

        Args:
            messaging_service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__
                to read the resources from.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/Services/{MessagingServiceSid}/ChannelSenders"),
            path_params=[param[str]("MessagingServiceSid", messaging_service_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListChannelSenderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncMessagingV1ChannelSenderWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_channel_sender(
        self, messaging_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV1ServiceChannelSender, RawError]:
        """A Messaging Service resource to read, fetch all Channel Senders associated with a Messaging Service.

        Args:
            messaging_service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__
                to create the resource under.
            sid: The SID of the Channel Sender being added to the Service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v1/Services/{MessagingServiceSid}/ChannelSenders"),
            path_params=[param[str]("MessagingServiceSid", messaging_service_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str]("Sid", sid)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1ServiceChannelSender],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_channel_sender(
        self, messaging_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """A Messaging Service resource to read, fetch all Channel Senders associated with a Messaging Service.

        Args:
            messaging_service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__
                to delete the resource from.
            sid: The SID of the Channel Sender resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default1("/v1/Services/{MessagingServiceSid}/ChannelSenders/{Sid}"),
            path_params=[param[str]("MessagingServiceSid", messaging_service_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_channel_sender(
        self, messaging_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV1ServiceChannelSender, RawError]:
        """A Messaging Service resource to read, fetch all Channel Senders associated with a Messaging Service.

        Args:
            messaging_service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__
                to fetch the resource from.
            sid: The SID of the ChannelSender resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/Services/{MessagingServiceSid}/ChannelSenders/{Sid}"),
            path_params=[param[str]("MessagingServiceSid", messaging_service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1ServiceChannelSender],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_channel_sender(
        self,
        messaging_service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListChannelSenderResponse, RawError]:
        """A Messaging Service resource to read, fetch all Channel Senders associated with a Messaging Service.

        Args:
            messaging_service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__
                to read the resources from.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/Services/{MessagingServiceSid}/ChannelSenders"),
            path_params=[param[str]("MessagingServiceSid", messaging_service_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListChannelSenderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
