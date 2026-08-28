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
from ..models.list_usage_record_response import ListUsageRecordResponse
from ..server.server import Server


class Api20100401Record:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401RecordWithRawResponse(client, server, auth)

    def list_usage_record(
        self,
        account_sid: str,
        *,
        category: str | None = None,
        start_date: Date | None = None,
        end_date: Date | None = None,
        include_subaccounts: bool | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListUsageRecordResponse:
        """Retrieve a list of usage-records belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                UsageRecord resources to read.
            category: The `usage category <https://www.twilio.com/docs/usage/api/usage-record#usage-categories>`__ of
                the UsageRecord resources to read. Only UsageRecord resources in the specified category are retrieved.
            start_date: Only include usage that has occurred on or after this date. Specify the date in GMT and format
                as ``YYYY-MM-DD``. You can also specify offsets from the current date, such as: ``-30days``, which will
                set the start date to be 30 days before the current date.
            end_date: Only include usage that occurred on or before this date. Specify the date in GMT and format as
                ``YYYY-MM-DD``. You can also specify offsets from the current date, such as: ``+30days``, which will set
                the end date to 30 days from the current date.
            include_subaccounts: Whether to include usage from the master account and all its subaccounts. Can be:
                ``true`` (the default) to include usage from the master account and all subaccounts or ``false`` to
                retrieve usage from only the specified account.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_usage_record(
            account_sid,
            category=category,
            start_date=start_date,
            end_date=end_date,
            include_subaccounts=include_subaccounts,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401RecordWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401Record:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401RecordWithRawResponse(client, server, auth)

    async def list_usage_record(
        self,
        account_sid: str,
        *,
        category: str | None = None,
        start_date: Date | None = None,
        end_date: Date | None = None,
        include_subaccounts: bool | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListUsageRecordResponse:
        """Retrieve a list of usage-records belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                UsageRecord resources to read.
            category: The `usage category <https://www.twilio.com/docs/usage/api/usage-record#usage-categories>`__ of
                the UsageRecord resources to read. Only UsageRecord resources in the specified category are retrieved.
            start_date: Only include usage that has occurred on or after this date. Specify the date in GMT and format
                as ``YYYY-MM-DD``. You can also specify offsets from the current date, such as: ``-30days``, which will
                set the start date to be 30 days before the current date.
            end_date: Only include usage that occurred on or before this date. Specify the date in GMT and format as
                ``YYYY-MM-DD``. You can also specify offsets from the current date, such as: ``+30days``, which will set
                the end date to 30 days from the current date.
            include_subaccounts: Whether to include usage from the master account and all its subaccounts. Can be:
                ``true`` (the default) to include usage from the master account and all subaccounts or ``false`` to
                retrieve usage from only the specified account.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_usage_record(
                account_sid,
                category=category,
                start_date=start_date,
                end_date=end_date,
                include_subaccounts=include_subaccounts,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401RecordWithRawResponse:
        return self._with_raw_response


class Api20100401RecordWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def list_usage_record(
        self,
        account_sid: str,
        *,
        category: str | None = None,
        start_date: Date | None = None,
        end_date: Date | None = None,
        include_subaccounts: bool | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListUsageRecordResponse, RawError]:
        """Retrieve a list of usage-records belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                UsageRecord resources to read.
            category: The `usage category <https://www.twilio.com/docs/usage/api/usage-record#usage-categories>`__ of
                the UsageRecord resources to read. Only UsageRecord resources in the specified category are retrieved.
            start_date: Only include usage that has occurred on or after this date. Specify the date in GMT and format
                as ``YYYY-MM-DD``. You can also specify offsets from the current date, such as: ``-30days``, which will
                set the start date to be 30 days before the current date.
            end_date: Only include usage that occurred on or before this date. Specify the date in GMT and format as
                ``YYYY-MM-DD``. You can also specify offsets from the current date, such as: ``+30days``, which will set
                the end date to 30 days from the current date.
            include_subaccounts: Whether to include usage from the master account and all its subaccounts. Can be:
                ``true`` (the default) to include usage from the master account and all subaccounts or ``false`` to
                retrieve usage from only the specified account.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Usage/Records.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            query_params=[
                param[str | None]("Category", category),
                param[Date | None]("StartDate", start_date),
                param[Date | None]("EndDate", end_date),
                param[bool | None]("IncludeSubaccounts", include_subaccounts),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListUsageRecordResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401RecordWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def list_usage_record(
        self,
        account_sid: str,
        *,
        category: str | None = None,
        start_date: Date | None = None,
        end_date: Date | None = None,
        include_subaccounts: bool | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListUsageRecordResponse, RawError]:
        """Retrieve a list of usage-records belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                UsageRecord resources to read.
            category: The `usage category <https://www.twilio.com/docs/usage/api/usage-record#usage-categories>`__ of
                the UsageRecord resources to read. Only UsageRecord resources in the specified category are retrieved.
            start_date: Only include usage that has occurred on or after this date. Specify the date in GMT and format
                as ``YYYY-MM-DD``. You can also specify offsets from the current date, such as: ``-30days``, which will
                set the start date to be 30 days before the current date.
            end_date: Only include usage that occurred on or before this date. Specify the date in GMT and format as
                ``YYYY-MM-DD``. You can also specify offsets from the current date, such as: ``+30days``, which will set
                the end date to 30 days from the current date.
            include_subaccounts: Whether to include usage from the master account and all its subaccounts. Can be:
                ``true`` (the default) to include usage from the master account and all subaccounts or ``false`` to
                retrieve usage from only the specified account.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Usage/Records.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            query_params=[
                param[str | None]("Category", category),
                param[Date | None]("StartDate", start_date),
                param[Date | None]("EndDate", end_date),
                param[bool | None]("IncludeSubaccounts", include_subaccounts),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListUsageRecordResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
