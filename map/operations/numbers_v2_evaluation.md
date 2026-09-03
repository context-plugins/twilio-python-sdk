<!-- Generated file — do not edit; regenerated with the SDK. -->

# NumbersV2Evaluation — operations

Accessor: `client.numbers_v2_evaluation` · Source: `twilio_sdk/apis/numbers_v2_evaluation.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.numbers_v2_evaluation.create_evaluation

- **Route**: `POST /v2/RegulatoryCompliance/Bundles/{BundleSid}/Evaluations`
- **Auth**: `account_sid_auth_token`
- **Server**: `default5`
- **Signature**: `def create_evaluation(bundle_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `bundle_sid`
- **Params**: `bundle_sid` — path `BundleSid`
- **Returns (parsed)**: `NumbersV2RegulatoryComplianceBundleEvaluation`
- **Returns (raw)**: `ApiResult[NumbersV2RegulatoryComplianceBundleEvaluation, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NumbersV2RegulatoryComplianceBundleEvaluation` | `twilio_sdk/models/numbers_v2_regulatory_compliance_bundle_evaluation.py` |

### client.numbers_v2_evaluation.fetch_evaluation

- **Route**: `GET /v2/RegulatoryCompliance/Bundles/{BundleSid}/Evaluations/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default5`
- **Signature**: `def fetch_evaluation(bundle_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `bundle_sid`, `sid`
- **Params**: `bundle_sid` — path `BundleSid` · `sid` — path `Sid`
- **Returns (parsed)**: `NumbersV2RegulatoryComplianceBundleEvaluation`
- **Returns (raw)**: `ApiResult[NumbersV2RegulatoryComplianceBundleEvaluation, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NumbersV2RegulatoryComplianceBundleEvaluation` | `twilio_sdk/models/numbers_v2_regulatory_compliance_bundle_evaluation.py` |

### client.numbers_v2_evaluation.list_evaluation

- **Route**: `GET /v2/RegulatoryCompliance/Bundles/{BundleSid}/Evaluations`
- **Auth**: `account_sid_auth_token`
- **Server**: `default5`
- **Signature**: `def list_evaluation(bundle_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `bundle_sid`
- **Params**: `bundle_sid` — path `BundleSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListEvaluationResponse`
- **Returns (raw)**: `ApiResult[ListEvaluationResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListEvaluationResponse` | `twilio_sdk/models/list_evaluation_response.py` |

