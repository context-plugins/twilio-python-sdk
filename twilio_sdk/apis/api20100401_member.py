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
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.api_v2010_account_queue_member import ApiV2010AccountQueueMember
from ..models.enums.method2 import Method2OrStr
from ..models.list_member_response import ListMemberResponse
from ..server.server import Server


class Api20100401Member:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401MemberWithRawResponse(client, server, auth)

    def fetch_member(
        self, account_sid: str, queue_sid: str, call_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountQueueMember:
        """Fetch a specific member from the queue

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Member resource(s) to fetch.
            queue_sid: The SID of the Queue in which to find the members to fetch.
            call_sid: The `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ SID of the resource(s) to
                fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_member(
            account_sid, queue_sid, call_sid, request_options=request_options
        ).unwrap()

    def list_member(
        self,
        account_sid: str,
        queue_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListMemberResponse:
        """Retrieve the members of the queue

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Member resource(s) to read.
            queue_sid: The SID of the Queue in which to find the members
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_member(
            account_sid,
            queue_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_member(
        self,
        account_sid: str,
        queue_sid: str,
        call_sid: str,
        url: str,
        *,
        method: Method2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountQueueMember:
        """Dequeue a member from a queue and have the member's call begin executing the TwiML document at that URL

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Member resource(s) to update.
            queue_sid: The SID of the Queue in which to find the members to update.
            call_sid: The `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ SID of the resource(s) to
                update.
            url: The absolute URL of the Queue resource.
            method: How to pass the update request data. Can be ``GET`` or ``POST`` and the default is ``POST``.
                ``POST`` sends the data as encoded form data and ``GET`` sends the data as query parameters.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_member(
            account_sid, queue_sid, call_sid, url, method=method, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401MemberWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401Member:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401MemberWithRawResponse(client, server, auth)

    async def fetch_member(
        self, account_sid: str, queue_sid: str, call_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountQueueMember:
        """Fetch a specific member from the queue

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Member resource(s) to fetch.
            queue_sid: The SID of the Queue in which to find the members to fetch.
            call_sid: The `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ SID of the resource(s) to
                fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_member(
                account_sid, queue_sid, call_sid, request_options=request_options
            )
        ).unwrap()

    async def list_member(
        self,
        account_sid: str,
        queue_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListMemberResponse:
        """Retrieve the members of the queue

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Member resource(s) to read.
            queue_sid: The SID of the Queue in which to find the members
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_member(
                account_sid,
                queue_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_member(
        self,
        account_sid: str,
        queue_sid: str,
        call_sid: str,
        url: str,
        *,
        method: Method2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountQueueMember:
        """Dequeue a member from a queue and have the member's call begin executing the TwiML document at that URL

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Member resource(s) to update.
            queue_sid: The SID of the Queue in which to find the members to update.
            call_sid: The `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ SID of the resource(s) to
                update.
            url: The absolute URL of the Queue resource.
            method: How to pass the update request data. Can be ``GET`` or ``POST`` and the default is ``POST``.
                ``POST`` sends the data as encoded form data and ``GET`` sends the data as query parameters.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_member(
                account_sid, queue_sid, call_sid, url, method=method, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401MemberWithRawResponse:
        return self._with_raw_response


class Api20100401MemberWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_member(
        self, account_sid: str, queue_sid: str, call_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountQueueMember, RawError]:
        """Fetch a specific member from the queue

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Member resource(s) to fetch.
            queue_sid: The SID of the Queue in which to find the members to fetch.
            call_sid: The `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ SID of the resource(s) to
                fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Queues/{QueueSid}/Members/{CallSid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("QueueSid", queue_sid),
                param[str]("CallSid", call_sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountQueueMember],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_member(
        self,
        account_sid: str,
        queue_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListMemberResponse, RawError]:
        """Retrieve the members of the queue

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Member resource(s) to read.
            queue_sid: The SID of the Queue in which to find the members
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Queues/{QueueSid}/Members.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("QueueSid", queue_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListMemberResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_member(
        self,
        account_sid: str,
        queue_sid: str,
        call_sid: str,
        url: str,
        *,
        method: Method2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountQueueMember, RawError]:
        """Dequeue a member from a queue and have the member's call begin executing the TwiML document at that URL

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Member resource(s) to update.
            queue_sid: The SID of the Queue in which to find the members to update.
            call_sid: The `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ SID of the resource(s) to
                update.
            url: The absolute URL of the Queue resource.
            method: How to pass the update request data. Can be ``GET`` or ``POST`` and the default is ``POST``.
                ``POST`` sends the data as encoded form data and ``GET`` sends the data as query parameters.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Queues/{QueueSid}/Members/{CallSid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("QueueSid", queue_sid),
                param[str]("CallSid", call_sid),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str]("Url", url), param[Method2OrStr | None]("Method", method)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountQueueMember],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401MemberWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_member(
        self, account_sid: str, queue_sid: str, call_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountQueueMember, RawError]:
        """Fetch a specific member from the queue

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Member resource(s) to fetch.
            queue_sid: The SID of the Queue in which to find the members to fetch.
            call_sid: The `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ SID of the resource(s) to
                fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Queues/{QueueSid}/Members/{CallSid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("QueueSid", queue_sid),
                param[str]("CallSid", call_sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountQueueMember],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_member(
        self,
        account_sid: str,
        queue_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListMemberResponse, RawError]:
        """Retrieve the members of the queue

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Member resource(s) to read.
            queue_sid: The SID of the Queue in which to find the members
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Queues/{QueueSid}/Members.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("QueueSid", queue_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListMemberResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_member(
        self,
        account_sid: str,
        queue_sid: str,
        call_sid: str,
        url: str,
        *,
        method: Method2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountQueueMember, RawError]:
        """Dequeue a member from a queue and have the member's call begin executing the TwiML document at that URL

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Member resource(s) to update.
            queue_sid: The SID of the Queue in which to find the members to update.
            call_sid: The `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ SID of the resource(s) to
                update.
            url: The absolute URL of the Queue resource.
            method: How to pass the update request data. Can be ``GET`` or ``POST`` and the default is ``POST``.
                ``POST`` sends the data as encoded form data and ``GET`` sends the data as query parameters.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Queues/{QueueSid}/Members/{CallSid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("QueueSid", queue_sid),
                param[str]("CallSid", call_sid),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str]("Url", url), param[Method2OrStr | None]("Method", method)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountQueueMember],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
