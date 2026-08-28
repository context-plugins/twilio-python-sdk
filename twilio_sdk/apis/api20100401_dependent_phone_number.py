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
from ..models.list_dependent_phone_number_response import ListDependentPhoneNumberResponse
from ..server.server import Server


class Api20100401DependentPhoneNumber:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401DependentPhoneNumberWithRawResponse(client, server, auth)

    def list_dependent_phone_number(
        self,
        account_sid: str,
        address_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListDependentPhoneNumberResponse:
        """Phone numbers dependent on an Address resource

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                DependentPhoneNumber resources to read.
            address_sid: The SID of the Address resource associated with the phone number.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_dependent_phone_number(
            account_sid,
            address_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401DependentPhoneNumberWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401DependentPhoneNumber:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401DependentPhoneNumberWithRawResponse(client, server, auth)

    async def list_dependent_phone_number(
        self,
        account_sid: str,
        address_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListDependentPhoneNumberResponse:
        """Phone numbers dependent on an Address resource

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                DependentPhoneNumber resources to read.
            address_sid: The SID of the Address resource associated with the phone number.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_dependent_phone_number(
                account_sid,
                address_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401DependentPhoneNumberWithRawResponse:
        return self._with_raw_response


class Api20100401DependentPhoneNumberWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def list_dependent_phone_number(
        self,
        account_sid: str,
        address_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListDependentPhoneNumberResponse, RawError]:
        """Phone numbers dependent on an Address resource

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                DependentPhoneNumber resources to read.
            address_sid: The SID of the Address resource associated with the phone number.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Addresses/{AddressSid}/DependentPhoneNumbers.json"
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("AddressSid", address_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListDependentPhoneNumberResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401DependentPhoneNumberWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def list_dependent_phone_number(
        self,
        account_sid: str,
        address_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListDependentPhoneNumberResponse, RawError]:
        """Phone numbers dependent on an Address resource

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                DependentPhoneNumber resources to read.
            address_sid: The SID of the Address resource associated with the phone number.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Addresses/{AddressSid}/DependentPhoneNumbers.json"
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("AddressSid", address_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListDependentPhoneNumberResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
