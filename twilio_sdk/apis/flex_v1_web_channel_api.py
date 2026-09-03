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
from ..models.enums.web_channel_enum_chat_status import WebChannelEnumChatStatusOrStr
from ..models.flex_v1_web_channel import FlexV1WebChannel
from ..models.list_web_channel_response import ListWebChannelResponse
from ..server.server import Server


class FlexV1WebChannelApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FlexV1WebChannelApiWithRawResponse(client, server, auth)

    def create_web_channel(
        self,
        flex_flow_sid: str,
        identity: str,
        customer_friendly_name: str,
        chat_friendly_name: str,
        *,
        chat_unique_name: str | None = None,
        pre_engagement_data: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1WebChannel:
        """Send a ``POST`` request.

        Args:
            flex_flow_sid: The SID of the Flex Flow.
            identity: The chat identity.
            customer_friendly_name: The chat participant's friendly name.
            chat_friendly_name: The chat channel's friendly name.
            chat_unique_name: The chat channel's unique name.
            pre_engagement_data: The pre-engagement data.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_web_channel(
            flex_flow_sid,
            identity,
            customer_friendly_name,
            chat_friendly_name,
            chat_unique_name=chat_unique_name,
            pre_engagement_data=pre_engagement_data,
            request_options=request_options,
        ).unwrap()

    def delete_web_channel(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Send a ``DELETE`` request.

        Args:
            sid: The SID of the WebChannel resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_web_channel(sid, request_options=request_options).unwrap()

    def fetch_web_channel(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> FlexV1WebChannel:
        """Send a ``GET`` request.

        Args:
            sid: The SID of the WebChannel resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_web_channel(sid, request_options=request_options).unwrap()

    def list_web_channel(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListWebChannelResponse:
        """Send a ``GET`` request.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_web_channel(
            page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    def update_web_channel(
        self,
        sid: str,
        *,
        chat_status: WebChannelEnumChatStatusOrStr | None = None,
        post_engagement_data: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1WebChannel:
        """Send a ``POST`` request.

        Args:
            sid: The SID of the WebChannel resource to update.
            chat_status: Value sent with the request.
            post_engagement_data: The post-engagement data.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_web_channel(
            sid, chat_status=chat_status, post_engagement_data=post_engagement_data, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> FlexV1WebChannelApiWithRawResponse:
        return self._with_raw_response


class AsyncFlexV1WebChannelApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFlexV1WebChannelApiWithRawResponse(client, server, auth)

    async def create_web_channel(
        self,
        flex_flow_sid: str,
        identity: str,
        customer_friendly_name: str,
        chat_friendly_name: str,
        *,
        chat_unique_name: str | None = None,
        pre_engagement_data: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1WebChannel:
        """Send a ``POST`` request.

        Args:
            flex_flow_sid: The SID of the Flex Flow.
            identity: The chat identity.
            customer_friendly_name: The chat participant's friendly name.
            chat_friendly_name: The chat channel's friendly name.
            chat_unique_name: The chat channel's unique name.
            pre_engagement_data: The pre-engagement data.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_web_channel(
                flex_flow_sid,
                identity,
                customer_friendly_name,
                chat_friendly_name,
                chat_unique_name=chat_unique_name,
                pre_engagement_data=pre_engagement_data,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_web_channel(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Send a ``DELETE`` request.

        Args:
            sid: The SID of the WebChannel resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_web_channel(sid, request_options=request_options)).unwrap()

    async def fetch_web_channel(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FlexV1WebChannel:
        """Send a ``GET`` request.

        Args:
            sid: The SID of the WebChannel resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_web_channel(sid, request_options=request_options)).unwrap()

    async def list_web_channel(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListWebChannelResponse:
        """Send a ``GET`` request.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_web_channel(
                page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    async def update_web_channel(
        self,
        sid: str,
        *,
        chat_status: WebChannelEnumChatStatusOrStr | None = None,
        post_engagement_data: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1WebChannel:
        """Send a ``POST`` request.

        Args:
            sid: The SID of the WebChannel resource to update.
            chat_status: Value sent with the request.
            post_engagement_data: The post-engagement data.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_web_channel(
                sid, chat_status=chat_status, post_engagement_data=post_engagement_data, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncFlexV1WebChannelApiWithRawResponse:
        return self._with_raw_response


class FlexV1WebChannelApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_web_channel(
        self,
        flex_flow_sid: str,
        identity: str,
        customer_friendly_name: str,
        chat_friendly_name: str,
        *,
        chat_unique_name: str | None = None,
        pre_engagement_data: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1WebChannel, RawError]:
        """Send a ``POST`` request.

        Args:
            flex_flow_sid: The SID of the Flex Flow.
            identity: The chat identity.
            customer_friendly_name: The chat participant's friendly name.
            chat_friendly_name: The chat channel's friendly name.
            chat_unique_name: The chat channel's unique name.
            pre_engagement_data: The pre-engagement data.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/WebChannels"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("FlexFlowSid", flex_flow_sid),
                    param[str]("Identity", identity),
                    param[str]("CustomerFriendlyName", customer_friendly_name),
                    param[str]("ChatFriendlyName", chat_friendly_name),
                    param[str | None]("ChatUniqueName", chat_unique_name),
                    param[str | None]("PreEngagementData", pre_engagement_data),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1WebChannel],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_web_channel(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Send a ``DELETE`` request.

        Args:
            sid: The SID of the WebChannel resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default13("/v1/WebChannels/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_web_channel(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FlexV1WebChannel, RawError]:
        """Send a ``GET`` request.

        Args:
            sid: The SID of the WebChannel resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/WebChannels/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1WebChannel],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_web_channel(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListWebChannelResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/WebChannels"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListWebChannelResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_web_channel(
        self,
        sid: str,
        *,
        chat_status: WebChannelEnumChatStatusOrStr | None = None,
        post_engagement_data: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1WebChannel, RawError]:
        """Send a ``POST`` request.

        Args:
            sid: The SID of the WebChannel resource to update.
            chat_status: Value sent with the request.
            post_engagement_data: The post-engagement data.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/WebChannels/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[WebChannelEnumChatStatusOrStr | None]("ChatStatus", chat_status),
                    param[str | None]("PostEngagementData", post_engagement_data),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1WebChannel],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncFlexV1WebChannelApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_web_channel(
        self,
        flex_flow_sid: str,
        identity: str,
        customer_friendly_name: str,
        chat_friendly_name: str,
        *,
        chat_unique_name: str | None = None,
        pre_engagement_data: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1WebChannel, RawError]:
        """Send a ``POST`` request.

        Args:
            flex_flow_sid: The SID of the Flex Flow.
            identity: The chat identity.
            customer_friendly_name: The chat participant's friendly name.
            chat_friendly_name: The chat channel's friendly name.
            chat_unique_name: The chat channel's unique name.
            pre_engagement_data: The pre-engagement data.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/WebChannels"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("FlexFlowSid", flex_flow_sid),
                    param[str]("Identity", identity),
                    param[str]("CustomerFriendlyName", customer_friendly_name),
                    param[str]("ChatFriendlyName", chat_friendly_name),
                    param[str | None]("ChatUniqueName", chat_unique_name),
                    param[str | None]("PreEngagementData", pre_engagement_data),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1WebChannel],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_web_channel(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Send a ``DELETE`` request.

        Args:
            sid: The SID of the WebChannel resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default13("/v1/WebChannels/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_web_channel(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FlexV1WebChannel, RawError]:
        """Send a ``GET`` request.

        Args:
            sid: The SID of the WebChannel resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/WebChannels/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1WebChannel],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_web_channel(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListWebChannelResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/WebChannels"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListWebChannelResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_web_channel(
        self,
        sid: str,
        *,
        chat_status: WebChannelEnumChatStatusOrStr | None = None,
        post_engagement_data: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1WebChannel, RawError]:
        """Send a ``POST`` request.

        Args:
            sid: The SID of the WebChannel resource to update.
            chat_status: Value sent with the request.
            post_engagement_data: The post-engagement data.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/WebChannels/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[WebChannelEnumChatStatusOrStr | None]("ChatStatus", chat_status),
                    param[str | None]("PostEngagementData", post_engagement_data),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1WebChannel],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
