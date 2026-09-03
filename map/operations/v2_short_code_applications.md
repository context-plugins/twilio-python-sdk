<!-- Generated file — do not edit; regenerated with the SDK. -->

# V2ShortCodeApplications — operations

Accessor: `client.v2_short_code_applications` · Source: `twilio_sdk/apis/v2_short_code_applications.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.v2_short_code_applications.create_short_code_application

- **Route**: `POST /v2/ShortCodes/Applications`
- **Auth**: `account_sid_auth_token`
- **Server**: `default5`
- **Signature**: `def create_short_code_application(body: CreateShortCodeApplicationRequest | CreateShortCodeApplicationRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateShortCodeApplicationResponse`
- **Returns (raw)**: `ApiResult[CreateShortCodeApplicationResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateShortCodeApplicationRequest` | `twilio_sdk/models/create_short_code_application_request.py` |
| `CreateShortCodeApplicationRequestDict` | `twilio_sdk/models/create_short_code_application_request.py` |
| `CreateShortCodeApplicationResponse` | `twilio_sdk/models/create_short_code_application_response.py` |

### client.v2_short_code_applications.fetch_short_code_application

- **Route**: `GET /v2/ShortCodes/Applications/{sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default5`
- **Signature**: `def fetch_short_code_application(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path
- **Returns (parsed)**: `ShortCodeApplication`
- **Returns (raw)**: `ApiResult[ShortCodeApplication, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ShortCodeApplication` | `twilio_sdk/models/short_code_application.py` |

### client.v2_short_code_applications.list_short_code_applications

- **Route**: `GET /v2/ShortCodes/Applications`
- **Auth**: `account_sid_auth_token`
- **Server**: `default5`
- **Signature**: `def list_short_code_applications(*, account_sid: str | None = None, iso_country: str | None = None, status: str | None = None, friendly_name: str | None = None, sid: str | None = None, page_size: int | None = None, page: int | None = 0, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `account_sid` — query `AccountSid` · `iso_country` — query `IsoCountry` · `status` — query `Status` · `friendly_name` — query `FriendlyName` · `sid` — query `Sid` · `page_size` — query `PageSize` · `page` — query `Page`
- **Returns (parsed)**: `ShortCodeApplicationResponsePage`
- **Returns (raw)**: `ApiResult[ShortCodeApplicationResponsePage, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ShortCodeApplicationResponsePage` | `twilio_sdk/models/short_code_application_response_page.py` |

