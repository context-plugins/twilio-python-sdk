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
    json_decoder,
    param,
    raw_error_response,
)
from ..models.api_v2010_account_recording_recording_add_on_result_recording_add_on_result_payload import (
    ApiV2010AccountRecordingRecordingAddOnResultRecordingAddOnResultPayload,
)
from ..models.list_recording_add_on_result_payload_response import ListRecordingAddOnResultPayloadResponse
from ..server.server import Server


class Api20100401Payload:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401PayloadWithRawResponse(client, server, auth)

    def delete_recording_add_on_result_payload(
        self,
        account_sid: str,
        reference_sid: str,
        add_on_result_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Delete a payload from the result along with all associated Data

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording AddOnResult Payload resources to delete.
            reference_sid: The SID of the recording to which the AddOnResult resource that contains the payloads to
                delete belongs.
            add_on_result_sid: The SID of the AddOnResult to which the payloads to delete belongs.
            sid: The Twilio-provided string that uniquely identifies the Recording AddOnResult Payload resource to
                delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_recording_add_on_result_payload(
            account_sid, reference_sid, add_on_result_sid, sid, request_options=request_options
        ).unwrap()

    def fetch_recording_add_on_result_payload(
        self,
        account_sid: str,
        reference_sid: str,
        add_on_result_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountRecordingRecordingAddOnResultRecordingAddOnResultPayload:
        """Fetch an instance of a result payload

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording AddOnResult Payload resource to fetch.
            reference_sid: The SID of the recording to which the AddOnResult resource that contains the payload to fetch
                belongs.
            add_on_result_sid: The SID of the AddOnResult to which the payload to fetch belongs.
            sid: The Twilio-provided string that uniquely identifies the Recording AddOnResult Payload resource to
                fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_recording_add_on_result_payload(
            account_sid, reference_sid, add_on_result_sid, sid, request_options=request_options
        ).unwrap()

    def list_recording_add_on_result_payload(
        self,
        account_sid: str,
        reference_sid: str,
        add_on_result_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListRecordingAddOnResultPayloadResponse:
        """Retrieve a list of payloads belonging to the AddOnResult

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording AddOnResult Payload resources to read.
            reference_sid: The SID of the recording to which the AddOnResult resource that contains the payloads to read
                belongs.
            add_on_result_sid: The SID of the AddOnResult to which the payloads to read belongs.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_recording_add_on_result_payload(
            account_sid,
            reference_sid,
            add_on_result_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401PayloadWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401Payload:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401PayloadWithRawResponse(client, server, auth)

    async def delete_recording_add_on_result_payload(
        self,
        account_sid: str,
        reference_sid: str,
        add_on_result_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Delete a payload from the result along with all associated Data

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording AddOnResult Payload resources to delete.
            reference_sid: The SID of the recording to which the AddOnResult resource that contains the payloads to
                delete belongs.
            add_on_result_sid: The SID of the AddOnResult to which the payloads to delete belongs.
            sid: The Twilio-provided string that uniquely identifies the Recording AddOnResult Payload resource to
                delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_recording_add_on_result_payload(
                account_sid, reference_sid, add_on_result_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def fetch_recording_add_on_result_payload(
        self,
        account_sid: str,
        reference_sid: str,
        add_on_result_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountRecordingRecordingAddOnResultRecordingAddOnResultPayload:
        """Fetch an instance of a result payload

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording AddOnResult Payload resource to fetch.
            reference_sid: The SID of the recording to which the AddOnResult resource that contains the payload to fetch
                belongs.
            add_on_result_sid: The SID of the AddOnResult to which the payload to fetch belongs.
            sid: The Twilio-provided string that uniquely identifies the Recording AddOnResult Payload resource to
                fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_recording_add_on_result_payload(
                account_sid, reference_sid, add_on_result_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def list_recording_add_on_result_payload(
        self,
        account_sid: str,
        reference_sid: str,
        add_on_result_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListRecordingAddOnResultPayloadResponse:
        """Retrieve a list of payloads belonging to the AddOnResult

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording AddOnResult Payload resources to read.
            reference_sid: The SID of the recording to which the AddOnResult resource that contains the payloads to read
                belongs.
            add_on_result_sid: The SID of the AddOnResult to which the payloads to read belongs.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_recording_add_on_result_payload(
                account_sid,
                reference_sid,
                add_on_result_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401PayloadWithRawResponse:
        return self._with_raw_response


class Api20100401PayloadWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_recording_add_on_result_payload(
        self,
        account_sid: str,
        reference_sid: str,
        add_on_result_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Delete a payload from the result along with all associated Data

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording AddOnResult Payload resources to delete.
            reference_sid: The SID of the recording to which the AddOnResult resource that contains the payloads to
                delete belongs.
            add_on_result_sid: The SID of the AddOnResult to which the payloads to delete belongs.
            sid: The Twilio-provided string that uniquely identifies the Recording AddOnResult Payload resource to
                delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults/{AddOnResultSid}/Payloads/{Sid}.json",
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("ReferenceSid", reference_sid),
                param[str]("AddOnResultSid", add_on_result_sid),
                param[str]("Sid", sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_recording_add_on_result_payload(
        self,
        account_sid: str,
        reference_sid: str,
        add_on_result_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountRecordingRecordingAddOnResultRecordingAddOnResultPayload, RawError]:
        """Fetch an instance of a result payload

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording AddOnResult Payload resource to fetch.
            reference_sid: The SID of the recording to which the AddOnResult resource that contains the payload to fetch
                belongs.
            add_on_result_sid: The SID of the AddOnResult to which the payload to fetch belongs.
            sid: The Twilio-provided string that uniquely identifies the Recording AddOnResult Payload resource to
                fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults/{AddOnResultSid}/Payloads/{Sid}.json",
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("ReferenceSid", reference_sid),
                param[str]("AddOnResultSid", add_on_result_sid),
                param[str]("Sid", sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountRecordingRecordingAddOnResultRecordingAddOnResultPayload],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_recording_add_on_result_payload(
        self,
        account_sid: str,
        reference_sid: str,
        add_on_result_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListRecordingAddOnResultPayloadResponse, RawError]:
        """Retrieve a list of payloads belonging to the AddOnResult

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording AddOnResult Payload resources to read.
            reference_sid: The SID of the recording to which the AddOnResult resource that contains the payloads to read
                belongs.
            add_on_result_sid: The SID of the AddOnResult to which the payloads to read belongs.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults/{AddOnResultSid}/Payloads.json",
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("ReferenceSid", reference_sid),
                param[str]("AddOnResultSid", add_on_result_sid),
            ],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListRecordingAddOnResultPayloadResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401PayloadWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_recording_add_on_result_payload(
        self,
        account_sid: str,
        reference_sid: str,
        add_on_result_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Delete a payload from the result along with all associated Data

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording AddOnResult Payload resources to delete.
            reference_sid: The SID of the recording to which the AddOnResult resource that contains the payloads to
                delete belongs.
            add_on_result_sid: The SID of the AddOnResult to which the payloads to delete belongs.
            sid: The Twilio-provided string that uniquely identifies the Recording AddOnResult Payload resource to
                delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults/{AddOnResultSid}/Payloads/{Sid}.json",
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("ReferenceSid", reference_sid),
                param[str]("AddOnResultSid", add_on_result_sid),
                param[str]("Sid", sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_recording_add_on_result_payload(
        self,
        account_sid: str,
        reference_sid: str,
        add_on_result_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountRecordingRecordingAddOnResultRecordingAddOnResultPayload, RawError]:
        """Fetch an instance of a result payload

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording AddOnResult Payload resource to fetch.
            reference_sid: The SID of the recording to which the AddOnResult resource that contains the payload to fetch
                belongs.
            add_on_result_sid: The SID of the AddOnResult to which the payload to fetch belongs.
            sid: The Twilio-provided string that uniquely identifies the Recording AddOnResult Payload resource to
                fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults/{AddOnResultSid}/Payloads/{Sid}.json",
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("ReferenceSid", reference_sid),
                param[str]("AddOnResultSid", add_on_result_sid),
                param[str]("Sid", sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountRecordingRecordingAddOnResultRecordingAddOnResultPayload],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_recording_add_on_result_payload(
        self,
        account_sid: str,
        reference_sid: str,
        add_on_result_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListRecordingAddOnResultPayloadResponse, RawError]:
        """Retrieve a list of payloads belonging to the AddOnResult

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording AddOnResult Payload resources to read.
            reference_sid: The SID of the recording to which the AddOnResult resource that contains the payloads to read
                belongs.
            add_on_result_sid: The SID of the AddOnResult to which the payloads to read belongs.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults/{AddOnResultSid}/Payloads.json",
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("ReferenceSid", reference_sid),
                param[str]("AddOnResultSid", add_on_result_sid),
            ],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListRecordingAddOnResultPayloadResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
