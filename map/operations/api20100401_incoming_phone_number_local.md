<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401IncomingPhoneNumberLocal — operations

Accessor: `client.api20100401_incoming_phone_number_local` · Source: `twilio/apis/api20100401_incoming_phone_number_local.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.api20100401_incoming_phone_number_local.create_incoming_phone_number_local

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/Local.json`
- **Server**: `default`
- **Signature**: `def create_incoming_phone_number_local(account_sid: str, phone_number: str, *, api_version: str | None = None, friendly_name: str | None = None, sms_application_sid: str | None = None, sms_fallback_method: SmsFallbackMethod9OrStr | None = None, sms_fallback_url: str | None = None, sms_method: SmsMethod9OrStr | None = None, sms_url: str | None = None, status_callback: str | None = None, status_callback_method: StatusCallbackMethod10OrStr | None = None, voice_application_sid: str | None = None, voice_caller_id_lookup: bool | None = None, voice_fallback_method: VoiceFallbackMethod9OrStr | None = None, voice_fallback_url: str | None = None, voice_method: VoiceMethod9OrStr | None = None, voice_url: str | None = None, identity_sid: str | None = None, address_sid: str | None = None, emergency_status: IncomingPhoneNumberLocalEnumEmergencyStatusOrStr | None = None, emergency_address_sid: str | None = None, trunk_sid: str | None = None, voice_receive_mode: IncomingPhoneNumberLocalEnumVoiceReceiveModeOrStr | None = None, bundle_sid: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `phone_number`
- **Params**: `account_sid` — path `AccountSid` · `phone_number` — form field `PhoneNumber` · `api_version` — form field `ApiVersion` · `friendly_name` — form field `FriendlyName` · `sms_application_sid` — form field `SmsApplicationSid` · `sms_fallback_method` — form field `SmsFallbackMethod` · `sms_fallback_url` — form field `SmsFallbackUrl` · `sms_method` — form field `SmsMethod` · `sms_url` — form field `SmsUrl` · `status_callback` — form field `StatusCallback` · `status_callback_method` — form field `StatusCallbackMethod` · `voice_application_sid` — form field `VoiceApplicationSid` · `voice_caller_id_lookup` — form field `VoiceCallerIdLookup` · `voice_fallback_method` — form field `VoiceFallbackMethod` · `voice_fallback_url` — form field `VoiceFallbackUrl` · `voice_method` — form field `VoiceMethod` · `voice_url` — form field `VoiceUrl` · `identity_sid` — form field `IdentitySid` · `address_sid` — form field `AddressSid` · `emergency_status` — form field `EmergencyStatus` · `emergency_address_sid` — form field `EmergencyAddressSid` · `trunk_sid` — form field `TrunkSid` · `voice_receive_mode` — form field `VoiceReceiveMode` · `bundle_sid` — form field `BundleSid`
- **Returns (parsed)**: `ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberLocal`
- **Returns (raw)**: `ApiResult[ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberLocal, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SmsFallbackMethod9OrStr` | `twilio/models/enums/sms_fallback_method9.py` |
| `SmsMethod9OrStr` | `twilio/models/enums/sms_method9.py` |
| `StatusCallbackMethod10OrStr` | `twilio/models/enums/status_callback_method10.py` |
| `VoiceFallbackMethod9OrStr` | `twilio/models/enums/voice_fallback_method9.py` |
| `VoiceMethod9OrStr` | `twilio/models/enums/voice_method9.py` |
| `IncomingPhoneNumberLocalEnumEmergencyStatusOrStr` | `twilio/models/enums/incoming_phone_number_local_enum_emergency_status.py` |
| `IncomingPhoneNumberLocalEnumVoiceReceiveModeOrStr` | `twilio/models/enums/incoming_phone_number_local_enum_voice_receive_mode.py` |
| `ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberLocal` | `twilio/models/api_v2010_account_incoming_phone_number_incoming_phone_number_local.py` |

### client.api20100401_incoming_phone_number_local.list_incoming_phone_number_local

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/Local.json`
- **Server**: `default`
- **Signature**: `def list_incoming_phone_number_local(account_sid: str, *, beta: bool | None = None, friendly_name: str | None = None, phone_number: str | None = None, origin: str | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`
- **Params**: `account_sid` — path `AccountSid` · `beta` — query `Beta` · `friendly_name` — query `FriendlyName` · `phone_number` — query `PhoneNumber` · `origin` — query `Origin` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListIncomingPhoneNumberLocalResponse`
- **Returns (raw)**: `ApiResult[ListIncomingPhoneNumberLocalResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListIncomingPhoneNumberLocalResponse` | `twilio/models/list_incoming_phone_number_local_response.py` |

