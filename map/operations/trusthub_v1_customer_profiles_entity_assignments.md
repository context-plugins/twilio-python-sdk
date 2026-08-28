<!-- Generated file — do not edit; regenerated with the SDK. -->

# TrusthubV1CustomerProfilesEntityAssignments — operations

Accessor: `client.trusthub_v1_customer_profiles_entity_assignments` · Source: `twilio_sdk/apis/trusthub_v1_customer_profiles_entity_assignments.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.trusthub_v1_customer_profiles_entity_assignments.create_customer_profile_entity_assignment

- **Route**: `POST /v1/CustomerProfiles/{CustomerProfileSid}/EntityAssignments`
- **Server**: `default9`
- **Signature**: `def create_customer_profile_entity_assignment(customer_profile_sid: str, object_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `customer_profile_sid`, `object_sid`
- **Params**: `customer_profile_sid` — path `CustomerProfileSid` · `object_sid` — form field `ObjectSid`
- **Returns (parsed)**: `TrusthubV1CustomerProfileCustomerProfileEntityAssignment`
- **Returns (raw)**: `ApiResult[TrusthubV1CustomerProfileCustomerProfileEntityAssignment, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TrusthubV1CustomerProfileCustomerProfileEntityAssignment` | `twilio_sdk/models/trusthub_v1_customer_profile_customer_profile_entity_assignment.py` |

### client.trusthub_v1_customer_profiles_entity_assignments.delete_customer_profile_entity_assignment

- **Route**: `DELETE /v1/CustomerProfiles/{CustomerProfileSid}/EntityAssignments/{Sid}`
- **Server**: `default9`
- **Signature**: `def delete_customer_profile_entity_assignment(customer_profile_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `customer_profile_sid`, `sid`
- **Params**: `customer_profile_sid` — path `CustomerProfileSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.trusthub_v1_customer_profiles_entity_assignments.fetch_customer_profile_entity_assignment

- **Route**: `GET /v1/CustomerProfiles/{CustomerProfileSid}/EntityAssignments/{Sid}`
- **Server**: `default9`
- **Signature**: `def fetch_customer_profile_entity_assignment(customer_profile_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `customer_profile_sid`, `sid`
- **Params**: `customer_profile_sid` — path `CustomerProfileSid` · `sid` — path `Sid`
- **Returns (parsed)**: `TrusthubV1CustomerProfileCustomerProfileEntityAssignment`
- **Returns (raw)**: `ApiResult[TrusthubV1CustomerProfileCustomerProfileEntityAssignment, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TrusthubV1CustomerProfileCustomerProfileEntityAssignment` | `twilio_sdk/models/trusthub_v1_customer_profile_customer_profile_entity_assignment.py` |

### client.trusthub_v1_customer_profiles_entity_assignments.list_customer_profile_entity_assignment

- **Route**: `GET /v1/CustomerProfiles/{CustomerProfileSid}/EntityAssignments`
- **Server**: `default9`
- **Signature**: `def list_customer_profile_entity_assignment(customer_profile_sid: str, *, object_type: str | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `customer_profile_sid`
- **Params**: `customer_profile_sid` — path `CustomerProfileSid` · `object_type` — query `ObjectType` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListCustomerProfileEntityAssignmentResponse`
- **Returns (raw)**: `ApiResult[ListCustomerProfileEntityAssignmentResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListCustomerProfileEntityAssignmentResponse` | `twilio_sdk/models/list_customer_profile_entity_assignment_response.py` |

