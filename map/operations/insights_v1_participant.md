<!-- Generated file — do not edit; regenerated with the SDK. -->

# InsightsV1Participant — operations

Accessor: `client.insights_v1_participant` · Source: `twilio/apis/insights_v1_participant.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.insights_v1_participant.fetch_video_participant_summary

- **Route**: `GET /v1/Video/Rooms/{RoomSid}/Participants/{ParticipantSid}`
- **Server**: `default14`
- **Signature**: `def fetch_video_participant_summary(room_sid: str, participant_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `room_sid`, `participant_sid`
- **Params**: `room_sid` — path `RoomSid` · `participant_sid` — path `ParticipantSid`
- **Returns (parsed)**: `InsightsV1VideoRoomSummaryVideoParticipantSummary`
- **Returns (raw)**: `ApiResult[InsightsV1VideoRoomSummaryVideoParticipantSummary, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InsightsV1VideoRoomSummaryVideoParticipantSummary` | `twilio/models/insights_v1_video_room_summary_video_participant_summary.py` |

### client.insights_v1_participant.list_video_participant_summary

- **Route**: `GET /v1/Video/Rooms/{RoomSid}/Participants`
- **Server**: `default14`
- **Signature**: `def list_video_participant_summary(room_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `room_sid`
- **Params**: `room_sid` — path `RoomSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListVideoParticipantSummaryResponse`
- **Returns (raw)**: `ApiResult[ListVideoParticipantSummaryResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListVideoParticipantSummaryResponse` | `twilio/models/list_video_participant_summary_response.py` |

