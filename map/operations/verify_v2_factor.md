<!-- Generated file — do not edit; regenerated with the SDK. -->

# VerifyV2Factor — operations

Accessor: `client.verify_v2_factor` · Source: `twilio/apis/verify_v2_factor.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.verify_v2_factor.delete_factor

- **Route**: `DELETE /v2/Services/{ServiceSid}/Entities/{Identity}/Factors/{Sid}`
- **Server**: `default3`
- **Signature**: `def delete_factor(service_sid: str, identity: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `identity`, `sid`
- **Params**: `service_sid` — path `ServiceSid` · `identity` — path `Identity` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.verify_v2_factor.fetch_factor

- **Route**: `GET /v2/Services/{ServiceSid}/Entities/{Identity}/Factors/{Sid}`
- **Server**: `default3`
- **Signature**: `def fetch_factor(service_sid: str, identity: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `identity`, `sid`
- **Params**: `service_sid` — path `ServiceSid` · `identity` — path `Identity` · `sid` — path `Sid`
- **Returns (parsed)**: `VerifyV2ServiceEntityFactor`
- **Returns (raw)**: `ApiResult[VerifyV2ServiceEntityFactor, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VerifyV2ServiceEntityFactor` | `twilio/models/verify_v2_service_entity_factor.py` |

### client.verify_v2_factor.list_factor

- **Route**: `GET /v2/Services/{ServiceSid}/Entities/{Identity}/Factors`
- **Server**: `default3`
- **Signature**: `def list_factor(service_sid: str, identity: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `identity`
- **Params**: `service_sid` — path `ServiceSid` · `identity` — path `Identity` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListFactorResponse`
- **Returns (raw)**: `ApiResult[ListFactorResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListFactorResponse` | `twilio/models/list_factor_response.py` |

### client.verify_v2_factor.update_factor

- **Route**: `POST /v2/Services/{ServiceSid}/Entities/{Identity}/Factors/{Sid}`
- **Server**: `default3`
- **Signature**: `def update_factor(service_sid: str, identity: str, sid: str, *, auth_payload: str | None = None, friendly_name: str | None = None, config_notification_token: str | None = None, config_sdk_version: str | None = None, config_time_step: int | None = None, config_skew: int | None = None, config_code_length: int | None = None, config_alg: FactorEnumTotpAlgorithmsOrStr | None = None, config_notification_platform: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `identity`, `sid`
- **Params**: `service_sid` — path `ServiceSid` · `identity` — path `Identity` · `sid` — path `Sid` · `auth_payload` — form field `AuthPayload` · `friendly_name` — form field `FriendlyName` · `config_notification_token` — form field `Config.NotificationToken` · `config_sdk_version` — form field `Config.SdkVersion` · `config_time_step` — form field `Config.TimeStep` · `config_skew` — form field `Config.Skew` · `config_code_length` — form field `Config.CodeLength` · `config_alg` — form field `Config.Alg` · `config_notification_platform` — form field `Config.NotificationPlatform`
- **Returns (parsed)**: `VerifyV2ServiceEntityFactor`
- **Returns (raw)**: `ApiResult[VerifyV2ServiceEntityFactor, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FactorEnumTotpAlgorithmsOrStr` | `twilio/models/enums/factor_enum_totp_algorithms.py` |
| `VerifyV2ServiceEntityFactor` | `twilio/models/verify_v2_service_entity_factor.py` |

