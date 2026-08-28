<!-- Generated file — do not edit; regenerated with the SDK. -->

# VerifyV2Challenge — operations

Accessor: `client.verify_v2_challenge` · Source: `twilio_sdk/apis/verify_v2_challenge.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.verify_v2_challenge.create_challenge

- **Route**: `POST /v2/Services/{ServiceSid}/Entities/{Identity}/Challenges`
- **Server**: `default3`
- **Signature**: `def create_challenge(service_sid: str, identity: str, factor_sid: str, *, expiration_date: RFC3339DateTime | None = None, details_message: str | None = None, details_fields: list[Any] | None = None, hidden_details: Any | None = None, auth_payload: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `identity`, `factor_sid`
- **Params**: `service_sid` — path `ServiceSid` · `identity` — path `Identity` · `factor_sid` — form field `FactorSid` · `expiration_date` — form field `ExpirationDate` · `details_message` — form field `Details.Message` · `details_fields` — form field `Details.Fields` · `hidden_details` — form field `HiddenDetails` · `auth_payload` — form field `AuthPayload`
- **Returns (parsed)**: `VerifyV2ServiceEntityChallenge`
- **Returns (raw)**: `ApiResult[VerifyV2ServiceEntityChallenge, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VerifyV2ServiceEntityChallenge` | `twilio_sdk/models/verify_v2_service_entity_challenge.py` |

### client.verify_v2_challenge.fetch_challenge

- **Route**: `GET /v2/Services/{ServiceSid}/Entities/{Identity}/Challenges/{Sid}`
- **Server**: `default3`
- **Signature**: `def fetch_challenge(service_sid: str, identity: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `identity`, `sid`
- **Params**: `service_sid` — path `ServiceSid` · `identity` — path `Identity` · `sid` — path `Sid`
- **Returns (parsed)**: `VerifyV2ServiceEntityChallenge`
- **Returns (raw)**: `ApiResult[VerifyV2ServiceEntityChallenge, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VerifyV2ServiceEntityChallenge` | `twilio_sdk/models/verify_v2_service_entity_challenge.py` |

### client.verify_v2_challenge.list_challenge

- **Route**: `GET /v2/Services/{ServiceSid}/Entities/{Identity}/Challenges`
- **Server**: `default3`
- **Signature**: `def list_challenge(service_sid: str, identity: str, *, factor_sid: str | None = None, status: ChallengeEnumChallengeStatusesOrStr | None = None, order: ChallengeEnumListOrdersOrStr | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `identity`
- **Params**: `service_sid` — path `ServiceSid` · `identity` — path `Identity` · `factor_sid` — query `FactorSid` · `status` — query `Status` · `order` — query `Order` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListChallengeResponse`
- **Returns (raw)**: `ApiResult[ListChallengeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ChallengeEnumChallengeStatusesOrStr` | `twilio_sdk/models/enums/challenge_enum_challenge_statuses.py` |
| `ChallengeEnumListOrdersOrStr` | `twilio_sdk/models/enums/challenge_enum_list_orders.py` |
| `ListChallengeResponse` | `twilio_sdk/models/list_challenge_response.py` |

### client.verify_v2_challenge.update_challenge

- **Route**: `POST /v2/Services/{ServiceSid}/Entities/{Identity}/Challenges/{Sid}`
- **Server**: `default3`
- **Signature**: `def update_challenge(service_sid: str, identity: str, sid: str, *, auth_payload: str | None = None, metadata: Any | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `identity`, `sid`
- **Params**: `service_sid` — path `ServiceSid` · `identity` — path `Identity` · `sid` — path `Sid` · `auth_payload` — form field `AuthPayload` · `metadata` — form field `Metadata`
- **Returns (parsed)**: `VerifyV2ServiceEntityChallenge`
- **Returns (raw)**: `ApiResult[VerifyV2ServiceEntityChallenge, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VerifyV2ServiceEntityChallenge` | `twilio_sdk/models/verify_v2_service_entity_challenge.py` |

