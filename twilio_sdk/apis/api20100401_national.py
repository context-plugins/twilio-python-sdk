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
from ..models.list_available_phone_number_national_response import ListAvailablePhoneNumberNationalResponse
from ..server.server import Server


class Api20100401National:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401NationalWithRawResponse(client, server, auth)

    def list_available_phone_number_national(
        self,
        account_sid: str,
        country_code: str,
        *,
        area_code: int | None = None,
        contains: str | None = None,
        sms_enabled: bool | None = None,
        mms_enabled: bool | None = None,
        voice_enabled: bool | None = None,
        exclude_all_address_required: bool | None = None,
        exclude_local_address_required: bool | None = None,
        exclude_foreign_address_required: bool | None = None,
        beta: bool | None = None,
        near_number: str | None = None,
        near_lat_long: str | None = None,
        distance: int | None = None,
        in_postal_code: str | None = None,
        in_region: str | None = None,
        in_rate_center: str | None = None,
        in_lata: str | None = None,
        in_locality: str | None = None,
        fax_enabled: bool | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListAvailablePhoneNumberNationalResponse:
        """Available national phone numbers

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ requesting the
                AvailablePhoneNumber resources.
            country_code: The `ISO-3166-1 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code of the
                country from which to read phone numbers.
            area_code: The area code of the phone numbers to read. Applies to only phone numbers in the US and Canada.
            contains: Matching pattern to identify phone numbers. This pattern can be between 2 and 16 characters long
                and allows all digits (0-9) and all non-diacritic latin alphabet letters (a-z, A-Z). It accepts four
                meta-characters: ``*``, ``%``, ``+``, ``$``. The ``*`` and ``%`` meta-characters can appear multiple
                times in the pattern. To match wildcards at the beginning or end of the pattern, use ``*`` to match any
                single character or ``%`` to match a sequence of characters. If you use the wildcard patterns, it must
                include at least two non-meta-characters, and wildcards cannot be used between non-meta-characters. To
                match the beginning of a pattern, start the pattern with ``+``. To match the end of the pattern, append
                the pattern with ``$``. These meta-characters can't be adjacent to each other.
            sms_enabled: Whether the phone numbers can receive text messages. Can be: ``true`` or ``false``.
            mms_enabled: Whether the phone numbers can receive MMS messages. Can be: ``true`` or ``false``.
            voice_enabled: Whether the phone numbers can receive calls. Can be: ``true`` or ``false``.
            exclude_all_address_required: Whether to exclude phone numbers that require an `Address
                <https://www.twilio.com/docs/usage/api/address>`__. Can be: ``true`` or ``false`` and the default is
                ``false``.
            exclude_local_address_required: Whether to exclude phone numbers that require a local `Address
                <https://www.twilio.com/docs/usage/api/address>`__. Can be: ``true`` or ``false`` and the default is
                ``false``.
            exclude_foreign_address_required: Whether to exclude phone numbers that require a foreign `Address
                <https://www.twilio.com/docs/usage/api/address>`__. Can be: ``true`` or ``false`` and the default is
                ``false``.
            beta: Whether to read phone numbers that are new to the Twilio platform. Can be: ``true`` or ``false`` and
                the default is ``true``.
            near_number: Given a phone number, find a geographically close number within ``distance`` miles. Distance
                defaults to 25 miles. Applies to only phone numbers in the US and Canada.
            near_lat_long: Given a latitude/longitude pair ``lat,long`` find geographically close numbers within
                ``distance`` miles. Applies to only phone numbers in the US and Canada.
            distance: The search radius, in miles, for a ``near_`` query. Can be up to ``500`` and the default is
                ``25``. Applies to only phone numbers in the US and Canada.
            in_postal_code: Limit results to a particular postal code. Given a phone number, search within the same
                postal code as that number. Applies to only phone numbers in the US and Canada.
            in_region: Limit results to a particular region, state, or province. Given a phone number, search within the
                same region as that number. Applies to only phone numbers in the US and Canada.
            in_rate_center: Limit results to a specific rate center, or given a phone number search within the same rate
                center as that number. Requires ``in_lata`` to be set as well. Applies to only phone numbers in the US
                and Canada.
            in_lata: Limit results to a specific local access and transport area (`LATA
                <https://en.wikipedia.org/wiki/Local_access_and_transport_area>`__). Given a phone number, search within
                the same `LATA <https://en.wikipedia.org/wiki/Local_access_and_transport_area>`__ as that number.
                Applies to only phone numbers in the US and Canada.
            in_locality: Limit results to a particular locality or city. Given a phone number, search within the same
                Locality as that number.
            fax_enabled: Whether the phone numbers can receive faxes. Can be: ``true`` or ``false``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_available_phone_number_national(
            account_sid,
            country_code,
            area_code=area_code,
            contains=contains,
            sms_enabled=sms_enabled,
            mms_enabled=mms_enabled,
            voice_enabled=voice_enabled,
            exclude_all_address_required=exclude_all_address_required,
            exclude_local_address_required=exclude_local_address_required,
            exclude_foreign_address_required=exclude_foreign_address_required,
            beta=beta,
            near_number=near_number,
            near_lat_long=near_lat_long,
            distance=distance,
            in_postal_code=in_postal_code,
            in_region=in_region,
            in_rate_center=in_rate_center,
            in_lata=in_lata,
            in_locality=in_locality,
            fax_enabled=fax_enabled,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401NationalWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401National:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401NationalWithRawResponse(client, server, auth)

    async def list_available_phone_number_national(
        self,
        account_sid: str,
        country_code: str,
        *,
        area_code: int | None = None,
        contains: str | None = None,
        sms_enabled: bool | None = None,
        mms_enabled: bool | None = None,
        voice_enabled: bool | None = None,
        exclude_all_address_required: bool | None = None,
        exclude_local_address_required: bool | None = None,
        exclude_foreign_address_required: bool | None = None,
        beta: bool | None = None,
        near_number: str | None = None,
        near_lat_long: str | None = None,
        distance: int | None = None,
        in_postal_code: str | None = None,
        in_region: str | None = None,
        in_rate_center: str | None = None,
        in_lata: str | None = None,
        in_locality: str | None = None,
        fax_enabled: bool | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListAvailablePhoneNumberNationalResponse:
        """Available national phone numbers

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ requesting the
                AvailablePhoneNumber resources.
            country_code: The `ISO-3166-1 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code of the
                country from which to read phone numbers.
            area_code: The area code of the phone numbers to read. Applies to only phone numbers in the US and Canada.
            contains: Matching pattern to identify phone numbers. This pattern can be between 2 and 16 characters long
                and allows all digits (0-9) and all non-diacritic latin alphabet letters (a-z, A-Z). It accepts four
                meta-characters: ``*``, ``%``, ``+``, ``$``. The ``*`` and ``%`` meta-characters can appear multiple
                times in the pattern. To match wildcards at the beginning or end of the pattern, use ``*`` to match any
                single character or ``%`` to match a sequence of characters. If you use the wildcard patterns, it must
                include at least two non-meta-characters, and wildcards cannot be used between non-meta-characters. To
                match the beginning of a pattern, start the pattern with ``+``. To match the end of the pattern, append
                the pattern with ``$``. These meta-characters can't be adjacent to each other.
            sms_enabled: Whether the phone numbers can receive text messages. Can be: ``true`` or ``false``.
            mms_enabled: Whether the phone numbers can receive MMS messages. Can be: ``true`` or ``false``.
            voice_enabled: Whether the phone numbers can receive calls. Can be: ``true`` or ``false``.
            exclude_all_address_required: Whether to exclude phone numbers that require an `Address
                <https://www.twilio.com/docs/usage/api/address>`__. Can be: ``true`` or ``false`` and the default is
                ``false``.
            exclude_local_address_required: Whether to exclude phone numbers that require a local `Address
                <https://www.twilio.com/docs/usage/api/address>`__. Can be: ``true`` or ``false`` and the default is
                ``false``.
            exclude_foreign_address_required: Whether to exclude phone numbers that require a foreign `Address
                <https://www.twilio.com/docs/usage/api/address>`__. Can be: ``true`` or ``false`` and the default is
                ``false``.
            beta: Whether to read phone numbers that are new to the Twilio platform. Can be: ``true`` or ``false`` and
                the default is ``true``.
            near_number: Given a phone number, find a geographically close number within ``distance`` miles. Distance
                defaults to 25 miles. Applies to only phone numbers in the US and Canada.
            near_lat_long: Given a latitude/longitude pair ``lat,long`` find geographically close numbers within
                ``distance`` miles. Applies to only phone numbers in the US and Canada.
            distance: The search radius, in miles, for a ``near_`` query. Can be up to ``500`` and the default is
                ``25``. Applies to only phone numbers in the US and Canada.
            in_postal_code: Limit results to a particular postal code. Given a phone number, search within the same
                postal code as that number. Applies to only phone numbers in the US and Canada.
            in_region: Limit results to a particular region, state, or province. Given a phone number, search within the
                same region as that number. Applies to only phone numbers in the US and Canada.
            in_rate_center: Limit results to a specific rate center, or given a phone number search within the same rate
                center as that number. Requires ``in_lata`` to be set as well. Applies to only phone numbers in the US
                and Canada.
            in_lata: Limit results to a specific local access and transport area (`LATA
                <https://en.wikipedia.org/wiki/Local_access_and_transport_area>`__). Given a phone number, search within
                the same `LATA <https://en.wikipedia.org/wiki/Local_access_and_transport_area>`__ as that number.
                Applies to only phone numbers in the US and Canada.
            in_locality: Limit results to a particular locality or city. Given a phone number, search within the same
                Locality as that number.
            fax_enabled: Whether the phone numbers can receive faxes. Can be: ``true`` or ``false``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_available_phone_number_national(
                account_sid,
                country_code,
                area_code=area_code,
                contains=contains,
                sms_enabled=sms_enabled,
                mms_enabled=mms_enabled,
                voice_enabled=voice_enabled,
                exclude_all_address_required=exclude_all_address_required,
                exclude_local_address_required=exclude_local_address_required,
                exclude_foreign_address_required=exclude_foreign_address_required,
                beta=beta,
                near_number=near_number,
                near_lat_long=near_lat_long,
                distance=distance,
                in_postal_code=in_postal_code,
                in_region=in_region,
                in_rate_center=in_rate_center,
                in_lata=in_lata,
                in_locality=in_locality,
                fax_enabled=fax_enabled,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401NationalWithRawResponse:
        return self._with_raw_response


class Api20100401NationalWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def list_available_phone_number_national(
        self,
        account_sid: str,
        country_code: str,
        *,
        area_code: int | None = None,
        contains: str | None = None,
        sms_enabled: bool | None = None,
        mms_enabled: bool | None = None,
        voice_enabled: bool | None = None,
        exclude_all_address_required: bool | None = None,
        exclude_local_address_required: bool | None = None,
        exclude_foreign_address_required: bool | None = None,
        beta: bool | None = None,
        near_number: str | None = None,
        near_lat_long: str | None = None,
        distance: int | None = None,
        in_postal_code: str | None = None,
        in_region: str | None = None,
        in_rate_center: str | None = None,
        in_lata: str | None = None,
        in_locality: str | None = None,
        fax_enabled: bool | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListAvailablePhoneNumberNationalResponse, RawError]:
        """Available national phone numbers

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ requesting the
                AvailablePhoneNumber resources.
            country_code: The `ISO-3166-1 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code of the
                country from which to read phone numbers.
            area_code: The area code of the phone numbers to read. Applies to only phone numbers in the US and Canada.
            contains: Matching pattern to identify phone numbers. This pattern can be between 2 and 16 characters long
                and allows all digits (0-9) and all non-diacritic latin alphabet letters (a-z, A-Z). It accepts four
                meta-characters: ``*``, ``%``, ``+``, ``$``. The ``*`` and ``%`` meta-characters can appear multiple
                times in the pattern. To match wildcards at the beginning or end of the pattern, use ``*`` to match any
                single character or ``%`` to match a sequence of characters. If you use the wildcard patterns, it must
                include at least two non-meta-characters, and wildcards cannot be used between non-meta-characters. To
                match the beginning of a pattern, start the pattern with ``+``. To match the end of the pattern, append
                the pattern with ``$``. These meta-characters can't be adjacent to each other.
            sms_enabled: Whether the phone numbers can receive text messages. Can be: ``true`` or ``false``.
            mms_enabled: Whether the phone numbers can receive MMS messages. Can be: ``true`` or ``false``.
            voice_enabled: Whether the phone numbers can receive calls. Can be: ``true`` or ``false``.
            exclude_all_address_required: Whether to exclude phone numbers that require an `Address
                <https://www.twilio.com/docs/usage/api/address>`__. Can be: ``true`` or ``false`` and the default is
                ``false``.
            exclude_local_address_required: Whether to exclude phone numbers that require a local `Address
                <https://www.twilio.com/docs/usage/api/address>`__. Can be: ``true`` or ``false`` and the default is
                ``false``.
            exclude_foreign_address_required: Whether to exclude phone numbers that require a foreign `Address
                <https://www.twilio.com/docs/usage/api/address>`__. Can be: ``true`` or ``false`` and the default is
                ``false``.
            beta: Whether to read phone numbers that are new to the Twilio platform. Can be: ``true`` or ``false`` and
                the default is ``true``.
            near_number: Given a phone number, find a geographically close number within ``distance`` miles. Distance
                defaults to 25 miles. Applies to only phone numbers in the US and Canada.
            near_lat_long: Given a latitude/longitude pair ``lat,long`` find geographically close numbers within
                ``distance`` miles. Applies to only phone numbers in the US and Canada.
            distance: The search radius, in miles, for a ``near_`` query. Can be up to ``500`` and the default is
                ``25``. Applies to only phone numbers in the US and Canada.
            in_postal_code: Limit results to a particular postal code. Given a phone number, search within the same
                postal code as that number. Applies to only phone numbers in the US and Canada.
            in_region: Limit results to a particular region, state, or province. Given a phone number, search within the
                same region as that number. Applies to only phone numbers in the US and Canada.
            in_rate_center: Limit results to a specific rate center, or given a phone number search within the same rate
                center as that number. Requires ``in_lata`` to be set as well. Applies to only phone numbers in the US
                and Canada.
            in_lata: Limit results to a specific local access and transport area (`LATA
                <https://en.wikipedia.org/wiki/Local_access_and_transport_area>`__). Given a phone number, search within
                the same `LATA <https://en.wikipedia.org/wiki/Local_access_and_transport_area>`__ as that number.
                Applies to only phone numbers in the US and Canada.
            in_locality: Limit results to a particular locality or city. Given a phone number, search within the same
                Locality as that number.
            fax_enabled: Whether the phone numbers can receive faxes. Can be: ``true`` or ``false``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers/{CountryCode}/National.json"
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("CountryCode", country_code)],
            query_params=[
                param[int | None]("AreaCode", area_code),
                param[str | None]("Contains", contains),
                param[bool | None]("SmsEnabled", sms_enabled),
                param[bool | None]("MmsEnabled", mms_enabled),
                param[bool | None]("VoiceEnabled", voice_enabled),
                param[bool | None]("ExcludeAllAddressRequired", exclude_all_address_required),
                param[bool | None]("ExcludeLocalAddressRequired", exclude_local_address_required),
                param[bool | None]("ExcludeForeignAddressRequired", exclude_foreign_address_required),
                param[bool | None]("Beta", beta),
                param[str | None]("NearNumber", near_number),
                param[str | None]("NearLatLong", near_lat_long),
                param[int | None]("Distance", distance),
                param[str | None]("InPostalCode", in_postal_code),
                param[str | None]("InRegion", in_region),
                param[str | None]("InRateCenter", in_rate_center),
                param[str | None]("InLata", in_lata),
                param[str | None]("InLocality", in_locality),
                param[bool | None]("FaxEnabled", fax_enabled),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListAvailablePhoneNumberNationalResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401NationalWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def list_available_phone_number_national(
        self,
        account_sid: str,
        country_code: str,
        *,
        area_code: int | None = None,
        contains: str | None = None,
        sms_enabled: bool | None = None,
        mms_enabled: bool | None = None,
        voice_enabled: bool | None = None,
        exclude_all_address_required: bool | None = None,
        exclude_local_address_required: bool | None = None,
        exclude_foreign_address_required: bool | None = None,
        beta: bool | None = None,
        near_number: str | None = None,
        near_lat_long: str | None = None,
        distance: int | None = None,
        in_postal_code: str | None = None,
        in_region: str | None = None,
        in_rate_center: str | None = None,
        in_lata: str | None = None,
        in_locality: str | None = None,
        fax_enabled: bool | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListAvailablePhoneNumberNationalResponse, RawError]:
        """Available national phone numbers

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ requesting the
                AvailablePhoneNumber resources.
            country_code: The `ISO-3166-1 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code of the
                country from which to read phone numbers.
            area_code: The area code of the phone numbers to read. Applies to only phone numbers in the US and Canada.
            contains: Matching pattern to identify phone numbers. This pattern can be between 2 and 16 characters long
                and allows all digits (0-9) and all non-diacritic latin alphabet letters (a-z, A-Z). It accepts four
                meta-characters: ``*``, ``%``, ``+``, ``$``. The ``*`` and ``%`` meta-characters can appear multiple
                times in the pattern. To match wildcards at the beginning or end of the pattern, use ``*`` to match any
                single character or ``%`` to match a sequence of characters. If you use the wildcard patterns, it must
                include at least two non-meta-characters, and wildcards cannot be used between non-meta-characters. To
                match the beginning of a pattern, start the pattern with ``+``. To match the end of the pattern, append
                the pattern with ``$``. These meta-characters can't be adjacent to each other.
            sms_enabled: Whether the phone numbers can receive text messages. Can be: ``true`` or ``false``.
            mms_enabled: Whether the phone numbers can receive MMS messages. Can be: ``true`` or ``false``.
            voice_enabled: Whether the phone numbers can receive calls. Can be: ``true`` or ``false``.
            exclude_all_address_required: Whether to exclude phone numbers that require an `Address
                <https://www.twilio.com/docs/usage/api/address>`__. Can be: ``true`` or ``false`` and the default is
                ``false``.
            exclude_local_address_required: Whether to exclude phone numbers that require a local `Address
                <https://www.twilio.com/docs/usage/api/address>`__. Can be: ``true`` or ``false`` and the default is
                ``false``.
            exclude_foreign_address_required: Whether to exclude phone numbers that require a foreign `Address
                <https://www.twilio.com/docs/usage/api/address>`__. Can be: ``true`` or ``false`` and the default is
                ``false``.
            beta: Whether to read phone numbers that are new to the Twilio platform. Can be: ``true`` or ``false`` and
                the default is ``true``.
            near_number: Given a phone number, find a geographically close number within ``distance`` miles. Distance
                defaults to 25 miles. Applies to only phone numbers in the US and Canada.
            near_lat_long: Given a latitude/longitude pair ``lat,long`` find geographically close numbers within
                ``distance`` miles. Applies to only phone numbers in the US and Canada.
            distance: The search radius, in miles, for a ``near_`` query. Can be up to ``500`` and the default is
                ``25``. Applies to only phone numbers in the US and Canada.
            in_postal_code: Limit results to a particular postal code. Given a phone number, search within the same
                postal code as that number. Applies to only phone numbers in the US and Canada.
            in_region: Limit results to a particular region, state, or province. Given a phone number, search within the
                same region as that number. Applies to only phone numbers in the US and Canada.
            in_rate_center: Limit results to a specific rate center, or given a phone number search within the same rate
                center as that number. Requires ``in_lata`` to be set as well. Applies to only phone numbers in the US
                and Canada.
            in_lata: Limit results to a specific local access and transport area (`LATA
                <https://en.wikipedia.org/wiki/Local_access_and_transport_area>`__). Given a phone number, search within
                the same `LATA <https://en.wikipedia.org/wiki/Local_access_and_transport_area>`__ as that number.
                Applies to only phone numbers in the US and Canada.
            in_locality: Limit results to a particular locality or city. Given a phone number, search within the same
                Locality as that number.
            fax_enabled: Whether the phone numbers can receive faxes. Can be: ``true`` or ``false``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers/{CountryCode}/National.json"
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("CountryCode", country_code)],
            query_params=[
                param[int | None]("AreaCode", area_code),
                param[str | None]("Contains", contains),
                param[bool | None]("SmsEnabled", sms_enabled),
                param[bool | None]("MmsEnabled", mms_enabled),
                param[bool | None]("VoiceEnabled", voice_enabled),
                param[bool | None]("ExcludeAllAddressRequired", exclude_all_address_required),
                param[bool | None]("ExcludeLocalAddressRequired", exclude_local_address_required),
                param[bool | None]("ExcludeForeignAddressRequired", exclude_foreign_address_required),
                param[bool | None]("Beta", beta),
                param[str | None]("NearNumber", near_number),
                param[str | None]("NearLatLong", near_lat_long),
                param[int | None]("Distance", distance),
                param[str | None]("InPostalCode", in_postal_code),
                param[str | None]("InRegion", in_region),
                param[str | None]("InRateCenter", in_rate_center),
                param[str | None]("InLata", in_lata),
                param[str | None]("InLocality", in_locality),
                param[bool | None]("FaxEnabled", fax_enabled),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListAvailablePhoneNumberNationalResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
