<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401AssignedAddOnExtension — operations

Accessor: `client.api20100401_assigned_add_on_extension` · Source: `twilio/apis/api20100401_assigned_add_on_extension.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.api20100401_assigned_add_on_extension.fetch_incoming_phone_number_assigned_add_on_extension

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns/{AssignedAddOnSid}/Extensions/{Sid}.json`
- **Server**: `default`
- **Signature**: `def fetch_incoming_phone_number_assigned_add_on_extension(account_sid: str, resource_sid: str, assigned_add_on_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `resource_sid`, `assigned_add_on_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `resource_sid` — path `ResourceSid` · `assigned_add_on_sid` — path `AssignedAddOnSid` · `sid` — path `Sid`
- **Returns (parsed)**: `IncomingPhoneNumberAssignedAddOnExtension`
- **Returns (raw)**: `ApiResult[IncomingPhoneNumberAssignedAddOnExtension, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IncomingPhoneNumberAssignedAddOnExtension` | `twilio/models/incoming_phone_number_assigned_add_on_extension.py` |

### client.api20100401_assigned_add_on_extension.list_incoming_phone_number_assigned_add_on_extension

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns/{AssignedAddOnSid}/Extensions.json`
- **Server**: `default`
- **Signature**: `def list_incoming_phone_number_assigned_add_on_extension(account_sid: str, resource_sid: str, assigned_add_on_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `resource_sid`, `assigned_add_on_sid`
- **Params**: `account_sid` — path `AccountSid` · `resource_sid` — path `ResourceSid` · `assigned_add_on_sid` — path `AssignedAddOnSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListIncomingPhoneNumberAssignedAddOnExtensionResponse`
- **Returns (raw)**: `ApiResult[ListIncomingPhoneNumberAssignedAddOnExtensionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListIncomingPhoneNumberAssignedAddOnExtensionResponse` | `twilio/models/list_incoming_phone_number_assigned_add_on_extension_response.py` |

