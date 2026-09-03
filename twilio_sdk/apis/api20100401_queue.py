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
from ..models.api_v2010_account_queue import ApiV2010AccountQueue
from ..models.list_queue_response import ListQueueResponse
from ..server.server import Server


class Api20100401Queue:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401QueueWithRawResponse(client, server, auth)

    def create_queue(
        self,
        account_sid: str,
        friendly_name: str,
        *,
        max_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountQueue:
        """Create a queue

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            friendly_name: A descriptive string that you created to describe this resource. It can be up to 64
                characters long.
            max_size: The maximum number of calls allowed to be in the queue. The default is 1000. The maximum is 5000.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_queue(
            account_sid, friendly_name, max_size=max_size, request_options=request_options
        ).unwrap()

    def delete_queue(self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Remove an empty queue

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Queue
                resource to delete.
            sid: The Twilio-provided string that uniquely identifies the Queue resource to delete
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_queue(account_sid, sid, request_options=request_options).unwrap()

    def fetch_queue(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountQueue:
        """Fetch an instance of a queue identified by the QueueSid

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Queue
                resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the Queue resource to fetch
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_queue(account_sid, sid, request_options=request_options).unwrap()

    def list_queue(
        self,
        account_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListQueueResponse:
        """Retrieve a list of queues belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Queue
                resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_queue(
            account_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    def update_queue(
        self,
        account_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        max_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountQueue:
        """Update the queue with the new parameters

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Queue
                resource to update.
            sid: The Twilio-provided string that uniquely identifies the Queue resource to update
            friendly_name: A descriptive string that you created to describe this resource. It can be up to 64
                characters long.
            max_size: The maximum number of calls allowed to be in the queue. The default is 1000. The maximum is 5000.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_queue(
            account_sid, sid, friendly_name=friendly_name, max_size=max_size, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401QueueWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401Queue:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401QueueWithRawResponse(client, server, auth)

    async def create_queue(
        self,
        account_sid: str,
        friendly_name: str,
        *,
        max_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountQueue:
        """Create a queue

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            friendly_name: A descriptive string that you created to describe this resource. It can be up to 64
                characters long.
            max_size: The maximum number of calls allowed to be in the queue. The default is 1000. The maximum is 5000.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_queue(
                account_sid, friendly_name, max_size=max_size, request_options=request_options
            )
        ).unwrap()

    async def delete_queue(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Remove an empty queue

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Queue
                resource to delete.
            sid: The Twilio-provided string that uniquely identifies the Queue resource to delete
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_queue(account_sid, sid, request_options=request_options)).unwrap()

    async def fetch_queue(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountQueue:
        """Fetch an instance of a queue identified by the QueueSid

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Queue
                resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the Queue resource to fetch
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_queue(account_sid, sid, request_options=request_options)).unwrap()

    async def list_queue(
        self,
        account_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListQueueResponse:
        """Retrieve a list of queues belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Queue
                resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_queue(
                account_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    async def update_queue(
        self,
        account_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        max_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountQueue:
        """Update the queue with the new parameters

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Queue
                resource to update.
            sid: The Twilio-provided string that uniquely identifies the Queue resource to update
            friendly_name: A descriptive string that you created to describe this resource. It can be up to 64
                characters long.
            max_size: The maximum number of calls allowed to be in the queue. The default is 1000. The maximum is 5000.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_queue(
                account_sid, sid, friendly_name=friendly_name, max_size=max_size, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401QueueWithRawResponse:
        return self._with_raw_response


class Api20100401QueueWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_queue(
        self,
        account_sid: str,
        friendly_name: str,
        *,
        max_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountQueue, RawError]:
        """Create a queue

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            friendly_name: A descriptive string that you created to describe this resource. It can be up to 64
                characters long.
            max_size: The maximum number of calls allowed to be in the queue. The default is 1000. The maximum is 5000.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Queues.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str]("FriendlyName", friendly_name), param[int | None]("MaxSize", max_size)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountQueue],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_queue(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Remove an empty queue

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Queue
                resource to delete.
            sid: The Twilio-provided string that uniquely identifies the Queue resource to delete
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Queues/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_queue(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountQueue, RawError]:
        """Fetch an instance of a queue identified by the QueueSid

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Queue
                resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the Queue resource to fetch
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Queues/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountQueue],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_queue(
        self,
        account_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListQueueResponse, RawError]:
        """Retrieve a list of queues belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Queue
                resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Queues.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListQueueResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_queue(
        self,
        account_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        max_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountQueue, RawError]:
        """Update the queue with the new parameters

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Queue
                resource to update.
            sid: The Twilio-provided string that uniquely identifies the Queue resource to update
            friendly_name: A descriptive string that you created to describe this resource. It can be up to 64
                characters long.
            max_size: The maximum number of calls allowed to be in the queue. The default is 1000. The maximum is 5000.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Queues/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str | None]("FriendlyName", friendly_name), param[int | None]("MaxSize", max_size)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountQueue],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401QueueWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_queue(
        self,
        account_sid: str,
        friendly_name: str,
        *,
        max_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountQueue, RawError]:
        """Create a queue

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            friendly_name: A descriptive string that you created to describe this resource. It can be up to 64
                characters long.
            max_size: The maximum number of calls allowed to be in the queue. The default is 1000. The maximum is 5000.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Queues.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str]("FriendlyName", friendly_name), param[int | None]("MaxSize", max_size)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountQueue],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_queue(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Remove an empty queue

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Queue
                resource to delete.
            sid: The Twilio-provided string that uniquely identifies the Queue resource to delete
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Queues/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_queue(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountQueue, RawError]:
        """Fetch an instance of a queue identified by the QueueSid

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Queue
                resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the Queue resource to fetch
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Queues/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountQueue],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_queue(
        self,
        account_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListQueueResponse, RawError]:
        """Retrieve a list of queues belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Queue
                resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Queues.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListQueueResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_queue(
        self,
        account_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        max_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountQueue, RawError]:
        """Update the queue with the new parameters

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Queue
                resource to update.
            sid: The Twilio-provided string that uniquely identifies the Queue resource to update
            friendly_name: A descriptive string that you created to describe this resource. It can be up to 64
                characters long.
            max_size: The maximum number of calls allowed to be in the queue. The default is 1000. The maximum is 5000.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Queues/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str | None]("FriendlyName", friendly_name), param[int | None]("MaxSize", max_size)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountQueue],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
