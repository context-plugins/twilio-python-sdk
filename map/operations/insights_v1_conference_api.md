<!-- Generated file — do not edit; regenerated with the SDK. -->

# InsightsV1ConferenceApi — operations

Accessor: `client.insights_v1_conference_api` · Source: `twilio_sdk/apis/insights_v1_conference_api.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.insights_v1_conference_api.fetch_conference2

- **Route**: `GET /v1/Conferences/{ConferenceSid}`
- **Server**: `default14`
- **Signature**: `def fetch_conference2(conference_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `conference_sid`
- **Params**: `conference_sid` — path `ConferenceSid`
- **Returns (parsed)**: `InsightsV1Conference`
- **Returns (raw)**: `ApiResult[InsightsV1Conference, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InsightsV1Conference` | `twilio_sdk/models/insights_v1_conference.py` |

### client.insights_v1_conference_api.list_conference2

- **Route**: `GET /v1/Conferences`
- **Server**: `default14`
- **Signature**: `def list_conference2(*, conference_sid: str | None = None, friendly_name: str | None = None, status: str | None = None, created_after: str | None = None, created_before: str | None = None, mixer_region: str | None = None, tags: str | None = None, subaccount: str | None = None, detected_issues: str | None = None, end_reason: str | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `conference_sid` — query `ConferenceSid` · `friendly_name` — query `FriendlyName` · `status` — query `Status` · `created_after` — query `CreatedAfter` · `created_before` — query `CreatedBefore` · `mixer_region` — query `MixerRegion` · `tags` — query `Tags` · `subaccount` — query `Subaccount` · `detected_issues` — query `DetectedIssues` · `end_reason` — query `EndReason` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListConferenceResponse1`
- **Returns (raw)**: `ApiResult[ListConferenceResponse1, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListConferenceResponse1` | `twilio_sdk/models/list_conference_response1.py` |

