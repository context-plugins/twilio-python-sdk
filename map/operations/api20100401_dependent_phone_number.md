<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401DependentPhoneNumber — operations

Accessor: `client.api20100401_dependent_phone_number` · Source: `twilio_sdk/apis/api20100401_dependent_phone_number.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.api20100401_dependent_phone_number.list_dependent_phone_number

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/Addresses/{AddressSid}/DependentPhoneNumbers.json`
- **Auth**: `account_sid_auth_token`
- **Server**: `default`
- **Signature**: `def list_dependent_phone_number(account_sid: str, address_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `address_sid`
- **Params**: `account_sid` — path `AccountSid` · `address_sid` — path `AddressSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListDependentPhoneNumberResponse`
- **Returns (raw)**: `ApiResult[ListDependentPhoneNumberResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListDependentPhoneNumberResponse` | `twilio_sdk/models/list_dependent_phone_number_response.py` |

