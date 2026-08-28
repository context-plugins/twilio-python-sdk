<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401Application — operations

Accessor: `client.api20100401_application` · Source: `twilio/apis/api20100401_application.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.api20100401_application.create_application

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/Applications.json`
- **Server**: `default`
- **Signature**: `def create_application(account_sid: str, *, api_version: str | None = None, voice_url: str | None = None, voice_method: VoiceMethod7OrStr | None = None, voice_fallback_url: str | None = None, voice_fallback_method: VoiceFallbackMethod7OrStr | None = None, status_callback: str | None = None, status_callback_method: StatusCallbackMethod6OrStr | None = None, voice_caller_id_lookup: bool | None = None, sms_url: str | None = None, sms_method: SmsMethod7OrStr | None = None, sms_fallback_url: str | None = None, sms_fallback_method: SmsFallbackMethod7OrStr | None = None, sms_status_callback: str | None = None, message_status_callback: str | None = None, friendly_name: str | None = None, public_application_connect_enabled: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`
- **Params**: `account_sid` — path `AccountSid` · `api_version` — form field `ApiVersion` · `voice_url` — form field `VoiceUrl` · `voice_method` — form field `VoiceMethod` · `voice_fallback_url` — form field `VoiceFallbackUrl` · `voice_fallback_method` — form field `VoiceFallbackMethod` · `status_callback` — form field `StatusCallback` · `status_callback_method` — form field `StatusCallbackMethod` · `voice_caller_id_lookup` — form field `VoiceCallerIdLookup` · `sms_url` — form field `SmsUrl` · `sms_method` — form field `SmsMethod` · `sms_fallback_url` — form field `SmsFallbackUrl` · `sms_fallback_method` — form field `SmsFallbackMethod` · `sms_status_callback` — form field `SmsStatusCallback` · `message_status_callback` — form field `MessageStatusCallback` · `friendly_name` — form field `FriendlyName` · `public_application_connect_enabled` — form field `PublicApplicationConnectEnabled`
- **Returns (parsed)**: `ApiV2010AccountApplication`
- **Returns (raw)**: `ApiResult[ApiV2010AccountApplication, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VoiceMethod7OrStr` | `twilio/models/enums/voice_method7.py` |
| `VoiceFallbackMethod7OrStr` | `twilio/models/enums/voice_fallback_method7.py` |
| `StatusCallbackMethod6OrStr` | `twilio/models/enums/status_callback_method6.py` |
| `SmsMethod7OrStr` | `twilio/models/enums/sms_method7.py` |
| `SmsFallbackMethod7OrStr` | `twilio/models/enums/sms_fallback_method7.py` |
| `ApiV2010AccountApplication` | `twilio/models/api_v2010_account_application.py` |

### client.api20100401_application.delete_application

- **Route**: `DELETE /2010-04-01/Accounts/{AccountSid}/Applications/{Sid}.json`
- **Server**: `default`
- **Signature**: `def delete_application(account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.api20100401_application.fetch_application

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/Applications/{Sid}.json`
- **Server**: `default`
- **Signature**: `def fetch_application(account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ApiV2010AccountApplication`
- **Returns (raw)**: `ApiResult[ApiV2010AccountApplication, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountApplication` | `twilio/models/api_v2010_account_application.py` |

### client.api20100401_application.list_application

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/Applications.json`
- **Server**: `default`
- **Signature**: `def list_application(account_sid: str, *, friendly_name: str | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`
- **Params**: `account_sid` — path `AccountSid` · `friendly_name` — query `FriendlyName` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListApplicationResponse`
- **Returns (raw)**: `ApiResult[ListApplicationResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListApplicationResponse` | `twilio/models/list_application_response.py` |

### client.api20100401_application.update_application

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/Applications/{Sid}.json`
- **Server**: `default`
- **Signature**: `def update_application(account_sid: str, sid: str, *, friendly_name: str | None = None, api_version: str | None = None, voice_url: str | None = None, voice_method: VoiceMethod7OrStr | None = None, voice_fallback_url: str | None = None, voice_fallback_method: VoiceFallbackMethod7OrStr | None = None, status_callback: str | None = None, status_callback_method: StatusCallbackMethod6OrStr | None = None, voice_caller_id_lookup: bool | None = None, sms_url: str | None = None, sms_method: SmsMethod7OrStr | None = None, sms_fallback_url: str | None = None, sms_fallback_method: SmsFallbackMethod7OrStr | None = None, sms_status_callback: str | None = None, message_status_callback: str | None = None, public_application_connect_enabled: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid` · `friendly_name` — form field `FriendlyName` · `api_version` — form field `ApiVersion` · `voice_url` — form field `VoiceUrl` · `voice_method` — form field `VoiceMethod` · `voice_fallback_url` — form field `VoiceFallbackUrl` · `voice_fallback_method` — form field `VoiceFallbackMethod` · `status_callback` — form field `StatusCallback` · `status_callback_method` — form field `StatusCallbackMethod` · `voice_caller_id_lookup` — form field `VoiceCallerIdLookup` · `sms_url` — form field `SmsUrl` · `sms_method` — form field `SmsMethod` · `sms_fallback_url` — form field `SmsFallbackUrl` · `sms_fallback_method` — form field `SmsFallbackMethod` · `sms_status_callback` — form field `SmsStatusCallback` · `message_status_callback` — form field `MessageStatusCallback` · `public_application_connect_enabled` — form field `PublicApplicationConnectEnabled`
- **Returns (parsed)**: `ApiV2010AccountApplication`
- **Returns (raw)**: `ApiResult[ApiV2010AccountApplication, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VoiceMethod7OrStr` | `twilio/models/enums/voice_method7.py` |
| `VoiceFallbackMethod7OrStr` | `twilio/models/enums/voice_fallback_method7.py` |
| `StatusCallbackMethod6OrStr` | `twilio/models/enums/status_callback_method6.py` |
| `SmsMethod7OrStr` | `twilio/models/enums/sms_method7.py` |
| `SmsFallbackMethod7OrStr` | `twilio/models/enums/sms_fallback_method7.py` |
| `ApiV2010AccountApplication` | `twilio/models/api_v2010_account_application.py` |

