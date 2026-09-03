<!-- Generated file — do not edit; regenerated with the SDK. -->

# InsightsV1Room — operations

Accessor: `client.insights_v1_room` · Source: `twilio_sdk/apis/insights_v1_room.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.insights_v1_room.fetch_video_room_summary

- **Route**: `GET /v1/Video/Rooms/{RoomSid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default14`
- **Signature**: `def fetch_video_room_summary(room_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `room_sid`
- **Params**: `room_sid` — path `RoomSid`
- **Returns (parsed)**: `InsightsV1VideoRoomSummary`
- **Returns (raw)**: `ApiResult[InsightsV1VideoRoomSummary, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InsightsV1VideoRoomSummary` | `twilio_sdk/models/insights_v1_video_room_summary.py` |

### client.insights_v1_room.list_video_room_summary

- **Route**: `GET /v1/Video/Rooms`
- **Auth**: `account_sid_auth_token`
- **Server**: `default14`
- **Signature**: `def list_video_room_summary(*, room_type: list[VideoRoomSummaryEnumRoomTypeOrStr] | None = None, codec: list[VideoRoomSummaryEnumCodecOrStr] | None = None, room_name: str | None = None, created_after: RFC3339DateTime | None = None, created_before: RFC3339DateTime | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `room_type` — query `RoomType` · `codec` — query `Codec` · `room_name` — query `RoomName` · `created_after` — query `CreatedAfter` · `created_before` — query `CreatedBefore` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListVideoRoomSummaryResponse`
- **Returns (raw)**: `ApiResult[ListVideoRoomSummaryResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VideoRoomSummaryEnumRoomTypeOrStr` | `twilio_sdk/models/enums/video_room_summary_enum_room_type.py` |
| `VideoRoomSummaryEnumCodecOrStr` | `twilio_sdk/models/enums/video_room_summary_enum_codec.py` |
| `ListVideoRoomSummaryResponse` | `twilio_sdk/models/list_video_room_summary_response.py` |

