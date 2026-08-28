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
from ..models.lookup_response import LookupResponse
from ..server.server import Server


class LookupsV2PhoneNumber:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = LookupsV2PhoneNumberWithRawResponse(client, server, auth)

    def fetch_phone_number3(
        self,
        phone_number: str,
        *,
        fields: str | None = None,
        country_code: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        address_line1: str | None = None,
        address_line2: str | None = None,
        city: str | None = None,
        state: str | None = None,
        postal_code: str | None = None,
        address_country_code: str | None = None,
        national_id: str | None = None,
        date_of_birth: str | None = None,
        last_verified_date: str | None = None,
        verification_sid: str | None = None,
        partner_sub_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> LookupResponse:
        """The Lookup API allows you to query information on a phone number so that you can make a trusted interaction
        with your user

        Args:
            phone_number: The phone number to lookup in E.164 or national format. Default country code is +1 (North
                America).
            fields: A comma-separated list of fields to return. Possible values are validation, caller_name, sim_swap,
                call_forwarding, line_status, line_type_intelligence, identity_match, reassigned_number,
                sms_pumping_risk, phone_number_quality_score, pre_fill.
            country_code: The `country code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ used if the phone
                number provided is in national format.
            first_name: User’s first name. This query parameter is only used (optionally) for identity_match package
                requests.
            last_name: User’s last name. This query parameter is only used (optionally) for identity_match package
                requests.
            address_line1: User’s first address line. This query parameter is only used (optionally) for identity_match
                package requests.
            address_line2: User’s second address line. This query parameter is only used (optionally) for identity_match
                package requests.
            city: User’s city. This query parameter is only used (optionally) for identity_match package requests.
            state: User’s country subdivision, such as state, province, or locality. This query parameter is only used
                (optionally) for identity_match package requests.
            postal_code: User’s postal zip code. This query parameter is only used (optionally) for identity_match
                package requests.
            address_country_code: User’s country, up to two characters. This query parameter is only used (optionally)
                for identity_match package requests.
            national_id: User’s national ID, such as SSN or Passport ID. This query parameter is only used (optionally)
                for identity_match package requests.
            date_of_birth: User’s date of birth, in YYYYMMDD format. This query parameter is only used (optionally) for
                identity_match package requests.
            last_verified_date: The date you obtained consent to call or text the end-user of the phone number or a date
                on which you are reasonably certain that the end-user could still be reached at that number. This query
                parameter is only used (optionally) for reassigned_number package requests.
            verification_sid: The unique identifier associated with a verification process through verify API. This
                query parameter is only used (optionally) for pre_fill package requests.
            partner_sub_id: The optional partnerSubId parameter to provide context for your sub-accounts, tenantIDs,
                sender IDs or other segmentation, enhancing the accuracy of the risk analysis.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_phone_number3(
            phone_number,
            fields=fields,
            country_code=country_code,
            first_name=first_name,
            last_name=last_name,
            address_line1=address_line1,
            address_line2=address_line2,
            city=city,
            state=state,
            postal_code=postal_code,
            address_country_code=address_country_code,
            national_id=national_id,
            date_of_birth=date_of_birth,
            last_verified_date=last_verified_date,
            verification_sid=verification_sid,
            partner_sub_id=partner_sub_id,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> LookupsV2PhoneNumberWithRawResponse:
        return self._with_raw_response


class AsyncLookupsV2PhoneNumber:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncLookupsV2PhoneNumberWithRawResponse(client, server, auth)

    async def fetch_phone_number3(
        self,
        phone_number: str,
        *,
        fields: str | None = None,
        country_code: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        address_line1: str | None = None,
        address_line2: str | None = None,
        city: str | None = None,
        state: str | None = None,
        postal_code: str | None = None,
        address_country_code: str | None = None,
        national_id: str | None = None,
        date_of_birth: str | None = None,
        last_verified_date: str | None = None,
        verification_sid: str | None = None,
        partner_sub_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> LookupResponse:
        """The Lookup API allows you to query information on a phone number so that you can make a trusted interaction
        with your user

        Args:
            phone_number: The phone number to lookup in E.164 or national format. Default country code is +1 (North
                America).
            fields: A comma-separated list of fields to return. Possible values are validation, caller_name, sim_swap,
                call_forwarding, line_status, line_type_intelligence, identity_match, reassigned_number,
                sms_pumping_risk, phone_number_quality_score, pre_fill.
            country_code: The `country code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ used if the phone
                number provided is in national format.
            first_name: User’s first name. This query parameter is only used (optionally) for identity_match package
                requests.
            last_name: User’s last name. This query parameter is only used (optionally) for identity_match package
                requests.
            address_line1: User’s first address line. This query parameter is only used (optionally) for identity_match
                package requests.
            address_line2: User’s second address line. This query parameter is only used (optionally) for identity_match
                package requests.
            city: User’s city. This query parameter is only used (optionally) for identity_match package requests.
            state: User’s country subdivision, such as state, province, or locality. This query parameter is only used
                (optionally) for identity_match package requests.
            postal_code: User’s postal zip code. This query parameter is only used (optionally) for identity_match
                package requests.
            address_country_code: User’s country, up to two characters. This query parameter is only used (optionally)
                for identity_match package requests.
            national_id: User’s national ID, such as SSN or Passport ID. This query parameter is only used (optionally)
                for identity_match package requests.
            date_of_birth: User’s date of birth, in YYYYMMDD format. This query parameter is only used (optionally) for
                identity_match package requests.
            last_verified_date: The date you obtained consent to call or text the end-user of the phone number or a date
                on which you are reasonably certain that the end-user could still be reached at that number. This query
                parameter is only used (optionally) for reassigned_number package requests.
            verification_sid: The unique identifier associated with a verification process through verify API. This
                query parameter is only used (optionally) for pre_fill package requests.
            partner_sub_id: The optional partnerSubId parameter to provide context for your sub-accounts, tenantIDs,
                sender IDs or other segmentation, enhancing the accuracy of the risk analysis.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_phone_number3(
                phone_number,
                fields=fields,
                country_code=country_code,
                first_name=first_name,
                last_name=last_name,
                address_line1=address_line1,
                address_line2=address_line2,
                city=city,
                state=state,
                postal_code=postal_code,
                address_country_code=address_country_code,
                national_id=national_id,
                date_of_birth=date_of_birth,
                last_verified_date=last_verified_date,
                verification_sid=verification_sid,
                partner_sub_id=partner_sub_id,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncLookupsV2PhoneNumberWithRawResponse:
        return self._with_raw_response


class LookupsV2PhoneNumberWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_phone_number3(
        self,
        phone_number: str,
        *,
        fields: str | None = None,
        country_code: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        address_line1: str | None = None,
        address_line2: str | None = None,
        city: str | None = None,
        state: str | None = None,
        postal_code: str | None = None,
        address_country_code: str | None = None,
        national_id: str | None = None,
        date_of_birth: str | None = None,
        last_verified_date: str | None = None,
        verification_sid: str | None = None,
        partner_sub_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[LookupResponse, RawError]:
        """The Lookup API allows you to query information on a phone number so that you can make a trusted interaction
        with your user

        Args:
            phone_number: The phone number to lookup in E.164 or national format. Default country code is +1 (North
                America).
            fields: A comma-separated list of fields to return. Possible values are validation, caller_name, sim_swap,
                call_forwarding, line_status, line_type_intelligence, identity_match, reassigned_number,
                sms_pumping_risk, phone_number_quality_score, pre_fill.
            country_code: The `country code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ used if the phone
                number provided is in national format.
            first_name: User’s first name. This query parameter is only used (optionally) for identity_match package
                requests.
            last_name: User’s last name. This query parameter is only used (optionally) for identity_match package
                requests.
            address_line1: User’s first address line. This query parameter is only used (optionally) for identity_match
                package requests.
            address_line2: User’s second address line. This query parameter is only used (optionally) for identity_match
                package requests.
            city: User’s city. This query parameter is only used (optionally) for identity_match package requests.
            state: User’s country subdivision, such as state, province, or locality. This query parameter is only used
                (optionally) for identity_match package requests.
            postal_code: User’s postal zip code. This query parameter is only used (optionally) for identity_match
                package requests.
            address_country_code: User’s country, up to two characters. This query parameter is only used (optionally)
                for identity_match package requests.
            national_id: User’s national ID, such as SSN or Passport ID. This query parameter is only used (optionally)
                for identity_match package requests.
            date_of_birth: User’s date of birth, in YYYYMMDD format. This query parameter is only used (optionally) for
                identity_match package requests.
            last_verified_date: The date you obtained consent to call or text the end-user of the phone number or a date
                on which you are reasonably certain that the end-user could still be reached at that number. This query
                parameter is only used (optionally) for reassigned_number package requests.
            verification_sid: The unique identifier associated with a verification process through verify API. This
                query parameter is only used (optionally) for pre_fill package requests.
            partner_sub_id: The optional partnerSubId parameter to provide context for your sub-accounts, tenantIDs,
                sender IDs or other segmentation, enhancing the accuracy of the risk analysis.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default4("/v2/PhoneNumbers/{PhoneNumber}"),
            path_params=[param[str]("PhoneNumber", phone_number)],
            query_params=[
                param[str | None]("Fields", fields),
                param[str | None]("CountryCode", country_code),
                param[str | None]("FirstName", first_name),
                param[str | None]("LastName", last_name),
                param[str | None]("AddressLine1", address_line1),
                param[str | None]("AddressLine2", address_line2),
                param[str | None]("City", city),
                param[str | None]("State", state),
                param[str | None]("PostalCode", postal_code),
                param[str | None]("AddressCountryCode", address_country_code),
                param[str | None]("NationalId", national_id),
                param[str | None]("DateOfBirth", date_of_birth),
                param[str | None]("LastVerifiedDate", last_verified_date),
                param[str | None]("VerificationSid", verification_sid),
                param[str | None]("PartnerSubId", partner_sub_id),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[LookupResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncLookupsV2PhoneNumberWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_phone_number3(
        self,
        phone_number: str,
        *,
        fields: str | None = None,
        country_code: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        address_line1: str | None = None,
        address_line2: str | None = None,
        city: str | None = None,
        state: str | None = None,
        postal_code: str | None = None,
        address_country_code: str | None = None,
        national_id: str | None = None,
        date_of_birth: str | None = None,
        last_verified_date: str | None = None,
        verification_sid: str | None = None,
        partner_sub_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[LookupResponse, RawError]:
        """The Lookup API allows you to query information on a phone number so that you can make a trusted interaction
        with your user

        Args:
            phone_number: The phone number to lookup in E.164 or national format. Default country code is +1 (North
                America).
            fields: A comma-separated list of fields to return. Possible values are validation, caller_name, sim_swap,
                call_forwarding, line_status, line_type_intelligence, identity_match, reassigned_number,
                sms_pumping_risk, phone_number_quality_score, pre_fill.
            country_code: The `country code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ used if the phone
                number provided is in national format.
            first_name: User’s first name. This query parameter is only used (optionally) for identity_match package
                requests.
            last_name: User’s last name. This query parameter is only used (optionally) for identity_match package
                requests.
            address_line1: User’s first address line. This query parameter is only used (optionally) for identity_match
                package requests.
            address_line2: User’s second address line. This query parameter is only used (optionally) for identity_match
                package requests.
            city: User’s city. This query parameter is only used (optionally) for identity_match package requests.
            state: User’s country subdivision, such as state, province, or locality. This query parameter is only used
                (optionally) for identity_match package requests.
            postal_code: User’s postal zip code. This query parameter is only used (optionally) for identity_match
                package requests.
            address_country_code: User’s country, up to two characters. This query parameter is only used (optionally)
                for identity_match package requests.
            national_id: User’s national ID, such as SSN or Passport ID. This query parameter is only used (optionally)
                for identity_match package requests.
            date_of_birth: User’s date of birth, in YYYYMMDD format. This query parameter is only used (optionally) for
                identity_match package requests.
            last_verified_date: The date you obtained consent to call or text the end-user of the phone number or a date
                on which you are reasonably certain that the end-user could still be reached at that number. This query
                parameter is only used (optionally) for reassigned_number package requests.
            verification_sid: The unique identifier associated with a verification process through verify API. This
                query parameter is only used (optionally) for pre_fill package requests.
            partner_sub_id: The optional partnerSubId parameter to provide context for your sub-accounts, tenantIDs,
                sender IDs or other segmentation, enhancing the accuracy of the risk analysis.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default4("/v2/PhoneNumbers/{PhoneNumber}"),
            path_params=[param[str]("PhoneNumber", phone_number)],
            query_params=[
                param[str | None]("Fields", fields),
                param[str | None]("CountryCode", country_code),
                param[str | None]("FirstName", first_name),
                param[str | None]("LastName", last_name),
                param[str | None]("AddressLine1", address_line1),
                param[str | None]("AddressLine2", address_line2),
                param[str | None]("City", city),
                param[str | None]("State", state),
                param[str | None]("PostalCode", postal_code),
                param[str | None]("AddressCountryCode", address_country_code),
                param[str | None]("NationalId", national_id),
                param[str | None]("DateOfBirth", date_of_birth),
                param[str | None]("LastVerifiedDate", last_verified_date),
                param[str | None]("VerificationSid", verification_sid),
                param[str | None]("PartnerSubId", partner_sub_id),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[LookupResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
