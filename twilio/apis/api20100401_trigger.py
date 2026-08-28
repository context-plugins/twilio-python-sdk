from __future__ import annotations

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
from ..models.api_v2010_account_usage_usage_trigger import ApiV2010AccountUsageUsageTrigger
from ..models.enums.callback_method1 import CallbackMethod1OrStr
from ..models.enums.usage_trigger_enum_recurring import UsageTriggerEnumRecurringOrStr
from ..models.enums.usage_trigger_enum_trigger_field import UsageTriggerEnumTriggerFieldOrStr
from ..models.list_usage_trigger_response import ListUsageTriggerResponse
from ..server.server import Server


class Api20100401Trigger:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401TriggerWithRawResponse(client, server, auth)

    def create_usage_trigger(
        self,
        account_sid: str,
        callback_url: str,
        trigger_value: str,
        usage_category: str,
        *,
        callback_method: CallbackMethod1OrStr | None = None,
        friendly_name: str | None = None,
        recurring: UsageTriggerEnumRecurringOrStr | None = None,
        trigger_by: UsageTriggerEnumTriggerFieldOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountUsageUsageTrigger:
        """Create a new UsageTrigger

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            callback_url: The URL we should call using ``callback_method`` when the trigger fires.
            trigger_value: The usage value at which the trigger should fire. For convenience, you can use an offset
                value such as ``+30`` to specify a trigger_value that is 30 units more than the current usage value. Be
                sure to urlencode a ``+`` as ``%2B``.
            usage_category: The usage category that the trigger should watch. Use one of the supported `usage categories
                <https://www.twilio.com/docs/usage/api/usage-record#usage-categories>`__ for this value.
            callback_method: The HTTP method we should use to call ``callback_url``. Can be: ``GET`` or ``POST`` and the
                default is ``POST``.
            friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters
                long.
            recurring: The frequency of a recurring UsageTrigger. Can be: ``daily``, ``monthly``, or ``yearly`` for
                recurring triggers or empty for non-recurring triggers. A trigger will only fire once during each
                period. Recurring times are in GMT.
            trigger_by: The field in the `UsageRecord <https://www.twilio.com/docs/usage/api/usage-record>`__ resource
                that fires the trigger. Can be: ``count``, ``usage``, or ``price``, as described in the `UsageRecords
                documentation <https://www.twilio.com/docs/usage/api/usage-record#usage-count-price>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_usage_trigger(
            account_sid,
            callback_url,
            trigger_value,
            usage_category,
            callback_method=callback_method,
            friendly_name=friendly_name,
            recurring=recurring,
            trigger_by=trigger_by,
            request_options=request_options,
        ).unwrap()

    def delete_usage_trigger(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Webhooks that notify you of usage thresholds

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                UsageTrigger resources to delete.
            sid: The Twilio-provided string that uniquely identifies the UsageTrigger resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_usage_trigger(account_sid, sid, request_options=request_options).unwrap()

    def fetch_usage_trigger(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountUsageUsageTrigger:
        """Fetch and instance of a usage-trigger

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                UsageTrigger resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the UsageTrigger resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_usage_trigger(account_sid, sid, request_options=request_options).unwrap()

    def list_usage_trigger(
        self,
        account_sid: str,
        *,
        recurring: UsageTriggerEnumRecurringOrStr | None = None,
        trigger_by: UsageTriggerEnumTriggerFieldOrStr | None = None,
        usage_category: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListUsageTriggerResponse:
        """Retrieve a list of usage-triggers belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                UsageTrigger resources to read.
            recurring: The frequency of recurring UsageTriggers to read. Can be: ``daily``, ``monthly``, or ``yearly``
                to read recurring UsageTriggers. An empty value or a value of ``alltime`` reads non-recurring
                UsageTriggers.
            trigger_by: The trigger field of the UsageTriggers to read. Can be: ``count``, ``usage``, or ``price`` as
                described in the `UsageRecords documentation
                <https://www.twilio.com/docs/usage/api/usage-record#usage-count-price>`__.
            usage_category: The usage category of the UsageTriggers to read. Must be a supported `usage categories
                <https://www.twilio.com/docs/usage/api/usage-record#usage-categories>`__.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_usage_trigger(
            account_sid,
            recurring=recurring,
            trigger_by=trigger_by,
            usage_category=usage_category,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_usage_trigger(
        self,
        account_sid: str,
        sid: str,
        *,
        callback_method: CallbackMethod1OrStr | None = None,
        callback_url: str | None = None,
        friendly_name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountUsageUsageTrigger:
        """Update an instance of a usage trigger

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                UsageTrigger resources to update.
            sid: The Twilio-provided string that uniquely identifies the UsageTrigger resource to update.
            callback_method: The HTTP method we should use to call ``callback_url``. Can be: ``GET`` or ``POST`` and the
                default is ``POST``.
            callback_url: The URL we should call using ``callback_method`` when the trigger fires.
            friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters
                long.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_usage_trigger(
            account_sid,
            sid,
            callback_method=callback_method,
            callback_url=callback_url,
            friendly_name=friendly_name,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401TriggerWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401Trigger:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401TriggerWithRawResponse(client, server, auth)

    async def create_usage_trigger(
        self,
        account_sid: str,
        callback_url: str,
        trigger_value: str,
        usage_category: str,
        *,
        callback_method: CallbackMethod1OrStr | None = None,
        friendly_name: str | None = None,
        recurring: UsageTriggerEnumRecurringOrStr | None = None,
        trigger_by: UsageTriggerEnumTriggerFieldOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountUsageUsageTrigger:
        """Create a new UsageTrigger

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            callback_url: The URL we should call using ``callback_method`` when the trigger fires.
            trigger_value: The usage value at which the trigger should fire. For convenience, you can use an offset
                value such as ``+30`` to specify a trigger_value that is 30 units more than the current usage value. Be
                sure to urlencode a ``+`` as ``%2B``.
            usage_category: The usage category that the trigger should watch. Use one of the supported `usage categories
                <https://www.twilio.com/docs/usage/api/usage-record#usage-categories>`__ for this value.
            callback_method: The HTTP method we should use to call ``callback_url``. Can be: ``GET`` or ``POST`` and the
                default is ``POST``.
            friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters
                long.
            recurring: The frequency of a recurring UsageTrigger. Can be: ``daily``, ``monthly``, or ``yearly`` for
                recurring triggers or empty for non-recurring triggers. A trigger will only fire once during each
                period. Recurring times are in GMT.
            trigger_by: The field in the `UsageRecord <https://www.twilio.com/docs/usage/api/usage-record>`__ resource
                that fires the trigger. Can be: ``count``, ``usage``, or ``price``, as described in the `UsageRecords
                documentation <https://www.twilio.com/docs/usage/api/usage-record#usage-count-price>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_usage_trigger(
                account_sid,
                callback_url,
                trigger_value,
                usage_category,
                callback_method=callback_method,
                friendly_name=friendly_name,
                recurring=recurring,
                trigger_by=trigger_by,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_usage_trigger(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Webhooks that notify you of usage thresholds

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                UsageTrigger resources to delete.
            sid: The Twilio-provided string that uniquely identifies the UsageTrigger resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_usage_trigger(account_sid, sid, request_options=request_options)
        ).unwrap()

    async def fetch_usage_trigger(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountUsageUsageTrigger:
        """Fetch and instance of a usage-trigger

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                UsageTrigger resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the UsageTrigger resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_usage_trigger(account_sid, sid, request_options=request_options)
        ).unwrap()

    async def list_usage_trigger(
        self,
        account_sid: str,
        *,
        recurring: UsageTriggerEnumRecurringOrStr | None = None,
        trigger_by: UsageTriggerEnumTriggerFieldOrStr | None = None,
        usage_category: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListUsageTriggerResponse:
        """Retrieve a list of usage-triggers belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                UsageTrigger resources to read.
            recurring: The frequency of recurring UsageTriggers to read. Can be: ``daily``, ``monthly``, or ``yearly``
                to read recurring UsageTriggers. An empty value or a value of ``alltime`` reads non-recurring
                UsageTriggers.
            trigger_by: The trigger field of the UsageTriggers to read. Can be: ``count``, ``usage``, or ``price`` as
                described in the `UsageRecords documentation
                <https://www.twilio.com/docs/usage/api/usage-record#usage-count-price>`__.
            usage_category: The usage category of the UsageTriggers to read. Must be a supported `usage categories
                <https://www.twilio.com/docs/usage/api/usage-record#usage-categories>`__.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_usage_trigger(
                account_sid,
                recurring=recurring,
                trigger_by=trigger_by,
                usage_category=usage_category,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_usage_trigger(
        self,
        account_sid: str,
        sid: str,
        *,
        callback_method: CallbackMethod1OrStr | None = None,
        callback_url: str | None = None,
        friendly_name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountUsageUsageTrigger:
        """Update an instance of a usage trigger

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                UsageTrigger resources to update.
            sid: The Twilio-provided string that uniquely identifies the UsageTrigger resource to update.
            callback_method: The HTTP method we should use to call ``callback_url``. Can be: ``GET`` or ``POST`` and the
                default is ``POST``.
            callback_url: The URL we should call using ``callback_method`` when the trigger fires.
            friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters
                long.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_usage_trigger(
                account_sid,
                sid,
                callback_method=callback_method,
                callback_url=callback_url,
                friendly_name=friendly_name,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401TriggerWithRawResponse:
        return self._with_raw_response


class Api20100401TriggerWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_usage_trigger(
        self,
        account_sid: str,
        callback_url: str,
        trigger_value: str,
        usage_category: str,
        *,
        callback_method: CallbackMethod1OrStr | None = None,
        friendly_name: str | None = None,
        recurring: UsageTriggerEnumRecurringOrStr | None = None,
        trigger_by: UsageTriggerEnumTriggerFieldOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountUsageUsageTrigger, RawError]:
        """Create a new UsageTrigger

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            callback_url: The URL we should call using ``callback_method`` when the trigger fires.
            trigger_value: The usage value at which the trigger should fire. For convenience, you can use an offset
                value such as ``+30`` to specify a trigger_value that is 30 units more than the current usage value. Be
                sure to urlencode a ``+`` as ``%2B``.
            usage_category: The usage category that the trigger should watch. Use one of the supported `usage categories
                <https://www.twilio.com/docs/usage/api/usage-record#usage-categories>`__ for this value.
            callback_method: The HTTP method we should use to call ``callback_url``. Can be: ``GET`` or ``POST`` and the
                default is ``POST``.
            friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters
                long.
            recurring: The frequency of a recurring UsageTrigger. Can be: ``daily``, ``monthly``, or ``yearly`` for
                recurring triggers or empty for non-recurring triggers. A trigger will only fire once during each
                period. Recurring times are in GMT.
            trigger_by: The field in the `UsageRecord <https://www.twilio.com/docs/usage/api/usage-record>`__ resource
                that fires the trigger. Can be: ``count``, ``usage``, or ``price``, as described in the `UsageRecords
                documentation <https://www.twilio.com/docs/usage/api/usage-record#usage-count-price>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Usage/Triggers.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            body=form_body(
                [
                    param[str]("CallbackUrl", callback_url),
                    param[str]("TriggerValue", trigger_value),
                    param[str]("UsageCategory", usage_category),
                    param[CallbackMethod1OrStr | None]("CallbackMethod", callback_method),
                    param[str | None]("FriendlyName", friendly_name),
                    param[UsageTriggerEnumRecurringOrStr | None]("Recurring", recurring),
                    param[UsageTriggerEnumTriggerFieldOrStr | None]("TriggerBy", trigger_by),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountUsageUsageTrigger],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_usage_trigger(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Webhooks that notify you of usage thresholds

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                UsageTrigger resources to delete.
            sid: The Twilio-provided string that uniquely identifies the UsageTrigger resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Usage/Triggers/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_usage_trigger(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountUsageUsageTrigger, RawError]:
        """Fetch and instance of a usage-trigger

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                UsageTrigger resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the UsageTrigger resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Usage/Triggers/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountUsageUsageTrigger],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_usage_trigger(
        self,
        account_sid: str,
        *,
        recurring: UsageTriggerEnumRecurringOrStr | None = None,
        trigger_by: UsageTriggerEnumTriggerFieldOrStr | None = None,
        usage_category: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListUsageTriggerResponse, RawError]:
        """Retrieve a list of usage-triggers belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                UsageTrigger resources to read.
            recurring: The frequency of recurring UsageTriggers to read. Can be: ``daily``, ``monthly``, or ``yearly``
                to read recurring UsageTriggers. An empty value or a value of ``alltime`` reads non-recurring
                UsageTriggers.
            trigger_by: The trigger field of the UsageTriggers to read. Can be: ``count``, ``usage``, or ``price`` as
                described in the `UsageRecords documentation
                <https://www.twilio.com/docs/usage/api/usage-record#usage-count-price>`__.
            usage_category: The usage category of the UsageTriggers to read. Must be a supported `usage categories
                <https://www.twilio.com/docs/usage/api/usage-record#usage-categories>`__.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Usage/Triggers.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            query_params=[
                param[UsageTriggerEnumRecurringOrStr | None]("Recurring", recurring),
                param[UsageTriggerEnumTriggerFieldOrStr | None]("TriggerBy", trigger_by),
                param[str | None]("UsageCategory", usage_category),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListUsageTriggerResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_usage_trigger(
        self,
        account_sid: str,
        sid: str,
        *,
        callback_method: CallbackMethod1OrStr | None = None,
        callback_url: str | None = None,
        friendly_name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountUsageUsageTrigger, RawError]:
        """Update an instance of a usage trigger

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                UsageTrigger resources to update.
            sid: The Twilio-provided string that uniquely identifies the UsageTrigger resource to update.
            callback_method: The HTTP method we should use to call ``callback_url``. Can be: ``GET`` or ``POST`` and the
                default is ``POST``.
            callback_url: The URL we should call using ``callback_method`` when the trigger fires.
            friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters
                long.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Usage/Triggers/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            body=form_body(
                [
                    param[CallbackMethod1OrStr | None]("CallbackMethod", callback_method),
                    param[str | None]("CallbackUrl", callback_url),
                    param[str | None]("FriendlyName", friendly_name),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountUsageUsageTrigger],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401TriggerWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_usage_trigger(
        self,
        account_sid: str,
        callback_url: str,
        trigger_value: str,
        usage_category: str,
        *,
        callback_method: CallbackMethod1OrStr | None = None,
        friendly_name: str | None = None,
        recurring: UsageTriggerEnumRecurringOrStr | None = None,
        trigger_by: UsageTriggerEnumTriggerFieldOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountUsageUsageTrigger, RawError]:
        """Create a new UsageTrigger

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            callback_url: The URL we should call using ``callback_method`` when the trigger fires.
            trigger_value: The usage value at which the trigger should fire. For convenience, you can use an offset
                value such as ``+30`` to specify a trigger_value that is 30 units more than the current usage value. Be
                sure to urlencode a ``+`` as ``%2B``.
            usage_category: The usage category that the trigger should watch. Use one of the supported `usage categories
                <https://www.twilio.com/docs/usage/api/usage-record#usage-categories>`__ for this value.
            callback_method: The HTTP method we should use to call ``callback_url``. Can be: ``GET`` or ``POST`` and the
                default is ``POST``.
            friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters
                long.
            recurring: The frequency of a recurring UsageTrigger. Can be: ``daily``, ``monthly``, or ``yearly`` for
                recurring triggers or empty for non-recurring triggers. A trigger will only fire once during each
                period. Recurring times are in GMT.
            trigger_by: The field in the `UsageRecord <https://www.twilio.com/docs/usage/api/usage-record>`__ resource
                that fires the trigger. Can be: ``count``, ``usage``, or ``price``, as described in the `UsageRecords
                documentation <https://www.twilio.com/docs/usage/api/usage-record#usage-count-price>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Usage/Triggers.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            body=form_body(
                [
                    param[str]("CallbackUrl", callback_url),
                    param[str]("TriggerValue", trigger_value),
                    param[str]("UsageCategory", usage_category),
                    param[CallbackMethod1OrStr | None]("CallbackMethod", callback_method),
                    param[str | None]("FriendlyName", friendly_name),
                    param[UsageTriggerEnumRecurringOrStr | None]("Recurring", recurring),
                    param[UsageTriggerEnumTriggerFieldOrStr | None]("TriggerBy", trigger_by),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountUsageUsageTrigger],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_usage_trigger(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Webhooks that notify you of usage thresholds

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                UsageTrigger resources to delete.
            sid: The Twilio-provided string that uniquely identifies the UsageTrigger resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Usage/Triggers/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_usage_trigger(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountUsageUsageTrigger, RawError]:
        """Fetch and instance of a usage-trigger

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                UsageTrigger resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the UsageTrigger resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Usage/Triggers/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountUsageUsageTrigger],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_usage_trigger(
        self,
        account_sid: str,
        *,
        recurring: UsageTriggerEnumRecurringOrStr | None = None,
        trigger_by: UsageTriggerEnumTriggerFieldOrStr | None = None,
        usage_category: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListUsageTriggerResponse, RawError]:
        """Retrieve a list of usage-triggers belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                UsageTrigger resources to read.
            recurring: The frequency of recurring UsageTriggers to read. Can be: ``daily``, ``monthly``, or ``yearly``
                to read recurring UsageTriggers. An empty value or a value of ``alltime`` reads non-recurring
                UsageTriggers.
            trigger_by: The trigger field of the UsageTriggers to read. Can be: ``count``, ``usage``, or ``price`` as
                described in the `UsageRecords documentation
                <https://www.twilio.com/docs/usage/api/usage-record#usage-count-price>`__.
            usage_category: The usage category of the UsageTriggers to read. Must be a supported `usage categories
                <https://www.twilio.com/docs/usage/api/usage-record#usage-categories>`__.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Usage/Triggers.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            query_params=[
                param[UsageTriggerEnumRecurringOrStr | None]("Recurring", recurring),
                param[UsageTriggerEnumTriggerFieldOrStr | None]("TriggerBy", trigger_by),
                param[str | None]("UsageCategory", usage_category),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListUsageTriggerResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_usage_trigger(
        self,
        account_sid: str,
        sid: str,
        *,
        callback_method: CallbackMethod1OrStr | None = None,
        callback_url: str | None = None,
        friendly_name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountUsageUsageTrigger, RawError]:
        """Update an instance of a usage trigger

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                UsageTrigger resources to update.
            sid: The Twilio-provided string that uniquely identifies the UsageTrigger resource to update.
            callback_method: The HTTP method we should use to call ``callback_url``. Can be: ``GET`` or ``POST`` and the
                default is ``POST``.
            callback_url: The URL we should call using ``callback_method`` when the trigger fires.
            friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters
                long.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Usage/Triggers/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            body=form_body(
                [
                    param[CallbackMethod1OrStr | None]("CallbackMethod", callback_method),
                    param[str | None]("CallbackUrl", callback_url),
                    param[str | None]("FriendlyName", friendly_name),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountUsageUsageTrigger],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
