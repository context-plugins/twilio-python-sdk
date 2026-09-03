<!-- Generated file — do not edit; regenerated with the SDK. -->

# InsightsV1ConferenceParticipant — operations

Accessor: `client.insights_v1_conference_participant` · Source: `twilio_sdk/apis/insights_v1_conference_participant.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.insights_v1_conference_participant.fetch_conference_participant

- **Route**: `GET /v1/Conferences/{ConferenceSid}/Participants/{ParticipantSid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default14`
- **Signature**: `def fetch_conference_participant(conference_sid: str, participant_sid: str, *, events: str | None = None, metrics: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `conference_sid`, `participant_sid`
- **Params**: `conference_sid` — path `ConferenceSid` · `participant_sid` — path `ParticipantSid` · `events` — query `Events` · `metrics` — query `Metrics`
- **Returns (parsed)**: `InsightsV1ConferenceConferenceParticipant`
- **Returns (raw)**: `ApiResult[InsightsV1ConferenceConferenceParticipant, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InsightsV1ConferenceConferenceParticipant` | `twilio_sdk/models/insights_v1_conference_conference_participant.py` |

### client.insights_v1_conference_participant.list_conference_participant

- **Route**: `GET /v1/Conferences/{ConferenceSid}/Participants`
- **Auth**: `account_sid_auth_token`
- **Server**: `default14`
- **Signature**: `def list_conference_participant(conference_sid: str, *, participant_sid: str | None = None, label: str | None = None, events: str | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `conference_sid`
- **Params**: `conference_sid` — path `ConferenceSid` · `participant_sid` — query `ParticipantSid` · `label` — query `Label` · `events` — query `Events` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListConferenceParticipantResponse`
- **Returns (raw)**: `ApiResult[ListConferenceParticipantResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListConferenceParticipantResponse` | `twilio_sdk/models/list_conference_participant_response.py` |

