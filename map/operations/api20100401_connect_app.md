<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401ConnectApp — operations

Accessor: `client.api20100401_connect_app` · Source: `twilio/apis/api20100401_connect_app.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.api20100401_connect_app.delete_connect_app

- **Route**: `DELETE /2010-04-01/Accounts/{AccountSid}/ConnectApps/{Sid}.json`
- **Server**: `default`
- **Signature**: `def delete_connect_app(account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.api20100401_connect_app.fetch_connect_app

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/ConnectApps/{Sid}.json`
- **Server**: `default`
- **Signature**: `def fetch_connect_app(account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ApiV2010AccountConnectApp`
- **Returns (raw)**: `ApiResult[ApiV2010AccountConnectApp, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountConnectApp` | `twilio/models/api_v2010_account_connect_app.py` |

### client.api20100401_connect_app.list_connect_app

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/ConnectApps.json`
- **Server**: `default`
- **Signature**: `def list_connect_app(account_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`
- **Params**: `account_sid` — path `AccountSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListConnectAppResponse`
- **Returns (raw)**: `ApiResult[ListConnectAppResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListConnectAppResponse` | `twilio/models/list_connect_app_response.py` |

### client.api20100401_connect_app.update_connect_app

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/ConnectApps/{Sid}.json`
- **Server**: `default`
- **Signature**: `def update_connect_app(account_sid: str, sid: str, *, authorize_redirect_url: str | None = None, company_name: str | None = None, deauthorize_callback_method: DeauthorizeCallbackMethod1OrStr | None = None, deauthorize_callback_url: str | None = None, description: str | None = None, friendly_name: str | None = None, homepage_url: str | None = None, permissions: list[ConnectAppEnumPermissionOrStr] | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid` · `authorize_redirect_url` — form field `AuthorizeRedirectUrl` · `company_name` — form field `CompanyName` · `deauthorize_callback_method` — form field `DeauthorizeCallbackMethod` · `deauthorize_callback_url` — form field `DeauthorizeCallbackUrl` · `description` — form field `Description` · `friendly_name` — form field `FriendlyName` · `homepage_url` — form field `HomepageUrl` · `permissions` — form field `Permissions`
- **Returns (parsed)**: `ApiV2010AccountConnectApp`
- **Returns (raw)**: `ApiResult[ApiV2010AccountConnectApp, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DeauthorizeCallbackMethod1OrStr` | `twilio/models/enums/deauthorize_callback_method1.py` |
| `ConnectAppEnumPermissionOrStr` | `twilio/models/enums/connect_app_enum_permission.py` |
| `ApiV2010AccountConnectApp` | `twilio/models/api_v2010_account_connect_app.py` |

