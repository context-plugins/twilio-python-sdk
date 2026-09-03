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
from ..models.conversations_v1_service_service_user import ConversationsV1ServiceServiceUser
from ..models.conversations_v1_user import ConversationsV1User
from ..models.enums.confirmation import ConfirmationOrStr
from ..models.list_service_user_response import ListServiceUserResponse
from ..models.list_user_response import ListUserResponse
from ..server.server import Server


class ConversationsV1UserApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ConversationsV1UserApiWithRawResponse(client, server, auth)

    def create_service_user(
        self,
        chat_service_sid: str,
        identity: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        attributes: str | None = None,
        role_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceUser:
        """Add a new conversation user to your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the User resource is associated
                with.
            identity: The application-defined string that uniquely identifies the resource's User within the
                `Conversation Service <https://www.twilio.com/docs/conversations/api/service-resource>`__. This value is
                often a username or an email address, and is case-sensitive.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The string that you assigned to describe the resource.
            attributes: The JSON Object string that stores application-specific data. If attributes have not been set,
                ``{}`` is returned.
            role_sid: The SID of a service-level `Role <https://www.twilio.com/docs/conversations/api/role-resource>`__
                to assign to the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_service_user(
            chat_service_sid,
            identity,
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
            friendly_name=friendly_name,
            attributes=attributes,
            role_sid=role_sid,
            request_options=request_options,
        ).unwrap()

    def create_user(
        self,
        identity: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        attributes: str | None = None,
        role_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1User:
        """Add a new conversation user to your account's default service

        Args:
            identity: The application-defined string that uniquely identifies the resource's User within the
                `Conversation Service <https://www.twilio.com/docs/conversations/api/service-resource>`__. This value is
                often a username or an email address, and is case-sensitive.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The string that you assigned to describe the resource.
            attributes: The JSON Object string that stores application-specific data. If attributes have not been set,
                ``{}`` is returned.
            role_sid: The SID of a service-level `Role <https://www.twilio.com/docs/conversations/api/role-resource>`__
                to assign to the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_user(
            identity,
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
            friendly_name=friendly_name,
            attributes=attributes,
            role_sid=role_sid,
            request_options=request_options,
        ).unwrap()

    def delete_service_user(
        self,
        chat_service_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove a conversation user from your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to delete the User resource from.
            sid: The SID of the User resource to delete. This value can be either the ``sid`` or the ``identity`` of the
                User resource to delete.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_service_user(
            chat_service_sid, sid, x_twilio_webhook_enabled=x_twilio_webhook_enabled, request_options=request_options
        ).unwrap()

    def delete_user(
        self,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove a conversation user from your account's default service

        Args:
            sid: The SID of the User resource to delete. This value can be either the ``sid`` or the ``identity`` of the
                User resource to delete.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_user(
            sid, x_twilio_webhook_enabled=x_twilio_webhook_enabled, request_options=request_options
        ).unwrap()

    def fetch_service_user(
        self, chat_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1ServiceServiceUser:
        """Fetch a conversation user from your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to fetch the User resource from.
            sid: The SID of the User resource to fetch. This value can be either the ``sid`` or the ``identity`` of the
                User resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_service_user(
            chat_service_sid, sid, request_options=request_options
        ).unwrap()

    def fetch_user(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> ConversationsV1User:
        """Fetch a conversation user from your account's default service

        Args:
            sid: The SID of the User resource to fetch. This value can be either the ``sid`` or the ``identity`` of the
                User resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_user(sid, request_options=request_options).unwrap()

    def list_service_user(
        self,
        chat_service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListServiceUserResponse:
        """Retrieve a list of all conversation users in your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to read the User resources from.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_service_user(
            chat_service_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    def list_user(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListUserResponse:
        """Retrieve a list of all conversation users in your account's default service

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_user(
            page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    def update_service_user(
        self,
        chat_service_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        attributes: str | None = None,
        role_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceUser:
        """Update an existing conversation user in your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the User resource is associated
                with.
            sid: The SID of the User resource to update. This value can be either the ``sid`` or the ``identity`` of the
                User resource to update.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The string that you assigned to describe the resource.
            attributes: The JSON Object string that stores application-specific data. If attributes have not been set,
                ``{}`` is returned.
            role_sid: The SID of a service-level `Role <https://www.twilio.com/docs/conversations/api/role-resource>`__
                to assign to the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_service_user(
            chat_service_sid,
            sid,
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
            friendly_name=friendly_name,
            attributes=attributes,
            role_sid=role_sid,
            request_options=request_options,
        ).unwrap()

    def update_user(
        self,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        attributes: str | None = None,
        role_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1User:
        """Update an existing conversation user in your account's default service

        Args:
            sid: The SID of the User resource to update. This value can be either the ``sid`` or the ``identity`` of the
                User resource to update.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The string that you assigned to describe the resource.
            attributes: The JSON Object string that stores application-specific data. If attributes have not been set,
                ``{}`` is returned.
            role_sid: The SID of a service-level `Role <https://www.twilio.com/docs/conversations/api/role-resource>`__
                to assign to the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_user(
            sid,
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
            friendly_name=friendly_name,
            attributes=attributes,
            role_sid=role_sid,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> ConversationsV1UserApiWithRawResponse:
        return self._with_raw_response


class AsyncConversationsV1UserApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncConversationsV1UserApiWithRawResponse(client, server, auth)

    async def create_service_user(
        self,
        chat_service_sid: str,
        identity: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        attributes: str | None = None,
        role_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceUser:
        """Add a new conversation user to your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the User resource is associated
                with.
            identity: The application-defined string that uniquely identifies the resource's User within the
                `Conversation Service <https://www.twilio.com/docs/conversations/api/service-resource>`__. This value is
                often a username or an email address, and is case-sensitive.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The string that you assigned to describe the resource.
            attributes: The JSON Object string that stores application-specific data. If attributes have not been set,
                ``{}`` is returned.
            role_sid: The SID of a service-level `Role <https://www.twilio.com/docs/conversations/api/role-resource>`__
                to assign to the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_service_user(
                chat_service_sid,
                identity,
                x_twilio_webhook_enabled=x_twilio_webhook_enabled,
                friendly_name=friendly_name,
                attributes=attributes,
                role_sid=role_sid,
                request_options=request_options,
            )
        ).unwrap()

    async def create_user(
        self,
        identity: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        attributes: str | None = None,
        role_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1User:
        """Add a new conversation user to your account's default service

        Args:
            identity: The application-defined string that uniquely identifies the resource's User within the
                `Conversation Service <https://www.twilio.com/docs/conversations/api/service-resource>`__. This value is
                often a username or an email address, and is case-sensitive.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The string that you assigned to describe the resource.
            attributes: The JSON Object string that stores application-specific data. If attributes have not been set,
                ``{}`` is returned.
            role_sid: The SID of a service-level `Role <https://www.twilio.com/docs/conversations/api/role-resource>`__
                to assign to the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_user(
                identity,
                x_twilio_webhook_enabled=x_twilio_webhook_enabled,
                friendly_name=friendly_name,
                attributes=attributes,
                role_sid=role_sid,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_service_user(
        self,
        chat_service_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove a conversation user from your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to delete the User resource from.
            sid: The SID of the User resource to delete. This value can be either the ``sid`` or the ``identity`` of the
                User resource to delete.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_service_user(
                chat_service_sid,
                sid,
                x_twilio_webhook_enabled=x_twilio_webhook_enabled,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_user(
        self,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove a conversation user from your account's default service

        Args:
            sid: The SID of the User resource to delete. This value can be either the ``sid`` or the ``identity`` of the
                User resource to delete.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_user(
                sid, x_twilio_webhook_enabled=x_twilio_webhook_enabled, request_options=request_options
            )
        ).unwrap()

    async def fetch_service_user(
        self, chat_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1ServiceServiceUser:
        """Fetch a conversation user from your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to fetch the User resource from.
            sid: The SID of the User resource to fetch. This value can be either the ``sid`` or the ``identity`` of the
                User resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_service_user(chat_service_sid, sid, request_options=request_options)
        ).unwrap()

    async def fetch_user(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> ConversationsV1User:
        """Fetch a conversation user from your account's default service

        Args:
            sid: The SID of the User resource to fetch. This value can be either the ``sid`` or the ``identity`` of the
                User resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_user(sid, request_options=request_options)).unwrap()

    async def list_service_user(
        self,
        chat_service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListServiceUserResponse:
        """Retrieve a list of all conversation users in your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to read the User resources from.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_service_user(
                chat_service_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    async def list_user(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListUserResponse:
        """Retrieve a list of all conversation users in your account's default service

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_user(
                page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    async def update_service_user(
        self,
        chat_service_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        attributes: str | None = None,
        role_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceUser:
        """Update an existing conversation user in your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the User resource is associated
                with.
            sid: The SID of the User resource to update. This value can be either the ``sid`` or the ``identity`` of the
                User resource to update.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The string that you assigned to describe the resource.
            attributes: The JSON Object string that stores application-specific data. If attributes have not been set,
                ``{}`` is returned.
            role_sid: The SID of a service-level `Role <https://www.twilio.com/docs/conversations/api/role-resource>`__
                to assign to the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_service_user(
                chat_service_sid,
                sid,
                x_twilio_webhook_enabled=x_twilio_webhook_enabled,
                friendly_name=friendly_name,
                attributes=attributes,
                role_sid=role_sid,
                request_options=request_options,
            )
        ).unwrap()

    async def update_user(
        self,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        attributes: str | None = None,
        role_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1User:
        """Update an existing conversation user in your account's default service

        Args:
            sid: The SID of the User resource to update. This value can be either the ``sid`` or the ``identity`` of the
                User resource to update.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The string that you assigned to describe the resource.
            attributes: The JSON Object string that stores application-specific data. If attributes have not been set,
                ``{}`` is returned.
            role_sid: The SID of a service-level `Role <https://www.twilio.com/docs/conversations/api/role-resource>`__
                to assign to the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_user(
                sid,
                x_twilio_webhook_enabled=x_twilio_webhook_enabled,
                friendly_name=friendly_name,
                attributes=attributes,
                role_sid=role_sid,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncConversationsV1UserApiWithRawResponse:
        return self._with_raw_response


class ConversationsV1UserApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_service_user(
        self,
        chat_service_sid: str,
        identity: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        attributes: str | None = None,
        role_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceUser, RawError]:
        """Add a new conversation user to your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the User resource is associated
                with.
            identity: The application-defined string that uniquely identifies the resource's User within the
                `Conversation Service <https://www.twilio.com/docs/conversations/api/service-resource>`__. This value is
                often a username or an email address, and is case-sensitive.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The string that you assigned to describe the resource.
            attributes: The JSON Object string that stores application-specific data. If attributes have not been set,
                ``{}`` is returned.
            role_sid: The SID of a service-level `Role <https://www.twilio.com/docs/conversations/api/role-resource>`__
                to assign to the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Users"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid)],
            headers=[
                param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=form_body(
                [
                    param[str]("Identity", identity),
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("Attributes", attributes),
                    param[str | None]("RoleSid", role_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceUser],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_user(
        self,
        identity: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        attributes: str | None = None,
        role_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1User, RawError]:
        """Add a new conversation user to your account's default service

        Args:
            identity: The application-defined string that uniquely identifies the resource's User within the
                `Conversation Service <https://www.twilio.com/docs/conversations/api/service-resource>`__. This value is
                often a username or an email address, and is case-sensitive.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The string that you assigned to describe the resource.
            attributes: The JSON Object string that stores application-specific data. If attributes have not been set,
                ``{}`` is returned.
            role_sid: The SID of a service-level `Role <https://www.twilio.com/docs/conversations/api/role-resource>`__
                to assign to the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Users"),
            headers=[
                param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=form_body(
                [
                    param[str]("Identity", identity),
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("Attributes", attributes),
                    param[str | None]("RoleSid", role_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1User],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_service_user(
        self,
        chat_service_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Remove a conversation user from your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to delete the User resource from.
            sid: The SID of the User resource to delete. This value can be either the ``sid`` or the ``identity`` of the
                User resource to delete.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Users/{Sid}"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid), param[str]("Sid", sid)],
            headers=[
                param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_user(
        self,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Remove a conversation user from your account's default service

        Args:
            sid: The SID of the User resource to delete. This value can be either the ``sid`` or the ``identity`` of the
                User resource to delete.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7("/v1/Users/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[
                param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_service_user(
        self, chat_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1ServiceServiceUser, RawError]:
        """Fetch a conversation user from your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to fetch the User resource from.
            sid: The SID of the User resource to fetch. This value can be either the ``sid`` or the ``identity`` of the
                User resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Users/{Sid}"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceUser],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_user(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1User, RawError]:
        """Fetch a conversation user from your account's default service

        Args:
            sid: The SID of the User resource to fetch. This value can be either the ``sid`` or the ``identity`` of the
                User resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Users/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1User],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_service_user(
        self,
        chat_service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListServiceUserResponse, RawError]:
        """Retrieve a list of all conversation users in your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to read the User resources from.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Users"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListServiceUserResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_user(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListUserResponse, RawError]:
        """Retrieve a list of all conversation users in your account's default service

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Users"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListUserResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_service_user(
        self,
        chat_service_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        attributes: str | None = None,
        role_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceUser, RawError]:
        """Update an existing conversation user in your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the User resource is associated
                with.
            sid: The SID of the User resource to update. This value can be either the ``sid`` or the ``identity`` of the
                User resource to update.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The string that you assigned to describe the resource.
            attributes: The JSON Object string that stores application-specific data. If attributes have not been set,
                ``{}`` is returned.
            role_sid: The SID of a service-level `Role <https://www.twilio.com/docs/conversations/api/role-resource>`__
                to assign to the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Users/{Sid}"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid), param[str]("Sid", sid)],
            headers=[
                param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("Attributes", attributes),
                    param[str | None]("RoleSid", role_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceUser],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_user(
        self,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        attributes: str | None = None,
        role_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1User, RawError]:
        """Update an existing conversation user in your account's default service

        Args:
            sid: The SID of the User resource to update. This value can be either the ``sid`` or the ``identity`` of the
                User resource to update.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The string that you assigned to describe the resource.
            attributes: The JSON Object string that stores application-specific data. If attributes have not been set,
                ``{}`` is returned.
            role_sid: The SID of a service-level `Role <https://www.twilio.com/docs/conversations/api/role-resource>`__
                to assign to the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Users/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[
                param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("Attributes", attributes),
                    param[str | None]("RoleSid", role_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1User],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncConversationsV1UserApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_service_user(
        self,
        chat_service_sid: str,
        identity: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        attributes: str | None = None,
        role_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceUser, RawError]:
        """Add a new conversation user to your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the User resource is associated
                with.
            identity: The application-defined string that uniquely identifies the resource's User within the
                `Conversation Service <https://www.twilio.com/docs/conversations/api/service-resource>`__. This value is
                often a username or an email address, and is case-sensitive.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The string that you assigned to describe the resource.
            attributes: The JSON Object string that stores application-specific data. If attributes have not been set,
                ``{}`` is returned.
            role_sid: The SID of a service-level `Role <https://www.twilio.com/docs/conversations/api/role-resource>`__
                to assign to the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Users"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid)],
            headers=[
                param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=form_body(
                [
                    param[str]("Identity", identity),
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("Attributes", attributes),
                    param[str | None]("RoleSid", role_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceUser],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_user(
        self,
        identity: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        attributes: str | None = None,
        role_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1User, RawError]:
        """Add a new conversation user to your account's default service

        Args:
            identity: The application-defined string that uniquely identifies the resource's User within the
                `Conversation Service <https://www.twilio.com/docs/conversations/api/service-resource>`__. This value is
                often a username or an email address, and is case-sensitive.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The string that you assigned to describe the resource.
            attributes: The JSON Object string that stores application-specific data. If attributes have not been set,
                ``{}`` is returned.
            role_sid: The SID of a service-level `Role <https://www.twilio.com/docs/conversations/api/role-resource>`__
                to assign to the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Users"),
            headers=[
                param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=form_body(
                [
                    param[str]("Identity", identity),
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("Attributes", attributes),
                    param[str | None]("RoleSid", role_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1User],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_service_user(
        self,
        chat_service_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Remove a conversation user from your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to delete the User resource from.
            sid: The SID of the User resource to delete. This value can be either the ``sid`` or the ``identity`` of the
                User resource to delete.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Users/{Sid}"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid), param[str]("Sid", sid)],
            headers=[
                param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_user(
        self,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Remove a conversation user from your account's default service

        Args:
            sid: The SID of the User resource to delete. This value can be either the ``sid`` or the ``identity`` of the
                User resource to delete.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7("/v1/Users/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[
                param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_service_user(
        self, chat_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1ServiceServiceUser, RawError]:
        """Fetch a conversation user from your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to fetch the User resource from.
            sid: The SID of the User resource to fetch. This value can be either the ``sid`` or the ``identity`` of the
                User resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Users/{Sid}"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceUser],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_user(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1User, RawError]:
        """Fetch a conversation user from your account's default service

        Args:
            sid: The SID of the User resource to fetch. This value can be either the ``sid`` or the ``identity`` of the
                User resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Users/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1User],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_service_user(
        self,
        chat_service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListServiceUserResponse, RawError]:
        """Retrieve a list of all conversation users in your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to read the User resources from.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Users"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListServiceUserResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_user(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListUserResponse, RawError]:
        """Retrieve a list of all conversation users in your account's default service

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Users"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListUserResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_service_user(
        self,
        chat_service_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        attributes: str | None = None,
        role_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceUser, RawError]:
        """Update an existing conversation user in your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the User resource is associated
                with.
            sid: The SID of the User resource to update. This value can be either the ``sid`` or the ``identity`` of the
                User resource to update.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The string that you assigned to describe the resource.
            attributes: The JSON Object string that stores application-specific data. If attributes have not been set,
                ``{}`` is returned.
            role_sid: The SID of a service-level `Role <https://www.twilio.com/docs/conversations/api/role-resource>`__
                to assign to the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Users/{Sid}"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid), param[str]("Sid", sid)],
            headers=[
                param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("Attributes", attributes),
                    param[str | None]("RoleSid", role_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceUser],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_user(
        self,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        attributes: str | None = None,
        role_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1User, RawError]:
        """Update an existing conversation user in your account's default service

        Args:
            sid: The SID of the User resource to update. This value can be either the ``sid`` or the ``identity`` of the
                User resource to update.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The string that you assigned to describe the resource.
            attributes: The JSON Object string that stores application-specific data. If attributes have not been set,
                ``{}`` is returned.
            role_sid: The SID of a service-level `Role <https://www.twilio.com/docs/conversations/api/role-resource>`__
                to assign to the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Users/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[
                param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("Attributes", attributes),
                    param[str | None]("RoleSid", role_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1User],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
