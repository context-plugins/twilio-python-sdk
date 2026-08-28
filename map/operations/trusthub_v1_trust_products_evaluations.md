<!-- Generated file — do not edit; regenerated with the SDK. -->

# TrusthubV1TrustProductsEvaluations — operations

Accessor: `client.trusthub_v1_trust_products_evaluations` · Source: `twilio_sdk/apis/trusthub_v1_trust_products_evaluations.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.trusthub_v1_trust_products_evaluations.create_trust_product_evaluation

- **Route**: `POST /v1/TrustProducts/{TrustProductSid}/Evaluations`
- **Server**: `default9`
- **Signature**: `def create_trust_product_evaluation(trust_product_sid: str, policy_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `trust_product_sid`, `policy_sid`
- **Params**: `trust_product_sid` — path `TrustProductSid` · `policy_sid` — form field `PolicySid`
- **Returns (parsed)**: `TrusthubV1TrustProductTrustProductEvaluation`
- **Returns (raw)**: `ApiResult[TrusthubV1TrustProductTrustProductEvaluation, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TrusthubV1TrustProductTrustProductEvaluation` | `twilio_sdk/models/trusthub_v1_trust_product_trust_product_evaluation.py` |

### client.trusthub_v1_trust_products_evaluations.fetch_trust_product_evaluation

- **Route**: `GET /v1/TrustProducts/{TrustProductSid}/Evaluations/{Sid}`
- **Server**: `default9`
- **Signature**: `def fetch_trust_product_evaluation(trust_product_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `trust_product_sid`, `sid`
- **Params**: `trust_product_sid` — path `TrustProductSid` · `sid` — path `Sid`
- **Returns (parsed)**: `TrusthubV1TrustProductTrustProductEvaluation`
- **Returns (raw)**: `ApiResult[TrusthubV1TrustProductTrustProductEvaluation, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TrusthubV1TrustProductTrustProductEvaluation` | `twilio_sdk/models/trusthub_v1_trust_product_trust_product_evaluation.py` |

### client.trusthub_v1_trust_products_evaluations.list_trust_product_evaluation

- **Route**: `GET /v1/TrustProducts/{TrustProductSid}/Evaluations`
- **Server**: `default9`
- **Signature**: `def list_trust_product_evaluation(trust_product_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `trust_product_sid`
- **Params**: `trust_product_sid` — path `TrustProductSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListTrustProductEvaluationResponse`
- **Returns (raw)**: `ApiResult[ListTrustProductEvaluationResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListTrustProductEvaluationResponse` | `twilio_sdk/models/list_trust_product_evaluation_response.py` |

