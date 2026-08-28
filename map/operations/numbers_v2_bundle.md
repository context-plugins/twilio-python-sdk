<!-- Generated file — do not edit; regenerated with the SDK. -->

# NumbersV2Bundle — operations

Accessor: `client.numbers_v2_bundle` · Source: `twilio/apis/numbers_v2_bundle.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.numbers_v2_bundle.create_bundle

- **Route**: `POST /v2/RegulatoryCompliance/Bundles`
- **Server**: `default5`
- **Signature**: `def create_bundle(friendly_name: str, email: str, *, status_callback: str | None = None, regulation_sid: str | None = None, iso_country: str | None = None, end_user_type: BundleEnumEndUserTypeOrStr | None = None, number_type: str | None = None, is_test: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `friendly_name`, `email`
- **Params**: `friendly_name` — form field `FriendlyName` · `email` — form field `Email` · `status_callback` — form field `StatusCallback` · `regulation_sid` — form field `RegulationSid` · `iso_country` — form field `IsoCountry` · `end_user_type` — form field `EndUserType` · `number_type` — form field `NumberType` · `is_test` — form field `IsTest`
- **Returns (parsed)**: `NumbersV2RegulatoryComplianceBundle`
- **Returns (raw)**: `ApiResult[NumbersV2RegulatoryComplianceBundle, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BundleEnumEndUserTypeOrStr` | `twilio/models/enums/bundle_enum_end_user_type.py` |
| `NumbersV2RegulatoryComplianceBundle` | `twilio/models/numbers_v2_regulatory_compliance_bundle.py` |

### client.numbers_v2_bundle.delete_bundle

- **Route**: `DELETE /v2/RegulatoryCompliance/Bundles/{Sid}`
- **Server**: `default5`
- **Signature**: `def delete_bundle(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.numbers_v2_bundle.fetch_bundle

- **Route**: `GET /v2/RegulatoryCompliance/Bundles/{Sid}`
- **Server**: `default5`
- **Signature**: `def fetch_bundle(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `NumbersV2RegulatoryComplianceBundle`
- **Returns (raw)**: `ApiResult[NumbersV2RegulatoryComplianceBundle, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NumbersV2RegulatoryComplianceBundle` | `twilio/models/numbers_v2_regulatory_compliance_bundle.py` |

### client.numbers_v2_bundle.list_bundle

- **Route**: `GET /v2/RegulatoryCompliance/Bundles`
- **Server**: `default5`
- **Signature**: `def list_bundle(*, status: BundleEnumStatusOrStr | None = None, bundle_sids: str | None = None, friendly_name: str | None = None, regulation_sid: str | None = None, iso_country: str | None = None, number_type: str | None = None, end_user_type: BundleEnumEndUserTypeOrStr | None = None, has_valid_until_date: bool | None = None, sort_by: BundleEnumSortByOrStr | None = None, sort_direction: BundleEnumSortDirectionOrStr | None = None, valid_until_date: RFC3339DateTime | None = None, valid_until_date_query: RFC3339DateTime | None = None, valid_until_date_query_query: RFC3339DateTime | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `status` — query `Status` · `bundle_sids` — query `BundleSids` · `friendly_name` — query `FriendlyName` · `regulation_sid` — query `RegulationSid` · `iso_country` — query `IsoCountry` · `number_type` — query `NumberType` · `end_user_type` — query `EndUserType` · `has_valid_until_date` — query `HasValidUntilDate` · `sort_by` — query `SortBy` · `sort_direction` — query `SortDirection` · `valid_until_date` — query `ValidUntilDate` · `valid_until_date_query` — query `ValidUntilDate<` · `valid_until_date_query_query` — query `ValidUntilDate>` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListBundleResponse`
- **Returns (raw)**: `ApiResult[ListBundleResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BundleEnumStatusOrStr` | `twilio/models/enums/bundle_enum_status.py` |
| `BundleEnumEndUserTypeOrStr` | `twilio/models/enums/bundle_enum_end_user_type.py` |
| `BundleEnumSortByOrStr` | `twilio/models/enums/bundle_enum_sort_by.py` |
| `BundleEnumSortDirectionOrStr` | `twilio/models/enums/bundle_enum_sort_direction.py` |
| `ListBundleResponse` | `twilio/models/list_bundle_response.py` |

### client.numbers_v2_bundle.update_bundle

- **Route**: `POST /v2/RegulatoryCompliance/Bundles/{Sid}`
- **Server**: `default5`
- **Signature**: `def update_bundle(sid: str, *, status: BundleEnumStatusOrStr | None = None, status_callback: str | None = None, friendly_name: str | None = None, email: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid` · `status` — form field `Status` · `status_callback` — form field `StatusCallback` · `friendly_name` — form field `FriendlyName` · `email` — form field `Email`
- **Returns (parsed)**: `NumbersV2RegulatoryComplianceBundle`
- **Returns (raw)**: `ApiResult[NumbersV2RegulatoryComplianceBundle, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BundleEnumStatusOrStr` | `twilio/models/enums/bundle_enum_status.py` |
| `NumbersV2RegulatoryComplianceBundle` | `twilio/models/numbers_v2_regulatory_compliance_bundle.py` |

