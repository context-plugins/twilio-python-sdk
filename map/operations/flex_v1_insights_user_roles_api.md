<!-- Generated file — do not edit; regenerated with the SDK. -->

# FlexV1InsightsUserRolesApi — operations

Accessor: `client.flex_v1_insights_user_roles_api` · Source: `twilio_sdk/apis/flex_v1_insights_user_roles_api.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.flex_v1_insights_user_roles_api.fetch_insights_user_roles

- **Route**: `GET /v1/Insights/UserRoles`
- **Auth**: `account_sid_auth_token`
- **Server**: `default13`
- **Signature**: `def fetch_insights_user_roles(*, authorization: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `authorization` — header `Authorization`
- **Returns (parsed)**: `FlexV1InsightsUserRoles`
- **Returns (raw)**: `ApiResult[FlexV1InsightsUserRoles, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1InsightsUserRoles` | `twilio_sdk/models/flex_v1_insights_user_roles.py` |

