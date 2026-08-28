<!-- Generated file — do not edit; regenerated with the SDK. -->

# FlexV1ProvisioningStatusApi — operations

Accessor: `client.flex_v1_provisioning_status_api` · Source: `twilio/apis/flex_v1_provisioning_status_api.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.flex_v1_provisioning_status_api.fetch_provisioning_status

- **Route**: `GET /v1/account/provision/status`
- **Server**: `default13`
- **Signature**: `def fetch_provisioning_status(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `FlexV1ProvisioningStatus`
- **Returns (raw)**: `ApiResult[FlexV1ProvisioningStatus, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1ProvisioningStatus` | `twilio/models/flex_v1_provisioning_status.py` |

