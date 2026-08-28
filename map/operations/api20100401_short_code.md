<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401ShortCode — operations

Accessor: `client.api20100401_short_code` · Source: `twilio/apis/api20100401_short_code.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.api20100401_short_code.fetch_short_code

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/SMS/ShortCodes/{Sid}.json`
- **Server**: `default`
- **Signature**: `def fetch_short_code(account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ApiV2010AccountShortCode`
- **Returns (raw)**: `ApiResult[ApiV2010AccountShortCode, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountShortCode` | `twilio/models/api_v2010_account_short_code.py` |

### client.api20100401_short_code.list_short_code

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/SMS/ShortCodes.json`
- **Server**: `default`
- **Signature**: `def list_short_code(account_sid: str, *, friendly_name: str | None = None, short_code: str | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`
- **Params**: `account_sid` — path `AccountSid` · `friendly_name` — query `FriendlyName` · `short_code` — query `ShortCode` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListShortCodeResponse`
- **Returns (raw)**: `ApiResult[ListShortCodeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListShortCodeResponse` | `twilio/models/list_short_code_response.py` |

### client.api20100401_short_code.update_short_code

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/SMS/ShortCodes/{Sid}.json`
- **Server**: `default`
- **Signature**: `def update_short_code(account_sid: str, sid: str, *, friendly_name: str | None = None, api_version: str | None = None, sms_url: str | None = None, sms_method: SmsMethod14OrStr | None = None, sms_fallback_url: str | None = None, sms_fallback_method: SmsFallbackMethod14OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid` · `friendly_name` — form field `FriendlyName` · `api_version` — form field `ApiVersion` · `sms_url` — form field `SmsUrl` · `sms_method` — form field `SmsMethod` · `sms_fallback_url` — form field `SmsFallbackUrl` · `sms_fallback_method` — form field `SmsFallbackMethod`
- **Returns (parsed)**: `ApiV2010AccountShortCode`
- **Returns (raw)**: `ApiResult[ApiV2010AccountShortCode, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SmsMethod14OrStr` | `twilio/models/enums/sms_method14.py` |
| `SmsFallbackMethod14OrStr` | `twilio/models/enums/sms_fallback_method14.py` |
| `ApiV2010AccountShortCode` | `twilio/models/api_v2010_account_short_code.py` |

