<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401NewKey — operations

Accessor: `client.api20100401_new_key` · Source: `twilio_sdk/apis/api20100401_new_key.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.api20100401_new_key.create_new_key

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/Keys.json`
- **Auth**: `account_sid_auth_token`
- **Server**: `default`
- **Signature**: `def create_new_key(account_sid: str, *, friendly_name: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`
- **Params**: `account_sid` — path `AccountSid` · `friendly_name` — form field `FriendlyName`
- **Returns (parsed)**: `ApiV2010AccountNewKey`
- **Returns (raw)**: `ApiResult[ApiV2010AccountNewKey, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountNewKey` | `twilio_sdk/models/api_v2010_account_new_key.py` |

