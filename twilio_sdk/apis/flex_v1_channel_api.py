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
from ..models.flex_v1_channel import FlexV1Channel
from ..models.list_channel_response import ListChannelResponse
from ..server.server import Server


class FlexV1ChannelApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FlexV1ChannelApiWithRawResponse(client, server, auth)

    def create_channel(
        self,
        flex_flow_sid: str,
        identity: str,
        chat_user_friendly_name: str,
        chat_friendly_name: str,
        *,
        target: str | None = None,
        chat_unique_name: str | None = None,
        pre_engagement_data: str | None = None,
        task_sid: str | None = None,
        task_attributes: str | None = None,
        long_lived: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1Channel:
        """Flex chat channels

        Args:
            flex_flow_sid: The SID of the Flex Flow.
            identity: The ``identity`` value that uniquely identifies the new resource's chat User.
            chat_user_friendly_name: The chat participant's friendly name.
            chat_friendly_name: The chat channel's friendly name.
            target: The Target Contact Identity, for example the phone number of an SMS.
            chat_unique_name: The chat channel's unique name.
            pre_engagement_data: The pre-engagement data.
            task_sid: The SID of the TaskRouter Task. Only valid when integration type is ``task``. ``null`` for
                integration types ``studio`` & ``external``
            task_attributes: The Task attributes to be added for the TaskRouter Task.
            long_lived: Whether to create the channel as long-lived.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_channel(
            flex_flow_sid,
            identity,
            chat_user_friendly_name,
            chat_friendly_name,
            target=target,
            chat_unique_name=chat_unique_name,
            pre_engagement_data=pre_engagement_data,
            task_sid=task_sid,
            task_attributes=task_attributes,
            long_lived=long_lived,
            request_options=request_options,
        ).unwrap()

    def delete_channel(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Flex chat channels

        Args:
            sid: The SID of the Flex chat channel resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_channel(sid, request_options=request_options).unwrap()

    def fetch_channel(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> FlexV1Channel:
        """Flex chat channels

        Args:
            sid: The SID of the Flex chat channel resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_channel(sid, request_options=request_options).unwrap()

    def list_channel(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListChannelResponse:
        """Flex chat channels

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_channel(
            page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> FlexV1ChannelApiWithRawResponse:
        return self._with_raw_response


class AsyncFlexV1ChannelApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFlexV1ChannelApiWithRawResponse(client, server, auth)

    async def create_channel(
        self,
        flex_flow_sid: str,
        identity: str,
        chat_user_friendly_name: str,
        chat_friendly_name: str,
        *,
        target: str | None = None,
        chat_unique_name: str | None = None,
        pre_engagement_data: str | None = None,
        task_sid: str | None = None,
        task_attributes: str | None = None,
        long_lived: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1Channel:
        """Flex chat channels

        Args:
            flex_flow_sid: The SID of the Flex Flow.
            identity: The ``identity`` value that uniquely identifies the new resource's chat User.
            chat_user_friendly_name: The chat participant's friendly name.
            chat_friendly_name: The chat channel's friendly name.
            target: The Target Contact Identity, for example the phone number of an SMS.
            chat_unique_name: The chat channel's unique name.
            pre_engagement_data: The pre-engagement data.
            task_sid: The SID of the TaskRouter Task. Only valid when integration type is ``task``. ``null`` for
                integration types ``studio`` & ``external``
            task_attributes: The Task attributes to be added for the TaskRouter Task.
            long_lived: Whether to create the channel as long-lived.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_channel(
                flex_flow_sid,
                identity,
                chat_user_friendly_name,
                chat_friendly_name,
                target=target,
                chat_unique_name=chat_unique_name,
                pre_engagement_data=pre_engagement_data,
                task_sid=task_sid,
                task_attributes=task_attributes,
                long_lived=long_lived,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_channel(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Flex chat channels

        Args:
            sid: The SID of the Flex chat channel resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_channel(sid, request_options=request_options)).unwrap()

    async def fetch_channel(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> FlexV1Channel:
        """Flex chat channels

        Args:
            sid: The SID of the Flex chat channel resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_channel(sid, request_options=request_options)).unwrap()

    async def list_channel(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListChannelResponse:
        """Flex chat channels

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
            await self._with_raw_response.list_channel(
                page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncFlexV1ChannelApiWithRawResponse:
        return self._with_raw_response


class FlexV1ChannelApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_channel(
        self,
        flex_flow_sid: str,
        identity: str,
        chat_user_friendly_name: str,
        chat_friendly_name: str,
        *,
        target: str | None = None,
        chat_unique_name: str | None = None,
        pre_engagement_data: str | None = None,
        task_sid: str | None = None,
        task_attributes: str | None = None,
        long_lived: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1Channel, RawError]:
        """Flex chat channels

        Args:
            flex_flow_sid: The SID of the Flex Flow.
            identity: The ``identity`` value that uniquely identifies the new resource's chat User.
            chat_user_friendly_name: The chat participant's friendly name.
            chat_friendly_name: The chat channel's friendly name.
            target: The Target Contact Identity, for example the phone number of an SMS.
            chat_unique_name: The chat channel's unique name.
            pre_engagement_data: The pre-engagement data.
            task_sid: The SID of the TaskRouter Task. Only valid when integration type is ``task``. ``null`` for
                integration types ``studio`` & ``external``
            task_attributes: The Task attributes to be added for the TaskRouter Task.
            long_lived: Whether to create the channel as long-lived.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/Channels"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("FlexFlowSid", flex_flow_sid),
                    param[str]("Identity", identity),
                    param[str]("ChatUserFriendlyName", chat_user_friendly_name),
                    param[str]("ChatFriendlyName", chat_friendly_name),
                    param[str | None]("Target", target),
                    param[str | None]("ChatUniqueName", chat_unique_name),
                    param[str | None]("PreEngagementData", pre_engagement_data),
                    param[str | None]("TaskSid", task_sid),
                    param[str | None]("TaskAttributes", task_attributes),
                    param[bool | None]("LongLived", long_lived),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1Channel],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_channel(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Flex chat channels

        Args:
            sid: The SID of the Flex chat channel resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default13("/v1/Channels/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_channel(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FlexV1Channel, RawError]:
        """Flex chat channels

        Args:
            sid: The SID of the Flex chat channel resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/Channels/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1Channel],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_channel(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListChannelResponse, RawError]:
        """Flex chat channels

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/Channels"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListChannelResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncFlexV1ChannelApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_channel(
        self,
        flex_flow_sid: str,
        identity: str,
        chat_user_friendly_name: str,
        chat_friendly_name: str,
        *,
        target: str | None = None,
        chat_unique_name: str | None = None,
        pre_engagement_data: str | None = None,
        task_sid: str | None = None,
        task_attributes: str | None = None,
        long_lived: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1Channel, RawError]:
        """Flex chat channels

        Args:
            flex_flow_sid: The SID of the Flex Flow.
            identity: The ``identity`` value that uniquely identifies the new resource's chat User.
            chat_user_friendly_name: The chat participant's friendly name.
            chat_friendly_name: The chat channel's friendly name.
            target: The Target Contact Identity, for example the phone number of an SMS.
            chat_unique_name: The chat channel's unique name.
            pre_engagement_data: The pre-engagement data.
            task_sid: The SID of the TaskRouter Task. Only valid when integration type is ``task``. ``null`` for
                integration types ``studio`` & ``external``
            task_attributes: The Task attributes to be added for the TaskRouter Task.
            long_lived: Whether to create the channel as long-lived.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/Channels"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("FlexFlowSid", flex_flow_sid),
                    param[str]("Identity", identity),
                    param[str]("ChatUserFriendlyName", chat_user_friendly_name),
                    param[str]("ChatFriendlyName", chat_friendly_name),
                    param[str | None]("Target", target),
                    param[str | None]("ChatUniqueName", chat_unique_name),
                    param[str | None]("PreEngagementData", pre_engagement_data),
                    param[str | None]("TaskSid", task_sid),
                    param[str | None]("TaskAttributes", task_attributes),
                    param[bool | None]("LongLived", long_lived),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1Channel],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_channel(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Flex chat channels

        Args:
            sid: The SID of the Flex chat channel resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default13("/v1/Channels/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_channel(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FlexV1Channel, RawError]:
        """Flex chat channels

        Args:
            sid: The SID of the Flex chat channel resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/Channels/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1Channel],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_channel(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListChannelResponse, RawError]:
        """Flex chat channels

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/Channels"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListChannelResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
