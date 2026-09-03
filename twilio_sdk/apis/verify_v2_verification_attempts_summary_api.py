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
from ..models.enums.verification_attempts_summary_enum_channels import VerificationAttemptsSummaryEnumChannelsOrStr
from ..models.verify_v2_verification_attempts_summary import VerifyV2VerificationAttemptsSummary
from ..server.server import Server


class VerifyV2VerificationAttemptsSummaryApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VerifyV2VerificationAttemptsSummaryApiWithRawResponse(client, server, auth)

    def fetch_verification_attempts_summary(
        self,
        *,
        verify_service_sid: str | None = None,
        date_created_after: RFC3339DateTime | None = None,
        date_created_before: RFC3339DateTime | None = None,
        country: str | None = None,
        channel: VerificationAttemptsSummaryEnumChannelsOrStr | None = None,
        destination_prefix: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VerifyV2VerificationAttemptsSummary:
        """Get a summary of how many attempts were made and how many were converted.

        Args:
            verify_service_sid: Filter used to consider only Verification Attempts of the given verify service on the
                summary aggregation.
            date_created_after: Datetime filter used to consider only Verification Attempts created after this datetime
                on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd'T'HH:mm:ss'Z.
            date_created_before: Datetime filter used to consider only Verification Attempts created before this
                datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string:
                yyyy-MM-dd'T'HH:mm:ss'Z.
            country: Filter used to consider only Verification Attempts sent to the specified destination country on the
                summary aggregation.
            channel: Filter Verification Attempts considered on the summary aggregation by communication channel.
            destination_prefix: Filter the Verification Attempts considered on the summary aggregation by Destination
                prefix. It is the prefix of a phone number in E.164 format.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_verification_attempts_summary(
            verify_service_sid=verify_service_sid,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            country=country,
            channel=channel,
            destination_prefix=destination_prefix,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> VerifyV2VerificationAttemptsSummaryApiWithRawResponse:
        return self._with_raw_response


class AsyncVerifyV2VerificationAttemptsSummaryApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVerifyV2VerificationAttemptsSummaryApiWithRawResponse(client, server, auth)

    async def fetch_verification_attempts_summary(
        self,
        *,
        verify_service_sid: str | None = None,
        date_created_after: RFC3339DateTime | None = None,
        date_created_before: RFC3339DateTime | None = None,
        country: str | None = None,
        channel: VerificationAttemptsSummaryEnumChannelsOrStr | None = None,
        destination_prefix: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VerifyV2VerificationAttemptsSummary:
        """Get a summary of how many attempts were made and how many were converted.

        Args:
            verify_service_sid: Filter used to consider only Verification Attempts of the given verify service on the
                summary aggregation.
            date_created_after: Datetime filter used to consider only Verification Attempts created after this datetime
                on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd'T'HH:mm:ss'Z.
            date_created_before: Datetime filter used to consider only Verification Attempts created before this
                datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string:
                yyyy-MM-dd'T'HH:mm:ss'Z.
            country: Filter used to consider only Verification Attempts sent to the specified destination country on the
                summary aggregation.
            channel: Filter Verification Attempts considered on the summary aggregation by communication channel.
            destination_prefix: Filter the Verification Attempts considered on the summary aggregation by Destination
                prefix. It is the prefix of a phone number in E.164 format.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_verification_attempts_summary(
                verify_service_sid=verify_service_sid,
                date_created_after=date_created_after,
                date_created_before=date_created_before,
                country=country,
                channel=channel,
                destination_prefix=destination_prefix,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVerifyV2VerificationAttemptsSummaryApiWithRawResponse:
        return self._with_raw_response


class VerifyV2VerificationAttemptsSummaryApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_verification_attempts_summary(
        self,
        *,
        verify_service_sid: str | None = None,
        date_created_after: RFC3339DateTime | None = None,
        date_created_before: RFC3339DateTime | None = None,
        country: str | None = None,
        channel: VerificationAttemptsSummaryEnumChannelsOrStr | None = None,
        destination_prefix: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VerifyV2VerificationAttemptsSummary, RawError]:
        """Get a summary of how many attempts were made and how many were converted.

        Args:
            verify_service_sid: Filter used to consider only Verification Attempts of the given verify service on the
                summary aggregation.
            date_created_after: Datetime filter used to consider only Verification Attempts created after this datetime
                on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd'T'HH:mm:ss'Z.
            date_created_before: Datetime filter used to consider only Verification Attempts created before this
                datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string:
                yyyy-MM-dd'T'HH:mm:ss'Z.
            country: Filter used to consider only Verification Attempts sent to the specified destination country on the
                summary aggregation.
            channel: Filter Verification Attempts considered on the summary aggregation by communication channel.
            destination_prefix: Filter the Verification Attempts considered on the summary aggregation by Destination
                prefix. It is the prefix of a phone number in E.164 format.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default3("/v2/Attempts/Summary"),
            query_params=[
                param[str | None]("VerifyServiceSid", verify_service_sid),
                param[RFC3339DateTime | None]("DateCreatedAfter", date_created_after),
                param[RFC3339DateTime | None]("DateCreatedBefore", date_created_before),
                param[str | None]("Country", country),
                param[VerificationAttemptsSummaryEnumChannelsOrStr | None]("Channel", channel),
                param[str | None]("DestinationPrefix", destination_prefix),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2VerificationAttemptsSummary],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncVerifyV2VerificationAttemptsSummaryApiWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def fetch_verification_attempts_summary(
        self,
        *,
        verify_service_sid: str | None = None,
        date_created_after: RFC3339DateTime | None = None,
        date_created_before: RFC3339DateTime | None = None,
        country: str | None = None,
        channel: VerificationAttemptsSummaryEnumChannelsOrStr | None = None,
        destination_prefix: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VerifyV2VerificationAttemptsSummary, RawError]:
        """Get a summary of how many attempts were made and how many were converted.

        Args:
            verify_service_sid: Filter used to consider only Verification Attempts of the given verify service on the
                summary aggregation.
            date_created_after: Datetime filter used to consider only Verification Attempts created after this datetime
                on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd'T'HH:mm:ss'Z.
            date_created_before: Datetime filter used to consider only Verification Attempts created before this
                datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string:
                yyyy-MM-dd'T'HH:mm:ss'Z.
            country: Filter used to consider only Verification Attempts sent to the specified destination country on the
                summary aggregation.
            channel: Filter Verification Attempts considered on the summary aggregation by communication channel.
            destination_prefix: Filter the Verification Attempts considered on the summary aggregation by Destination
                prefix. It is the prefix of a phone number in E.164 format.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default3("/v2/Attempts/Summary"),
            query_params=[
                param[str | None]("VerifyServiceSid", verify_service_sid),
                param[RFC3339DateTime | None]("DateCreatedAfter", date_created_after),
                param[RFC3339DateTime | None]("DateCreatedBefore", date_created_before),
                param[str | None]("Country", country),
                param[VerificationAttemptsSummaryEnumChannelsOrStr | None]("Channel", channel),
                param[str | None]("DestinationPrefix", destination_prefix),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2VerificationAttemptsSummary],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
