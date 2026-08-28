<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401AssignedAddOn — operations

Accessor: `client.api20100401_assigned_add_on` · Source: `twilio/apis/api20100401_assigned_add_on.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.api20100401_assigned_add_on.create_incoming_phone_number_assigned_add_on

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns.json`
- **Server**: `default`
- **Signature**: `def create_incoming_phone_number_assigned_add_on(account_sid: str, resource_sid: str, installed_add_on_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `resource_sid`, `installed_add_on_sid`
- **Params**: `account_sid` — path `AccountSid` · `resource_sid` — path `ResourceSid` · `installed_add_on_sid` — form field `InstalledAddOnSid`
- **Returns (parsed)**: `ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn`
- **Returns (raw)**: `ApiResult[ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn` | `twilio/models/api_v2010_account_incoming_phone_number_incoming_phone_number_assigned_add_on.py` |

### client.api20100401_assigned_add_on.delete_incoming_phone_number_assigned_add_on

- **Route**: `DELETE /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns/{Sid}.json`
- **Server**: `default`
- **Signature**: `def delete_incoming_phone_number_assigned_add_on(account_sid: str, resource_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `resource_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `resource_sid` — path `ResourceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.api20100401_assigned_add_on.fetch_incoming_phone_number_assigned_add_on

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns/{Sid}.json`
- **Server**: `default`
- **Signature**: `def fetch_incoming_phone_number_assigned_add_on(account_sid: str, resource_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `resource_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `resource_sid` — path `ResourceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn`
- **Returns (raw)**: `ApiResult[ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn` | `twilio/models/api_v2010_account_incoming_phone_number_incoming_phone_number_assigned_add_on.py` |

### client.api20100401_assigned_add_on.list_incoming_phone_number_assigned_add_on

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns.json`
- **Server**: `default`
- **Signature**: `def list_incoming_phone_number_assigned_add_on(account_sid: str, resource_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `resource_sid`
- **Params**: `account_sid` — path `AccountSid` · `resource_sid` — path `ResourceSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListIncomingPhoneNumberAssignedAddOnResponse`
- **Returns (raw)**: `ApiResult[ListIncomingPhoneNumberAssignedAddOnResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListIncomingPhoneNumberAssignedAddOnResponse` | `twilio/models/list_incoming_phone_number_assigned_add_on_response.py` |

