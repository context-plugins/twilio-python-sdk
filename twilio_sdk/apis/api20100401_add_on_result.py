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
    json_decoder,
    param,
    raw_error_response,
)
from ..models.api_v2010_account_recording_recording_add_on_result import ApiV2010AccountRecordingRecordingAddOnResult
from ..models.list_recording_add_on_result_response import ListRecordingAddOnResultResponse
from ..server.server import Server


class Api20100401AddOnResult:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401AddOnResultWithRawResponse(client, server, auth)

    def delete_recording_add_on_result(
        self, account_sid: str, reference_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a result and purge all associated Payloads

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording AddOnResult resources to delete.
            reference_sid: The SID of the recording to which the result to delete belongs.
            sid: The Twilio-provided string that uniquely identifies the Recording AddOnResult resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_recording_add_on_result(
            account_sid, reference_sid, sid, request_options=request_options
        ).unwrap()

    def fetch_recording_add_on_result(
        self, account_sid: str, reference_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountRecordingRecordingAddOnResult:
        """Fetch an instance of an AddOnResult

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording AddOnResult resource to fetch.
            reference_sid: The SID of the recording to which the result to fetch belongs.
            sid: The Twilio-provided string that uniquely identifies the Recording AddOnResult resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_recording_add_on_result(
            account_sid, reference_sid, sid, request_options=request_options
        ).unwrap()

    def list_recording_add_on_result(
        self,
        account_sid: str,
        reference_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListRecordingAddOnResultResponse:
        """Retrieve a list of results belonging to the recording

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording AddOnResult resources to read.
            reference_sid: The SID of the recording to which the result to read belongs.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_recording_add_on_result(
            account_sid,
            reference_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401AddOnResultWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401AddOnResult:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401AddOnResultWithRawResponse(client, server, auth)

    async def delete_recording_add_on_result(
        self, account_sid: str, reference_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a result and purge all associated Payloads

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording AddOnResult resources to delete.
            reference_sid: The SID of the recording to which the result to delete belongs.
            sid: The Twilio-provided string that uniquely identifies the Recording AddOnResult resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_recording_add_on_result(
                account_sid, reference_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def fetch_recording_add_on_result(
        self, account_sid: str, reference_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountRecordingRecordingAddOnResult:
        """Fetch an instance of an AddOnResult

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording AddOnResult resource to fetch.
            reference_sid: The SID of the recording to which the result to fetch belongs.
            sid: The Twilio-provided string that uniquely identifies the Recording AddOnResult resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_recording_add_on_result(
                account_sid, reference_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def list_recording_add_on_result(
        self,
        account_sid: str,
        reference_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListRecordingAddOnResultResponse:
        """Retrieve a list of results belonging to the recording

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording AddOnResult resources to read.
            reference_sid: The SID of the recording to which the result to read belongs.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_recording_add_on_result(
                account_sid,
                reference_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401AddOnResultWithRawResponse:
        return self._with_raw_response


class Api20100401AddOnResultWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_recording_add_on_result(
        self, account_sid: str, reference_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a result and purge all associated Payloads

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording AddOnResult resources to delete.
            reference_sid: The SID of the recording to which the result to delete belongs.
            sid: The Twilio-provided string that uniquely identifies the Recording AddOnResult resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults/{Sid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid), param[str]("ReferenceSid", reference_sid), param[str]("Sid", sid)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_recording_add_on_result(
        self, account_sid: str, reference_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountRecordingRecordingAddOnResult, RawError]:
        """Fetch an instance of an AddOnResult

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording AddOnResult resource to fetch.
            reference_sid: The SID of the recording to which the result to fetch belongs.
            sid: The Twilio-provided string that uniquely identifies the Recording AddOnResult resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults/{Sid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid), param[str]("ReferenceSid", reference_sid), param[str]("Sid", sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountRecordingRecordingAddOnResult],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_recording_add_on_result(
        self,
        account_sid: str,
        reference_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListRecordingAddOnResultResponse, RawError]:
        """Retrieve a list of results belonging to the recording

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording AddOnResult resources to read.
            reference_sid: The SID of the recording to which the result to read belongs.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults.json"
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("ReferenceSid", reference_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListRecordingAddOnResultResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401AddOnResultWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_recording_add_on_result(
        self, account_sid: str, reference_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a result and purge all associated Payloads

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording AddOnResult resources to delete.
            reference_sid: The SID of the recording to which the result to delete belongs.
            sid: The Twilio-provided string that uniquely identifies the Recording AddOnResult resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults/{Sid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid), param[str]("ReferenceSid", reference_sid), param[str]("Sid", sid)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_recording_add_on_result(
        self, account_sid: str, reference_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountRecordingRecordingAddOnResult, RawError]:
        """Fetch an instance of an AddOnResult

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording AddOnResult resource to fetch.
            reference_sid: The SID of the recording to which the result to fetch belongs.
            sid: The Twilio-provided string that uniquely identifies the Recording AddOnResult resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults/{Sid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid), param[str]("ReferenceSid", reference_sid), param[str]("Sid", sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountRecordingRecordingAddOnResult],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_recording_add_on_result(
        self,
        account_sid: str,
        reference_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListRecordingAddOnResultResponse, RawError]:
        """Retrieve a list of results belonging to the recording

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording AddOnResult resources to read.
            reference_sid: The SID of the recording to which the result to read belongs.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults.json"
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("ReferenceSid", reference_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListRecordingAddOnResultResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
