<!-- Generated file — do not edit; regenerated with the SDK. -->

# VideoV1RoomApi — operations

Accessor: `client.video_v1_room_api` · Source: `twilio_sdk/apis/video_v1_room_api.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.video_v1_room_api.create_room

- **Route**: `POST /v1/Rooms`
- **Server**: `default6`
- **Signature**: `def create_room(*, enable_turn: bool | None = None, type_: RoomEnumRoomTypeOrStr | None = None, unique_name: str | None = None, status_callback: AnyUrl | None = None, status_callback_method: AmdStatusCallbackMethodOrStr | None = None, max_participants: int | None = None, record_participants_on_connect: bool | None = None, transcribe_participants_on_connect: bool | None = None, video_codecs: list[RoomEnumVideoCodecOrStr] | None = None, media_region: str | None = None, recording_rules: Any | None = None, transcriptions_configuration: Any | None = None, audio_only: bool | None = None, max_participant_duration: int | None = None, empty_room_timeout: int | None = None, unused_room_timeout: int | None = None, large_room: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `enable_turn` — form field `EnableTurn` · `type_` — form field `Type` · `unique_name` — form field `UniqueName` · `status_callback` — form field `StatusCallback` · `status_callback_method` — form field `StatusCallbackMethod` · `max_participants` — form field `MaxParticipants` · `record_participants_on_connect` — form field `RecordParticipantsOnConnect` · `transcribe_participants_on_connect` — form field `TranscribeParticipantsOnConnect` · `video_codecs` — form field `VideoCodecs` · `media_region` — form field `MediaRegion` · `recording_rules` — form field `RecordingRules` · `transcriptions_configuration` — form field `TranscriptionsConfiguration` · `audio_only` — form field `AudioOnly` · `max_participant_duration` — form field `MaxParticipantDuration` · `empty_room_timeout` — form field `EmptyRoomTimeout` · `unused_room_timeout` — form field `UnusedRoomTimeout` · `large_room` — form field `LargeRoom`
- **Returns (parsed)**: `VideoV1Room`
- **Returns (raw)**: `ApiResult[VideoV1Room, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RoomEnumRoomTypeOrStr` | `twilio_sdk/models/enums/room_enum_room_type.py` |
| `AmdStatusCallbackMethodOrStr` | `twilio_sdk/models/enums/amd_status_callback_method.py` |
| `RoomEnumVideoCodecOrStr` | `twilio_sdk/models/enums/room_enum_video_codec.py` |
| `VideoV1Room` | `twilio_sdk/models/video_v1_room.py` |

### client.video_v1_room_api.fetch_room

- **Route**: `GET /v1/Rooms/{Sid}`
- **Server**: `default6`
- **Signature**: `def fetch_room(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `VideoV1Room`
- **Returns (raw)**: `ApiResult[VideoV1Room, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VideoV1Room` | `twilio_sdk/models/video_v1_room.py` |

### client.video_v1_room_api.list_room

- **Route**: `GET /v1/Rooms`
- **Server**: `default6`
- **Signature**: `def list_room(*, status: RecordingTranscriptionEnumStatusOrStr | None = None, unique_name: str | None = None, date_created_after: RFC3339DateTime | None = None, date_created_before: RFC3339DateTime | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `status` — query `Status` · `unique_name` — query `UniqueName` · `date_created_after` — query `DateCreatedAfter` · `date_created_before` — query `DateCreatedBefore` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListRoomResponse`
- **Returns (raw)**: `ApiResult[ListRoomResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RecordingTranscriptionEnumStatusOrStr` | `twilio_sdk/models/enums/recording_transcription_enum_status.py` |
| `ListRoomResponse` | `twilio_sdk/models/list_room_response.py` |

### client.video_v1_room_api.update_room

- **Route**: `POST /v1/Rooms/{Sid}`
- **Server**: `default6`
- **Signature**: `def update_room(sid: str, status: RecordingTranscriptionEnumStatusOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`, `status`
- **Params**: `sid` — path `Sid` · `status` — form field `Status`
- **Returns (parsed)**: `VideoV1Room`
- **Returns (raw)**: `ApiResult[VideoV1Room, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RecordingTranscriptionEnumStatusOrStr` | `twilio_sdk/models/enums/recording_transcription_enum_status.py` |
| `VideoV1Room` | `twilio_sdk/models/video_v1_room.py` |

