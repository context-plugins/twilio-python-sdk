<!-- Generated file — do not edit; regenerated with the SDK. -->

# NumbersV1PortingWebhookConfigurationApi — operations

Accessor: `client.numbers_v1_porting_webhook_configuration_api` · Source: `twilio_sdk/apis/numbers_v1_porting_webhook_configuration_api.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.numbers_v1_porting_webhook_configuration_api.create_porting_webhook_configuration

- **Route**: `POST /v1/Porting/Configuration/Webhook`
- **Server**: `default5`
- **Signature**: `def create_porting_webhook_configuration(*, body: Any | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `NumbersV1PortingWebhookConfiguration`
- **Returns (raw)**: `ApiResult[NumbersV1PortingWebhookConfiguration, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NumbersV1PortingWebhookConfiguration` | `twilio_sdk/models/numbers_v1_porting_webhook_configuration.py` |

