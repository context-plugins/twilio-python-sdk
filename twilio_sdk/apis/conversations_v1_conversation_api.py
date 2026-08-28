from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    RFC3339DateTime,
    SecuredRawResponse,
    empty_response,
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.conversations_v1_conversation import ConversationsV1Conversation
from ..models.conversations_v1_service_service_conversation import ConversationsV1ServiceServiceConversation
from ..models.enums.confirmation import ConfirmationOrStr
from ..models.enums.conversation_enum_state import ConversationEnumStateOrStr
from ..models.enums.service_conversation_enum_state import ServiceConversationEnumStateOrStr
from ..models.list_conversation_response import ListConversationResponse
from ..models.list_service_conversation_response import ListServiceConversationResponse
from ..server.server import Server


class ConversationsV1ConversationApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ConversationsV1ConversationApiWithRawResponse(client, server, auth)

    def create_conversation(
        self,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        unique_name: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        messaging_service_sid: str | None = None,
        attributes: str | None = None,
        state: ConversationEnumStateOrStr | None = None,
        timers_inactive: str | None = None,
        timers_closed: str | None = None,
        bindings_email_address: str | None = None,
        bindings_email_name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1Conversation:
        """Create a new conversation in your account's default service

        Args:
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The human-readable name of this conversation, limited to 256 characters. Optional.
            unique_name: An application-defined string that uniquely identifies the resource. It can be used to address
                the resource in place of the resource's ``sid`` in the URL.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated.
            messaging_service_sid: The unique ID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ this conversation belongs to.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be
                returned.
            state: Current state of this conversation. Can be either ``initializing``, ``active``, ``inactive`` or
                ``closed`` and defaults to ``active``
            timers_inactive: ISO8601 duration when conversation will be switched to ``inactive`` state. Minimum value
                for this timer is 1 minute.
            timers_closed: ISO8601 duration when conversation will be switched to ``closed`` state. Minimum value for
                this timer is 10 minutes.
            bindings_email_address: The default email address that will be used when sending outbound emails in this
                conversation.
            bindings_email_name: The default name that will be used when sending outbound emails in this conversation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_conversation(
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
            friendly_name=friendly_name,
            unique_name=unique_name,
            date_created=date_created,
            date_updated=date_updated,
            messaging_service_sid=messaging_service_sid,
            attributes=attributes,
            state=state,
            timers_inactive=timers_inactive,
            timers_closed=timers_closed,
            bindings_email_address=bindings_email_address,
            bindings_email_name=bindings_email_name,
            request_options=request_options,
        ).unwrap()

    def create_service_conversation(
        self,
        chat_service_sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        unique_name: str | None = None,
        attributes: str | None = None,
        messaging_service_sid: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        state: ServiceConversationEnumStateOrStr | None = None,
        timers_inactive: str | None = None,
        timers_closed: str | None = None,
        bindings_email_address: str | None = None,
        bindings_email_name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceConversation:
        """Create a new conversation in your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The human-readable name of this conversation, limited to 256 characters. Optional.
            unique_name: An application-defined string that uniquely identifies the resource. It can be used to address
                the resource in place of the resource's ``sid`` in the URL.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be
                returned.
            messaging_service_sid: The unique ID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ this conversation belongs to.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated.
            state: Current state of this conversation. Can be either ``initializing``, ``active``, ``inactive`` or
                ``closed`` and defaults to ``active``
            timers_inactive: ISO8601 duration when conversation will be switched to ``inactive`` state. Minimum value
                for this timer is 1 minute.
            timers_closed: ISO8601 duration when conversation will be switched to ``closed`` state. Minimum value for
                this timer is 10 minutes.
            bindings_email_address: The default email address that will be used when sending outbound emails in this
                conversation.
            bindings_email_name: The default name that will be used when sending outbound emails in this conversation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_service_conversation(
            chat_service_sid,
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
            friendly_name=friendly_name,
            unique_name=unique_name,
            attributes=attributes,
            messaging_service_sid=messaging_service_sid,
            date_created=date_created,
            date_updated=date_updated,
            state=state,
            timers_inactive=timers_inactive,
            timers_closed=timers_closed,
            bindings_email_address=bindings_email_address,
            bindings_email_name=bindings_email_name,
            request_options=request_options,
        ).unwrap()

    def delete_conversation(
        self,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove a conversation from your account's default service

        Args:
            sid: A 34 character string that uniquely identifies this resource. Can also be the ``unique_name`` of the
                Conversation.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_conversation(
            sid, x_twilio_webhook_enabled=x_twilio_webhook_enabled, request_options=request_options
        ).unwrap()

    def delete_service_conversation(
        self,
        chat_service_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove a conversation from your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            sid: A 34 character string that uniquely identifies this resource. Can also be the ``unique_name`` of the
                Conversation.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_service_conversation(
            chat_service_sid, sid, x_twilio_webhook_enabled=x_twilio_webhook_enabled, request_options=request_options
        ).unwrap()

    def fetch_conversation(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1Conversation:
        """Fetch a conversation from your account's default service

        Args:
            sid: A 34 character string that uniquely identifies this resource. Can also be the ``unique_name`` of the
                Conversation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_conversation(sid, request_options=request_options).unwrap()

    def fetch_service_conversation(
        self, chat_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1ServiceServiceConversation:
        """Fetch a conversation from your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            sid: A 34 character string that uniquely identifies this resource. Can also be the ``unique_name`` of the
                Conversation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_service_conversation(
            chat_service_sid, sid, request_options=request_options
        ).unwrap()

    def list_conversation(
        self,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        state: ConversationEnumStateOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListConversationResponse:
        """Retrieve a list of conversations in your account's default service

        Args:
            start_date: Specifies the beginning of the date range for filtering Conversations based on their creation
                date. Conversations that were created on or after this date will be included in the results. The date
                must be in ISO8601 format, specifically starting at the beginning of the specified date
                (YYYY-MM-DDT00:00:00Z), for precise filtering. This parameter can be combined with other filters. If
                this filter is used, the returned list is sorted by latest conversation creation date in descending
                order.
            end_date: Defines the end of the date range for filtering conversations by their creation date. Only
                conversations that were created on or before this date will appear in the results. The date must be in
                ISO8601 format, specifically capturing up to the end of the specified date (YYYY-MM-DDT23:59:59Z), to
                ensure that conversations from the entire end day are included. This parameter can be combined with
                other filters. If this filter is used, the returned list is sorted by latest conversation creation date
                in descending order.
            state: State for sorting and filtering list of Conversations. Can be ``active``, ``inactive`` or ``closed``
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_conversation(
            start_date=start_date,
            end_date=end_date,
            state=state,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def list_service_conversation(
        self,
        chat_service_sid: str,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        state: ServiceConversationEnumStateOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListServiceConversationResponse:
        """Retrieve a list of conversations in your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            start_date: Specifies the beginning of the date range for filtering Conversations based on their creation
                date. Conversations that were created on or after this date will be included in the results. The date
                must be in ISO8601 format, specifically starting at the beginning of the specified date
                (YYYY-MM-DDT00:00:00Z), for precise filtering. This parameter can be combined with other filters. If
                this filter is used, the returned list is sorted by latest conversation creation date in descending
                order.
            end_date: Defines the end of the date range for filtering conversations by their creation date. Only
                conversations that were created on or before this date will appear in the results. The date must be in
                ISO8601 format, specifically capturing up to the end of the specified date (YYYY-MM-DDT23:59:59Z), to
                ensure that conversations from the entire end day are included. This parameter can be combined with
                other filters. If this filter is used, the returned list is sorted by latest conversation creation date
                in descending order.
            state: State for sorting and filtering list of Conversations. Can be ``active``, ``inactive`` or ``closed``
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_service_conversation(
            chat_service_sid,
            start_date=start_date,
            end_date=end_date,
            state=state,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_conversation(
        self,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        attributes: str | None = None,
        messaging_service_sid: str | None = None,
        state: ConversationEnumStateOrStr | None = None,
        timers_inactive: str | None = None,
        timers_closed: str | None = None,
        unique_name: str | None = None,
        bindings_email_address: str | None = None,
        bindings_email_name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1Conversation:
        """Update an existing conversation in your account's default service

        Args:
            sid: A 34 character string that uniquely identifies this resource. Can also be the ``unique_name`` of the
                Conversation.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The human-readable name of this conversation, limited to 256 characters. Optional.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be
                returned.
            messaging_service_sid: The unique ID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ this conversation belongs to.
            state: Current state of this conversation. Can be either ``initializing``, ``active``, ``inactive`` or
                ``closed`` and defaults to ``active``
            timers_inactive: ISO8601 duration when conversation will be switched to ``inactive`` state. Minimum value
                for this timer is 1 minute.
            timers_closed: ISO8601 duration when conversation will be switched to ``closed`` state. Minimum value for
                this timer is 10 minutes.
            unique_name: An application-defined string that uniquely identifies the resource. It can be used to address
                the resource in place of the resource's ``sid`` in the URL.
            bindings_email_address: The default email address that will be used when sending outbound emails in this
                conversation.
            bindings_email_name: The default name that will be used when sending outbound emails in this conversation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_conversation(
            sid,
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
            friendly_name=friendly_name,
            date_created=date_created,
            date_updated=date_updated,
            attributes=attributes,
            messaging_service_sid=messaging_service_sid,
            state=state,
            timers_inactive=timers_inactive,
            timers_closed=timers_closed,
            unique_name=unique_name,
            bindings_email_address=bindings_email_address,
            bindings_email_name=bindings_email_name,
            request_options=request_options,
        ).unwrap()

    def update_service_conversation(
        self,
        chat_service_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        attributes: str | None = None,
        messaging_service_sid: str | None = None,
        state: ServiceConversationEnumStateOrStr | None = None,
        timers_inactive: str | None = None,
        timers_closed: str | None = None,
        unique_name: str | None = None,
        bindings_email_address: str | None = None,
        bindings_email_name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceConversation:
        """Update an existing conversation in your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            sid: A 34 character string that uniquely identifies this resource. Can also be the ``unique_name`` of the
                Conversation.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The human-readable name of this conversation, limited to 256 characters. Optional.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be
                returned.
            messaging_service_sid: The unique ID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ this conversation belongs to.
            state: Current state of this conversation. Can be either ``initializing``, ``active``, ``inactive`` or
                ``closed`` and defaults to ``active``
            timers_inactive: ISO8601 duration when conversation will be switched to ``inactive`` state. Minimum value
                for this timer is 1 minute.
            timers_closed: ISO8601 duration when conversation will be switched to ``closed`` state. Minimum value for
                this timer is 10 minutes.
            unique_name: An application-defined string that uniquely identifies the resource. It can be used to address
                the resource in place of the resource's ``sid`` in the URL.
            bindings_email_address: The default email address that will be used when sending outbound emails in this
                conversation.
            bindings_email_name: The default name that will be used when sending outbound emails in this conversation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_service_conversation(
            chat_service_sid,
            sid,
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
            friendly_name=friendly_name,
            date_created=date_created,
            date_updated=date_updated,
            attributes=attributes,
            messaging_service_sid=messaging_service_sid,
            state=state,
            timers_inactive=timers_inactive,
            timers_closed=timers_closed,
            unique_name=unique_name,
            bindings_email_address=bindings_email_address,
            bindings_email_name=bindings_email_name,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> ConversationsV1ConversationApiWithRawResponse:
        return self._with_raw_response


class AsyncConversationsV1ConversationApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncConversationsV1ConversationApiWithRawResponse(client, server, auth)

    async def create_conversation(
        self,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        unique_name: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        messaging_service_sid: str | None = None,
        attributes: str | None = None,
        state: ConversationEnumStateOrStr | None = None,
        timers_inactive: str | None = None,
        timers_closed: str | None = None,
        bindings_email_address: str | None = None,
        bindings_email_name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1Conversation:
        """Create a new conversation in your account's default service

        Args:
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The human-readable name of this conversation, limited to 256 characters. Optional.
            unique_name: An application-defined string that uniquely identifies the resource. It can be used to address
                the resource in place of the resource's ``sid`` in the URL.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated.
            messaging_service_sid: The unique ID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ this conversation belongs to.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be
                returned.
            state: Current state of this conversation. Can be either ``initializing``, ``active``, ``inactive`` or
                ``closed`` and defaults to ``active``
            timers_inactive: ISO8601 duration when conversation will be switched to ``inactive`` state. Minimum value
                for this timer is 1 minute.
            timers_closed: ISO8601 duration when conversation will be switched to ``closed`` state. Minimum value for
                this timer is 10 minutes.
            bindings_email_address: The default email address that will be used when sending outbound emails in this
                conversation.
            bindings_email_name: The default name that will be used when sending outbound emails in this conversation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_conversation(
                x_twilio_webhook_enabled=x_twilio_webhook_enabled,
                friendly_name=friendly_name,
                unique_name=unique_name,
                date_created=date_created,
                date_updated=date_updated,
                messaging_service_sid=messaging_service_sid,
                attributes=attributes,
                state=state,
                timers_inactive=timers_inactive,
                timers_closed=timers_closed,
                bindings_email_address=bindings_email_address,
                bindings_email_name=bindings_email_name,
                request_options=request_options,
            )
        ).unwrap()

    async def create_service_conversation(
        self,
        chat_service_sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        unique_name: str | None = None,
        attributes: str | None = None,
        messaging_service_sid: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        state: ServiceConversationEnumStateOrStr | None = None,
        timers_inactive: str | None = None,
        timers_closed: str | None = None,
        bindings_email_address: str | None = None,
        bindings_email_name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceConversation:
        """Create a new conversation in your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The human-readable name of this conversation, limited to 256 characters. Optional.
            unique_name: An application-defined string that uniquely identifies the resource. It can be used to address
                the resource in place of the resource's ``sid`` in the URL.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be
                returned.
            messaging_service_sid: The unique ID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ this conversation belongs to.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated.
            state: Current state of this conversation. Can be either ``initializing``, ``active``, ``inactive`` or
                ``closed`` and defaults to ``active``
            timers_inactive: ISO8601 duration when conversation will be switched to ``inactive`` state. Minimum value
                for this timer is 1 minute.
            timers_closed: ISO8601 duration when conversation will be switched to ``closed`` state. Minimum value for
                this timer is 10 minutes.
            bindings_email_address: The default email address that will be used when sending outbound emails in this
                conversation.
            bindings_email_name: The default name that will be used when sending outbound emails in this conversation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_service_conversation(
                chat_service_sid,
                x_twilio_webhook_enabled=x_twilio_webhook_enabled,
                friendly_name=friendly_name,
                unique_name=unique_name,
                attributes=attributes,
                messaging_service_sid=messaging_service_sid,
                date_created=date_created,
                date_updated=date_updated,
                state=state,
                timers_inactive=timers_inactive,
                timers_closed=timers_closed,
                bindings_email_address=bindings_email_address,
                bindings_email_name=bindings_email_name,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_conversation(
        self,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove a conversation from your account's default service

        Args:
            sid: A 34 character string that uniquely identifies this resource. Can also be the ``unique_name`` of the
                Conversation.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_conversation(
                sid, x_twilio_webhook_enabled=x_twilio_webhook_enabled, request_options=request_options
            )
        ).unwrap()

    async def delete_service_conversation(
        self,
        chat_service_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove a conversation from your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            sid: A 34 character string that uniquely identifies this resource. Can also be the ``unique_name`` of the
                Conversation.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_service_conversation(
                chat_service_sid,
                sid,
                x_twilio_webhook_enabled=x_twilio_webhook_enabled,
                request_options=request_options,
            )
        ).unwrap()

    async def fetch_conversation(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1Conversation:
        """Fetch a conversation from your account's default service

        Args:
            sid: A 34 character string that uniquely identifies this resource. Can also be the ``unique_name`` of the
                Conversation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_conversation(sid, request_options=request_options)).unwrap()

    async def fetch_service_conversation(
        self, chat_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1ServiceServiceConversation:
        """Fetch a conversation from your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            sid: A 34 character string that uniquely identifies this resource. Can also be the ``unique_name`` of the
                Conversation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_service_conversation(
                chat_service_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def list_conversation(
        self,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        state: ConversationEnumStateOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListConversationResponse:
        """Retrieve a list of conversations in your account's default service

        Args:
            start_date: Specifies the beginning of the date range for filtering Conversations based on their creation
                date. Conversations that were created on or after this date will be included in the results. The date
                must be in ISO8601 format, specifically starting at the beginning of the specified date
                (YYYY-MM-DDT00:00:00Z), for precise filtering. This parameter can be combined with other filters. If
                this filter is used, the returned list is sorted by latest conversation creation date in descending
                order.
            end_date: Defines the end of the date range for filtering conversations by their creation date. Only
                conversations that were created on or before this date will appear in the results. The date must be in
                ISO8601 format, specifically capturing up to the end of the specified date (YYYY-MM-DDT23:59:59Z), to
                ensure that conversations from the entire end day are included. This parameter can be combined with
                other filters. If this filter is used, the returned list is sorted by latest conversation creation date
                in descending order.
            state: State for sorting and filtering list of Conversations. Can be ``active``, ``inactive`` or ``closed``
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_conversation(
                start_date=start_date,
                end_date=end_date,
                state=state,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def list_service_conversation(
        self,
        chat_service_sid: str,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        state: ServiceConversationEnumStateOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListServiceConversationResponse:
        """Retrieve a list of conversations in your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            start_date: Specifies the beginning of the date range for filtering Conversations based on their creation
                date. Conversations that were created on or after this date will be included in the results. The date
                must be in ISO8601 format, specifically starting at the beginning of the specified date
                (YYYY-MM-DDT00:00:00Z), for precise filtering. This parameter can be combined with other filters. If
                this filter is used, the returned list is sorted by latest conversation creation date in descending
                order.
            end_date: Defines the end of the date range for filtering conversations by their creation date. Only
                conversations that were created on or before this date will appear in the results. The date must be in
                ISO8601 format, specifically capturing up to the end of the specified date (YYYY-MM-DDT23:59:59Z), to
                ensure that conversations from the entire end day are included. This parameter can be combined with
                other filters. If this filter is used, the returned list is sorted by latest conversation creation date
                in descending order.
            state: State for sorting and filtering list of Conversations. Can be ``active``, ``inactive`` or ``closed``
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_service_conversation(
                chat_service_sid,
                start_date=start_date,
                end_date=end_date,
                state=state,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_conversation(
        self,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        attributes: str | None = None,
        messaging_service_sid: str | None = None,
        state: ConversationEnumStateOrStr | None = None,
        timers_inactive: str | None = None,
        timers_closed: str | None = None,
        unique_name: str | None = None,
        bindings_email_address: str | None = None,
        bindings_email_name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1Conversation:
        """Update an existing conversation in your account's default service

        Args:
            sid: A 34 character string that uniquely identifies this resource. Can also be the ``unique_name`` of the
                Conversation.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The human-readable name of this conversation, limited to 256 characters. Optional.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be
                returned.
            messaging_service_sid: The unique ID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ this conversation belongs to.
            state: Current state of this conversation. Can be either ``initializing``, ``active``, ``inactive`` or
                ``closed`` and defaults to ``active``
            timers_inactive: ISO8601 duration when conversation will be switched to ``inactive`` state. Minimum value
                for this timer is 1 minute.
            timers_closed: ISO8601 duration when conversation will be switched to ``closed`` state. Minimum value for
                this timer is 10 minutes.
            unique_name: An application-defined string that uniquely identifies the resource. It can be used to address
                the resource in place of the resource's ``sid`` in the URL.
            bindings_email_address: The default email address that will be used when sending outbound emails in this
                conversation.
            bindings_email_name: The default name that will be used when sending outbound emails in this conversation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_conversation(
                sid,
                x_twilio_webhook_enabled=x_twilio_webhook_enabled,
                friendly_name=friendly_name,
                date_created=date_created,
                date_updated=date_updated,
                attributes=attributes,
                messaging_service_sid=messaging_service_sid,
                state=state,
                timers_inactive=timers_inactive,
                timers_closed=timers_closed,
                unique_name=unique_name,
                bindings_email_address=bindings_email_address,
                bindings_email_name=bindings_email_name,
                request_options=request_options,
            )
        ).unwrap()

    async def update_service_conversation(
        self,
        chat_service_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        attributes: str | None = None,
        messaging_service_sid: str | None = None,
        state: ServiceConversationEnumStateOrStr | None = None,
        timers_inactive: str | None = None,
        timers_closed: str | None = None,
        unique_name: str | None = None,
        bindings_email_address: str | None = None,
        bindings_email_name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceConversation:
        """Update an existing conversation in your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            sid: A 34 character string that uniquely identifies this resource. Can also be the ``unique_name`` of the
                Conversation.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The human-readable name of this conversation, limited to 256 characters. Optional.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be
                returned.
            messaging_service_sid: The unique ID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ this conversation belongs to.
            state: Current state of this conversation. Can be either ``initializing``, ``active``, ``inactive`` or
                ``closed`` and defaults to ``active``
            timers_inactive: ISO8601 duration when conversation will be switched to ``inactive`` state. Minimum value
                for this timer is 1 minute.
            timers_closed: ISO8601 duration when conversation will be switched to ``closed`` state. Minimum value for
                this timer is 10 minutes.
            unique_name: An application-defined string that uniquely identifies the resource. It can be used to address
                the resource in place of the resource's ``sid`` in the URL.
            bindings_email_address: The default email address that will be used when sending outbound emails in this
                conversation.
            bindings_email_name: The default name that will be used when sending outbound emails in this conversation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_service_conversation(
                chat_service_sid,
                sid,
                x_twilio_webhook_enabled=x_twilio_webhook_enabled,
                friendly_name=friendly_name,
                date_created=date_created,
                date_updated=date_updated,
                attributes=attributes,
                messaging_service_sid=messaging_service_sid,
                state=state,
                timers_inactive=timers_inactive,
                timers_closed=timers_closed,
                unique_name=unique_name,
                bindings_email_address=bindings_email_address,
                bindings_email_name=bindings_email_name,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncConversationsV1ConversationApiWithRawResponse:
        return self._with_raw_response


class ConversationsV1ConversationApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_conversation(
        self,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        unique_name: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        messaging_service_sid: str | None = None,
        attributes: str | None = None,
        state: ConversationEnumStateOrStr | None = None,
        timers_inactive: str | None = None,
        timers_closed: str | None = None,
        bindings_email_address: str | None = None,
        bindings_email_name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1Conversation, RawError]:
        """Create a new conversation in your account's default service

        Args:
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The human-readable name of this conversation, limited to 256 characters. Optional.
            unique_name: An application-defined string that uniquely identifies the resource. It can be used to address
                the resource in place of the resource's ``sid`` in the URL.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated.
            messaging_service_sid: The unique ID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ this conversation belongs to.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be
                returned.
            state: Current state of this conversation. Can be either ``initializing``, ``active``, ``inactive`` or
                ``closed`` and defaults to ``active``
            timers_inactive: ISO8601 duration when conversation will be switched to ``inactive`` state. Minimum value
                for this timer is 1 minute.
            timers_closed: ISO8601 duration when conversation will be switched to ``closed`` state. Minimum value for
                this timer is 10 minutes.
            bindings_email_address: The default email address that will be used when sending outbound emails in this
                conversation.
            bindings_email_name: The default name that will be used when sending outbound emails in this conversation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Conversations"),
            headers=[param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled)],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("UniqueName", unique_name),
                    param[RFC3339DateTime | None]("DateCreated", date_created),
                    param[RFC3339DateTime | None]("DateUpdated", date_updated),
                    param[str | None]("MessagingServiceSid", messaging_service_sid),
                    param[str | None]("Attributes", attributes),
                    param[ConversationEnumStateOrStr | None]("State", state),
                    param[str | None]("Timers.Inactive", timers_inactive),
                    param[str | None]("Timers.Closed", timers_closed),
                    param[str | None]("Bindings.Email.Address", bindings_email_address),
                    param[str | None]("Bindings.Email.Name", bindings_email_name),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1Conversation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_service_conversation(
        self,
        chat_service_sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        unique_name: str | None = None,
        attributes: str | None = None,
        messaging_service_sid: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        state: ServiceConversationEnumStateOrStr | None = None,
        timers_inactive: str | None = None,
        timers_closed: str | None = None,
        bindings_email_address: str | None = None,
        bindings_email_name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceConversation, RawError]:
        """Create a new conversation in your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The human-readable name of this conversation, limited to 256 characters. Optional.
            unique_name: An application-defined string that uniquely identifies the resource. It can be used to address
                the resource in place of the resource's ``sid`` in the URL.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be
                returned.
            messaging_service_sid: The unique ID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ this conversation belongs to.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated.
            state: Current state of this conversation. Can be either ``initializing``, ``active``, ``inactive`` or
                ``closed`` and defaults to ``active``
            timers_inactive: ISO8601 duration when conversation will be switched to ``inactive`` state. Minimum value
                for this timer is 1 minute.
            timers_closed: ISO8601 duration when conversation will be switched to ``closed`` state. Minimum value for
                this timer is 10 minutes.
            bindings_email_address: The default email address that will be used when sending outbound emails in this
                conversation.
            bindings_email_name: The default name that will be used when sending outbound emails in this conversation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Conversations"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid)],
            headers=[param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled)],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("UniqueName", unique_name),
                    param[str | None]("Attributes", attributes),
                    param[str | None]("MessagingServiceSid", messaging_service_sid),
                    param[RFC3339DateTime | None]("DateCreated", date_created),
                    param[RFC3339DateTime | None]("DateUpdated", date_updated),
                    param[ServiceConversationEnumStateOrStr | None]("State", state),
                    param[str | None]("Timers.Inactive", timers_inactive),
                    param[str | None]("Timers.Closed", timers_closed),
                    param[str | None]("Bindings.Email.Address", bindings_email_address),
                    param[str | None]("Bindings.Email.Name", bindings_email_name),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConversation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_conversation(
        self,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Remove a conversation from your account's default service

        Args:
            sid: A 34 character string that uniquely identifies this resource. Can also be the ``unique_name`` of the
                Conversation.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7("/v1/Conversations/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_service_conversation(
        self,
        chat_service_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Remove a conversation from your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            sid: A 34 character string that uniquely identifies this resource. Can also be the ``unique_name`` of the
                Conversation.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Conversations/{Sid}"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid), param[str]("Sid", sid)],
            headers=[param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_conversation(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1Conversation, RawError]:
        """Fetch a conversation from your account's default service

        Args:
            sid: A 34 character string that uniquely identifies this resource. Can also be the ``unique_name`` of the
                Conversation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Conversations/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1Conversation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_service_conversation(
        self, chat_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1ServiceServiceConversation, RawError]:
        """Fetch a conversation from your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            sid: A 34 character string that uniquely identifies this resource. Can also be the ``unique_name`` of the
                Conversation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Conversations/{Sid}"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConversation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_conversation(
        self,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        state: ConversationEnumStateOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListConversationResponse, RawError]:
        """Retrieve a list of conversations in your account's default service

        Args:
            start_date: Specifies the beginning of the date range for filtering Conversations based on their creation
                date. Conversations that were created on or after this date will be included in the results. The date
                must be in ISO8601 format, specifically starting at the beginning of the specified date
                (YYYY-MM-DDT00:00:00Z), for precise filtering. This parameter can be combined with other filters. If
                this filter is used, the returned list is sorted by latest conversation creation date in descending
                order.
            end_date: Defines the end of the date range for filtering conversations by their creation date. Only
                conversations that were created on or before this date will appear in the results. The date must be in
                ISO8601 format, specifically capturing up to the end of the specified date (YYYY-MM-DDT23:59:59Z), to
                ensure that conversations from the entire end day are included. This parameter can be combined with
                other filters. If this filter is used, the returned list is sorted by latest conversation creation date
                in descending order.
            state: State for sorting and filtering list of Conversations. Can be ``active``, ``inactive`` or ``closed``
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Conversations"),
            query_params=[
                param[str | None]("StartDate", start_date),
                param[str | None]("EndDate", end_date),
                param[ConversationEnumStateOrStr | None]("State", state),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListConversationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_service_conversation(
        self,
        chat_service_sid: str,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        state: ServiceConversationEnumStateOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListServiceConversationResponse, RawError]:
        """Retrieve a list of conversations in your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            start_date: Specifies the beginning of the date range for filtering Conversations based on their creation
                date. Conversations that were created on or after this date will be included in the results. The date
                must be in ISO8601 format, specifically starting at the beginning of the specified date
                (YYYY-MM-DDT00:00:00Z), for precise filtering. This parameter can be combined with other filters. If
                this filter is used, the returned list is sorted by latest conversation creation date in descending
                order.
            end_date: Defines the end of the date range for filtering conversations by their creation date. Only
                conversations that were created on or before this date will appear in the results. The date must be in
                ISO8601 format, specifically capturing up to the end of the specified date (YYYY-MM-DDT23:59:59Z), to
                ensure that conversations from the entire end day are included. This parameter can be combined with
                other filters. If this filter is used, the returned list is sorted by latest conversation creation date
                in descending order.
            state: State for sorting and filtering list of Conversations. Can be ``active``, ``inactive`` or ``closed``
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Conversations"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid)],
            query_params=[
                param[str | None]("StartDate", start_date),
                param[str | None]("EndDate", end_date),
                param[ServiceConversationEnumStateOrStr | None]("State", state),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListServiceConversationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_conversation(
        self,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        attributes: str | None = None,
        messaging_service_sid: str | None = None,
        state: ConversationEnumStateOrStr | None = None,
        timers_inactive: str | None = None,
        timers_closed: str | None = None,
        unique_name: str | None = None,
        bindings_email_address: str | None = None,
        bindings_email_name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1Conversation, RawError]:
        """Update an existing conversation in your account's default service

        Args:
            sid: A 34 character string that uniquely identifies this resource. Can also be the ``unique_name`` of the
                Conversation.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The human-readable name of this conversation, limited to 256 characters. Optional.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be
                returned.
            messaging_service_sid: The unique ID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ this conversation belongs to.
            state: Current state of this conversation. Can be either ``initializing``, ``active``, ``inactive`` or
                ``closed`` and defaults to ``active``
            timers_inactive: ISO8601 duration when conversation will be switched to ``inactive`` state. Minimum value
                for this timer is 1 minute.
            timers_closed: ISO8601 duration when conversation will be switched to ``closed`` state. Minimum value for
                this timer is 10 minutes.
            unique_name: An application-defined string that uniquely identifies the resource. It can be used to address
                the resource in place of the resource's ``sid`` in the URL.
            bindings_email_address: The default email address that will be used when sending outbound emails in this
                conversation.
            bindings_email_name: The default name that will be used when sending outbound emails in this conversation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Conversations/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled)],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[RFC3339DateTime | None]("DateCreated", date_created),
                    param[RFC3339DateTime | None]("DateUpdated", date_updated),
                    param[str | None]("Attributes", attributes),
                    param[str | None]("MessagingServiceSid", messaging_service_sid),
                    param[ConversationEnumStateOrStr | None]("State", state),
                    param[str | None]("Timers.Inactive", timers_inactive),
                    param[str | None]("Timers.Closed", timers_closed),
                    param[str | None]("UniqueName", unique_name),
                    param[str | None]("Bindings.Email.Address", bindings_email_address),
                    param[str | None]("Bindings.Email.Name", bindings_email_name),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1Conversation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_service_conversation(
        self,
        chat_service_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        attributes: str | None = None,
        messaging_service_sid: str | None = None,
        state: ServiceConversationEnumStateOrStr | None = None,
        timers_inactive: str | None = None,
        timers_closed: str | None = None,
        unique_name: str | None = None,
        bindings_email_address: str | None = None,
        bindings_email_name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceConversation, RawError]:
        """Update an existing conversation in your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            sid: A 34 character string that uniquely identifies this resource. Can also be the ``unique_name`` of the
                Conversation.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The human-readable name of this conversation, limited to 256 characters. Optional.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be
                returned.
            messaging_service_sid: The unique ID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ this conversation belongs to.
            state: Current state of this conversation. Can be either ``initializing``, ``active``, ``inactive`` or
                ``closed`` and defaults to ``active``
            timers_inactive: ISO8601 duration when conversation will be switched to ``inactive`` state. Minimum value
                for this timer is 1 minute.
            timers_closed: ISO8601 duration when conversation will be switched to ``closed`` state. Minimum value for
                this timer is 10 minutes.
            unique_name: An application-defined string that uniquely identifies the resource. It can be used to address
                the resource in place of the resource's ``sid`` in the URL.
            bindings_email_address: The default email address that will be used when sending outbound emails in this
                conversation.
            bindings_email_name: The default name that will be used when sending outbound emails in this conversation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Conversations/{Sid}"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid), param[str]("Sid", sid)],
            headers=[param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled)],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[RFC3339DateTime | None]("DateCreated", date_created),
                    param[RFC3339DateTime | None]("DateUpdated", date_updated),
                    param[str | None]("Attributes", attributes),
                    param[str | None]("MessagingServiceSid", messaging_service_sid),
                    param[ServiceConversationEnumStateOrStr | None]("State", state),
                    param[str | None]("Timers.Inactive", timers_inactive),
                    param[str | None]("Timers.Closed", timers_closed),
                    param[str | None]("UniqueName", unique_name),
                    param[str | None]("Bindings.Email.Address", bindings_email_address),
                    param[str | None]("Bindings.Email.Name", bindings_email_name),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConversation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncConversationsV1ConversationApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_conversation(
        self,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        unique_name: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        messaging_service_sid: str | None = None,
        attributes: str | None = None,
        state: ConversationEnumStateOrStr | None = None,
        timers_inactive: str | None = None,
        timers_closed: str | None = None,
        bindings_email_address: str | None = None,
        bindings_email_name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1Conversation, RawError]:
        """Create a new conversation in your account's default service

        Args:
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The human-readable name of this conversation, limited to 256 characters. Optional.
            unique_name: An application-defined string that uniquely identifies the resource. It can be used to address
                the resource in place of the resource's ``sid`` in the URL.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated.
            messaging_service_sid: The unique ID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ this conversation belongs to.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be
                returned.
            state: Current state of this conversation. Can be either ``initializing``, ``active``, ``inactive`` or
                ``closed`` and defaults to ``active``
            timers_inactive: ISO8601 duration when conversation will be switched to ``inactive`` state. Minimum value
                for this timer is 1 minute.
            timers_closed: ISO8601 duration when conversation will be switched to ``closed`` state. Minimum value for
                this timer is 10 minutes.
            bindings_email_address: The default email address that will be used when sending outbound emails in this
                conversation.
            bindings_email_name: The default name that will be used when sending outbound emails in this conversation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Conversations"),
            headers=[param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled)],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("UniqueName", unique_name),
                    param[RFC3339DateTime | None]("DateCreated", date_created),
                    param[RFC3339DateTime | None]("DateUpdated", date_updated),
                    param[str | None]("MessagingServiceSid", messaging_service_sid),
                    param[str | None]("Attributes", attributes),
                    param[ConversationEnumStateOrStr | None]("State", state),
                    param[str | None]("Timers.Inactive", timers_inactive),
                    param[str | None]("Timers.Closed", timers_closed),
                    param[str | None]("Bindings.Email.Address", bindings_email_address),
                    param[str | None]("Bindings.Email.Name", bindings_email_name),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1Conversation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_service_conversation(
        self,
        chat_service_sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        unique_name: str | None = None,
        attributes: str | None = None,
        messaging_service_sid: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        state: ServiceConversationEnumStateOrStr | None = None,
        timers_inactive: str | None = None,
        timers_closed: str | None = None,
        bindings_email_address: str | None = None,
        bindings_email_name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceConversation, RawError]:
        """Create a new conversation in your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The human-readable name of this conversation, limited to 256 characters. Optional.
            unique_name: An application-defined string that uniquely identifies the resource. It can be used to address
                the resource in place of the resource's ``sid`` in the URL.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be
                returned.
            messaging_service_sid: The unique ID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ this conversation belongs to.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated.
            state: Current state of this conversation. Can be either ``initializing``, ``active``, ``inactive`` or
                ``closed`` and defaults to ``active``
            timers_inactive: ISO8601 duration when conversation will be switched to ``inactive`` state. Minimum value
                for this timer is 1 minute.
            timers_closed: ISO8601 duration when conversation will be switched to ``closed`` state. Minimum value for
                this timer is 10 minutes.
            bindings_email_address: The default email address that will be used when sending outbound emails in this
                conversation.
            bindings_email_name: The default name that will be used when sending outbound emails in this conversation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Conversations"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid)],
            headers=[param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled)],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("UniqueName", unique_name),
                    param[str | None]("Attributes", attributes),
                    param[str | None]("MessagingServiceSid", messaging_service_sid),
                    param[RFC3339DateTime | None]("DateCreated", date_created),
                    param[RFC3339DateTime | None]("DateUpdated", date_updated),
                    param[ServiceConversationEnumStateOrStr | None]("State", state),
                    param[str | None]("Timers.Inactive", timers_inactive),
                    param[str | None]("Timers.Closed", timers_closed),
                    param[str | None]("Bindings.Email.Address", bindings_email_address),
                    param[str | None]("Bindings.Email.Name", bindings_email_name),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConversation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_conversation(
        self,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Remove a conversation from your account's default service

        Args:
            sid: A 34 character string that uniquely identifies this resource. Can also be the ``unique_name`` of the
                Conversation.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7("/v1/Conversations/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_service_conversation(
        self,
        chat_service_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Remove a conversation from your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            sid: A 34 character string that uniquely identifies this resource. Can also be the ``unique_name`` of the
                Conversation.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Conversations/{Sid}"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid), param[str]("Sid", sid)],
            headers=[param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_conversation(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1Conversation, RawError]:
        """Fetch a conversation from your account's default service

        Args:
            sid: A 34 character string that uniquely identifies this resource. Can also be the ``unique_name`` of the
                Conversation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Conversations/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1Conversation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_service_conversation(
        self, chat_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1ServiceServiceConversation, RawError]:
        """Fetch a conversation from your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            sid: A 34 character string that uniquely identifies this resource. Can also be the ``unique_name`` of the
                Conversation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Conversations/{Sid}"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConversation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_conversation(
        self,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        state: ConversationEnumStateOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListConversationResponse, RawError]:
        """Retrieve a list of conversations in your account's default service

        Args:
            start_date: Specifies the beginning of the date range for filtering Conversations based on their creation
                date. Conversations that were created on or after this date will be included in the results. The date
                must be in ISO8601 format, specifically starting at the beginning of the specified date
                (YYYY-MM-DDT00:00:00Z), for precise filtering. This parameter can be combined with other filters. If
                this filter is used, the returned list is sorted by latest conversation creation date in descending
                order.
            end_date: Defines the end of the date range for filtering conversations by their creation date. Only
                conversations that were created on or before this date will appear in the results. The date must be in
                ISO8601 format, specifically capturing up to the end of the specified date (YYYY-MM-DDT23:59:59Z), to
                ensure that conversations from the entire end day are included. This parameter can be combined with
                other filters. If this filter is used, the returned list is sorted by latest conversation creation date
                in descending order.
            state: State for sorting and filtering list of Conversations. Can be ``active``, ``inactive`` or ``closed``
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Conversations"),
            query_params=[
                param[str | None]("StartDate", start_date),
                param[str | None]("EndDate", end_date),
                param[ConversationEnumStateOrStr | None]("State", state),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListConversationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_service_conversation(
        self,
        chat_service_sid: str,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        state: ServiceConversationEnumStateOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListServiceConversationResponse, RawError]:
        """Retrieve a list of conversations in your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            start_date: Specifies the beginning of the date range for filtering Conversations based on their creation
                date. Conversations that were created on or after this date will be included in the results. The date
                must be in ISO8601 format, specifically starting at the beginning of the specified date
                (YYYY-MM-DDT00:00:00Z), for precise filtering. This parameter can be combined with other filters. If
                this filter is used, the returned list is sorted by latest conversation creation date in descending
                order.
            end_date: Defines the end of the date range for filtering conversations by their creation date. Only
                conversations that were created on or before this date will appear in the results. The date must be in
                ISO8601 format, specifically capturing up to the end of the specified date (YYYY-MM-DDT23:59:59Z), to
                ensure that conversations from the entire end day are included. This parameter can be combined with
                other filters. If this filter is used, the returned list is sorted by latest conversation creation date
                in descending order.
            state: State for sorting and filtering list of Conversations. Can be ``active``, ``inactive`` or ``closed``
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Conversations"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid)],
            query_params=[
                param[str | None]("StartDate", start_date),
                param[str | None]("EndDate", end_date),
                param[ServiceConversationEnumStateOrStr | None]("State", state),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListServiceConversationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_conversation(
        self,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        attributes: str | None = None,
        messaging_service_sid: str | None = None,
        state: ConversationEnumStateOrStr | None = None,
        timers_inactive: str | None = None,
        timers_closed: str | None = None,
        unique_name: str | None = None,
        bindings_email_address: str | None = None,
        bindings_email_name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1Conversation, RawError]:
        """Update an existing conversation in your account's default service

        Args:
            sid: A 34 character string that uniquely identifies this resource. Can also be the ``unique_name`` of the
                Conversation.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The human-readable name of this conversation, limited to 256 characters. Optional.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be
                returned.
            messaging_service_sid: The unique ID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ this conversation belongs to.
            state: Current state of this conversation. Can be either ``initializing``, ``active``, ``inactive`` or
                ``closed`` and defaults to ``active``
            timers_inactive: ISO8601 duration when conversation will be switched to ``inactive`` state. Minimum value
                for this timer is 1 minute.
            timers_closed: ISO8601 duration when conversation will be switched to ``closed`` state. Minimum value for
                this timer is 10 minutes.
            unique_name: An application-defined string that uniquely identifies the resource. It can be used to address
                the resource in place of the resource's ``sid`` in the URL.
            bindings_email_address: The default email address that will be used when sending outbound emails in this
                conversation.
            bindings_email_name: The default name that will be used when sending outbound emails in this conversation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Conversations/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled)],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[RFC3339DateTime | None]("DateCreated", date_created),
                    param[RFC3339DateTime | None]("DateUpdated", date_updated),
                    param[str | None]("Attributes", attributes),
                    param[str | None]("MessagingServiceSid", messaging_service_sid),
                    param[ConversationEnumStateOrStr | None]("State", state),
                    param[str | None]("Timers.Inactive", timers_inactive),
                    param[str | None]("Timers.Closed", timers_closed),
                    param[str | None]("UniqueName", unique_name),
                    param[str | None]("Bindings.Email.Address", bindings_email_address),
                    param[str | None]("Bindings.Email.Name", bindings_email_name),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1Conversation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_service_conversation(
        self,
        chat_service_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        attributes: str | None = None,
        messaging_service_sid: str | None = None,
        state: ServiceConversationEnumStateOrStr | None = None,
        timers_inactive: str | None = None,
        timers_closed: str | None = None,
        unique_name: str | None = None,
        bindings_email_address: str | None = None,
        bindings_email_name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceConversation, RawError]:
        """Update an existing conversation in your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            sid: A 34 character string that uniquely identifies this resource. Can also be the ``unique_name`` of the
                Conversation.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The human-readable name of this conversation, limited to 256 characters. Optional.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be
                returned.
            messaging_service_sid: The unique ID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ this conversation belongs to.
            state: Current state of this conversation. Can be either ``initializing``, ``active``, ``inactive`` or
                ``closed`` and defaults to ``active``
            timers_inactive: ISO8601 duration when conversation will be switched to ``inactive`` state. Minimum value
                for this timer is 1 minute.
            timers_closed: ISO8601 duration when conversation will be switched to ``closed`` state. Minimum value for
                this timer is 10 minutes.
            unique_name: An application-defined string that uniquely identifies the resource. It can be used to address
                the resource in place of the resource's ``sid`` in the URL.
            bindings_email_address: The default email address that will be used when sending outbound emails in this
                conversation.
            bindings_email_name: The default name that will be used when sending outbound emails in this conversation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Conversations/{Sid}"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid), param[str]("Sid", sid)],
            headers=[param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled)],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[RFC3339DateTime | None]("DateCreated", date_created),
                    param[RFC3339DateTime | None]("DateUpdated", date_updated),
                    param[str | None]("Attributes", attributes),
                    param[str | None]("MessagingServiceSid", messaging_service_sid),
                    param[ServiceConversationEnumStateOrStr | None]("State", state),
                    param[str | None]("Timers.Inactive", timers_inactive),
                    param[str | None]("Timers.Closed", timers_closed),
                    param[str | None]("UniqueName", unique_name),
                    param[str | None]("Bindings.Email.Address", bindings_email_address),
                    param[str | None]("Bindings.Email.Name", bindings_email_name),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConversation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
