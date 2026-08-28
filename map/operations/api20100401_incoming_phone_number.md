<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401IncomingPhoneNumber — operations

Accessor: `client.api20100401_incoming_phone_number` · Source: `twilio_sdk/apis/api20100401_incoming_phone_number.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.api20100401_incoming_phone_number.create_incoming_phone_number

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers.json`
- **Server**: `default`
- **Signature**: `def create_incoming_phone_number(account_sid: str, *, api_version: str | None = None, friendly_name: str | None = None, sms_application_sid: str | None = None, sms_fallback_method: SmsFallbackMethod9OrStr | None = None, sms_fallback_url: AnyUrl | None = None, sms_method: SmsMethod9OrStr | None = None, sms_url: AnyUrl | None = None, status_callback: AnyUrl | None = None, status_callback_method: StatusCallbackMethod10OrStr | None = None, voice_application_sid: str | None = None, voice_caller_id_lookup: bool | None = None, voice_fallback_method: VoiceFallbackMethod9OrStr | None = None, voice_fallback_url: AnyUrl | None = None, voice_method: VoiceMethod9OrStr | None = None, voice_url: AnyUrl | None = None, emergency_status: IncomingPhoneNumberEnumEmergencyStatusOrStr | None = None, emergency_address_sid: str | None = None, trunk_sid: str | None = None, identity_sid: str | None = None, address_sid: str | None = None, voice_receive_mode: IncomingPhoneNumberEnumVoiceReceiveModeOrStr | None = None, bundle_sid: str | None = None, phone_number: str | None = None, area_code: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`
- **Params**: `account_sid` — path `AccountSid` · `api_version` — form field `ApiVersion` · `friendly_name` — form field `FriendlyName` · `sms_application_sid` — form field `SmsApplicationSid` · `sms_fallback_method` — form field `SmsFallbackMethod` · `sms_fallback_url` — form field `SmsFallbackUrl` · `sms_method` — form field `SmsMethod` · `sms_url` — form field `SmsUrl` · `status_callback` — form field `StatusCallback` · `status_callback_method` — form field `StatusCallbackMethod` · `voice_application_sid` — form field `VoiceApplicationSid` · `voice_caller_id_lookup` — form field `VoiceCallerIdLookup` · `voice_fallback_method` — form field `VoiceFallbackMethod` · `voice_fallback_url` — form field `VoiceFallbackUrl` · `voice_method` — form field `VoiceMethod` · `voice_url` — form field `VoiceUrl` · `emergency_status` — form field `EmergencyStatus` · `emergency_address_sid` — form field `EmergencyAddressSid` · `trunk_sid` — form field `TrunkSid` · `identity_sid` — form field `IdentitySid` · `address_sid` — form field `AddressSid` · `voice_receive_mode` — form field `VoiceReceiveMode` · `bundle_sid` — form field `BundleSid` · `phone_number` — form field `PhoneNumber` · `area_code` — form field `AreaCode`
- **Returns (parsed)**: `ApiV2010AccountIncomingPhoneNumber`
- **Returns (raw)**: `ApiResult[ApiV2010AccountIncomingPhoneNumber, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SmsFallbackMethod9OrStr` | `twilio_sdk/models/enums/sms_fallback_method9.py` |
| `SmsMethod9OrStr` | `twilio_sdk/models/enums/sms_method9.py` |
| `StatusCallbackMethod10OrStr` | `twilio_sdk/models/enums/status_callback_method10.py` |
| `VoiceFallbackMethod9OrStr` | `twilio_sdk/models/enums/voice_fallback_method9.py` |
| `VoiceMethod9OrStr` | `twilio_sdk/models/enums/voice_method9.py` |
| `IncomingPhoneNumberEnumEmergencyStatusOrStr` | `twilio_sdk/models/enums/incoming_phone_number_enum_emergency_status.py` |
| `IncomingPhoneNumberEnumVoiceReceiveModeOrStr` | `twilio_sdk/models/enums/incoming_phone_number_enum_voice_receive_mode.py` |
| `ApiV2010AccountIncomingPhoneNumber` | `twilio_sdk/models/api_v2010_account_incoming_phone_number.py` |

### client.api20100401_incoming_phone_number.delete_incoming_phone_number

- **Route**: `DELETE /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{Sid}.json`
- **Server**: `default`
- **Signature**: `def delete_incoming_phone_number(account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.api20100401_incoming_phone_number.fetch_incoming_phone_number

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{Sid}.json`
- **Server**: `default`
- **Signature**: `def fetch_incoming_phone_number(account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ApiV2010AccountIncomingPhoneNumber`
- **Returns (raw)**: `ApiResult[ApiV2010AccountIncomingPhoneNumber, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountIncomingPhoneNumber` | `twilio_sdk/models/api_v2010_account_incoming_phone_number.py` |

### client.api20100401_incoming_phone_number.list_incoming_phone_number

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers.json`
- **Server**: `default`
- **Signature**: `def list_incoming_phone_number(account_sid: str, *, beta: bool | None = None, friendly_name: str | None = None, phone_number: str | None = None, origin: str | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`
- **Params**: `account_sid` — path `AccountSid` · `beta` — query `Beta` · `friendly_name` — query `FriendlyName` · `phone_number` — query `PhoneNumber` · `origin` — query `Origin` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListIncomingPhoneNumberResponse`
- **Returns (raw)**: `ApiResult[ListIncomingPhoneNumberResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListIncomingPhoneNumberResponse` | `twilio_sdk/models/list_incoming_phone_number_response.py` |

### client.api20100401_incoming_phone_number.update_incoming_phone_number

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{Sid}.json`
- **Server**: `default`
- **Signature**: `def update_incoming_phone_number(account_sid_template: str, sid: str, *, account_sid: str | None = None, api_version: str | None = None, friendly_name: str | None = None, sms_application_sid: str | None = None, sms_fallback_method: SmsFallbackMethod9OrStr | None = None, sms_fallback_url: AnyUrl | None = None, sms_method: SmsMethod9OrStr | None = None, sms_url: AnyUrl | None = None, status_callback: AnyUrl | None = None, status_callback_method: StatusCallbackMethod10OrStr | None = None, voice_application_sid: str | None = None, voice_caller_id_lookup: bool | None = None, voice_fallback_method: VoiceFallbackMethod9OrStr | None = None, voice_fallback_url: AnyUrl | None = None, voice_method: VoiceMethod9OrStr | None = None, voice_url: AnyUrl | None = None, emergency_status: IncomingPhoneNumberEnumEmergencyStatusOrStr | None = None, emergency_address_sid: str | None = None, trunk_sid: str | None = None, voice_receive_mode: IncomingPhoneNumberEnumVoiceReceiveModeOrStr | None = None, identity_sid: str | None = None, address_sid: str | None = None, bundle_sid: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid_template`, `sid`
- **Params**: `account_sid_template` — path `AccountSid` · `sid` — path `Sid` · `account_sid` — form field `AccountSid` · `api_version` — form field `ApiVersion` · `friendly_name` — form field `FriendlyName` · `sms_application_sid` — form field `SmsApplicationSid` · `sms_fallback_method` — form field `SmsFallbackMethod` · `sms_fallback_url` — form field `SmsFallbackUrl` · `sms_method` — form field `SmsMethod` · `sms_url` — form field `SmsUrl` · `status_callback` — form field `StatusCallback` · `status_callback_method` — form field `StatusCallbackMethod` · `voice_application_sid` — form field `VoiceApplicationSid` · `voice_caller_id_lookup` — form field `VoiceCallerIdLookup` · `voice_fallback_method` — form field `VoiceFallbackMethod` · `voice_fallback_url` — form field `VoiceFallbackUrl` · `voice_method` — form field `VoiceMethod` · `voice_url` — form field `VoiceUrl` · `emergency_status` — form field `EmergencyStatus` · `emergency_address_sid` — form field `EmergencyAddressSid` · `trunk_sid` — form field `TrunkSid` · `voice_receive_mode` — form field `VoiceReceiveMode` · `identity_sid` — form field `IdentitySid` · `address_sid` — form field `AddressSid` · `bundle_sid` — form field `BundleSid`
- **Returns (parsed)**: `ApiV2010AccountIncomingPhoneNumber`
- **Returns (raw)**: `ApiResult[ApiV2010AccountIncomingPhoneNumber, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SmsFallbackMethod9OrStr` | `twilio_sdk/models/enums/sms_fallback_method9.py` |
| `SmsMethod9OrStr` | `twilio_sdk/models/enums/sms_method9.py` |
| `StatusCallbackMethod10OrStr` | `twilio_sdk/models/enums/status_callback_method10.py` |
| `VoiceFallbackMethod9OrStr` | `twilio_sdk/models/enums/voice_fallback_method9.py` |
| `VoiceMethod9OrStr` | `twilio_sdk/models/enums/voice_method9.py` |
| `IncomingPhoneNumberEnumEmergencyStatusOrStr` | `twilio_sdk/models/enums/incoming_phone_number_enum_emergency_status.py` |
| `IncomingPhoneNumberEnumVoiceReceiveModeOrStr` | `twilio_sdk/models/enums/incoming_phone_number_enum_voice_receive_mode.py` |
| `ApiV2010AccountIncomingPhoneNumber` | `twilio_sdk/models/api_v2010_account_incoming_phone_number.py` |

