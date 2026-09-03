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
    empty_response,
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.api_v2010_account_address import ApiV2010AccountAddress
from ..models.list_address_response import ListAddressResponse
from ..server.server import Server


class Api20100401Address:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401AddressWithRawResponse(client, server, auth)

    def create_address(
        self,
        account_sid: str,
        customer_name: str,
        street: str,
        city: str,
        region: str,
        postal_code: str,
        iso_country: str,
        *,
        friendly_name: str | None = None,
        emergency_enabled: bool | None = None,
        auto_correct_address: bool | None = None,
        street_secondary: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountAddress:
        """An Address instance resource represents your or your customer's physical location within a country. Around
        the world, some local authorities require the name and address of the user to be on file with Twilio to purchase
        and own a phone number.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will be
                responsible for the new Address resource.
            customer_name: The name to associate with the new address.
            street: The number and street address of the new address.
            city: The city of the new address.
            region: The state or region of the new address.
            postal_code: The postal code of the new address.
            iso_country: The ISO country code of the new address.
            friendly_name: A descriptive string that you create to describe the new address. It can be up to 64
                characters long for Regulatory Compliance addresses and 32 characters long for Emergency addresses.
            emergency_enabled: Whether to enable emergency calling on the new address. Can be: ``true`` or ``false``.
            auto_correct_address: Whether we should automatically correct the address. Can be: ``true`` or ``false`` and
                the default is ``true``. If empty or ``true``, we will correct the address you provide if necessary. If
                ``false``, we won't alter the address you provide.
            street_secondary: The additional number and street address of the address.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_address(
            account_sid,
            customer_name,
            street,
            city,
            region,
            postal_code,
            iso_country,
            friendly_name=friendly_name,
            emergency_enabled=emergency_enabled,
            auto_correct_address=auto_correct_address,
            street_secondary=street_secondary,
            request_options=request_options,
        ).unwrap()

    def delete_address(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """An Address instance resource represents your or your customer's physical location within a country. Around
        the world, some local authorities require the name and address of the user to be on file with Twilio to purchase
        and own a phone number.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that is responsible
                for the Address resource to delete.
            sid: The Twilio-provided string that uniquely identifies the Address resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_address(account_sid, sid, request_options=request_options).unwrap()

    def fetch_address(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountAddress:
        """An Address instance resource represents your or your customer's physical location within a country. Around
        the world, some local authorities require the name and address of the user to be on file with Twilio to purchase
        and own a phone number.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that is responsible
                for the Address resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the Address resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_address(account_sid, sid, request_options=request_options).unwrap()

    def list_address(
        self,
        account_sid: str,
        *,
        customer_name: str | None = None,
        friendly_name: str | None = None,
        emergency_enabled: bool | None = None,
        iso_country: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListAddressResponse:
        """An Address instance resource represents your or your customer's physical location within a country. Around
        the world, some local authorities require the name and address of the user to be on file with Twilio to purchase
        and own a phone number.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that is responsible
                for the Address resource to read.
            customer_name: The ``customer_name`` of the Address resources to read.
            friendly_name: The string that identifies the Address resources to read.
            emergency_enabled: Whether the address can be associated to a number for emergency calling.
            iso_country: The ISO country code of the Address resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_address(
            account_sid,
            customer_name=customer_name,
            friendly_name=friendly_name,
            emergency_enabled=emergency_enabled,
            iso_country=iso_country,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_address(
        self,
        account_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        customer_name: str | None = None,
        street: str | None = None,
        city: str | None = None,
        region: str | None = None,
        postal_code: str | None = None,
        emergency_enabled: bool | None = None,
        auto_correct_address: bool | None = None,
        street_secondary: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountAddress:
        """An Address instance resource represents your or your customer's physical location within a country. Around
        the world, some local authorities require the name and address of the user to be on file with Twilio to purchase
        and own a phone number.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that is responsible
                for the Address resource to update.
            sid: The Twilio-provided string that uniquely identifies the Address resource to update.
            friendly_name: A descriptive string that you create to describe the new address. It can be up to 64
                characters long for Regulatory Compliance addresses and 32 characters long for Emergency addresses.
            customer_name: The name to associate with the address.
            street: The number and street address of the address.
            city: The city of the address.
            region: The state or region of the address.
            postal_code: The postal code of the address.
            emergency_enabled: Whether to enable emergency calling on the address. Can be: ``true`` or ``false``.
            auto_correct_address: Whether we should automatically correct the address. Can be: ``true`` or ``false`` and
                the default is ``true``. If empty or ``true``, we will correct the address you provide if necessary. If
                ``false``, we won't alter the address you provide.
            street_secondary: The additional number and street address of the address.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_address(
            account_sid,
            sid,
            friendly_name=friendly_name,
            customer_name=customer_name,
            street=street,
            city=city,
            region=region,
            postal_code=postal_code,
            emergency_enabled=emergency_enabled,
            auto_correct_address=auto_correct_address,
            street_secondary=street_secondary,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401AddressWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401Address:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401AddressWithRawResponse(client, server, auth)

    async def create_address(
        self,
        account_sid: str,
        customer_name: str,
        street: str,
        city: str,
        region: str,
        postal_code: str,
        iso_country: str,
        *,
        friendly_name: str | None = None,
        emergency_enabled: bool | None = None,
        auto_correct_address: bool | None = None,
        street_secondary: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountAddress:
        """An Address instance resource represents your or your customer's physical location within a country. Around
        the world, some local authorities require the name and address of the user to be on file with Twilio to purchase
        and own a phone number.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will be
                responsible for the new Address resource.
            customer_name: The name to associate with the new address.
            street: The number and street address of the new address.
            city: The city of the new address.
            region: The state or region of the new address.
            postal_code: The postal code of the new address.
            iso_country: The ISO country code of the new address.
            friendly_name: A descriptive string that you create to describe the new address. It can be up to 64
                characters long for Regulatory Compliance addresses and 32 characters long for Emergency addresses.
            emergency_enabled: Whether to enable emergency calling on the new address. Can be: ``true`` or ``false``.
            auto_correct_address: Whether we should automatically correct the address. Can be: ``true`` or ``false`` and
                the default is ``true``. If empty or ``true``, we will correct the address you provide if necessary. If
                ``false``, we won't alter the address you provide.
            street_secondary: The additional number and street address of the address.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_address(
                account_sid,
                customer_name,
                street,
                city,
                region,
                postal_code,
                iso_country,
                friendly_name=friendly_name,
                emergency_enabled=emergency_enabled,
                auto_correct_address=auto_correct_address,
                street_secondary=street_secondary,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_address(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """An Address instance resource represents your or your customer's physical location within a country. Around
        the world, some local authorities require the name and address of the user to be on file with Twilio to purchase
        and own a phone number.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that is responsible
                for the Address resource to delete.
            sid: The Twilio-provided string that uniquely identifies the Address resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_address(account_sid, sid, request_options=request_options)
        ).unwrap()

    async def fetch_address(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountAddress:
        """An Address instance resource represents your or your customer's physical location within a country. Around
        the world, some local authorities require the name and address of the user to be on file with Twilio to purchase
        and own a phone number.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that is responsible
                for the Address resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the Address resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_address(account_sid, sid, request_options=request_options)).unwrap()

    async def list_address(
        self,
        account_sid: str,
        *,
        customer_name: str | None = None,
        friendly_name: str | None = None,
        emergency_enabled: bool | None = None,
        iso_country: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListAddressResponse:
        """An Address instance resource represents your or your customer's physical location within a country. Around
        the world, some local authorities require the name and address of the user to be on file with Twilio to purchase
        and own a phone number.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that is responsible
                for the Address resource to read.
            customer_name: The ``customer_name`` of the Address resources to read.
            friendly_name: The string that identifies the Address resources to read.
            emergency_enabled: Whether the address can be associated to a number for emergency calling.
            iso_country: The ISO country code of the Address resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_address(
                account_sid,
                customer_name=customer_name,
                friendly_name=friendly_name,
                emergency_enabled=emergency_enabled,
                iso_country=iso_country,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_address(
        self,
        account_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        customer_name: str | None = None,
        street: str | None = None,
        city: str | None = None,
        region: str | None = None,
        postal_code: str | None = None,
        emergency_enabled: bool | None = None,
        auto_correct_address: bool | None = None,
        street_secondary: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountAddress:
        """An Address instance resource represents your or your customer's physical location within a country. Around
        the world, some local authorities require the name and address of the user to be on file with Twilio to purchase
        and own a phone number.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that is responsible
                for the Address resource to update.
            sid: The Twilio-provided string that uniquely identifies the Address resource to update.
            friendly_name: A descriptive string that you create to describe the new address. It can be up to 64
                characters long for Regulatory Compliance addresses and 32 characters long for Emergency addresses.
            customer_name: The name to associate with the address.
            street: The number and street address of the address.
            city: The city of the address.
            region: The state or region of the address.
            postal_code: The postal code of the address.
            emergency_enabled: Whether to enable emergency calling on the address. Can be: ``true`` or ``false``.
            auto_correct_address: Whether we should automatically correct the address. Can be: ``true`` or ``false`` and
                the default is ``true``. If empty or ``true``, we will correct the address you provide if necessary. If
                ``false``, we won't alter the address you provide.
            street_secondary: The additional number and street address of the address.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_address(
                account_sid,
                sid,
                friendly_name=friendly_name,
                customer_name=customer_name,
                street=street,
                city=city,
                region=region,
                postal_code=postal_code,
                emergency_enabled=emergency_enabled,
                auto_correct_address=auto_correct_address,
                street_secondary=street_secondary,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401AddressWithRawResponse:
        return self._with_raw_response


class Api20100401AddressWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_address(
        self,
        account_sid: str,
        customer_name: str,
        street: str,
        city: str,
        region: str,
        postal_code: str,
        iso_country: str,
        *,
        friendly_name: str | None = None,
        emergency_enabled: bool | None = None,
        auto_correct_address: bool | None = None,
        street_secondary: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountAddress, RawError]:
        """An Address instance resource represents your or your customer's physical location within a country. Around
        the world, some local authorities require the name and address of the user to be on file with Twilio to purchase
        and own a phone number.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will be
                responsible for the new Address resource.
            customer_name: The name to associate with the new address.
            street: The number and street address of the new address.
            city: The city of the new address.
            region: The state or region of the new address.
            postal_code: The postal code of the new address.
            iso_country: The ISO country code of the new address.
            friendly_name: A descriptive string that you create to describe the new address. It can be up to 64
                characters long for Regulatory Compliance addresses and 32 characters long for Emergency addresses.
            emergency_enabled: Whether to enable emergency calling on the new address. Can be: ``true`` or ``false``.
            auto_correct_address: Whether we should automatically correct the address. Can be: ``true`` or ``false`` and
                the default is ``true``. If empty or ``true``, we will correct the address you provide if necessary. If
                ``false``, we won't alter the address you provide.
            street_secondary: The additional number and street address of the address.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Addresses.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("CustomerName", customer_name),
                    param[str]("Street", street),
                    param[str]("City", city),
                    param[str]("Region", region),
                    param[str]("PostalCode", postal_code),
                    param[str]("IsoCountry", iso_country),
                    param[str | None]("FriendlyName", friendly_name),
                    param[bool | None]("EmergencyEnabled", emergency_enabled),
                    param[bool | None]("AutoCorrectAddress", auto_correct_address),
                    param[str | None]("StreetSecondary", street_secondary),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountAddress],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_address(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """An Address instance resource represents your or your customer's physical location within a country. Around
        the world, some local authorities require the name and address of the user to be on file with Twilio to purchase
        and own a phone number.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that is responsible
                for the Address resource to delete.
            sid: The Twilio-provided string that uniquely identifies the Address resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Addresses/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_address(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountAddress, RawError]:
        """An Address instance resource represents your or your customer's physical location within a country. Around
        the world, some local authorities require the name and address of the user to be on file with Twilio to purchase
        and own a phone number.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that is responsible
                for the Address resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the Address resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Addresses/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountAddress],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_address(
        self,
        account_sid: str,
        *,
        customer_name: str | None = None,
        friendly_name: str | None = None,
        emergency_enabled: bool | None = None,
        iso_country: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListAddressResponse, RawError]:
        """An Address instance resource represents your or your customer's physical location within a country. Around
        the world, some local authorities require the name and address of the user to be on file with Twilio to purchase
        and own a phone number.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that is responsible
                for the Address resource to read.
            customer_name: The ``customer_name`` of the Address resources to read.
            friendly_name: The string that identifies the Address resources to read.
            emergency_enabled: Whether the address can be associated to a number for emergency calling.
            iso_country: The ISO country code of the Address resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Addresses.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            query_params=[
                param[str | None]("CustomerName", customer_name),
                param[str | None]("FriendlyName", friendly_name),
                param[bool | None]("EmergencyEnabled", emergency_enabled),
                param[str | None]("IsoCountry", iso_country),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListAddressResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_address(
        self,
        account_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        customer_name: str | None = None,
        street: str | None = None,
        city: str | None = None,
        region: str | None = None,
        postal_code: str | None = None,
        emergency_enabled: bool | None = None,
        auto_correct_address: bool | None = None,
        street_secondary: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountAddress, RawError]:
        """An Address instance resource represents your or your customer's physical location within a country. Around
        the world, some local authorities require the name and address of the user to be on file with Twilio to purchase
        and own a phone number.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that is responsible
                for the Address resource to update.
            sid: The Twilio-provided string that uniquely identifies the Address resource to update.
            friendly_name: A descriptive string that you create to describe the new address. It can be up to 64
                characters long for Regulatory Compliance addresses and 32 characters long for Emergency addresses.
            customer_name: The name to associate with the address.
            street: The number and street address of the address.
            city: The city of the address.
            region: The state or region of the address.
            postal_code: The postal code of the address.
            emergency_enabled: Whether to enable emergency calling on the address. Can be: ``true`` or ``false``.
            auto_correct_address: Whether we should automatically correct the address. Can be: ``true`` or ``false`` and
                the default is ``true``. If empty or ``true``, we will correct the address you provide if necessary. If
                ``false``, we won't alter the address you provide.
            street_secondary: The additional number and street address of the address.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Addresses/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("CustomerName", customer_name),
                    param[str | None]("Street", street),
                    param[str | None]("City", city),
                    param[str | None]("Region", region),
                    param[str | None]("PostalCode", postal_code),
                    param[bool | None]("EmergencyEnabled", emergency_enabled),
                    param[bool | None]("AutoCorrectAddress", auto_correct_address),
                    param[str | None]("StreetSecondary", street_secondary),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountAddress],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401AddressWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_address(
        self,
        account_sid: str,
        customer_name: str,
        street: str,
        city: str,
        region: str,
        postal_code: str,
        iso_country: str,
        *,
        friendly_name: str | None = None,
        emergency_enabled: bool | None = None,
        auto_correct_address: bool | None = None,
        street_secondary: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountAddress, RawError]:
        """An Address instance resource represents your or your customer's physical location within a country. Around
        the world, some local authorities require the name and address of the user to be on file with Twilio to purchase
        and own a phone number.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will be
                responsible for the new Address resource.
            customer_name: The name to associate with the new address.
            street: The number and street address of the new address.
            city: The city of the new address.
            region: The state or region of the new address.
            postal_code: The postal code of the new address.
            iso_country: The ISO country code of the new address.
            friendly_name: A descriptive string that you create to describe the new address. It can be up to 64
                characters long for Regulatory Compliance addresses and 32 characters long for Emergency addresses.
            emergency_enabled: Whether to enable emergency calling on the new address. Can be: ``true`` or ``false``.
            auto_correct_address: Whether we should automatically correct the address. Can be: ``true`` or ``false`` and
                the default is ``true``. If empty or ``true``, we will correct the address you provide if necessary. If
                ``false``, we won't alter the address you provide.
            street_secondary: The additional number and street address of the address.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Addresses.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("CustomerName", customer_name),
                    param[str]("Street", street),
                    param[str]("City", city),
                    param[str]("Region", region),
                    param[str]("PostalCode", postal_code),
                    param[str]("IsoCountry", iso_country),
                    param[str | None]("FriendlyName", friendly_name),
                    param[bool | None]("EmergencyEnabled", emergency_enabled),
                    param[bool | None]("AutoCorrectAddress", auto_correct_address),
                    param[str | None]("StreetSecondary", street_secondary),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountAddress],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_address(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """An Address instance resource represents your or your customer's physical location within a country. Around
        the world, some local authorities require the name and address of the user to be on file with Twilio to purchase
        and own a phone number.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that is responsible
                for the Address resource to delete.
            sid: The Twilio-provided string that uniquely identifies the Address resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Addresses/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_address(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountAddress, RawError]:
        """An Address instance resource represents your or your customer's physical location within a country. Around
        the world, some local authorities require the name and address of the user to be on file with Twilio to purchase
        and own a phone number.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that is responsible
                for the Address resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the Address resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Addresses/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountAddress],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_address(
        self,
        account_sid: str,
        *,
        customer_name: str | None = None,
        friendly_name: str | None = None,
        emergency_enabled: bool | None = None,
        iso_country: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListAddressResponse, RawError]:
        """An Address instance resource represents your or your customer's physical location within a country. Around
        the world, some local authorities require the name and address of the user to be on file with Twilio to purchase
        and own a phone number.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that is responsible
                for the Address resource to read.
            customer_name: The ``customer_name`` of the Address resources to read.
            friendly_name: The string that identifies the Address resources to read.
            emergency_enabled: Whether the address can be associated to a number for emergency calling.
            iso_country: The ISO country code of the Address resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Addresses.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            query_params=[
                param[str | None]("CustomerName", customer_name),
                param[str | None]("FriendlyName", friendly_name),
                param[bool | None]("EmergencyEnabled", emergency_enabled),
                param[str | None]("IsoCountry", iso_country),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListAddressResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_address(
        self,
        account_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        customer_name: str | None = None,
        street: str | None = None,
        city: str | None = None,
        region: str | None = None,
        postal_code: str | None = None,
        emergency_enabled: bool | None = None,
        auto_correct_address: bool | None = None,
        street_secondary: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountAddress, RawError]:
        """An Address instance resource represents your or your customer's physical location within a country. Around
        the world, some local authorities require the name and address of the user to be on file with Twilio to purchase
        and own a phone number.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that is responsible
                for the Address resource to update.
            sid: The Twilio-provided string that uniquely identifies the Address resource to update.
            friendly_name: A descriptive string that you create to describe the new address. It can be up to 64
                characters long for Regulatory Compliance addresses and 32 characters long for Emergency addresses.
            customer_name: The name to associate with the address.
            street: The number and street address of the address.
            city: The city of the address.
            region: The state or region of the address.
            postal_code: The postal code of the address.
            emergency_enabled: Whether to enable emergency calling on the address. Can be: ``true`` or ``false``.
            auto_correct_address: Whether we should automatically correct the address. Can be: ``true`` or ``false`` and
                the default is ``true``. If empty or ``true``, we will correct the address you provide if necessary. If
                ``false``, we won't alter the address you provide.
            street_secondary: The additional number and street address of the address.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Addresses/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("CustomerName", customer_name),
                    param[str | None]("Street", street),
                    param[str | None]("City", city),
                    param[str | None]("Region", region),
                    param[str | None]("PostalCode", postal_code),
                    param[bool | None]("EmergencyEnabled", emergency_enabled),
                    param[bool | None]("AutoCorrectAddress", auto_correct_address),
                    param[str | None]("StreetSecondary", street_secondary),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountAddress],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
