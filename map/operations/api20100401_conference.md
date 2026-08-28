<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401Conference — operations

Accessor: `client.api20100401_conference` · Source: `twilio/apis/api20100401_conference.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.api20100401_conference.fetch_conference

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/Conferences/{Sid}.json`
- **Server**: `default`
- **Signature**: `def fetch_conference(account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ApiV2010AccountConference`
- **Returns (raw)**: `ApiResult[ApiV2010AccountConference, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountConference` | `twilio/models/api_v2010_account_conference.py` |

### client.api20100401_conference.list_conference

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/Conferences.json`
- **Server**: `default`
- **Signature**: `def list_conference(account_sid: str, *, date_created: Date | None = None, date_created_query: Date | None = None, date_created_query_query: Date | None = None, date_updated: Date | None = None, date_updated_query: Date | None = None, date_updated_query_query: Date | None = None, friendly_name: str | None = None, status: ConferenceEnumStatusOrStr | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`
- **Params**: `account_sid` — path `AccountSid` · `date_created` — query `DateCreated` · `date_created_query` — query `DateCreated<` · `date_created_query_query` — query `DateCreated>` · `date_updated` — query `DateUpdated` · `date_updated_query` — query `DateUpdated<` · `date_updated_query_query` — query `DateUpdated>` · `friendly_name` — query `FriendlyName` · `status` — query `Status` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListConferenceResponse`
- **Returns (raw)**: `ApiResult[ListConferenceResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConferenceEnumStatusOrStr` | `twilio/models/enums/conference_enum_status.py` |
| `ListConferenceResponse` | `twilio/models/list_conference_response.py` |

### client.api20100401_conference.update_conference

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/Conferences/{Sid}.json`
- **Server**: `default`
- **Signature**: `def update_conference(account_sid: str, sid: str, *, status: ConferenceEnumUpdateStatusOrStr | None = None, announce_url: str | None = None, announce_method: AnnounceMethodOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid` · `status` — form field `Status` · `announce_url` — form field `AnnounceUrl` · `announce_method` — form field `AnnounceMethod`
- **Returns (parsed)**: `ApiV2010AccountConference`
- **Returns (raw)**: `ApiResult[ApiV2010AccountConference, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConferenceEnumUpdateStatusOrStr` | `twilio/models/enums/conference_enum_update_status.py` |
| `AnnounceMethodOrStr` | `twilio/models/enums/announce_method.py` |
| `ApiV2010AccountConference` | `twilio/models/api_v2010_account_conference.py` |

