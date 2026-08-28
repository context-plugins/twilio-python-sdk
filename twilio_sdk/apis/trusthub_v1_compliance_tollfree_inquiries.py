from __future__ import annotations

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
from ..models.enums.compliance_tollfree_inquiry_enum_opt_in_type import ComplianceTollfreeInquiryEnumOptInTypeOrStr
from ..models.enums.tollfree_verification_enum_business_type import TollfreeVerificationEnumBusinessTypeOrStr
from ..models.trusthub_v1_compliance_tollfree_inquiry import TrusthubV1ComplianceTollfreeInquiry
from ..server.server import Server


class TrusthubV1ComplianceTollfreeInquiries:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TrusthubV1ComplianceTollfreeInquiriesWithRawResponse(client, server, auth)

    def create_compliance_tollfree_inquiry(
        self,
        tollfree_phone_number: str,
        notification_email: str,
        *,
        customer_profile_sid: str | None = None,
        business_name: str | None = None,
        business_website: str | None = None,
        use_case_categories: list[str] | None = None,
        use_case_summary: str | None = None,
        production_message_sample: str | None = None,
        opt_in_image_urls: list[str] | None = None,
        opt_in_type: ComplianceTollfreeInquiryEnumOptInTypeOrStr | None = None,
        message_volume: str | None = None,
        business_street_address: str | None = None,
        business_street_address2: str | None = None,
        business_city: str | None = None,
        business_state_province_region: str | None = None,
        business_postal_code: str | None = None,
        business_country: str | None = None,
        additional_information: str | None = None,
        business_contact_first_name: str | None = None,
        business_contact_last_name: str | None = None,
        business_contact_email: str | None = None,
        business_contact_phone: str | None = None,
        theme_set_id: str | None = None,
        skip_messaging_use_case: bool | None = None,
        business_registration_number: str | None = None,
        business_registration_authority: str | None = None,
        business_registration_country: str | None = None,
        business_type: TollfreeVerificationEnumBusinessTypeOrStr | None = None,
        doing_business_as: str | None = None,
        opt_in_confirmation_message: str | None = None,
        help_message_sample: str | None = None,
        privacy_policy_url: str | None = None,
        terms_and_conditions_url: str | None = None,
        age_gated_content: bool | None = None,
        external_reference_id: str | None = None,
        opt_in_keywords: list[str] | None = None,
        vetting_id: str | None = None,
        vetting_provider: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TrusthubV1ComplianceTollfreeInquiry:
        """Create a new Compliance Tollfree Verification Inquiry for the authenticated account. This is necessary to
        start a new embedded session.

        Args:
            tollfree_phone_number: The Tollfree phone number to be verified
            notification_email: The email address to receive the notification about the verification result.
            customer_profile_sid: The Customer Profile Sid associated with the Account.
            business_name: The name of the business or organization using the Tollfree number.
            business_website: The website of the business or organization using the Tollfree number.
            use_case_categories: The category of the use case for the Tollfree Number. List as many are applicable..
            use_case_summary: Use this to further explain how messaging is used by the business or organization.
            production_message_sample: An example of message content, i.e. a sample message.
            opt_in_image_urls: Link to an image that shows the opt-in workflow. Multiple images allowed and must be a
                publicly hosted URL.
            opt_in_type: Describe how a user opts-in to text messages.
            message_volume: Estimate monthly volume of messages from the Tollfree Number.
            business_street_address: The address of the business or organization using the Tollfree number.
            business_street_address2: The address of the business or organization using the Tollfree number.
            business_city: The city of the business or organization using the Tollfree number.
            business_state_province_region: The state/province/region of the business or organization using the Tollfree
                number.
            business_postal_code: The postal code of the business or organization using the Tollfree number.
            business_country: The country of the business or organization using the Tollfree number.
            additional_information: Additional information to be provided for verification.
            business_contact_first_name: The first name of the contact for the business or organization using the
                Tollfree number.
            business_contact_last_name: The last name of the contact for the business or organization using the Tollfree
                number.
            business_contact_email: The email address of the contact for the business or organization using the Tollfree
                number.
            business_contact_phone: The phone number of the contact for the business or organization using the Tollfree
                number.
            theme_set_id: Theme id for styling the inquiry form.
            skip_messaging_use_case: Skip the messaging use case screen of the inquiry form.
            business_registration_number: The Business Registration Number of the business or organization.
            business_registration_authority: The Business Registration Authority of the business or organization.
            business_registration_country: The Business Registration Country of the business or organization.
            business_type: Type of Business.
            doing_business_as: Trade name, sub entity, or downstream business name of business being submitted for
                verification.
            opt_in_confirmation_message: The confirmation message sent to users when they opt in to receive messages.
            help_message_sample: A sample help message provided to users.
            privacy_policy_url: The URL to the privacy policy for the business or organization.
            terms_and_conditions_url: The URL to the terms and conditions for the business or organization.
            age_gated_content: Indicates if the content is age gated.
            external_reference_id: A legally recognized business registration number.
            opt_in_keywords: List of keywords that users can text in to opt in to receive messages.
            vetting_id: Unique identifier for the created Vetting .
            vetting_provider: Name of the vetting provider.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_compliance_tollfree_inquiry(
            tollfree_phone_number,
            notification_email,
            customer_profile_sid=customer_profile_sid,
            business_name=business_name,
            business_website=business_website,
            use_case_categories=use_case_categories,
            use_case_summary=use_case_summary,
            production_message_sample=production_message_sample,
            opt_in_image_urls=opt_in_image_urls,
            opt_in_type=opt_in_type,
            message_volume=message_volume,
            business_street_address=business_street_address,
            business_street_address2=business_street_address2,
            business_city=business_city,
            business_state_province_region=business_state_province_region,
            business_postal_code=business_postal_code,
            business_country=business_country,
            additional_information=additional_information,
            business_contact_first_name=business_contact_first_name,
            business_contact_last_name=business_contact_last_name,
            business_contact_email=business_contact_email,
            business_contact_phone=business_contact_phone,
            theme_set_id=theme_set_id,
            skip_messaging_use_case=skip_messaging_use_case,
            business_registration_number=business_registration_number,
            business_registration_authority=business_registration_authority,
            business_registration_country=business_registration_country,
            business_type=business_type,
            doing_business_as=doing_business_as,
            opt_in_confirmation_message=opt_in_confirmation_message,
            help_message_sample=help_message_sample,
            privacy_policy_url=privacy_policy_url,
            terms_and_conditions_url=terms_and_conditions_url,
            age_gated_content=age_gated_content,
            external_reference_id=external_reference_id,
            opt_in_keywords=opt_in_keywords,
            vetting_id=vetting_id,
            vetting_provider=vetting_provider,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> TrusthubV1ComplianceTollfreeInquiriesWithRawResponse:
        return self._with_raw_response


class AsyncTrusthubV1ComplianceTollfreeInquiries:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTrusthubV1ComplianceTollfreeInquiriesWithRawResponse(client, server, auth)

    async def create_compliance_tollfree_inquiry(
        self,
        tollfree_phone_number: str,
        notification_email: str,
        *,
        customer_profile_sid: str | None = None,
        business_name: str | None = None,
        business_website: str | None = None,
        use_case_categories: list[str] | None = None,
        use_case_summary: str | None = None,
        production_message_sample: str | None = None,
        opt_in_image_urls: list[str] | None = None,
        opt_in_type: ComplianceTollfreeInquiryEnumOptInTypeOrStr | None = None,
        message_volume: str | None = None,
        business_street_address: str | None = None,
        business_street_address2: str | None = None,
        business_city: str | None = None,
        business_state_province_region: str | None = None,
        business_postal_code: str | None = None,
        business_country: str | None = None,
        additional_information: str | None = None,
        business_contact_first_name: str | None = None,
        business_contact_last_name: str | None = None,
        business_contact_email: str | None = None,
        business_contact_phone: str | None = None,
        theme_set_id: str | None = None,
        skip_messaging_use_case: bool | None = None,
        business_registration_number: str | None = None,
        business_registration_authority: str | None = None,
        business_registration_country: str | None = None,
        business_type: TollfreeVerificationEnumBusinessTypeOrStr | None = None,
        doing_business_as: str | None = None,
        opt_in_confirmation_message: str | None = None,
        help_message_sample: str | None = None,
        privacy_policy_url: str | None = None,
        terms_and_conditions_url: str | None = None,
        age_gated_content: bool | None = None,
        external_reference_id: str | None = None,
        opt_in_keywords: list[str] | None = None,
        vetting_id: str | None = None,
        vetting_provider: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TrusthubV1ComplianceTollfreeInquiry:
        """Create a new Compliance Tollfree Verification Inquiry for the authenticated account. This is necessary to
        start a new embedded session.

        Args:
            tollfree_phone_number: The Tollfree phone number to be verified
            notification_email: The email address to receive the notification about the verification result.
            customer_profile_sid: The Customer Profile Sid associated with the Account.
            business_name: The name of the business or organization using the Tollfree number.
            business_website: The website of the business or organization using the Tollfree number.
            use_case_categories: The category of the use case for the Tollfree Number. List as many are applicable..
            use_case_summary: Use this to further explain how messaging is used by the business or organization.
            production_message_sample: An example of message content, i.e. a sample message.
            opt_in_image_urls: Link to an image that shows the opt-in workflow. Multiple images allowed and must be a
                publicly hosted URL.
            opt_in_type: Describe how a user opts-in to text messages.
            message_volume: Estimate monthly volume of messages from the Tollfree Number.
            business_street_address: The address of the business or organization using the Tollfree number.
            business_street_address2: The address of the business or organization using the Tollfree number.
            business_city: The city of the business or organization using the Tollfree number.
            business_state_province_region: The state/province/region of the business or organization using the Tollfree
                number.
            business_postal_code: The postal code of the business or organization using the Tollfree number.
            business_country: The country of the business or organization using the Tollfree number.
            additional_information: Additional information to be provided for verification.
            business_contact_first_name: The first name of the contact for the business or organization using the
                Tollfree number.
            business_contact_last_name: The last name of the contact for the business or organization using the Tollfree
                number.
            business_contact_email: The email address of the contact for the business or organization using the Tollfree
                number.
            business_contact_phone: The phone number of the contact for the business or organization using the Tollfree
                number.
            theme_set_id: Theme id for styling the inquiry form.
            skip_messaging_use_case: Skip the messaging use case screen of the inquiry form.
            business_registration_number: The Business Registration Number of the business or organization.
            business_registration_authority: The Business Registration Authority of the business or organization.
            business_registration_country: The Business Registration Country of the business or organization.
            business_type: Type of Business.
            doing_business_as: Trade name, sub entity, or downstream business name of business being submitted for
                verification.
            opt_in_confirmation_message: The confirmation message sent to users when they opt in to receive messages.
            help_message_sample: A sample help message provided to users.
            privacy_policy_url: The URL to the privacy policy for the business or organization.
            terms_and_conditions_url: The URL to the terms and conditions for the business or organization.
            age_gated_content: Indicates if the content is age gated.
            external_reference_id: A legally recognized business registration number.
            opt_in_keywords: List of keywords that users can text in to opt in to receive messages.
            vetting_id: Unique identifier for the created Vetting .
            vetting_provider: Name of the vetting provider.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_compliance_tollfree_inquiry(
                tollfree_phone_number,
                notification_email,
                customer_profile_sid=customer_profile_sid,
                business_name=business_name,
                business_website=business_website,
                use_case_categories=use_case_categories,
                use_case_summary=use_case_summary,
                production_message_sample=production_message_sample,
                opt_in_image_urls=opt_in_image_urls,
                opt_in_type=opt_in_type,
                message_volume=message_volume,
                business_street_address=business_street_address,
                business_street_address2=business_street_address2,
                business_city=business_city,
                business_state_province_region=business_state_province_region,
                business_postal_code=business_postal_code,
                business_country=business_country,
                additional_information=additional_information,
                business_contact_first_name=business_contact_first_name,
                business_contact_last_name=business_contact_last_name,
                business_contact_email=business_contact_email,
                business_contact_phone=business_contact_phone,
                theme_set_id=theme_set_id,
                skip_messaging_use_case=skip_messaging_use_case,
                business_registration_number=business_registration_number,
                business_registration_authority=business_registration_authority,
                business_registration_country=business_registration_country,
                business_type=business_type,
                doing_business_as=doing_business_as,
                opt_in_confirmation_message=opt_in_confirmation_message,
                help_message_sample=help_message_sample,
                privacy_policy_url=privacy_policy_url,
                terms_and_conditions_url=terms_and_conditions_url,
                age_gated_content=age_gated_content,
                external_reference_id=external_reference_id,
                opt_in_keywords=opt_in_keywords,
                vetting_id=vetting_id,
                vetting_provider=vetting_provider,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTrusthubV1ComplianceTollfreeInquiriesWithRawResponse:
        return self._with_raw_response


class TrusthubV1ComplianceTollfreeInquiriesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_compliance_tollfree_inquiry(
        self,
        tollfree_phone_number: str,
        notification_email: str,
        *,
        customer_profile_sid: str | None = None,
        business_name: str | None = None,
        business_website: str | None = None,
        use_case_categories: list[str] | None = None,
        use_case_summary: str | None = None,
        production_message_sample: str | None = None,
        opt_in_image_urls: list[str] | None = None,
        opt_in_type: ComplianceTollfreeInquiryEnumOptInTypeOrStr | None = None,
        message_volume: str | None = None,
        business_street_address: str | None = None,
        business_street_address2: str | None = None,
        business_city: str | None = None,
        business_state_province_region: str | None = None,
        business_postal_code: str | None = None,
        business_country: str | None = None,
        additional_information: str | None = None,
        business_contact_first_name: str | None = None,
        business_contact_last_name: str | None = None,
        business_contact_email: str | None = None,
        business_contact_phone: str | None = None,
        theme_set_id: str | None = None,
        skip_messaging_use_case: bool | None = None,
        business_registration_number: str | None = None,
        business_registration_authority: str | None = None,
        business_registration_country: str | None = None,
        business_type: TollfreeVerificationEnumBusinessTypeOrStr | None = None,
        doing_business_as: str | None = None,
        opt_in_confirmation_message: str | None = None,
        help_message_sample: str | None = None,
        privacy_policy_url: str | None = None,
        terms_and_conditions_url: str | None = None,
        age_gated_content: bool | None = None,
        external_reference_id: str | None = None,
        opt_in_keywords: list[str] | None = None,
        vetting_id: str | None = None,
        vetting_provider: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TrusthubV1ComplianceTollfreeInquiry, RawError]:
        """Create a new Compliance Tollfree Verification Inquiry for the authenticated account. This is necessary to
        start a new embedded session.

        Args:
            tollfree_phone_number: The Tollfree phone number to be verified
            notification_email: The email address to receive the notification about the verification result.
            customer_profile_sid: The Customer Profile Sid associated with the Account.
            business_name: The name of the business or organization using the Tollfree number.
            business_website: The website of the business or organization using the Tollfree number.
            use_case_categories: The category of the use case for the Tollfree Number. List as many are applicable..
            use_case_summary: Use this to further explain how messaging is used by the business or organization.
            production_message_sample: An example of message content, i.e. a sample message.
            opt_in_image_urls: Link to an image that shows the opt-in workflow. Multiple images allowed and must be a
                publicly hosted URL.
            opt_in_type: Describe how a user opts-in to text messages.
            message_volume: Estimate monthly volume of messages from the Tollfree Number.
            business_street_address: The address of the business or organization using the Tollfree number.
            business_street_address2: The address of the business or organization using the Tollfree number.
            business_city: The city of the business or organization using the Tollfree number.
            business_state_province_region: The state/province/region of the business or organization using the Tollfree
                number.
            business_postal_code: The postal code of the business or organization using the Tollfree number.
            business_country: The country of the business or organization using the Tollfree number.
            additional_information: Additional information to be provided for verification.
            business_contact_first_name: The first name of the contact for the business or organization using the
                Tollfree number.
            business_contact_last_name: The last name of the contact for the business or organization using the Tollfree
                number.
            business_contact_email: The email address of the contact for the business or organization using the Tollfree
                number.
            business_contact_phone: The phone number of the contact for the business or organization using the Tollfree
                number.
            theme_set_id: Theme id for styling the inquiry form.
            skip_messaging_use_case: Skip the messaging use case screen of the inquiry form.
            business_registration_number: The Business Registration Number of the business or organization.
            business_registration_authority: The Business Registration Authority of the business or organization.
            business_registration_country: The Business Registration Country of the business or organization.
            business_type: Type of Business.
            doing_business_as: Trade name, sub entity, or downstream business name of business being submitted for
                verification.
            opt_in_confirmation_message: The confirmation message sent to users when they opt in to receive messages.
            help_message_sample: A sample help message provided to users.
            privacy_policy_url: The URL to the privacy policy for the business or organization.
            terms_and_conditions_url: The URL to the terms and conditions for the business or organization.
            age_gated_content: Indicates if the content is age gated.
            external_reference_id: A legally recognized business registration number.
            opt_in_keywords: List of keywords that users can text in to opt in to receive messages.
            vetting_id: Unique identifier for the created Vetting .
            vetting_provider: Name of the vetting provider.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/v1/ComplianceInquiries/Tollfree/Initialize"),
            body=form_body(
                [
                    param[str]("TollfreePhoneNumber", tollfree_phone_number),
                    param[str]("NotificationEmail", notification_email),
                    param[str | None]("CustomerProfileSid", customer_profile_sid),
                    param[str | None]("BusinessName", business_name),
                    param[str | None]("BusinessWebsite", business_website),
                    param[list[str] | None]("UseCaseCategories", use_case_categories),
                    param[str | None]("UseCaseSummary", use_case_summary),
                    param[str | None]("ProductionMessageSample", production_message_sample),
                    param[list[str] | None]("OptInImageUrls", opt_in_image_urls),
                    param[ComplianceTollfreeInquiryEnumOptInTypeOrStr | None]("OptInType", opt_in_type),
                    param[str | None]("MessageVolume", message_volume),
                    param[str | None]("BusinessStreetAddress", business_street_address),
                    param[str | None]("BusinessStreetAddress2", business_street_address2),
                    param[str | None]("BusinessCity", business_city),
                    param[str | None]("BusinessStateProvinceRegion", business_state_province_region),
                    param[str | None]("BusinessPostalCode", business_postal_code),
                    param[str | None]("BusinessCountry", business_country),
                    param[str | None]("AdditionalInformation", additional_information),
                    param[str | None]("BusinessContactFirstName", business_contact_first_name),
                    param[str | None]("BusinessContactLastName", business_contact_last_name),
                    param[str | None]("BusinessContactEmail", business_contact_email),
                    param[str | None]("BusinessContactPhone", business_contact_phone),
                    param[str | None]("ThemeSetId", theme_set_id),
                    param[bool | None]("SkipMessagingUseCase", skip_messaging_use_case),
                    param[str | None]("BusinessRegistrationNumber", business_registration_number),
                    param[str | None]("BusinessRegistrationAuthority", business_registration_authority),
                    param[str | None]("BusinessRegistrationCountry", business_registration_country),
                    param[TollfreeVerificationEnumBusinessTypeOrStr | None]("BusinessType", business_type),
                    param[str | None]("DoingBusinessAs", doing_business_as),
                    param[str | None]("OptInConfirmationMessage", opt_in_confirmation_message),
                    param[str | None]("HelpMessageSample", help_message_sample),
                    param[str | None]("PrivacyPolicyUrl", privacy_policy_url),
                    param[str | None]("TermsAndConditionsUrl", terms_and_conditions_url),
                    param[bool | None]("AgeGatedContent", age_gated_content),
                    param[str | None]("ExternalReferenceId", external_reference_id),
                    param[list[str] | None]("OptInKeywords", opt_in_keywords),
                    param[str | None]("VettingId", vetting_id),
                    param[str | None]("VettingProvider", vetting_provider),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1ComplianceTollfreeInquiry],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTrusthubV1ComplianceTollfreeInquiriesWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def create_compliance_tollfree_inquiry(
        self,
        tollfree_phone_number: str,
        notification_email: str,
        *,
        customer_profile_sid: str | None = None,
        business_name: str | None = None,
        business_website: str | None = None,
        use_case_categories: list[str] | None = None,
        use_case_summary: str | None = None,
        production_message_sample: str | None = None,
        opt_in_image_urls: list[str] | None = None,
        opt_in_type: ComplianceTollfreeInquiryEnumOptInTypeOrStr | None = None,
        message_volume: str | None = None,
        business_street_address: str | None = None,
        business_street_address2: str | None = None,
        business_city: str | None = None,
        business_state_province_region: str | None = None,
        business_postal_code: str | None = None,
        business_country: str | None = None,
        additional_information: str | None = None,
        business_contact_first_name: str | None = None,
        business_contact_last_name: str | None = None,
        business_contact_email: str | None = None,
        business_contact_phone: str | None = None,
        theme_set_id: str | None = None,
        skip_messaging_use_case: bool | None = None,
        business_registration_number: str | None = None,
        business_registration_authority: str | None = None,
        business_registration_country: str | None = None,
        business_type: TollfreeVerificationEnumBusinessTypeOrStr | None = None,
        doing_business_as: str | None = None,
        opt_in_confirmation_message: str | None = None,
        help_message_sample: str | None = None,
        privacy_policy_url: str | None = None,
        terms_and_conditions_url: str | None = None,
        age_gated_content: bool | None = None,
        external_reference_id: str | None = None,
        opt_in_keywords: list[str] | None = None,
        vetting_id: str | None = None,
        vetting_provider: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TrusthubV1ComplianceTollfreeInquiry, RawError]:
        """Create a new Compliance Tollfree Verification Inquiry for the authenticated account. This is necessary to
        start a new embedded session.

        Args:
            tollfree_phone_number: The Tollfree phone number to be verified
            notification_email: The email address to receive the notification about the verification result.
            customer_profile_sid: The Customer Profile Sid associated with the Account.
            business_name: The name of the business or organization using the Tollfree number.
            business_website: The website of the business or organization using the Tollfree number.
            use_case_categories: The category of the use case for the Tollfree Number. List as many are applicable..
            use_case_summary: Use this to further explain how messaging is used by the business or organization.
            production_message_sample: An example of message content, i.e. a sample message.
            opt_in_image_urls: Link to an image that shows the opt-in workflow. Multiple images allowed and must be a
                publicly hosted URL.
            opt_in_type: Describe how a user opts-in to text messages.
            message_volume: Estimate monthly volume of messages from the Tollfree Number.
            business_street_address: The address of the business or organization using the Tollfree number.
            business_street_address2: The address of the business or organization using the Tollfree number.
            business_city: The city of the business or organization using the Tollfree number.
            business_state_province_region: The state/province/region of the business or organization using the Tollfree
                number.
            business_postal_code: The postal code of the business or organization using the Tollfree number.
            business_country: The country of the business or organization using the Tollfree number.
            additional_information: Additional information to be provided for verification.
            business_contact_first_name: The first name of the contact for the business or organization using the
                Tollfree number.
            business_contact_last_name: The last name of the contact for the business or organization using the Tollfree
                number.
            business_contact_email: The email address of the contact for the business or organization using the Tollfree
                number.
            business_contact_phone: The phone number of the contact for the business or organization using the Tollfree
                number.
            theme_set_id: Theme id for styling the inquiry form.
            skip_messaging_use_case: Skip the messaging use case screen of the inquiry form.
            business_registration_number: The Business Registration Number of the business or organization.
            business_registration_authority: The Business Registration Authority of the business or organization.
            business_registration_country: The Business Registration Country of the business or organization.
            business_type: Type of Business.
            doing_business_as: Trade name, sub entity, or downstream business name of business being submitted for
                verification.
            opt_in_confirmation_message: The confirmation message sent to users when they opt in to receive messages.
            help_message_sample: A sample help message provided to users.
            privacy_policy_url: The URL to the privacy policy for the business or organization.
            terms_and_conditions_url: The URL to the terms and conditions for the business or organization.
            age_gated_content: Indicates if the content is age gated.
            external_reference_id: A legally recognized business registration number.
            opt_in_keywords: List of keywords that users can text in to opt in to receive messages.
            vetting_id: Unique identifier for the created Vetting .
            vetting_provider: Name of the vetting provider.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/v1/ComplianceInquiries/Tollfree/Initialize"),
            body=form_body(
                [
                    param[str]("TollfreePhoneNumber", tollfree_phone_number),
                    param[str]("NotificationEmail", notification_email),
                    param[str | None]("CustomerProfileSid", customer_profile_sid),
                    param[str | None]("BusinessName", business_name),
                    param[str | None]("BusinessWebsite", business_website),
                    param[list[str] | None]("UseCaseCategories", use_case_categories),
                    param[str | None]("UseCaseSummary", use_case_summary),
                    param[str | None]("ProductionMessageSample", production_message_sample),
                    param[list[str] | None]("OptInImageUrls", opt_in_image_urls),
                    param[ComplianceTollfreeInquiryEnumOptInTypeOrStr | None]("OptInType", opt_in_type),
                    param[str | None]("MessageVolume", message_volume),
                    param[str | None]("BusinessStreetAddress", business_street_address),
                    param[str | None]("BusinessStreetAddress2", business_street_address2),
                    param[str | None]("BusinessCity", business_city),
                    param[str | None]("BusinessStateProvinceRegion", business_state_province_region),
                    param[str | None]("BusinessPostalCode", business_postal_code),
                    param[str | None]("BusinessCountry", business_country),
                    param[str | None]("AdditionalInformation", additional_information),
                    param[str | None]("BusinessContactFirstName", business_contact_first_name),
                    param[str | None]("BusinessContactLastName", business_contact_last_name),
                    param[str | None]("BusinessContactEmail", business_contact_email),
                    param[str | None]("BusinessContactPhone", business_contact_phone),
                    param[str | None]("ThemeSetId", theme_set_id),
                    param[bool | None]("SkipMessagingUseCase", skip_messaging_use_case),
                    param[str | None]("BusinessRegistrationNumber", business_registration_number),
                    param[str | None]("BusinessRegistrationAuthority", business_registration_authority),
                    param[str | None]("BusinessRegistrationCountry", business_registration_country),
                    param[TollfreeVerificationEnumBusinessTypeOrStr | None]("BusinessType", business_type),
                    param[str | None]("DoingBusinessAs", doing_business_as),
                    param[str | None]("OptInConfirmationMessage", opt_in_confirmation_message),
                    param[str | None]("HelpMessageSample", help_message_sample),
                    param[str | None]("PrivacyPolicyUrl", privacy_policy_url),
                    param[str | None]("TermsAndConditionsUrl", terms_and_conditions_url),
                    param[bool | None]("AgeGatedContent", age_gated_content),
                    param[str | None]("ExternalReferenceId", external_reference_id),
                    param[list[str] | None]("OptInKeywords", opt_in_keywords),
                    param[str | None]("VettingId", vetting_id),
                    param[str | None]("VettingProvider", vetting_provider),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1ComplianceTollfreeInquiry],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
