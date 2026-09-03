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
from ..models.enums.compliance_registration_enum_business_identity_type import (
    ComplianceRegistrationEnumBusinessIdentityTypeOrStr,
)
from ..models.enums.compliance_registration_enum_business_registration_authority import (
    ComplianceRegistrationEnumBusinessRegistrationAuthorityOrStr,
)
from ..models.enums.compliance_registration_enum_phone_number_type import ComplianceRegistrationEnumPhoneNumberTypeOrStr
from ..models.enums.customer_type import CustomerTypeOrStr
from ..models.trusthub_v1_compliance_registration import TrusthubV1ComplianceRegistration
from ..server.server import Server


class TrusthubV1ComplianceRegistrationInquiries:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TrusthubV1ComplianceRegistrationInquiriesWithRawResponse(client, server, auth)

    def create_compliance_registration(
        self,
        end_user_type: CustomerTypeOrStr,
        phone_number_type: ComplianceRegistrationEnumPhoneNumberTypeOrStr,
        *,
        business_identity_type: ComplianceRegistrationEnumBusinessIdentityTypeOrStr | None = None,
        business_registration_authority: ComplianceRegistrationEnumBusinessRegistrationAuthorityOrStr | None = None,
        business_legal_name: str | None = None,
        notification_email: str | None = None,
        accepted_notification_receipt: bool | None = None,
        business_registration_number: str | None = None,
        business_website_url: str | None = None,
        friendly_name: str | None = None,
        authorized_representative1_first_name: str | None = None,
        authorized_representative1_last_name: str | None = None,
        authorized_representative1_phone: str | None = None,
        authorized_representative1_email: str | None = None,
        authorized_representative1_date_of_birth: str | None = None,
        address_street: str | None = None,
        address_street_secondary: str | None = None,
        address_city: str | None = None,
        address_subdivision: str | None = None,
        address_postal_code: str | None = None,
        address_country_code: str | None = None,
        emergency_address_street: str | None = None,
        emergency_address_street_secondary: str | None = None,
        emergency_address_city: str | None = None,
        emergency_address_subdivision: str | None = None,
        emergency_address_postal_code: str | None = None,
        emergency_address_country_code: str | None = None,
        use_address_as_emergency_address: bool | None = None,
        file_name: str | None = None,
        file: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        date_of_birth: str | None = None,
        individual_email: str | None = None,
        individual_phone: str | None = None,
        is_isv_embed: bool | None = None,
        isv_registering_for_self_or_tenant: str | None = None,
        status_callback_url: str | None = None,
        theme_set_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TrusthubV1ComplianceRegistration:
        """Create a new Compliance Registration Inquiry for the authenticated account. This is necessary to start a new
        embedded session.

        Args:
            end_user_type: The type of End User the regulation requires - can be ``Individual`` or ``Business``.
            phone_number_type: The type of phone number of the Bundle's ownership request. Can be ``local``, ``mobile``,
                ``national``, or ``toll-free``.
            business_identity_type: The type of business identity. Can be ``direct customer`` or ``ISV``.
            business_registration_authority: The authority that registered the business
            business_legal_name: he name of the business or organization using the Tollfree number.
            notification_email: he email address to receive the notification about the verification result.
            accepted_notification_receipt: The email address to receive the notification about the verification result.
            business_registration_number: Business registration number of the business
            business_website_url: The URL of the business website
            friendly_name: Friendly name for your business information
            authorized_representative1_first_name: First name of the authorized representative
            authorized_representative1_last_name: Last name of the authorized representative
            authorized_representative1_phone: Phone number of the authorized representative
            authorized_representative1_email: Email address of the authorized representative
            authorized_representative1_date_of_birth: Birthdate of the authorized representative
            address_street: Street address of the business
            address_street_secondary: Street address of the business
            address_city: City of the business
            address_subdivision: State or province of the business
            address_postal_code: Postal code of the business
            address_country_code: Country code of the business
            emergency_address_street: Street address of the business
            emergency_address_street_secondary: Street address of the business
            emergency_address_city: City of the business
            emergency_address_subdivision: State or province of the business
            emergency_address_postal_code: Postal code of the business
            emergency_address_country_code: Country code of the business
            use_address_as_emergency_address: Use the business address as the emergency address
            file_name: The name of the verification document to upload
            file: The verification document to upload
            first_name: The first name of the Individual User.
            last_name: The last name of the Individual User.
            date_of_birth: The date of birth of the Individual User.
            individual_email: The email address of the Individual User.
            individual_phone: The phone number of the Individual User.
            is_isv_embed: Indicates if the inquiry is being started from an ISV embedded component.
            isv_registering_for_self_or_tenant: Indicates if the isv registering for self or tenant.
            status_callback_url: The url we call to inform you of bundle changes.
            theme_set_id: Theme id for styling the inquiry form.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_compliance_registration(
            end_user_type,
            phone_number_type,
            business_identity_type=business_identity_type,
            business_registration_authority=business_registration_authority,
            business_legal_name=business_legal_name,
            notification_email=notification_email,
            accepted_notification_receipt=accepted_notification_receipt,
            business_registration_number=business_registration_number,
            business_website_url=business_website_url,
            friendly_name=friendly_name,
            authorized_representative1_first_name=authorized_representative1_first_name,
            authorized_representative1_last_name=authorized_representative1_last_name,
            authorized_representative1_phone=authorized_representative1_phone,
            authorized_representative1_email=authorized_representative1_email,
            authorized_representative1_date_of_birth=authorized_representative1_date_of_birth,
            address_street=address_street,
            address_street_secondary=address_street_secondary,
            address_city=address_city,
            address_subdivision=address_subdivision,
            address_postal_code=address_postal_code,
            address_country_code=address_country_code,
            emergency_address_street=emergency_address_street,
            emergency_address_street_secondary=emergency_address_street_secondary,
            emergency_address_city=emergency_address_city,
            emergency_address_subdivision=emergency_address_subdivision,
            emergency_address_postal_code=emergency_address_postal_code,
            emergency_address_country_code=emergency_address_country_code,
            use_address_as_emergency_address=use_address_as_emergency_address,
            file_name=file_name,
            file=file,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            individual_email=individual_email,
            individual_phone=individual_phone,
            is_isv_embed=is_isv_embed,
            isv_registering_for_self_or_tenant=isv_registering_for_self_or_tenant,
            status_callback_url=status_callback_url,
            theme_set_id=theme_set_id,
            request_options=request_options,
        ).unwrap()

    def update_compliance_registration(
        self,
        registration_id: str,
        *,
        is_isv_embed: bool | None = None,
        theme_set_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TrusthubV1ComplianceRegistration:
        """Resume a specific Regulatory Compliance Inquiry that has expired, or re-open a rejected Compliance Inquiry
        for editing.

        Args:
            registration_id: The unique RegistrationId matching the Regulatory Compliance Inquiry that should be resumed
                or resubmitted. This value will have been returned by the initial Regulatory Compliance Inquiry creation
                call.
            is_isv_embed: Indicates if the inquiry is being started from an ISV embedded component.
            theme_set_id: Theme id for styling the inquiry form.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_compliance_registration(
            registration_id, is_isv_embed=is_isv_embed, theme_set_id=theme_set_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> TrusthubV1ComplianceRegistrationInquiriesWithRawResponse:
        return self._with_raw_response


class AsyncTrusthubV1ComplianceRegistrationInquiries:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTrusthubV1ComplianceRegistrationInquiriesWithRawResponse(client, server, auth)

    async def create_compliance_registration(
        self,
        end_user_type: CustomerTypeOrStr,
        phone_number_type: ComplianceRegistrationEnumPhoneNumberTypeOrStr,
        *,
        business_identity_type: ComplianceRegistrationEnumBusinessIdentityTypeOrStr | None = None,
        business_registration_authority: ComplianceRegistrationEnumBusinessRegistrationAuthorityOrStr | None = None,
        business_legal_name: str | None = None,
        notification_email: str | None = None,
        accepted_notification_receipt: bool | None = None,
        business_registration_number: str | None = None,
        business_website_url: str | None = None,
        friendly_name: str | None = None,
        authorized_representative1_first_name: str | None = None,
        authorized_representative1_last_name: str | None = None,
        authorized_representative1_phone: str | None = None,
        authorized_representative1_email: str | None = None,
        authorized_representative1_date_of_birth: str | None = None,
        address_street: str | None = None,
        address_street_secondary: str | None = None,
        address_city: str | None = None,
        address_subdivision: str | None = None,
        address_postal_code: str | None = None,
        address_country_code: str | None = None,
        emergency_address_street: str | None = None,
        emergency_address_street_secondary: str | None = None,
        emergency_address_city: str | None = None,
        emergency_address_subdivision: str | None = None,
        emergency_address_postal_code: str | None = None,
        emergency_address_country_code: str | None = None,
        use_address_as_emergency_address: bool | None = None,
        file_name: str | None = None,
        file: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        date_of_birth: str | None = None,
        individual_email: str | None = None,
        individual_phone: str | None = None,
        is_isv_embed: bool | None = None,
        isv_registering_for_self_or_tenant: str | None = None,
        status_callback_url: str | None = None,
        theme_set_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TrusthubV1ComplianceRegistration:
        """Create a new Compliance Registration Inquiry for the authenticated account. This is necessary to start a new
        embedded session.

        Args:
            end_user_type: The type of End User the regulation requires - can be ``Individual`` or ``Business``.
            phone_number_type: The type of phone number of the Bundle's ownership request. Can be ``local``, ``mobile``,
                ``national``, or ``toll-free``.
            business_identity_type: The type of business identity. Can be ``direct customer`` or ``ISV``.
            business_registration_authority: The authority that registered the business
            business_legal_name: he name of the business or organization using the Tollfree number.
            notification_email: he email address to receive the notification about the verification result.
            accepted_notification_receipt: The email address to receive the notification about the verification result.
            business_registration_number: Business registration number of the business
            business_website_url: The URL of the business website
            friendly_name: Friendly name for your business information
            authorized_representative1_first_name: First name of the authorized representative
            authorized_representative1_last_name: Last name of the authorized representative
            authorized_representative1_phone: Phone number of the authorized representative
            authorized_representative1_email: Email address of the authorized representative
            authorized_representative1_date_of_birth: Birthdate of the authorized representative
            address_street: Street address of the business
            address_street_secondary: Street address of the business
            address_city: City of the business
            address_subdivision: State or province of the business
            address_postal_code: Postal code of the business
            address_country_code: Country code of the business
            emergency_address_street: Street address of the business
            emergency_address_street_secondary: Street address of the business
            emergency_address_city: City of the business
            emergency_address_subdivision: State or province of the business
            emergency_address_postal_code: Postal code of the business
            emergency_address_country_code: Country code of the business
            use_address_as_emergency_address: Use the business address as the emergency address
            file_name: The name of the verification document to upload
            file: The verification document to upload
            first_name: The first name of the Individual User.
            last_name: The last name of the Individual User.
            date_of_birth: The date of birth of the Individual User.
            individual_email: The email address of the Individual User.
            individual_phone: The phone number of the Individual User.
            is_isv_embed: Indicates if the inquiry is being started from an ISV embedded component.
            isv_registering_for_self_or_tenant: Indicates if the isv registering for self or tenant.
            status_callback_url: The url we call to inform you of bundle changes.
            theme_set_id: Theme id for styling the inquiry form.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_compliance_registration(
                end_user_type,
                phone_number_type,
                business_identity_type=business_identity_type,
                business_registration_authority=business_registration_authority,
                business_legal_name=business_legal_name,
                notification_email=notification_email,
                accepted_notification_receipt=accepted_notification_receipt,
                business_registration_number=business_registration_number,
                business_website_url=business_website_url,
                friendly_name=friendly_name,
                authorized_representative1_first_name=authorized_representative1_first_name,
                authorized_representative1_last_name=authorized_representative1_last_name,
                authorized_representative1_phone=authorized_representative1_phone,
                authorized_representative1_email=authorized_representative1_email,
                authorized_representative1_date_of_birth=authorized_representative1_date_of_birth,
                address_street=address_street,
                address_street_secondary=address_street_secondary,
                address_city=address_city,
                address_subdivision=address_subdivision,
                address_postal_code=address_postal_code,
                address_country_code=address_country_code,
                emergency_address_street=emergency_address_street,
                emergency_address_street_secondary=emergency_address_street_secondary,
                emergency_address_city=emergency_address_city,
                emergency_address_subdivision=emergency_address_subdivision,
                emergency_address_postal_code=emergency_address_postal_code,
                emergency_address_country_code=emergency_address_country_code,
                use_address_as_emergency_address=use_address_as_emergency_address,
                file_name=file_name,
                file=file,
                first_name=first_name,
                last_name=last_name,
                date_of_birth=date_of_birth,
                individual_email=individual_email,
                individual_phone=individual_phone,
                is_isv_embed=is_isv_embed,
                isv_registering_for_self_or_tenant=isv_registering_for_self_or_tenant,
                status_callback_url=status_callback_url,
                theme_set_id=theme_set_id,
                request_options=request_options,
            )
        ).unwrap()

    async def update_compliance_registration(
        self,
        registration_id: str,
        *,
        is_isv_embed: bool | None = None,
        theme_set_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TrusthubV1ComplianceRegistration:
        """Resume a specific Regulatory Compliance Inquiry that has expired, or re-open a rejected Compliance Inquiry
        for editing.

        Args:
            registration_id: The unique RegistrationId matching the Regulatory Compliance Inquiry that should be resumed
                or resubmitted. This value will have been returned by the initial Regulatory Compliance Inquiry creation
                call.
            is_isv_embed: Indicates if the inquiry is being started from an ISV embedded component.
            theme_set_id: Theme id for styling the inquiry form.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_compliance_registration(
                registration_id, is_isv_embed=is_isv_embed, theme_set_id=theme_set_id, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTrusthubV1ComplianceRegistrationInquiriesWithRawResponse:
        return self._with_raw_response


class TrusthubV1ComplianceRegistrationInquiriesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_compliance_registration(
        self,
        end_user_type: CustomerTypeOrStr,
        phone_number_type: ComplianceRegistrationEnumPhoneNumberTypeOrStr,
        *,
        business_identity_type: ComplianceRegistrationEnumBusinessIdentityTypeOrStr | None = None,
        business_registration_authority: ComplianceRegistrationEnumBusinessRegistrationAuthorityOrStr | None = None,
        business_legal_name: str | None = None,
        notification_email: str | None = None,
        accepted_notification_receipt: bool | None = None,
        business_registration_number: str | None = None,
        business_website_url: str | None = None,
        friendly_name: str | None = None,
        authorized_representative1_first_name: str | None = None,
        authorized_representative1_last_name: str | None = None,
        authorized_representative1_phone: str | None = None,
        authorized_representative1_email: str | None = None,
        authorized_representative1_date_of_birth: str | None = None,
        address_street: str | None = None,
        address_street_secondary: str | None = None,
        address_city: str | None = None,
        address_subdivision: str | None = None,
        address_postal_code: str | None = None,
        address_country_code: str | None = None,
        emergency_address_street: str | None = None,
        emergency_address_street_secondary: str | None = None,
        emergency_address_city: str | None = None,
        emergency_address_subdivision: str | None = None,
        emergency_address_postal_code: str | None = None,
        emergency_address_country_code: str | None = None,
        use_address_as_emergency_address: bool | None = None,
        file_name: str | None = None,
        file: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        date_of_birth: str | None = None,
        individual_email: str | None = None,
        individual_phone: str | None = None,
        is_isv_embed: bool | None = None,
        isv_registering_for_self_or_tenant: str | None = None,
        status_callback_url: str | None = None,
        theme_set_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TrusthubV1ComplianceRegistration, RawError]:
        """Create a new Compliance Registration Inquiry for the authenticated account. This is necessary to start a new
        embedded session.

        Args:
            end_user_type: The type of End User the regulation requires - can be ``Individual`` or ``Business``.
            phone_number_type: The type of phone number of the Bundle's ownership request. Can be ``local``, ``mobile``,
                ``national``, or ``toll-free``.
            business_identity_type: The type of business identity. Can be ``direct customer`` or ``ISV``.
            business_registration_authority: The authority that registered the business
            business_legal_name: he name of the business or organization using the Tollfree number.
            notification_email: he email address to receive the notification about the verification result.
            accepted_notification_receipt: The email address to receive the notification about the verification result.
            business_registration_number: Business registration number of the business
            business_website_url: The URL of the business website
            friendly_name: Friendly name for your business information
            authorized_representative1_first_name: First name of the authorized representative
            authorized_representative1_last_name: Last name of the authorized representative
            authorized_representative1_phone: Phone number of the authorized representative
            authorized_representative1_email: Email address of the authorized representative
            authorized_representative1_date_of_birth: Birthdate of the authorized representative
            address_street: Street address of the business
            address_street_secondary: Street address of the business
            address_city: City of the business
            address_subdivision: State or province of the business
            address_postal_code: Postal code of the business
            address_country_code: Country code of the business
            emergency_address_street: Street address of the business
            emergency_address_street_secondary: Street address of the business
            emergency_address_city: City of the business
            emergency_address_subdivision: State or province of the business
            emergency_address_postal_code: Postal code of the business
            emergency_address_country_code: Country code of the business
            use_address_as_emergency_address: Use the business address as the emergency address
            file_name: The name of the verification document to upload
            file: The verification document to upload
            first_name: The first name of the Individual User.
            last_name: The last name of the Individual User.
            date_of_birth: The date of birth of the Individual User.
            individual_email: The email address of the Individual User.
            individual_phone: The phone number of the Individual User.
            is_isv_embed: Indicates if the inquiry is being started from an ISV embedded component.
            isv_registering_for_self_or_tenant: Indicates if the isv registering for self or tenant.
            status_callback_url: The url we call to inform you of bundle changes.
            theme_set_id: Theme id for styling the inquiry form.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9(
                "/v1/ComplianceInquiries/Registration/RegulatoryCompliance/GB/Initialize"
            ),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[CustomerTypeOrStr]("EndUserType", end_user_type),
                    param[ComplianceRegistrationEnumPhoneNumberTypeOrStr]("PhoneNumberType", phone_number_type),
                    param[ComplianceRegistrationEnumBusinessIdentityTypeOrStr | None](
                        "BusinessIdentityType", business_identity_type
                    ),
                    param[ComplianceRegistrationEnumBusinessRegistrationAuthorityOrStr | None](
                        "BusinessRegistrationAuthority", business_registration_authority
                    ),
                    param[str | None]("BusinessLegalName", business_legal_name),
                    param[str | None]("NotificationEmail", notification_email),
                    param[bool | None]("AcceptedNotificationReceipt", accepted_notification_receipt),
                    param[str | None]("BusinessRegistrationNumber", business_registration_number),
                    param[str | None]("BusinessWebsiteUrl", business_website_url),
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("AuthorizedRepresentative1FirstName", authorized_representative1_first_name),
                    param[str | None]("AuthorizedRepresentative1LastName", authorized_representative1_last_name),
                    param[str | None]("AuthorizedRepresentative1Phone", authorized_representative1_phone),
                    param[str | None]("AuthorizedRepresentative1Email", authorized_representative1_email),
                    param[str | None]("AuthorizedRepresentative1DateOfBirth", authorized_representative1_date_of_birth),
                    param[str | None]("AddressStreet", address_street),
                    param[str | None]("AddressStreetSecondary", address_street_secondary),
                    param[str | None]("AddressCity", address_city),
                    param[str | None]("AddressSubdivision", address_subdivision),
                    param[str | None]("AddressPostalCode", address_postal_code),
                    param[str | None]("AddressCountryCode", address_country_code),
                    param[str | None]("EmergencyAddressStreet", emergency_address_street),
                    param[str | None]("EmergencyAddressStreetSecondary", emergency_address_street_secondary),
                    param[str | None]("EmergencyAddressCity", emergency_address_city),
                    param[str | None]("EmergencyAddressSubdivision", emergency_address_subdivision),
                    param[str | None]("EmergencyAddressPostalCode", emergency_address_postal_code),
                    param[str | None]("EmergencyAddressCountryCode", emergency_address_country_code),
                    param[bool | None]("UseAddressAsEmergencyAddress", use_address_as_emergency_address),
                    param[str | None]("FileName", file_name),
                    param[str | None]("File", file),
                    param[str | None]("FirstName", first_name),
                    param[str | None]("LastName", last_name),
                    param[str | None]("DateOfBirth", date_of_birth),
                    param[str | None]("IndividualEmail", individual_email),
                    param[str | None]("IndividualPhone", individual_phone),
                    param[bool | None]("IsIsvEmbed", is_isv_embed),
                    param[str | None]("IsvRegisteringForSelfOrTenant", isv_registering_for_self_or_tenant),
                    param[str | None]("StatusCallbackUrl", status_callback_url),
                    param[str | None]("ThemeSetId", theme_set_id),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1ComplianceRegistration],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_compliance_registration(
        self,
        registration_id: str,
        *,
        is_isv_embed: bool | None = None,
        theme_set_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TrusthubV1ComplianceRegistration, RawError]:
        """Resume a specific Regulatory Compliance Inquiry that has expired, or re-open a rejected Compliance Inquiry
        for editing.

        Args:
            registration_id: The unique RegistrationId matching the Regulatory Compliance Inquiry that should be resumed
                or resubmitted. This value will have been returned by the initial Regulatory Compliance Inquiry creation
                call.
            is_isv_embed: Indicates if the inquiry is being started from an ISV embedded component.
            theme_set_id: Theme id for styling the inquiry form.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9(
                "/v1/ComplianceInquiries/Registration/{RegistrationId}/RegulatoryCompliance/GB/Initialize"
            ),
            path_params=[param[str]("RegistrationId", registration_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [param[bool | None]("IsIsvEmbed", is_isv_embed), param[str | None]("ThemeSetId", theme_set_id)]
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1ComplianceRegistration],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTrusthubV1ComplianceRegistrationInquiriesWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def create_compliance_registration(
        self,
        end_user_type: CustomerTypeOrStr,
        phone_number_type: ComplianceRegistrationEnumPhoneNumberTypeOrStr,
        *,
        business_identity_type: ComplianceRegistrationEnumBusinessIdentityTypeOrStr | None = None,
        business_registration_authority: ComplianceRegistrationEnumBusinessRegistrationAuthorityOrStr | None = None,
        business_legal_name: str | None = None,
        notification_email: str | None = None,
        accepted_notification_receipt: bool | None = None,
        business_registration_number: str | None = None,
        business_website_url: str | None = None,
        friendly_name: str | None = None,
        authorized_representative1_first_name: str | None = None,
        authorized_representative1_last_name: str | None = None,
        authorized_representative1_phone: str | None = None,
        authorized_representative1_email: str | None = None,
        authorized_representative1_date_of_birth: str | None = None,
        address_street: str | None = None,
        address_street_secondary: str | None = None,
        address_city: str | None = None,
        address_subdivision: str | None = None,
        address_postal_code: str | None = None,
        address_country_code: str | None = None,
        emergency_address_street: str | None = None,
        emergency_address_street_secondary: str | None = None,
        emergency_address_city: str | None = None,
        emergency_address_subdivision: str | None = None,
        emergency_address_postal_code: str | None = None,
        emergency_address_country_code: str | None = None,
        use_address_as_emergency_address: bool | None = None,
        file_name: str | None = None,
        file: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        date_of_birth: str | None = None,
        individual_email: str | None = None,
        individual_phone: str | None = None,
        is_isv_embed: bool | None = None,
        isv_registering_for_self_or_tenant: str | None = None,
        status_callback_url: str | None = None,
        theme_set_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TrusthubV1ComplianceRegistration, RawError]:
        """Create a new Compliance Registration Inquiry for the authenticated account. This is necessary to start a new
        embedded session.

        Args:
            end_user_type: The type of End User the regulation requires - can be ``Individual`` or ``Business``.
            phone_number_type: The type of phone number of the Bundle's ownership request. Can be ``local``, ``mobile``,
                ``national``, or ``toll-free``.
            business_identity_type: The type of business identity. Can be ``direct customer`` or ``ISV``.
            business_registration_authority: The authority that registered the business
            business_legal_name: he name of the business or organization using the Tollfree number.
            notification_email: he email address to receive the notification about the verification result.
            accepted_notification_receipt: The email address to receive the notification about the verification result.
            business_registration_number: Business registration number of the business
            business_website_url: The URL of the business website
            friendly_name: Friendly name for your business information
            authorized_representative1_first_name: First name of the authorized representative
            authorized_representative1_last_name: Last name of the authorized representative
            authorized_representative1_phone: Phone number of the authorized representative
            authorized_representative1_email: Email address of the authorized representative
            authorized_representative1_date_of_birth: Birthdate of the authorized representative
            address_street: Street address of the business
            address_street_secondary: Street address of the business
            address_city: City of the business
            address_subdivision: State or province of the business
            address_postal_code: Postal code of the business
            address_country_code: Country code of the business
            emergency_address_street: Street address of the business
            emergency_address_street_secondary: Street address of the business
            emergency_address_city: City of the business
            emergency_address_subdivision: State or province of the business
            emergency_address_postal_code: Postal code of the business
            emergency_address_country_code: Country code of the business
            use_address_as_emergency_address: Use the business address as the emergency address
            file_name: The name of the verification document to upload
            file: The verification document to upload
            first_name: The first name of the Individual User.
            last_name: The last name of the Individual User.
            date_of_birth: The date of birth of the Individual User.
            individual_email: The email address of the Individual User.
            individual_phone: The phone number of the Individual User.
            is_isv_embed: Indicates if the inquiry is being started from an ISV embedded component.
            isv_registering_for_self_or_tenant: Indicates if the isv registering for self or tenant.
            status_callback_url: The url we call to inform you of bundle changes.
            theme_set_id: Theme id for styling the inquiry form.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9(
                "/v1/ComplianceInquiries/Registration/RegulatoryCompliance/GB/Initialize"
            ),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[CustomerTypeOrStr]("EndUserType", end_user_type),
                    param[ComplianceRegistrationEnumPhoneNumberTypeOrStr]("PhoneNumberType", phone_number_type),
                    param[ComplianceRegistrationEnumBusinessIdentityTypeOrStr | None](
                        "BusinessIdentityType", business_identity_type
                    ),
                    param[ComplianceRegistrationEnumBusinessRegistrationAuthorityOrStr | None](
                        "BusinessRegistrationAuthority", business_registration_authority
                    ),
                    param[str | None]("BusinessLegalName", business_legal_name),
                    param[str | None]("NotificationEmail", notification_email),
                    param[bool | None]("AcceptedNotificationReceipt", accepted_notification_receipt),
                    param[str | None]("BusinessRegistrationNumber", business_registration_number),
                    param[str | None]("BusinessWebsiteUrl", business_website_url),
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("AuthorizedRepresentative1FirstName", authorized_representative1_first_name),
                    param[str | None]("AuthorizedRepresentative1LastName", authorized_representative1_last_name),
                    param[str | None]("AuthorizedRepresentative1Phone", authorized_representative1_phone),
                    param[str | None]("AuthorizedRepresentative1Email", authorized_representative1_email),
                    param[str | None]("AuthorizedRepresentative1DateOfBirth", authorized_representative1_date_of_birth),
                    param[str | None]("AddressStreet", address_street),
                    param[str | None]("AddressStreetSecondary", address_street_secondary),
                    param[str | None]("AddressCity", address_city),
                    param[str | None]("AddressSubdivision", address_subdivision),
                    param[str | None]("AddressPostalCode", address_postal_code),
                    param[str | None]("AddressCountryCode", address_country_code),
                    param[str | None]("EmergencyAddressStreet", emergency_address_street),
                    param[str | None]("EmergencyAddressStreetSecondary", emergency_address_street_secondary),
                    param[str | None]("EmergencyAddressCity", emergency_address_city),
                    param[str | None]("EmergencyAddressSubdivision", emergency_address_subdivision),
                    param[str | None]("EmergencyAddressPostalCode", emergency_address_postal_code),
                    param[str | None]("EmergencyAddressCountryCode", emergency_address_country_code),
                    param[bool | None]("UseAddressAsEmergencyAddress", use_address_as_emergency_address),
                    param[str | None]("FileName", file_name),
                    param[str | None]("File", file),
                    param[str | None]("FirstName", first_name),
                    param[str | None]("LastName", last_name),
                    param[str | None]("DateOfBirth", date_of_birth),
                    param[str | None]("IndividualEmail", individual_email),
                    param[str | None]("IndividualPhone", individual_phone),
                    param[bool | None]("IsIsvEmbed", is_isv_embed),
                    param[str | None]("IsvRegisteringForSelfOrTenant", isv_registering_for_self_or_tenant),
                    param[str | None]("StatusCallbackUrl", status_callback_url),
                    param[str | None]("ThemeSetId", theme_set_id),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1ComplianceRegistration],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_compliance_registration(
        self,
        registration_id: str,
        *,
        is_isv_embed: bool | None = None,
        theme_set_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TrusthubV1ComplianceRegistration, RawError]:
        """Resume a specific Regulatory Compliance Inquiry that has expired, or re-open a rejected Compliance Inquiry
        for editing.

        Args:
            registration_id: The unique RegistrationId matching the Regulatory Compliance Inquiry that should be resumed
                or resubmitted. This value will have been returned by the initial Regulatory Compliance Inquiry creation
                call.
            is_isv_embed: Indicates if the inquiry is being started from an ISV embedded component.
            theme_set_id: Theme id for styling the inquiry form.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9(
                "/v1/ComplianceInquiries/Registration/{RegistrationId}/RegulatoryCompliance/GB/Initialize"
            ),
            path_params=[param[str]("RegistrationId", registration_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [param[bool | None]("IsIsvEmbed", is_isv_embed), param[str | None]("ThemeSetId", theme_set_id)]
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1ComplianceRegistration],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
