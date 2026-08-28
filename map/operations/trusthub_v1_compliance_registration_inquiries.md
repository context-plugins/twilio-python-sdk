<!-- Generated file — do not edit; regenerated with the SDK. -->

# TrusthubV1ComplianceRegistrationInquiries — operations

Accessor: `client.trusthub_v1_compliance_registration_inquiries` · Source: `twilio/apis/trusthub_v1_compliance_registration_inquiries.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.trusthub_v1_compliance_registration_inquiries.create_compliance_registration

- **Route**: `POST /v1/ComplianceInquiries/Registration/RegulatoryCompliance/GB/Initialize`
- **Server**: `default9`
- **Signature**: `def create_compliance_registration(end_user_type: CustomerTypeOrStr, phone_number_type: ComplianceRegistrationEnumPhoneNumberTypeOrStr, *, business_identity_type: ComplianceRegistrationEnumBusinessIdentityTypeOrStr | None = None, business_registration_authority: ComplianceRegistrationEnumBusinessRegistrationAuthorityOrStr | None = None, business_legal_name: str | None = None, notification_email: str | None = None, accepted_notification_receipt: bool | None = None, business_registration_number: str | None = None, business_website_url: str | None = None, friendly_name: str | None = None, authorized_representative1_first_name: str | None = None, authorized_representative1_last_name: str | None = None, authorized_representative1_phone: str | None = None, authorized_representative1_email: str | None = None, authorized_representative1_date_of_birth: str | None = None, address_street: str | None = None, address_street_secondary: str | None = None, address_city: str | None = None, address_subdivision: str | None = None, address_postal_code: str | None = None, address_country_code: str | None = None, emergency_address_street: str | None = None, emergency_address_street_secondary: str | None = None, emergency_address_city: str | None = None, emergency_address_subdivision: str | None = None, emergency_address_postal_code: str | None = None, emergency_address_country_code: str | None = None, use_address_as_emergency_address: bool | None = None, file_name: str | None = None, file: str | None = None, first_name: str | None = None, last_name: str | None = None, date_of_birth: str | None = None, individual_email: str | None = None, individual_phone: str | None = None, is_isv_embed: bool | None = None, isv_registering_for_self_or_tenant: str | None = None, status_callback_url: str | None = None, theme_set_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `end_user_type`, `phone_number_type`
- **Params**: `end_user_type` — form field `EndUserType` · `phone_number_type` — form field `PhoneNumberType` · `business_identity_type` — form field `BusinessIdentityType` · `business_registration_authority` — form field `BusinessRegistrationAuthority` · `business_legal_name` — form field `BusinessLegalName` · `notification_email` — form field `NotificationEmail` · `accepted_notification_receipt` — form field `AcceptedNotificationReceipt` · `business_registration_number` — form field `BusinessRegistrationNumber` · `business_website_url` — form field `BusinessWebsiteUrl` · `friendly_name` — form field `FriendlyName` · `authorized_representative1_first_name` — form field `AuthorizedRepresentative1FirstName` · `authorized_representative1_last_name` — form field `AuthorizedRepresentative1LastName` · `authorized_representative1_phone` — form field `AuthorizedRepresentative1Phone` · `authorized_representative1_email` — form field `AuthorizedRepresentative1Email` · `authorized_representative1_date_of_birth` — form field `AuthorizedRepresentative1DateOfBirth` · `address_street` — form field `AddressStreet` · `address_street_secondary` — form field `AddressStreetSecondary` · `address_city` — form field `AddressCity` · `address_subdivision` — form field `AddressSubdivision` · `address_postal_code` — form field `AddressPostalCode` · `address_country_code` — form field `AddressCountryCode` · `emergency_address_street` — form field `EmergencyAddressStreet` · `emergency_address_street_secondary` — form field `EmergencyAddressStreetSecondary` · `emergency_address_city` — form field `EmergencyAddressCity` · `emergency_address_subdivision` — form field `EmergencyAddressSubdivision` · `emergency_address_postal_code` — form field `EmergencyAddressPostalCode` · `emergency_address_country_code` — form field `EmergencyAddressCountryCode` · `use_address_as_emergency_address` — form field `UseAddressAsEmergencyAddress` · `file_name` — form field `FileName` · `file` — form field `File` · `first_name` — form field `FirstName` · `last_name` — form field `LastName` · `date_of_birth` — form field `DateOfBirth` · `individual_email` — form field `IndividualEmail` · `individual_phone` — form field `IndividualPhone` · `is_isv_embed` — form field `IsIsvEmbed` · `isv_registering_for_self_or_tenant` — form field `IsvRegisteringForSelfOrTenant` · `status_callback_url` — form field `StatusCallbackUrl` · `theme_set_id` — form field `ThemeSetId`
- **Returns (parsed)**: `TrusthubV1ComplianceRegistration`
- **Returns (raw)**: `ApiResult[TrusthubV1ComplianceRegistration, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CustomerTypeOrStr` | `twilio/models/enums/customer_type.py` |
| `ComplianceRegistrationEnumPhoneNumberTypeOrStr` | `twilio/models/enums/compliance_registration_enum_phone_number_type.py` |
| `ComplianceRegistrationEnumBusinessIdentityTypeOrStr` | `twilio/models/enums/compliance_registration_enum_business_identity_type.py` |
| `ComplianceRegistrationEnumBusinessRegistrationAuthorityOrStr` | `twilio/models/enums/compliance_registration_enum_business_registration_authority.py` |
| `TrusthubV1ComplianceRegistration` | `twilio/models/trusthub_v1_compliance_registration.py` |

### client.trusthub_v1_compliance_registration_inquiries.update_compliance_registration

- **Route**: `POST /v1/ComplianceInquiries/Registration/{RegistrationId}/RegulatoryCompliance/GB/Initialize`
- **Server**: `default9`
- **Signature**: `def update_compliance_registration(registration_id: str, *, is_isv_embed: bool | None = None, theme_set_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `registration_id`
- **Params**: `registration_id` — path `RegistrationId` · `is_isv_embed` — form field `IsIsvEmbed` · `theme_set_id` — form field `ThemeSetId`
- **Returns (parsed)**: `TrusthubV1ComplianceRegistration`
- **Returns (raw)**: `ApiResult[TrusthubV1ComplianceRegistration, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TrusthubV1ComplianceRegistration` | `twilio/models/trusthub_v1_compliance_registration.py` |

