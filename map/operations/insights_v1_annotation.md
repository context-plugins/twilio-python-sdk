<!-- Generated file — do not edit; regenerated with the SDK. -->

# InsightsV1Annotation — operations

Accessor: `client.insights_v1_annotation` · Source: `twilio_sdk/apis/insights_v1_annotation.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.insights_v1_annotation.fetch_annotation

- **Route**: `GET /v1/Voice/{CallSid}/Annotation`
- **Server**: `default14`
- **Signature**: `def fetch_annotation(call_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `call_sid`
- **Params**: `call_sid` — path `CallSid`
- **Returns (parsed)**: `InsightsV1CallAnnotation`
- **Returns (raw)**: `ApiResult[InsightsV1CallAnnotation, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InsightsV1CallAnnotation` | `twilio_sdk/models/insights_v1_call_annotation.py` |

### client.insights_v1_annotation.update_annotation

- **Route**: `POST /v1/Voice/{CallSid}/Annotation`
- **Server**: `default14`
- **Signature**: `def update_annotation(call_sid: str, *, answered_by: AnnotationEnumAnsweredByOrStr | None = None, connectivity_issue: AnnotationEnumConnectivityIssueOrStr | None = None, quality_issues: str | None = None, spam: bool | None = None, call_score: int | None = None, comment: str | None = None, incident: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `call_sid`
- **Params**: `call_sid` — path `CallSid` · `answered_by` — form field `AnsweredBy` · `connectivity_issue` — form field `ConnectivityIssue` · `quality_issues` — form field `QualityIssues` · `spam` — form field `Spam` · `call_score` — form field `CallScore` · `comment` — form field `Comment` · `incident` — form field `Incident`
- **Returns (parsed)**: `InsightsV1CallAnnotation`
- **Returns (raw)**: `ApiResult[InsightsV1CallAnnotation, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AnnotationEnumAnsweredByOrStr` | `twilio_sdk/models/enums/annotation_enum_answered_by.py` |
| `AnnotationEnumConnectivityIssueOrStr` | `twilio_sdk/models/enums/annotation_enum_connectivity_issue.py` |
| `InsightsV1CallAnnotation` | `twilio_sdk/models/insights_v1_call_annotation.py` |

