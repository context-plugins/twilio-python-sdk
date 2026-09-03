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
from ..models.api_v2010_account_short_code import ApiV2010AccountShortCode
from ..models.enums.sms_fallback_method14 import SmsFallbackMethod14OrStr
from ..models.enums.sms_method14 import SmsMethod14OrStr
from ..models.list_short_code_response import ListShortCodeResponse
from ..server.server import Server


class Api20100401ShortCode:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401ShortCodeWithRawResponse(client, server, auth)

    def fetch_short_code(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountShortCode:
        """Fetch an instance of a short code

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                ShortCode resource(s) to fetch.
            sid: The Twilio-provided string that uniquely identifies the ShortCode resource to fetch
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_short_code(account_sid, sid, request_options=request_options).unwrap()

    def list_short_code(
        self,
        account_sid: str,
        *,
        friendly_name: str | None = None,
        short_code: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListShortCodeResponse:
        """Retrieve a list of short-codes belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                ShortCode resource(s) to read.
            friendly_name: The string that identifies the ShortCode resources to read.
            short_code: Only show the ShortCode resources that match this pattern. You can specify partial numbers and
                use '*' as a wildcard for any digit.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_short_code(
            account_sid,
            friendly_name=friendly_name,
            short_code=short_code,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_short_code(
        self,
        account_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        api_version: str | None = None,
        sms_url: str | None = None,
        sms_method: SmsMethod14OrStr | None = None,
        sms_fallback_url: str | None = None,
        sms_fallback_method: SmsFallbackMethod14OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountShortCode:
        """Update a short code with the following parameters

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                ShortCode resource(s) to update.
            sid: The Twilio-provided string that uniquely identifies the ShortCode resource to update
            friendly_name: A descriptive string that you created to describe this resource. It can be up to 64
                characters long. By default, the ``FriendlyName`` is the short code.
            api_version: The API version to use to start a new TwiML session. Can be: ``2010-04-01`` or ``2008-08-01``.
            sms_url: The URL we should call when receiving an incoming SMS message to this short code.
            sms_method: The HTTP method we should use when calling the ``sms_url``. Can be: ``GET`` or ``POST``.
            sms_fallback_url: The URL that we should call if an error occurs while retrieving or executing the TwiML
                from ``sms_url``.
            sms_fallback_method: The HTTP method that we should use to call the ``sms_fallback_url``. Can be: ``GET`` or
                ``POST``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_short_code(
            account_sid,
            sid,
            friendly_name=friendly_name,
            api_version=api_version,
            sms_url=sms_url,
            sms_method=sms_method,
            sms_fallback_url=sms_fallback_url,
            sms_fallback_method=sms_fallback_method,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401ShortCodeWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401ShortCode:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401ShortCodeWithRawResponse(client, server, auth)

    async def fetch_short_code(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountShortCode:
        """Fetch an instance of a short code

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                ShortCode resource(s) to fetch.
            sid: The Twilio-provided string that uniquely identifies the ShortCode resource to fetch
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_short_code(account_sid, sid, request_options=request_options)
        ).unwrap()

    async def list_short_code(
        self,
        account_sid: str,
        *,
        friendly_name: str | None = None,
        short_code: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListShortCodeResponse:
        """Retrieve a list of short-codes belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                ShortCode resource(s) to read.
            friendly_name: The string that identifies the ShortCode resources to read.
            short_code: Only show the ShortCode resources that match this pattern. You can specify partial numbers and
                use '*' as a wildcard for any digit.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_short_code(
                account_sid,
                friendly_name=friendly_name,
                short_code=short_code,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_short_code(
        self,
        account_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        api_version: str | None = None,
        sms_url: str | None = None,
        sms_method: SmsMethod14OrStr | None = None,
        sms_fallback_url: str | None = None,
        sms_fallback_method: SmsFallbackMethod14OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountShortCode:
        """Update a short code with the following parameters

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                ShortCode resource(s) to update.
            sid: The Twilio-provided string that uniquely identifies the ShortCode resource to update
            friendly_name: A descriptive string that you created to describe this resource. It can be up to 64
                characters long. By default, the ``FriendlyName`` is the short code.
            api_version: The API version to use to start a new TwiML session. Can be: ``2010-04-01`` or ``2008-08-01``.
            sms_url: The URL we should call when receiving an incoming SMS message to this short code.
            sms_method: The HTTP method we should use when calling the ``sms_url``. Can be: ``GET`` or ``POST``.
            sms_fallback_url: The URL that we should call if an error occurs while retrieving or executing the TwiML
                from ``sms_url``.
            sms_fallback_method: The HTTP method that we should use to call the ``sms_fallback_url``. Can be: ``GET`` or
                ``POST``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_short_code(
                account_sid,
                sid,
                friendly_name=friendly_name,
                api_version=api_version,
                sms_url=sms_url,
                sms_method=sms_method,
                sms_fallback_url=sms_fallback_url,
                sms_fallback_method=sms_fallback_method,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401ShortCodeWithRawResponse:
        return self._with_raw_response


class Api20100401ShortCodeWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_short_code(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountShortCode, RawError]:
        """Fetch an instance of a short code

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                ShortCode resource(s) to fetch.
            sid: The Twilio-provided string that uniquely identifies the ShortCode resource to fetch
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/SMS/ShortCodes/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountShortCode],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_short_code(
        self,
        account_sid: str,
        *,
        friendly_name: str | None = None,
        short_code: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListShortCodeResponse, RawError]:
        """Retrieve a list of short-codes belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                ShortCode resource(s) to read.
            friendly_name: The string that identifies the ShortCode resources to read.
            short_code: Only show the ShortCode resources that match this pattern. You can specify partial numbers and
                use '*' as a wildcard for any digit.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/SMS/ShortCodes.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            query_params=[
                param[str | None]("FriendlyName", friendly_name),
                param[str | None]("ShortCode", short_code),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListShortCodeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_short_code(
        self,
        account_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        api_version: str | None = None,
        sms_url: str | None = None,
        sms_method: SmsMethod14OrStr | None = None,
        sms_fallback_url: str | None = None,
        sms_fallback_method: SmsFallbackMethod14OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountShortCode, RawError]:
        """Update a short code with the following parameters

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                ShortCode resource(s) to update.
            sid: The Twilio-provided string that uniquely identifies the ShortCode resource to update
            friendly_name: A descriptive string that you created to describe this resource. It can be up to 64
                characters long. By default, the ``FriendlyName`` is the short code.
            api_version: The API version to use to start a new TwiML session. Can be: ``2010-04-01`` or ``2008-08-01``.
            sms_url: The URL we should call when receiving an incoming SMS message to this short code.
            sms_method: The HTTP method we should use when calling the ``sms_url``. Can be: ``GET`` or ``POST``.
            sms_fallback_url: The URL that we should call if an error occurs while retrieving or executing the TwiML
                from ``sms_url``.
            sms_fallback_method: The HTTP method that we should use to call the ``sms_fallback_url``. Can be: ``GET`` or
                ``POST``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/SMS/ShortCodes/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("ApiVersion", api_version),
                    param[str | None]("SmsUrl", sms_url),
                    param[SmsMethod14OrStr | None]("SmsMethod", sms_method),
                    param[str | None]("SmsFallbackUrl", sms_fallback_url),
                    param[SmsFallbackMethod14OrStr | None]("SmsFallbackMethod", sms_fallback_method),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountShortCode],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401ShortCodeWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_short_code(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountShortCode, RawError]:
        """Fetch an instance of a short code

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                ShortCode resource(s) to fetch.
            sid: The Twilio-provided string that uniquely identifies the ShortCode resource to fetch
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/SMS/ShortCodes/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountShortCode],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_short_code(
        self,
        account_sid: str,
        *,
        friendly_name: str | None = None,
        short_code: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListShortCodeResponse, RawError]:
        """Retrieve a list of short-codes belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                ShortCode resource(s) to read.
            friendly_name: The string that identifies the ShortCode resources to read.
            short_code: Only show the ShortCode resources that match this pattern. You can specify partial numbers and
                use '*' as a wildcard for any digit.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/SMS/ShortCodes.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            query_params=[
                param[str | None]("FriendlyName", friendly_name),
                param[str | None]("ShortCode", short_code),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListShortCodeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_short_code(
        self,
        account_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        api_version: str | None = None,
        sms_url: str | None = None,
        sms_method: SmsMethod14OrStr | None = None,
        sms_fallback_url: str | None = None,
        sms_fallback_method: SmsFallbackMethod14OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountShortCode, RawError]:
        """Update a short code with the following parameters

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                ShortCode resource(s) to update.
            sid: The Twilio-provided string that uniquely identifies the ShortCode resource to update
            friendly_name: A descriptive string that you created to describe this resource. It can be up to 64
                characters long. By default, the ``FriendlyName`` is the short code.
            api_version: The API version to use to start a new TwiML session. Can be: ``2010-04-01`` or ``2008-08-01``.
            sms_url: The URL we should call when receiving an incoming SMS message to this short code.
            sms_method: The HTTP method we should use when calling the ``sms_url``. Can be: ``GET`` or ``POST``.
            sms_fallback_url: The URL that we should call if an error occurs while retrieving or executing the TwiML
                from ``sms_url``.
            sms_fallback_method: The HTTP method that we should use to call the ``sms_fallback_url``. Can be: ``GET`` or
                ``POST``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/SMS/ShortCodes/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("ApiVersion", api_version),
                    param[str | None]("SmsUrl", sms_url),
                    param[SmsMethod14OrStr | None]("SmsMethod", sms_method),
                    param[str | None]("SmsFallbackUrl", sms_fallback_url),
                    param[SmsFallbackMethod14OrStr | None]("SmsFallbackMethod", sms_fallback_method),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountShortCode],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
