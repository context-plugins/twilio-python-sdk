<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401OutgoingCallerId — operations

Accessor: `client.api20100401_outgoing_caller_id` · Source: `twilio/apis/api20100401_outgoing_caller_id.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.api20100401_outgoing_caller_id.delete_outgoing_caller_id

- **Route**: `DELETE /2010-04-01/Accounts/{AccountSid}/OutgoingCallerIds/{Sid}.json`
- **Server**: `default`
- **Signature**: `def delete_outgoing_caller_id(account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.api20100401_outgoing_caller_id.fetch_outgoing_caller_id

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/OutgoingCallerIds/{Sid}.json`
- **Server**: `default`
- **Signature**: `def fetch_outgoing_caller_id(account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ApiV2010AccountOutgoingCallerId`
- **Returns (raw)**: `ApiResult[ApiV2010AccountOutgoingCallerId, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountOutgoingCallerId` | `twilio/models/api_v2010_account_outgoing_caller_id.py` |

### client.api20100401_outgoing_caller_id.list_outgoing_caller_id

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/OutgoingCallerIds.json`
- **Server**: `default`
- **Signature**: `def list_outgoing_caller_id(account_sid: str, *, phone_number: str | None = None, friendly_name: str | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`
- **Params**: `account_sid` — path `AccountSid` · `phone_number` — query `PhoneNumber` · `friendly_name` — query `FriendlyName` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListOutgoingCallerIdResponse`
- **Returns (raw)**: `ApiResult[ListOutgoingCallerIdResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListOutgoingCallerIdResponse` | `twilio/models/list_outgoing_caller_id_response.py` |

### client.api20100401_outgoing_caller_id.update_outgoing_caller_id

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/OutgoingCallerIds/{Sid}.json`
- **Server**: `default`
- **Signature**: `def update_outgoing_caller_id(account_sid: str, sid: str, *, friendly_name: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid` · `friendly_name` — form field `FriendlyName`
- **Returns (parsed)**: `ApiV2010AccountOutgoingCallerId`
- **Returns (raw)**: `ApiResult[ApiV2010AccountOutgoingCallerId, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountOutgoingCallerId` | `twilio/models/api_v2010_account_outgoing_caller_id.py` |

