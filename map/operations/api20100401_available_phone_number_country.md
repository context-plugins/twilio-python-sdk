<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401AvailablePhoneNumberCountry — operations

Accessor: `client.api20100401_available_phone_number_country` · Source: `twilio_sdk/apis/api20100401_available_phone_number_country.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.api20100401_available_phone_number_country.fetch_available_phone_number_country

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers/{CountryCode}.json`
- **Server**: `default`
- **Signature**: `def fetch_available_phone_number_country(account_sid: str, country_code: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `country_code`
- **Params**: `account_sid` — path `AccountSid` · `country_code` — path `CountryCode`
- **Returns (parsed)**: `ApiV2010AccountAvailablePhoneNumberCountry`
- **Returns (raw)**: `ApiResult[ApiV2010AccountAvailablePhoneNumberCountry, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountAvailablePhoneNumberCountry` | `twilio_sdk/models/api_v2010_account_available_phone_number_country.py` |

### client.api20100401_available_phone_number_country.list_available_phone_number_country

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers.json`
- **Server**: `default`
- **Signature**: `def list_available_phone_number_country(account_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`
- **Params**: `account_sid` — path `AccountSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListAvailablePhoneNumberCountryResponse`
- **Returns (raw)**: `ApiResult[ListAvailablePhoneNumberCountryResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListAvailablePhoneNumberCountryResponse` | `twilio_sdk/models/list_available_phone_number_country_response.py` |

