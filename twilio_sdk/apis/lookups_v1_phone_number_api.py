from __future__ import annotations

from typing import Any

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
from ..models.lookups_v1_phone_number import LookupsV1PhoneNumber
from ..server.server import Server


class LookupsV1PhoneNumberApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = LookupsV1PhoneNumberApiWithRawResponse(client, server, auth)

    def fetch_phone_number2(
        self,
        phone_number: str,
        *,
        country_code: str | None = None,
        type_: list[str] | None = None,
        add_ons: list[str] | None = None,
        add_ons_data: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> LookupsV1PhoneNumber:
        """Detailed information on phone numbers

        Args:
            phone_number: The phone number to lookup in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__
                format, which consists of a + followed by the country code and subscriber number.
            country_code: The `ISO country code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ of the phone
                number to fetch. This is used to specify the country when the phone number is provided in a national
                format.
            type_: The type of information to return. Can be: ``carrier`` or ``caller-name``. The default is null. To
                retrieve both types of information, specify this parameter twice; once with ``carrier`` and once with
                ``caller-name`` as the value.
            add_ons: The ``unique_name`` of an Add-on you would like to invoke. Can be the ``unique_name`` of an Add-on
                that is installed on your account. You can specify multiple instances of this parameter to invoke
                multiple Add-ons. For more information about Add-ons, see the `Add-ons documentation
                <https://www.twilio.com/docs/add-ons>`__.
            add_ons_data: Data specific to the add-on you would like to invoke. The content and format of this value
                depends on the add-on.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_phone_number2(
            phone_number,
            country_code=country_code,
            type_=type_,
            add_ons=add_ons,
            add_ons_data=add_ons_data,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> LookupsV1PhoneNumberApiWithRawResponse:
        return self._with_raw_response


class AsyncLookupsV1PhoneNumberApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncLookupsV1PhoneNumberApiWithRawResponse(client, server, auth)

    async def fetch_phone_number2(
        self,
        phone_number: str,
        *,
        country_code: str | None = None,
        type_: list[str] | None = None,
        add_ons: list[str] | None = None,
        add_ons_data: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> LookupsV1PhoneNumber:
        """Detailed information on phone numbers

        Args:
            phone_number: The phone number to lookup in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__
                format, which consists of a + followed by the country code and subscriber number.
            country_code: The `ISO country code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ of the phone
                number to fetch. This is used to specify the country when the phone number is provided in a national
                format.
            type_: The type of information to return. Can be: ``carrier`` or ``caller-name``. The default is null. To
                retrieve both types of information, specify this parameter twice; once with ``carrier`` and once with
                ``caller-name`` as the value.
            add_ons: The ``unique_name`` of an Add-on you would like to invoke. Can be the ``unique_name`` of an Add-on
                that is installed on your account. You can specify multiple instances of this parameter to invoke
                multiple Add-ons. For more information about Add-ons, see the `Add-ons documentation
                <https://www.twilio.com/docs/add-ons>`__.
            add_ons_data: Data specific to the add-on you would like to invoke. The content and format of this value
                depends on the add-on.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_phone_number2(
                phone_number,
                country_code=country_code,
                type_=type_,
                add_ons=add_ons,
                add_ons_data=add_ons_data,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncLookupsV1PhoneNumberApiWithRawResponse:
        return self._with_raw_response


class LookupsV1PhoneNumberApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_phone_number2(
        self,
        phone_number: str,
        *,
        country_code: str | None = None,
        type_: list[str] | None = None,
        add_ons: list[str] | None = None,
        add_ons_data: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[LookupsV1PhoneNumber, RawError]:
        """Detailed information on phone numbers

        Args:
            phone_number: The phone number to lookup in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__
                format, which consists of a + followed by the country code and subscriber number.
            country_code: The `ISO country code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ of the phone
                number to fetch. This is used to specify the country when the phone number is provided in a national
                format.
            type_: The type of information to return. Can be: ``carrier`` or ``caller-name``. The default is null. To
                retrieve both types of information, specify this parameter twice; once with ``carrier`` and once with
                ``caller-name`` as the value.
            add_ons: The ``unique_name`` of an Add-on you would like to invoke. Can be the ``unique_name`` of an Add-on
                that is installed on your account. You can specify multiple instances of this parameter to invoke
                multiple Add-ons. For more information about Add-ons, see the `Add-ons documentation
                <https://www.twilio.com/docs/add-ons>`__.
            add_ons_data: Data specific to the add-on you would like to invoke. The content and format of this value
                depends on the add-on.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default4("/v1/PhoneNumbers/{PhoneNumber}"),
            path_params=[param[str]("PhoneNumber", phone_number)],
            query_params=[
                param[str | None]("CountryCode", country_code),
                param[list[str] | None]("Type", type_),
                param[list[str] | None]("AddOns", add_ons),
                param[Any | None]("AddOnsData", add_ons_data),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[LookupsV1PhoneNumber],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncLookupsV1PhoneNumberApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_phone_number2(
        self,
        phone_number: str,
        *,
        country_code: str | None = None,
        type_: list[str] | None = None,
        add_ons: list[str] | None = None,
        add_ons_data: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[LookupsV1PhoneNumber, RawError]:
        """Detailed information on phone numbers

        Args:
            phone_number: The phone number to lookup in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__
                format, which consists of a + followed by the country code and subscriber number.
            country_code: The `ISO country code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ of the phone
                number to fetch. This is used to specify the country when the phone number is provided in a national
                format.
            type_: The type of information to return. Can be: ``carrier`` or ``caller-name``. The default is null. To
                retrieve both types of information, specify this parameter twice; once with ``carrier`` and once with
                ``caller-name`` as the value.
            add_ons: The ``unique_name`` of an Add-on you would like to invoke. Can be the ``unique_name`` of an Add-on
                that is installed on your account. You can specify multiple instances of this parameter to invoke
                multiple Add-ons. For more information about Add-ons, see the `Add-ons documentation
                <https://www.twilio.com/docs/add-ons>`__.
            add_ons_data: Data specific to the add-on you would like to invoke. The content and format of this value
                depends on the add-on.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default4("/v1/PhoneNumbers/{PhoneNumber}"),
            path_params=[param[str]("PhoneNumber", phone_number)],
            query_params=[
                param[str | None]("CountryCode", country_code),
                param[list[str] | None]("Type", type_),
                param[list[str] | None]("AddOns", add_ons),
                param[Any | None]("AddOnsData", add_ons_data),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[LookupsV1PhoneNumber],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
