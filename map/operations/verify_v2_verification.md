<!-- Generated file — do not edit; regenerated with the SDK. -->

# VerifyV2Verification — operations

Accessor: `client.verify_v2_verification` · Source: `twilio_sdk/apis/verify_v2_verification.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.verify_v2_verification.create_verification

- **Route**: `POST /v2/Services/{ServiceSid}/Verifications`
- **Auth**: `account_sid_auth_token`
- **Server**: `default3`
- **Signature**: `def create_verification(service_sid: str, to: str, channel: str, *, custom_friendly_name: str | None = None, custom_message: str | None = None, send_digits: str | None = None, locale: str | None = None, custom_code: str | None = None, amount: str | None = None, payee: str | None = None, rate_limits: Any | None = None, channel_configuration: Any | None = None, app_hash: str | None = None, template_sid: str | None = None, template_custom_substitutions: str | None = None, device_ip: str | None = None, enable_sna_client_token: bool | None = None, risk_check: MessageEnumRiskCheckOrStr | None = None, tags: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `to`, `channel`
- **Params**: `service_sid` — path `ServiceSid` · `to` — form field `To` · `channel` — form field `Channel` · `custom_friendly_name` — form field `CustomFriendlyName` · `custom_message` — form field `CustomMessage` · `send_digits` — form field `SendDigits` · `locale` — form field `Locale` · `custom_code` — form field `CustomCode` · `amount` — form field `Amount` · `payee` — form field `Payee` · `rate_limits` — form field `RateLimits` · `channel_configuration` — form field `ChannelConfiguration` · `app_hash` — form field `AppHash` · `template_sid` — form field `TemplateSid` · `template_custom_substitutions` — form field `TemplateCustomSubstitutions` · `device_ip` — form field `DeviceIp` · `enable_sna_client_token` — form field `EnableSnaClientToken` · `risk_check` — form field `RiskCheck` · `tags` — form field `Tags`
- **Returns (parsed)**: `VerifyV2ServiceVerification`
- **Returns (raw)**: `ApiResult[VerifyV2ServiceVerification, CreateVerificationErrorBody]`
- **Error**: `CreateVerificationErrorBody` — **Case A (typed)**
- **Error arms**: `AccountsCallsRecordingsSidJson201041408Error1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MessageEnumRiskCheckOrStr` | `twilio_sdk/models/enums/message_enum_risk_check.py` |
| `VerifyV2ServiceVerification` | `twilio_sdk/models/verify_v2_service_verification.py` |
| `CreateVerificationErrorBody` | `twilio_sdk/errors/create_verification_error.py` |
| `AccountsCallsRecordingsSidJson201041408Error1` | `twilio_sdk/models/accounts_calls_recordings_sid_json201041408_error1.py` |

### client.verify_v2_verification.fetch_verification

- **Route**: `GET /v2/Services/{ServiceSid}/Verifications/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default3`
- **Signature**: `def fetch_verification(service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `sid`
- **Params**: `service_sid` — path `ServiceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `VerifyV2ServiceVerification`
- **Returns (raw)**: `ApiResult[VerifyV2ServiceVerification, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VerifyV2ServiceVerification` | `twilio_sdk/models/verify_v2_service_verification.py` |

### client.verify_v2_verification.update_verification

- **Route**: `POST /v2/Services/{ServiceSid}/Verifications/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default3`
- **Signature**: `def update_verification(service_sid: str, sid: str, status: VerificationEnumStatusOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `sid`, `status`
- **Params**: `service_sid` — path `ServiceSid` · `sid` — path `Sid` · `status` — form field `Status`
- **Returns (parsed)**: `VerifyV2ServiceVerification`
- **Returns (raw)**: `ApiResult[VerifyV2ServiceVerification, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VerificationEnumStatusOrStr` | `twilio_sdk/models/enums/verification_enum_status.py` |
| `VerifyV2ServiceVerification` | `twilio_sdk/models/verify_v2_service_verification.py` |

