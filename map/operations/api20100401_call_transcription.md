<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401CallTranscription — operations

Accessor: `client.api20100401_call_transcription` · Source: `twilio/apis/api20100401_call_transcription.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.api20100401_call_transcription.create_realtime_transcription

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Transcriptions.json`
- **Server**: `default`
- **Signature**: `def create_realtime_transcription(account_sid: str, call_sid: str, *, name: str | None = None, track: RealtimeTranscriptionEnumTrackOrStr | None = None, status_callback_url: str | None = None, status_callback_method: StatusCallbackMethod17OrStr | None = None, inbound_track_label: str | None = None, outbound_track_label: str | None = None, partial_results: bool | None = None, language_code: str | None = None, transcription_engine: str | None = None, profanity_filter: bool | None = None, speech_model: str | None = None, hints: str | None = None, enable_automatic_punctuation: bool | None = None, intelligence_service: str | None = None, conversation_configuration: str | None = None, conversation_id: str | None = None, transcription_configuration_id: str | None = None, enable_provider_data: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `call_sid`
- **Params**: `account_sid` — path `AccountSid` · `call_sid` — path `CallSid` · `name` — form field `Name` · `track` — form field `Track` · `status_callback_url` — form field `StatusCallbackUrl` · `status_callback_method` — form field `StatusCallbackMethod` · `inbound_track_label` — form field `InboundTrackLabel` · `outbound_track_label` — form field `OutboundTrackLabel` · `partial_results` — form field `PartialResults` · `language_code` — form field `LanguageCode` · `transcription_engine` — form field `TranscriptionEngine` · `profanity_filter` — form field `ProfanityFilter` · `speech_model` — form field `SpeechModel` · `hints` — form field `Hints` · `enable_automatic_punctuation` — form field `EnableAutomaticPunctuation` · `intelligence_service` — form field `IntelligenceService` · `conversation_configuration` — form field `ConversationConfiguration` · `conversation_id` — form field `ConversationId` · `transcription_configuration_id` — form field `TranscriptionConfigurationId` · `enable_provider_data` — form field `EnableProviderData`
- **Returns (parsed)**: `ApiV2010AccountCallRealtimeTranscription`
- **Returns (raw)**: `ApiResult[ApiV2010AccountCallRealtimeTranscription, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RealtimeTranscriptionEnumTrackOrStr` | `twilio/models/enums/realtime_transcription_enum_track.py` |
| `StatusCallbackMethod17OrStr` | `twilio/models/enums/status_callback_method17.py` |
| `ApiV2010AccountCallRealtimeTranscription` | `twilio/models/api_v2010_account_call_realtime_transcription.py` |

### client.api20100401_call_transcription.update_realtime_transcription

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Transcriptions/{Sid}.json`
- **Server**: `default`
- **Signature**: `def update_realtime_transcription(account_sid: str, call_sid: str, sid: str, status: RealtimeTranscriptionEnumUpdateStatusOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `call_sid`, `sid`, `status`
- **Params**: `account_sid` — path `AccountSid` · `call_sid` — path `CallSid` · `sid` — path `Sid` · `status` — form field `Status`
- **Returns (parsed)**: `ApiV2010AccountCallRealtimeTranscription`
- **Returns (raw)**: `ApiResult[ApiV2010AccountCallRealtimeTranscription, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RealtimeTranscriptionEnumUpdateStatusOrStr` | `twilio/models/enums/realtime_transcription_enum_update_status.py` |
| `ApiV2010AccountCallRealtimeTranscription` | `twilio/models/api_v2010_account_call_realtime_transcription.py` |

