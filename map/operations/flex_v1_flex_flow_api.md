<!-- Generated file — do not edit; regenerated with the SDK. -->

# FlexV1FlexFlowApi — operations

Accessor: `client.flex_v1_flex_flow_api` · Source: `twilio_sdk/apis/flex_v1_flex_flow_api.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.flex_v1_flex_flow_api.create_flex_flow

- **Route**: `POST /v1/FlexFlows`
- **Server**: `default13`
- **Signature**: `def create_flex_flow(friendly_name: str, chat_service_sid: str, channel_type: FlexFlowEnumChannelTypeOrStr, *, contact_identity: str | None = None, enabled: bool | None = None, integration_type: FlexFlowEnumIntegrationTypeOrStr | None = None, integration_flow_sid: str | None = None, integration_url: AnyUrl | None = None, integration_workspace_sid: str | None = None, integration_workflow_sid: str | None = None, integration_channel: str | None = None, integration_timeout: int | None = None, integration_priority: int | None = None, integration_creation_on_message: bool | None = None, long_lived: bool | None = None, janitor_enabled: bool | None = None, integration_retry_count: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `friendly_name`, `chat_service_sid`, `channel_type`
- **Params**: `friendly_name` — form field `FriendlyName` · `chat_service_sid` — form field `ChatServiceSid` · `channel_type` — form field `ChannelType` · `contact_identity` — form field `ContactIdentity` · `enabled` — form field `Enabled` · `integration_type` — form field `IntegrationType` · `integration_flow_sid` — form field `Integration.FlowSid` · `integration_url` — form field `Integration.Url` · `integration_workspace_sid` — form field `Integration.WorkspaceSid` · `integration_workflow_sid` — form field `Integration.WorkflowSid` · `integration_channel` — form field `Integration.Channel` · `integration_timeout` — form field `Integration.Timeout` · `integration_priority` — form field `Integration.Priority` · `integration_creation_on_message` — form field `Integration.CreationOnMessage` · `long_lived` — form field `LongLived` · `janitor_enabled` — form field `JanitorEnabled` · `integration_retry_count` — form field `Integration.RetryCount`
- **Returns (parsed)**: `FlexV1FlexFlow`
- **Returns (raw)**: `ApiResult[FlexV1FlexFlow, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexFlowEnumChannelTypeOrStr` | `twilio_sdk/models/enums/flex_flow_enum_channel_type.py` |
| `FlexFlowEnumIntegrationTypeOrStr` | `twilio_sdk/models/enums/flex_flow_enum_integration_type.py` |
| `FlexV1FlexFlow` | `twilio_sdk/models/flex_v1_flex_flow.py` |

### client.flex_v1_flex_flow_api.delete_flex_flow

- **Route**: `DELETE /v1/FlexFlows/{Sid}`
- **Server**: `default13`
- **Signature**: `def delete_flex_flow(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.flex_v1_flex_flow_api.fetch_flex_flow

- **Route**: `GET /v1/FlexFlows/{Sid}`
- **Server**: `default13`
- **Signature**: `def fetch_flex_flow(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `FlexV1FlexFlow`
- **Returns (raw)**: `ApiResult[FlexV1FlexFlow, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1FlexFlow` | `twilio_sdk/models/flex_v1_flex_flow.py` |

### client.flex_v1_flex_flow_api.list_flex_flow

- **Route**: `GET /v1/FlexFlows`
- **Server**: `default13`
- **Signature**: `def list_flex_flow(*, friendly_name: str | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `friendly_name` — query `FriendlyName` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListFlexFlowResponse`
- **Returns (raw)**: `ApiResult[ListFlexFlowResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListFlexFlowResponse` | `twilio_sdk/models/list_flex_flow_response.py` |

### client.flex_v1_flex_flow_api.update_flex_flow

- **Route**: `POST /v1/FlexFlows/{Sid}`
- **Server**: `default13`
- **Signature**: `def update_flex_flow(sid: str, *, friendly_name: str | None = None, chat_service_sid: str | None = None, channel_type: FlexFlowEnumChannelTypeOrStr | None = None, contact_identity: str | None = None, enabled: bool | None = None, integration_type: FlexFlowEnumIntegrationTypeOrStr | None = None, integration_flow_sid: str | None = None, integration_url: AnyUrl | None = None, integration_workspace_sid: str | None = None, integration_workflow_sid: str | None = None, integration_channel: str | None = None, integration_timeout: int | None = None, integration_priority: int | None = None, integration_creation_on_message: bool | None = None, long_lived: bool | None = None, janitor_enabled: bool | None = None, integration_retry_count: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid` · `friendly_name` — form field `FriendlyName` · `chat_service_sid` — form field `ChatServiceSid` · `channel_type` — form field `ChannelType` · `contact_identity` — form field `ContactIdentity` · `enabled` — form field `Enabled` · `integration_type` — form field `IntegrationType` · `integration_flow_sid` — form field `Integration.FlowSid` · `integration_url` — form field `Integration.Url` · `integration_workspace_sid` — form field `Integration.WorkspaceSid` · `integration_workflow_sid` — form field `Integration.WorkflowSid` · `integration_channel` — form field `Integration.Channel` · `integration_timeout` — form field `Integration.Timeout` · `integration_priority` — form field `Integration.Priority` · `integration_creation_on_message` — form field `Integration.CreationOnMessage` · `long_lived` — form field `LongLived` · `janitor_enabled` — form field `JanitorEnabled` · `integration_retry_count` — form field `Integration.RetryCount`
- **Returns (parsed)**: `FlexV1FlexFlow`
- **Returns (raw)**: `ApiResult[FlexV1FlexFlow, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexFlowEnumChannelTypeOrStr` | `twilio_sdk/models/enums/flex_flow_enum_channel_type.py` |
| `FlexFlowEnumIntegrationTypeOrStr` | `twilio_sdk/models/enums/flex_flow_enum_integration_type.py` |
| `FlexV1FlexFlow` | `twilio_sdk/models/flex_v1_flex_flow.py` |

