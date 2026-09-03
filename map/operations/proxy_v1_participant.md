<!-- Generated file — do not edit; regenerated with the SDK. -->

# ProxyV1Participant — operations

Accessor: `client.proxy_v1_participant` · Source: `twilio_sdk/apis/proxy_v1_participant.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.proxy_v1_participant.create_participant2

- **Route**: `POST /v1/Services/{ServiceSid}/Sessions/{SessionSid}/Participants`
- **Auth**: `account_sid_auth_token`
- **Server**: `default10`
- **Signature**: `def create_participant2(service_sid: str, session_sid: str, identifier: str, *, friendly_name: str | None = None, proxy_identifier: str | None = None, proxy_identifier_sid: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `session_sid`, `identifier`
- **Params**: `service_sid` — path `ServiceSid` · `session_sid` — path `SessionSid` · `identifier` — form field `Identifier` · `friendly_name` — form field `FriendlyName` · `proxy_identifier` — form field `ProxyIdentifier` · `proxy_identifier_sid` — form field `ProxyIdentifierSid`
- **Returns (parsed)**: `ProxyV1ServiceSessionParticipant`
- **Returns (raw)**: `ApiResult[ProxyV1ServiceSessionParticipant, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProxyV1ServiceSessionParticipant` | `twilio_sdk/models/proxy_v1_service_session_participant.py` |

### client.proxy_v1_participant.delete_participant2

- **Route**: `DELETE /v1/Services/{ServiceSid}/Sessions/{SessionSid}/Participants/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default10`
- **Signature**: `def delete_participant2(service_sid: str, session_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `session_sid`, `sid`
- **Params**: `service_sid` — path `ServiceSid` · `session_sid` — path `SessionSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.proxy_v1_participant.fetch_participant3

- **Route**: `GET /v1/Services/{ServiceSid}/Sessions/{SessionSid}/Participants/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default10`
- **Signature**: `def fetch_participant3(service_sid: str, session_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `session_sid`, `sid`
- **Params**: `service_sid` — path `ServiceSid` · `session_sid` — path `SessionSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ProxyV1ServiceSessionParticipant`
- **Returns (raw)**: `ApiResult[ProxyV1ServiceSessionParticipant, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProxyV1ServiceSessionParticipant` | `twilio_sdk/models/proxy_v1_service_session_participant.py` |

### client.proxy_v1_participant.list_participant2

- **Route**: `GET /v1/Services/{ServiceSid}/Sessions/{SessionSid}/Participants`
- **Auth**: `account_sid_auth_token`
- **Server**: `default10`
- **Signature**: `def list_participant2(service_sid: str, session_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `session_sid`
- **Params**: `service_sid` — path `ServiceSid` · `session_sid` — path `SessionSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListParticipantResponse1`
- **Returns (raw)**: `ApiResult[ListParticipantResponse1, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListParticipantResponse1` | `twilio_sdk/models/list_participant_response1.py` |

