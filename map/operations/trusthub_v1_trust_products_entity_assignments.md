<!-- Generated file — do not edit; regenerated with the SDK. -->

# TrusthubV1TrustProductsEntityAssignments — operations

Accessor: `client.trusthub_v1_trust_products_entity_assignments` · Source: `twilio/apis/trusthub_v1_trust_products_entity_assignments.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.trusthub_v1_trust_products_entity_assignments.create_trust_product_entity_assignment

- **Route**: `POST /v1/TrustProducts/{TrustProductSid}/EntityAssignments`
- **Server**: `default9`
- **Signature**: `def create_trust_product_entity_assignment(trust_product_sid: str, object_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `trust_product_sid`, `object_sid`
- **Params**: `trust_product_sid` — path `TrustProductSid` · `object_sid` — form field `ObjectSid`
- **Returns (parsed)**: `TrusthubV1TrustProductTrustProductEntityAssignment`
- **Returns (raw)**: `ApiResult[TrusthubV1TrustProductTrustProductEntityAssignment, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TrusthubV1TrustProductTrustProductEntityAssignment` | `twilio/models/trusthub_v1_trust_product_trust_product_entity_assignment.py` |

### client.trusthub_v1_trust_products_entity_assignments.delete_trust_product_entity_assignment

- **Route**: `DELETE /v1/TrustProducts/{TrustProductSid}/EntityAssignments/{Sid}`
- **Server**: `default9`
- **Signature**: `def delete_trust_product_entity_assignment(trust_product_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `trust_product_sid`, `sid`
- **Params**: `trust_product_sid` — path `TrustProductSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.trusthub_v1_trust_products_entity_assignments.fetch_trust_product_entity_assignment

- **Route**: `GET /v1/TrustProducts/{TrustProductSid}/EntityAssignments/{Sid}`
- **Server**: `default9`
- **Signature**: `def fetch_trust_product_entity_assignment(trust_product_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `trust_product_sid`, `sid`
- **Params**: `trust_product_sid` — path `TrustProductSid` · `sid` — path `Sid`
- **Returns (parsed)**: `TrusthubV1TrustProductTrustProductEntityAssignment`
- **Returns (raw)**: `ApiResult[TrusthubV1TrustProductTrustProductEntityAssignment, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TrusthubV1TrustProductTrustProductEntityAssignment` | `twilio/models/trusthub_v1_trust_product_trust_product_entity_assignment.py` |

### client.trusthub_v1_trust_products_entity_assignments.list_trust_product_entity_assignment

- **Route**: `GET /v1/TrustProducts/{TrustProductSid}/EntityAssignments`
- **Server**: `default9`
- **Signature**: `def list_trust_product_entity_assignment(trust_product_sid: str, *, object_type: str | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `trust_product_sid`
- **Params**: `trust_product_sid` — path `TrustProductSid` · `object_type` — query `ObjectType` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListTrustProductEntityAssignmentResponse`
- **Returns (raw)**: `ApiResult[ListTrustProductEntityAssignmentResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListTrustProductEntityAssignmentResponse` | `twilio/models/list_trust_product_entity_assignment_response.py` |

