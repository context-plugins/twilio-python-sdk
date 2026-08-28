from __future__ import annotations

from pydantic import AnyUrl

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
from ..models.list_service_response4 import ListServiceResponse4
from ..models.sync_v1_service import SyncV1Service
from ..server.server import Server


class SyncV1ServiceApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SyncV1ServiceApiWithRawResponse(client, server, auth)

    def create_service5(
        self,
        *,
        friendly_name: str | None = None,
        webhook_url: AnyUrl | None = None,
        reachability_webhooks_enabled: bool | None = None,
        acl_enabled: bool | None = None,
        reachability_debouncing_enabled: bool | None = None,
        reachability_debouncing_window: int | None = None,
        webhooks_from_rest_enabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SyncV1Service:
        """Containers for sync objects

        Args:
            friendly_name: A string that you assign to describe the resource.
            webhook_url: The URL we should call when Sync objects are manipulated.
            reachability_webhooks_enabled: Whether the service instance should call ``webhook_url`` when client
                endpoints connect to Sync. The default is ``false``.
            acl_enabled: Whether token identities in the Service must be granted access to Sync objects by using the
                `Permissions <https://www.twilio.com/docs/sync/api/sync-permissions>`__ resource.
            reachability_debouncing_enabled: Whether every ``endpoint_disconnected`` event should occur after a
                configurable delay. The default is ``false``, where the ``endpoint_disconnected`` event occurs
                immediately after disconnection. When ``true``, intervening reconnections can prevent the
                ``endpoint_disconnected`` event.
            reachability_debouncing_window: The reachability event delay in milliseconds if
                ``reachability_debouncing_enabled`` = ``true``. Must be between 1,000 and 30,000 and defaults to 5,000.
                This is the number of milliseconds after the last running client disconnects, and a Sync identity is
                declared offline, before the ``webhook_url`` is called if all endpoints remain offline. A reconnection
                from the same identity by any endpoint during this interval prevents the call to ``webhook_url``.
            webhooks_from_rest_enabled: Whether the Service instance should call ``webhook_url`` when the REST API is
                used to update Sync objects. The default is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_service5(
            friendly_name=friendly_name,
            webhook_url=webhook_url,
            reachability_webhooks_enabled=reachability_webhooks_enabled,
            acl_enabled=acl_enabled,
            reachability_debouncing_enabled=reachability_debouncing_enabled,
            reachability_debouncing_window=reachability_debouncing_window,
            webhooks_from_rest_enabled=webhooks_from_rest_enabled,
            request_options=request_options,
        ).unwrap()

    def delete_service5(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Containers for sync objects

        Args:
            sid: The SID of the Service resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_service5(sid, request_options=request_options).unwrap()

    def fetch_service5(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> SyncV1Service:
        """Containers for sync objects

        Args:
            sid: The SID of the Service resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_service5(sid, request_options=request_options).unwrap()

    def list_service5(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListServiceResponse4:
        """Containers for sync objects

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_service5(
            page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    def update_service4(
        self,
        sid: str,
        *,
        webhook_url: AnyUrl | None = None,
        friendly_name: str | None = None,
        reachability_webhooks_enabled: bool | None = None,
        acl_enabled: bool | None = None,
        reachability_debouncing_enabled: bool | None = None,
        reachability_debouncing_window: int | None = None,
        webhooks_from_rest_enabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SyncV1Service:
        """Containers for sync objects

        Args:
            sid: The SID of the Service resource to update.
            webhook_url: The URL we should call when Sync objects are manipulated.
            friendly_name: A string that you assign to describe the resource.
            reachability_webhooks_enabled: Whether the service instance should call ``webhook_url`` when client
                endpoints connect to Sync. The default is ``false``.
            acl_enabled: Whether token identities in the Service must be granted access to Sync objects by using the
                `Permissions <https://www.twilio.com/docs/sync/api/sync-permissions>`__ resource.
            reachability_debouncing_enabled: Whether every ``endpoint_disconnected`` event should occur after a
                configurable delay. The default is ``false``, where the ``endpoint_disconnected`` event occurs
                immediately after disconnection. When ``true``, intervening reconnections can prevent the
                ``endpoint_disconnected`` event.
            reachability_debouncing_window: The reachability event delay in milliseconds if
                ``reachability_debouncing_enabled`` = ``true``. Must be between 1,000 and 30,000 and defaults to 5,000.
                This is the number of milliseconds after the last running client disconnects, and a Sync identity is
                declared offline, before the webhook is called if all endpoints remain offline. A reconnection from the
                same identity by any endpoint during this interval prevents the webhook from being called.
            webhooks_from_rest_enabled: Whether the Service instance should call ``webhook_url`` when the REST API is
                used to update Sync objects. The default is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_service4(
            sid,
            webhook_url=webhook_url,
            friendly_name=friendly_name,
            reachability_webhooks_enabled=reachability_webhooks_enabled,
            acl_enabled=acl_enabled,
            reachability_debouncing_enabled=reachability_debouncing_enabled,
            reachability_debouncing_window=reachability_debouncing_window,
            webhooks_from_rest_enabled=webhooks_from_rest_enabled,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> SyncV1ServiceApiWithRawResponse:
        return self._with_raw_response


class AsyncSyncV1ServiceApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSyncV1ServiceApiWithRawResponse(client, server, auth)

    async def create_service5(
        self,
        *,
        friendly_name: str | None = None,
        webhook_url: AnyUrl | None = None,
        reachability_webhooks_enabled: bool | None = None,
        acl_enabled: bool | None = None,
        reachability_debouncing_enabled: bool | None = None,
        reachability_debouncing_window: int | None = None,
        webhooks_from_rest_enabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SyncV1Service:
        """Containers for sync objects

        Args:
            friendly_name: A string that you assign to describe the resource.
            webhook_url: The URL we should call when Sync objects are manipulated.
            reachability_webhooks_enabled: Whether the service instance should call ``webhook_url`` when client
                endpoints connect to Sync. The default is ``false``.
            acl_enabled: Whether token identities in the Service must be granted access to Sync objects by using the
                `Permissions <https://www.twilio.com/docs/sync/api/sync-permissions>`__ resource.
            reachability_debouncing_enabled: Whether every ``endpoint_disconnected`` event should occur after a
                configurable delay. The default is ``false``, where the ``endpoint_disconnected`` event occurs
                immediately after disconnection. When ``true``, intervening reconnections can prevent the
                ``endpoint_disconnected`` event.
            reachability_debouncing_window: The reachability event delay in milliseconds if
                ``reachability_debouncing_enabled`` = ``true``. Must be between 1,000 and 30,000 and defaults to 5,000.
                This is the number of milliseconds after the last running client disconnects, and a Sync identity is
                declared offline, before the ``webhook_url`` is called if all endpoints remain offline. A reconnection
                from the same identity by any endpoint during this interval prevents the call to ``webhook_url``.
            webhooks_from_rest_enabled: Whether the Service instance should call ``webhook_url`` when the REST API is
                used to update Sync objects. The default is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_service5(
                friendly_name=friendly_name,
                webhook_url=webhook_url,
                reachability_webhooks_enabled=reachability_webhooks_enabled,
                acl_enabled=acl_enabled,
                reachability_debouncing_enabled=reachability_debouncing_enabled,
                reachability_debouncing_window=reachability_debouncing_window,
                webhooks_from_rest_enabled=webhooks_from_rest_enabled,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_service5(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Containers for sync objects

        Args:
            sid: The SID of the Service resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_service5(sid, request_options=request_options)).unwrap()

    async def fetch_service5(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> SyncV1Service:
        """Containers for sync objects

        Args:
            sid: The SID of the Service resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_service5(sid, request_options=request_options)).unwrap()

    async def list_service5(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListServiceResponse4:
        """Containers for sync objects

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_service5(
                page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    async def update_service4(
        self,
        sid: str,
        *,
        webhook_url: AnyUrl | None = None,
        friendly_name: str | None = None,
        reachability_webhooks_enabled: bool | None = None,
        acl_enabled: bool | None = None,
        reachability_debouncing_enabled: bool | None = None,
        reachability_debouncing_window: int | None = None,
        webhooks_from_rest_enabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SyncV1Service:
        """Containers for sync objects

        Args:
            sid: The SID of the Service resource to update.
            webhook_url: The URL we should call when Sync objects are manipulated.
            friendly_name: A string that you assign to describe the resource.
            reachability_webhooks_enabled: Whether the service instance should call ``webhook_url`` when client
                endpoints connect to Sync. The default is ``false``.
            acl_enabled: Whether token identities in the Service must be granted access to Sync objects by using the
                `Permissions <https://www.twilio.com/docs/sync/api/sync-permissions>`__ resource.
            reachability_debouncing_enabled: Whether every ``endpoint_disconnected`` event should occur after a
                configurable delay. The default is ``false``, where the ``endpoint_disconnected`` event occurs
                immediately after disconnection. When ``true``, intervening reconnections can prevent the
                ``endpoint_disconnected`` event.
            reachability_debouncing_window: The reachability event delay in milliseconds if
                ``reachability_debouncing_enabled`` = ``true``. Must be between 1,000 and 30,000 and defaults to 5,000.
                This is the number of milliseconds after the last running client disconnects, and a Sync identity is
                declared offline, before the webhook is called if all endpoints remain offline. A reconnection from the
                same identity by any endpoint during this interval prevents the webhook from being called.
            webhooks_from_rest_enabled: Whether the Service instance should call ``webhook_url`` when the REST API is
                used to update Sync objects. The default is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_service4(
                sid,
                webhook_url=webhook_url,
                friendly_name=friendly_name,
                reachability_webhooks_enabled=reachability_webhooks_enabled,
                acl_enabled=acl_enabled,
                reachability_debouncing_enabled=reachability_debouncing_enabled,
                reachability_debouncing_window=reachability_debouncing_window,
                webhooks_from_rest_enabled=webhooks_from_rest_enabled,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSyncV1ServiceApiWithRawResponse:
        return self._with_raw_response


class SyncV1ServiceApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_service5(
        self,
        *,
        friendly_name: str | None = None,
        webhook_url: AnyUrl | None = None,
        reachability_webhooks_enabled: bool | None = None,
        acl_enabled: bool | None = None,
        reachability_debouncing_enabled: bool | None = None,
        reachability_debouncing_window: int | None = None,
        webhooks_from_rest_enabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SyncV1Service, RawError]:
        """Containers for sync objects

        Args:
            friendly_name: A string that you assign to describe the resource.
            webhook_url: The URL we should call when Sync objects are manipulated.
            reachability_webhooks_enabled: Whether the service instance should call ``webhook_url`` when client
                endpoints connect to Sync. The default is ``false``.
            acl_enabled: Whether token identities in the Service must be granted access to Sync objects by using the
                `Permissions <https://www.twilio.com/docs/sync/api/sync-permissions>`__ resource.
            reachability_debouncing_enabled: Whether every ``endpoint_disconnected`` event should occur after a
                configurable delay. The default is ``false``, where the ``endpoint_disconnected`` event occurs
                immediately after disconnection. When ``true``, intervening reconnections can prevent the
                ``endpoint_disconnected`` event.
            reachability_debouncing_window: The reachability event delay in milliseconds if
                ``reachability_debouncing_enabled`` = ``true``. Must be between 1,000 and 30,000 and defaults to 5,000.
                This is the number of milliseconds after the last running client disconnects, and a Sync identity is
                declared offline, before the ``webhook_url`` is called if all endpoints remain offline. A reconnection
                from the same identity by any endpoint during this interval prevents the call to ``webhook_url``.
            webhooks_from_rest_enabled: Whether the Service instance should call ``webhook_url`` when the REST API is
                used to update Sync objects. The default is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/v1/Services"),
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[AnyUrl | None]("WebhookUrl", webhook_url),
                    param[bool | None]("ReachabilityWebhooksEnabled", reachability_webhooks_enabled),
                    param[bool | None]("AclEnabled", acl_enabled),
                    param[bool | None]("ReachabilityDebouncingEnabled", reachability_debouncing_enabled),
                    param[int | None]("ReachabilityDebouncingWindow", reachability_debouncing_window),
                    param[bool | None]("WebhooksFromRestEnabled", webhooks_from_rest_enabled),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1Service],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_service5(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Containers for sync objects

        Args:
            sid: The SID of the Service resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default12("/v1/Services/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_service5(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SyncV1Service, RawError]:
        """Containers for sync objects

        Args:
            sid: The SID of the Service resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default12("/v1/Services/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1Service],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_service5(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListServiceResponse4, RawError]:
        """Containers for sync objects

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default12("/v1/Services"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListServiceResponse4],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_service4(
        self,
        sid: str,
        *,
        webhook_url: AnyUrl | None = None,
        friendly_name: str | None = None,
        reachability_webhooks_enabled: bool | None = None,
        acl_enabled: bool | None = None,
        reachability_debouncing_enabled: bool | None = None,
        reachability_debouncing_window: int | None = None,
        webhooks_from_rest_enabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SyncV1Service, RawError]:
        """Containers for sync objects

        Args:
            sid: The SID of the Service resource to update.
            webhook_url: The URL we should call when Sync objects are manipulated.
            friendly_name: A string that you assign to describe the resource.
            reachability_webhooks_enabled: Whether the service instance should call ``webhook_url`` when client
                endpoints connect to Sync. The default is ``false``.
            acl_enabled: Whether token identities in the Service must be granted access to Sync objects by using the
                `Permissions <https://www.twilio.com/docs/sync/api/sync-permissions>`__ resource.
            reachability_debouncing_enabled: Whether every ``endpoint_disconnected`` event should occur after a
                configurable delay. The default is ``false``, where the ``endpoint_disconnected`` event occurs
                immediately after disconnection. When ``true``, intervening reconnections can prevent the
                ``endpoint_disconnected`` event.
            reachability_debouncing_window: The reachability event delay in milliseconds if
                ``reachability_debouncing_enabled`` = ``true``. Must be between 1,000 and 30,000 and defaults to 5,000.
                This is the number of milliseconds after the last running client disconnects, and a Sync identity is
                declared offline, before the webhook is called if all endpoints remain offline. A reconnection from the
                same identity by any endpoint during this interval prevents the webhook from being called.
            webhooks_from_rest_enabled: Whether the Service instance should call ``webhook_url`` when the REST API is
                used to update Sync objects. The default is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/v1/Services/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            body=form_body(
                [
                    param[AnyUrl | None]("WebhookUrl", webhook_url),
                    param[str | None]("FriendlyName", friendly_name),
                    param[bool | None]("ReachabilityWebhooksEnabled", reachability_webhooks_enabled),
                    param[bool | None]("AclEnabled", acl_enabled),
                    param[bool | None]("ReachabilityDebouncingEnabled", reachability_debouncing_enabled),
                    param[int | None]("ReachabilityDebouncingWindow", reachability_debouncing_window),
                    param[bool | None]("WebhooksFromRestEnabled", webhooks_from_rest_enabled),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1Service],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncSyncV1ServiceApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_service5(
        self,
        *,
        friendly_name: str | None = None,
        webhook_url: AnyUrl | None = None,
        reachability_webhooks_enabled: bool | None = None,
        acl_enabled: bool | None = None,
        reachability_debouncing_enabled: bool | None = None,
        reachability_debouncing_window: int | None = None,
        webhooks_from_rest_enabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SyncV1Service, RawError]:
        """Containers for sync objects

        Args:
            friendly_name: A string that you assign to describe the resource.
            webhook_url: The URL we should call when Sync objects are manipulated.
            reachability_webhooks_enabled: Whether the service instance should call ``webhook_url`` when client
                endpoints connect to Sync. The default is ``false``.
            acl_enabled: Whether token identities in the Service must be granted access to Sync objects by using the
                `Permissions <https://www.twilio.com/docs/sync/api/sync-permissions>`__ resource.
            reachability_debouncing_enabled: Whether every ``endpoint_disconnected`` event should occur after a
                configurable delay. The default is ``false``, where the ``endpoint_disconnected`` event occurs
                immediately after disconnection. When ``true``, intervening reconnections can prevent the
                ``endpoint_disconnected`` event.
            reachability_debouncing_window: The reachability event delay in milliseconds if
                ``reachability_debouncing_enabled`` = ``true``. Must be between 1,000 and 30,000 and defaults to 5,000.
                This is the number of milliseconds after the last running client disconnects, and a Sync identity is
                declared offline, before the ``webhook_url`` is called if all endpoints remain offline. A reconnection
                from the same identity by any endpoint during this interval prevents the call to ``webhook_url``.
            webhooks_from_rest_enabled: Whether the Service instance should call ``webhook_url`` when the REST API is
                used to update Sync objects. The default is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/v1/Services"),
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[AnyUrl | None]("WebhookUrl", webhook_url),
                    param[bool | None]("ReachabilityWebhooksEnabled", reachability_webhooks_enabled),
                    param[bool | None]("AclEnabled", acl_enabled),
                    param[bool | None]("ReachabilityDebouncingEnabled", reachability_debouncing_enabled),
                    param[int | None]("ReachabilityDebouncingWindow", reachability_debouncing_window),
                    param[bool | None]("WebhooksFromRestEnabled", webhooks_from_rest_enabled),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1Service],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_service5(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Containers for sync objects

        Args:
            sid: The SID of the Service resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default12("/v1/Services/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_service5(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SyncV1Service, RawError]:
        """Containers for sync objects

        Args:
            sid: The SID of the Service resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default12("/v1/Services/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1Service],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_service5(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListServiceResponse4, RawError]:
        """Containers for sync objects

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default12("/v1/Services"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListServiceResponse4],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_service4(
        self,
        sid: str,
        *,
        webhook_url: AnyUrl | None = None,
        friendly_name: str | None = None,
        reachability_webhooks_enabled: bool | None = None,
        acl_enabled: bool | None = None,
        reachability_debouncing_enabled: bool | None = None,
        reachability_debouncing_window: int | None = None,
        webhooks_from_rest_enabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SyncV1Service, RawError]:
        """Containers for sync objects

        Args:
            sid: The SID of the Service resource to update.
            webhook_url: The URL we should call when Sync objects are manipulated.
            friendly_name: A string that you assign to describe the resource.
            reachability_webhooks_enabled: Whether the service instance should call ``webhook_url`` when client
                endpoints connect to Sync. The default is ``false``.
            acl_enabled: Whether token identities in the Service must be granted access to Sync objects by using the
                `Permissions <https://www.twilio.com/docs/sync/api/sync-permissions>`__ resource.
            reachability_debouncing_enabled: Whether every ``endpoint_disconnected`` event should occur after a
                configurable delay. The default is ``false``, where the ``endpoint_disconnected`` event occurs
                immediately after disconnection. When ``true``, intervening reconnections can prevent the
                ``endpoint_disconnected`` event.
            reachability_debouncing_window: The reachability event delay in milliseconds if
                ``reachability_debouncing_enabled`` = ``true``. Must be between 1,000 and 30,000 and defaults to 5,000.
                This is the number of milliseconds after the last running client disconnects, and a Sync identity is
                declared offline, before the webhook is called if all endpoints remain offline. A reconnection from the
                same identity by any endpoint during this interval prevents the webhook from being called.
            webhooks_from_rest_enabled: Whether the Service instance should call ``webhook_url`` when the REST API is
                used to update Sync objects. The default is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/v1/Services/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            body=form_body(
                [
                    param[AnyUrl | None]("WebhookUrl", webhook_url),
                    param[str | None]("FriendlyName", friendly_name),
                    param[bool | None]("ReachabilityWebhooksEnabled", reachability_webhooks_enabled),
                    param[bool | None]("AclEnabled", acl_enabled),
                    param[bool | None]("ReachabilityDebouncingEnabled", reachability_debouncing_enabled),
                    param[int | None]("ReachabilityDebouncingWindow", reachability_debouncing_window),
                    param[bool | None]("WebhooksFromRestEnabled", webhooks_from_rest_enabled),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1Service],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
