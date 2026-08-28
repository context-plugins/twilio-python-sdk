<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401Balance — operations

Accessor: `client.api20100401_balance` · Source: `twilio_sdk/apis/api20100401_balance.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.api20100401_balance.fetch_balance

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/Balance.json`
- **Server**: `default`
- **Signature**: `def fetch_balance(account_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`
- **Params**: `account_sid` — path `AccountSid`
- **Returns (parsed)**: `ApiV2010AccountBalance`
- **Returns (raw)**: `ApiResult[ApiV2010AccountBalance, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountBalance` | `twilio_sdk/models/api_v2010_account_balance.py` |

