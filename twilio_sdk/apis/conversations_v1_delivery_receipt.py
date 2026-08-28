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
from ..models.conversations_v1_conversation_conversation_message_conversation_message_receipt import (
    ConversationsV1ConversationConversationMessageConversationMessageReceipt,
)
from ..models.list_conversation_message_receipt_response import ListConversationMessageReceiptResponse
from ..models.list_service_conversation_message_receipt_response import ListServiceConversationMessageReceiptResponse
from ..models.service_conversation_message_receipt import ServiceConversationMessageReceipt
from ..server.server import Server


class ConversationsV1DeliveryReceipt:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ConversationsV1DeliveryReceiptWithRawResponse(client, server, auth)

    def fetch_conversation_message_receipt(
        self, conversation_sid: str, message_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1ConversationConversationMessageConversationMessageReceipt:
        """Fetch the delivery and read receipts of the conversation message

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            message_sid: The SID of the message within a `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ the delivery receipt belongs
                to.
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_conversation_message_receipt(
            conversation_sid, message_sid, sid, request_options=request_options
        ).unwrap()

    def fetch_service_conversation_message_receipt(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        message_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ServiceConversationMessageReceipt:
        """Fetch the delivery and read receipts of the conversation message

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Message resource is associated
                with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            message_sid: The SID of the message within a `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ the delivery receipt belongs
                to.
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_service_conversation_message_receipt(
            chat_service_sid, conversation_sid, message_sid, sid, request_options=request_options
        ).unwrap()

    def list_conversation_message_receipt(
        self,
        conversation_sid: str,
        message_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListConversationMessageReceiptResponse:
        """Retrieve a list of all delivery and read receipts of the conversation message

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            message_sid: The SID of the message within a `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ the delivery receipt belongs
                to.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_conversation_message_receipt(
            conversation_sid,
            message_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def list_service_conversation_message_receipt(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        message_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListServiceConversationMessageReceiptResponse:
        """Retrieve a list of all delivery and read receipts of the conversation message

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Message resource is associated
                with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            message_sid: The SID of the message within a `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ the delivery receipt belongs
                to.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_service_conversation_message_receipt(
            chat_service_sid,
            conversation_sid,
            message_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> ConversationsV1DeliveryReceiptWithRawResponse:
        return self._with_raw_response


class AsyncConversationsV1DeliveryReceipt:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncConversationsV1DeliveryReceiptWithRawResponse(client, server, auth)

    async def fetch_conversation_message_receipt(
        self, conversation_sid: str, message_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1ConversationConversationMessageConversationMessageReceipt:
        """Fetch the delivery and read receipts of the conversation message

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            message_sid: The SID of the message within a `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ the delivery receipt belongs
                to.
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_conversation_message_receipt(
                conversation_sid, message_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def fetch_service_conversation_message_receipt(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        message_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ServiceConversationMessageReceipt:
        """Fetch the delivery and read receipts of the conversation message

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Message resource is associated
                with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            message_sid: The SID of the message within a `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ the delivery receipt belongs
                to.
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_service_conversation_message_receipt(
                chat_service_sid, conversation_sid, message_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def list_conversation_message_receipt(
        self,
        conversation_sid: str,
        message_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListConversationMessageReceiptResponse:
        """Retrieve a list of all delivery and read receipts of the conversation message

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            message_sid: The SID of the message within a `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ the delivery receipt belongs
                to.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_conversation_message_receipt(
                conversation_sid,
                message_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def list_service_conversation_message_receipt(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        message_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListServiceConversationMessageReceiptResponse:
        """Retrieve a list of all delivery and read receipts of the conversation message

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Message resource is associated
                with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            message_sid: The SID of the message within a `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ the delivery receipt belongs
                to.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_service_conversation_message_receipt(
                chat_service_sid,
                conversation_sid,
                message_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncConversationsV1DeliveryReceiptWithRawResponse:
        return self._with_raw_response


class ConversationsV1DeliveryReceiptWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_conversation_message_receipt(
        self, conversation_sid: str, message_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1ConversationConversationMessageConversationMessageReceipt, RawError]:
        """Fetch the delivery and read receipts of the conversation message

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            message_sid: The SID of the message within a `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ the delivery receipt belongs
                to.
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7(
                "/v1/Conversations/{ConversationSid}/Messages/{MessageSid}/Receipts/{Sid}"
            ),
            path_params=[
                param[str]("ConversationSid", conversation_sid),
                param[str]("MessageSid", message_sid),
                param[str]("Sid", sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ConversationConversationMessageConversationMessageReceipt],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_service_conversation_message_receipt(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        message_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ServiceConversationMessageReceipt, RawError]:
        """Fetch the delivery and read receipts of the conversation message

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Message resource is associated
                with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            message_sid: The SID of the message within a `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ the delivery receipt belongs
                to.
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages/{MessageSid}/Receipts/{Sid}"
            ),
            path_params=[
                param[str]("ChatServiceSid", chat_service_sid),
                param[str]("ConversationSid", conversation_sid),
                param[str]("MessageSid", message_sid),
                param[str]("Sid", sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ServiceConversationMessageReceipt],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_conversation_message_receipt(
        self,
        conversation_sid: str,
        message_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListConversationMessageReceiptResponse, RawError]:
        """Retrieve a list of all delivery and read receipts of the conversation message

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            message_sid: The SID of the message within a `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ the delivery receipt belongs
                to.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Conversations/{ConversationSid}/Messages/{MessageSid}/Receipts"),
            path_params=[param[str]("ConversationSid", conversation_sid), param[str]("MessageSid", message_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListConversationMessageReceiptResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_service_conversation_message_receipt(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        message_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListServiceConversationMessageReceiptResponse, RawError]:
        """Retrieve a list of all delivery and read receipts of the conversation message

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Message resource is associated
                with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            message_sid: The SID of the message within a `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ the delivery receipt belongs
                to.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages/{MessageSid}/Receipts"
            ),
            path_params=[
                param[str]("ChatServiceSid", chat_service_sid),
                param[str]("ConversationSid", conversation_sid),
                param[str]("MessageSid", message_sid),
            ],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListServiceConversationMessageReceiptResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncConversationsV1DeliveryReceiptWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_conversation_message_receipt(
        self, conversation_sid: str, message_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1ConversationConversationMessageConversationMessageReceipt, RawError]:
        """Fetch the delivery and read receipts of the conversation message

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            message_sid: The SID of the message within a `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ the delivery receipt belongs
                to.
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7(
                "/v1/Conversations/{ConversationSid}/Messages/{MessageSid}/Receipts/{Sid}"
            ),
            path_params=[
                param[str]("ConversationSid", conversation_sid),
                param[str]("MessageSid", message_sid),
                param[str]("Sid", sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ConversationConversationMessageConversationMessageReceipt],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_service_conversation_message_receipt(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        message_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ServiceConversationMessageReceipt, RawError]:
        """Fetch the delivery and read receipts of the conversation message

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Message resource is associated
                with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            message_sid: The SID of the message within a `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ the delivery receipt belongs
                to.
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages/{MessageSid}/Receipts/{Sid}"
            ),
            path_params=[
                param[str]("ChatServiceSid", chat_service_sid),
                param[str]("ConversationSid", conversation_sid),
                param[str]("MessageSid", message_sid),
                param[str]("Sid", sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ServiceConversationMessageReceipt],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_conversation_message_receipt(
        self,
        conversation_sid: str,
        message_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListConversationMessageReceiptResponse, RawError]:
        """Retrieve a list of all delivery and read receipts of the conversation message

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            message_sid: The SID of the message within a `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ the delivery receipt belongs
                to.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Conversations/{ConversationSid}/Messages/{MessageSid}/Receipts"),
            path_params=[param[str]("ConversationSid", conversation_sid), param[str]("MessageSid", message_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListConversationMessageReceiptResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_service_conversation_message_receipt(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        message_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListServiceConversationMessageReceiptResponse, RawError]:
        """Retrieve a list of all delivery and read receipts of the conversation message

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Message resource is associated
                with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            message_sid: The SID of the message within a `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ the delivery receipt belongs
                to.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages/{MessageSid}/Receipts"
            ),
            path_params=[
                param[str]("ChatServiceSid", chat_service_sid),
                param[str]("ConversationSid", conversation_sid),
                param[str]("MessageSid", message_sid),
            ],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListServiceConversationMessageReceiptResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
