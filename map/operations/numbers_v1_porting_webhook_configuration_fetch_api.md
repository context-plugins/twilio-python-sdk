<!-- Generated file — do not edit; regenerated with the SDK. -->

# NumbersV1PortingWebhookConfigurationFetchApi — operations

Accessor: `client.numbers_v1_porting_webhook_configuration_fetch_api` · Source: `twilio_sdk/apis/numbers_v1_porting_webhook_configuration_fetch_api.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.numbers_v1_porting_webhook_configuration_fetch_api.fetch_porting_webhook_configuration_fetch

- **Route**: `GET /v1/Porting/Configuration/Webhook`
- **Auth**: `account_sid_auth_token`
- **Server**: `default5`
- **Signature**: `def fetch_porting_webhook_configuration_fetch(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `NumbersV1PortingWebhookConfigurationFetch`
- **Returns (raw)**: `ApiResult[NumbersV1PortingWebhookConfigurationFetch, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NumbersV1PortingWebhookConfigurationFetch` | `twilio_sdk/models/numbers_v1_porting_webhook_configuration_fetch.py` |

