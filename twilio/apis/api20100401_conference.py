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
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.api_v2010_account_conference import ApiV2010AccountConference
from ..models.enums.announce_method import AnnounceMethodOrStr
from ..models.enums.conference_enum_status import ConferenceEnumStatusOrStr
from ..models.enums.conference_enum_update_status import ConferenceEnumUpdateStatusOrStr
from ..models.list_conference_response import ListConferenceResponse
from ..server.server import Server


class Api20100401Conference:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401ConferenceWithRawResponse(client, server, auth)

    def fetch_conference(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountConference:
        """Fetch an instance of a conference

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Conference resource(s) to fetch.
            sid: The Twilio-provided string that uniquely identifies the Conference resource to fetch
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_conference(account_sid, sid, request_options=request_options).unwrap()

    def list_conference(
        self,
        account_sid: str,
        *,
        date_created: Date | None = None,
        date_created_query: Date | None = None,
        date_created_query_query: Date | None = None,
        date_updated: Date | None = None,
        date_updated_query: Date | None = None,
        date_updated_query_query: Date | None = None,
        friendly_name: str | None = None,
        status: ConferenceEnumStatusOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListConferenceResponse:
        """Retrieve a list of conferences belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Conference resource(s) to read.
            date_created: Only include conferences that were created on this date. Specify a date as ``YYYY-MM-DD`` in
                UTC, for example: ``2009-07-06``, to read only conferences that were created on this date. You can also
                specify an inequality, such as ``DateCreated<=YYYY-MM-DD``, to read conferences that were created on or
                before midnight of this date, and ``DateCreated>=YYYY-MM-DD`` to read conferences that were created on
                or after midnight of this date.
            date_created_query: Only include conferences that were created on this date. Specify a date as
                ``YYYY-MM-DD`` in UTC, for example: ``2009-07-06``, to read only conferences that were created on this
                date. You can also specify an inequality, such as ``DateCreated<=YYYY-MM-DD``, to read conferences that
                were created on or before midnight of this date, and ``DateCreated>=YYYY-MM-DD`` to read conferences
                that were created on or after midnight of this date.
            date_created_query_query: Only include conferences that were created on this date. Specify a date as
                ``YYYY-MM-DD`` in UTC, for example: ``2009-07-06``, to read only conferences that were created on this
                date. You can also specify an inequality, such as ``DateCreated<=YYYY-MM-DD``, to read conferences that
                were created on or before midnight of this date, and ``DateCreated>=YYYY-MM-DD`` to read conferences
                that were created on or after midnight of this date.
            date_updated: Only include conferences that were last updated on this date. Specify a date as ``YYYY-MM-DD``
                in UTC, for example: ``2009-07-06``, to read only conferences that were last updated on this date. You
                can also specify an inequality, such as ``DateUpdated<=YYYY-MM-DD``, to read conferences that were last
                updated on or before midnight of this date, and ``DateUpdated>=YYYY-MM-DD`` to read conferences that
                were last updated on or after midnight of this date.
            date_updated_query: Only include conferences that were last updated on this date. Specify a date as
                ``YYYY-MM-DD`` in UTC, for example: ``2009-07-06``, to read only conferences that were last updated on
                this date. You can also specify an inequality, such as ``DateUpdated<=YYYY-MM-DD``, to read conferences
                that were last updated on or before midnight of this date, and ``DateUpdated>=YYYY-MM-DD`` to read
                conferences that were last updated on or after midnight of this date.
            date_updated_query_query: Only include conferences that were last updated on this date. Specify a date as
                ``YYYY-MM-DD`` in UTC, for example: ``2009-07-06``, to read only conferences that were last updated on
                this date. You can also specify an inequality, such as ``DateUpdated<=YYYY-MM-DD``, to read conferences
                that were last updated on or before midnight of this date, and ``DateUpdated>=YYYY-MM-DD`` to read
                conferences that were last updated on or after midnight of this date.
            friendly_name: The string that identifies the Conference resources to read.
            status: The status of the resources to read. Can be: ``init``, ``in-progress``, or ``completed``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_conference(
            account_sid,
            date_created=date_created,
            date_created_query=date_created_query,
            date_created_query_query=date_created_query_query,
            date_updated=date_updated,
            date_updated_query=date_updated_query,
            date_updated_query_query=date_updated_query_query,
            friendly_name=friendly_name,
            status=status,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_conference(
        self,
        account_sid: str,
        sid: str,
        *,
        status: ConferenceEnumUpdateStatusOrStr | None = None,
        announce_url: str | None = None,
        announce_method: AnnounceMethodOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountConference:
        """Voice call conferences

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Conference resource(s) to update.
            sid: The Twilio-provided string that uniquely identifies the Conference resource to update
            status: Value sent with the request.
            announce_url: The URL we should call to announce something into the conference. The URL may return an MP3
                file, a WAV file, or a TwiML document that contains ``<Play>``, ``<Say>``, ``<Pause>``, or
                ``<Redirect>`` verbs.
            announce_method: The HTTP method used to call ``announce_url``. Can be: ``GET`` or ``POST`` and the default
                is ``POST``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_conference(
            account_sid,
            sid,
            status=status,
            announce_url=announce_url,
            announce_method=announce_method,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401ConferenceWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401Conference:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401ConferenceWithRawResponse(client, server, auth)

    async def fetch_conference(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountConference:
        """Fetch an instance of a conference

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Conference resource(s) to fetch.
            sid: The Twilio-provided string that uniquely identifies the Conference resource to fetch
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_conference(account_sid, sid, request_options=request_options)
        ).unwrap()

    async def list_conference(
        self,
        account_sid: str,
        *,
        date_created: Date | None = None,
        date_created_query: Date | None = None,
        date_created_query_query: Date | None = None,
        date_updated: Date | None = None,
        date_updated_query: Date | None = None,
        date_updated_query_query: Date | None = None,
        friendly_name: str | None = None,
        status: ConferenceEnumStatusOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListConferenceResponse:
        """Retrieve a list of conferences belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Conference resource(s) to read.
            date_created: Only include conferences that were created on this date. Specify a date as ``YYYY-MM-DD`` in
                UTC, for example: ``2009-07-06``, to read only conferences that were created on this date. You can also
                specify an inequality, such as ``DateCreated<=YYYY-MM-DD``, to read conferences that were created on or
                before midnight of this date, and ``DateCreated>=YYYY-MM-DD`` to read conferences that were created on
                or after midnight of this date.
            date_created_query: Only include conferences that were created on this date. Specify a date as
                ``YYYY-MM-DD`` in UTC, for example: ``2009-07-06``, to read only conferences that were created on this
                date. You can also specify an inequality, such as ``DateCreated<=YYYY-MM-DD``, to read conferences that
                were created on or before midnight of this date, and ``DateCreated>=YYYY-MM-DD`` to read conferences
                that were created on or after midnight of this date.
            date_created_query_query: Only include conferences that were created on this date. Specify a date as
                ``YYYY-MM-DD`` in UTC, for example: ``2009-07-06``, to read only conferences that were created on this
                date. You can also specify an inequality, such as ``DateCreated<=YYYY-MM-DD``, to read conferences that
                were created on or before midnight of this date, and ``DateCreated>=YYYY-MM-DD`` to read conferences
                that were created on or after midnight of this date.
            date_updated: Only include conferences that were last updated on this date. Specify a date as ``YYYY-MM-DD``
                in UTC, for example: ``2009-07-06``, to read only conferences that were last updated on this date. You
                can also specify an inequality, such as ``DateUpdated<=YYYY-MM-DD``, to read conferences that were last
                updated on or before midnight of this date, and ``DateUpdated>=YYYY-MM-DD`` to read conferences that
                were last updated on or after midnight of this date.
            date_updated_query: Only include conferences that were last updated on this date. Specify a date as
                ``YYYY-MM-DD`` in UTC, for example: ``2009-07-06``, to read only conferences that were last updated on
                this date. You can also specify an inequality, such as ``DateUpdated<=YYYY-MM-DD``, to read conferences
                that were last updated on or before midnight of this date, and ``DateUpdated>=YYYY-MM-DD`` to read
                conferences that were last updated on or after midnight of this date.
            date_updated_query_query: Only include conferences that were last updated on this date. Specify a date as
                ``YYYY-MM-DD`` in UTC, for example: ``2009-07-06``, to read only conferences that were last updated on
                this date. You can also specify an inequality, such as ``DateUpdated<=YYYY-MM-DD``, to read conferences
                that were last updated on or before midnight of this date, and ``DateUpdated>=YYYY-MM-DD`` to read
                conferences that were last updated on or after midnight of this date.
            friendly_name: The string that identifies the Conference resources to read.
            status: The status of the resources to read. Can be: ``init``, ``in-progress``, or ``completed``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_conference(
                account_sid,
                date_created=date_created,
                date_created_query=date_created_query,
                date_created_query_query=date_created_query_query,
                date_updated=date_updated,
                date_updated_query=date_updated_query,
                date_updated_query_query=date_updated_query_query,
                friendly_name=friendly_name,
                status=status,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_conference(
        self,
        account_sid: str,
        sid: str,
        *,
        status: ConferenceEnumUpdateStatusOrStr | None = None,
        announce_url: str | None = None,
        announce_method: AnnounceMethodOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountConference:
        """Voice call conferences

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Conference resource(s) to update.
            sid: The Twilio-provided string that uniquely identifies the Conference resource to update
            status: Value sent with the request.
            announce_url: The URL we should call to announce something into the conference. The URL may return an MP3
                file, a WAV file, or a TwiML document that contains ``<Play>``, ``<Say>``, ``<Pause>``, or
                ``<Redirect>`` verbs.
            announce_method: The HTTP method used to call ``announce_url``. Can be: ``GET`` or ``POST`` and the default
                is ``POST``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_conference(
                account_sid,
                sid,
                status=status,
                announce_url=announce_url,
                announce_method=announce_method,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401ConferenceWithRawResponse:
        return self._with_raw_response


class Api20100401ConferenceWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_conference(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountConference, RawError]:
        """Fetch an instance of a conference

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Conference resource(s) to fetch.
            sid: The Twilio-provided string that uniquely identifies the Conference resource to fetch
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Conferences/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountConference],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_conference(
        self,
        account_sid: str,
        *,
        date_created: Date | None = None,
        date_created_query: Date | None = None,
        date_created_query_query: Date | None = None,
        date_updated: Date | None = None,
        date_updated_query: Date | None = None,
        date_updated_query_query: Date | None = None,
        friendly_name: str | None = None,
        status: ConferenceEnumStatusOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListConferenceResponse, RawError]:
        """Retrieve a list of conferences belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Conference resource(s) to read.
            date_created: Only include conferences that were created on this date. Specify a date as ``YYYY-MM-DD`` in
                UTC, for example: ``2009-07-06``, to read only conferences that were created on this date. You can also
                specify an inequality, such as ``DateCreated<=YYYY-MM-DD``, to read conferences that were created on or
                before midnight of this date, and ``DateCreated>=YYYY-MM-DD`` to read conferences that were created on
                or after midnight of this date.
            date_created_query: Only include conferences that were created on this date. Specify a date as
                ``YYYY-MM-DD`` in UTC, for example: ``2009-07-06``, to read only conferences that were created on this
                date. You can also specify an inequality, such as ``DateCreated<=YYYY-MM-DD``, to read conferences that
                were created on or before midnight of this date, and ``DateCreated>=YYYY-MM-DD`` to read conferences
                that were created on or after midnight of this date.
            date_created_query_query: Only include conferences that were created on this date. Specify a date as
                ``YYYY-MM-DD`` in UTC, for example: ``2009-07-06``, to read only conferences that were created on this
                date. You can also specify an inequality, such as ``DateCreated<=YYYY-MM-DD``, to read conferences that
                were created on or before midnight of this date, and ``DateCreated>=YYYY-MM-DD`` to read conferences
                that were created on or after midnight of this date.
            date_updated: Only include conferences that were last updated on this date. Specify a date as ``YYYY-MM-DD``
                in UTC, for example: ``2009-07-06``, to read only conferences that were last updated on this date. You
                can also specify an inequality, such as ``DateUpdated<=YYYY-MM-DD``, to read conferences that were last
                updated on or before midnight of this date, and ``DateUpdated>=YYYY-MM-DD`` to read conferences that
                were last updated on or after midnight of this date.
            date_updated_query: Only include conferences that were last updated on this date. Specify a date as
                ``YYYY-MM-DD`` in UTC, for example: ``2009-07-06``, to read only conferences that were last updated on
                this date. You can also specify an inequality, such as ``DateUpdated<=YYYY-MM-DD``, to read conferences
                that were last updated on or before midnight of this date, and ``DateUpdated>=YYYY-MM-DD`` to read
                conferences that were last updated on or after midnight of this date.
            date_updated_query_query: Only include conferences that were last updated on this date. Specify a date as
                ``YYYY-MM-DD`` in UTC, for example: ``2009-07-06``, to read only conferences that were last updated on
                this date. You can also specify an inequality, such as ``DateUpdated<=YYYY-MM-DD``, to read conferences
                that were last updated on or before midnight of this date, and ``DateUpdated>=YYYY-MM-DD`` to read
                conferences that were last updated on or after midnight of this date.
            friendly_name: The string that identifies the Conference resources to read.
            status: The status of the resources to read. Can be: ``init``, ``in-progress``, or ``completed``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Conferences.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            query_params=[
                param[Date | None]("DateCreated", date_created),
                param[Date | None]("DateCreated<", date_created_query),
                param[Date | None]("DateCreated>", date_created_query_query),
                param[Date | None]("DateUpdated", date_updated),
                param[Date | None]("DateUpdated<", date_updated_query),
                param[Date | None]("DateUpdated>", date_updated_query_query),
                param[str | None]("FriendlyName", friendly_name),
                param[ConferenceEnumStatusOrStr | None]("Status", status),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListConferenceResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_conference(
        self,
        account_sid: str,
        sid: str,
        *,
        status: ConferenceEnumUpdateStatusOrStr | None = None,
        announce_url: str | None = None,
        announce_method: AnnounceMethodOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountConference, RawError]:
        """Voice call conferences

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Conference resource(s) to update.
            sid: The Twilio-provided string that uniquely identifies the Conference resource to update
            status: Value sent with the request.
            announce_url: The URL we should call to announce something into the conference. The URL may return an MP3
                file, a WAV file, or a TwiML document that contains ``<Play>``, ``<Say>``, ``<Pause>``, or
                ``<Redirect>`` verbs.
            announce_method: The HTTP method used to call ``announce_url``. Can be: ``GET`` or ``POST`` and the default
                is ``POST``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Conferences/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            body=form_body(
                [
                    param[ConferenceEnumUpdateStatusOrStr | None]("Status", status),
                    param[str | None]("AnnounceUrl", announce_url),
                    param[AnnounceMethodOrStr | None]("AnnounceMethod", announce_method),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountConference],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401ConferenceWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_conference(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountConference, RawError]:
        """Fetch an instance of a conference

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Conference resource(s) to fetch.
            sid: The Twilio-provided string that uniquely identifies the Conference resource to fetch
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Conferences/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountConference],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_conference(
        self,
        account_sid: str,
        *,
        date_created: Date | None = None,
        date_created_query: Date | None = None,
        date_created_query_query: Date | None = None,
        date_updated: Date | None = None,
        date_updated_query: Date | None = None,
        date_updated_query_query: Date | None = None,
        friendly_name: str | None = None,
        status: ConferenceEnumStatusOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListConferenceResponse, RawError]:
        """Retrieve a list of conferences belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Conference resource(s) to read.
            date_created: Only include conferences that were created on this date. Specify a date as ``YYYY-MM-DD`` in
                UTC, for example: ``2009-07-06``, to read only conferences that were created on this date. You can also
                specify an inequality, such as ``DateCreated<=YYYY-MM-DD``, to read conferences that were created on or
                before midnight of this date, and ``DateCreated>=YYYY-MM-DD`` to read conferences that were created on
                or after midnight of this date.
            date_created_query: Only include conferences that were created on this date. Specify a date as
                ``YYYY-MM-DD`` in UTC, for example: ``2009-07-06``, to read only conferences that were created on this
                date. You can also specify an inequality, such as ``DateCreated<=YYYY-MM-DD``, to read conferences that
                were created on or before midnight of this date, and ``DateCreated>=YYYY-MM-DD`` to read conferences
                that were created on or after midnight of this date.
            date_created_query_query: Only include conferences that were created on this date. Specify a date as
                ``YYYY-MM-DD`` in UTC, for example: ``2009-07-06``, to read only conferences that were created on this
                date. You can also specify an inequality, such as ``DateCreated<=YYYY-MM-DD``, to read conferences that
                were created on or before midnight of this date, and ``DateCreated>=YYYY-MM-DD`` to read conferences
                that were created on or after midnight of this date.
            date_updated: Only include conferences that were last updated on this date. Specify a date as ``YYYY-MM-DD``
                in UTC, for example: ``2009-07-06``, to read only conferences that were last updated on this date. You
                can also specify an inequality, such as ``DateUpdated<=YYYY-MM-DD``, to read conferences that were last
                updated on or before midnight of this date, and ``DateUpdated>=YYYY-MM-DD`` to read conferences that
                were last updated on or after midnight of this date.
            date_updated_query: Only include conferences that were last updated on this date. Specify a date as
                ``YYYY-MM-DD`` in UTC, for example: ``2009-07-06``, to read only conferences that were last updated on
                this date. You can also specify an inequality, such as ``DateUpdated<=YYYY-MM-DD``, to read conferences
                that were last updated on or before midnight of this date, and ``DateUpdated>=YYYY-MM-DD`` to read
                conferences that were last updated on or after midnight of this date.
            date_updated_query_query: Only include conferences that were last updated on this date. Specify a date as
                ``YYYY-MM-DD`` in UTC, for example: ``2009-07-06``, to read only conferences that were last updated on
                this date. You can also specify an inequality, such as ``DateUpdated<=YYYY-MM-DD``, to read conferences
                that were last updated on or before midnight of this date, and ``DateUpdated>=YYYY-MM-DD`` to read
                conferences that were last updated on or after midnight of this date.
            friendly_name: The string that identifies the Conference resources to read.
            status: The status of the resources to read. Can be: ``init``, ``in-progress``, or ``completed``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Conferences.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            query_params=[
                param[Date | None]("DateCreated", date_created),
                param[Date | None]("DateCreated<", date_created_query),
                param[Date | None]("DateCreated>", date_created_query_query),
                param[Date | None]("DateUpdated", date_updated),
                param[Date | None]("DateUpdated<", date_updated_query),
                param[Date | None]("DateUpdated>", date_updated_query_query),
                param[str | None]("FriendlyName", friendly_name),
                param[ConferenceEnumStatusOrStr | None]("Status", status),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListConferenceResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_conference(
        self,
        account_sid: str,
        sid: str,
        *,
        status: ConferenceEnumUpdateStatusOrStr | None = None,
        announce_url: str | None = None,
        announce_method: AnnounceMethodOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountConference, RawError]:
        """Voice call conferences

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Conference resource(s) to update.
            sid: The Twilio-provided string that uniquely identifies the Conference resource to update
            status: Value sent with the request.
            announce_url: The URL we should call to announce something into the conference. The URL may return an MP3
                file, a WAV file, or a TwiML document that contains ``<Play>``, ``<Say>``, ``<Pause>``, or
                ``<Redirect>`` verbs.
            announce_method: The HTTP method used to call ``announce_url``. Can be: ``GET`` or ``POST`` and the default
                is ``POST``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Conferences/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            body=form_body(
                [
                    param[ConferenceEnumUpdateStatusOrStr | None]("Status", status),
                    param[str | None]("AnnounceUrl", announce_url),
                    param[AnnounceMethodOrStr | None]("AnnounceMethod", announce_method),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountConference],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
