<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401SipIpAddress — operations

Accessor: `client.api20100401_sip_ip_address` · Source: `twilio_sdk/apis/api20100401_sip_ip_address.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.api20100401_sip_ip_address.create_sip_ip_address

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{IpAccessControlListSid}/IpAddresses.json`
- **Auth**: `account_sid_auth_token`
- **Server**: `default`
- **Signature**: `def create_sip_ip_address(account_sid: str, ip_access_control_list_sid: str, friendly_name: str, ip_address: str, *, cidr_prefix_length: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `ip_access_control_list_sid`, `friendly_name`, `ip_address`
- **Params**: `account_sid` — path `AccountSid` · `ip_access_control_list_sid` — path `IpAccessControlListSid` · `friendly_name` — form field `FriendlyName` · `ip_address` — form field `IpAddress` · `cidr_prefix_length` — form field `CidrPrefixLength`
- **Returns (parsed)**: `ApiV2010AccountSipSipIpAccessControlListSipIpAddress`
- **Returns (raw)**: `ApiResult[ApiV2010AccountSipSipIpAccessControlListSipIpAddress, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountSipSipIpAccessControlListSipIpAddress` | `twilio_sdk/models/api_v2010_account_sip_sip_ip_access_control_list_sip_ip_address.py` |

### client.api20100401_sip_ip_address.delete_sip_ip_address

- **Route**: `DELETE /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{IpAccessControlListSid}/IpAddresses/{Sid}.json`
- **Auth**: `account_sid_auth_token`
- **Server**: `default`
- **Signature**: `def delete_sip_ip_address(account_sid: str, ip_access_control_list_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `ip_access_control_list_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `ip_access_control_list_sid` — path `IpAccessControlListSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.api20100401_sip_ip_address.fetch_sip_ip_address

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{IpAccessControlListSid}/IpAddresses/{Sid}.json`
- **Auth**: `account_sid_auth_token`
- **Server**: `default`
- **Signature**: `def fetch_sip_ip_address(account_sid: str, ip_access_control_list_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `ip_access_control_list_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `ip_access_control_list_sid` — path `IpAccessControlListSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ApiV2010AccountSipSipIpAccessControlListSipIpAddress`
- **Returns (raw)**: `ApiResult[ApiV2010AccountSipSipIpAccessControlListSipIpAddress, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountSipSipIpAccessControlListSipIpAddress` | `twilio_sdk/models/api_v2010_account_sip_sip_ip_access_control_list_sip_ip_address.py` |

### client.api20100401_sip_ip_address.list_sip_ip_address

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{IpAccessControlListSid}/IpAddresses.json`
- **Auth**: `account_sid_auth_token`
- **Server**: `default`
- **Signature**: `def list_sip_ip_address(account_sid: str, ip_access_control_list_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `ip_access_control_list_sid`
- **Params**: `account_sid` — path `AccountSid` · `ip_access_control_list_sid` — path `IpAccessControlListSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListSipIpAddressResponse`
- **Returns (raw)**: `ApiResult[ListSipIpAddressResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListSipIpAddressResponse` | `twilio_sdk/models/list_sip_ip_address_response.py` |

### client.api20100401_sip_ip_address.update_sip_ip_address

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{IpAccessControlListSid}/IpAddresses/{Sid}.json`
- **Auth**: `account_sid_auth_token`
- **Server**: `default`
- **Signature**: `def update_sip_ip_address(account_sid: str, ip_access_control_list_sid: str, sid: str, *, ip_address: str | None = None, friendly_name: str | None = None, cidr_prefix_length: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `ip_access_control_list_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `ip_access_control_list_sid` — path `IpAccessControlListSid` · `sid` — path `Sid` · `ip_address` — form field `IpAddress` · `friendly_name` — form field `FriendlyName` · `cidr_prefix_length` — form field `CidrPrefixLength`
- **Returns (parsed)**: `ApiV2010AccountSipSipIpAccessControlListSipIpAddress`
- **Returns (raw)**: `ApiResult[ApiV2010AccountSipSipIpAccessControlListSipIpAddress, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountSipSipIpAccessControlListSipIpAddress` | `twilio_sdk/models/api_v2010_account_sip_sip_ip_access_control_list_sip_ip_address.py` |

