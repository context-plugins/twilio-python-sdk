<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401SigningKey — operations

Accessor: `client.api20100401_signing_key` · Source: `twilio_sdk/apis/api20100401_signing_key.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.api20100401_signing_key.delete_signing_key

- **Route**: `DELETE /2010-04-01/Accounts/{AccountSid}/SigningKeys/{Sid}.json`
- **Server**: `default`
- **Signature**: `def delete_signing_key(account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.api20100401_signing_key.fetch_signing_key

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/SigningKeys/{Sid}.json`
- **Server**: `default`
- **Signature**: `def fetch_signing_key(account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ApiV2010AccountSigningKey`
- **Returns (raw)**: `ApiResult[ApiV2010AccountSigningKey, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountSigningKey` | `twilio_sdk/models/api_v2010_account_signing_key.py` |

### client.api20100401_signing_key.list_signing_key

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/SigningKeys.json`
- **Server**: `default`
- **Signature**: `def list_signing_key(account_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`
- **Params**: `account_sid` — path `AccountSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListSigningKeyResponse`
- **Returns (raw)**: `ApiResult[ListSigningKeyResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListSigningKeyResponse` | `twilio_sdk/models/list_signing_key_response.py` |

### client.api20100401_signing_key.update_signing_key

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/SigningKeys/{Sid}.json`
- **Server**: `default`
- **Signature**: `def update_signing_key(account_sid: str, sid: str, *, friendly_name: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid` · `friendly_name` — form field `FriendlyName`
- **Returns (parsed)**: `ApiV2010AccountSigningKey`
- **Returns (raw)**: `ApiResult[ApiV2010AccountSigningKey, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountSigningKey` | `twilio_sdk/models/api_v2010_account_signing_key.py` |

