<!-- Generated file — do not edit; regenerated with the SDK. -->

# VerifyV2AccessToken — operations

Accessor: `client.verify_v2_access_token` · Source: `twilio_sdk/apis/verify_v2_access_token.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.verify_v2_access_token.create_access_token

- **Route**: `POST /v2/Services/{ServiceSid}/AccessTokens`
- **Auth**: `account_sid_auth_token`
- **Server**: `default3`
- **Signature**: `def create_access_token(service_sid: str, identity: str, factor_type: AccessTokenEnumFactorTypesOrStr, *, factor_friendly_name: str | None = None, ttl: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `identity`, `factor_type`
- **Params**: `service_sid` — path `ServiceSid` · `identity` — form field `Identity` · `factor_type` — form field `FactorType` · `factor_friendly_name` — form field `FactorFriendlyName` · `ttl` — form field `Ttl`
- **Returns (parsed)**: `VerifyV2ServiceAccessToken`
- **Returns (raw)**: `ApiResult[VerifyV2ServiceAccessToken, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AccessTokenEnumFactorTypesOrStr` | `twilio_sdk/models/enums/access_token_enum_factor_types.py` |
| `VerifyV2ServiceAccessToken` | `twilio_sdk/models/verify_v2_service_access_token.py` |

### client.verify_v2_access_token.fetch_access_token

- **Route**: `GET /v2/Services/{ServiceSid}/AccessTokens/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default3`
- **Signature**: `def fetch_access_token(service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `sid`
- **Params**: `service_sid` — path `ServiceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `VerifyV2ServiceAccessToken`
- **Returns (raw)**: `ApiResult[VerifyV2ServiceAccessToken, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VerifyV2ServiceAccessToken` | `twilio_sdk/models/verify_v2_service_access_token.py` |

