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
from ..models.conversations_v1_role import ConversationsV1Role
from ..models.conversations_v1_service_service_role import ConversationsV1ServiceServiceRole
from ..models.enums.role_enum_role_type import RoleEnumRoleTypeOrStr
from ..models.enums.service_role_enum_role_type import ServiceRoleEnumRoleTypeOrStr
from ..models.list_role_response import ListRoleResponse
from ..models.list_service_role_response import ListServiceRoleResponse
from ..server.server import Server


class ConversationsV1RoleApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ConversationsV1RoleApiWithRawResponse(client, server, auth)

    def create_role(
        self,
        friendly_name: str,
        type_: RoleEnumRoleTypeOrStr,
        permission: list[str],
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1Role:
        """Create a new user role in your account's default service

        Args:
            friendly_name: A descriptive string that you create to describe the new resource. It can be up to 64
                characters long.
            type_: The type of role. Can be: ``conversation`` for `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ roles or ``service`` for
                `Conversation Service <https://www.twilio.com/docs/conversations/api/service-resource>`__ roles.
            permission: A permission that you grant to the new role. Only one permission can be granted per parameter.
                To assign more than one permission, repeat this parameter for each permission value. The values for this
                parameter depend on the role's ``type``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_role(
            friendly_name, type_, permission, request_options=request_options
        ).unwrap()

    def create_service_role(
        self,
        chat_service_sid: str,
        friendly_name: str,
        type_: ServiceRoleEnumRoleTypeOrStr,
        permission: list[str],
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceRole:
        """Create a new user role in your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to create the Role resource under.
            friendly_name: A descriptive string that you create to describe the new resource. It can be up to 64
                characters long.
            type_: The type of role. Can be: ``conversation`` for `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ roles or ``service`` for
                `Conversation Service <https://www.twilio.com/docs/conversations/api/service-resource>`__ roles.
            permission: A permission that you grant to the new role. Only one permission can be granted per parameter.
                To assign more than one permission, repeat this parameter for each permission value. The values for this
                parameter depend on the role's ``type``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_service_role(
            chat_service_sid, friendly_name, type_, permission, request_options=request_options
        ).unwrap()

    def delete_role(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Remove a user role from your account's default service

        Args:
            sid: The SID of the Role resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_role(sid, request_options=request_options).unwrap()

    def delete_service_role(
        self, chat_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Remove a user role from your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to delete the Role resource from.
            sid: The SID of the Role resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_service_role(
            chat_service_sid, sid, request_options=request_options
        ).unwrap()

    def fetch_role(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> ConversationsV1Role:
        """Fetch a user role from your account's default service

        Args:
            sid: The SID of the Role resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_role(sid, request_options=request_options).unwrap()

    def fetch_service_role(
        self, chat_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1ServiceServiceRole:
        """Fetch a user role from your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to fetch the Role resource from.
            sid: The SID of the Role resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_service_role(
            chat_service_sid, sid, request_options=request_options
        ).unwrap()

    def list_role(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListRoleResponse:
        """Retrieve a list of all user roles in your account's default service

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_role(
            page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    def list_service_role(
        self,
        chat_service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListServiceRoleResponse:
        """Retrieve a list of all user roles in your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to read the Role resources from.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_service_role(
            chat_service_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    def update_role(
        self, sid: str, permission: list[str], *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1Role:
        """Update an existing user role in your account's default service

        Args:
            sid: The SID of the Role resource to update.
            permission: A permission that you grant to the role. Only one permission can be granted per parameter. To
                assign more than one permission, repeat this parameter for each permission value. Note that the update
                action replaces all previously assigned permissions with those defined in the update action. To remove a
                permission, do not include it in the subsequent update action. The values for this parameter depend on
                the role's ``type``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_role(sid, permission, request_options=request_options).unwrap()

    def update_service_role(
        self,
        chat_service_sid: str,
        sid: str,
        permission: list[str],
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceRole:
        """Update an existing user role in your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to update the Role resource in.
            sid: The SID of the Role resource to update.
            permission: A permission that you grant to the role. Only one permission can be granted per parameter. To
                assign more than one permission, repeat this parameter for each permission value. Note that the update
                action replaces all previously assigned permissions with those defined in the update action. To remove a
                permission, do not include it in the subsequent update action. The values for this parameter depend on
                the role's ``type``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_service_role(
            chat_service_sid, sid, permission, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ConversationsV1RoleApiWithRawResponse:
        return self._with_raw_response


class AsyncConversationsV1RoleApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncConversationsV1RoleApiWithRawResponse(client, server, auth)

    async def create_role(
        self,
        friendly_name: str,
        type_: RoleEnumRoleTypeOrStr,
        permission: list[str],
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1Role:
        """Create a new user role in your account's default service

        Args:
            friendly_name: A descriptive string that you create to describe the new resource. It can be up to 64
                characters long.
            type_: The type of role. Can be: ``conversation`` for `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ roles or ``service`` for
                `Conversation Service <https://www.twilio.com/docs/conversations/api/service-resource>`__ roles.
            permission: A permission that you grant to the new role. Only one permission can be granted per parameter.
                To assign more than one permission, repeat this parameter for each permission value. The values for this
                parameter depend on the role's ``type``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_role(friendly_name, type_, permission, request_options=request_options)
        ).unwrap()

    async def create_service_role(
        self,
        chat_service_sid: str,
        friendly_name: str,
        type_: ServiceRoleEnumRoleTypeOrStr,
        permission: list[str],
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceRole:
        """Create a new user role in your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to create the Role resource under.
            friendly_name: A descriptive string that you create to describe the new resource. It can be up to 64
                characters long.
            type_: The type of role. Can be: ``conversation`` for `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ roles or ``service`` for
                `Conversation Service <https://www.twilio.com/docs/conversations/api/service-resource>`__ roles.
            permission: A permission that you grant to the new role. Only one permission can be granted per parameter.
                To assign more than one permission, repeat this parameter for each permission value. The values for this
                parameter depend on the role's ``type``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_service_role(
                chat_service_sid, friendly_name, type_, permission, request_options=request_options
            )
        ).unwrap()

    async def delete_role(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Remove a user role from your account's default service

        Args:
            sid: The SID of the Role resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_role(sid, request_options=request_options)).unwrap()

    async def delete_service_role(
        self, chat_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Remove a user role from your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to delete the Role resource from.
            sid: The SID of the Role resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_service_role(chat_service_sid, sid, request_options=request_options)
        ).unwrap()

    async def fetch_role(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> ConversationsV1Role:
        """Fetch a user role from your account's default service

        Args:
            sid: The SID of the Role resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_role(sid, request_options=request_options)).unwrap()

    async def fetch_service_role(
        self, chat_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1ServiceServiceRole:
        """Fetch a user role from your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to fetch the Role resource from.
            sid: The SID of the Role resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_service_role(chat_service_sid, sid, request_options=request_options)
        ).unwrap()

    async def list_role(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListRoleResponse:
        """Retrieve a list of all user roles in your account's default service

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
            await self._with_raw_response.list_role(
                page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    async def list_service_role(
        self,
        chat_service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListServiceRoleResponse:
        """Retrieve a list of all user roles in your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to read the Role resources from.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_service_role(
                chat_service_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    async def update_role(
        self, sid: str, permission: list[str], *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1Role:
        """Update an existing user role in your account's default service

        Args:
            sid: The SID of the Role resource to update.
            permission: A permission that you grant to the role. Only one permission can be granted per parameter. To
                assign more than one permission, repeat this parameter for each permission value. Note that the update
                action replaces all previously assigned permissions with those defined in the update action. To remove a
                permission, do not include it in the subsequent update action. The values for this parameter depend on
                the role's ``type``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.update_role(sid, permission, request_options=request_options)).unwrap()

    async def update_service_role(
        self,
        chat_service_sid: str,
        sid: str,
        permission: list[str],
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceRole:
        """Update an existing user role in your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to update the Role resource in.
            sid: The SID of the Role resource to update.
            permission: A permission that you grant to the role. Only one permission can be granted per parameter. To
                assign more than one permission, repeat this parameter for each permission value. Note that the update
                action replaces all previously assigned permissions with those defined in the update action. To remove a
                permission, do not include it in the subsequent update action. The values for this parameter depend on
                the role's ``type``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_service_role(
                chat_service_sid, sid, permission, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncConversationsV1RoleApiWithRawResponse:
        return self._with_raw_response


class ConversationsV1RoleApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_role(
        self,
        friendly_name: str,
        type_: RoleEnumRoleTypeOrStr,
        permission: list[str],
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1Role, RawError]:
        """Create a new user role in your account's default service

        Args:
            friendly_name: A descriptive string that you create to describe the new resource. It can be up to 64
                characters long.
            type_: The type of role. Can be: ``conversation`` for `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ roles or ``service`` for
                `Conversation Service <https://www.twilio.com/docs/conversations/api/service-resource>`__ roles.
            permission: A permission that you grant to the new role. Only one permission can be granted per parameter.
                To assign more than one permission, repeat this parameter for each permission value. The values for this
                parameter depend on the role's ``type``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Roles"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[RoleEnumRoleTypeOrStr]("Type", type_),
                    param[list[str]]("Permission", permission),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1Role],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_service_role(
        self,
        chat_service_sid: str,
        friendly_name: str,
        type_: ServiceRoleEnumRoleTypeOrStr,
        permission: list[str],
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceRole, RawError]:
        """Create a new user role in your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to create the Role resource under.
            friendly_name: A descriptive string that you create to describe the new resource. It can be up to 64
                characters long.
            type_: The type of role. Can be: ``conversation`` for `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ roles or ``service`` for
                `Conversation Service <https://www.twilio.com/docs/conversations/api/service-resource>`__ roles.
            permission: A permission that you grant to the new role. Only one permission can be granted per parameter.
                To assign more than one permission, repeat this parameter for each permission value. The values for this
                parameter depend on the role's ``type``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Roles"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[ServiceRoleEnumRoleTypeOrStr]("Type", type_),
                    param[list[str]]("Permission", permission),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceRole],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_role(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Remove a user role from your account's default service

        Args:
            sid: The SID of the Role resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7("/v1/Roles/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_service_role(
        self, chat_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Remove a user role from your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to delete the Role resource from.
            sid: The SID of the Role resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Roles/{Sid}"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_role(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1Role, RawError]:
        """Fetch a user role from your account's default service

        Args:
            sid: The SID of the Role resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Roles/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1Role],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_service_role(
        self, chat_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1ServiceServiceRole, RawError]:
        """Fetch a user role from your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to fetch the Role resource from.
            sid: The SID of the Role resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Roles/{Sid}"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceRole],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_role(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListRoleResponse, RawError]:
        """Retrieve a list of all user roles in your account's default service

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Roles"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListRoleResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_service_role(
        self,
        chat_service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListServiceRoleResponse, RawError]:
        """Retrieve a list of all user roles in your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to read the Role resources from.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Roles"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListServiceRoleResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_role(
        self, sid: str, permission: list[str], *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1Role, RawError]:
        """Update an existing user role in your account's default service

        Args:
            sid: The SID of the Role resource to update.
            permission: A permission that you grant to the role. Only one permission can be granted per parameter. To
                assign more than one permission, repeat this parameter for each permission value. Note that the update
                action replaces all previously assigned permissions with those defined in the update action. To remove a
                permission, do not include it in the subsequent update action. The values for this parameter depend on
                the role's ``type``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Roles/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[list[str]]("Permission", permission)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1Role],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_service_role(
        self,
        chat_service_sid: str,
        sid: str,
        permission: list[str],
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceRole, RawError]:
        """Update an existing user role in your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to update the Role resource in.
            sid: The SID of the Role resource to update.
            permission: A permission that you grant to the role. Only one permission can be granted per parameter. To
                assign more than one permission, repeat this parameter for each permission value. Note that the update
                action replaces all previously assigned permissions with those defined in the update action. To remove a
                permission, do not include it in the subsequent update action. The values for this parameter depend on
                the role's ``type``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Roles/{Sid}"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[list[str]]("Permission", permission)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceRole],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncConversationsV1RoleApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_role(
        self,
        friendly_name: str,
        type_: RoleEnumRoleTypeOrStr,
        permission: list[str],
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1Role, RawError]:
        """Create a new user role in your account's default service

        Args:
            friendly_name: A descriptive string that you create to describe the new resource. It can be up to 64
                characters long.
            type_: The type of role. Can be: ``conversation`` for `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ roles or ``service`` for
                `Conversation Service <https://www.twilio.com/docs/conversations/api/service-resource>`__ roles.
            permission: A permission that you grant to the new role. Only one permission can be granted per parameter.
                To assign more than one permission, repeat this parameter for each permission value. The values for this
                parameter depend on the role's ``type``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Roles"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[RoleEnumRoleTypeOrStr]("Type", type_),
                    param[list[str]]("Permission", permission),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1Role],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_service_role(
        self,
        chat_service_sid: str,
        friendly_name: str,
        type_: ServiceRoleEnumRoleTypeOrStr,
        permission: list[str],
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceRole, RawError]:
        """Create a new user role in your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to create the Role resource under.
            friendly_name: A descriptive string that you create to describe the new resource. It can be up to 64
                characters long.
            type_: The type of role. Can be: ``conversation`` for `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ roles or ``service`` for
                `Conversation Service <https://www.twilio.com/docs/conversations/api/service-resource>`__ roles.
            permission: A permission that you grant to the new role. Only one permission can be granted per parameter.
                To assign more than one permission, repeat this parameter for each permission value. The values for this
                parameter depend on the role's ``type``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Roles"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[ServiceRoleEnumRoleTypeOrStr]("Type", type_),
                    param[list[str]]("Permission", permission),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceRole],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_role(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Remove a user role from your account's default service

        Args:
            sid: The SID of the Role resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7("/v1/Roles/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_service_role(
        self, chat_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Remove a user role from your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to delete the Role resource from.
            sid: The SID of the Role resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Roles/{Sid}"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_role(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1Role, RawError]:
        """Fetch a user role from your account's default service

        Args:
            sid: The SID of the Role resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Roles/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1Role],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_service_role(
        self, chat_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1ServiceServiceRole, RawError]:
        """Fetch a user role from your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to fetch the Role resource from.
            sid: The SID of the Role resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Roles/{Sid}"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceRole],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_role(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListRoleResponse, RawError]:
        """Retrieve a list of all user roles in your account's default service

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Roles"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListRoleResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_service_role(
        self,
        chat_service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListServiceRoleResponse, RawError]:
        """Retrieve a list of all user roles in your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to read the Role resources from.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Roles"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListServiceRoleResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_role(
        self, sid: str, permission: list[str], *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1Role, RawError]:
        """Update an existing user role in your account's default service

        Args:
            sid: The SID of the Role resource to update.
            permission: A permission that you grant to the role. Only one permission can be granted per parameter. To
                assign more than one permission, repeat this parameter for each permission value. Note that the update
                action replaces all previously assigned permissions with those defined in the update action. To remove a
                permission, do not include it in the subsequent update action. The values for this parameter depend on
                the role's ``type``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Roles/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[list[str]]("Permission", permission)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1Role],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_service_role(
        self,
        chat_service_sid: str,
        sid: str,
        permission: list[str],
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceRole, RawError]:
        """Update an existing user role in your service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to update the Role resource in.
            sid: The SID of the Role resource to update.
            permission: A permission that you grant to the role. Only one permission can be granted per parameter. To
                assign more than one permission, repeat this parameter for each permission value. Note that the update
                action replaces all previously assigned permissions with those defined in the update action. To remove a
                permission, do not include it in the subsequent update action. The values for this parameter depend on
                the role's ``type``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Roles/{Sid}"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[list[str]]("Permission", permission)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceRole],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
