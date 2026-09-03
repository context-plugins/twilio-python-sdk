<!-- Generated file — do not edit; regenerated with the SDK. -->

# MessagingV2ChannelsSender — operations

Accessor: `client.messaging_v2_channels_sender` · Source: `twilio_sdk/apis/messaging_v2_channels_sender.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.messaging_v2_channels_sender.create_channels_sender

- **Route**: `POST /v2/Channels/Senders`
- **Auth**: `account_sid_auth_token`
- **Server**: `default1`
- **Signature**: `def create_channels_sender(body: MessagingV2ChannelsSenderRequestsCreate | MessagingV2ChannelsSenderRequestsCreateDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `MessagingV2ChannelsSenderResponse`
- **Returns (raw)**: `ApiResult[MessagingV2ChannelsSenderResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MessagingV2ChannelsSenderRequestsCreate` | `twilio_sdk/models/messaging_v2_channels_sender_requests_create.py` |
| `MessagingV2ChannelsSenderRequestsCreateDict` | `twilio_sdk/models/messaging_v2_channels_sender_requests_create.py` |
| `MessagingV2ChannelsSenderResponse` | `twilio_sdk/models/messaging_v2_channels_sender_response.py` |

### client.messaging_v2_channels_sender.delete_channels_sender

- **Route**: `DELETE /v2/Channels/Senders/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default1`
- **Signature**: `def delete_channels_sender(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.messaging_v2_channels_sender.fetch_channels_sender

- **Route**: `GET /v2/Channels/Senders/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default1`
- **Signature**: `def fetch_channels_sender(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `MessagingV2ChannelsSenderResponse`
- **Returns (raw)**: `ApiResult[MessagingV2ChannelsSenderResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MessagingV2ChannelsSenderResponse` | `twilio_sdk/models/messaging_v2_channels_sender_response.py` |

### client.messaging_v2_channels_sender.list_channels_sender

- **Route**: `GET /v2/Channels/Senders`
- **Auth**: `account_sid_auth_token`
- **Server**: `default1`
- **Signature**: `def list_channels_sender(channel: str, *, page_size: int | None = 50, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel`
- **Params**: `channel` — query `Channel` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListChannelsSenderResponse`
- **Returns (raw)**: `ApiResult[ListChannelsSenderResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListChannelsSenderResponse` | `twilio_sdk/models/list_channels_sender_response.py` |

### client.messaging_v2_channels_sender.update_channels_sender

- **Route**: `POST /v2/Channels/Senders/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default1`
- **Signature**: `def update_channels_sender(sid: str, *, body: MessagingV2ChannelsSenderRequestsUpdate | MessagingV2ChannelsSenderRequestsUpdateDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid` · `body` — JSON body
- **Returns (parsed)**: `MessagingV2ChannelsSenderResponse`
- **Returns (raw)**: `ApiResult[MessagingV2ChannelsSenderResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MessagingV2ChannelsSenderRequestsUpdate` | `twilio_sdk/models/messaging_v2_channels_sender_requests_update.py` |
| `MessagingV2ChannelsSenderRequestsUpdateDict` | `twilio_sdk/models/messaging_v2_channels_sender_requests_update.py` |
| `MessagingV2ChannelsSenderResponse` | `twilio_sdk/models/messaging_v2_channels_sender_response.py` |

