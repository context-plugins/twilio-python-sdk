<!-- Generated file — do not edit; regenerated with the SDK. -->

# NumbersV1PortingWebhookConfigurationDeleteApi — operations

Accessor: `client.numbers_v1_porting_webhook_configuration_delete_api` · Source: `twilio_sdk/apis/numbers_v1_porting_webhook_configuration_delete_api.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.numbers_v1_porting_webhook_configuration_delete_api.delete_porting_webhook_configuration_delete

- **Route**: `DELETE /v1/Porting/Configuration/Webhook/{WebhookType}`
- **Server**: `default5`
- **Signature**: `def delete_porting_webhook_configuration_delete(webhook_type: PortingWebhookConfigurationDeleteEnumWebhookTypeOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `webhook_type`
- **Params**: `webhook_type` — path `WebhookType`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PortingWebhookConfigurationDeleteEnumWebhookTypeOrStr` | `twilio_sdk/models/enums/porting_webhook_configuration_delete_enum_webhook_type.py` |

