<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401Account — operations

Accessor: `client.api20100401_account` · Source: `twilio/apis/api20100401_account.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.api20100401_account.create_account

- **Route**: `POST /2010-04-01/Accounts.json`
- **Server**: `default`
- **Signature**: `def create_account(*, friendly_name: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `friendly_name` — form field `FriendlyName`
- **Returns (parsed)**: `ApiV2010Account`
- **Returns (raw)**: `ApiResult[ApiV2010Account, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010Account` | `twilio/models/api_v2010_account.py` |

### client.api20100401_account.fetch_account

- **Route**: `GET /2010-04-01/Accounts/{Sid}.json`
- **Server**: `default`
- **Signature**: `def fetch_account(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `ApiV2010Account`
- **Returns (raw)**: `ApiResult[ApiV2010Account, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010Account` | `twilio/models/api_v2010_account.py` |

### client.api20100401_account.list_account

- **Route**: `GET /2010-04-01/Accounts.json`
- **Server**: `default`
- **Signature**: `def list_account(*, friendly_name: str | None = None, status: AccountEnumStatusOrStr | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `friendly_name` — query `FriendlyName` · `status` — query `Status` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListAccountResponse`
- **Returns (raw)**: `ApiResult[ListAccountResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AccountEnumStatusOrStr` | `twilio/models/enums/account_enum_status.py` |
| `ListAccountResponse` | `twilio/models/list_account_response.py` |

### client.api20100401_account.update_account

- **Route**: `POST /2010-04-01/Accounts/{Sid}.json`
- **Server**: `default`
- **Signature**: `def update_account(sid: str, *, friendly_name: str | None = None, status: AccountEnumStatusOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid` · `friendly_name` — form field `FriendlyName` · `status` — form field `Status`
- **Returns (parsed)**: `ApiV2010Account`
- **Returns (raw)**: `ApiResult[ApiV2010Account, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AccountEnumStatusOrStr` | `twilio/models/enums/account_enum_status.py` |
| `ApiV2010Account` | `twilio/models/api_v2010_account.py` |

