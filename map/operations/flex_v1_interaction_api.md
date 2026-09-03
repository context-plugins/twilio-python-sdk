<!-- Generated file — do not edit; regenerated with the SDK. -->

# FlexV1InteractionApi — operations

Accessor: `client.flex_v1_interaction_api` · Source: `twilio_sdk/apis/flex_v1_interaction_api.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.flex_v1_interaction_api.create_interaction

- **Route**: `POST /v1/Interactions`
- **Auth**: `account_sid_auth_token`
- **Server**: `default13`
- **Signature**: `def create_interaction(channel: Any, *, routing: Any | None = None, interaction_context_sid: str | None = None, webhook_ttid: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel`
- **Params**: `channel` — form field `Channel` · `routing` — form field `Routing` · `interaction_context_sid` — form field `InteractionContextSid` · `webhook_ttid` — form field `WebhookTtid`
- **Returns (parsed)**: `FlexV1Interaction`
- **Returns (raw)**: `ApiResult[FlexV1Interaction, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1Interaction` | `twilio_sdk/models/flex_v1_interaction.py` |

### client.flex_v1_interaction_api.fetch_interaction2

- **Route**: `GET /v1/Interactions/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default13`
- **Signature**: `def fetch_interaction2(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `FlexV1Interaction`
- **Returns (raw)**: `ApiResult[FlexV1Interaction, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1Interaction` | `twilio_sdk/models/flex_v1_interaction.py` |

### client.flex_v1_interaction_api.update_interaction

- **Route**: `POST /v1/Interactions/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default13`
- **Signature**: `def update_interaction(sid: str, *, webhook_ttid: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid` · `webhook_ttid` — form field `WebhookTtid`
- **Returns (parsed)**: `FlexV1Interaction`
- **Returns (raw)**: `ApiResult[FlexV1Interaction, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1Interaction` | `twilio_sdk/models/flex_v1_interaction.py` |

