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
from ..models.api_v2010_account_new_key import ApiV2010AccountNewKey
from ..server.server import Server


class Api20100401NewKey:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401NewKeyWithRawResponse(client, server, auth)

    def create_new_key(
        self, account_sid: str, *, friendly_name: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountNewKey:
        """API keys

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will be
                responsible for the new Key resource.
            friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters
                long.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_new_key(
            account_sid, friendly_name=friendly_name, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401NewKeyWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401NewKey:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401NewKeyWithRawResponse(client, server, auth)

    async def create_new_key(
        self, account_sid: str, *, friendly_name: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountNewKey:
        """API keys

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will be
                responsible for the new Key resource.
            friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters
                long.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_new_key(
                account_sid, friendly_name=friendly_name, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401NewKeyWithRawResponse:
        return self._with_raw_response


class Api20100401NewKeyWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_new_key(
        self, account_sid: str, *, friendly_name: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountNewKey, RawError]:
        """API keys

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will be
                responsible for the new Key resource.
            friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters
                long.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Keys.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str | None]("FriendlyName", friendly_name)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountNewKey],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401NewKeyWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_new_key(
        self, account_sid: str, *, friendly_name: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountNewKey, RawError]:
        """API keys

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will be
                responsible for the new Key resource.
            friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters
                long.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Keys.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str | None]("FriendlyName", friendly_name)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountNewKey],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
