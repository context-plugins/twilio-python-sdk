from __future__ import annotations

from typing import Any

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
from ..models.enums.sync_list_item_enum_query_from_bound_type import SyncListItemEnumQueryFromBoundTypeOrStr
from ..models.list_sync_list_item_response import ListSyncListItemResponse
from ..models.sync_v1_service_sync_list_sync_list_item import SyncV1ServiceSyncListSyncListItem
from ..server.server import Server


class SyncV1SyncListItem:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SyncV1SyncListItemWithRawResponse(client, server, auth)

    def create_sync_list_item(
        self,
        service_sid: str,
        list_sid: str,
        data: Any,
        *,
        ttl: int | None = None,
        item_ttl: int | None = None,
        collection_ttl: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SyncV1ServiceSyncListSyncListItem:
        """Items in a sync list

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ to create the
                new List Item in.
            list_sid: The SID of the Sync List to add the new List Item to. Can be the Sync List resource's ``sid`` or
                its ``unique_name``.
            data: A JSON string that represents an arbitrary, schema-less object that the List Item stores. Can be up to
                16 KiB in length.
            ttl: An alias for ``item_ttl``. If both parameters are provided, this value is ignored.
            item_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__, before the
                List Item expires (time-to-live) and is deleted.
            collection_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__,
                before the List Item's parent Sync List expires (time-to-live) and is deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_sync_list_item(
            service_sid,
            list_sid,
            data,
            ttl=ttl,
            item_ttl=item_ttl,
            collection_ttl=collection_ttl,
            request_options=request_options,
        ).unwrap()

    def delete_sync_list_item(
        self,
        service_sid: str,
        list_sid: str,
        index: int,
        *,
        if_match: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Items in a sync list

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                List Item resource to delete.
            list_sid: The SID of the Sync List with the Sync List Item resource to delete. Can be the Sync List
                resource's ``sid`` or its ``unique_name``.
            index: The index of the Sync List Item resource to delete.
            if_match: If provided, applies this mutation if (and only if) the “revision” field of this [map item]
                matches the provided value. This matches the semantics of (and is implemented with) the HTTP `If-Match
                header <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_sync_list_item(
            service_sid, list_sid, index, if_match=if_match, request_options=request_options
        ).unwrap()

    def fetch_sync_list_item(
        self, service_sid: str, list_sid: str, index: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> SyncV1ServiceSyncListSyncListItem:
        """Items in a sync list

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                List Item resource to fetch.
            list_sid: The SID of the Sync List with the Sync List Item resource to fetch. Can be the Sync List
                resource's ``sid`` or its ``unique_name``.
            index: The index of the Sync List Item resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_sync_list_item(
            service_sid, list_sid, index, request_options=request_options
        ).unwrap()

    def list_sync_list_item(
        self,
        service_sid: str,
        list_sid: str,
        *,
        order: ChallengeEnumListOrdersOrStr | None = None,
        from_: str | None = None,
        bounds: SyncListItemEnumQueryFromBoundTypeOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSyncListItemResponse:
        """Items in a sync list

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the List
                Item resources to read.
            list_sid: The SID of the Sync List with the List Items to read. Can be the Sync List resource's ``sid`` or
                its ``unique_name``.
            order: How to order the List Items returned by their ``index`` value. Can be: ``asc`` (ascending) or
                ``desc`` (descending) and the default is ascending.
            from_: The ``index`` of the first Sync List Item resource to read. See also ``bounds``.
            bounds: Whether to include the List Item referenced by the ``from`` parameter. Can be: ``inclusive`` to
                include the List Item referenced by the ``from`` parameter or ``exclusive`` to start with the next List
                Item. The default value is ``inclusive``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_sync_list_item(
            service_sid,
            list_sid,
            order=order,
            from_=from_,
            bounds=bounds,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_sync_list_item(
        self,
        service_sid: str,
        list_sid: str,
        index: int,
        *,
        if_match: str | None = None,
        data: Any | None = None,
        ttl: int | None = None,
        item_ttl: int | None = None,
        collection_ttl: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SyncV1ServiceSyncListSyncListItem:
        """Items in a sync list

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                List Item resource to update.
            list_sid: The SID of the Sync List with the Sync List Item resource to update. Can be the Sync List
                resource's ``sid`` or its ``unique_name``.
            index: The index of the Sync List Item resource to update.
            if_match: If provided, applies this mutation if (and only if) the “revision” field of this [map item]
                matches the provided value. This matches the semantics of (and is implemented with) the HTTP `If-Match
                header <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match>`__.
            data: A JSON string that represents an arbitrary, schema-less object that the List Item stores. Can be up to
                16 KiB in length.
            ttl: An alias for ``item_ttl``. If both parameters are provided, this value is ignored.
            item_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__, before the
                List Item expires (time-to-live) and is deleted.
            collection_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__,
                before the List Item's parent Sync List expires (time-to-live) and is deleted. This parameter can only
                be used when the List Item's ``data`` or ``ttl`` is updated in the same request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_sync_list_item(
            service_sid,
            list_sid,
            index,
            if_match=if_match,
            data=data,
            ttl=ttl,
            item_ttl=item_ttl,
            collection_ttl=collection_ttl,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> SyncV1SyncListItemWithRawResponse:
        return self._with_raw_response


class AsyncSyncV1SyncListItem:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSyncV1SyncListItemWithRawResponse(client, server, auth)

    async def create_sync_list_item(
        self,
        service_sid: str,
        list_sid: str,
        data: Any,
        *,
        ttl: int | None = None,
        item_ttl: int | None = None,
        collection_ttl: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SyncV1ServiceSyncListSyncListItem:
        """Items in a sync list

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ to create the
                new List Item in.
            list_sid: The SID of the Sync List to add the new List Item to. Can be the Sync List resource's ``sid`` or
                its ``unique_name``.
            data: A JSON string that represents an arbitrary, schema-less object that the List Item stores. Can be up to
                16 KiB in length.
            ttl: An alias for ``item_ttl``. If both parameters are provided, this value is ignored.
            item_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__, before the
                List Item expires (time-to-live) and is deleted.
            collection_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__,
                before the List Item's parent Sync List expires (time-to-live) and is deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_sync_list_item(
                service_sid,
                list_sid,
                data,
                ttl=ttl,
                item_ttl=item_ttl,
                collection_ttl=collection_ttl,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_sync_list_item(
        self,
        service_sid: str,
        list_sid: str,
        index: int,
        *,
        if_match: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Items in a sync list

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                List Item resource to delete.
            list_sid: The SID of the Sync List with the Sync List Item resource to delete. Can be the Sync List
                resource's ``sid`` or its ``unique_name``.
            index: The index of the Sync List Item resource to delete.
            if_match: If provided, applies this mutation if (and only if) the “revision” field of this [map item]
                matches the provided value. This matches the semantics of (and is implemented with) the HTTP `If-Match
                header <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_sync_list_item(
                service_sid, list_sid, index, if_match=if_match, request_options=request_options
            )
        ).unwrap()

    async def fetch_sync_list_item(
        self, service_sid: str, list_sid: str, index: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> SyncV1ServiceSyncListSyncListItem:
        """Items in a sync list

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                List Item resource to fetch.
            list_sid: The SID of the Sync List with the Sync List Item resource to fetch. Can be the Sync List
                resource's ``sid`` or its ``unique_name``.
            index: The index of the Sync List Item resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_sync_list_item(
                service_sid, list_sid, index, request_options=request_options
            )
        ).unwrap()

    async def list_sync_list_item(
        self,
        service_sid: str,
        list_sid: str,
        *,
        order: ChallengeEnumListOrdersOrStr | None = None,
        from_: str | None = None,
        bounds: SyncListItemEnumQueryFromBoundTypeOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSyncListItemResponse:
        """Items in a sync list

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the List
                Item resources to read.
            list_sid: The SID of the Sync List with the List Items to read. Can be the Sync List resource's ``sid`` or
                its ``unique_name``.
            order: How to order the List Items returned by their ``index`` value. Can be: ``asc`` (ascending) or
                ``desc`` (descending) and the default is ascending.
            from_: The ``index`` of the first Sync List Item resource to read. See also ``bounds``.
            bounds: Whether to include the List Item referenced by the ``from`` parameter. Can be: ``inclusive`` to
                include the List Item referenced by the ``from`` parameter or ``exclusive`` to start with the next List
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
            await self._with_raw_response.list_sync_list_item(
                service_sid,
                list_sid,
                order=order,
                from_=from_,
                bounds=bounds,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_sync_list_item(
        self,
        service_sid: str,
        list_sid: str,
        index: int,
        *,
        if_match: str | None = None,
        data: Any | None = None,
        ttl: int | None = None,
        item_ttl: int | None = None,
        collection_ttl: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SyncV1ServiceSyncListSyncListItem:
        """Items in a sync list

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                List Item resource to update.
            list_sid: The SID of the Sync List with the Sync List Item resource to update. Can be the Sync List
                resource's ``sid`` or its ``unique_name``.
            index: The index of the Sync List Item resource to update.
            if_match: If provided, applies this mutation if (and only if) the “revision” field of this [map item]
                matches the provided value. This matches the semantics of (and is implemented with) the HTTP `If-Match
                header <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match>`__.
            data: A JSON string that represents an arbitrary, schema-less object that the List Item stores. Can be up to
                16 KiB in length.
            ttl: An alias for ``item_ttl``. If both parameters are provided, this value is ignored.
            item_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__, before the
                List Item expires (time-to-live) and is deleted.
            collection_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__,
                before the List Item's parent Sync List expires (time-to-live) and is deleted. This parameter can only
                be used when the List Item's ``data`` or ``ttl`` is updated in the same request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_sync_list_item(
                service_sid,
                list_sid,
                index,
                if_match=if_match,
                data=data,
                ttl=ttl,
                item_ttl=item_ttl,
                collection_ttl=collection_ttl,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSyncV1SyncListItemWithRawResponse:
        return self._with_raw_response


class SyncV1SyncListItemWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_sync_list_item(
        self,
        service_sid: str,
        list_sid: str,
        data: Any,
        *,
        ttl: int | None = None,
        item_ttl: int | None = None,
        collection_ttl: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SyncV1ServiceSyncListSyncListItem, RawError]:
        """Items in a sync list

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ to create the
                new List Item in.
            list_sid: The SID of the Sync List to add the new List Item to. Can be the Sync List resource's ``sid`` or
                its ``unique_name``.
            data: A JSON string that represents an arbitrary, schema-less object that the List Item stores. Can be up to
                16 KiB in length.
            ttl: An alias for ``item_ttl``. If both parameters are provided, this value is ignored.
            item_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__, before the
                List Item expires (time-to-live) and is deleted.
            collection_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__,
                before the List Item's parent Sync List expires (time-to-live) and is deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Lists/{ListSid}/Items"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("ListSid", list_sid)],
            body=form_body(
                [
                    param[Any]("Data", data),
                    param[int | None]("Ttl", ttl),
                    param[int | None]("ItemTtl", item_ttl),
                    param[int | None]("CollectionTtl", collection_ttl),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceSyncListSyncListItem],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_sync_list_item(
        self,
        service_sid: str,
        list_sid: str,
        index: int,
        *,
        if_match: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Items in a sync list

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                List Item resource to delete.
            list_sid: The SID of the Sync List with the Sync List Item resource to delete. Can be the Sync List
                resource's ``sid`` or its ``unique_name``.
            index: The index of the Sync List Item resource to delete.
            if_match: If provided, applies this mutation if (and only if) the “revision” field of this [map item]
                matches the provided value. This matches the semantics of (and is implemented with) the HTTP `If-Match
                header <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Lists/{ListSid}/Items/{Index}"),
            path_params=[
                param[str]("ServiceSid", service_sid), param[str]("ListSid", list_sid), param[int]("Index", index)
            ],
            headers=[param[str | None]("If-Match", if_match)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_sync_list_item(
        self, service_sid: str, list_sid: str, index: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SyncV1ServiceSyncListSyncListItem, RawError]:
        """Items in a sync list

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                List Item resource to fetch.
            list_sid: The SID of the Sync List with the Sync List Item resource to fetch. Can be the Sync List
                resource's ``sid`` or its ``unique_name``.
            index: The index of the Sync List Item resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Lists/{ListSid}/Items/{Index}"),
            path_params=[
                param[str]("ServiceSid", service_sid), param[str]("ListSid", list_sid), param[int]("Index", index)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceSyncListSyncListItem],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_sync_list_item(
        self,
        service_sid: str,
        list_sid: str,
        *,
        order: ChallengeEnumListOrdersOrStr | None = None,
        from_: str | None = None,
        bounds: SyncListItemEnumQueryFromBoundTypeOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSyncListItemResponse, RawError]:
        """Items in a sync list

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the List
                Item resources to read.
            list_sid: The SID of the Sync List with the List Items to read. Can be the Sync List resource's ``sid`` or
                its ``unique_name``.
            order: How to order the List Items returned by their ``index`` value. Can be: ``asc`` (ascending) or
                ``desc`` (descending) and the default is ascending.
            from_: The ``index`` of the first Sync List Item resource to read. See also ``bounds``.
            bounds: Whether to include the List Item referenced by the ``from`` parameter. Can be: ``inclusive`` to
                include the List Item referenced by the ``from`` parameter or ``exclusive`` to start with the next List
                Item. The default value is ``inclusive``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Lists/{ListSid}/Items"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("ListSid", list_sid)],
            query_params=[
                param[ChallengeEnumListOrdersOrStr | None]("Order", order),
                param[str | None]("From", from_),
                param[SyncListItemEnumQueryFromBoundTypeOrStr | None]("Bounds", bounds),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListSyncListItemResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_sync_list_item(
        self,
        service_sid: str,
        list_sid: str,
        index: int,
        *,
        if_match: str | None = None,
        data: Any | None = None,
        ttl: int | None = None,
        item_ttl: int | None = None,
        collection_ttl: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SyncV1ServiceSyncListSyncListItem, RawError]:
        """Items in a sync list

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                List Item resource to update.
            list_sid: The SID of the Sync List with the Sync List Item resource to update. Can be the Sync List
                resource's ``sid`` or its ``unique_name``.
            index: The index of the Sync List Item resource to update.
            if_match: If provided, applies this mutation if (and only if) the “revision” field of this [map item]
                matches the provided value. This matches the semantics of (and is implemented with) the HTTP `If-Match
                header <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match>`__.
            data: A JSON string that represents an arbitrary, schema-less object that the List Item stores. Can be up to
                16 KiB in length.
            ttl: An alias for ``item_ttl``. If both parameters are provided, this value is ignored.
            item_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__, before the
                List Item expires (time-to-live) and is deleted.
            collection_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__,
                before the List Item's parent Sync List expires (time-to-live) and is deleted. This parameter can only
                be used when the List Item's ``data`` or ``ttl`` is updated in the same request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Lists/{ListSid}/Items/{Index}"),
            path_params=[
                param[str]("ServiceSid", service_sid), param[str]("ListSid", list_sid), param[int]("Index", index)
            ],
            headers=[param[str | None]("If-Match", if_match)],
            body=form_body(
                [
                    param[Any | None]("Data", data),
                    param[int | None]("Ttl", ttl),
                    param[int | None]("ItemTtl", item_ttl),
                    param[int | None]("CollectionTtl", collection_ttl),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceSyncListSyncListItem],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncSyncV1SyncListItemWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_sync_list_item(
        self,
        service_sid: str,
        list_sid: str,
        data: Any,
        *,
        ttl: int | None = None,
        item_ttl: int | None = None,
        collection_ttl: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SyncV1ServiceSyncListSyncListItem, RawError]:
        """Items in a sync list

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ to create the
                new List Item in.
            list_sid: The SID of the Sync List to add the new List Item to. Can be the Sync List resource's ``sid`` or
                its ``unique_name``.
            data: A JSON string that represents an arbitrary, schema-less object that the List Item stores. Can be up to
                16 KiB in length.
            ttl: An alias for ``item_ttl``. If both parameters are provided, this value is ignored.
            item_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__, before the
                List Item expires (time-to-live) and is deleted.
            collection_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__,
                before the List Item's parent Sync List expires (time-to-live) and is deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Lists/{ListSid}/Items"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("ListSid", list_sid)],
            body=form_body(
                [
                    param[Any]("Data", data),
                    param[int | None]("Ttl", ttl),
                    param[int | None]("ItemTtl", item_ttl),
                    param[int | None]("CollectionTtl", collection_ttl),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceSyncListSyncListItem],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_sync_list_item(
        self,
        service_sid: str,
        list_sid: str,
        index: int,
        *,
        if_match: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Items in a sync list

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                List Item resource to delete.
            list_sid: The SID of the Sync List with the Sync List Item resource to delete. Can be the Sync List
                resource's ``sid`` or its ``unique_name``.
            index: The index of the Sync List Item resource to delete.
            if_match: If provided, applies this mutation if (and only if) the “revision” field of this [map item]
                matches the provided value. This matches the semantics of (and is implemented with) the HTTP `If-Match
                header <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Lists/{ListSid}/Items/{Index}"),
            path_params=[
                param[str]("ServiceSid", service_sid), param[str]("ListSid", list_sid), param[int]("Index", index)
            ],
            headers=[param[str | None]("If-Match", if_match)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_sync_list_item(
        self, service_sid: str, list_sid: str, index: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SyncV1ServiceSyncListSyncListItem, RawError]:
        """Items in a sync list

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                List Item resource to fetch.
            list_sid: The SID of the Sync List with the Sync List Item resource to fetch. Can be the Sync List
                resource's ``sid`` or its ``unique_name``.
            index: The index of the Sync List Item resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Lists/{ListSid}/Items/{Index}"),
            path_params=[
                param[str]("ServiceSid", service_sid), param[str]("ListSid", list_sid), param[int]("Index", index)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceSyncListSyncListItem],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_sync_list_item(
        self,
        service_sid: str,
        list_sid: str,
        *,
        order: ChallengeEnumListOrdersOrStr | None = None,
        from_: str | None = None,
        bounds: SyncListItemEnumQueryFromBoundTypeOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSyncListItemResponse, RawError]:
        """Items in a sync list

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the List
                Item resources to read.
            list_sid: The SID of the Sync List with the List Items to read. Can be the Sync List resource's ``sid`` or
                its ``unique_name``.
            order: How to order the List Items returned by their ``index`` value. Can be: ``asc`` (ascending) or
                ``desc`` (descending) and the default is ascending.
            from_: The ``index`` of the first Sync List Item resource to read. See also ``bounds``.
            bounds: Whether to include the List Item referenced by the ``from`` parameter. Can be: ``inclusive`` to
                include the List Item referenced by the ``from`` parameter or ``exclusive`` to start with the next List
                Item. The default value is ``inclusive``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Lists/{ListSid}/Items"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("ListSid", list_sid)],
            query_params=[
                param[ChallengeEnumListOrdersOrStr | None]("Order", order),
                param[str | None]("From", from_),
                param[SyncListItemEnumQueryFromBoundTypeOrStr | None]("Bounds", bounds),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListSyncListItemResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_sync_list_item(
        self,
        service_sid: str,
        list_sid: str,
        index: int,
        *,
        if_match: str | None = None,
        data: Any | None = None,
        ttl: int | None = None,
        item_ttl: int | None = None,
        collection_ttl: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SyncV1ServiceSyncListSyncListItem, RawError]:
        """Items in a sync list

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                List Item resource to update.
            list_sid: The SID of the Sync List with the Sync List Item resource to update. Can be the Sync List
                resource's ``sid`` or its ``unique_name``.
            index: The index of the Sync List Item resource to update.
            if_match: If provided, applies this mutation if (and only if) the “revision” field of this [map item]
                matches the provided value. This matches the semantics of (and is implemented with) the HTTP `If-Match
                header <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match>`__.
            data: A JSON string that represents an arbitrary, schema-less object that the List Item stores. Can be up to
                16 KiB in length.
            ttl: An alias for ``item_ttl``. If both parameters are provided, this value is ignored.
            item_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__, before the
                List Item expires (time-to-live) and is deleted.
            collection_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__,
                before the List Item's parent Sync List expires (time-to-live) and is deleted. This parameter can only
                be used when the List Item's ``data`` or ``ttl`` is updated in the same request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Lists/{ListSid}/Items/{Index}"),
            path_params=[
                param[str]("ServiceSid", service_sid), param[str]("ListSid", list_sid), param[int]("Index", index)
            ],
            headers=[param[str | None]("If-Match", if_match)],
            body=form_body(
                [
                    param[Any | None]("Data", data),
                    param[int | None]("Ttl", ttl),
                    param[int | None]("ItemTtl", item_ttl),
                    param[int | None]("CollectionTtl", collection_ttl),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceSyncListSyncListItem],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
