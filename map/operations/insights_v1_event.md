<!-- Generated file — do not edit; regenerated with the SDK. -->

# InsightsV1Event — operations

Accessor: `client.insights_v1_event` · Source: `twilio/apis/insights_v1_event.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.insights_v1_event.list_event2

- **Route**: `GET /v1/Voice/{CallSid}/Events`
- **Server**: `default14`
- **Signature**: `def list_event2(call_sid: str, *, edge: EventEnumTwilioEdgeOrStr | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `call_sid`
- **Params**: `call_sid` — path `CallSid` · `edge` — query `Edge` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListEventResponse1`
- **Returns (raw)**: `ApiResult[ListEventResponse1, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EventEnumTwilioEdgeOrStr` | `twilio/models/enums/event_enum_twilio_edge.py` |
| `ListEventResponse1` | `twilio/models/list_event_response1.py` |

