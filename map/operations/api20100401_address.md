<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401Address — operations

Accessor: `client.api20100401_address` · Source: `twilio_sdk/apis/api20100401_address.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.api20100401_address.create_address

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/Addresses.json`
- **Server**: `default`
- **Signature**: `def create_address(account_sid: str, customer_name: str, street: str, city: str, region: str, postal_code: str, iso_country: str, *, friendly_name: str | None = None, emergency_enabled: bool | None = None, auto_correct_address: bool | None = None, street_secondary: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `customer_name`, `street`, `city`, `region`, `postal_code`, `iso_country`
- **Params**: `account_sid` — path `AccountSid` · `customer_name` — form field `CustomerName` · `street` — form field `Street` · `city` — form field `City` · `region` — form field `Region` · `postal_code` — form field `PostalCode` · `iso_country` — form field `IsoCountry` · `friendly_name` — form field `FriendlyName` · `emergency_enabled` — form field `EmergencyEnabled` · `auto_correct_address` — form field `AutoCorrectAddress` · `street_secondary` — form field `StreetSecondary`
- **Returns (parsed)**: `ApiV2010AccountAddress`
- **Returns (raw)**: `ApiResult[ApiV2010AccountAddress, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountAddress` | `twilio_sdk/models/api_v2010_account_address.py` |

### client.api20100401_address.delete_address

- **Route**: `DELETE /2010-04-01/Accounts/{AccountSid}/Addresses/{Sid}.json`
- **Server**: `default`
- **Signature**: `def delete_address(account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.api20100401_address.fetch_address

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/Addresses/{Sid}.json`
- **Server**: `default`
- **Signature**: `def fetch_address(account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ApiV2010AccountAddress`
- **Returns (raw)**: `ApiResult[ApiV2010AccountAddress, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountAddress` | `twilio_sdk/models/api_v2010_account_address.py` |

### client.api20100401_address.list_address

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/Addresses.json`
- **Server**: `default`
- **Signature**: `def list_address(account_sid: str, *, customer_name: str | None = None, friendly_name: str | None = None, emergency_enabled: bool | None = None, iso_country: str | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`
- **Params**: `account_sid` — path `AccountSid` · `customer_name` — query `CustomerName` · `friendly_name` — query `FriendlyName` · `emergency_enabled` — query `EmergencyEnabled` · `iso_country` — query `IsoCountry` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListAddressResponse`
- **Returns (raw)**: `ApiResult[ListAddressResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListAddressResponse` | `twilio_sdk/models/list_address_response.py` |

### client.api20100401_address.update_address

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/Addresses/{Sid}.json`
- **Server**: `default`
- **Signature**: `def update_address(account_sid: str, sid: str, *, friendly_name: str | None = None, customer_name: str | None = None, street: str | None = None, city: str | None = None, region: str | None = None, postal_code: str | None = None, emergency_enabled: bool | None = None, auto_correct_address: bool | None = None, street_secondary: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid` · `friendly_name` — form field `FriendlyName` · `customer_name` — form field `CustomerName` · `street` — form field `Street` · `city` — form field `City` · `region` — form field `Region` · `postal_code` — form field `PostalCode` · `emergency_enabled` — form field `EmergencyEnabled` · `auto_correct_address` — form field `AutoCorrectAddress` · `street_secondary` — form field `StreetSecondary`
- **Returns (parsed)**: `ApiV2010AccountAddress`
- **Returns (raw)**: `ApiResult[ApiV2010AccountAddress, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountAddress` | `twilio_sdk/models/api_v2010_account_address.py` |

