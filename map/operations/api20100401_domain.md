<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401Domain — operations

Accessor: `client.api20100401_domain` · Source: `twilio_sdk/apis/api20100401_domain.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.api20100401_domain.create_sip_domain

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/SIP/Domains.json`
- **Server**: `default`
- **Signature**: `def create_sip_domain(account_sid: str, domain_name: str, *, friendly_name: str | None = None, voice_url: AnyUrl | None = None, voice_method: VoiceMethod7OrStr | None = None, voice_fallback_url: AnyUrl | None = None, voice_fallback_method: VoiceFallbackMethod7OrStr | None = None, voice_status_callback_url: AnyUrl | None = None, voice_status_callback_method: VoiceStatusCallbackMethod1OrStr | None = None, sip_registration: bool | None = None, emergency_calling_enabled: bool | None = None, secure: bool | None = None, byoc_trunk_sid: str | None = None, emergency_caller_sid: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `domain_name`
- **Params**: `account_sid` — path `AccountSid` · `domain_name` — form field `DomainName` · `friendly_name` — form field `FriendlyName` · `voice_url` — form field `VoiceUrl` · `voice_method` — form field `VoiceMethod` · `voice_fallback_url` — form field `VoiceFallbackUrl` · `voice_fallback_method` — form field `VoiceFallbackMethod` · `voice_status_callback_url` — form field `VoiceStatusCallbackUrl` · `voice_status_callback_method` — form field `VoiceStatusCallbackMethod` · `sip_registration` — form field `SipRegistration` · `emergency_calling_enabled` — form field `EmergencyCallingEnabled` · `secure` — form field `Secure` · `byoc_trunk_sid` — form field `ByocTrunkSid` · `emergency_caller_sid` — form field `EmergencyCallerSid`
- **Returns (parsed)**: `ApiV2010AccountSipSipDomain`
- **Returns (raw)**: `ApiResult[ApiV2010AccountSipSipDomain, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VoiceMethod7OrStr` | `twilio_sdk/models/enums/voice_method7.py` |
| `VoiceFallbackMethod7OrStr` | `twilio_sdk/models/enums/voice_fallback_method7.py` |
| `VoiceStatusCallbackMethod1OrStr` | `twilio_sdk/models/enums/voice_status_callback_method1.py` |
| `ApiV2010AccountSipSipDomain` | `twilio_sdk/models/api_v2010_account_sip_sip_domain.py` |

### client.api20100401_domain.delete_sip_domain

- **Route**: `DELETE /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{Sid}.json`
- **Server**: `default`
- **Signature**: `def delete_sip_domain(account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.api20100401_domain.fetch_sip_domain

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{Sid}.json`
- **Server**: `default`
- **Signature**: `def fetch_sip_domain(account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ApiV2010AccountSipSipDomain`
- **Returns (raw)**: `ApiResult[ApiV2010AccountSipSipDomain, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountSipSipDomain` | `twilio_sdk/models/api_v2010_account_sip_sip_domain.py` |

### client.api20100401_domain.list_sip_domain

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/SIP/Domains.json`
- **Server**: `default`
- **Signature**: `def list_sip_domain(account_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`
- **Params**: `account_sid` — path `AccountSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListSipDomainResponse`
- **Returns (raw)**: `ApiResult[ListSipDomainResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListSipDomainResponse` | `twilio_sdk/models/list_sip_domain_response.py` |

### client.api20100401_domain.update_sip_domain

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{Sid}.json`
- **Server**: `default`
- **Signature**: `def update_sip_domain(account_sid: str, sid: str, *, friendly_name: str | None = None, voice_fallback_method: VoiceFallbackMethod7OrStr | None = None, voice_fallback_url: AnyUrl | None = None, voice_method: VoiceMethod15OrStr | None = None, voice_status_callback_method: VoiceStatusCallbackMethod1OrStr | None = None, voice_status_callback_url: AnyUrl | None = None, voice_url: AnyUrl | None = None, sip_registration: bool | None = None, domain_name: str | None = None, emergency_calling_enabled: bool | None = None, secure: bool | None = None, byoc_trunk_sid: str | None = None, emergency_caller_sid: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid` · `friendly_name` — form field `FriendlyName` · `voice_fallback_method` — form field `VoiceFallbackMethod` · `voice_fallback_url` — form field `VoiceFallbackUrl` · `voice_method` — form field `VoiceMethod` · `voice_status_callback_method` — form field `VoiceStatusCallbackMethod` · `voice_status_callback_url` — form field `VoiceStatusCallbackUrl` · `voice_url` — form field `VoiceUrl` · `sip_registration` — form field `SipRegistration` · `domain_name` — form field `DomainName` · `emergency_calling_enabled` — form field `EmergencyCallingEnabled` · `secure` — form field `Secure` · `byoc_trunk_sid` — form field `ByocTrunkSid` · `emergency_caller_sid` — form field `EmergencyCallerSid`
- **Returns (parsed)**: `ApiV2010AccountSipSipDomain`
- **Returns (raw)**: `ApiResult[ApiV2010AccountSipSipDomain, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VoiceFallbackMethod7OrStr` | `twilio_sdk/models/enums/voice_fallback_method7.py` |
| `VoiceMethod15OrStr` | `twilio_sdk/models/enums/voice_method15.py` |
| `VoiceStatusCallbackMethod1OrStr` | `twilio_sdk/models/enums/voice_status_callback_method1.py` |
| `ApiV2010AccountSipSipDomain` | `twilio_sdk/models/api_v2010_account_sip_sip_domain.py` |

