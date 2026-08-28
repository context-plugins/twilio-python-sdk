<!-- Generated file — do not edit; regenerated with the SDK. -->

# TrusthubV1TrustProductsChannelEndpointAssignment — operations

Accessor: `client.trusthub_v1_trust_products_channel_endpoint_assignment` · Source: `twilio/apis/trusthub_v1_trust_products_channel_endpoint_assignment.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.trusthub_v1_trust_products_channel_endpoint_assignment.create_trust_product_channel_endpoint_assignment

- **Route**: `POST /v1/TrustProducts/{TrustProductSid}/ChannelEndpointAssignments`
- **Server**: `default9`
- **Signature**: `def create_trust_product_channel_endpoint_assignment(trust_product_sid: str, channel_endpoint_type: str, channel_endpoint_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `trust_product_sid`, `channel_endpoint_type`, `channel_endpoint_sid`
- **Params**: `trust_product_sid` — path `TrustProductSid` · `channel_endpoint_type` — form field `ChannelEndpointType` · `channel_endpoint_sid` — form field `ChannelEndpointSid`
- **Returns (parsed)**: `TrusthubV1TrustProductTrustProductChannelEndpointAssignment`
- **Returns (raw)**: `ApiResult[TrusthubV1TrustProductTrustProductChannelEndpointAssignment, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TrusthubV1TrustProductTrustProductChannelEndpointAssignment` | `twilio/models/trusthub_v1_trust_product_trust_product_channel_endpoint_assignment.py` |

### client.trusthub_v1_trust_products_channel_endpoint_assignment.delete_trust_product_channel_endpoint_assignment

- **Route**: `DELETE /v1/TrustProducts/{TrustProductSid}/ChannelEndpointAssignments/{Sid}`
- **Server**: `default9`
- **Signature**: `def delete_trust_product_channel_endpoint_assignment(trust_product_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `trust_product_sid`, `sid`
- **Params**: `trust_product_sid` — path `TrustProductSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.trusthub_v1_trust_products_channel_endpoint_assignment.fetch_trust_product_channel_endpoint_assignment

- **Route**: `GET /v1/TrustProducts/{TrustProductSid}/ChannelEndpointAssignments/{Sid}`
- **Server**: `default9`
- **Signature**: `def fetch_trust_product_channel_endpoint_assignment(trust_product_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `trust_product_sid`, `sid`
- **Params**: `trust_product_sid` — path `TrustProductSid` · `sid` — path `Sid`
- **Returns (parsed)**: `TrusthubV1TrustProductTrustProductChannelEndpointAssignment`
- **Returns (raw)**: `ApiResult[TrusthubV1TrustProductTrustProductChannelEndpointAssignment, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TrusthubV1TrustProductTrustProductChannelEndpointAssignment` | `twilio/models/trusthub_v1_trust_product_trust_product_channel_endpoint_assignment.py` |

### client.trusthub_v1_trust_products_channel_endpoint_assignment.list_trust_product_channel_endpoint_assignment

- **Route**: `GET /v1/TrustProducts/{TrustProductSid}/ChannelEndpointAssignments`
- **Server**: `default9`
- **Signature**: `def list_trust_product_channel_endpoint_assignment(trust_product_sid: str, *, channel_endpoint_sid: str | None = None, channel_endpoint_sids: str | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `trust_product_sid`
- **Params**: `trust_product_sid` — path `TrustProductSid` · `channel_endpoint_sid` — query `ChannelEndpointSid` · `channel_endpoint_sids` — query `ChannelEndpointSids` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListTrustProductChannelEndpointAssignmentResponse`
- **Returns (raw)**: `ApiResult[ListTrustProductChannelEndpointAssignmentResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListTrustProductChannelEndpointAssignmentResponse` | `twilio/models/list_trust_product_channel_endpoint_assignment_response.py` |

