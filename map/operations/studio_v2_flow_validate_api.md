<!-- Generated file — do not edit; regenerated with the SDK. -->

# StudioV2FlowValidateApi — operations

Accessor: `client.studio_v2_flow_validate_api` · Source: `twilio_sdk/apis/studio_v2_flow_validate_api.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.studio_v2_flow_validate_api.update_flow_validate

- **Route**: `POST /v2/Flows/Validate`
- **Auth**: `account_sid_auth_token`
- **Server**: `default11`
- **Signature**: `def update_flow_validate(friendly_name: str, status: FlowEnumStatusOrStr, definition: Any, *, commit_message: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `friendly_name`, `status`, `definition`
- **Params**: `friendly_name` — form field `FriendlyName` · `status` — form field `Status` · `definition` — form field `Definition` · `commit_message` — form field `CommitMessage`
- **Returns (parsed)**: `StudioV2FlowValidate`
- **Returns (raw)**: `ApiResult[StudioV2FlowValidate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlowEnumStatusOrStr` | `twilio_sdk/models/enums/flow_enum_status.py` |
| `StudioV2FlowValidate` | `twilio_sdk/models/studio_v2_flow_validate.py` |

