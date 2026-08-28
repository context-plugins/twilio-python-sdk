<!-- Generated file — do not edit; regenerated with the SDK. -->

# NumbersV3HostedNumbersHostedNumberOrderApi — operations

Accessor: `client.numbers_v3_hosted_numbers_hosted_number_order_api` · Source: `twilio/apis/numbers_v3_hosted_numbers_hosted_number_order_api.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.numbers_v3_hosted_numbers_hosted_number_order_api.create_hosted_numbers_hosted_number_order

- **Route**: `POST /v3/HostedNumbers/HostedNumberOrders`
- **Server**: `default5`
- **Signature**: `def create_hosted_numbers_hosted_number_order(phone_number: str, sms_capability: bool, *, account_sid: str | None = None, friendly_name: str | None = None, unique_name: str | None = None, cc_emails: list[str] | None = None, sms_url: str | None = None, sms_method: AmdStatusCallbackMethodOrStr | None = None, sms_fallback_url: str | None = None, sms_fallback_method: AmdStatusCallbackMethodOrStr | None = None, status_callback_url: str | None = None, status_callback_method: AmdStatusCallbackMethodOrStr | None = None, sms_application_sid: str | None = None, address_sid: str | None = None, email: str | None = None, verification_type: DependentOrderEnumVerificationTypeOrStr | None = None, verification_document_sid: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `phone_number`, `sms_capability`
- **Params**: `phone_number` — form field `phoneNumber` · `sms_capability` — form field `smsCapability` · `account_sid` — form field `accountSid` · `friendly_name` — form field `friendlyName` · `unique_name` — form field `uniqueName` · `cc_emails` — form field `ccEmails` · `sms_url` — form field `smsUrl` · `sms_method` — form field `smsMethod` · `sms_fallback_url` — form field `smsFallbackUrl` · `sms_fallback_method` — form field `smsFallbackMethod` · `status_callback_url` — form field `statusCallbackUrl` · `status_callback_method` — form field `statusCallbackMethod` · `sms_application_sid` — form field `smsApplicationSid` · `address_sid` — form field `addressSid` · `email` — form field · `verification_type` — form field `verificationType` · `verification_document_sid` — form field `verificationDocumentSid`
- **Returns (parsed)**: `NumbersV3HostedNumbersHostedNumberOrder`
- **Returns (raw)**: `ApiResult[NumbersV3HostedNumbersHostedNumberOrder, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AmdStatusCallbackMethodOrStr` | `twilio/models/enums/amd_status_callback_method.py` |
| `DependentOrderEnumVerificationTypeOrStr` | `twilio/models/enums/dependent_order_enum_verification_type.py` |
| `NumbersV3HostedNumbersHostedNumberOrder` | `twilio/models/numbers_v3_hosted_numbers_hosted_number_order.py` |

