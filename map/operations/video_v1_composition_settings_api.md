<!-- Generated file — do not edit; regenerated with the SDK. -->

# VideoV1CompositionSettingsApi — operations

Accessor: `client.video_v1_composition_settings_api` · Source: `twilio_sdk/apis/video_v1_composition_settings_api.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.video_v1_composition_settings_api.create_composition_settings

- **Route**: `POST /v1/CompositionSettings/Default`
- **Server**: `default6`
- **Signature**: `def create_composition_settings(friendly_name: str, *, aws_credentials_sid: str | None = None, encryption_key_sid: str | None = None, aws_s3_url: AnyUrl | None = None, aws_storage_enabled: bool | None = None, encryption_enabled: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `friendly_name`
- **Params**: `friendly_name` — form field `FriendlyName` · `aws_credentials_sid` — form field `AwsCredentialsSid` · `encryption_key_sid` — form field `EncryptionKeySid` · `aws_s3_url` — form field `AwsS3Url` · `aws_storage_enabled` — form field `AwsStorageEnabled` · `encryption_enabled` — form field `EncryptionEnabled`
- **Returns (parsed)**: `VideoV1CompositionSettings`
- **Returns (raw)**: `ApiResult[VideoV1CompositionSettings, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VideoV1CompositionSettings` | `twilio_sdk/models/video_v1_composition_settings.py` |

### client.video_v1_composition_settings_api.fetch_composition_settings

- **Route**: `GET /v1/CompositionSettings/Default`
- **Server**: `default6`
- **Signature**: `def fetch_composition_settings(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `VideoV1CompositionSettings`
- **Returns (raw)**: `ApiResult[VideoV1CompositionSettings, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VideoV1CompositionSettings` | `twilio_sdk/models/video_v1_composition_settings.py` |

