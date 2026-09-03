<!-- Generated file — do not edit; regenerated with the SDK. -->

# VideoV1Participant — operations

Accessor: `client.video_v1_participant` · Source: `twilio_sdk/apis/video_v1_participant.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.video_v1_participant.fetch_room_participant

- **Route**: `GET /v1/Rooms/{RoomSid}/Participants/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default6`
- **Signature**: `def fetch_room_participant(room_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `room_sid`, `sid`
- **Params**: `room_sid` — path `RoomSid` · `sid` — path `Sid`
- **Returns (parsed)**: `VideoV1RoomRoomParticipant`
- **Returns (raw)**: `ApiResult[VideoV1RoomRoomParticipant, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VideoV1RoomRoomParticipant` | `twilio_sdk/models/video_v1_room_room_participant.py` |

### client.video_v1_participant.list_room_participant

- **Route**: `GET /v1/Rooms/{RoomSid}/Participants`
- **Auth**: `account_sid_auth_token`
- **Server**: `default6`
- **Signature**: `def list_room_participant(room_sid: str, *, status: RoomParticipantEnumStatusOrStr | None = None, identity: str | None = None, date_created_after: RFC3339DateTime | None = None, date_created_before: RFC3339DateTime | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `room_sid`
- **Params**: `room_sid` — path `RoomSid` · `status` — query `Status` · `identity` — query `Identity` · `date_created_after` — query `DateCreatedAfter` · `date_created_before` — query `DateCreatedBefore` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListRoomParticipantResponse`
- **Returns (raw)**: `ApiResult[ListRoomParticipantResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RoomParticipantEnumStatusOrStr` | `twilio_sdk/models/enums/room_participant_enum_status.py` |
| `ListRoomParticipantResponse` | `twilio_sdk/models/list_room_participant_response.py` |

### client.video_v1_participant.update_room_participant

- **Route**: `POST /v1/Rooms/{RoomSid}/Participants/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default6`
- **Signature**: `def update_room_participant(room_sid: str, sid: str, *, status: RoomParticipantEnumStatusOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `room_sid`, `sid`
- **Params**: `room_sid` — path `RoomSid` · `sid` — path `Sid` · `status` — form field `Status`
- **Returns (parsed)**: `VideoV1RoomRoomParticipant`
- **Returns (raw)**: `ApiResult[VideoV1RoomRoomParticipant, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RoomParticipantEnumStatusOrStr` | `twilio_sdk/models/enums/room_participant_enum_status.py` |
| `VideoV1RoomRoomParticipant` | `twilio_sdk/models/video_v1_room_room_participant.py` |

