<!-- Generated file — do not edit; regenerated with the SDK. -->

# ConversationsV1ConversationWithParticipantsApi — operations

Accessor: `client.conversations_v1_conversation_with_participants_api` · Source: `twilio_sdk/apis/conversations_v1_conversation_with_participants_api.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.conversations_v1_conversation_with_participants_api.create_conversation_with_participants

- **Route**: `POST /v1/ConversationWithParticipants`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def create_conversation_with_participants(*, x_twilio_webhook_enabled: ConfirmationOrStr | None = None, friendly_name: str | None = None, unique_name: str | None = None, date_created: RFC3339DateTime | None = None, date_updated: RFC3339DateTime | None = None, messaging_service_sid: str | None = None, attributes: str | None = None, state: ConversationWithParticipantsEnumStateOrStr | None = None, timers_inactive: str | None = None, timers_closed: str | None = None, bindings_email_address: str | None = None, bindings_email_name: str | None = None, participant: list[str] | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `x_twilio_webhook_enabled` — header `X-Twilio-Webhook-Enabled` · `friendly_name` — form field `FriendlyName` · `unique_name` — form field `UniqueName` · `date_created` — form field `DateCreated` · `date_updated` — form field `DateUpdated` · `messaging_service_sid` — form field `MessagingServiceSid` · `attributes` — form field `Attributes` · `state` — form field `State` · `timers_inactive` — form field `Timers.Inactive` · `timers_closed` — form field `Timers.Closed` · `bindings_email_address` — form field `Bindings.Email.Address` · `bindings_email_name` — form field `Bindings.Email.Name` · `participant` — form field `Participant`
- **Returns (parsed)**: `ConversationsV1ConversationWithParticipants`
- **Returns (raw)**: `ApiResult[ConversationsV1ConversationWithParticipants, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConfirmationOrStr` | `twilio_sdk/models/enums/confirmation.py` |
| `ConversationWithParticipantsEnumStateOrStr` | `twilio_sdk/models/enums/conversation_with_participants_enum_state.py` |
| `ConversationsV1ConversationWithParticipants` | `twilio_sdk/models/conversations_v1_conversation_with_participants.py` |

### client.conversations_v1_conversation_with_participants_api.create_service_conversation_with_participants

- **Route**: `POST /v1/Services/{ChatServiceSid}/ConversationWithParticipants`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def create_service_conversation_with_participants(chat_service_sid: str, *, x_twilio_webhook_enabled: ConfirmationOrStr | None = None, friendly_name: str | None = None, unique_name: str | None = None, date_created: RFC3339DateTime | None = None, date_updated: RFC3339DateTime | None = None, messaging_service_sid: str | None = None, attributes: str | None = None, state: ServiceConversationWithParticipantsEnumStateOrStr | None = None, timers_inactive: str | None = None, timers_closed: str | None = None, bindings_email_address: str | None = None, bindings_email_name: str | None = None, participant: list[str] | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `x_twilio_webhook_enabled` — header `X-Twilio-Webhook-Enabled` · `friendly_name` — form field `FriendlyName` · `unique_name` — form field `UniqueName` · `date_created` — form field `DateCreated` · `date_updated` — form field `DateUpdated` · `messaging_service_sid` — form field `MessagingServiceSid` · `attributes` — form field `Attributes` · `state` — form field `State` · `timers_inactive` — form field `Timers.Inactive` · `timers_closed` — form field `Timers.Closed` · `bindings_email_address` — form field `Bindings.Email.Address` · `bindings_email_name` — form field `Bindings.Email.Name` · `participant` — form field `Participant`
- **Returns (parsed)**: `ConversationsV1ServiceServiceConversationWithParticipants`
- **Returns (raw)**: `ApiResult[ConversationsV1ServiceServiceConversationWithParticipants, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConfirmationOrStr` | `twilio_sdk/models/enums/confirmation.py` |
| `ServiceConversationWithParticipantsEnumStateOrStr` | `twilio_sdk/models/enums/service_conversation_with_participants_enum_state.py` |
| `ConversationsV1ServiceServiceConversationWithParticipants` | `twilio_sdk/models/conversations_v1_service_service_conversation_with_participants.py` |

