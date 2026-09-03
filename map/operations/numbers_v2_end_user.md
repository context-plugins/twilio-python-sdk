<!-- Generated file — do not edit; regenerated with the SDK. -->

# NumbersV2EndUser — operations

Accessor: `client.numbers_v2_end_user` · Source: `twilio_sdk/apis/numbers_v2_end_user.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.numbers_v2_end_user.create_end_user

- **Route**: `POST /v2/RegulatoryCompliance/EndUsers`
- **Auth**: `account_sid_auth_token`
- **Server**: `default5`
- **Signature**: `def create_end_user(friendly_name: str, type_: EndUserEnumTypeOrStr, *, attributes: Any | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `friendly_name`, `type_`
- **Params**: `friendly_name` — form field `FriendlyName` · `type_` — form field `Type` · `attributes` — form field `Attributes`
- **Returns (parsed)**: `NumbersV2RegulatoryComplianceEndUser`
- **Returns (raw)**: `ApiResult[NumbersV2RegulatoryComplianceEndUser, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EndUserEnumTypeOrStr` | `twilio_sdk/models/enums/end_user_enum_type.py` |
| `NumbersV2RegulatoryComplianceEndUser` | `twilio_sdk/models/numbers_v2_regulatory_compliance_end_user.py` |

### client.numbers_v2_end_user.delete_end_user

- **Route**: `DELETE /v2/RegulatoryCompliance/EndUsers/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default5`
- **Signature**: `def delete_end_user(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.numbers_v2_end_user.fetch_end_user

- **Route**: `GET /v2/RegulatoryCompliance/EndUsers/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default5`
- **Signature**: `def fetch_end_user(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `NumbersV2RegulatoryComplianceEndUser`
- **Returns (raw)**: `ApiResult[NumbersV2RegulatoryComplianceEndUser, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NumbersV2RegulatoryComplianceEndUser` | `twilio_sdk/models/numbers_v2_regulatory_compliance_end_user.py` |

### client.numbers_v2_end_user.list_end_user

- **Route**: `GET /v2/RegulatoryCompliance/EndUsers`
- **Auth**: `account_sid_auth_token`
- **Server**: `default5`
- **Signature**: `def list_end_user(*, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListEndUserResponse`
- **Returns (raw)**: `ApiResult[ListEndUserResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListEndUserResponse` | `twilio_sdk/models/list_end_user_response.py` |

### client.numbers_v2_end_user.update_end_user

- **Route**: `POST /v2/RegulatoryCompliance/EndUsers/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default5`
- **Signature**: `def update_end_user(sid: str, *, friendly_name: str | None = None, attributes: Any | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid` · `friendly_name` — form field `FriendlyName` · `attributes` — form field `Attributes`
- **Returns (parsed)**: `NumbersV2RegulatoryComplianceEndUser`
- **Returns (raw)**: `ApiResult[NumbersV2RegulatoryComplianceEndUser, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NumbersV2RegulatoryComplianceEndUser` | `twilio_sdk/models/numbers_v2_regulatory_compliance_end_user.py` |

