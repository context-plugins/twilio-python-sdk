<!-- Generated file — do not edit; regenerated with the SDK. -->

# TrusthubV1ComplianceInquiries — operations

Accessor: `client.trusthub_v1_compliance_inquiries` · Source: `twilio_sdk/apis/trusthub_v1_compliance_inquiries.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.trusthub_v1_compliance_inquiries.create_compliance_inquiry

- **Route**: `POST /v1/ComplianceInquiries/Customers/Initialize`
- **Auth**: `account_sid_auth_token`
- **Server**: `default9`
- **Signature**: `def create_compliance_inquiry(*, notification_email: str | None = None, theme_set_id: str | None = None, primary_profile_sid: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `notification_email` — form field `NotificationEmail` · `theme_set_id` — form field `ThemeSetId` · `primary_profile_sid` — form field `PrimaryProfileSid`
- **Returns (parsed)**: `TrusthubV1ComplianceInquiry`
- **Returns (raw)**: `ApiResult[TrusthubV1ComplianceInquiry, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TrusthubV1ComplianceInquiry` | `twilio_sdk/models/trusthub_v1_compliance_inquiry.py` |

### client.trusthub_v1_compliance_inquiries.update_compliance_inquiry

- **Route**: `POST /v1/ComplianceInquiries/Customers/{CustomerId}/Initialize`
- **Auth**: `account_sid_auth_token`
- **Server**: `default9`
- **Signature**: `def update_compliance_inquiry(customer_id: str, primary_profile_sid: str, *, theme_set_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `customer_id`, `primary_profile_sid`
- **Params**: `customer_id` — path `CustomerId` · `primary_profile_sid` — form field `PrimaryProfileSid` · `theme_set_id` — form field `ThemeSetId`
- **Returns (parsed)**: `TrusthubV1ComplianceInquiry`
- **Returns (raw)**: `ApiResult[TrusthubV1ComplianceInquiry, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TrusthubV1ComplianceInquiry` | `twilio_sdk/models/trusthub_v1_compliance_inquiry.py` |

