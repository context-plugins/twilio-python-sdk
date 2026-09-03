from __future__ import annotations

from typing import Any
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
from ..models.enums.challenge_enum_list_orders import ChallengeEnumListOrdersOrStr
from ..models.enums.sync_map_item_enum_query_from_bound_type import SyncMapItemEnumQueryFromBoundTypeOrStr
from ..models.list_sync_map_item_response import ListSyncMapItemResponse
from ..models.sync_v1_service_sync_map_sync_map_item import SyncV1ServiceSyncMapSyncMapItem
from ..server.server import Server


class SyncV1SyncMapItem:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SyncV1SyncMapItemWithRawResponse(client, server, auth)

    def create_sync_map_item(
        self,
        service_sid: str,
        map_sid: str,
        key: str,
        data: Any,
        *,
        ttl: int | None = None,
        item_ttl: int | None = None,
        collection_ttl: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SyncV1ServiceSyncMapSyncMapItem:
        """Keys in a sync map

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ to create the
                Map Item in.
            map_sid: The SID of the Sync Map to add the new Map Item to. Can be the Sync Map resource's ``sid`` or its
                ``unique_name``.
            key: The unique, user-defined key for the Map Item. Can be up to 320 characters long.
            data: A JSON string that represents an arbitrary, schema-less object that the Map Item stores. Can be up to
                16 KiB in length.
            ttl: An alias for ``item_ttl``. If both parameters are provided, this value is ignored.
            item_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__, before the
                Map Item expires (time-to-live) and is deleted.
            collection_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__,
                before the Map Item's parent Sync Map expires (time-to-live) and is deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_sync_map_item(
            service_sid,
            map_sid,
            key,
            data,
            ttl=ttl,
            item_ttl=item_ttl,
            collection_ttl=collection_ttl,
            request_options=request_options,
        ).unwrap()

    def delete_sync_map_item(
        self,
        service_sid: str,
        map_sid: str,
        key: str,
        *,
        if_match: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Keys in a sync map

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map Item resource to delete.
            map_sid: The SID of the Sync Map with the Sync Map Item resource to delete. Can be the Sync Map resource's
                ``sid`` or its ``unique_name``.
            key: The ``key`` value of the Sync Map Item resource to delete.
            if_match: If provided, applies this mutation if (and only if) the “revision” field of this [map item]
                matches the provided value. This matches the semantics of (and is implemented with) the HTTP `If-Match
                header <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_sync_map_item(
            service_sid, map_sid, key, if_match=if_match, request_options=request_options
        ).unwrap()

    def fetch_sync_map_item(
        self, service_sid: str, map_sid: str, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SyncV1ServiceSyncMapSyncMapItem:
        """Keys in a sync map

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map Item resource to fetch.
            map_sid: The SID of the Sync Map with the Sync Map Item resource to fetch. Can be the Sync Map resource's
                ``sid`` or its ``unique_name``.
            key: The ``key`` value of the Sync Map Item resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_sync_map_item(
            service_sid, map_sid, key, request_options=request_options
        ).unwrap()

    def list_sync_map_item(
        self,
        service_sid: str,
        map_sid: str,
        *,
        order: ChallengeEnumListOrdersOrStr | None = None,
        from_: str | None = None,
        bounds: SyncMapItemEnumQueryFromBoundTypeOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSyncMapItemResponse:
        """Keys in a sync map

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Map
                Item resources to read.
            map_sid: The SID of the Sync Map with the Sync Map Item resource to fetch. Can be the Sync Map resource's
                ``sid`` or its ``unique_name``.
            order: How to order the Map Items returned by their ``key`` value. Can be: ``asc`` (ascending) or ``desc``
                (descending) and the default is ascending. Map Items are `ordered lexicographically
                <https://en.wikipedia.org/wiki/Lexicographical_order>`__ by Item key.
            from_: The ``key`` of the first Sync Map Item resource to read. See also ``bounds``.
            bounds: Whether to include the Map Item referenced by the ``from`` parameter. Can be: ``inclusive`` to
                include the Map Item referenced by the ``from`` parameter or ``exclusive`` to start with the next Map
                Item. The default value is ``inclusive``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_sync_map_item(
            service_sid,
            map_sid,
            order=order,
            from_=from_,
            bounds=bounds,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_sync_map_item(
        self,
        service_sid: str,
        map_sid: str,
        key: str,
        *,
        if_match: str | None = None,
        data: Any | None = None,
        ttl: int | None = None,
        item_ttl: int | None = None,
        collection_ttl: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SyncV1ServiceSyncMapSyncMapItem:
        """Keys in a sync map

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map Item resource to update.
            map_sid: The SID of the Sync Map with the Sync Map Item resource to update. Can be the Sync Map resource's
                ``sid`` or its ``unique_name``.
            key: The ``key`` value of the Sync Map Item resource to update.
            if_match: If provided, applies this mutation if (and only if) the “revision” field of this [map item]
                matches the provided value. This matches the semantics of (and is implemented with) the HTTP `If-Match
                header <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match>`__.
            data: A JSON string that represents an arbitrary, schema-less object that the Map Item stores. Can be up to
                16 KiB in length.
            ttl: An alias for ``item_ttl``. If both parameters are provided, this value is ignored.
            item_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__, before the
                Map Item expires (time-to-live) and is deleted.
            collection_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__,
                before the Map Item's parent Sync Map expires (time-to-live) and is deleted. This parameter can only be
                used when the Map Item's ``data`` or ``ttl`` is updated in the same request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_sync_map_item(
            service_sid,
            map_sid,
            key,
            if_match=if_match,
            data=data,
            ttl=ttl,
            item_ttl=item_ttl,
            collection_ttl=collection_ttl,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> SyncV1SyncMapItemWithRawResponse:
        return self._with_raw_response


class AsyncSyncV1SyncMapItem:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSyncV1SyncMapItemWithRawResponse(client, server, auth)

    async def create_sync_map_item(
        self,
        service_sid: str,
        map_sid: str,
        key: str,
        data: Any,
        *,
        ttl: int | None = None,
        item_ttl: int | None = None,
        collection_ttl: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SyncV1ServiceSyncMapSyncMapItem:
        """Keys in a sync map

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ to create the
                Map Item in.
            map_sid: The SID of the Sync Map to add the new Map Item to. Can be the Sync Map resource's ``sid`` or its
                ``unique_name``.
            key: The unique, user-defined key for the Map Item. Can be up to 320 characters long.
            data: A JSON string that represents an arbitrary, schema-less object that the Map Item stores. Can be up to
                16 KiB in length.
            ttl: An alias for ``item_ttl``. If both parameters are provided, this value is ignored.
            item_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__, before the
                Map Item expires (time-to-live) and is deleted.
            collection_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__,
                before the Map Item's parent Sync Map expires (time-to-live) and is deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_sync_map_item(
                service_sid,
                map_sid,
                key,
                data,
                ttl=ttl,
                item_ttl=item_ttl,
                collection_ttl=collection_ttl,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_sync_map_item(
        self,
        service_sid: str,
        map_sid: str,
        key: str,
        *,
        if_match: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Keys in a sync map

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map Item resource to delete.
            map_sid: The SID of the Sync Map with the Sync Map Item resource to delete. Can be the Sync Map resource's
                ``sid`` or its ``unique_name``.
            key: The ``key`` value of the Sync Map Item resource to delete.
            if_match: If provided, applies this mutation if (and only if) the “revision” field of this [map item]
                matches the provided value. This matches the semantics of (and is implemented with) the HTTP `If-Match
                header <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_sync_map_item(
                service_sid, map_sid, key, if_match=if_match, request_options=request_options
            )
        ).unwrap()

    async def fetch_sync_map_item(
        self, service_sid: str, map_sid: str, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SyncV1ServiceSyncMapSyncMapItem:
        """Keys in a sync map

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map Item resource to fetch.
            map_sid: The SID of the Sync Map with the Sync Map Item resource to fetch. Can be the Sync Map resource's
                ``sid`` or its ``unique_name``.
            key: The ``key`` value of the Sync Map Item resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_sync_map_item(
                service_sid, map_sid, key, request_options=request_options
            )
        ).unwrap()

    async def list_sync_map_item(
        self,
        service_sid: str,
        map_sid: str,
        *,
        order: ChallengeEnumListOrdersOrStr | None = None,
        from_: str | None = None,
        bounds: SyncMapItemEnumQueryFromBoundTypeOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSyncMapItemResponse:
        """Keys in a sync map

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Map
                Item resources to read.
            map_sid: The SID of the Sync Map with the Sync Map Item resource to fetch. Can be the Sync Map resource's
                ``sid`` or its ``unique_name``.
            order: How to order the Map Items returned by their ``key`` value. Can be: ``asc`` (ascending) or ``desc``
                (descending) and the default is ascending. Map Items are `ordered lexicographically
                <https://en.wikipedia.org/wiki/Lexicographical_order>`__ by Item key.
            from_: The ``key`` of the first Sync Map Item resource to read. See also ``bounds``.
            bounds: Whether to include the Map Item referenced by the ``from`` parameter. Can be: ``inclusive`` to
                include the Map Item referenced by the ``from`` parameter or ``exclusive`` to start with the next Map
                Item. The default value is ``inclusive``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_sync_map_item(
                service_sid,
                map_sid,
                order=order,
                from_=from_,
                bounds=bounds,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_sync_map_item(
        self,
        service_sid: str,
        map_sid: str,
        key: str,
        *,
        if_match: str | None = None,
        data: Any | None = None,
        ttl: int | None = None,
        item_ttl: int | None = None,
        collection_ttl: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SyncV1ServiceSyncMapSyncMapItem:
        """Keys in a sync map

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map Item resource to update.
            map_sid: The SID of the Sync Map with the Sync Map Item resource to update. Can be the Sync Map resource's
                ``sid`` or its ``unique_name``.
            key: The ``key`` value of the Sync Map Item resource to update.
            if_match: If provided, applies this mutation if (and only if) the “revision” field of this [map item]
                matches the provided value. This matches the semantics of (and is implemented with) the HTTP `If-Match
                header <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match>`__.
            data: A JSON string that represents an arbitrary, schema-less object that the Map Item stores. Can be up to
                16 KiB in length.
            ttl: An alias for ``item_ttl``. If both parameters are provided, this value is ignored.
            item_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__, before the
                Map Item expires (time-to-live) and is deleted.
            collection_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__,
                before the Map Item's parent Sync Map expires (time-to-live) and is deleted. This parameter can only be
                used when the Map Item's ``data`` or ``ttl`` is updated in the same request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_sync_map_item(
                service_sid,
                map_sid,
                key,
                if_match=if_match,
                data=data,
                ttl=ttl,
                item_ttl=item_ttl,
                collection_ttl=collection_ttl,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSyncV1SyncMapItemWithRawResponse:
        return self._with_raw_response


class SyncV1SyncMapItemWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_sync_map_item(
        self,
        service_sid: str,
        map_sid: str,
        key: str,
        data: Any,
        *,
        ttl: int | None = None,
        item_ttl: int | None = None,
        collection_ttl: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SyncV1ServiceSyncMapSyncMapItem, RawError]:
        """Keys in a sync map

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ to create the
                Map Item in.
            map_sid: The SID of the Sync Map to add the new Map Item to. Can be the Sync Map resource's ``sid`` or its
                ``unique_name``.
            key: The unique, user-defined key for the Map Item. Can be up to 320 characters long.
            data: A JSON string that represents an arbitrary, schema-less object that the Map Item stores. Can be up to
                16 KiB in length.
            ttl: An alias for ``item_ttl``. If both parameters are provided, this value is ignored.
            item_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__, before the
                Map Item expires (time-to-live) and is deleted.
            collection_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__,
                before the Map Item's parent Sync Map expires (time-to-live) and is deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Maps/{MapSid}/Items"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("MapSid", map_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("Key", key),
                    param[Any]("Data", data),
                    param[int | None]("Ttl", ttl),
                    param[int | None]("ItemTtl", item_ttl),
                    param[int | None]("CollectionTtl", collection_ttl),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceSyncMapSyncMapItem],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_sync_map_item(
        self,
        service_sid: str,
        map_sid: str,
        key: str,
        *,
        if_match: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Keys in a sync map

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map Item resource to delete.
            map_sid: The SID of the Sync Map with the Sync Map Item resource to delete. Can be the Sync Map resource's
                ``sid`` or its ``unique_name``.
            key: The ``key`` value of the Sync Map Item resource to delete.
            if_match: If provided, applies this mutation if (and only if) the “revision” field of this [map item]
                matches the provided value. This matches the semantics of (and is implemented with) the HTTP `If-Match
                header <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Maps/{MapSid}/Items/{Key}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("MapSid", map_sid), param[str]("Key", key)],
            headers=[param[str | None]("If-Match", if_match), param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_sync_map_item(
        self, service_sid: str, map_sid: str, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SyncV1ServiceSyncMapSyncMapItem, RawError]:
        """Keys in a sync map

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map Item resource to fetch.
            map_sid: The SID of the Sync Map with the Sync Map Item resource to fetch. Can be the Sync Map resource's
                ``sid`` or its ``unique_name``.
            key: The ``key`` value of the Sync Map Item resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Maps/{MapSid}/Items/{Key}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("MapSid", map_sid), param[str]("Key", key)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceSyncMapSyncMapItem],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_sync_map_item(
        self,
        service_sid: str,
        map_sid: str,
        *,
        order: ChallengeEnumListOrdersOrStr | None = None,
        from_: str | None = None,
        bounds: SyncMapItemEnumQueryFromBoundTypeOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSyncMapItemResponse, RawError]:
        """Keys in a sync map

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Map
                Item resources to read.
            map_sid: The SID of the Sync Map with the Sync Map Item resource to fetch. Can be the Sync Map resource's
                ``sid`` or its ``unique_name``.
            order: How to order the Map Items returned by their ``key`` value. Can be: ``asc`` (ascending) or ``desc``
                (descending) and the default is ascending. Map Items are `ordered lexicographically
                <https://en.wikipedia.org/wiki/Lexicographical_order>`__ by Item key.
            from_: The ``key`` of the first Sync Map Item resource to read. See also ``bounds``.
            bounds: Whether to include the Map Item referenced by the ``from`` parameter. Can be: ``inclusive`` to
                include the Map Item referenced by the ``from`` parameter or ``exclusive`` to start with the next Map
                Item. The default value is ``inclusive``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Maps/{MapSid}/Items"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("MapSid", map_sid)],
            query_params=[
                param[ChallengeEnumListOrdersOrStr | None]("Order", order),
                param[str | None]("From", from_),
                param[SyncMapItemEnumQueryFromBoundTypeOrStr | None]("Bounds", bounds),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListSyncMapItemResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_sync_map_item(
        self,
        service_sid: str,
        map_sid: str,
        key: str,
        *,
        if_match: str | None = None,
        data: Any | None = None,
        ttl: int | None = None,
        item_ttl: int | None = None,
        collection_ttl: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SyncV1ServiceSyncMapSyncMapItem, RawError]:
        """Keys in a sync map

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map Item resource to update.
            map_sid: The SID of the Sync Map with the Sync Map Item resource to update. Can be the Sync Map resource's
                ``sid`` or its ``unique_name``.
            key: The ``key`` value of the Sync Map Item resource to update.
            if_match: If provided, applies this mutation if (and only if) the “revision” field of this [map item]
                matches the provided value. This matches the semantics of (and is implemented with) the HTTP `If-Match
                header <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match>`__.
            data: A JSON string that represents an arbitrary, schema-less object that the Map Item stores. Can be up to
                16 KiB in length.
            ttl: An alias for ``item_ttl``. If both parameters are provided, this value is ignored.
            item_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__, before the
                Map Item expires (time-to-live) and is deleted.
            collection_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__,
                before the Map Item's parent Sync Map expires (time-to-live) and is deleted. This parameter can only be
                used when the Map Item's ``data`` or ``ttl`` is updated in the same request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Maps/{MapSid}/Items/{Key}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("MapSid", map_sid), param[str]("Key", key)],
            headers=[param[str | None]("If-Match", if_match), param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[Any | None]("Data", data),
                    param[int | None]("Ttl", ttl),
                    param[int | None]("ItemTtl", item_ttl),
                    param[int | None]("CollectionTtl", collection_ttl),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceSyncMapSyncMapItem],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncSyncV1SyncMapItemWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_sync_map_item(
        self,
        service_sid: str,
        map_sid: str,
        key: str,
        data: Any,
        *,
        ttl: int | None = None,
        item_ttl: int | None = None,
        collection_ttl: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SyncV1ServiceSyncMapSyncMapItem, RawError]:
        """Keys in a sync map

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ to create the
                Map Item in.
            map_sid: The SID of the Sync Map to add the new Map Item to. Can be the Sync Map resource's ``sid`` or its
                ``unique_name``.
            key: The unique, user-defined key for the Map Item. Can be up to 320 characters long.
            data: A JSON string that represents an arbitrary, schema-less object that the Map Item stores. Can be up to
                16 KiB in length.
            ttl: An alias for ``item_ttl``. If both parameters are provided, this value is ignored.
            item_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__, before the
                Map Item expires (time-to-live) and is deleted.
            collection_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__,
                before the Map Item's parent Sync Map expires (time-to-live) and is deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Maps/{MapSid}/Items"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("MapSid", map_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("Key", key),
                    param[Any]("Data", data),
                    param[int | None]("Ttl", ttl),
                    param[int | None]("ItemTtl", item_ttl),
                    param[int | None]("CollectionTtl", collection_ttl),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceSyncMapSyncMapItem],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_sync_map_item(
        self,
        service_sid: str,
        map_sid: str,
        key: str,
        *,
        if_match: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Keys in a sync map

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map Item resource to delete.
            map_sid: The SID of the Sync Map with the Sync Map Item resource to delete. Can be the Sync Map resource's
                ``sid`` or its ``unique_name``.
            key: The ``key`` value of the Sync Map Item resource to delete.
            if_match: If provided, applies this mutation if (and only if) the “revision” field of this [map item]
                matches the provided value. This matches the semantics of (and is implemented with) the HTTP `If-Match
                header <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Maps/{MapSid}/Items/{Key}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("MapSid", map_sid), param[str]("Key", key)],
            headers=[param[str | None]("If-Match", if_match), param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_sync_map_item(
        self, service_sid: str, map_sid: str, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SyncV1ServiceSyncMapSyncMapItem, RawError]:
        """Keys in a sync map

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map Item resource to fetch.
            map_sid: The SID of the Sync Map with the Sync Map Item resource to fetch. Can be the Sync Map resource's
                ``sid`` or its ``unique_name``.
            key: The ``key`` value of the Sync Map Item resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Maps/{MapSid}/Items/{Key}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("MapSid", map_sid), param[str]("Key", key)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceSyncMapSyncMapItem],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_sync_map_item(
        self,
        service_sid: str,
        map_sid: str,
        *,
        order: ChallengeEnumListOrdersOrStr | None = None,
        from_: str | None = None,
        bounds: SyncMapItemEnumQueryFromBoundTypeOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSyncMapItemResponse, RawError]:
        """Keys in a sync map

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Map
                Item resources to read.
            map_sid: The SID of the Sync Map with the Sync Map Item resource to fetch. Can be the Sync Map resource's
                ``sid`` or its ``unique_name``.
            order: How to order the Map Items returned by their ``key`` value. Can be: ``asc`` (ascending) or ``desc``
                (descending) and the default is ascending. Map Items are `ordered lexicographically
                <https://en.wikipedia.org/wiki/Lexicographical_order>`__ by Item key.
            from_: The ``key`` of the first Sync Map Item resource to read. See also ``bounds``.
            bounds: Whether to include the Map Item referenced by the ``from`` parameter. Can be: ``inclusive`` to
                include the Map Item referenced by the ``from`` parameter or ``exclusive`` to start with the next Map
                Item. The default value is ``inclusive``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Maps/{MapSid}/Items"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("MapSid", map_sid)],
            query_params=[
                param[ChallengeEnumListOrdersOrStr | None]("Order", order),
                param[str | None]("From", from_),
                param[SyncMapItemEnumQueryFromBoundTypeOrStr | None]("Bounds", bounds),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListSyncMapItemResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_sync_map_item(
        self,
        service_sid: str,
        map_sid: str,
        key: str,
        *,
        if_match: str | None = None,
        data: Any | None = None,
        ttl: int | None = None,
        item_ttl: int | None = None,
        collection_ttl: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SyncV1ServiceSyncMapSyncMapItem, RawError]:
        """Keys in a sync map

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map Item resource to update.
            map_sid: The SID of the Sync Map with the Sync Map Item resource to update. Can be the Sync Map resource's
                ``sid`` or its ``unique_name``.
            key: The ``key`` value of the Sync Map Item resource to update.
            if_match: If provided, applies this mutation if (and only if) the “revision” field of this [map item]
                matches the provided value. This matches the semantics of (and is implemented with) the HTTP `If-Match
                header <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match>`__.
            data: A JSON string that represents an arbitrary, schema-less object that the Map Item stores. Can be up to
                16 KiB in length.
            ttl: An alias for ``item_ttl``. If both parameters are provided, this value is ignored.
            item_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__, before the
                Map Item expires (time-to-live) and is deleted.
            collection_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__,
                before the Map Item's parent Sync Map expires (time-to-live) and is deleted. This parameter can only be
                used when the Map Item's ``data`` or ``ttl`` is updated in the same request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Maps/{MapSid}/Items/{Key}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("MapSid", map_sid), param[str]("Key", key)],
            headers=[param[str | None]("If-Match", if_match), param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[Any | None]("Data", data),
                    param[int | None]("Ttl", ttl),
                    param[int | None]("ItemTtl", item_ttl),
                    param[int | None]("CollectionTtl", collection_ttl),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceSyncMapSyncMapItem],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
