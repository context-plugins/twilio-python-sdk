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
from ..models.conversations_v1_service_service_binding import ConversationsV1ServiceServiceBinding
from ..models.enums.service_binding_enum_binding_type import ServiceBindingEnumBindingTypeOrStr
from ..models.list_service_binding_response import ListServiceBindingResponse
from ..server.server import Server


class ConversationsV1Binding:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ConversationsV1BindingWithRawResponse(client, server, auth)

    def delete_service_binding(
        self, chat_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Remove a push notification binding from the conversation service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to delete the Binding resource from.
            sid: The SID of the Binding resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_service_binding(
            chat_service_sid, sid, request_options=request_options
        ).unwrap()

    def fetch_service_binding(
        self, chat_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1ServiceServiceBinding:
        """Fetch a push notification binding from the conversation service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Binding resource is associated
                with.
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_service_binding(
            chat_service_sid, sid, request_options=request_options
        ).unwrap()

    def list_service_binding(
        self,
        chat_service_sid: str,
        *,
        binding_type: list[ServiceBindingEnumBindingTypeOrStr] | None = None,
        identity: list[str] | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListServiceBindingResponse:
        """Retrieve a list of all push notification bindings in the conversation service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Binding resource is associated
                with.
            binding_type: The push technology used by the Binding resources to read. Can be: ``apn``, ``gcm``, ``fcm``,
                or ``twilsock``. See `push notification configuration
                <https://www.twilio.com/docs/chat/push-notification-configuration>`__ for more info.
            identity: The identity of a `Conversation User
                <https://www.twilio.com/docs/conversations/api/user-resource>`__ this binding belongs to. See `access
                tokens <https://www.twilio.com/docs/conversations/create-tokens>`__ for more details.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_service_binding(
            chat_service_sid,
            binding_type=binding_type,
            identity=identity,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> ConversationsV1BindingWithRawResponse:
        return self._with_raw_response


class AsyncConversationsV1Binding:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncConversationsV1BindingWithRawResponse(client, server, auth)

    async def delete_service_binding(
        self, chat_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Remove a push notification binding from the conversation service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to delete the Binding resource from.
            sid: The SID of the Binding resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_service_binding(chat_service_sid, sid, request_options=request_options)
        ).unwrap()

    async def fetch_service_binding(
        self, chat_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1ServiceServiceBinding:
        """Fetch a push notification binding from the conversation service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Binding resource is associated
                with.
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_service_binding(chat_service_sid, sid, request_options=request_options)
        ).unwrap()

    async def list_service_binding(
        self,
        chat_service_sid: str,
        *,
        binding_type: list[ServiceBindingEnumBindingTypeOrStr] | None = None,
        identity: list[str] | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListServiceBindingResponse:
        """Retrieve a list of all push notification bindings in the conversation service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Binding resource is associated
                with.
            binding_type: The push technology used by the Binding resources to read. Can be: ``apn``, ``gcm``, ``fcm``,
                or ``twilsock``. See `push notification configuration
                <https://www.twilio.com/docs/chat/push-notification-configuration>`__ for more info.
            identity: The identity of a `Conversation User
                <https://www.twilio.com/docs/conversations/api/user-resource>`__ this binding belongs to. See `access
                tokens <https://www.twilio.com/docs/conversations/create-tokens>`__ for more details.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_service_binding(
                chat_service_sid,
                binding_type=binding_type,
                identity=identity,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncConversationsV1BindingWithRawResponse:
        return self._with_raw_response


class ConversationsV1BindingWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_service_binding(
        self, chat_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Remove a push notification binding from the conversation service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to delete the Binding resource from.
            sid: The SID of the Binding resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Bindings/{Sid}"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_service_binding(
        self, chat_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1ServiceServiceBinding, RawError]:
        """Fetch a push notification binding from the conversation service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Binding resource is associated
                with.
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Bindings/{Sid}"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceBinding],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_service_binding(
        self,
        chat_service_sid: str,
        *,
        binding_type: list[ServiceBindingEnumBindingTypeOrStr] | None = None,
        identity: list[str] | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListServiceBindingResponse, RawError]:
        """Retrieve a list of all push notification bindings in the conversation service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Binding resource is associated
                with.
            binding_type: The push technology used by the Binding resources to read. Can be: ``apn``, ``gcm``, ``fcm``,
                or ``twilsock``. See `push notification configuration
                <https://www.twilio.com/docs/chat/push-notification-configuration>`__ for more info.
            identity: The identity of a `Conversation User
                <https://www.twilio.com/docs/conversations/api/user-resource>`__ this binding belongs to. See `access
                tokens <https://www.twilio.com/docs/conversations/create-tokens>`__ for more details.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Bindings"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid)],
            query_params=[
                param[list[ServiceBindingEnumBindingTypeOrStr] | None]("BindingType", binding_type),
                param[list[str] | None]("Identity", identity),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListServiceBindingResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncConversationsV1BindingWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_service_binding(
        self, chat_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Remove a push notification binding from the conversation service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to delete the Binding resource from.
            sid: The SID of the Binding resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Bindings/{Sid}"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_service_binding(
        self, chat_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1ServiceServiceBinding, RawError]:
        """Fetch a push notification binding from the conversation service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Binding resource is associated
                with.
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Bindings/{Sid}"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceBinding],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_service_binding(
        self,
        chat_service_sid: str,
        *,
        binding_type: list[ServiceBindingEnumBindingTypeOrStr] | None = None,
        identity: list[str] | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListServiceBindingResponse, RawError]:
        """Retrieve a list of all push notification bindings in the conversation service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Binding resource is associated
                with.
            binding_type: The push technology used by the Binding resources to read. Can be: ``apn``, ``gcm``, ``fcm``,
                or ``twilsock``. See `push notification configuration
                <https://www.twilio.com/docs/chat/push-notification-configuration>`__ for more info.
            identity: The identity of a `Conversation User
                <https://www.twilio.com/docs/conversations/api/user-resource>`__ this binding belongs to. See `access
                tokens <https://www.twilio.com/docs/conversations/create-tokens>`__ for more details.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Bindings"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid)],
            query_params=[
                param[list[ServiceBindingEnumBindingTypeOrStr] | None]("BindingType", binding_type),
                param[list[str] | None]("Identity", identity),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListServiceBindingResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
