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
    empty_response,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.api_v2010_account_recording import ApiV2010AccountRecording
from ..models.list_recording_response import ListRecordingResponse
from ..server.server import Server


class Api20100401Recording:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401RecordingWithRawResponse(client, server, auth)

    def delete_recording(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a recording from your account

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording resources to delete.
            sid: The Twilio-provided string that uniquely identifies the Recording resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_recording(account_sid, sid, request_options=request_options).unwrap()

    def fetch_recording(
        self,
        account_sid: str,
        sid: str,
        *,
        include_soft_deleted: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountRecording:
        """Fetch an instance of a recording

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the Recording resource to fetch.
            include_soft_deleted: A boolean parameter indicating whether to retrieve soft deleted recordings or not.
                Recordings metadata are kept after deletion for a retention period of 40 days.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_recording(
            account_sid, sid, include_soft_deleted=include_soft_deleted, request_options=request_options
        ).unwrap()

    def list_recording(
        self,
        account_sid: str,
        *,
        date_created: RFC3339DateTime | None = None,
        date_created_query: RFC3339DateTime | None = None,
        date_created_query_query: RFC3339DateTime | None = None,
        call_sid: str | None = None,
        conference_sid: str | None = None,
        include_soft_deleted: bool | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListRecordingResponse:
        """Retrieve a list of recordings belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording resources to read.
            date_created: Only include recordings that were created on this date. Specify a date as ``YYYY-MM-DD`` in
                GMT, for example: ``2009-07-06``, to read recordings that were created on this date. You can also
                specify an inequality, such as ``DateCreated<=YYYY-MM-DD``, to read recordings that were created on or
                before midnight of this date, and ``DateCreated>=YYYY-MM-DD`` to read recordings that were created on or
                after midnight of this date.
            date_created_query: Only include recordings that were created on this date. Specify a date as ``YYYY-MM-DD``
                in GMT, for example: ``2009-07-06``, to read recordings that were created on this date. You can also
                specify an inequality, such as ``DateCreated<=YYYY-MM-DD``, to read recordings that were created on or
                before midnight of this date, and ``DateCreated>=YYYY-MM-DD`` to read recordings that were created on or
                after midnight of this date.
            date_created_query_query: Only include recordings that were created on this date. Specify a date as
                ``YYYY-MM-DD`` in GMT, for example: ``2009-07-06``, to read recordings that were created on this date.
                You can also specify an inequality, such as ``DateCreated<=YYYY-MM-DD``, to read recordings that were
                created on or before midnight of this date, and ``DateCreated>=YYYY-MM-DD`` to read recordings that were
                created on or after midnight of this date.
            call_sid: The `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ SID of the resources to read.
            conference_sid: The Conference SID that identifies the conference associated with the recording to read.
            include_soft_deleted: A boolean parameter indicating whether to retrieve soft deleted recordings or not.
                Recordings metadata are kept after deletion for a retention period of 40 days.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_recording(
            account_sid,
            date_created=date_created,
            date_created_query=date_created_query,
            date_created_query_query=date_created_query_query,
            call_sid=call_sid,
            conference_sid=conference_sid,
            include_soft_deleted=include_soft_deleted,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401RecordingWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401Recording:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401RecordingWithRawResponse(client, server, auth)

    async def delete_recording(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a recording from your account

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording resources to delete.
            sid: The Twilio-provided string that uniquely identifies the Recording resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_recording(account_sid, sid, request_options=request_options)
        ).unwrap()

    async def fetch_recording(
        self,
        account_sid: str,
        sid: str,
        *,
        include_soft_deleted: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountRecording:
        """Fetch an instance of a recording

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the Recording resource to fetch.
            include_soft_deleted: A boolean parameter indicating whether to retrieve soft deleted recordings or not.
                Recordings metadata are kept after deletion for a retention period of 40 days.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_recording(
                account_sid, sid, include_soft_deleted=include_soft_deleted, request_options=request_options
            )
        ).unwrap()

    async def list_recording(
        self,
        account_sid: str,
        *,
        date_created: RFC3339DateTime | None = None,
        date_created_query: RFC3339DateTime | None = None,
        date_created_query_query: RFC3339DateTime | None = None,
        call_sid: str | None = None,
        conference_sid: str | None = None,
        include_soft_deleted: bool | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListRecordingResponse:
        """Retrieve a list of recordings belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording resources to read.
            date_created: Only include recordings that were created on this date. Specify a date as ``YYYY-MM-DD`` in
                GMT, for example: ``2009-07-06``, to read recordings that were created on this date. You can also
                specify an inequality, such as ``DateCreated<=YYYY-MM-DD``, to read recordings that were created on or
                before midnight of this date, and ``DateCreated>=YYYY-MM-DD`` to read recordings that were created on or
                after midnight of this date.
            date_created_query: Only include recordings that were created on this date. Specify a date as ``YYYY-MM-DD``
                in GMT, for example: ``2009-07-06``, to read recordings that were created on this date. You can also
                specify an inequality, such as ``DateCreated<=YYYY-MM-DD``, to read recordings that were created on or
                before midnight of this date, and ``DateCreated>=YYYY-MM-DD`` to read recordings that were created on or
                after midnight of this date.
            date_created_query_query: Only include recordings that were created on this date. Specify a date as
                ``YYYY-MM-DD`` in GMT, for example: ``2009-07-06``, to read recordings that were created on this date.
                You can also specify an inequality, such as ``DateCreated<=YYYY-MM-DD``, to read recordings that were
                created on or before midnight of this date, and ``DateCreated>=YYYY-MM-DD`` to read recordings that were
                created on or after midnight of this date.
            call_sid: The `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ SID of the resources to read.
            conference_sid: The Conference SID that identifies the conference associated with the recording to read.
            include_soft_deleted: A boolean parameter indicating whether to retrieve soft deleted recordings or not.
                Recordings metadata are kept after deletion for a retention period of 40 days.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_recording(
                account_sid,
                date_created=date_created,
                date_created_query=date_created_query,
                date_created_query_query=date_created_query_query,
                call_sid=call_sid,
                conference_sid=conference_sid,
                include_soft_deleted=include_soft_deleted,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401RecordingWithRawResponse:
        return self._with_raw_response


class Api20100401RecordingWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_recording(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a recording from your account

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording resources to delete.
            sid: The Twilio-provided string that uniquely identifies the Recording resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Recordings/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_recording(
        self,
        account_sid: str,
        sid: str,
        *,
        include_soft_deleted: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountRecording, RawError]:
        """Fetch an instance of a recording

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the Recording resource to fetch.
            include_soft_deleted: A boolean parameter indicating whether to retrieve soft deleted recordings or not.
                Recordings metadata are kept after deletion for a retention period of 40 days.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Recordings/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            query_params=[param[bool | None]("IncludeSoftDeleted", include_soft_deleted)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountRecording],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_recording(
        self,
        account_sid: str,
        *,
        date_created: RFC3339DateTime | None = None,
        date_created_query: RFC3339DateTime | None = None,
        date_created_query_query: RFC3339DateTime | None = None,
        call_sid: str | None = None,
        conference_sid: str | None = None,
        include_soft_deleted: bool | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListRecordingResponse, RawError]:
        """Retrieve a list of recordings belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording resources to read.
            date_created: Only include recordings that were created on this date. Specify a date as ``YYYY-MM-DD`` in
                GMT, for example: ``2009-07-06``, to read recordings that were created on this date. You can also
                specify an inequality, such as ``DateCreated<=YYYY-MM-DD``, to read recordings that were created on or
                before midnight of this date, and ``DateCreated>=YYYY-MM-DD`` to read recordings that were created on or
                after midnight of this date.
            date_created_query: Only include recordings that were created on this date. Specify a date as ``YYYY-MM-DD``
                in GMT, for example: ``2009-07-06``, to read recordings that were created on this date. You can also
                specify an inequality, such as ``DateCreated<=YYYY-MM-DD``, to read recordings that were created on or
                before midnight of this date, and ``DateCreated>=YYYY-MM-DD`` to read recordings that were created on or
                after midnight of this date.
            date_created_query_query: Only include recordings that were created on this date. Specify a date as
                ``YYYY-MM-DD`` in GMT, for example: ``2009-07-06``, to read recordings that were created on this date.
                You can also specify an inequality, such as ``DateCreated<=YYYY-MM-DD``, to read recordings that were
                created on or before midnight of this date, and ``DateCreated>=YYYY-MM-DD`` to read recordings that were
                created on or after midnight of this date.
            call_sid: The `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ SID of the resources to read.
            conference_sid: The Conference SID that identifies the conference associated with the recording to read.
            include_soft_deleted: A boolean parameter indicating whether to retrieve soft deleted recordings or not.
                Recordings metadata are kept after deletion for a retention period of 40 days.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Recordings.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            query_params=[
                param[RFC3339DateTime | None]("DateCreated", date_created),
                param[RFC3339DateTime | None]("DateCreated<", date_created_query),
                param[RFC3339DateTime | None]("DateCreated>", date_created_query_query),
                param[str | None]("CallSid", call_sid),
                param[str | None]("ConferenceSid", conference_sid),
                param[bool | None]("IncludeSoftDeleted", include_soft_deleted),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListRecordingResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401RecordingWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_recording(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a recording from your account

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording resources to delete.
            sid: The Twilio-provided string that uniquely identifies the Recording resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Recordings/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_recording(
        self,
        account_sid: str,
        sid: str,
        *,
        include_soft_deleted: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountRecording, RawError]:
        """Fetch an instance of a recording

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the Recording resource to fetch.
            include_soft_deleted: A boolean parameter indicating whether to retrieve soft deleted recordings or not.
                Recordings metadata are kept after deletion for a retention period of 40 days.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Recordings/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            query_params=[param[bool | None]("IncludeSoftDeleted", include_soft_deleted)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountRecording],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_recording(
        self,
        account_sid: str,
        *,
        date_created: RFC3339DateTime | None = None,
        date_created_query: RFC3339DateTime | None = None,
        date_created_query_query: RFC3339DateTime | None = None,
        call_sid: str | None = None,
        conference_sid: str | None = None,
        include_soft_deleted: bool | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListRecordingResponse, RawError]:
        """Retrieve a list of recordings belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording resources to read.
            date_created: Only include recordings that were created on this date. Specify a date as ``YYYY-MM-DD`` in
                GMT, for example: ``2009-07-06``, to read recordings that were created on this date. You can also
                specify an inequality, such as ``DateCreated<=YYYY-MM-DD``, to read recordings that were created on or
                before midnight of this date, and ``DateCreated>=YYYY-MM-DD`` to read recordings that were created on or
                after midnight of this date.
            date_created_query: Only include recordings that were created on this date. Specify a date as ``YYYY-MM-DD``
                in GMT, for example: ``2009-07-06``, to read recordings that were created on this date. You can also
                specify an inequality, such as ``DateCreated<=YYYY-MM-DD``, to read recordings that were created on or
                before midnight of this date, and ``DateCreated>=YYYY-MM-DD`` to read recordings that were created on or
                after midnight of this date.
            date_created_query_query: Only include recordings that were created on this date. Specify a date as
                ``YYYY-MM-DD`` in GMT, for example: ``2009-07-06``, to read recordings that were created on this date.
                You can also specify an inequality, such as ``DateCreated<=YYYY-MM-DD``, to read recordings that were
                created on or before midnight of this date, and ``DateCreated>=YYYY-MM-DD`` to read recordings that were
                created on or after midnight of this date.
            call_sid: The `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ SID of the resources to read.
            conference_sid: The Conference SID that identifies the conference associated with the recording to read.
            include_soft_deleted: A boolean parameter indicating whether to retrieve soft deleted recordings or not.
                Recordings metadata are kept after deletion for a retention period of 40 days.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Recordings.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            query_params=[
                param[RFC3339DateTime | None]("DateCreated", date_created),
                param[RFC3339DateTime | None]("DateCreated<", date_created_query),
                param[RFC3339DateTime | None]("DateCreated>", date_created_query_query),
                param[str | None]("CallSid", call_sid),
                param[str | None]("ConferenceSid", conference_sid),
                param[bool | None]("IncludeSoftDeleted", include_soft_deleted),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListRecordingResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
