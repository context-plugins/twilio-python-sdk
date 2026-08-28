from __future__ import annotations

from pydantic import AnyUrl

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
from ..models.messaging_v1_domain_config import MessagingV1DomainConfig
from ..server.server import Server


class MessagingV1DomainConfigApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MessagingV1DomainConfigApiWithRawResponse(client, server, auth)

    def fetch_domain_config(
        self, domain_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MessagingV1DomainConfig:
        """Send a ``GET`` request.

        Args:
            domain_sid: Unique string used to identify the domain that this config should be associated with.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_domain_config(domain_sid, request_options=request_options).unwrap()

    def update_domain_config(
        self,
        domain_sid: str,
        *,
        fallback_url: AnyUrl | None = None,
        callback_url: AnyUrl | None = None,
        continue_on_failure: bool | None = None,
        disable_https: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MessagingV1DomainConfig:
        """Send a ``POST`` request.

        Args:
            domain_sid: Unique string used to identify the domain that this config should be associated with.
            fallback_url: Any requests we receive to this domain that do not match an existing shortened message will be
                redirected to the fallback url. These will likely be either expired messages, random misdirected
                traffic, or intentional scraping.
            callback_url: URL to receive click events to your webhook whenever the recipients click on the shortened
                links
            continue_on_failure: Boolean field to set customer delivery preference when there is a failure in
                linkShortening service
            disable_https: Customer's choice to send links with/without "https://" attached to shortened url. If true,
                messages will not be sent with https:// at the beginning of the url. If false, messages will be sent
                with https:// at the beginning of the url. False is the default behavior if it is not specified.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_domain_config(
            domain_sid,
            fallback_url=fallback_url,
            callback_url=callback_url,
            continue_on_failure=continue_on_failure,
            disable_https=disable_https,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> MessagingV1DomainConfigApiWithRawResponse:
        return self._with_raw_response


class AsyncMessagingV1DomainConfigApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMessagingV1DomainConfigApiWithRawResponse(client, server, auth)

    async def fetch_domain_config(
        self, domain_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MessagingV1DomainConfig:
        """Send a ``GET`` request.

        Args:
            domain_sid: Unique string used to identify the domain that this config should be associated with.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_domain_config(domain_sid, request_options=request_options)).unwrap()

    async def update_domain_config(
        self,
        domain_sid: str,
        *,
        fallback_url: AnyUrl | None = None,
        callback_url: AnyUrl | None = None,
        continue_on_failure: bool | None = None,
        disable_https: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MessagingV1DomainConfig:
        """Send a ``POST`` request.

        Args:
            domain_sid: Unique string used to identify the domain that this config should be associated with.
            fallback_url: Any requests we receive to this domain that do not match an existing shortened message will be
                redirected to the fallback url. These will likely be either expired messages, random misdirected
                traffic, or intentional scraping.
            callback_url: URL to receive click events to your webhook whenever the recipients click on the shortened
                links
            continue_on_failure: Boolean field to set customer delivery preference when there is a failure in
                linkShortening service
            disable_https: Customer's choice to send links with/without "https://" attached to shortened url. If true,
                messages will not be sent with https:// at the beginning of the url. If false, messages will be sent
                with https:// at the beginning of the url. False is the default behavior if it is not specified.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_domain_config(
                domain_sid,
                fallback_url=fallback_url,
                callback_url=callback_url,
                continue_on_failure=continue_on_failure,
                disable_https=disable_https,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncMessagingV1DomainConfigApiWithRawResponse:
        return self._with_raw_response


class MessagingV1DomainConfigApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_domain_config(
        self, domain_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV1DomainConfig, RawError]:
        """Send a ``GET`` request.

        Args:
            domain_sid: Unique string used to identify the domain that this config should be associated with.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/LinkShortening/Domains/{DomainSid}/Config"),
            path_params=[param[str]("DomainSid", domain_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1DomainConfig],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_domain_config(
        self,
        domain_sid: str,
        *,
        fallback_url: AnyUrl | None = None,
        callback_url: AnyUrl | None = None,
        continue_on_failure: bool | None = None,
        disable_https: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MessagingV1DomainConfig, RawError]:
        """Send a ``POST`` request.

        Args:
            domain_sid: Unique string used to identify the domain that this config should be associated with.
            fallback_url: Any requests we receive to this domain that do not match an existing shortened message will be
                redirected to the fallback url. These will likely be either expired messages, random misdirected
                traffic, or intentional scraping.
            callback_url: URL to receive click events to your webhook whenever the recipients click on the shortened
                links
            continue_on_failure: Boolean field to set customer delivery preference when there is a failure in
                linkShortening service
            disable_https: Customer's choice to send links with/without "https://" attached to shortened url. If true,
                messages will not be sent with https:// at the beginning of the url. If false, messages will be sent
                with https:// at the beginning of the url. False is the default behavior if it is not specified.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v1/LinkShortening/Domains/{DomainSid}/Config"),
            path_params=[param[str]("DomainSid", domain_sid)],
            body=form_body(
                [
                    param[AnyUrl | None]("FallbackUrl", fallback_url),
                    param[AnyUrl | None]("CallbackUrl", callback_url),
                    param[bool | None]("ContinueOnFailure", continue_on_failure),
                    param[bool | None]("DisableHttps", disable_https),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1DomainConfig],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncMessagingV1DomainConfigApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_domain_config(
        self, domain_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV1DomainConfig, RawError]:
        """Send a ``GET`` request.

        Args:
            domain_sid: Unique string used to identify the domain that this config should be associated with.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/LinkShortening/Domains/{DomainSid}/Config"),
            path_params=[param[str]("DomainSid", domain_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1DomainConfig],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_domain_config(
        self,
        domain_sid: str,
        *,
        fallback_url: AnyUrl | None = None,
        callback_url: AnyUrl | None = None,
        continue_on_failure: bool | None = None,
        disable_https: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MessagingV1DomainConfig, RawError]:
        """Send a ``POST`` request.

        Args:
            domain_sid: Unique string used to identify the domain that this config should be associated with.
            fallback_url: Any requests we receive to this domain that do not match an existing shortened message will be
                redirected to the fallback url. These will likely be either expired messages, random misdirected
                traffic, or intentional scraping.
            callback_url: URL to receive click events to your webhook whenever the recipients click on the shortened
                links
            continue_on_failure: Boolean field to set customer delivery preference when there is a failure in
                linkShortening service
            disable_https: Customer's choice to send links with/without "https://" attached to shortened url. If true,
                messages will not be sent with https:// at the beginning of the url. If false, messages will be sent
                with https:// at the beginning of the url. False is the default behavior if it is not specified.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v1/LinkShortening/Domains/{DomainSid}/Config"),
            path_params=[param[str]("DomainSid", domain_sid)],
            body=form_body(
                [
                    param[AnyUrl | None]("FallbackUrl", fallback_url),
                    param[AnyUrl | None]("CallbackUrl", callback_url),
                    param[bool | None]("ContinueOnFailure", continue_on_failure),
                    param[bool | None]("DisableHttps", disable_https),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1DomainConfig],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
