<!-- Generated file — do not edit; regenerated with the SDK. -->

# FlexV1WebChannelApi — operations

Accessor: `client.flex_v1_web_channel_api` · Source: `twilio_sdk/apis/flex_v1_web_channel_api.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.flex_v1_web_channel_api.create_web_channel

- **Route**: `POST /v1/WebChannels`
- **Server**: `default13`
- **Signature**: `def create_web_channel(flex_flow_sid: str, identity: str, customer_friendly_name: str, chat_friendly_name: str, *, chat_unique_name: str | None = None, pre_engagement_data: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `flex_flow_sid`, `identity`, `customer_friendly_name`, `chat_friendly_name`
- **Params**: `flex_flow_sid` — form field `FlexFlowSid` · `identity` — form field `Identity` · `customer_friendly_name` — form field `CustomerFriendlyName` · `chat_friendly_name` — form field `ChatFriendlyName` · `chat_unique_name` — form field `ChatUniqueName` · `pre_engagement_data` — form field `PreEngagementData`
- **Returns (parsed)**: `FlexV1WebChannel`
- **Returns (raw)**: `ApiResult[FlexV1WebChannel, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1WebChannel` | `twilio_sdk/models/flex_v1_web_channel.py` |

### client.flex_v1_web_channel_api.delete_web_channel

- **Route**: `DELETE /v1/WebChannels/{Sid}`
- **Server**: `default13`
- **Signature**: `def delete_web_channel(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.flex_v1_web_channel_api.fetch_web_channel

- **Route**: `GET /v1/WebChannels/{Sid}`
- **Server**: `default13`
- **Signature**: `def fetch_web_channel(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `FlexV1WebChannel`
- **Returns (raw)**: `ApiResult[FlexV1WebChannel, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1WebChannel` | `twilio_sdk/models/flex_v1_web_channel.py` |

### client.flex_v1_web_channel_api.list_web_channel

- **Route**: `GET /v1/WebChannels`
- **Server**: `default13`
- **Signature**: `def list_web_channel(*, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListWebChannelResponse`
- **Returns (raw)**: `ApiResult[ListWebChannelResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListWebChannelResponse` | `twilio_sdk/models/list_web_channel_response.py` |

### client.flex_v1_web_channel_api.update_web_channel

- **Route**: `POST /v1/WebChannels/{Sid}`
- **Server**: `default13`
- **Signature**: `def update_web_channel(sid: str, *, chat_status: WebChannelEnumChatStatusOrStr | None = None, post_engagement_data: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid` · `chat_status` — form field `ChatStatus` · `post_engagement_data` — form field `PostEngagementData`
- **Returns (parsed)**: `FlexV1WebChannel`
- **Returns (raw)**: `ApiResult[FlexV1WebChannel, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WebChannelEnumChatStatusOrStr` | `twilio_sdk/models/enums/web_channel_enum_chat_status.py` |
| `FlexV1WebChannel` | `twilio_sdk/models/flex_v1_web_channel.py` |

