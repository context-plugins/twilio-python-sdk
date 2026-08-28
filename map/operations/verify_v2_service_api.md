<!-- Generated file — do not edit; regenerated with the SDK. -->

# VerifyV2ServiceApi — operations

Accessor: `client.verify_v2_service_api` · Source: `twilio/apis/verify_v2_service_api.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.verify_v2_service_api.create_service2

- **Route**: `POST /v2/Services`
- **Server**: `default3`
- **Signature**: `def create_service2(friendly_name: str, *, code_length: int | None = None, lookup_enabled: bool | None = None, skip_sms_to_landlines: bool | None = None, dtmf_input_required: bool | None = None, tts_name: str | None = None, psd2_enabled: bool | None = None, do_not_share_warning_enabled: bool | None = None, custom_code_enabled: bool | None = None, push_include_date: bool | None = None, push_apn_credential_sid: str | None = None, push_fcm_credential_sid: str | None = None, totp_issuer: str | None = None, totp_time_step: int | None = None, totp_code_length: int | None = None, totp_skew: int | None = None, default_template_sid: str | None = None, whatsapp_msg_service_sid: str | None = None, whatsapp_from: str | None = None, passkeys_relying_party_id: str | None = None, passkeys_relying_party_name: str | None = None, passkeys_relying_party_origins: str | None = None, passkeys_authenticator_attachment: str | None = None, passkeys_discoverable_credentials: str | None = None, passkeys_user_verification: str | None = None, verify_event_subscription_enabled: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `friendly_name`
- **Params**: `friendly_name` — form field `FriendlyName` · `code_length` — form field `CodeLength` · `lookup_enabled` — form field `LookupEnabled` · `skip_sms_to_landlines` — form field `SkipSmsToLandlines` · `dtmf_input_required` — form field `DtmfInputRequired` · `tts_name` — form field `TtsName` · `psd2_enabled` — form field `Psd2Enabled` · `do_not_share_warning_enabled` — form field `DoNotShareWarningEnabled` · `custom_code_enabled` — form field `CustomCodeEnabled` · `push_include_date` — form field `Push.IncludeDate` · `push_apn_credential_sid` — form field `Push.ApnCredentialSid` · `push_fcm_credential_sid` — form field `Push.FcmCredentialSid` · `totp_issuer` — form field `Totp.Issuer` · `totp_time_step` — form field `Totp.TimeStep` · `totp_code_length` — form field `Totp.CodeLength` · `totp_skew` — form field `Totp.Skew` · `default_template_sid` — form field `DefaultTemplateSid` · `whatsapp_msg_service_sid` — form field `Whatsapp.MsgServiceSid` · `whatsapp_from` — form field `Whatsapp.From` · `passkeys_relying_party_id` — form field `Passkeys.RelyingParty.Id` · `passkeys_relying_party_name` — form field `Passkeys.RelyingParty.Name` · `passkeys_relying_party_origins` — form field `Passkeys.RelyingParty.Origins` · `passkeys_authenticator_attachment` — form field `Passkeys.AuthenticatorAttachment` · `passkeys_discoverable_credentials` — form field `Passkeys.DiscoverableCredentials` · `passkeys_user_verification` — form field `Passkeys.UserVerification` · `verify_event_subscription_enabled` — form field `VerifyEventSubscriptionEnabled`
- **Returns (parsed)**: `VerifyV2Service`
- **Returns (raw)**: `ApiResult[VerifyV2Service, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VerifyV2Service` | `twilio/models/verify_v2_service.py` |

### client.verify_v2_service_api.delete_service2

- **Route**: `DELETE /v2/Services/{Sid}`
- **Server**: `default3`
- **Signature**: `def delete_service2(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.verify_v2_service_api.fetch_service2

- **Route**: `GET /v2/Services/{Sid}`
- **Server**: `default3`
- **Signature**: `def fetch_service2(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `VerifyV2Service`
- **Returns (raw)**: `ApiResult[VerifyV2Service, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VerifyV2Service` | `twilio/models/verify_v2_service.py` |

### client.verify_v2_service_api.list_service2

- **Route**: `GET /v2/Services`
- **Server**: `default3`
- **Signature**: `def list_service2(*, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListServiceResponse1`
- **Returns (raw)**: `ApiResult[ListServiceResponse1, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListServiceResponse1` | `twilio/models/list_service_response1.py` |

### client.verify_v2_service_api.update_service2

- **Route**: `POST /v2/Services/{Sid}`
- **Server**: `default3`
- **Signature**: `def update_service2(sid: str, *, friendly_name: str | None = None, code_length: int | None = None, lookup_enabled: bool | None = None, skip_sms_to_landlines: bool | None = None, dtmf_input_required: bool | None = None, tts_name: str | None = None, psd2_enabled: bool | None = None, do_not_share_warning_enabled: bool | None = None, custom_code_enabled: bool | None = None, push_include_date: bool | None = None, push_apn_credential_sid: str | None = None, push_fcm_credential_sid: str | None = None, totp_issuer: str | None = None, totp_time_step: int | None = None, totp_code_length: int | None = None, totp_skew: int | None = None, default_template_sid: str | None = None, whatsapp_msg_service_sid: str | None = None, whatsapp_from: str | None = None, passkeys_relying_party_id: str | None = None, passkeys_relying_party_name: str | None = None, passkeys_relying_party_origins: str | None = None, passkeys_authenticator_attachment: str | None = None, passkeys_discoverable_credentials: str | None = None, passkeys_user_verification: str | None = None, verify_event_subscription_enabled: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid` · `friendly_name` — form field `FriendlyName` · `code_length` — form field `CodeLength` · `lookup_enabled` — form field `LookupEnabled` · `skip_sms_to_landlines` — form field `SkipSmsToLandlines` · `dtmf_input_required` — form field `DtmfInputRequired` · `tts_name` — form field `TtsName` · `psd2_enabled` — form field `Psd2Enabled` · `do_not_share_warning_enabled` — form field `DoNotShareWarningEnabled` · `custom_code_enabled` — form field `CustomCodeEnabled` · `push_include_date` — form field `Push.IncludeDate` · `push_apn_credential_sid` — form field `Push.ApnCredentialSid` · `push_fcm_credential_sid` — form field `Push.FcmCredentialSid` · `totp_issuer` — form field `Totp.Issuer` · `totp_time_step` — form field `Totp.TimeStep` · `totp_code_length` — form field `Totp.CodeLength` · `totp_skew` — form field `Totp.Skew` · `default_template_sid` — form field `DefaultTemplateSid` · `whatsapp_msg_service_sid` — form field `Whatsapp.MsgServiceSid` · `whatsapp_from` — form field `Whatsapp.From` · `passkeys_relying_party_id` — form field `Passkeys.RelyingParty.Id` · `passkeys_relying_party_name` — form field `Passkeys.RelyingParty.Name` · `passkeys_relying_party_origins` — form field `Passkeys.RelyingParty.Origins` · `passkeys_authenticator_attachment` — form field `Passkeys.AuthenticatorAttachment` · `passkeys_discoverable_credentials` — form field `Passkeys.DiscoverableCredentials` · `passkeys_user_verification` — form field `Passkeys.UserVerification` · `verify_event_subscription_enabled` — form field `VerifyEventSubscriptionEnabled`
- **Returns (parsed)**: `VerifyV2Service`
- **Returns (raw)**: `ApiResult[VerifyV2Service, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VerifyV2Service` | `twilio/models/verify_v2_service.py` |

