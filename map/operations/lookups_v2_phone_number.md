<!-- Generated file — do not edit; regenerated with the SDK. -->

# LookupsV2PhoneNumber — operations

Accessor: `client.lookups_v2_phone_number` · Source: `twilio_sdk/apis/lookups_v2_phone_number.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.lookups_v2_phone_number.fetch_phone_number3

- **Route**: `GET /v2/PhoneNumbers/{PhoneNumber}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default4`
- **Signature**: `def fetch_phone_number3(phone_number: str, *, fields: str | None = None, country_code: str | None = None, first_name: str | None = None, last_name: str | None = None, address_line1: str | None = None, address_line2: str | None = None, city: str | None = None, state: str | None = None, postal_code: str | None = None, address_country_code: str | None = None, national_id: str | None = None, date_of_birth: str | None = None, last_verified_date: str | None = None, verification_sid: str | None = None, partner_sub_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `phone_number`
- **Params**: `phone_number` — path `PhoneNumber` · `fields` — query `Fields` · `country_code` — query `CountryCode` · `first_name` — query `FirstName` · `last_name` — query `LastName` · `address_line1` — query `AddressLine1` · `address_line2` — query `AddressLine2` · `city` — query `City` · `state` — query `State` · `postal_code` — query `PostalCode` · `address_country_code` — query `AddressCountryCode` · `national_id` — query `NationalId` · `date_of_birth` — query `DateOfBirth` · `last_verified_date` — query `LastVerifiedDate` · `verification_sid` — query `VerificationSid` · `partner_sub_id` — query `PartnerSubId`
- **Returns (parsed)**: `LookupResponse`
- **Returns (raw)**: `ApiResult[LookupResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `LookupResponse` | `twilio_sdk/models/lookup_response.py` |

