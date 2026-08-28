<!-- Generated file — do not edit; regenerated with the SDK. -->

# NumbersV2HostedNumberOrderApi — operations

Accessor: `client.numbers_v2_hosted_number_order_api` · Source: `twilio_sdk/apis/numbers_v2_hosted_number_order_api.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.numbers_v2_hosted_number_order_api.create_hosted_number_order

- **Route**: `POST /v2/HostedNumber/Orders`
- **Server**: `default5`
- **Signature**: `def create_hosted_number_order(phone_number: str, contact_phone_number: str, address_sid: str, email: str, *, account_sid: str | None = None, friendly_name: str | None = None, cc_emails: list[str] | None = None, sms_url: AnyUrl | None = None, sms_method: AmdStatusCallbackMethodOrStr | None = None, sms_fallback_url: AnyUrl | None = None, sms_capability: bool | None = None, sms_fallback_method: AmdStatusCallbackMethodOrStr | None = None, status_callback_url: AnyUrl | None = None, status_callback_method: AmdStatusCallbackMethodOrStr | None = None, sms_application_sid: str | None = None, contact_title: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `phone_number`, `contact_phone_number`, `address_sid`, `email`
- **Params**: `phone_number` — form field `PhoneNumber` · `contact_phone_number` — form field `ContactPhoneNumber` · `address_sid` — form field `AddressSid` · `email` — form field `Email` · `account_sid` — form field `AccountSid` · `friendly_name` — form field `FriendlyName` · `cc_emails` — form field `CcEmails` · `sms_url` — form field `SmsUrl` · `sms_method` — form field `SmsMethod` · `sms_fallback_url` — form field `SmsFallbackUrl` · `sms_capability` — form field `SmsCapability` · `sms_fallback_method` — form field `SmsFallbackMethod` · `status_callback_url` — form field `StatusCallbackUrl` · `status_callback_method` — form field `StatusCallbackMethod` · `sms_application_sid` — form field `SmsApplicationSid` · `contact_title` — form field `ContactTitle`
- **Returns (parsed)**: `NumbersV2HostedNumberOrder`
- **Returns (raw)**: `ApiResult[NumbersV2HostedNumberOrder, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AmdStatusCallbackMethodOrStr` | `twilio_sdk/models/enums/amd_status_callback_method.py` |
| `NumbersV2HostedNumberOrder` | `twilio_sdk/models/numbers_v2_hosted_number_order.py` |

### client.numbers_v2_hosted_number_order_api.delete_hosted_number_order

- **Route**: `DELETE /v2/HostedNumber/Orders/{Sid}`
- **Server**: `default5`
- **Signature**: `def delete_hosted_number_order(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.numbers_v2_hosted_number_order_api.fetch_hosted_number_order

- **Route**: `GET /v2/HostedNumber/Orders/{Sid}`
- **Server**: `default5`
- **Signature**: `def fetch_hosted_number_order(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `NumbersV2HostedNumberOrder`
- **Returns (raw)**: `ApiResult[NumbersV2HostedNumberOrder, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NumbersV2HostedNumberOrder` | `twilio_sdk/models/numbers_v2_hosted_number_order.py` |

### client.numbers_v2_hosted_number_order_api.list_hosted_number_order

- **Route**: `GET /v2/HostedNumber/Orders`
- **Server**: `default5`
- **Signature**: `def list_hosted_number_order(*, status: DependentOrderEnumStatusOrStr | None = None, sms_capability: bool | None = None, phone_number: str | None = None, incoming_phone_number_sid: str | None = None, friendly_name: str | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `status` — query `Status` · `sms_capability` — query `SmsCapability` · `phone_number` — query `PhoneNumber` · `incoming_phone_number_sid` — query `IncomingPhoneNumberSid` · `friendly_name` — query `FriendlyName` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListHostedNumberOrderResponse`
- **Returns (raw)**: `ApiResult[ListHostedNumberOrderResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DependentOrderEnumStatusOrStr` | `twilio_sdk/models/enums/dependent_order_enum_status.py` |
| `ListHostedNumberOrderResponse` | `twilio_sdk/models/list_hosted_number_order_response.py` |

### client.numbers_v2_hosted_number_order_api.update_hosted_number_order

- **Route**: `POST /v2/HostedNumber/Orders/{Sid}`
- **Server**: `default5`
- **Signature**: `def update_hosted_number_order(sid: str, status: DependentOrderEnumStatusOrStr, *, verification_call_delay: int | None = None, verification_call_extension: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`, `status`
- **Params**: `sid` — path `Sid` · `status` — form field `Status` · `verification_call_delay` — form field `VerificationCallDelay` · `verification_call_extension` — form field `VerificationCallExtension`
- **Returns (parsed)**: `NumbersV2HostedNumberOrder`
- **Returns (raw)**: `ApiResult[NumbersV2HostedNumberOrder, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DependentOrderEnumStatusOrStr` | `twilio_sdk/models/enums/dependent_order_enum_status.py` |
| `NumbersV2HostedNumberOrder` | `twilio_sdk/models/numbers_v2_hosted_number_order.py` |

