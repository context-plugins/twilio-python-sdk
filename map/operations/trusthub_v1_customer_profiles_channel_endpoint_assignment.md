<!-- Generated file — do not edit; regenerated with the SDK. -->

# TrusthubV1CustomerProfilesChannelEndpointAssignment — operations

Accessor: `client.trusthub_v1_customer_profiles_channel_endpoint_assignment` · Source: `twilio_sdk/apis/trusthub_v1_customer_profiles_channel_endpoint_assignment.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.trusthub_v1_customer_profiles_channel_endpoint_assignment.create_customer_profile_channel_endpoint_assignment

- **Route**: `POST /v1/CustomerProfiles/{CustomerProfileSid}/ChannelEndpointAssignments`
- **Server**: `default9`
- **Signature**: `def create_customer_profile_channel_endpoint_assignment(customer_profile_sid: str, channel_endpoint_type: str, channel_endpoint_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `customer_profile_sid`, `channel_endpoint_type`, `channel_endpoint_sid`
- **Params**: `customer_profile_sid` — path `CustomerProfileSid` · `channel_endpoint_type` — form field `ChannelEndpointType` · `channel_endpoint_sid` — form field `ChannelEndpointSid`
- **Returns (parsed)**: `TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment`
- **Returns (raw)**: `ApiResult[TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment` | `twilio_sdk/models/trusthub_v1_customer_profile_customer_profile_channel_endpoint_assignment.py` |

### client.trusthub_v1_customer_profiles_channel_endpoint_assignment.delete_customer_profile_channel_endpoint_assignment

- **Route**: `DELETE /v1/CustomerProfiles/{CustomerProfileSid}/ChannelEndpointAssignments/{Sid}`
- **Server**: `default9`
- **Signature**: `def delete_customer_profile_channel_endpoint_assignment(customer_profile_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `customer_profile_sid`, `sid`
- **Params**: `customer_profile_sid` — path `CustomerProfileSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.trusthub_v1_customer_profiles_channel_endpoint_assignment.fetch_customer_profile_channel_endpoint_assignment

- **Route**: `GET /v1/CustomerProfiles/{CustomerProfileSid}/ChannelEndpointAssignments/{Sid}`
- **Server**: `default9`
- **Signature**: `def fetch_customer_profile_channel_endpoint_assignment(customer_profile_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `customer_profile_sid`, `sid`
- **Params**: `customer_profile_sid` — path `CustomerProfileSid` · `sid` — path `Sid`
- **Returns (parsed)**: `TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment`
- **Returns (raw)**: `ApiResult[TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment` | `twilio_sdk/models/trusthub_v1_customer_profile_customer_profile_channel_endpoint_assignment.py` |

### client.trusthub_v1_customer_profiles_channel_endpoint_assignment.list_customer_profile_channel_endpoint_assignment

- **Route**: `GET /v1/CustomerProfiles/{CustomerProfileSid}/ChannelEndpointAssignments`
- **Server**: `default9`
- **Signature**: `def list_customer_profile_channel_endpoint_assignment(customer_profile_sid: str, *, channel_endpoint_sid: str | None = None, channel_endpoint_sids: str | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `customer_profile_sid`
- **Params**: `customer_profile_sid` — path `CustomerProfileSid` · `channel_endpoint_sid` — query `ChannelEndpointSid` · `channel_endpoint_sids` — query `ChannelEndpointSids` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListCustomerProfileChannelEndpointAssignmentResponse`
- **Returns (raw)**: `ApiResult[ListCustomerProfileChannelEndpointAssignmentResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListCustomerProfileChannelEndpointAssignmentResponse` | `twilio_sdk/models/list_customer_profile_channel_endpoint_assignment_response.py` |

