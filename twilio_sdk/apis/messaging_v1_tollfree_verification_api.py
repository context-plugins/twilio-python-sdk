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
from ..models.enums.tollfree_verification_enum_business_registration_authority import (
    TollfreeVerificationEnumBusinessRegistrationAuthorityOrStr,
)
from ..models.enums.tollfree_verification_enum_business_type import TollfreeVerificationEnumBusinessTypeOrStr
from ..models.enums.tollfree_verification_enum_opt_in_type import TollfreeVerificationEnumOptInTypeOrStr
from ..models.enums.tollfree_verification_enum_status import TollfreeVerificationEnumStatusOrStr
from ..models.enums.tollfree_verification_enum_use_case_category import TollfreeVerificationEnumUseCaseCategoryOrStr
from ..models.enums.tollfree_verification_enum_vetting_provider import TollfreeVerificationEnumVettingProviderOrStr
from ..models.list_tollfree_verification_response import ListTollfreeVerificationResponse
from ..models.messaging_v1_tollfree_verification import MessagingV1TollfreeVerification
from ..server.server import Server


class MessagingV1TollfreeVerificationApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MessagingV1TollfreeVerificationApiWithRawResponse(client, server, auth)

    def create_tollfree_verification(
        self,
        business_name: str,
        business_website: str,
        notification_email: str,
        use_case_categories: list[TollfreeVerificationEnumUseCaseCategoryOrStr | None],
        use_case_summary: str,
        production_message_sample: str,
        opt_in_image_urls: list[str],
        opt_in_type: TollfreeVerificationEnumOptInTypeOrStr,
        message_volume: str,
        tollfree_phone_number_sid: str,
        *,
        customer_profile_sid: str | None = None,
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
        external_reference_id: str | None = None,
        business_registration_number: str | None = None,
        business_registration_authority: TollfreeVerificationEnumBusinessRegistrationAuthorityOrStr | None = None,
        business_registration_country: str | None = None,
        business_type: TollfreeVerificationEnumBusinessTypeOrStr | None = None,
        business_registration_phone_number: str | None = None,
        doing_business_as: str | None = None,
        opt_in_confirmation_message: str | None = None,
        help_message_sample: str | None = None,
        privacy_policy_url: str | None = None,
        terms_and_conditions_url: str | None = None,
        age_gated_content: bool | None = None,
        opt_in_keywords: list[str] | None = None,
        vetting_provider: TollfreeVerificationEnumVettingProviderOrStr | None = None,
        vetting_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MessagingV1TollfreeVerification:
        """Create a tollfree verification

        Args:
            business_name: The name of the business or organization using the Tollfree number.
            business_website: The website of the business or organization using the Tollfree number.
            notification_email: The email address to receive the notification about the verification result. .
            use_case_categories: The category of the use case for the Tollfree Number. List as many as are applicable.
            use_case_summary: Use this to further explain how messaging is used by the business or organization.
            production_message_sample: An example of message content, i.e. a sample message.
            opt_in_image_urls: Link to an image that shows the opt-in workflow. Multiple images allowed and must be a
                publicly hosted URL.
            opt_in_type: Describe how a user opts-in to text messages.
            message_volume: Estimate monthly volume of messages from the Tollfree Number.
            tollfree_phone_number_sid: The SID of the Phone Number associated with the Tollfree Verification.
            customer_profile_sid: Customer's Profile Bundle BundleSid.
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
            business_contact_phone: The E.164 formatted phone number of the contact for the business or organization
                using the Tollfree number.
            external_reference_id: An optional external reference ID supplied by customer and echoed back on status
                retrieval.
            business_registration_number: A legally recognized business registration number. Required for all business
                types except SOLE_PROPRIETOR.
            business_registration_authority: The organizational authority for business registrations. Required for all
                business types except SOLE_PROPRIETOR.
            business_registration_country: The country where the business is registered. Required for all business types
                except SOLE_PROPRIETOR.
            business_type: The type of business, valid values are PRIVATE_PROFIT, PUBLIC_PROFIT, NON_PROFIT,
                SOLE_PROPRIETOR, GOVERNMENT. Required field.
            business_registration_phone_number: The E.164 formatted number associated with the business.
            doing_business_as: Trade name, sub entity, or downstream business name of business being submitted for
                verification
            opt_in_confirmation_message: The confirmation message sent to users when they opt in to receive messages.
            help_message_sample: A sample help message provided to users.
            privacy_policy_url: The URL to the privacy policy for the business or organization.
            terms_and_conditions_url: The URL to the terms and conditions for the business or organization.
            age_gated_content: Indicates if the content is age gated.
            opt_in_keywords: List of keywords that users can text in to opt in to receive messages.
            vetting_provider: The third-party political vetting provider.
            vetting_id: The unique ID of the vetting
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_tollfree_verification(
            business_name,
            business_website,
            notification_email,
            use_case_categories,
            use_case_summary,
            production_message_sample,
            opt_in_image_urls,
            opt_in_type,
            message_volume,
            tollfree_phone_number_sid,
            customer_profile_sid=customer_profile_sid,
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
            external_reference_id=external_reference_id,
            business_registration_number=business_registration_number,
            business_registration_authority=business_registration_authority,
            business_registration_country=business_registration_country,
            business_type=business_type,
            business_registration_phone_number=business_registration_phone_number,
            doing_business_as=doing_business_as,
            opt_in_confirmation_message=opt_in_confirmation_message,
            help_message_sample=help_message_sample,
            privacy_policy_url=privacy_policy_url,
            terms_and_conditions_url=terms_and_conditions_url,
            age_gated_content=age_gated_content,
            opt_in_keywords=opt_in_keywords,
            vetting_provider=vetting_provider,
            vetting_id=vetting_id,
            request_options=request_options,
        ).unwrap()

    def delete_tollfree_verification(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Delete a tollfree verification

        Args:
            sid: The unique string to identify Tollfree Verification.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_tollfree_verification(sid, request_options=request_options).unwrap()

    def fetch_tollfree_verification(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MessagingV1TollfreeVerification:
        """Retrieve a tollfree verification

        Args:
            sid: A unique string identifying a Tollfree Verification.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_tollfree_verification(sid, request_options=request_options).unwrap()

    def list_tollfree_verification(
        self,
        *,
        tollfree_phone_number_sid: str | None = None,
        status: TollfreeVerificationEnumStatusOrStr | None = None,
        external_reference_id: str | None = None,
        include_sub_accounts: bool | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        trust_product_sid: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListTollfreeVerificationResponse:
        """List tollfree verifications

        Args:
            tollfree_phone_number_sid: The SID of the Phone Number associated with the Tollfree Verification.
            status: The compliance status of the Tollfree Verification record.
            external_reference_id: Customer supplied reference id for the Tollfree Verification record.
            include_sub_accounts: Whether to include Tollfree Verifications from sub accounts in list response.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            trust_product_sid: The trust product sids / tollfree bundle sids of tollfree verifications
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_tollfree_verification(
            tollfree_phone_number_sid=tollfree_phone_number_sid,
            status=status,
            external_reference_id=external_reference_id,
            include_sub_accounts=include_sub_accounts,
            page_size=page_size,
            page=page,
            page_token=page_token,
            trust_product_sid=trust_product_sid,
            request_options=request_options,
        ).unwrap()

    def update_tollfree_verification(
        self,
        sid: str,
        *,
        business_name: str | None = None,
        business_website: str | None = None,
        notification_email: str | None = None,
        use_case_categories: list[TollfreeVerificationEnumUseCaseCategoryOrStr | None] | None = None,
        use_case_summary: str | None = None,
        production_message_sample: str | None = None,
        opt_in_image_urls: list[str] | None = None,
        opt_in_type: TollfreeVerificationEnumOptInTypeOrStr | None = None,
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
        edit_reason: str | None = None,
        business_registration_number: str | None = None,
        business_registration_authority: TollfreeVerificationEnumBusinessRegistrationAuthorityOrStr | None = None,
        business_registration_country: str | None = None,
        business_type: TollfreeVerificationEnumBusinessTypeOrStr | None = None,
        business_registration_phone_number: str | None = None,
        doing_business_as: str | None = None,
        opt_in_confirmation_message: str | None = None,
        help_message_sample: str | None = None,
        privacy_policy_url: str | None = None,
        terms_and_conditions_url: str | None = None,
        age_gated_content: bool | None = None,
        opt_in_keywords: list[str] | None = None,
        vetting_provider: TollfreeVerificationEnumVettingProviderOrStr | None = None,
        vetting_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MessagingV1TollfreeVerification:
        """Edit a tollfree verification

        Args:
            sid: The unique string to identify Tollfree Verification.
            business_name: The name of the business or organization using the Tollfree number.
            business_website: The website of the business or organization using the Tollfree number.
            notification_email: The email address to receive the notification about the verification result. .
            use_case_categories: The category of the use case for the Tollfree Number. List as many as are applicable.
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
            business_contact_phone: The E.164 formatted phone number of the contact for the business or organization
                using the Tollfree number.
            edit_reason: Describe why the verification is being edited. If the verification was rejected because of a
                technical issue, such as the website being down, and the issue has been resolved this parameter should
                be set to something similar to 'Website fixed'.
            business_registration_number: A legally recognized business registration number
            business_registration_authority: The organizational authority for business registrations. Required for all
                business types except SOLE_PROPRIETOR.
            business_registration_country: Country business is registered in
            business_type: The type of business, valid values are PRIVATE_PROFIT, PUBLIC_PROFIT, NON_PROFIT,
                SOLE_PROPRIETOR, GOVERNMENT. Required field.
            business_registration_phone_number: The E.164 formatted number associated with the business.
            doing_business_as: Trade name, sub entity, or downstream business name of business being submitted for
                verification
            opt_in_confirmation_message: The confirmation message sent to users when they opt in to receive messages.
            help_message_sample: A sample help message provided to users.
            privacy_policy_url: The URL to the privacy policy for the business or organization.
            terms_and_conditions_url: The URL to the terms and conditions for the business or organization.
            age_gated_content: Indicates if the content is age gated.
            opt_in_keywords: List of keywords that users can text in to opt in to receive messages.
            vetting_provider: The third-party political vetting provider.
            vetting_id: The unique ID of the vetting
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Accepted

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_tollfree_verification(
            sid,
            business_name=business_name,
            business_website=business_website,
            notification_email=notification_email,
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
            edit_reason=edit_reason,
            business_registration_number=business_registration_number,
            business_registration_authority=business_registration_authority,
            business_registration_country=business_registration_country,
            business_type=business_type,
            business_registration_phone_number=business_registration_phone_number,
            doing_business_as=doing_business_as,
            opt_in_confirmation_message=opt_in_confirmation_message,
            help_message_sample=help_message_sample,
            privacy_policy_url=privacy_policy_url,
            terms_and_conditions_url=terms_and_conditions_url,
            age_gated_content=age_gated_content,
            opt_in_keywords=opt_in_keywords,
            vetting_provider=vetting_provider,
            vetting_id=vetting_id,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> MessagingV1TollfreeVerificationApiWithRawResponse:
        return self._with_raw_response


class AsyncMessagingV1TollfreeVerificationApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMessagingV1TollfreeVerificationApiWithRawResponse(client, server, auth)

    async def create_tollfree_verification(
        self,
        business_name: str,
        business_website: str,
        notification_email: str,
        use_case_categories: list[TollfreeVerificationEnumUseCaseCategoryOrStr | None],
        use_case_summary: str,
        production_message_sample: str,
        opt_in_image_urls: list[str],
        opt_in_type: TollfreeVerificationEnumOptInTypeOrStr,
        message_volume: str,
        tollfree_phone_number_sid: str,
        *,
        customer_profile_sid: str | None = None,
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
        external_reference_id: str | None = None,
        business_registration_number: str | None = None,
        business_registration_authority: TollfreeVerificationEnumBusinessRegistrationAuthorityOrStr | None = None,
        business_registration_country: str | None = None,
        business_type: TollfreeVerificationEnumBusinessTypeOrStr | None = None,
        business_registration_phone_number: str | None = None,
        doing_business_as: str | None = None,
        opt_in_confirmation_message: str | None = None,
        help_message_sample: str | None = None,
        privacy_policy_url: str | None = None,
        terms_and_conditions_url: str | None = None,
        age_gated_content: bool | None = None,
        opt_in_keywords: list[str] | None = None,
        vetting_provider: TollfreeVerificationEnumVettingProviderOrStr | None = None,
        vetting_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MessagingV1TollfreeVerification:
        """Create a tollfree verification

        Args:
            business_name: The name of the business or organization using the Tollfree number.
            business_website: The website of the business or organization using the Tollfree number.
            notification_email: The email address to receive the notification about the verification result. .
            use_case_categories: The category of the use case for the Tollfree Number. List as many as are applicable.
            use_case_summary: Use this to further explain how messaging is used by the business or organization.
            production_message_sample: An example of message content, i.e. a sample message.
            opt_in_image_urls: Link to an image that shows the opt-in workflow. Multiple images allowed and must be a
                publicly hosted URL.
            opt_in_type: Describe how a user opts-in to text messages.
            message_volume: Estimate monthly volume of messages from the Tollfree Number.
            tollfree_phone_number_sid: The SID of the Phone Number associated with the Tollfree Verification.
            customer_profile_sid: Customer's Profile Bundle BundleSid.
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
            business_contact_phone: The E.164 formatted phone number of the contact for the business or organization
                using the Tollfree number.
            external_reference_id: An optional external reference ID supplied by customer and echoed back on status
                retrieval.
            business_registration_number: A legally recognized business registration number. Required for all business
                types except SOLE_PROPRIETOR.
            business_registration_authority: The organizational authority for business registrations. Required for all
                business types except SOLE_PROPRIETOR.
            business_registration_country: The country where the business is registered. Required for all business types
                except SOLE_PROPRIETOR.
            business_type: The type of business, valid values are PRIVATE_PROFIT, PUBLIC_PROFIT, NON_PROFIT,
                SOLE_PROPRIETOR, GOVERNMENT. Required field.
            business_registration_phone_number: The E.164 formatted number associated with the business.
            doing_business_as: Trade name, sub entity, or downstream business name of business being submitted for
                verification
            opt_in_confirmation_message: The confirmation message sent to users when they opt in to receive messages.
            help_message_sample: A sample help message provided to users.
            privacy_policy_url: The URL to the privacy policy for the business or organization.
            terms_and_conditions_url: The URL to the terms and conditions for the business or organization.
            age_gated_content: Indicates if the content is age gated.
            opt_in_keywords: List of keywords that users can text in to opt in to receive messages.
            vetting_provider: The third-party political vetting provider.
            vetting_id: The unique ID of the vetting
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_tollfree_verification(
                business_name,
                business_website,
                notification_email,
                use_case_categories,
                use_case_summary,
                production_message_sample,
                opt_in_image_urls,
                opt_in_type,
                message_volume,
                tollfree_phone_number_sid,
                customer_profile_sid=customer_profile_sid,
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
                external_reference_id=external_reference_id,
                business_registration_number=business_registration_number,
                business_registration_authority=business_registration_authority,
                business_registration_country=business_registration_country,
                business_type=business_type,
                business_registration_phone_number=business_registration_phone_number,
                doing_business_as=doing_business_as,
                opt_in_confirmation_message=opt_in_confirmation_message,
                help_message_sample=help_message_sample,
                privacy_policy_url=privacy_policy_url,
                terms_and_conditions_url=terms_and_conditions_url,
                age_gated_content=age_gated_content,
                opt_in_keywords=opt_in_keywords,
                vetting_provider=vetting_provider,
                vetting_id=vetting_id,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_tollfree_verification(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a tollfree verification

        Args:
            sid: The unique string to identify Tollfree Verification.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_tollfree_verification(sid, request_options=request_options)
        ).unwrap()

    async def fetch_tollfree_verification(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MessagingV1TollfreeVerification:
        """Retrieve a tollfree verification

        Args:
            sid: A unique string identifying a Tollfree Verification.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_tollfree_verification(sid, request_options=request_options)
        ).unwrap()

    async def list_tollfree_verification(
        self,
        *,
        tollfree_phone_number_sid: str | None = None,
        status: TollfreeVerificationEnumStatusOrStr | None = None,
        external_reference_id: str | None = None,
        include_sub_accounts: bool | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        trust_product_sid: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListTollfreeVerificationResponse:
        """List tollfree verifications

        Args:
            tollfree_phone_number_sid: The SID of the Phone Number associated with the Tollfree Verification.
            status: The compliance status of the Tollfree Verification record.
            external_reference_id: Customer supplied reference id for the Tollfree Verification record.
            include_sub_accounts: Whether to include Tollfree Verifications from sub accounts in list response.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            trust_product_sid: The trust product sids / tollfree bundle sids of tollfree verifications
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_tollfree_verification(
                tollfree_phone_number_sid=tollfree_phone_number_sid,
                status=status,
                external_reference_id=external_reference_id,
                include_sub_accounts=include_sub_accounts,
                page_size=page_size,
                page=page,
                page_token=page_token,
                trust_product_sid=trust_product_sid,
                request_options=request_options,
            )
        ).unwrap()

    async def update_tollfree_verification(
        self,
        sid: str,
        *,
        business_name: str | None = None,
        business_website: str | None = None,
        notification_email: str | None = None,
        use_case_categories: list[TollfreeVerificationEnumUseCaseCategoryOrStr | None] | None = None,
        use_case_summary: str | None = None,
        production_message_sample: str | None = None,
        opt_in_image_urls: list[str] | None = None,
        opt_in_type: TollfreeVerificationEnumOptInTypeOrStr | None = None,
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
        edit_reason: str | None = None,
        business_registration_number: str | None = None,
        business_registration_authority: TollfreeVerificationEnumBusinessRegistrationAuthorityOrStr | None = None,
        business_registration_country: str | None = None,
        business_type: TollfreeVerificationEnumBusinessTypeOrStr | None = None,
        business_registration_phone_number: str | None = None,
        doing_business_as: str | None = None,
        opt_in_confirmation_message: str | None = None,
        help_message_sample: str | None = None,
        privacy_policy_url: str | None = None,
        terms_and_conditions_url: str | None = None,
        age_gated_content: bool | None = None,
        opt_in_keywords: list[str] | None = None,
        vetting_provider: TollfreeVerificationEnumVettingProviderOrStr | None = None,
        vetting_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MessagingV1TollfreeVerification:
        """Edit a tollfree verification

        Args:
            sid: The unique string to identify Tollfree Verification.
            business_name: The name of the business or organization using the Tollfree number.
            business_website: The website of the business or organization using the Tollfree number.
            notification_email: The email address to receive the notification about the verification result. .
            use_case_categories: The category of the use case for the Tollfree Number. List as many as are applicable.
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
            business_contact_phone: The E.164 formatted phone number of the contact for the business or organization
                using the Tollfree number.
            edit_reason: Describe why the verification is being edited. If the verification was rejected because of a
                technical issue, such as the website being down, and the issue has been resolved this parameter should
                be set to something similar to 'Website fixed'.
            business_registration_number: A legally recognized business registration number
            business_registration_authority: The organizational authority for business registrations. Required for all
                business types except SOLE_PROPRIETOR.
            business_registration_country: Country business is registered in
            business_type: The type of business, valid values are PRIVATE_PROFIT, PUBLIC_PROFIT, NON_PROFIT,
                SOLE_PROPRIETOR, GOVERNMENT. Required field.
            business_registration_phone_number: The E.164 formatted number associated with the business.
            doing_business_as: Trade name, sub entity, or downstream business name of business being submitted for
                verification
            opt_in_confirmation_message: The confirmation message sent to users when they opt in to receive messages.
            help_message_sample: A sample help message provided to users.
            privacy_policy_url: The URL to the privacy policy for the business or organization.
            terms_and_conditions_url: The URL to the terms and conditions for the business or organization.
            age_gated_content: Indicates if the content is age gated.
            opt_in_keywords: List of keywords that users can text in to opt in to receive messages.
            vetting_provider: The third-party political vetting provider.
            vetting_id: The unique ID of the vetting
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Accepted

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_tollfree_verification(
                sid,
                business_name=business_name,
                business_website=business_website,
                notification_email=notification_email,
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
                edit_reason=edit_reason,
                business_registration_number=business_registration_number,
                business_registration_authority=business_registration_authority,
                business_registration_country=business_registration_country,
                business_type=business_type,
                business_registration_phone_number=business_registration_phone_number,
                doing_business_as=doing_business_as,
                opt_in_confirmation_message=opt_in_confirmation_message,
                help_message_sample=help_message_sample,
                privacy_policy_url=privacy_policy_url,
                terms_and_conditions_url=terms_and_conditions_url,
                age_gated_content=age_gated_content,
                opt_in_keywords=opt_in_keywords,
                vetting_provider=vetting_provider,
                vetting_id=vetting_id,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncMessagingV1TollfreeVerificationApiWithRawResponse:
        return self._with_raw_response


class MessagingV1TollfreeVerificationApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_tollfree_verification(
        self,
        business_name: str,
        business_website: str,
        notification_email: str,
        use_case_categories: list[TollfreeVerificationEnumUseCaseCategoryOrStr | None],
        use_case_summary: str,
        production_message_sample: str,
        opt_in_image_urls: list[str],
        opt_in_type: TollfreeVerificationEnumOptInTypeOrStr,
        message_volume: str,
        tollfree_phone_number_sid: str,
        *,
        customer_profile_sid: str | None = None,
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
        external_reference_id: str | None = None,
        business_registration_number: str | None = None,
        business_registration_authority: TollfreeVerificationEnumBusinessRegistrationAuthorityOrStr | None = None,
        business_registration_country: str | None = None,
        business_type: TollfreeVerificationEnumBusinessTypeOrStr | None = None,
        business_registration_phone_number: str | None = None,
        doing_business_as: str | None = None,
        opt_in_confirmation_message: str | None = None,
        help_message_sample: str | None = None,
        privacy_policy_url: str | None = None,
        terms_and_conditions_url: str | None = None,
        age_gated_content: bool | None = None,
        opt_in_keywords: list[str] | None = None,
        vetting_provider: TollfreeVerificationEnumVettingProviderOrStr | None = None,
        vetting_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MessagingV1TollfreeVerification, RawError]:
        """Create a tollfree verification

        Args:
            business_name: The name of the business or organization using the Tollfree number.
            business_website: The website of the business or organization using the Tollfree number.
            notification_email: The email address to receive the notification about the verification result. .
            use_case_categories: The category of the use case for the Tollfree Number. List as many as are applicable.
            use_case_summary: Use this to further explain how messaging is used by the business or organization.
            production_message_sample: An example of message content, i.e. a sample message.
            opt_in_image_urls: Link to an image that shows the opt-in workflow. Multiple images allowed and must be a
                publicly hosted URL.
            opt_in_type: Describe how a user opts-in to text messages.
            message_volume: Estimate monthly volume of messages from the Tollfree Number.
            tollfree_phone_number_sid: The SID of the Phone Number associated with the Tollfree Verification.
            customer_profile_sid: Customer's Profile Bundle BundleSid.
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
            business_contact_phone: The E.164 formatted phone number of the contact for the business or organization
                using the Tollfree number.
            external_reference_id: An optional external reference ID supplied by customer and echoed back on status
                retrieval.
            business_registration_number: A legally recognized business registration number. Required for all business
                types except SOLE_PROPRIETOR.
            business_registration_authority: The organizational authority for business registrations. Required for all
                business types except SOLE_PROPRIETOR.
            business_registration_country: The country where the business is registered. Required for all business types
                except SOLE_PROPRIETOR.
            business_type: The type of business, valid values are PRIVATE_PROFIT, PUBLIC_PROFIT, NON_PROFIT,
                SOLE_PROPRIETOR, GOVERNMENT. Required field.
            business_registration_phone_number: The E.164 formatted number associated with the business.
            doing_business_as: Trade name, sub entity, or downstream business name of business being submitted for
                verification
            opt_in_confirmation_message: The confirmation message sent to users when they opt in to receive messages.
            help_message_sample: A sample help message provided to users.
            privacy_policy_url: The URL to the privacy policy for the business or organization.
            terms_and_conditions_url: The URL to the terms and conditions for the business or organization.
            age_gated_content: Indicates if the content is age gated.
            opt_in_keywords: List of keywords that users can text in to opt in to receive messages.
            vetting_provider: The third-party political vetting provider.
            vetting_id: The unique ID of the vetting
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v1/Tollfree/Verifications"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("BusinessName", business_name),
                    param[str]("BusinessWebsite", business_website),
                    param[str]("NotificationEmail", notification_email),
                    param[list[TollfreeVerificationEnumUseCaseCategoryOrStr | None]](
                        "UseCaseCategories", use_case_categories
                    ),
                    param[str]("UseCaseSummary", use_case_summary),
                    param[str]("ProductionMessageSample", production_message_sample),
                    param[list[str]]("OptInImageUrls", opt_in_image_urls),
                    param[TollfreeVerificationEnumOptInTypeOrStr]("OptInType", opt_in_type),
                    param[str]("MessageVolume", message_volume),
                    param[str]("TollfreePhoneNumberSid", tollfree_phone_number_sid),
                    param[str | None]("CustomerProfileSid", customer_profile_sid),
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
                    param[str | None]("ExternalReferenceId", external_reference_id),
                    param[str | None]("BusinessRegistrationNumber", business_registration_number),
                    param[TollfreeVerificationEnumBusinessRegistrationAuthorityOrStr | None](
                        "BusinessRegistrationAuthority", business_registration_authority
                    ),
                    param[str | None]("BusinessRegistrationCountry", business_registration_country),
                    param[TollfreeVerificationEnumBusinessTypeOrStr | None]("BusinessType", business_type),
                    param[str | None]("BusinessRegistrationPhoneNumber", business_registration_phone_number),
                    param[str | None]("DoingBusinessAs", doing_business_as),
                    param[str | None]("OptInConfirmationMessage", opt_in_confirmation_message),
                    param[str | None]("HelpMessageSample", help_message_sample),
                    param[str | None]("PrivacyPolicyUrl", privacy_policy_url),
                    param[str | None]("TermsAndConditionsUrl", terms_and_conditions_url),
                    param[bool | None]("AgeGatedContent", age_gated_content),
                    param[list[str] | None]("OptInKeywords", opt_in_keywords),
                    param[TollfreeVerificationEnumVettingProviderOrStr | None]("VettingProvider", vetting_provider),
                    param[str | None]("VettingId", vetting_id),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1TollfreeVerification],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_tollfree_verification(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a tollfree verification

        Args:
            sid: The unique string to identify Tollfree Verification.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default1("/v1/Tollfree/Verifications/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_tollfree_verification(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV1TollfreeVerification, RawError]:
        """Retrieve a tollfree verification

        Args:
            sid: A unique string identifying a Tollfree Verification.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/Tollfree/Verifications/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1TollfreeVerification],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_tollfree_verification(
        self,
        *,
        tollfree_phone_number_sid: str | None = None,
        status: TollfreeVerificationEnumStatusOrStr | None = None,
        external_reference_id: str | None = None,
        include_sub_accounts: bool | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        trust_product_sid: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListTollfreeVerificationResponse, RawError]:
        """List tollfree verifications

        Args:
            tollfree_phone_number_sid: The SID of the Phone Number associated with the Tollfree Verification.
            status: The compliance status of the Tollfree Verification record.
            external_reference_id: Customer supplied reference id for the Tollfree Verification record.
            include_sub_accounts: Whether to include Tollfree Verifications from sub accounts in list response.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            trust_product_sid: The trust product sids / tollfree bundle sids of tollfree verifications
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/Tollfree/Verifications"),
            query_params=[
                param[str | None]("TollfreePhoneNumberSid", tollfree_phone_number_sid),
                param[TollfreeVerificationEnumStatusOrStr | None]("Status", status),
                param[str | None]("ExternalReferenceId", external_reference_id),
                param[bool | None]("IncludeSubAccounts", include_sub_accounts),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
                param[list[str] | None]("TrustProductSid", trust_product_sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListTollfreeVerificationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_tollfree_verification(
        self,
        sid: str,
        *,
        business_name: str | None = None,
        business_website: str | None = None,
        notification_email: str | None = None,
        use_case_categories: list[TollfreeVerificationEnumUseCaseCategoryOrStr | None] | None = None,
        use_case_summary: str | None = None,
        production_message_sample: str | None = None,
        opt_in_image_urls: list[str] | None = None,
        opt_in_type: TollfreeVerificationEnumOptInTypeOrStr | None = None,
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
        edit_reason: str | None = None,
        business_registration_number: str | None = None,
        business_registration_authority: TollfreeVerificationEnumBusinessRegistrationAuthorityOrStr | None = None,
        business_registration_country: str | None = None,
        business_type: TollfreeVerificationEnumBusinessTypeOrStr | None = None,
        business_registration_phone_number: str | None = None,
        doing_business_as: str | None = None,
        opt_in_confirmation_message: str | None = None,
        help_message_sample: str | None = None,
        privacy_policy_url: str | None = None,
        terms_and_conditions_url: str | None = None,
        age_gated_content: bool | None = None,
        opt_in_keywords: list[str] | None = None,
        vetting_provider: TollfreeVerificationEnumVettingProviderOrStr | None = None,
        vetting_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MessagingV1TollfreeVerification, RawError]:
        """Edit a tollfree verification

        Args:
            sid: The unique string to identify Tollfree Verification.
            business_name: The name of the business or organization using the Tollfree number.
            business_website: The website of the business or organization using the Tollfree number.
            notification_email: The email address to receive the notification about the verification result. .
            use_case_categories: The category of the use case for the Tollfree Number. List as many as are applicable.
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
            business_contact_phone: The E.164 formatted phone number of the contact for the business or organization
                using the Tollfree number.
            edit_reason: Describe why the verification is being edited. If the verification was rejected because of a
                technical issue, such as the website being down, and the issue has been resolved this parameter should
                be set to something similar to 'Website fixed'.
            business_registration_number: A legally recognized business registration number
            business_registration_authority: The organizational authority for business registrations. Required for all
                business types except SOLE_PROPRIETOR.
            business_registration_country: Country business is registered in
            business_type: The type of business, valid values are PRIVATE_PROFIT, PUBLIC_PROFIT, NON_PROFIT,
                SOLE_PROPRIETOR, GOVERNMENT. Required field.
            business_registration_phone_number: The E.164 formatted number associated with the business.
            doing_business_as: Trade name, sub entity, or downstream business name of business being submitted for
                verification
            opt_in_confirmation_message: The confirmation message sent to users when they opt in to receive messages.
            help_message_sample: A sample help message provided to users.
            privacy_policy_url: The URL to the privacy policy for the business or organization.
            terms_and_conditions_url: The URL to the terms and conditions for the business or organization.
            age_gated_content: Indicates if the content is age gated.
            opt_in_keywords: List of keywords that users can text in to opt in to receive messages.
            vetting_provider: The third-party political vetting provider.
            vetting_id: The unique ID of the vetting
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v1/Tollfree/Verifications/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("BusinessName", business_name),
                    param[str | None]("BusinessWebsite", business_website),
                    param[str | None]("NotificationEmail", notification_email),
                    param[list[TollfreeVerificationEnumUseCaseCategoryOrStr | None] | None](
                        "UseCaseCategories", use_case_categories
                    ),
                    param[str | None]("UseCaseSummary", use_case_summary),
                    param[str | None]("ProductionMessageSample", production_message_sample),
                    param[list[str] | None]("OptInImageUrls", opt_in_image_urls),
                    param[TollfreeVerificationEnumOptInTypeOrStr | None]("OptInType", opt_in_type),
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
                    param[str | None]("EditReason", edit_reason),
                    param[str | None]("BusinessRegistrationNumber", business_registration_number),
                    param[TollfreeVerificationEnumBusinessRegistrationAuthorityOrStr | None](
                        "BusinessRegistrationAuthority", business_registration_authority
                    ),
                    param[str | None]("BusinessRegistrationCountry", business_registration_country),
                    param[TollfreeVerificationEnumBusinessTypeOrStr | None]("BusinessType", business_type),
                    param[str | None]("BusinessRegistrationPhoneNumber", business_registration_phone_number),
                    param[str | None]("DoingBusinessAs", doing_business_as),
                    param[str | None]("OptInConfirmationMessage", opt_in_confirmation_message),
                    param[str | None]("HelpMessageSample", help_message_sample),
                    param[str | None]("PrivacyPolicyUrl", privacy_policy_url),
                    param[str | None]("TermsAndConditionsUrl", terms_and_conditions_url),
                    param[bool | None]("AgeGatedContent", age_gated_content),
                    param[list[str] | None]("OptInKeywords", opt_in_keywords),
                    param[TollfreeVerificationEnumVettingProviderOrStr | None]("VettingProvider", vetting_provider),
                    param[str | None]("VettingId", vetting_id),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1TollfreeVerification],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncMessagingV1TollfreeVerificationApiWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def create_tollfree_verification(
        self,
        business_name: str,
        business_website: str,
        notification_email: str,
        use_case_categories: list[TollfreeVerificationEnumUseCaseCategoryOrStr | None],
        use_case_summary: str,
        production_message_sample: str,
        opt_in_image_urls: list[str],
        opt_in_type: TollfreeVerificationEnumOptInTypeOrStr,
        message_volume: str,
        tollfree_phone_number_sid: str,
        *,
        customer_profile_sid: str | None = None,
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
        external_reference_id: str | None = None,
        business_registration_number: str | None = None,
        business_registration_authority: TollfreeVerificationEnumBusinessRegistrationAuthorityOrStr | None = None,
        business_registration_country: str | None = None,
        business_type: TollfreeVerificationEnumBusinessTypeOrStr | None = None,
        business_registration_phone_number: str | None = None,
        doing_business_as: str | None = None,
        opt_in_confirmation_message: str | None = None,
        help_message_sample: str | None = None,
        privacy_policy_url: str | None = None,
        terms_and_conditions_url: str | None = None,
        age_gated_content: bool | None = None,
        opt_in_keywords: list[str] | None = None,
        vetting_provider: TollfreeVerificationEnumVettingProviderOrStr | None = None,
        vetting_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MessagingV1TollfreeVerification, RawError]:
        """Create a tollfree verification

        Args:
            business_name: The name of the business or organization using the Tollfree number.
            business_website: The website of the business or organization using the Tollfree number.
            notification_email: The email address to receive the notification about the verification result. .
            use_case_categories: The category of the use case for the Tollfree Number. List as many as are applicable.
            use_case_summary: Use this to further explain how messaging is used by the business or organization.
            production_message_sample: An example of message content, i.e. a sample message.
            opt_in_image_urls: Link to an image that shows the opt-in workflow. Multiple images allowed and must be a
                publicly hosted URL.
            opt_in_type: Describe how a user opts-in to text messages.
            message_volume: Estimate monthly volume of messages from the Tollfree Number.
            tollfree_phone_number_sid: The SID of the Phone Number associated with the Tollfree Verification.
            customer_profile_sid: Customer's Profile Bundle BundleSid.
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
            business_contact_phone: The E.164 formatted phone number of the contact for the business or organization
                using the Tollfree number.
            external_reference_id: An optional external reference ID supplied by customer and echoed back on status
                retrieval.
            business_registration_number: A legally recognized business registration number. Required for all business
                types except SOLE_PROPRIETOR.
            business_registration_authority: The organizational authority for business registrations. Required for all
                business types except SOLE_PROPRIETOR.
            business_registration_country: The country where the business is registered. Required for all business types
                except SOLE_PROPRIETOR.
            business_type: The type of business, valid values are PRIVATE_PROFIT, PUBLIC_PROFIT, NON_PROFIT,
                SOLE_PROPRIETOR, GOVERNMENT. Required field.
            business_registration_phone_number: The E.164 formatted number associated with the business.
            doing_business_as: Trade name, sub entity, or downstream business name of business being submitted for
                verification
            opt_in_confirmation_message: The confirmation message sent to users when they opt in to receive messages.
            help_message_sample: A sample help message provided to users.
            privacy_policy_url: The URL to the privacy policy for the business or organization.
            terms_and_conditions_url: The URL to the terms and conditions for the business or organization.
            age_gated_content: Indicates if the content is age gated.
            opt_in_keywords: List of keywords that users can text in to opt in to receive messages.
            vetting_provider: The third-party political vetting provider.
            vetting_id: The unique ID of the vetting
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v1/Tollfree/Verifications"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("BusinessName", business_name),
                    param[str]("BusinessWebsite", business_website),
                    param[str]("NotificationEmail", notification_email),
                    param[list[TollfreeVerificationEnumUseCaseCategoryOrStr | None]](
                        "UseCaseCategories", use_case_categories
                    ),
                    param[str]("UseCaseSummary", use_case_summary),
                    param[str]("ProductionMessageSample", production_message_sample),
                    param[list[str]]("OptInImageUrls", opt_in_image_urls),
                    param[TollfreeVerificationEnumOptInTypeOrStr]("OptInType", opt_in_type),
                    param[str]("MessageVolume", message_volume),
                    param[str]("TollfreePhoneNumberSid", tollfree_phone_number_sid),
                    param[str | None]("CustomerProfileSid", customer_profile_sid),
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
                    param[str | None]("ExternalReferenceId", external_reference_id),
                    param[str | None]("BusinessRegistrationNumber", business_registration_number),
                    param[TollfreeVerificationEnumBusinessRegistrationAuthorityOrStr | None](
                        "BusinessRegistrationAuthority", business_registration_authority
                    ),
                    param[str | None]("BusinessRegistrationCountry", business_registration_country),
                    param[TollfreeVerificationEnumBusinessTypeOrStr | None]("BusinessType", business_type),
                    param[str | None]("BusinessRegistrationPhoneNumber", business_registration_phone_number),
                    param[str | None]("DoingBusinessAs", doing_business_as),
                    param[str | None]("OptInConfirmationMessage", opt_in_confirmation_message),
                    param[str | None]("HelpMessageSample", help_message_sample),
                    param[str | None]("PrivacyPolicyUrl", privacy_policy_url),
                    param[str | None]("TermsAndConditionsUrl", terms_and_conditions_url),
                    param[bool | None]("AgeGatedContent", age_gated_content),
                    param[list[str] | None]("OptInKeywords", opt_in_keywords),
                    param[TollfreeVerificationEnumVettingProviderOrStr | None]("VettingProvider", vetting_provider),
                    param[str | None]("VettingId", vetting_id),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1TollfreeVerification],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_tollfree_verification(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a tollfree verification

        Args:
            sid: The unique string to identify Tollfree Verification.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default1("/v1/Tollfree/Verifications/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_tollfree_verification(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV1TollfreeVerification, RawError]:
        """Retrieve a tollfree verification

        Args:
            sid: A unique string identifying a Tollfree Verification.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/Tollfree/Verifications/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1TollfreeVerification],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_tollfree_verification(
        self,
        *,
        tollfree_phone_number_sid: str | None = None,
        status: TollfreeVerificationEnumStatusOrStr | None = None,
        external_reference_id: str | None = None,
        include_sub_accounts: bool | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        trust_product_sid: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListTollfreeVerificationResponse, RawError]:
        """List tollfree verifications

        Args:
            tollfree_phone_number_sid: The SID of the Phone Number associated with the Tollfree Verification.
            status: The compliance status of the Tollfree Verification record.
            external_reference_id: Customer supplied reference id for the Tollfree Verification record.
            include_sub_accounts: Whether to include Tollfree Verifications from sub accounts in list response.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            trust_product_sid: The trust product sids / tollfree bundle sids of tollfree verifications
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/Tollfree/Verifications"),
            query_params=[
                param[str | None]("TollfreePhoneNumberSid", tollfree_phone_number_sid),
                param[TollfreeVerificationEnumStatusOrStr | None]("Status", status),
                param[str | None]("ExternalReferenceId", external_reference_id),
                param[bool | None]("IncludeSubAccounts", include_sub_accounts),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
                param[list[str] | None]("TrustProductSid", trust_product_sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListTollfreeVerificationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_tollfree_verification(
        self,
        sid: str,
        *,
        business_name: str | None = None,
        business_website: str | None = None,
        notification_email: str | None = None,
        use_case_categories: list[TollfreeVerificationEnumUseCaseCategoryOrStr | None] | None = None,
        use_case_summary: str | None = None,
        production_message_sample: str | None = None,
        opt_in_image_urls: list[str] | None = None,
        opt_in_type: TollfreeVerificationEnumOptInTypeOrStr | None = None,
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
        edit_reason: str | None = None,
        business_registration_number: str | None = None,
        business_registration_authority: TollfreeVerificationEnumBusinessRegistrationAuthorityOrStr | None = None,
        business_registration_country: str | None = None,
        business_type: TollfreeVerificationEnumBusinessTypeOrStr | None = None,
        business_registration_phone_number: str | None = None,
        doing_business_as: str | None = None,
        opt_in_confirmation_message: str | None = None,
        help_message_sample: str | None = None,
        privacy_policy_url: str | None = None,
        terms_and_conditions_url: str | None = None,
        age_gated_content: bool | None = None,
        opt_in_keywords: list[str] | None = None,
        vetting_provider: TollfreeVerificationEnumVettingProviderOrStr | None = None,
        vetting_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MessagingV1TollfreeVerification, RawError]:
        """Edit a tollfree verification

        Args:
            sid: The unique string to identify Tollfree Verification.
            business_name: The name of the business or organization using the Tollfree number.
            business_website: The website of the business or organization using the Tollfree number.
            notification_email: The email address to receive the notification about the verification result. .
            use_case_categories: The category of the use case for the Tollfree Number. List as many as are applicable.
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
            business_contact_phone: The E.164 formatted phone number of the contact for the business or organization
                using the Tollfree number.
            edit_reason: Describe why the verification is being edited. If the verification was rejected because of a
                technical issue, such as the website being down, and the issue has been resolved this parameter should
                be set to something similar to 'Website fixed'.
            business_registration_number: A legally recognized business registration number
            business_registration_authority: The organizational authority for business registrations. Required for all
                business types except SOLE_PROPRIETOR.
            business_registration_country: Country business is registered in
            business_type: The type of business, valid values are PRIVATE_PROFIT, PUBLIC_PROFIT, NON_PROFIT,
                SOLE_PROPRIETOR, GOVERNMENT. Required field.
            business_registration_phone_number: The E.164 formatted number associated with the business.
            doing_business_as: Trade name, sub entity, or downstream business name of business being submitted for
                verification
            opt_in_confirmation_message: The confirmation message sent to users when they opt in to receive messages.
            help_message_sample: A sample help message provided to users.
            privacy_policy_url: The URL to the privacy policy for the business or organization.
            terms_and_conditions_url: The URL to the terms and conditions for the business or organization.
            age_gated_content: Indicates if the content is age gated.
            opt_in_keywords: List of keywords that users can text in to opt in to receive messages.
            vetting_provider: The third-party political vetting provider.
            vetting_id: The unique ID of the vetting
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v1/Tollfree/Verifications/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("BusinessName", business_name),
                    param[str | None]("BusinessWebsite", business_website),
                    param[str | None]("NotificationEmail", notification_email),
                    param[list[TollfreeVerificationEnumUseCaseCategoryOrStr | None] | None](
                        "UseCaseCategories", use_case_categories
                    ),
                    param[str | None]("UseCaseSummary", use_case_summary),
                    param[str | None]("ProductionMessageSample", production_message_sample),
                    param[list[str] | None]("OptInImageUrls", opt_in_image_urls),
                    param[TollfreeVerificationEnumOptInTypeOrStr | None]("OptInType", opt_in_type),
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
                    param[str | None]("EditReason", edit_reason),
                    param[str | None]("BusinessRegistrationNumber", business_registration_number),
                    param[TollfreeVerificationEnumBusinessRegistrationAuthorityOrStr | None](
                        "BusinessRegistrationAuthority", business_registration_authority
                    ),
                    param[str | None]("BusinessRegistrationCountry", business_registration_country),
                    param[TollfreeVerificationEnumBusinessTypeOrStr | None]("BusinessType", business_type),
                    param[str | None]("BusinessRegistrationPhoneNumber", business_registration_phone_number),
                    param[str | None]("DoingBusinessAs", doing_business_as),
                    param[str | None]("OptInConfirmationMessage", opt_in_confirmation_message),
                    param[str | None]("HelpMessageSample", help_message_sample),
                    param[str | None]("PrivacyPolicyUrl", privacy_policy_url),
                    param[str | None]("TermsAndConditionsUrl", terms_and_conditions_url),
                    param[bool | None]("AgeGatedContent", age_gated_content),
                    param[list[str] | None]("OptInKeywords", opt_in_keywords),
                    param[TollfreeVerificationEnumVettingProviderOrStr | None]("VettingProvider", vetting_provider),
                    param[str | None]("VettingId", vetting_id),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1TollfreeVerification],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
