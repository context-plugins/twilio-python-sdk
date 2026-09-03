<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401AuthorizedConnectApp — operations

Accessor: `client.api20100401_authorized_connect_app` · Source: `twilio_sdk/apis/api20100401_authorized_connect_app.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.api20100401_authorized_connect_app.fetch_authorized_connect_app

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/AuthorizedConnectApps/{ConnectAppSid}.json`
- **Auth**: `account_sid_auth_token`
- **Server**: `default`
- **Signature**: `def fetch_authorized_connect_app(account_sid: str, connect_app_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `connect_app_sid`
- **Params**: `account_sid` — path `AccountSid` · `connect_app_sid` — path `ConnectAppSid`
- **Returns (parsed)**: `ApiV2010AccountAuthorizedConnectApp`
- **Returns (raw)**: `ApiResult[ApiV2010AccountAuthorizedConnectApp, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountAuthorizedConnectApp` | `twilio_sdk/models/api_v2010_account_authorized_connect_app.py` |

### client.api20100401_authorized_connect_app.list_authorized_connect_app

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/AuthorizedConnectApps.json`
- **Auth**: `account_sid_auth_token`
- **Server**: `default`
- **Signature**: `def list_authorized_connect_app(account_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`
- **Params**: `account_sid` — path `AccountSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListAuthorizedConnectAppResponse`
- **Returns (raw)**: `ApiResult[ListAuthorizedConnectAppResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListAuthorizedConnectAppResponse` | `twilio_sdk/models/list_authorized_connect_app_response.py` |

