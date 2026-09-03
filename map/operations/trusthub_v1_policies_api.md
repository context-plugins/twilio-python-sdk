<!-- Generated file — do not edit; regenerated with the SDK. -->

# TrusthubV1PoliciesApi — operations

Accessor: `client.trusthub_v1_policies_api` · Source: `twilio_sdk/apis/trusthub_v1_policies_api.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.trusthub_v1_policies_api.fetch_policies

- **Route**: `GET /v1/Policies/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default9`
- **Signature**: `def fetch_policies(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `TrusthubV1Policies`
- **Returns (raw)**: `ApiResult[TrusthubV1Policies, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TrusthubV1Policies` | `twilio_sdk/models/trusthub_v1_policies.py` |

### client.trusthub_v1_policies_api.list_policies

- **Route**: `GET /v1/Policies`
- **Auth**: `account_sid_auth_token`
- **Server**: `default9`
- **Signature**: `def list_policies(*, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListPoliciesResponse`
- **Returns (raw)**: `ApiResult[ListPoliciesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListPoliciesResponse` | `twilio_sdk/models/list_policies_response.py` |

