<!-- Generated file — do not edit; regenerated with the SDK. -->

# VideoV1RecordingApi — operations

Accessor: `client.video_v1_recording_api` · Source: `twilio_sdk/apis/video_v1_recording_api.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.video_v1_recording_api.delete_recording2

- **Route**: `DELETE /v1/Recordings/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default6`
- **Signature**: `def delete_recording2(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.video_v1_recording_api.fetch_recording2

- **Route**: `GET /v1/Recordings/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default6`
- **Signature**: `def fetch_recording2(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `VideoV1Recording`
- **Returns (raw)**: `ApiResult[VideoV1Recording, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VideoV1Recording` | `twilio_sdk/models/video_v1_recording.py` |

### client.video_v1_recording_api.list_recording2

- **Route**: `GET /v1/Recordings`
- **Auth**: `account_sid_auth_token`
- **Server**: `default6`
- **Signature**: `def list_recording2(*, status: RecordingEnumStatus1OrStr | None = None, source_sid: str | None = None, grouping_sid: list[str] | None = None, date_created_after: RFC3339DateTime | None = None, date_created_before: RFC3339DateTime | None = None, media_type: RecordingEnumTypeOrStr | None = None, page_size: int | None = 50, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `status` — query `Status` · `source_sid` — query `SourceSid` · `grouping_sid` — query `GroupingSid` · `date_created_after` — query `DateCreatedAfter` · `date_created_before` — query `DateCreatedBefore` · `media_type` — query `MediaType` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListRecordingResponse1`
- **Returns (raw)**: `ApiResult[ListRecordingResponse1, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RecordingEnumStatus1OrStr` | `twilio_sdk/models/enums/recording_enum_status1.py` |
| `RecordingEnumTypeOrStr` | `twilio_sdk/models/enums/recording_enum_type.py` |
| `ListRecordingResponse1` | `twilio_sdk/models/list_recording_response1.py` |

