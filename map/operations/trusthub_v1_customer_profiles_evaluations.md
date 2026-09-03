<!-- Generated file — do not edit; regenerated with the SDK. -->

# TrusthubV1CustomerProfilesEvaluations — operations

Accessor: `client.trusthub_v1_customer_profiles_evaluations` · Source: `twilio_sdk/apis/trusthub_v1_customer_profiles_evaluations.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.trusthub_v1_customer_profiles_evaluations.create_customer_profile_evaluation

- **Route**: `POST /v1/CustomerProfiles/{CustomerProfileSid}/Evaluations`
- **Auth**: `account_sid_auth_token`
- **Server**: `default9`
- **Signature**: `def create_customer_profile_evaluation(customer_profile_sid: str, policy_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `customer_profile_sid`, `policy_sid`
- **Params**: `customer_profile_sid` — path `CustomerProfileSid` · `policy_sid` — form field `PolicySid`
- **Returns (parsed)**: `TrusthubV1CustomerProfileCustomerProfileEvaluation`
- **Returns (raw)**: `ApiResult[TrusthubV1CustomerProfileCustomerProfileEvaluation, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TrusthubV1CustomerProfileCustomerProfileEvaluation` | `twilio_sdk/models/trusthub_v1_customer_profile_customer_profile_evaluation.py` |

### client.trusthub_v1_customer_profiles_evaluations.fetch_customer_profile_evaluation

- **Route**: `GET /v1/CustomerProfiles/{CustomerProfileSid}/Evaluations/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default9`
- **Signature**: `def fetch_customer_profile_evaluation(customer_profile_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `customer_profile_sid`, `sid`
- **Params**: `customer_profile_sid` — path `CustomerProfileSid` · `sid` — path `Sid`
- **Returns (parsed)**: `TrusthubV1CustomerProfileCustomerProfileEvaluation`
- **Returns (raw)**: `ApiResult[TrusthubV1CustomerProfileCustomerProfileEvaluation, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TrusthubV1CustomerProfileCustomerProfileEvaluation` | `twilio_sdk/models/trusthub_v1_customer_profile_customer_profile_evaluation.py` |

### client.trusthub_v1_customer_profiles_evaluations.list_customer_profile_evaluation

- **Route**: `GET /v1/CustomerProfiles/{CustomerProfileSid}/Evaluations`
- **Auth**: `account_sid_auth_token`
- **Server**: `default9`
- **Signature**: `def list_customer_profile_evaluation(customer_profile_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `customer_profile_sid`
- **Params**: `customer_profile_sid` — path `CustomerProfileSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListCustomerProfileEvaluationResponse`
- **Returns (raw)**: `ApiResult[ListCustomerProfileEvaluationResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListCustomerProfileEvaluationResponse` | `twilio_sdk/models/list_customer_profile_evaluation_response.py` |

