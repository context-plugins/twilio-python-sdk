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
from ..models.insights_v1_account_settings import InsightsV1AccountSettings
from ..server.server import Server


class InsightsV1Setting:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = InsightsV1SettingWithRawResponse(client, server, auth)

    def fetch_account_settings(
        self, *, subaccount_sid: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> InsightsV1AccountSettings:
        """Get the Voice Insights Settings.

        Args:
            subaccount_sid: The unique SID identifier of the Subaccount.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_account_settings(
            subaccount_sid=subaccount_sid, request_options=request_options
        ).unwrap()

    def update_account_settings(
        self,
        *,
        advanced_features: bool | None = None,
        voice_trace: bool | None = None,
        subaccount_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> InsightsV1AccountSettings:
        """Update a specific Voice Insights Setting.

        Args:
            advanced_features: A boolean flag to enable Advanced Features for Voice Insights.
            voice_trace: A boolean flag to enable Voice Trace.
            subaccount_sid: The unique SID identifier of the Subaccount.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_account_settings(
            advanced_features=advanced_features,
            voice_trace=voice_trace,
            subaccount_sid=subaccount_sid,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> InsightsV1SettingWithRawResponse:
        return self._with_raw_response


class AsyncInsightsV1Setting:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncInsightsV1SettingWithRawResponse(client, server, auth)

    async def fetch_account_settings(
        self, *, subaccount_sid: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> InsightsV1AccountSettings:
        """Get the Voice Insights Settings.

        Args:
            subaccount_sid: The unique SID identifier of the Subaccount.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_account_settings(
                subaccount_sid=subaccount_sid, request_options=request_options
            )
        ).unwrap()

    async def update_account_settings(
        self,
        *,
        advanced_features: bool | None = None,
        voice_trace: bool | None = None,
        subaccount_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> InsightsV1AccountSettings:
        """Update a specific Voice Insights Setting.

        Args:
            advanced_features: A boolean flag to enable Advanced Features for Voice Insights.
            voice_trace: A boolean flag to enable Voice Trace.
            subaccount_sid: The unique SID identifier of the Subaccount.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_account_settings(
                advanced_features=advanced_features,
                voice_trace=voice_trace,
                subaccount_sid=subaccount_sid,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncInsightsV1SettingWithRawResponse:
        return self._with_raw_response


class InsightsV1SettingWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_account_settings(
        self, *, subaccount_sid: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InsightsV1AccountSettings, RawError]:
        """Get the Voice Insights Settings.

        Args:
            subaccount_sid: The unique SID identifier of the Subaccount.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/v1/Voice/Settings"),
            query_params=[param[str | None]("SubaccountSid", subaccount_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[InsightsV1AccountSettings],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_account_settings(
        self,
        *,
        advanced_features: bool | None = None,
        voice_trace: bool | None = None,
        subaccount_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[InsightsV1AccountSettings, RawError]:
        """Update a specific Voice Insights Setting.

        Args:
            advanced_features: A boolean flag to enable Advanced Features for Voice Insights.
            voice_trace: A boolean flag to enable Voice Trace.
            subaccount_sid: The unique SID identifier of the Subaccount.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default14("/v1/Voice/Settings"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[bool | None]("AdvancedFeatures", advanced_features),
                    param[bool | None]("VoiceTrace", voice_trace),
                    param[str | None]("SubaccountSid", subaccount_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[InsightsV1AccountSettings],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncInsightsV1SettingWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_account_settings(
        self, *, subaccount_sid: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InsightsV1AccountSettings, RawError]:
        """Get the Voice Insights Settings.

        Args:
            subaccount_sid: The unique SID identifier of the Subaccount.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/v1/Voice/Settings"),
            query_params=[param[str | None]("SubaccountSid", subaccount_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[InsightsV1AccountSettings],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_account_settings(
        self,
        *,
        advanced_features: bool | None = None,
        voice_trace: bool | None = None,
        subaccount_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[InsightsV1AccountSettings, RawError]:
        """Update a specific Voice Insights Setting.

        Args:
            advanced_features: A boolean flag to enable Advanced Features for Voice Insights.
            voice_trace: A boolean flag to enable Voice Trace.
            subaccount_sid: The unique SID identifier of the Subaccount.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default14("/v1/Voice/Settings"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[bool | None]("AdvancedFeatures", advanced_features),
                    param[bool | None]("VoiceTrace", voice_trace),
                    param[str | None]("SubaccountSid", subaccount_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[InsightsV1AccountSettings],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
