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
    param,
    raw_error_response,
)
from ..server.server import Server


class Api20100401Data:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401DataWithRawResponse(client, server, auth)

    def fetch_recording_add_on_result_payload_data(
        self,
        account_sid: str,
        reference_sid: str,
        add_on_result_sid: str,
        payload_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Fetch an instance of a result payload

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording AddOnResult Payload resource to fetch.
            reference_sid: The SID of the recording to which the AddOnResult resource that contains the payload to fetch
                belongs.
            add_on_result_sid: The SID of the AddOnResult to which the payload to fetch belongs.
            payload_sid: The Twilio-provided string that uniquely identifies the Recording AddOnResult Payload resource
                to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_recording_add_on_result_payload_data(
            account_sid, reference_sid, add_on_result_sid, payload_sid, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401DataWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401Data:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401DataWithRawResponse(client, server, auth)

    async def fetch_recording_add_on_result_payload_data(
        self,
        account_sid: str,
        reference_sid: str,
        add_on_result_sid: str,
        payload_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Fetch an instance of a result payload

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording AddOnResult Payload resource to fetch.
            reference_sid: The SID of the recording to which the AddOnResult resource that contains the payload to fetch
                belongs.
            add_on_result_sid: The SID of the AddOnResult to which the payload to fetch belongs.
            payload_sid: The Twilio-provided string that uniquely identifies the Recording AddOnResult Payload resource
                to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_recording_add_on_result_payload_data(
                account_sid, reference_sid, add_on_result_sid, payload_sid, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401DataWithRawResponse:
        return self._with_raw_response


class Api20100401DataWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_recording_add_on_result_payload_data(
        self,
        account_sid: str,
        reference_sid: str,
        add_on_result_sid: str,
        payload_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Fetch an instance of a result payload

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording AddOnResult Payload resource to fetch.
            reference_sid: The SID of the recording to which the AddOnResult resource that contains the payload to fetch
                belongs.
            add_on_result_sid: The SID of the AddOnResult to which the payload to fetch belongs.
            payload_sid: The Twilio-provided string that uniquely identifies the Recording AddOnResult Payload resource
                to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults/{AddOnResultSid}/Payloads/{PayloadSid}/Data.json",
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("ReferenceSid", reference_sid),
                param[str]("AddOnResultSid", add_on_result_sid),
                param[str]("PayloadSid", payload_sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401DataWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_recording_add_on_result_payload_data(
        self,
        account_sid: str,
        reference_sid: str,
        add_on_result_sid: str,
        payload_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Fetch an instance of a result payload

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Recording AddOnResult Payload resource to fetch.
            reference_sid: The SID of the recording to which the AddOnResult resource that contains the payload to fetch
                belongs.
            add_on_result_sid: The SID of the AddOnResult to which the payload to fetch belongs.
            payload_sid: The Twilio-provided string that uniquely identifies the Recording AddOnResult Payload resource
                to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults/{AddOnResultSid}/Payloads/{PayloadSid}/Data.json",
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("ReferenceSid", reference_sid),
                param[str]("AddOnResultSid", add_on_result_sid),
                param[str]("PayloadSid", payload_sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )
