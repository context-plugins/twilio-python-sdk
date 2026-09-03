<!-- Generated file — do not edit; regenerated with the SDK. -->

# MessagingV1UsAppToPerson — operations

Accessor: `client.messaging_v1_us_app_to_person` · Source: `twilio_sdk/apis/messaging_v1_us_app_to_person.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.messaging_v1_us_app_to_person.create_us_app_to_person

- **Route**: `POST /v1/Services/{MessagingServiceSid}/Compliance/Usa2p`
- **Auth**: `account_sid_auth_token`
- **Server**: `default1`
- **Signature**: `def create_us_app_to_person(messaging_service_sid: str, brand_registration_sid: str, description: str, message_flow: str, message_samples: list[str], us_app_to_person_usecase: str, has_embedded_links: bool, has_embedded_phone: bool, *, x_twilio_api_version: str | None = None, opt_in_message: str | None = None, opt_out_message: str | None = None, help_message: str | None = None, opt_in_keywords: list[str] | None = None, opt_out_keywords: list[str] | None = None, help_keywords: list[str] | None = None, subscriber_opt_in: bool | None = None, age_gated: bool | None = None, direct_lending: bool | None = None, privacy_policy_url: str | None = None, terms_and_conditions_url: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `messaging_service_sid`, `brand_registration_sid`, `description`, `message_flow`, `message_samples`, `us_app_to_person_usecase`, `has_embedded_links`, `has_embedded_phone`
- **Params**: `messaging_service_sid` — path `MessagingServiceSid` · `x_twilio_api_version` — header `X-Twilio-Api-Version` · `brand_registration_sid` — form field `BrandRegistrationSid` · `description` — form field `Description` · `message_flow` — form field `MessageFlow` · `message_samples` — form field `MessageSamples` · `us_app_to_person_usecase` — form field `UsAppToPersonUsecase` · `has_embedded_links` — form field `HasEmbeddedLinks` · `has_embedded_phone` — form field `HasEmbeddedPhone` · `opt_in_message` — form field `OptInMessage` · `opt_out_message` — form field `OptOutMessage` · `help_message` — form field `HelpMessage` · `opt_in_keywords` — form field `OptInKeywords` · `opt_out_keywords` — form field `OptOutKeywords` · `help_keywords` — form field `HelpKeywords` · `subscriber_opt_in` — form field `SubscriberOptIn` · `age_gated` — form field `AgeGated` · `direct_lending` — form field `DirectLending` · `privacy_policy_url` — form field `PrivacyPolicyUrl` · `terms_and_conditions_url` — form field `TermsAndConditionsUrl`
- **Returns (parsed)**: `MessagingV1ServiceUsAppToPersonResponse`
- **Returns (raw)**: `ApiResult[MessagingV1ServiceUsAppToPersonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MessagingV1ServiceUsAppToPersonResponse` | `twilio_sdk/models/unions/messaging_v1_service_us_app_to_person_response.py` |

### client.messaging_v1_us_app_to_person.delete_us_app_to_person

- **Route**: `DELETE /v1/Services/{MessagingServiceSid}/Compliance/Usa2p/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default1`
- **Signature**: `def delete_us_app_to_person(messaging_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `messaging_service_sid`, `sid`
- **Params**: `messaging_service_sid` — path `MessagingServiceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.messaging_v1_us_app_to_person.fetch_us_app_to_person

- **Route**: `GET /v1/Services/{MessagingServiceSid}/Compliance/Usa2p/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default1`
- **Signature**: `def fetch_us_app_to_person(messaging_service_sid: str, sid: str, *, x_twilio_api_version: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `messaging_service_sid`, `sid`
- **Params**: `messaging_service_sid` — path `MessagingServiceSid` · `sid` — path `Sid` · `x_twilio_api_version` — header `X-Twilio-Api-Version`
- **Returns (parsed)**: `MessagingV1ServiceUsAppToPersonResponse`
- **Returns (raw)**: `ApiResult[MessagingV1ServiceUsAppToPersonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MessagingV1ServiceUsAppToPersonResponse` | `twilio_sdk/models/unions/messaging_v1_service_us_app_to_person_response.py` |

### client.messaging_v1_us_app_to_person.list_us_app_to_person

- **Route**: `GET /v1/Services/{MessagingServiceSid}/Compliance/Usa2p`
- **Auth**: `account_sid_auth_token`
- **Server**: `default1`
- **Signature**: `def list_us_app_to_person(messaging_service_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, x_twilio_api_version: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `messaging_service_sid`
- **Params**: `messaging_service_sid` — path `MessagingServiceSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken` · `x_twilio_api_version` — header `X-Twilio-Api-Version`
- **Returns (parsed)**: `ListUsAppToPersonResponse`
- **Returns (raw)**: `ApiResult[ListUsAppToPersonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListUsAppToPersonResponse` | `twilio_sdk/models/list_us_app_to_person_response.py` |

### client.messaging_v1_us_app_to_person.update_us_app_to_person

- **Route**: `POST /v1/Services/{MessagingServiceSid}/Compliance/Usa2p/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default1`
- **Signature**: `def update_us_app_to_person(messaging_service_sid: str, sid: str, has_embedded_links: bool, has_embedded_phone: bool, message_samples: list[str], message_flow: str, description: str, age_gated: bool, direct_lending: bool, *, x_twilio_api_version: str | None = None, privacy_policy_url: str | None = None, terms_and_conditions_url: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `messaging_service_sid`, `sid`, `has_embedded_links`, `has_embedded_phone`, `message_samples`, `message_flow`, `description`, `age_gated`, `direct_lending`
- **Params**: `messaging_service_sid` — path `MessagingServiceSid` · `sid` — path `Sid` · `x_twilio_api_version` — header `X-Twilio-Api-Version` · `has_embedded_links` — form field `HasEmbeddedLinks` · `has_embedded_phone` — form field `HasEmbeddedPhone` · `message_samples` — form field `MessageSamples` · `message_flow` — form field `MessageFlow` · `description` — form field `Description` · `age_gated` — form field `AgeGated` · `direct_lending` — form field `DirectLending` · `privacy_policy_url` — form field `PrivacyPolicyUrl` · `terms_and_conditions_url` — form field `TermsAndConditionsUrl`
- **Returns (parsed)**: `MessagingV1ServiceUsAppToPersonResponse`
- **Returns (raw)**: `ApiResult[MessagingV1ServiceUsAppToPersonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MessagingV1ServiceUsAppToPersonResponse` | `twilio_sdk/models/unions/messaging_v1_service_us_app_to_person_response.py` |

