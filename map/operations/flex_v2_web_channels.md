<!-- Generated file — do not edit; regenerated with the SDK. -->

# FlexV2WebChannels — operations

Accessor: `client.flex_v2_web_channels` · Source: `twilio/apis/flex_v2_web_channels.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.flex_v2_web_channels.create_web_channel2

- **Route**: `POST /v2/WebChats`
- **Server**: `default13`
- **Signature**: `def create_web_channel2(address_sid: str, *, ui_version: str | None = None, chat_friendly_name: str | None = None, customer_friendly_name: str | None = None, pre_engagement_data: str | None = None, identity: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `address_sid`
- **Params**: `ui_version` — header `Ui-Version` · `address_sid` — form field `AddressSid` · `chat_friendly_name` — form field `ChatFriendlyName` · `customer_friendly_name` — form field `CustomerFriendlyName` · `pre_engagement_data` — form field `PreEngagementData` · `identity` — form field `Identity`
- **Returns (parsed)**: `FlexV2WebChannel`
- **Returns (raw)**: `ApiResult[FlexV2WebChannel, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV2WebChannel` | `twilio/models/flex_v2_web_channel.py` |

