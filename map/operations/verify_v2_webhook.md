<!-- Generated file — do not edit; regenerated with the SDK. -->

# VerifyV2Webhook — operations

Accessor: `client.verify_v2_webhook` · Source: `twilio_sdk/apis/verify_v2_webhook.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.verify_v2_webhook.create_webhook

- **Route**: `POST /v2/Services/{ServiceSid}/Webhooks`
- **Server**: `default3`
- **Signature**: `def create_webhook(service_sid: str, friendly_name: str, event_types: list[str], webhook_url: str, *, status: WebhookEnumStatusOrStr | None = None, version: WebhookEnumVersionOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `friendly_name`, `event_types`, `webhook_url`
- **Params**: `service_sid` — path `ServiceSid` · `friendly_name` — form field `FriendlyName` · `event_types` — form field `EventTypes` · `webhook_url` — form field `WebhookUrl` · `status` — form field `Status` · `version` — form field `Version`
- **Returns (parsed)**: `VerifyV2ServiceWebhook`
- **Returns (raw)**: `ApiResult[VerifyV2ServiceWebhook, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WebhookEnumStatusOrStr` | `twilio_sdk/models/enums/webhook_enum_status.py` |
| `WebhookEnumVersionOrStr` | `twilio_sdk/models/enums/webhook_enum_version.py` |
| `VerifyV2ServiceWebhook` | `twilio_sdk/models/verify_v2_service_webhook.py` |

### client.verify_v2_webhook.delete_webhook

- **Route**: `DELETE /v2/Services/{ServiceSid}/Webhooks/{Sid}`
- **Server**: `default3`
- **Signature**: `def delete_webhook(service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `sid`
- **Params**: `service_sid` — path `ServiceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.verify_v2_webhook.fetch_webhook

- **Route**: `GET /v2/Services/{ServiceSid}/Webhooks/{Sid}`
- **Server**: `default3`
- **Signature**: `def fetch_webhook(service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `sid`
- **Params**: `service_sid` — path `ServiceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `VerifyV2ServiceWebhook`
- **Returns (raw)**: `ApiResult[VerifyV2ServiceWebhook, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VerifyV2ServiceWebhook` | `twilio_sdk/models/verify_v2_service_webhook.py` |

### client.verify_v2_webhook.list_webhook

- **Route**: `GET /v2/Services/{ServiceSid}/Webhooks`
- **Server**: `default3`
- **Signature**: `def list_webhook(service_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`
- **Params**: `service_sid` — path `ServiceSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListWebhookResponse`
- **Returns (raw)**: `ApiResult[ListWebhookResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListWebhookResponse` | `twilio_sdk/models/list_webhook_response.py` |

### client.verify_v2_webhook.update_webhook

- **Route**: `POST /v2/Services/{ServiceSid}/Webhooks/{Sid}`
- **Server**: `default3`
- **Signature**: `def update_webhook(service_sid: str, sid: str, *, friendly_name: str | None = None, event_types: list[str] | None = None, webhook_url: str | None = None, status: WebhookEnumStatusOrStr | None = None, version: WebhookEnumVersionOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `sid`
- **Params**: `service_sid` — path `ServiceSid` · `sid` — path `Sid` · `friendly_name` — form field `FriendlyName` · `event_types` — form field `EventTypes` · `webhook_url` — form field `WebhookUrl` · `status` — form field `Status` · `version` — form field `Version`
- **Returns (parsed)**: `VerifyV2ServiceWebhook`
- **Returns (raw)**: `ApiResult[VerifyV2ServiceWebhook, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WebhookEnumStatusOrStr` | `twilio_sdk/models/enums/webhook_enum_status.py` |
| `WebhookEnumVersionOrStr` | `twilio_sdk/models/enums/webhook_enum_version.py` |
| `VerifyV2ServiceWebhook` | `twilio_sdk/models/verify_v2_service_webhook.py` |

