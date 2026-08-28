<!-- Generated file — do not edit; regenerated with the SDK. -->

# ConversationsV1Webhook — operations

Accessor: `client.conversations_v1_webhook` · Source: `twilio_sdk/apis/conversations_v1_webhook.py` · 14 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.conversations_v1_webhook.create_conversation_scoped_webhook

- **Route**: `POST /v1/Conversations/{ConversationSid}/Webhooks`
- **Server**: `default7`
- **Signature**: `def create_conversation_scoped_webhook(conversation_sid: str, target: ConversationScopedWebhookEnumTargetOrStr, *, configuration_url: str | None = None, configuration_method: ConversationScopedWebhookEnumMethodOrStr | None = None, configuration_filters: list[str] | None = None, configuration_triggers: list[str] | None = None, configuration_flow_sid: str | None = None, configuration_replay_after: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `conversation_sid`, `target`
- **Params**: `conversation_sid` — path `ConversationSid` · `target` — form field `Target` · `configuration_url` — form field `Configuration.Url` · `configuration_method` — form field `Configuration.Method` · `configuration_filters` — form field `Configuration.Filters` · `configuration_triggers` — form field `Configuration.Triggers` · `configuration_flow_sid` — form field `Configuration.FlowSid` · `configuration_replay_after` — form field `Configuration.ReplayAfter`
- **Returns (parsed)**: `ConversationsV1ConversationConversationScopedWebhook`
- **Returns (raw)**: `ApiResult[ConversationsV1ConversationConversationScopedWebhook, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConversationScopedWebhookEnumTargetOrStr` | `twilio_sdk/models/enums/conversation_scoped_webhook_enum_target.py` |
| `ConversationScopedWebhookEnumMethodOrStr` | `twilio_sdk/models/enums/conversation_scoped_webhook_enum_method.py` |
| `ConversationsV1ConversationConversationScopedWebhook` | `twilio_sdk/models/conversations_v1_conversation_conversation_scoped_webhook.py` |

### client.conversations_v1_webhook.create_service_conversation_scoped_webhook

- **Route**: `POST /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Webhooks`
- **Server**: `default7`
- **Signature**: `def create_service_conversation_scoped_webhook(chat_service_sid: str, conversation_sid: str, target: ServiceConversationScopedWebhookEnumTargetOrStr, *, configuration_url: str | None = None, configuration_method: ServiceConversationScopedWebhookEnumMethodOrStr | None = None, configuration_filters: list[str] | None = None, configuration_triggers: list[str] | None = None, configuration_flow_sid: str | None = None, configuration_replay_after: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`, `conversation_sid`, `target`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `conversation_sid` — path `ConversationSid` · `target` — form field `Target` · `configuration_url` — form field `Configuration.Url` · `configuration_method` — form field `Configuration.Method` · `configuration_filters` — form field `Configuration.Filters` · `configuration_triggers` — form field `Configuration.Triggers` · `configuration_flow_sid` — form field `Configuration.FlowSid` · `configuration_replay_after` — form field `Configuration.ReplayAfter`
- **Returns (parsed)**: `ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook`
- **Returns (raw)**: `ApiResult[ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ServiceConversationScopedWebhookEnumTargetOrStr` | `twilio_sdk/models/enums/service_conversation_scoped_webhook_enum_target.py` |
| `ServiceConversationScopedWebhookEnumMethodOrStr` | `twilio_sdk/models/enums/service_conversation_scoped_webhook_enum_method.py` |
| `ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook` | `twilio_sdk/models/conversations_v1_service_service_conversation_service_conversation_scoped_webhook.py` |

### client.conversations_v1_webhook.delete_conversation_scoped_webhook

- **Route**: `DELETE /v1/Conversations/{ConversationSid}/Webhooks/{Sid}`
- **Server**: `default7`
- **Signature**: `def delete_conversation_scoped_webhook(conversation_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `conversation_sid`, `sid`
- **Params**: `conversation_sid` — path `ConversationSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.conversations_v1_webhook.delete_service_conversation_scoped_webhook

- **Route**: `DELETE /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Webhooks/{Sid}`
- **Server**: `default7`
- **Signature**: `def delete_service_conversation_scoped_webhook(chat_service_sid: str, conversation_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`, `conversation_sid`, `sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `conversation_sid` — path `ConversationSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.conversations_v1_webhook.fetch_configuration_webhook

- **Route**: `GET /v1/Configuration/Webhooks`
- **Server**: `default7`
- **Signature**: `def fetch_configuration_webhook(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `ConversationsV1ConfigurationConfigurationWebhook`
- **Returns (raw)**: `ApiResult[ConversationsV1ConfigurationConfigurationWebhook, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConversationsV1ConfigurationConfigurationWebhook` | `twilio_sdk/models/conversations_v1_configuration_configuration_webhook.py` |

### client.conversations_v1_webhook.fetch_conversation_scoped_webhook

- **Route**: `GET /v1/Conversations/{ConversationSid}/Webhooks/{Sid}`
- **Server**: `default7`
- **Signature**: `def fetch_conversation_scoped_webhook(conversation_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `conversation_sid`, `sid`
- **Params**: `conversation_sid` — path `ConversationSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ConversationsV1ConversationConversationScopedWebhook`
- **Returns (raw)**: `ApiResult[ConversationsV1ConversationConversationScopedWebhook, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConversationsV1ConversationConversationScopedWebhook` | `twilio_sdk/models/conversations_v1_conversation_conversation_scoped_webhook.py` |

### client.conversations_v1_webhook.fetch_service_conversation_scoped_webhook

- **Route**: `GET /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Webhooks/{Sid}`
- **Server**: `default7`
- **Signature**: `def fetch_service_conversation_scoped_webhook(chat_service_sid: str, conversation_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`, `conversation_sid`, `sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `conversation_sid` — path `ConversationSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook`
- **Returns (raw)**: `ApiResult[ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook` | `twilio_sdk/models/conversations_v1_service_service_conversation_service_conversation_scoped_webhook.py` |

### client.conversations_v1_webhook.fetch_service_webhook_configuration

- **Route**: `GET /v1/Services/{ChatServiceSid}/Configuration/Webhooks`
- **Server**: `default7`
- **Signature**: `def fetch_service_webhook_configuration(chat_service_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid`
- **Returns (parsed)**: `ConversationsV1ServiceServiceConfigurationServiceWebhookConfiguration`
- **Returns (raw)**: `ApiResult[ConversationsV1ServiceServiceConfigurationServiceWebhookConfiguration, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConversationsV1ServiceServiceConfigurationServiceWebhookConfiguration` | `twilio_sdk/models/conversations_v1_service_service_configuration_service_webhook_configuration.py` |

### client.conversations_v1_webhook.list_conversation_scoped_webhook

- **Route**: `GET /v1/Conversations/{ConversationSid}/Webhooks`
- **Server**: `default7`
- **Signature**: `def list_conversation_scoped_webhook(conversation_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `conversation_sid`
- **Params**: `conversation_sid` — path `ConversationSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListConversationScopedWebhookResponse`
- **Returns (raw)**: `ApiResult[ListConversationScopedWebhookResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListConversationScopedWebhookResponse` | `twilio_sdk/models/list_conversation_scoped_webhook_response.py` |

### client.conversations_v1_webhook.list_service_conversation_scoped_webhook

- **Route**: `GET /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Webhooks`
- **Server**: `default7`
- **Signature**: `def list_service_conversation_scoped_webhook(chat_service_sid: str, conversation_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`, `conversation_sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `conversation_sid` — path `ConversationSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListServiceConversationScopedWebhookResponse`
- **Returns (raw)**: `ApiResult[ListServiceConversationScopedWebhookResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListServiceConversationScopedWebhookResponse` | `twilio_sdk/models/list_service_conversation_scoped_webhook_response.py` |

### client.conversations_v1_webhook.update_configuration_webhook

- **Route**: `POST /v1/Configuration/Webhooks`
- **Server**: `default7`
- **Signature**: `def update_configuration_webhook(*, method: str | None = None, filters: list[str] | None = None, pre_webhook_url: str | None = None, post_webhook_url: str | None = None, target: ConfigurationWebhookEnumTargetOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `method` — form field `Method` · `filters` — form field `Filters` · `pre_webhook_url` — form field `PreWebhookUrl` · `post_webhook_url` — form field `PostWebhookUrl` · `target` — form field `Target`
- **Returns (parsed)**: `ConversationsV1ConfigurationConfigurationWebhook`
- **Returns (raw)**: `ApiResult[ConversationsV1ConfigurationConfigurationWebhook, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConfigurationWebhookEnumTargetOrStr` | `twilio_sdk/models/enums/configuration_webhook_enum_target.py` |
| `ConversationsV1ConfigurationConfigurationWebhook` | `twilio_sdk/models/conversations_v1_configuration_configuration_webhook.py` |

### client.conversations_v1_webhook.update_conversation_scoped_webhook

- **Route**: `POST /v1/Conversations/{ConversationSid}/Webhooks/{Sid}`
- **Server**: `default7`
- **Signature**: `def update_conversation_scoped_webhook(conversation_sid: str, sid: str, *, configuration_url: str | None = None, configuration_method: ConversationScopedWebhookEnumMethodOrStr | None = None, configuration_filters: list[str] | None = None, configuration_triggers: list[str] | None = None, configuration_flow_sid: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `conversation_sid`, `sid`
- **Params**: `conversation_sid` — path `ConversationSid` · `sid` — path `Sid` · `configuration_url` — form field `Configuration.Url` · `configuration_method` — form field `Configuration.Method` · `configuration_filters` — form field `Configuration.Filters` · `configuration_triggers` — form field `Configuration.Triggers` · `configuration_flow_sid` — form field `Configuration.FlowSid`
- **Returns (parsed)**: `ConversationsV1ConversationConversationScopedWebhook`
- **Returns (raw)**: `ApiResult[ConversationsV1ConversationConversationScopedWebhook, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConversationScopedWebhookEnumMethodOrStr` | `twilio_sdk/models/enums/conversation_scoped_webhook_enum_method.py` |
| `ConversationsV1ConversationConversationScopedWebhook` | `twilio_sdk/models/conversations_v1_conversation_conversation_scoped_webhook.py` |

### client.conversations_v1_webhook.update_service_conversation_scoped_webhook

- **Route**: `POST /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Webhooks/{Sid}`
- **Server**: `default7`
- **Signature**: `def update_service_conversation_scoped_webhook(chat_service_sid: str, conversation_sid: str, sid: str, *, configuration_url: str | None = None, configuration_method: ServiceConversationScopedWebhookEnumMethodOrStr | None = None, configuration_filters: list[str] | None = None, configuration_triggers: list[str] | None = None, configuration_flow_sid: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`, `conversation_sid`, `sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `conversation_sid` — path `ConversationSid` · `sid` — path `Sid` · `configuration_url` — form field `Configuration.Url` · `configuration_method` — form field `Configuration.Method` · `configuration_filters` — form field `Configuration.Filters` · `configuration_triggers` — form field `Configuration.Triggers` · `configuration_flow_sid` — form field `Configuration.FlowSid`
- **Returns (parsed)**: `ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook`
- **Returns (raw)**: `ApiResult[ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ServiceConversationScopedWebhookEnumMethodOrStr` | `twilio_sdk/models/enums/service_conversation_scoped_webhook_enum_method.py` |
| `ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook` | `twilio_sdk/models/conversations_v1_service_service_conversation_service_conversation_scoped_webhook.py` |

### client.conversations_v1_webhook.update_service_webhook_configuration

- **Route**: `POST /v1/Services/{ChatServiceSid}/Configuration/Webhooks`
- **Server**: `default7`
- **Signature**: `def update_service_webhook_configuration(chat_service_sid: str, *, pre_webhook_url: AnyUrl | None = None, post_webhook_url: AnyUrl | None = None, filters: list[str] | None = None, method: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `pre_webhook_url` — form field `PreWebhookUrl` · `post_webhook_url` — form field `PostWebhookUrl` · `filters` — form field `Filters` · `method` — form field `Method`
- **Returns (parsed)**: `ConversationsV1ServiceServiceConfigurationServiceWebhookConfiguration`
- **Returns (raw)**: `ApiResult[ConversationsV1ServiceServiceConfigurationServiceWebhookConfiguration, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConversationsV1ServiceServiceConfigurationServiceWebhookConfiguration` | `twilio_sdk/models/conversations_v1_service_service_configuration_service_webhook_configuration.py` |

