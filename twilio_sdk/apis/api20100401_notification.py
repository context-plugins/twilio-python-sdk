from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    Date,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.api_v2010_account_notification_instance import ApiV2010AccountNotificationInstance
from ..models.list_notification_response import ListNotificationResponse
from ..server.server import Server


class Api20100401Notification:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401NotificationWithRawResponse(client, server, auth)

    def fetch_notification(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountNotificationInstance:
        """Fetch a notification belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Notification resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the Notification resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_notification(account_sid, sid, request_options=request_options).unwrap()

    def list_notification(
        self,
        account_sid: str,
        *,
        log: int | None = None,
        message_date: Date | None = None,
        message_date_query: Date | None = None,
        message_date_query_query: Date | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListNotificationResponse:
        """Retrieve a list of notifications belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Notification resources to read.
            log: Only read notifications of the specified log level. Can be: ``0`` to read only ERROR notifications or
                ``1`` to read only WARNING notifications. By default, all notifications are read.
            message_date: Only show notifications for the specified date, formatted as ``YYYY-MM-DD``. You can also
                specify an inequality, such as ``<=YYYY-MM-DD`` for messages logged at or before midnight on a date, or
                ``>=YYYY-MM-DD`` for messages logged at or after midnight on a date.
            message_date_query: Only show notifications for the specified date, formatted as ``YYYY-MM-DD``. You can
                also specify an inequality, such as ``<=YYYY-MM-DD`` for messages logged at or before midnight on a
                date, or ``>=YYYY-MM-DD`` for messages logged at or after midnight on a date.
            message_date_query_query: Only show notifications for the specified date, formatted as ``YYYY-MM-DD``. You
                can also specify an inequality, such as ``<=YYYY-MM-DD`` for messages logged at or before midnight on a
                date, or ``>=YYYY-MM-DD`` for messages logged at or after midnight on a date.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_notification(
            account_sid,
            log=log,
            message_date=message_date,
            message_date_query=message_date_query,
            message_date_query_query=message_date_query_query,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401NotificationWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401Notification:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401NotificationWithRawResponse(client, server, auth)

    async def fetch_notification(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountNotificationInstance:
        """Fetch a notification belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Notification resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the Notification resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_notification(account_sid, sid, request_options=request_options)
        ).unwrap()

    async def list_notification(
        self,
        account_sid: str,
        *,
        log: int | None = None,
        message_date: Date | None = None,
        message_date_query: Date | None = None,
        message_date_query_query: Date | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListNotificationResponse:
        """Retrieve a list of notifications belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Notification resources to read.
            log: Only read notifications of the specified log level. Can be: ``0`` to read only ERROR notifications or
                ``1`` to read only WARNING notifications. By default, all notifications are read.
            message_date: Only show notifications for the specified date, formatted as ``YYYY-MM-DD``. You can also
                specify an inequality, such as ``<=YYYY-MM-DD`` for messages logged at or before midnight on a date, or
                ``>=YYYY-MM-DD`` for messages logged at or after midnight on a date.
            message_date_query: Only show notifications for the specified date, formatted as ``YYYY-MM-DD``. You can
                also specify an inequality, such as ``<=YYYY-MM-DD`` for messages logged at or before midnight on a
                date, or ``>=YYYY-MM-DD`` for messages logged at or after midnight on a date.
            message_date_query_query: Only show notifications for the specified date, formatted as ``YYYY-MM-DD``. You
                can also specify an inequality, such as ``<=YYYY-MM-DD`` for messages logged at or before midnight on a
                date, or ``>=YYYY-MM-DD`` for messages logged at or after midnight on a date.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_notification(
                account_sid,
                log=log,
                message_date=message_date,
                message_date_query=message_date_query,
                message_date_query_query=message_date_query_query,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401NotificationWithRawResponse:
        return self._with_raw_response


class Api20100401NotificationWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_notification(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountNotificationInstance, RawError]:
        """Fetch a notification belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Notification resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the Notification resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Notifications/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountNotificationInstance],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_notification(
        self,
        account_sid: str,
        *,
        log: int | None = None,
        message_date: Date | None = None,
        message_date_query: Date | None = None,
        message_date_query_query: Date | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListNotificationResponse, RawError]:
        """Retrieve a list of notifications belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Notification resources to read.
            log: Only read notifications of the specified log level. Can be: ``0`` to read only ERROR notifications or
                ``1`` to read only WARNING notifications. By default, all notifications are read.
            message_date: Only show notifications for the specified date, formatted as ``YYYY-MM-DD``. You can also
                specify an inequality, such as ``<=YYYY-MM-DD`` for messages logged at or before midnight on a date, or
                ``>=YYYY-MM-DD`` for messages logged at or after midnight on a date.
            message_date_query: Only show notifications for the specified date, formatted as ``YYYY-MM-DD``. You can
                also specify an inequality, such as ``<=YYYY-MM-DD`` for messages logged at or before midnight on a
                date, or ``>=YYYY-MM-DD`` for messages logged at or after midnight on a date.
            message_date_query_query: Only show notifications for the specified date, formatted as ``YYYY-MM-DD``. You
                can also specify an inequality, such as ``<=YYYY-MM-DD`` for messages logged at or before midnight on a
                date, or ``>=YYYY-MM-DD`` for messages logged at or after midnight on a date.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Notifications.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            query_params=[
                param[int | None]("Log", log),
                param[Date | None]("MessageDate", message_date),
                param[Date | None]("MessageDate<", message_date_query),
                param[Date | None]("MessageDate>", message_date_query_query),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListNotificationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401NotificationWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_notification(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountNotificationInstance, RawError]:
        """Fetch a notification belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Notification resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the Notification resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Notifications/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountNotificationInstance],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_notification(
        self,
        account_sid: str,
        *,
        log: int | None = None,
        message_date: Date | None = None,
        message_date_query: Date | None = None,
        message_date_query_query: Date | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListNotificationResponse, RawError]:
        """Retrieve a list of notifications belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Notification resources to read.
            log: Only read notifications of the specified log level. Can be: ``0`` to read only ERROR notifications or
                ``1`` to read only WARNING notifications. By default, all notifications are read.
            message_date: Only show notifications for the specified date, formatted as ``YYYY-MM-DD``. You can also
                specify an inequality, such as ``<=YYYY-MM-DD`` for messages logged at or before midnight on a date, or
                ``>=YYYY-MM-DD`` for messages logged at or after midnight on a date.
            message_date_query: Only show notifications for the specified date, formatted as ``YYYY-MM-DD``. You can
                also specify an inequality, such as ``<=YYYY-MM-DD`` for messages logged at or before midnight on a
                date, or ``>=YYYY-MM-DD`` for messages logged at or after midnight on a date.
            message_date_query_query: Only show notifications for the specified date, formatted as ``YYYY-MM-DD``. You
                can also specify an inequality, such as ``<=YYYY-MM-DD`` for messages logged at or before midnight on a
                date, or ``>=YYYY-MM-DD`` for messages logged at or after midnight on a date.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Notifications.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            query_params=[
                param[int | None]("Log", log),
                param[Date | None]("MessageDate", message_date),
                param[Date | None]("MessageDate<", message_date_query),
                param[Date | None]("MessageDate>", message_date_query_query),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListNotificationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
