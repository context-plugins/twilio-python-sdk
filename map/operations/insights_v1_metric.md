<!-- Generated file — do not edit; regenerated with the SDK. -->

# InsightsV1Metric — operations

Accessor: `client.insights_v1_metric` · Source: `twilio_sdk/apis/insights_v1_metric.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.insights_v1_metric.list_metric

- **Route**: `GET /v1/Voice/{CallSid}/Metrics`
- **Server**: `default14`
- **Signature**: `def list_metric(call_sid: str, *, edge: MetricEnumTwilioEdgeOrStr | None = None, direction: MetricEnumStreamDirectionOrStr | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `call_sid`
- **Params**: `call_sid` — path `CallSid` · `edge` — query `Edge` · `direction` — query `Direction` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListMetricResponse`
- **Returns (raw)**: `ApiResult[ListMetricResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MetricEnumTwilioEdgeOrStr` | `twilio_sdk/models/enums/metric_enum_twilio_edge.py` |
| `MetricEnumStreamDirectionOrStr` | `twilio_sdk/models/enums/metric_enum_stream_direction.py` |
| `ListMetricResponse` | `twilio_sdk/models/list_metric_response.py` |

