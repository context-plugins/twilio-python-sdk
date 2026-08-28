<!-- Generated file — do not edit; regenerated with the SDK. -->

# InsightsV1Setting — operations

Accessor: `client.insights_v1_setting` · Source: `twilio_sdk/apis/insights_v1_setting.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.insights_v1_setting.fetch_account_settings

- **Route**: `GET /v1/Voice/Settings`
- **Server**: `default14`
- **Signature**: `def fetch_account_settings(*, subaccount_sid: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `subaccount_sid` — query `SubaccountSid`
- **Returns (parsed)**: `InsightsV1AccountSettings`
- **Returns (raw)**: `ApiResult[InsightsV1AccountSettings, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InsightsV1AccountSettings` | `twilio_sdk/models/insights_v1_account_settings.py` |

### client.insights_v1_setting.update_account_settings

- **Route**: `POST /v1/Voice/Settings`
- **Server**: `default14`
- **Signature**: `def update_account_settings(*, advanced_features: bool | None = None, voice_trace: bool | None = None, subaccount_sid: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `advanced_features` — form field `AdvancedFeatures` · `voice_trace` — form field `VoiceTrace` · `subaccount_sid` — form field `SubaccountSid`
- **Returns (parsed)**: `InsightsV1AccountSettings`
- **Returns (raw)**: `ApiResult[InsightsV1AccountSettings, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InsightsV1AccountSettings` | `twilio_sdk/models/insights_v1_account_settings.py` |

