<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401MediaInstance — operations

Accessor: `client.api20100401_media_instance` · Source: `twilio_sdk/apis/api20100401_media_instance.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.api20100401_media_instance.delete_media

- **Route**: `DELETE /2010-04-01/Accounts/{AccountSid}/Messages/{MessageSid}/Media/{Sid}.json`
- **Server**: `default`
- **Signature**: `def delete_media(account_sid: str, message_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `message_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `message_sid` — path `MessageSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.api20100401_media_instance.fetch_media

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/Messages/{MessageSid}/Media/{Sid}.json`
- **Server**: `default`
- **Signature**: `def fetch_media(account_sid: str, message_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `message_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `message_sid` — path `MessageSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ApiV2010AccountMessageMedia`
- **Returns (raw)**: `ApiResult[ApiV2010AccountMessageMedia, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountMessageMedia` | `twilio_sdk/models/api_v2010_account_message_media.py` |

