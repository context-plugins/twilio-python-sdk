<!-- Generated file — do not edit; regenerated with the SDK. -->

# MessagingV2TypingIndicator — operations

Accessor: `client.messaging_v2_typing_indicator` · Source: `twilio_sdk/apis/messaging_v2_typing_indicator.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.messaging_v2_typing_indicator.create_typing_indicator

- **Route**: `POST /v2/Indicators/Typing.json`
- **Server**: `default1`
- **Signature**: `def create_typing_indicator(channel: ChannelOrStr, message_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel`, `message_id`
- **Params**: `channel` — form field · `message_id` — form field `messageId`
- **Returns (parsed)**: `V2IndicatorsTypingJsonResponse`
- **Returns (raw)**: `ApiResult[V2IndicatorsTypingJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ChannelOrStr` | `twilio_sdk/models/enums/channel.py` |
| `V2IndicatorsTypingJsonResponse` | `twilio_sdk/models/v2_indicators_typing_json_response.py` |

