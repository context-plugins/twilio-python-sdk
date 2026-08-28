<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401IpAccessControlList — operations

Accessor: `client.api20100401_ip_access_control_list` · Source: `twilio/apis/api20100401_ip_access_control_list.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.api20100401_ip_access_control_list.create_sip_ip_access_control_list

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists.json`
- **Server**: `default`
- **Signature**: `def create_sip_ip_access_control_list(account_sid: str, friendly_name: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `friendly_name`
- **Params**: `account_sid` — path `AccountSid` · `friendly_name` — form field `FriendlyName`
- **Returns (parsed)**: `ApiV2010AccountSipSipIpAccessControlList`
- **Returns (raw)**: `ApiResult[ApiV2010AccountSipSipIpAccessControlList, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountSipSipIpAccessControlList` | `twilio/models/api_v2010_account_sip_sip_ip_access_control_list.py` |

### client.api20100401_ip_access_control_list.delete_sip_ip_access_control_list

- **Route**: `DELETE /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{Sid}.json`
- **Server**: `default`
- **Signature**: `def delete_sip_ip_access_control_list(account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.api20100401_ip_access_control_list.fetch_sip_ip_access_control_list

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{Sid}.json`
- **Server**: `default`
- **Signature**: `def fetch_sip_ip_access_control_list(account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ApiV2010AccountSipSipIpAccessControlList`
- **Returns (raw)**: `ApiResult[ApiV2010AccountSipSipIpAccessControlList, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountSipSipIpAccessControlList` | `twilio/models/api_v2010_account_sip_sip_ip_access_control_list.py` |

### client.api20100401_ip_access_control_list.list_sip_ip_access_control_list

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists.json`
- **Server**: `default`
- **Signature**: `def list_sip_ip_access_control_list(account_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`
- **Params**: `account_sid` — path `AccountSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListSipIpAccessControlListResponse`
- **Returns (raw)**: `ApiResult[ListSipIpAccessControlListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListSipIpAccessControlListResponse` | `twilio/models/list_sip_ip_access_control_list_response.py` |

### client.api20100401_ip_access_control_list.update_sip_ip_access_control_list

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{Sid}.json`
- **Server**: `default`
- **Signature**: `def update_sip_ip_access_control_list(account_sid: str, sid: str, friendly_name: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`, `friendly_name`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid` · `friendly_name` — form field `FriendlyName`
- **Returns (parsed)**: `ApiV2010AccountSipSipIpAccessControlList`
- **Returns (raw)**: `ApiResult[ApiV2010AccountSipSipIpAccessControlList, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountSipSipIpAccessControlList` | `twilio/models/api_v2010_account_sip_sip_ip_access_control_list.py` |

