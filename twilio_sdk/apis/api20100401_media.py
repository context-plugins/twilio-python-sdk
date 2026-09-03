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
    json_decoder,
    param,
    raw_error_response,
)
from ..models.list_media_response import ListMediaResponse
from ..server.server import Server


class Api20100401Media:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401MediaWithRawResponse(client, server, auth)

    def list_media(
        self,
        account_sid: str,
        message_sid: str,
        *,
        date_created: RFC3339DateTime | None = None,
        date_created_query: RFC3339DateTime | None = None,
        date_created_query_query: RFC3339DateTime | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListMediaResponse:
        """Read a list of Media resources associated with a specific Message resource

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that is associated
                with the Media resources.
            message_sid: The SID of the Message resource that is associated with the Media resources.
            date_created: Only include Media resources that were created on this date. Specify a date as ``YYYY-MM-DD``
                in GMT, for example: ``2009-07-06``, to read Media that were created on this date. You can also specify
                an inequality, such as ``StartTime<=YYYY-MM-DD``, to read Media that were created on or before midnight
                of this date, and ``StartTime>=YYYY-MM-DD`` to read Media that were created on or after midnight of this
                date.
            date_created_query: Only include Media resources that were created on this date. Specify a date as
                ``YYYY-MM-DD`` in GMT, for example: ``2009-07-06``, to read Media that were created on this date. You
                can also specify an inequality, such as ``StartTime<=YYYY-MM-DD``, to read Media that were created on or
                before midnight of this date, and ``StartTime>=YYYY-MM-DD`` to read Media that were created on or after
                midnight of this date.
            date_created_query_query: Only include Media resources that were created on this date. Specify a date as
                ``YYYY-MM-DD`` in GMT, for example: ``2009-07-06``, to read Media that were created on this date. You
                can also specify an inequality, such as ``StartTime<=YYYY-MM-DD``, to read Media that were created on or
                before midnight of this date, and ``StartTime>=YYYY-MM-DD`` to read Media that were created on or after
                midnight of this date.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_media(
            account_sid,
            message_sid,
            date_created=date_created,
            date_created_query=date_created_query,
            date_created_query_query=date_created_query_query,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401MediaWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401Media:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401MediaWithRawResponse(client, server, auth)

    async def list_media(
        self,
        account_sid: str,
        message_sid: str,
        *,
        date_created: RFC3339DateTime | None = None,
        date_created_query: RFC3339DateTime | None = None,
        date_created_query_query: RFC3339DateTime | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListMediaResponse:
        """Read a list of Media resources associated with a specific Message resource

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that is associated
                with the Media resources.
            message_sid: The SID of the Message resource that is associated with the Media resources.
            date_created: Only include Media resources that were created on this date. Specify a date as ``YYYY-MM-DD``
                in GMT, for example: ``2009-07-06``, to read Media that were created on this date. You can also specify
                an inequality, such as ``StartTime<=YYYY-MM-DD``, to read Media that were created on or before midnight
                of this date, and ``StartTime>=YYYY-MM-DD`` to read Media that were created on or after midnight of this
                date.
            date_created_query: Only include Media resources that were created on this date. Specify a date as
                ``YYYY-MM-DD`` in GMT, for example: ``2009-07-06``, to read Media that were created on this date. You
                can also specify an inequality, such as ``StartTime<=YYYY-MM-DD``, to read Media that were created on or
                before midnight of this date, and ``StartTime>=YYYY-MM-DD`` to read Media that were created on or after
                midnight of this date.
            date_created_query_query: Only include Media resources that were created on this date. Specify a date as
                ``YYYY-MM-DD`` in GMT, for example: ``2009-07-06``, to read Media that were created on this date. You
                can also specify an inequality, such as ``StartTime<=YYYY-MM-DD``, to read Media that were created on or
                before midnight of this date, and ``StartTime>=YYYY-MM-DD`` to read Media that were created on or after
                midnight of this date.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_media(
                account_sid,
                message_sid,
                date_created=date_created,
                date_created_query=date_created_query,
                date_created_query_query=date_created_query_query,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401MediaWithRawResponse:
        return self._with_raw_response


class Api20100401MediaWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def list_media(
        self,
        account_sid: str,
        message_sid: str,
        *,
        date_created: RFC3339DateTime | None = None,
        date_created_query: RFC3339DateTime | None = None,
        date_created_query_query: RFC3339DateTime | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListMediaResponse, RawError]:
        """Read a list of Media resources associated with a specific Message resource

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that is associated
                with the Media resources.
            message_sid: The SID of the Message resource that is associated with the Media resources.
            date_created: Only include Media resources that were created on this date. Specify a date as ``YYYY-MM-DD``
                in GMT, for example: ``2009-07-06``, to read Media that were created on this date. You can also specify
                an inequality, such as ``StartTime<=YYYY-MM-DD``, to read Media that were created on or before midnight
                of this date, and ``StartTime>=YYYY-MM-DD`` to read Media that were created on or after midnight of this
                date.
            date_created_query: Only include Media resources that were created on this date. Specify a date as
                ``YYYY-MM-DD`` in GMT, for example: ``2009-07-06``, to read Media that were created on this date. You
                can also specify an inequality, such as ``StartTime<=YYYY-MM-DD``, to read Media that were created on or
                before midnight of this date, and ``StartTime>=YYYY-MM-DD`` to read Media that were created on or after
                midnight of this date.
            date_created_query_query: Only include Media resources that were created on this date. Specify a date as
                ``YYYY-MM-DD`` in GMT, for example: ``2009-07-06``, to read Media that were created on this date. You
                can also specify an inequality, such as ``StartTime<=YYYY-MM-DD``, to read Media that were created on or
                before midnight of this date, and ``StartTime>=YYYY-MM-DD`` to read Media that were created on or after
                midnight of this date.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Messages/{MessageSid}/Media.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("MessageSid", message_sid)],
            query_params=[
                param[RFC3339DateTime | None]("DateCreated", date_created),
                param[RFC3339DateTime | None]("DateCreated<", date_created_query),
                param[RFC3339DateTime | None]("DateCreated>", date_created_query_query),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListMediaResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401MediaWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def list_media(
        self,
        account_sid: str,
        message_sid: str,
        *,
        date_created: RFC3339DateTime | None = None,
        date_created_query: RFC3339DateTime | None = None,
        date_created_query_query: RFC3339DateTime | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListMediaResponse, RawError]:
        """Read a list of Media resources associated with a specific Message resource

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that is associated
                with the Media resources.
            message_sid: The SID of the Message resource that is associated with the Media resources.
            date_created: Only include Media resources that were created on this date. Specify a date as ``YYYY-MM-DD``
                in GMT, for example: ``2009-07-06``, to read Media that were created on this date. You can also specify
                an inequality, such as ``StartTime<=YYYY-MM-DD``, to read Media that were created on or before midnight
                of this date, and ``StartTime>=YYYY-MM-DD`` to read Media that were created on or after midnight of this
                date.
            date_created_query: Only include Media resources that were created on this date. Specify a date as
                ``YYYY-MM-DD`` in GMT, for example: ``2009-07-06``, to read Media that were created on this date. You
                can also specify an inequality, such as ``StartTime<=YYYY-MM-DD``, to read Media that were created on or
                before midnight of this date, and ``StartTime>=YYYY-MM-DD`` to read Media that were created on or after
                midnight of this date.
            date_created_query_query: Only include Media resources that were created on this date. Specify a date as
                ``YYYY-MM-DD`` in GMT, for example: ``2009-07-06``, to read Media that were created on this date. You
                can also specify an inequality, such as ``StartTime<=YYYY-MM-DD``, to read Media that were created on or
                before midnight of this date, and ``StartTime>=YYYY-MM-DD`` to read Media that were created on or after
                midnight of this date.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Messages/{MessageSid}/Media.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("MessageSid", message_sid)],
            query_params=[
                param[RFC3339DateTime | None]("DateCreated", date_created),
                param[RFC3339DateTime | None]("DateCreated<", date_created_query),
                param[RFC3339DateTime | None]("DateCreated>", date_created_query_query),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListMediaResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
