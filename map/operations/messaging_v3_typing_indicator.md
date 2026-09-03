<!-- Generated file — do not edit; regenerated with the SDK. -->

# MessagingV3TypingIndicator — operations

Accessor: `client.messaging_v3_typing_indicator` · Source: `twilio_sdk/apis/messaging_v3_typing_indicator.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.messaging_v3_typing_indicator.create_v3_typing_indicator

- **Route**: `POST /v3/Indicators/Typing.json`
- **Auth**: `account_sid_auth_token`
- **Server**: `default1`
- **Signature**: `def create_v3_typing_indicator(body: TypingIndicatorRequest | TypingIndicatorRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `V2IndicatorsTypingJsonResponse`
- **Returns (raw)**: `ApiResult[V2IndicatorsTypingJsonResponse, CreateV3TypingIndicatorErrorBody]`
- **Error**: `CreateV3TypingIndicatorErrorBody` — **Case A (typed)**
- **Error arms**: `AccountsCallsRecordingsSidJson201041408Error1` [400, 401, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TypingIndicatorRequest` | `twilio_sdk/models/unions/typing_indicator_request.py` |
| `TypingIndicatorRequestDict` | `twilio_sdk/models/unions/typing_indicator_request.py` |
| `V2IndicatorsTypingJsonResponse` | `twilio_sdk/models/v2_indicators_typing_json_response.py` |
| `CreateV3TypingIndicatorErrorBody` | `twilio_sdk/errors/create_v3_typing_indicator_error.py` |
| `AccountsCallsRecordingsSidJson201041408Error1` | `twilio_sdk/models/accounts_calls_recordings_sid_json201041408_error1.py` |

