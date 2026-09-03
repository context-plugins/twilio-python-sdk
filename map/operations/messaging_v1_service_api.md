<!-- Generated file — do not edit; regenerated with the SDK. -->

# MessagingV1ServiceApi — operations

Accessor: `client.messaging_v1_service_api` · Source: `twilio_sdk/apis/messaging_v1_service_api.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.messaging_v1_service_api.create_service

- **Route**: `POST /v1/Services`
- **Auth**: `account_sid_auth_token`
- **Server**: `default1`
- **Signature**: `def create_service(friendly_name: str, *, inbound_request_url: str | None = None, inbound_method: AmdStatusCallbackMethodOrStr | None = None, fallback_url: str | None = None, fallback_method: AmdStatusCallbackMethodOrStr | None = None, status_callback: str | None = None, sticky_sender: bool | None = None, mms_converter: bool | None = None, smart_encoding: bool | None = None, scan_message_content: ServiceEnumScanMessageContentOrStr | None = None, fallback_to_long_code: bool | None = None, area_code_geomatch: bool | None = None, validity_period: int | None = None, synchronous_validation: bool | None = None, usecase: str | None = None, use_inbound_webhook_on_number: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `friendly_name`
- **Params**: `friendly_name` — form field `FriendlyName` · `inbound_request_url` — form field `InboundRequestUrl` · `inbound_method` — form field `InboundMethod` · `fallback_url` — form field `FallbackUrl` · `fallback_method` — form field `FallbackMethod` · `status_callback` — form field `StatusCallback` · `sticky_sender` — form field `StickySender` · `mms_converter` — form field `MmsConverter` · `smart_encoding` — form field `SmartEncoding` · `scan_message_content` — form field `ScanMessageContent` · `fallback_to_long_code` — form field `FallbackToLongCode` · `area_code_geomatch` — form field `AreaCodeGeomatch` · `validity_period` — form field `ValidityPeriod` · `synchronous_validation` — form field `SynchronousValidation` · `usecase` — form field `Usecase` · `use_inbound_webhook_on_number` — form field `UseInboundWebhookOnNumber`
- **Returns (parsed)**: `MessagingV1Service`
- **Returns (raw)**: `ApiResult[MessagingV1Service, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AmdStatusCallbackMethodOrStr` | `twilio_sdk/models/enums/amd_status_callback_method.py` |
| `ServiceEnumScanMessageContentOrStr` | `twilio_sdk/models/enums/service_enum_scan_message_content.py` |
| `MessagingV1Service` | `twilio_sdk/models/messaging_v1_service.py` |

### client.messaging_v1_service_api.delete_service

- **Route**: `DELETE /v1/Services/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default1`
- **Signature**: `def delete_service(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.messaging_v1_service_api.fetch_service

- **Route**: `GET /v1/Services/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default1`
- **Signature**: `def fetch_service(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `MessagingV1Service`
- **Returns (raw)**: `ApiResult[MessagingV1Service, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MessagingV1Service` | `twilio_sdk/models/messaging_v1_service.py` |

### client.messaging_v1_service_api.list_service

- **Route**: `GET /v1/Services`
- **Auth**: `account_sid_auth_token`
- **Server**: `default1`
- **Signature**: `def list_service(*, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListServiceResponse`
- **Returns (raw)**: `ApiResult[ListServiceResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListServiceResponse` | `twilio_sdk/models/list_service_response.py` |

### client.messaging_v1_service_api.update_service

- **Route**: `POST /v1/Services/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default1`
- **Signature**: `def update_service(sid: str, *, friendly_name: str | None = None, inbound_request_url: str | None = None, inbound_method: AmdStatusCallbackMethodOrStr | None = None, fallback_url: str | None = None, fallback_method: AmdStatusCallbackMethodOrStr | None = None, status_callback: str | None = None, sticky_sender: bool | None = None, mms_converter: bool | None = None, smart_encoding: bool | None = None, scan_message_content: ServiceEnumScanMessageContentOrStr | None = None, fallback_to_long_code: bool | None = None, area_code_geomatch: bool | None = None, validity_period: int | None = None, synchronous_validation: bool | None = None, usecase: str | None = None, use_inbound_webhook_on_number: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid` · `friendly_name` — form field `FriendlyName` · `inbound_request_url` — form field `InboundRequestUrl` · `inbound_method` — form field `InboundMethod` · `fallback_url` — form field `FallbackUrl` · `fallback_method` — form field `FallbackMethod` · `status_callback` — form field `StatusCallback` · `sticky_sender` — form field `StickySender` · `mms_converter` — form field `MmsConverter` · `smart_encoding` — form field `SmartEncoding` · `scan_message_content` — form field `ScanMessageContent` · `fallback_to_long_code` — form field `FallbackToLongCode` · `area_code_geomatch` — form field `AreaCodeGeomatch` · `validity_period` — form field `ValidityPeriod` · `synchronous_validation` — form field `SynchronousValidation` · `usecase` — form field `Usecase` · `use_inbound_webhook_on_number` — form field `UseInboundWebhookOnNumber`
- **Returns (parsed)**: `MessagingV1Service`
- **Returns (raw)**: `ApiResult[MessagingV1Service, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AmdStatusCallbackMethodOrStr` | `twilio_sdk/models/enums/amd_status_callback_method.py` |
| `ServiceEnumScanMessageContentOrStr` | `twilio_sdk/models/enums/service_enum_scan_message_content.py` |
| `MessagingV1Service` | `twilio_sdk/models/messaging_v1_service.py` |

