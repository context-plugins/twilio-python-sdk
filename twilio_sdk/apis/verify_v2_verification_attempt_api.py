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
    json_decoder,
    param,
    raw_error_response,
)
from ..models.enums.verification_attempt_enum_channels import VerificationAttemptEnumChannelsOrStr
from ..models.enums.verification_attempt_enum_conversion_status import VerificationAttemptEnumConversionStatusOrStr
from ..models.list_verification_attempt_response import ListVerificationAttemptResponse
from ..models.verify_v2_verification_attempt import VerifyV2VerificationAttempt
from ..server.server import Server


class VerifyV2VerificationAttemptApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VerifyV2VerificationAttemptApiWithRawResponse(client, server, auth)

    def fetch_verification_attempt(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VerifyV2VerificationAttempt:
        """Fetch a specific verification attempt.

        Args:
            sid: The unique SID identifier of a Verification Attempt
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_verification_attempt(sid, request_options=request_options).unwrap()

    def list_verification_attempt(
        self,
        *,
        date_created_after: RFC3339DateTime | None = None,
        date_created_before: RFC3339DateTime | None = None,
        channel_data_to: str | None = None,
        country: str | None = None,
        channel: VerificationAttemptEnumChannelsOrStr | None = None,
        verify_service_sid: str | None = None,
        verification_sid: str | None = None,
        status: VerificationAttemptEnumConversionStatusOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListVerificationAttemptResponse:
        """List all the verification attempts for a given Account.

        Args:
            date_created_after: Datetime filter used to consider only Verification Attempts created after this datetime
                on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd'T'HH:mm:ss'Z.
            date_created_before: Datetime filter used to consider only Verification Attempts created before this
                datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string:
                yyyy-MM-dd'T'HH:mm:ss'Z.
            channel_data_to: Destination of a verification. It is phone number in E.164 format.
            country: Filter used to query Verification Attempts sent to the specified destination country.
            channel: Filter used to query Verification Attempts by communication channel.
            verify_service_sid: Filter used to query Verification Attempts by verify service. Only attempts of the
                provided SID will be returned.
            verification_sid: Filter used to return all the Verification Attempts of a single verification. Only
                attempts of the provided verification SID will be returned.
            status: Filter used to query Verification Attempts by conversion status. Valid values are ``UNCONVERTED``,
                for attempts that were not converted, and ``CONVERTED``, for attempts that were confirmed.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_verification_attempt(
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            channel_data_to=channel_data_to,
            country=country,
            channel=channel,
            verify_service_sid=verify_service_sid,
            verification_sid=verification_sid,
            status=status,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> VerifyV2VerificationAttemptApiWithRawResponse:
        return self._with_raw_response


class AsyncVerifyV2VerificationAttemptApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVerifyV2VerificationAttemptApiWithRawResponse(client, server, auth)

    async def fetch_verification_attempt(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VerifyV2VerificationAttempt:
        """Fetch a specific verification attempt.

        Args:
            sid: The unique SID identifier of a Verification Attempt
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_verification_attempt(sid, request_options=request_options)).unwrap()

    async def list_verification_attempt(
        self,
        *,
        date_created_after: RFC3339DateTime | None = None,
        date_created_before: RFC3339DateTime | None = None,
        channel_data_to: str | None = None,
        country: str | None = None,
        channel: VerificationAttemptEnumChannelsOrStr | None = None,
        verify_service_sid: str | None = None,
        verification_sid: str | None = None,
        status: VerificationAttemptEnumConversionStatusOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListVerificationAttemptResponse:
        """List all the verification attempts for a given Account.

        Args:
            date_created_after: Datetime filter used to consider only Verification Attempts created after this datetime
                on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd'T'HH:mm:ss'Z.
            date_created_before: Datetime filter used to consider only Verification Attempts created before this
                datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string:
                yyyy-MM-dd'T'HH:mm:ss'Z.
            channel_data_to: Destination of a verification. It is phone number in E.164 format.
            country: Filter used to query Verification Attempts sent to the specified destination country.
            channel: Filter used to query Verification Attempts by communication channel.
            verify_service_sid: Filter used to query Verification Attempts by verify service. Only attempts of the
                provided SID will be returned.
            verification_sid: Filter used to return all the Verification Attempts of a single verification. Only
                attempts of the provided verification SID will be returned.
            status: Filter used to query Verification Attempts by conversion status. Valid values are ``UNCONVERTED``,
                for attempts that were not converted, and ``CONVERTED``, for attempts that were confirmed.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_verification_attempt(
                date_created_after=date_created_after,
                date_created_before=date_created_before,
                channel_data_to=channel_data_to,
                country=country,
                channel=channel,
                verify_service_sid=verify_service_sid,
                verification_sid=verification_sid,
                status=status,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVerifyV2VerificationAttemptApiWithRawResponse:
        return self._with_raw_response


class VerifyV2VerificationAttemptApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_verification_attempt(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VerifyV2VerificationAttempt, RawError]:
        """Fetch a specific verification attempt.

        Args:
            sid: The unique SID identifier of a Verification Attempt
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default3("/v2/Attempts/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2VerificationAttempt],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_verification_attempt(
        self,
        *,
        date_created_after: RFC3339DateTime | None = None,
        date_created_before: RFC3339DateTime | None = None,
        channel_data_to: str | None = None,
        country: str | None = None,
        channel: VerificationAttemptEnumChannelsOrStr | None = None,
        verify_service_sid: str | None = None,
        verification_sid: str | None = None,
        status: VerificationAttemptEnumConversionStatusOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListVerificationAttemptResponse, RawError]:
        """List all the verification attempts for a given Account.

        Args:
            date_created_after: Datetime filter used to consider only Verification Attempts created after this datetime
                on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd'T'HH:mm:ss'Z.
            date_created_before: Datetime filter used to consider only Verification Attempts created before this
                datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string:
                yyyy-MM-dd'T'HH:mm:ss'Z.
            channel_data_to: Destination of a verification. It is phone number in E.164 format.
            country: Filter used to query Verification Attempts sent to the specified destination country.
            channel: Filter used to query Verification Attempts by communication channel.
            verify_service_sid: Filter used to query Verification Attempts by verify service. Only attempts of the
                provided SID will be returned.
            verification_sid: Filter used to return all the Verification Attempts of a single verification. Only
                attempts of the provided verification SID will be returned.
            status: Filter used to query Verification Attempts by conversion status. Valid values are ``UNCONVERTED``,
                for attempts that were not converted, and ``CONVERTED``, for attempts that were confirmed.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default3("/v2/Attempts"),
            query_params=[
                param[RFC3339DateTime | None]("DateCreatedAfter", date_created_after),
                param[RFC3339DateTime | None]("DateCreatedBefore", date_created_before),
                param[str | None]("ChannelData.To", channel_data_to),
                param[str | None]("Country", country),
                param[VerificationAttemptEnumChannelsOrStr | None]("Channel", channel),
                param[str | None]("VerifyServiceSid", verify_service_sid),
                param[str | None]("VerificationSid", verification_sid),
                param[VerificationAttemptEnumConversionStatusOrStr | None]("Status", status),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListVerificationAttemptResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncVerifyV2VerificationAttemptApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_verification_attempt(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VerifyV2VerificationAttempt, RawError]:
        """Fetch a specific verification attempt.

        Args:
            sid: The unique SID identifier of a Verification Attempt
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default3("/v2/Attempts/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2VerificationAttempt],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_verification_attempt(
        self,
        *,
        date_created_after: RFC3339DateTime | None = None,
        date_created_before: RFC3339DateTime | None = None,
        channel_data_to: str | None = None,
        country: str | None = None,
        channel: VerificationAttemptEnumChannelsOrStr | None = None,
        verify_service_sid: str | None = None,
        verification_sid: str | None = None,
        status: VerificationAttemptEnumConversionStatusOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListVerificationAttemptResponse, RawError]:
        """List all the verification attempts for a given Account.

        Args:
            date_created_after: Datetime filter used to consider only Verification Attempts created after this datetime
                on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd'T'HH:mm:ss'Z.
            date_created_before: Datetime filter used to consider only Verification Attempts created before this
                datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string:
                yyyy-MM-dd'T'HH:mm:ss'Z.
            channel_data_to: Destination of a verification. It is phone number in E.164 format.
            country: Filter used to query Verification Attempts sent to the specified destination country.
            channel: Filter used to query Verification Attempts by communication channel.
            verify_service_sid: Filter used to query Verification Attempts by verify service. Only attempts of the
                provided SID will be returned.
            verification_sid: Filter used to return all the Verification Attempts of a single verification. Only
                attempts of the provided verification SID will be returned.
            status: Filter used to query Verification Attempts by conversion status. Valid values are ``UNCONVERTED``,
                for attempts that were not converted, and ``CONVERTED``, for attempts that were confirmed.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default3("/v2/Attempts"),
            query_params=[
                param[RFC3339DateTime | None]("DateCreatedAfter", date_created_after),
                param[RFC3339DateTime | None]("DateCreatedBefore", date_created_before),
                param[str | None]("ChannelData.To", channel_data_to),
                param[str | None]("Country", country),
                param[VerificationAttemptEnumChannelsOrStr | None]("Channel", channel),
                param[str | None]("VerifyServiceSid", verify_service_sid),
                param[str | None]("VerificationSid", verification_sid),
                param[VerificationAttemptEnumConversionStatusOrStr | None]("Status", status),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListVerificationAttemptResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
