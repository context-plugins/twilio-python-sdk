from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.api_v2010_account_available_phone_number_country import ApiV2010AccountAvailablePhoneNumberCountry
from ..models.list_available_phone_number_country_response import ListAvailablePhoneNumberCountryResponse
from ..server.server import Server


class Api20100401AvailablePhoneNumberCountry:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401AvailablePhoneNumberCountryWithRawResponse(client, server, auth)

    def fetch_available_phone_number_country(
        self, account_sid: str, country_code: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountAvailablePhoneNumberCountry:
        """Country codes with available phone numbers

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ requesting the
                available phone number Country resource.
            country_code: The `ISO-3166-1 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code of the
                country to fetch available phone number information about.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_available_phone_number_country(
            account_sid, country_code, request_options=request_options
        ).unwrap()

    def list_available_phone_number_country(
        self,
        account_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListAvailablePhoneNumberCountryResponse:
        """Country codes with available phone numbers

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ requesting the
                available phone number Country resources.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_available_phone_number_country(
            account_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401AvailablePhoneNumberCountryWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401AvailablePhoneNumberCountry:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401AvailablePhoneNumberCountryWithRawResponse(client, server, auth)

    async def fetch_available_phone_number_country(
        self, account_sid: str, country_code: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountAvailablePhoneNumberCountry:
        """Country codes with available phone numbers

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ requesting the
                available phone number Country resource.
            country_code: The `ISO-3166-1 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code of the
                country to fetch available phone number information about.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_available_phone_number_country(
                account_sid, country_code, request_options=request_options
            )
        ).unwrap()

    async def list_available_phone_number_country(
        self,
        account_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListAvailablePhoneNumberCountryResponse:
        """Country codes with available phone numbers

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ requesting the
                available phone number Country resources.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_available_phone_number_country(
                account_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401AvailablePhoneNumberCountryWithRawResponse:
        return self._with_raw_response


class Api20100401AvailablePhoneNumberCountryWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_available_phone_number_country(
        self, account_sid: str, country_code: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountAvailablePhoneNumberCountry, RawError]:
        """Country codes with available phone numbers

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ requesting the
                available phone number Country resource.
            country_code: The `ISO-3166-1 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code of the
                country to fetch available phone number information about.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers/{CountryCode}.json"
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("CountryCode", country_code)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountAvailablePhoneNumberCountry],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_available_phone_number_country(
        self,
        account_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListAvailablePhoneNumberCountryResponse, RawError]:
        """Country codes with available phone numbers

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ requesting the
                available phone number Country resources.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListAvailablePhoneNumberCountryResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401AvailablePhoneNumberCountryWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def fetch_available_phone_number_country(
        self, account_sid: str, country_code: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountAvailablePhoneNumberCountry, RawError]:
        """Country codes with available phone numbers

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ requesting the
                available phone number Country resource.
            country_code: The `ISO-3166-1 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code of the
                country to fetch available phone number information about.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers/{CountryCode}.json"
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("CountryCode", country_code)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountAvailablePhoneNumberCountry],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_available_phone_number_country(
        self,
        account_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListAvailablePhoneNumberCountryResponse, RawError]:
        """Country codes with available phone numbers

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ requesting the
                available phone number Country resources.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListAvailablePhoneNumberCountryResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
