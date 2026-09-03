<!-- Generated file — do not edit; regenerated with the SDK. -->

# ConversationsV1Notification — operations

Accessor: `client.conversations_v1_notification` · Source: `twilio_sdk/apis/conversations_v1_notification.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.conversations_v1_notification.fetch_service_notification

- **Route**: `GET /v1/Services/{ChatServiceSid}/Configuration/Notifications`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def fetch_service_notification(chat_service_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid`
- **Returns (parsed)**: `ConversationsV1ServiceServiceConfigurationServiceNotification`
- **Returns (raw)**: `ApiResult[ConversationsV1ServiceServiceConfigurationServiceNotification, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConversationsV1ServiceServiceConfigurationServiceNotification` | `twilio_sdk/models/conversations_v1_service_service_configuration_service_notification.py` |

### client.conversations_v1_notification.update_service_notification

- **Route**: `POST /v1/Services/{ChatServiceSid}/Configuration/Notifications`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def update_service_notification(chat_service_sid: str, *, log_enabled: bool | None = None, new_message_enabled: bool | None = None, new_message_template: str | None = None, new_message_sound: str | None = None, new_message_badge_count_enabled: bool | None = None, added_to_conversation_enabled: bool | None = None, added_to_conversation_template: str | None = None, added_to_conversation_sound: str | None = None, removed_from_conversation_enabled: bool | None = None, removed_from_conversation_template: str | None = None, removed_from_conversation_sound: str | None = None, new_message_with_media_enabled: bool | None = None, new_message_with_media_template: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `log_enabled` — form field `LogEnabled` · `new_message_enabled` — form field `NewMessage.Enabled` · `new_message_template` — form field `NewMessage.Template` · `new_message_sound` — form field `NewMessage.Sound` · `new_message_badge_count_enabled` — form field `NewMessage.BadgeCountEnabled` · `added_to_conversation_enabled` — form field `AddedToConversation.Enabled` · `added_to_conversation_template` — form field `AddedToConversation.Template` · `added_to_conversation_sound` — form field `AddedToConversation.Sound` · `removed_from_conversation_enabled` — form field `RemovedFromConversation.Enabled` · `removed_from_conversation_template` — form field `RemovedFromConversation.Template` · `removed_from_conversation_sound` — form field `RemovedFromConversation.Sound` · `new_message_with_media_enabled` — form field `NewMessage.WithMedia.Enabled` · `new_message_with_media_template` — form field `NewMessage.WithMedia.Template`
- **Returns (parsed)**: `ConversationsV1ServiceServiceConfigurationServiceNotification`
- **Returns (raw)**: `ApiResult[ConversationsV1ServiceServiceConfigurationServiceNotification, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConversationsV1ServiceServiceConfigurationServiceNotification` | `twilio_sdk/models/conversations_v1_service_service_configuration_service_notification.py` |

