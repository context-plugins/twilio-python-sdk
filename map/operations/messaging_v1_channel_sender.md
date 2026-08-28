<!-- Generated file — do not edit; regenerated with the SDK. -->

# MessagingV1ChannelSender — operations

Accessor: `client.messaging_v1_channel_sender` · Source: `twilio_sdk/apis/messaging_v1_channel_sender.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.messaging_v1_channel_sender.create_channel_sender

- **Route**: `POST /v1/Services/{MessagingServiceSid}/ChannelSenders`
- **Server**: `default1`
- **Signature**: `def create_channel_sender(messaging_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `messaging_service_sid`, `sid`
- **Params**: `messaging_service_sid` — path `MessagingServiceSid` · `sid` — form field `Sid`
- **Returns (parsed)**: `MessagingV1ServiceChannelSender`
- **Returns (raw)**: `ApiResult[MessagingV1ServiceChannelSender, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MessagingV1ServiceChannelSender` | `twilio_sdk/models/messaging_v1_service_channel_sender.py` |

### client.messaging_v1_channel_sender.delete_channel_sender

- **Route**: `DELETE /v1/Services/{MessagingServiceSid}/ChannelSenders/{Sid}`
- **Server**: `default1`
- **Signature**: `def delete_channel_sender(messaging_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `messaging_service_sid`, `sid`
- **Params**: `messaging_service_sid` — path `MessagingServiceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.messaging_v1_channel_sender.fetch_channel_sender

- **Route**: `GET /v1/Services/{MessagingServiceSid}/ChannelSenders/{Sid}`
- **Server**: `default1`
- **Signature**: `def fetch_channel_sender(messaging_service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `messaging_service_sid`, `sid`
- **Params**: `messaging_service_sid` — path `MessagingServiceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `MessagingV1ServiceChannelSender`
- **Returns (raw)**: `ApiResult[MessagingV1ServiceChannelSender, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MessagingV1ServiceChannelSender` | `twilio_sdk/models/messaging_v1_service_channel_sender.py` |

### client.messaging_v1_channel_sender.list_channel_sender

- **Route**: `GET /v1/Services/{MessagingServiceSid}/ChannelSenders`
- **Server**: `default1`
- **Signature**: `def list_channel_sender(messaging_service_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `messaging_service_sid`
- **Params**: `messaging_service_sid` — path `MessagingServiceSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListChannelSenderResponse`
- **Returns (raw)**: `ApiResult[ListChannelSenderResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListChannelSenderResponse` | `twilio_sdk/models/list_channel_sender_response.py` |

