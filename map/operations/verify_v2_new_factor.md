<!-- Generated file — do not edit; regenerated with the SDK. -->

# VerifyV2NewFactor — operations

Accessor: `client.verify_v2_new_factor` · Source: `twilio_sdk/apis/verify_v2_new_factor.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.verify_v2_new_factor.create_new_factor

- **Route**: `POST /v2/Services/{ServiceSid}/Entities/{Identity}/Factors`
- **Server**: `default3`
- **Signature**: `def create_new_factor(service_sid: str, identity: str, friendly_name: str, factor_type: NewFactorEnumFactorTypesOrStr, *, binding_alg: str | None = None, binding_public_key: str | None = None, config_app_id: str | None = None, config_notification_platform: NewFactorEnumNotificationPlatformsOrStr | None = None, config_notification_token: str | None = None, config_sdk_version: str | None = None, binding_secret: str | None = None, config_time_step: int | None = None, config_skew: int | None = None, config_code_length: int | None = None, config_alg: NewFactorEnumTotpAlgorithmsOrStr | None = None, metadata: Any | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `identity`, `friendly_name`, `factor_type`
- **Params**: `service_sid` — path `ServiceSid` · `identity` — path `Identity` · `friendly_name` — form field `FriendlyName` · `factor_type` — form field `FactorType` · `binding_alg` — form field `Binding.Alg` · `binding_public_key` — form field `Binding.PublicKey` · `config_app_id` — form field `Config.AppId` · `config_notification_platform` — form field `Config.NotificationPlatform` · `config_notification_token` — form field `Config.NotificationToken` · `config_sdk_version` — form field `Config.SdkVersion` · `binding_secret` — form field `Binding.Secret` · `config_time_step` — form field `Config.TimeStep` · `config_skew` — form field `Config.Skew` · `config_code_length` — form field `Config.CodeLength` · `config_alg` — form field `Config.Alg` · `metadata` — form field `Metadata`
- **Returns (parsed)**: `VerifyV2ServiceEntityNewFactor`
- **Returns (raw)**: `ApiResult[VerifyV2ServiceEntityNewFactor, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NewFactorEnumFactorTypesOrStr` | `twilio_sdk/models/enums/new_factor_enum_factor_types.py` |
| `NewFactorEnumNotificationPlatformsOrStr` | `twilio_sdk/models/enums/new_factor_enum_notification_platforms.py` |
| `NewFactorEnumTotpAlgorithmsOrStr` | `twilio_sdk/models/enums/new_factor_enum_totp_algorithms.py` |
| `VerifyV2ServiceEntityNewFactor` | `twilio_sdk/models/verify_v2_service_entity_new_factor.py` |

### client.verify_v2_new_factor.create_new_factor_passkey

- **Route**: `POST /v2/Services/{ServiceSid}/Passkeys/Factors`
- **Server**: `default3`
- **Signature**: `def create_new_factor_passkey(service_sid: str, body: CreateNewPasskeysFactorRequest | CreateNewPasskeysFactorRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `body`
- **Params**: `service_sid` — path `ServiceSid` · `body` — JSON body
- **Returns (parsed)**: `V2ServicesPasskeysFactorsResponse`
- **Returns (raw)**: `ApiResult[V2ServicesPasskeysFactorsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateNewPasskeysFactorRequest` | `twilio_sdk/models/create_new_passkeys_factor_request.py` |
| `CreateNewPasskeysFactorRequestDict` | `twilio_sdk/models/create_new_passkeys_factor_request.py` |
| `V2ServicesPasskeysFactorsResponse` | `twilio_sdk/models/v2_services_passkeys_factors_response.py` |

