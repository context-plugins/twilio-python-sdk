<!-- Generated file — do not edit; regenerated with the SDK. -->

# FlexV1ChannelApi — operations

Accessor: `client.flex_v1_channel_api` · Source: `twilio/apis/flex_v1_channel_api.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.flex_v1_channel_api.create_channel

- **Route**: `POST /v1/Channels`
- **Server**: `default13`
- **Signature**: `def create_channel(flex_flow_sid: str, identity: str, chat_user_friendly_name: str, chat_friendly_name: str, *, target: str | None = None, chat_unique_name: str | None = None, pre_engagement_data: str | None = None, task_sid: str | None = None, task_attributes: str | None = None, long_lived: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `flex_flow_sid`, `identity`, `chat_user_friendly_name`, `chat_friendly_name`
- **Params**: `flex_flow_sid` — form field `FlexFlowSid` · `identity` — form field `Identity` · `chat_user_friendly_name` — form field `ChatUserFriendlyName` · `chat_friendly_name` — form field `ChatFriendlyName` · `target` — form field `Target` · `chat_unique_name` — form field `ChatUniqueName` · `pre_engagement_data` — form field `PreEngagementData` · `task_sid` — form field `TaskSid` · `task_attributes` — form field `TaskAttributes` · `long_lived` — form field `LongLived`
- **Returns (parsed)**: `FlexV1Channel`
- **Returns (raw)**: `ApiResult[FlexV1Channel, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1Channel` | `twilio/models/flex_v1_channel.py` |

### client.flex_v1_channel_api.delete_channel

- **Route**: `DELETE /v1/Channels/{Sid}`
- **Server**: `default13`
- **Signature**: `def delete_channel(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.flex_v1_channel_api.fetch_channel

- **Route**: `GET /v1/Channels/{Sid}`
- **Server**: `default13`
- **Signature**: `def fetch_channel(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `FlexV1Channel`
- **Returns (raw)**: `ApiResult[FlexV1Channel, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1Channel` | `twilio/models/flex_v1_channel.py` |

### client.flex_v1_channel_api.list_channel

- **Route**: `GET /v1/Channels`
- **Server**: `default13`
- **Signature**: `def list_channel(*, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListChannelResponse`
- **Returns (raw)**: `ApiResult[ListChannelResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListChannelResponse` | `twilio/models/list_channel_response.py` |

