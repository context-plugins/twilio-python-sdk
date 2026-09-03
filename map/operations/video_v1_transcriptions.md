<!-- Generated file — do not edit; regenerated with the SDK. -->

# VideoV1Transcriptions — operations

Accessor: `client.video_v1_transcriptions` · Source: `twilio_sdk/apis/video_v1_transcriptions.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.video_v1_transcriptions.create_room_transcriptions

- **Route**: `POST /v1/Rooms/{RoomSid}/Transcriptions`
- **Auth**: `account_sid_auth_token`
- **Server**: `default6`
- **Signature**: `def create_room_transcriptions(room_sid: str, *, configuration: Any | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `room_sid`
- **Params**: `room_sid` — path `RoomSid` · `configuration` — form field `Configuration`
- **Returns (parsed)**: `VideoV1RoomRoomTranscriptions`
- **Returns (raw)**: `ApiResult[VideoV1RoomRoomTranscriptions, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VideoV1RoomRoomTranscriptions` | `twilio_sdk/models/video_v1_room_room_transcriptions.py` |

### client.video_v1_transcriptions.fetch_room_transcriptions

- **Route**: `GET /v1/Rooms/{RoomSid}/Transcriptions/{Ttid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default6`
- **Signature**: `def fetch_room_transcriptions(room_sid: str, ttid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `room_sid`, `ttid`
- **Params**: `room_sid` — path `RoomSid` · `ttid` — path `Ttid`
- **Returns (parsed)**: `VideoV1RoomRoomTranscriptions`
- **Returns (raw)**: `ApiResult[VideoV1RoomRoomTranscriptions, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VideoV1RoomRoomTranscriptions` | `twilio_sdk/models/video_v1_room_room_transcriptions.py` |

### client.video_v1_transcriptions.list_room_transcriptions

- **Route**: `GET /v1/Rooms/{RoomSid}/Transcriptions`
- **Auth**: `account_sid_auth_token`
- **Server**: `default6`
- **Signature**: `def list_room_transcriptions(room_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `room_sid`
- **Params**: `room_sid` — path `RoomSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListRoomTranscriptionsResponse`
- **Returns (raw)**: `ApiResult[ListRoomTranscriptionsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListRoomTranscriptionsResponse` | `twilio_sdk/models/list_room_transcriptions_response.py` |

### client.video_v1_transcriptions.update_room_transcriptions

- **Route**: `POST /v1/Rooms/{RoomSid}/Transcriptions/{Ttid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default6`
- **Signature**: `def update_room_transcriptions(room_sid: str, ttid: str, *, status: RoomTranscriptionsEnumStatusOrStr | None = None, configuration: Any | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `room_sid`, `ttid`
- **Params**: `room_sid` — path `RoomSid` · `ttid` — path `Ttid` · `status` — form field `Status` · `configuration` — form field `Configuration`
- **Returns (parsed)**: `VideoV1RoomRoomTranscriptions`
- **Returns (raw)**: `ApiResult[VideoV1RoomRoomTranscriptions, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RoomTranscriptionsEnumStatusOrStr` | `twilio_sdk/models/enums/room_transcriptions_enum_status.py` |
| `VideoV1RoomRoomTranscriptions` | `twilio_sdk/models/video_v1_room_room_transcriptions.py` |

