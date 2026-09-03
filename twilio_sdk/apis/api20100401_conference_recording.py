from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    Date,
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
from ..models.api_v2010_account_conference_conference_recording import ApiV2010AccountConferenceConferenceRecording
from ..models.enums.conference_recording_enum_status import ConferenceRecordingEnumStatusOrStr
from ..models.list_conference_recording_response import ListConferenceRecordingResponse
from ..server.server import Server


class Api20100401ConferenceRecording:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401ConferenceRecordingWithRawResponse(client, server, auth)

    def delete_conference_recording(
        self, account_sid: str, conference_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a recording from your account

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Conference Recording resources to delete.
            conference_sid: The Conference SID that identifies the conference associated with the recording to delete.
            sid: The Twilio-provided string that uniquely identifies the Conference Recording resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_conference_recording(
            account_sid, conference_sid, sid, request_options=request_options
        ).unwrap()

    def fetch_conference_recording(
        self, account_sid: str, conference_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountConferenceConferenceRecording:
        """Fetch an instance of a recording for a call

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Conference Recording resource to fetch.
            conference_sid: The Conference SID that identifies the conference associated with the recording to fetch.
            sid: The Twilio-provided string that uniquely identifies the Conference Recording resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_conference_recording(
            account_sid, conference_sid, sid, request_options=request_options
        ).unwrap()

    def list_conference_recording(
        self,
        account_sid: str,
        conference_sid: str,
        *,
        date_created: Date | None = None,
        date_created_query: Date | None = None,
        date_created_query_query: Date | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListConferenceRecordingResponse:
        """Retrieve a list of recordings belonging to the call used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Conference Recording resources to read.
            conference_sid: The Conference SID that identifies the conference associated with the recording to read.
            date_created: The ``date_created`` value, specified as ``YYYY-MM-DD``, of the resources to read. You can
                also specify inequality: ``DateCreated<=YYYY-MM-DD`` will return recordings generated at or before
                midnight on a given date, and ``DateCreated>=YYYY-MM-DD`` returns recordings generated at or after
                midnight on a date.
            date_created_query: The ``date_created`` value, specified as ``YYYY-MM-DD``, of the resources to read. You
                can also specify inequality: ``DateCreated<=YYYY-MM-DD`` will return recordings generated at or before
                midnight on a given date, and ``DateCreated>=YYYY-MM-DD`` returns recordings generated at or after
                midnight on a date.
            date_created_query_query: The ``date_created`` value, specified as ``YYYY-MM-DD``, of the resources to read.
                You can also specify inequality: ``DateCreated<=YYYY-MM-DD`` will return recordings generated at or
                before midnight on a given date, and ``DateCreated>=YYYY-MM-DD`` returns recordings generated at or
                after midnight on a date.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_conference_recording(
            account_sid,
            conference_sid,
            date_created=date_created,
            date_created_query=date_created_query,
            date_created_query_query=date_created_query_query,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_conference_recording(
        self,
        account_sid: str,
        conference_sid: str,
        sid: str,
        status: ConferenceRecordingEnumStatusOrStr,
        *,
        pause_behavior: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountConferenceConferenceRecording:
        """Changes the status of the recording to paused, stopped, or in-progress. Note: To use ``Twilio.CURRENT``, pass
        it as recording sid.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Conference Recording resource to update.
            conference_sid: The Conference SID that identifies the conference associated with the recording to update.
            sid: The Twilio-provided string that uniquely identifies the Conference Recording resource to update. Use
                ``Twilio.CURRENT`` to reference the current active recording.
            status: The status of the recording. Can be: ``processing``, ``completed`` and ``absent``. For more detailed
                statuses on in-progress recordings, check out how to `Update a Recording Resource
                <https://www.twilio.com/docs/voice/api/recording#update-a-recording-resource>`__.
            pause_behavior: Whether to record during a pause. Can be: ``skip`` or ``silence`` and the default is
                ``silence``. ``skip`` does not record during the pause period, while ``silence`` will replace the actual
                audio of the call with silence during the pause period. This parameter only applies when setting
                ``status`` is set to ``paused``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_conference_recording(
            account_sid, conference_sid, sid, status, pause_behavior=pause_behavior, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401ConferenceRecordingWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401ConferenceRecording:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401ConferenceRecordingWithRawResponse(client, server, auth)

    async def delete_conference_recording(
        self, account_sid: str, conference_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a recording from your account

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Conference Recording resources to delete.
            conference_sid: The Conference SID that identifies the conference associated with the recording to delete.
            sid: The Twilio-provided string that uniquely identifies the Conference Recording resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_conference_recording(
                account_sid, conference_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def fetch_conference_recording(
        self, account_sid: str, conference_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountConferenceConferenceRecording:
        """Fetch an instance of a recording for a call

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Conference Recording resource to fetch.
            conference_sid: The Conference SID that identifies the conference associated with the recording to fetch.
            sid: The Twilio-provided string that uniquely identifies the Conference Recording resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_conference_recording(
                account_sid, conference_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def list_conference_recording(
        self,
        account_sid: str,
        conference_sid: str,
        *,
        date_created: Date | None = None,
        date_created_query: Date | None = None,
        date_created_query_query: Date | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListConferenceRecordingResponse:
        """Retrieve a list of recordings belonging to the call used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Conference Recording resources to read.
            conference_sid: The Conference SID that identifies the conference associated with the recording to read.
            date_created: The ``date_created`` value, specified as ``YYYY-MM-DD``, of the resources to read. You can
                also specify inequality: ``DateCreated<=YYYY-MM-DD`` will return recordings generated at or before
                midnight on a given date, and ``DateCreated>=YYYY-MM-DD`` returns recordings generated at or after
                midnight on a date.
            date_created_query: The ``date_created`` value, specified as ``YYYY-MM-DD``, of the resources to read. You
                can also specify inequality: ``DateCreated<=YYYY-MM-DD`` will return recordings generated at or before
                midnight on a given date, and ``DateCreated>=YYYY-MM-DD`` returns recordings generated at or after
                midnight on a date.
            date_created_query_query: The ``date_created`` value, specified as ``YYYY-MM-DD``, of the resources to read.
                You can also specify inequality: ``DateCreated<=YYYY-MM-DD`` will return recordings generated at or
                before midnight on a given date, and ``DateCreated>=YYYY-MM-DD`` returns recordings generated at or
                after midnight on a date.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_conference_recording(
                account_sid,
                conference_sid,
                date_created=date_created,
                date_created_query=date_created_query,
                date_created_query_query=date_created_query_query,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_conference_recording(
        self,
        account_sid: str,
        conference_sid: str,
        sid: str,
        status: ConferenceRecordingEnumStatusOrStr,
        *,
        pause_behavior: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountConferenceConferenceRecording:
        """Changes the status of the recording to paused, stopped, or in-progress. Note: To use ``Twilio.CURRENT``, pass
        it as recording sid.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Conference Recording resource to update.
            conference_sid: The Conference SID that identifies the conference associated with the recording to update.
            sid: The Twilio-provided string that uniquely identifies the Conference Recording resource to update. Use
                ``Twilio.CURRENT`` to reference the current active recording.
            status: The status of the recording. Can be: ``processing``, ``completed`` and ``absent``. For more detailed
                statuses on in-progress recordings, check out how to `Update a Recording Resource
                <https://www.twilio.com/docs/voice/api/recording#update-a-recording-resource>`__.
            pause_behavior: Whether to record during a pause. Can be: ``skip`` or ``silence`` and the default is
                ``silence``. ``skip`` does not record during the pause period, while ``silence`` will replace the actual
                audio of the call with silence during the pause period. This parameter only applies when setting
                ``status`` is set to ``paused``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_conference_recording(
                account_sid, conference_sid, sid, status, pause_behavior=pause_behavior, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401ConferenceRecordingWithRawResponse:
        return self._with_raw_response


class Api20100401ConferenceRecordingWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_conference_recording(
        self, account_sid: str, conference_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a recording from your account

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Conference Recording resources to delete.
            conference_sid: The Conference SID that identifies the conference associated with the recording to delete.
            sid: The Twilio-provided string that uniquely identifies the Conference Recording resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Recordings/{Sid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("ConferenceSid", conference_sid),
                param[str]("Sid", sid),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_conference_recording(
        self, account_sid: str, conference_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountConferenceConferenceRecording, RawError]:
        """Fetch an instance of a recording for a call

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Conference Recording resource to fetch.
            conference_sid: The Conference SID that identifies the conference associated with the recording to fetch.
            sid: The Twilio-provided string that uniquely identifies the Conference Recording resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Recordings/{Sid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("ConferenceSid", conference_sid),
                param[str]("Sid", sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountConferenceConferenceRecording],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_conference_recording(
        self,
        account_sid: str,
        conference_sid: str,
        *,
        date_created: Date | None = None,
        date_created_query: Date | None = None,
        date_created_query_query: Date | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListConferenceRecordingResponse, RawError]:
        """Retrieve a list of recordings belonging to the call used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Conference Recording resources to read.
            conference_sid: The Conference SID that identifies the conference associated with the recording to read.
            date_created: The ``date_created`` value, specified as ``YYYY-MM-DD``, of the resources to read. You can
                also specify inequality: ``DateCreated<=YYYY-MM-DD`` will return recordings generated at or before
                midnight on a given date, and ``DateCreated>=YYYY-MM-DD`` returns recordings generated at or after
                midnight on a date.
            date_created_query: The ``date_created`` value, specified as ``YYYY-MM-DD``, of the resources to read. You
                can also specify inequality: ``DateCreated<=YYYY-MM-DD`` will return recordings generated at or before
                midnight on a given date, and ``DateCreated>=YYYY-MM-DD`` returns recordings generated at or after
                midnight on a date.
            date_created_query_query: The ``date_created`` value, specified as ``YYYY-MM-DD``, of the resources to read.
                You can also specify inequality: ``DateCreated<=YYYY-MM-DD`` will return recordings generated at or
                before midnight on a given date, and ``DateCreated>=YYYY-MM-DD`` returns recordings generated at or
                after midnight on a date.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Recordings.json"
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("ConferenceSid", conference_sid)],
            query_params=[
                param[Date | None]("DateCreated", date_created),
                param[Date | None]("DateCreated<", date_created_query),
                param[Date | None]("DateCreated>", date_created_query_query),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListConferenceRecordingResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_conference_recording(
        self,
        account_sid: str,
        conference_sid: str,
        sid: str,
        status: ConferenceRecordingEnumStatusOrStr,
        *,
        pause_behavior: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountConferenceConferenceRecording, RawError]:
        """Changes the status of the recording to paused, stopped, or in-progress. Note: To use ``Twilio.CURRENT``, pass
        it as recording sid.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Conference Recording resource to update.
            conference_sid: The Conference SID that identifies the conference associated with the recording to update.
            sid: The Twilio-provided string that uniquely identifies the Conference Recording resource to update. Use
                ``Twilio.CURRENT`` to reference the current active recording.
            status: The status of the recording. Can be: ``processing``, ``completed`` and ``absent``. For more detailed
                statuses on in-progress recordings, check out how to `Update a Recording Resource
                <https://www.twilio.com/docs/voice/api/recording#update-a-recording-resource>`__.
            pause_behavior: Whether to record during a pause. Can be: ``skip`` or ``silence`` and the default is
                ``silence``. ``skip`` does not record during the pause period, while ``silence`` will replace the actual
                audio of the call with silence during the pause period. This parameter only applies when setting
                ``status`` is set to ``paused``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Recordings/{Sid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("ConferenceSid", conference_sid),
                param[str]("Sid", sid),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[ConferenceRecordingEnumStatusOrStr]("Status", status),
                    param[str | None]("PauseBehavior", pause_behavior),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountConferenceConferenceRecording],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401ConferenceRecordingWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_conference_recording(
        self, account_sid: str, conference_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a recording from your account

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Conference Recording resources to delete.
            conference_sid: The Conference SID that identifies the conference associated with the recording to delete.
            sid: The Twilio-provided string that uniquely identifies the Conference Recording resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Recordings/{Sid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("ConferenceSid", conference_sid),
                param[str]("Sid", sid),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_conference_recording(
        self, account_sid: str, conference_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountConferenceConferenceRecording, RawError]:
        """Fetch an instance of a recording for a call

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Conference Recording resource to fetch.
            conference_sid: The Conference SID that identifies the conference associated with the recording to fetch.
            sid: The Twilio-provided string that uniquely identifies the Conference Recording resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Recordings/{Sid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("ConferenceSid", conference_sid),
                param[str]("Sid", sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountConferenceConferenceRecording],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_conference_recording(
        self,
        account_sid: str,
        conference_sid: str,
        *,
        date_created: Date | None = None,
        date_created_query: Date | None = None,
        date_created_query_query: Date | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListConferenceRecordingResponse, RawError]:
        """Retrieve a list of recordings belonging to the call used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Conference Recording resources to read.
            conference_sid: The Conference SID that identifies the conference associated with the recording to read.
            date_created: The ``date_created`` value, specified as ``YYYY-MM-DD``, of the resources to read. You can
                also specify inequality: ``DateCreated<=YYYY-MM-DD`` will return recordings generated at or before
                midnight on a given date, and ``DateCreated>=YYYY-MM-DD`` returns recordings generated at or after
                midnight on a date.
            date_created_query: The ``date_created`` value, specified as ``YYYY-MM-DD``, of the resources to read. You
                can also specify inequality: ``DateCreated<=YYYY-MM-DD`` will return recordings generated at or before
                midnight on a given date, and ``DateCreated>=YYYY-MM-DD`` returns recordings generated at or after
                midnight on a date.
            date_created_query_query: The ``date_created`` value, specified as ``YYYY-MM-DD``, of the resources to read.
                You can also specify inequality: ``DateCreated<=YYYY-MM-DD`` will return recordings generated at or
                before midnight on a given date, and ``DateCreated>=YYYY-MM-DD`` returns recordings generated at or
                after midnight on a date.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Recordings.json"
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("ConferenceSid", conference_sid)],
            query_params=[
                param[Date | None]("DateCreated", date_created),
                param[Date | None]("DateCreated<", date_created_query),
                param[Date | None]("DateCreated>", date_created_query_query),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListConferenceRecordingResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_conference_recording(
        self,
        account_sid: str,
        conference_sid: str,
        sid: str,
        status: ConferenceRecordingEnumStatusOrStr,
        *,
        pause_behavior: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountConferenceConferenceRecording, RawError]:
        """Changes the status of the recording to paused, stopped, or in-progress. Note: To use ``Twilio.CURRENT``, pass
        it as recording sid.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Conference Recording resource to update.
            conference_sid: The Conference SID that identifies the conference associated with the recording to update.
            sid: The Twilio-provided string that uniquely identifies the Conference Recording resource to update. Use
                ``Twilio.CURRENT`` to reference the current active recording.
            status: The status of the recording. Can be: ``processing``, ``completed`` and ``absent``. For more detailed
                statuses on in-progress recordings, check out how to `Update a Recording Resource
                <https://www.twilio.com/docs/voice/api/recording#update-a-recording-resource>`__.
            pause_behavior: Whether to record during a pause. Can be: ``skip`` or ``silence`` and the default is
                ``silence``. ``skip`` does not record during the pause period, while ``silence`` will replace the actual
                audio of the call with silence during the pause period. This parameter only applies when setting
                ``status`` is set to ``paused``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Recordings/{Sid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("ConferenceSid", conference_sid),
                param[str]("Sid", sid),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[ConferenceRecordingEnumStatusOrStr]("Status", status),
                    param[str | None]("PauseBehavior", pause_behavior),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountConferenceConferenceRecording],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
