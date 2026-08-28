<!-- Generated file — do not edit; regenerated with the SDK. -->

# FlexV2FlexUserApi — operations

Accessor: `client.flex_v2_flex_user_api` · Source: `twilio_sdk/apis/flex_v2_flex_user_api.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.flex_v2_flex_user_api.fetch_flex_user

- **Route**: `GET /v2/Instances/{InstanceSid}/Users/{FlexUserSid}`
- **Server**: `default13`
- **Signature**: `def fetch_flex_user(instance_sid: str, flex_user_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `instance_sid`, `flex_user_sid`
- **Params**: `instance_sid` — path `InstanceSid` · `flex_user_sid` — path `FlexUserSid`
- **Returns (parsed)**: `FlexV2FlexUser`
- **Returns (raw)**: `ApiResult[FlexV2FlexUser, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV2FlexUser` | `twilio_sdk/models/flex_v2_flex_user.py` |

### client.flex_v2_flex_user_api.update_flex_user

- **Route**: `POST /v2/Instances/{InstanceSid}/Users/{FlexUserSid}`
- **Server**: `default13`
- **Signature**: `def update_flex_user(instance_sid: str, flex_user_sid: str, *, email: str | None = None, user_sid: str | None = None, locale: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `instance_sid`, `flex_user_sid`
- **Params**: `instance_sid` — path `InstanceSid` · `flex_user_sid` — path `FlexUserSid` · `email` — form field `Email` · `user_sid` — form field `UserSid` · `locale` — form field `Locale`
- **Returns (parsed)**: `FlexV2FlexUser`
- **Returns (raw)**: `ApiResult[FlexV2FlexUser, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV2FlexUser` | `twilio_sdk/models/flex_v2_flex_user.py` |

