<!-- Generated file — do not edit; regenerated with the SDK. -->

# StudioV2FlowTestUserApi — operations

Accessor: `client.studio_v2_flow_test_user_api` · Source: `twilio_sdk/apis/studio_v2_flow_test_user_api.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.studio_v2_flow_test_user_api.fetch_test_user

- **Route**: `GET /v2/Flows/{Sid}/TestUsers`
- **Auth**: `account_sid_auth_token`
- **Server**: `default11`
- **Signature**: `def fetch_test_user(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `StudioV2FlowTestUser`
- **Returns (raw)**: `ApiResult[StudioV2FlowTestUser, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StudioV2FlowTestUser` | `twilio_sdk/models/studio_v2_flow_test_user.py` |

### client.studio_v2_flow_test_user_api.update_test_user

- **Route**: `POST /v2/Flows/{Sid}/TestUsers`
- **Auth**: `account_sid_auth_token`
- **Server**: `default11`
- **Signature**: `def update_test_user(sid: str, test_users: list[str], *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`, `test_users`
- **Params**: `sid` — path `Sid` · `test_users` — form field `TestUsers`
- **Returns (parsed)**: `StudioV2FlowTestUser`
- **Returns (raw)**: `ApiResult[StudioV2FlowTestUser, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StudioV2FlowTestUser` | `twilio_sdk/models/studio_v2_flow_test_user.py` |

