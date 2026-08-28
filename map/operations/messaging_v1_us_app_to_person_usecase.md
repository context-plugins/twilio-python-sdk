<!-- Generated file — do not edit; regenerated with the SDK. -->

# MessagingV1UsAppToPersonUsecase — operations

Accessor: `client.messaging_v1_us_app_to_person_usecase` · Source: `twilio_sdk/apis/messaging_v1_us_app_to_person_usecase.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.messaging_v1_us_app_to_person_usecase.fetch_us_app_to_person_usecase

- **Route**: `GET /v1/Services/{MessagingServiceSid}/Compliance/Usa2p/Usecases`
- **Server**: `default1`
- **Signature**: `def fetch_us_app_to_person_usecase(messaging_service_sid: str, *, brand_registration_sid: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `messaging_service_sid`
- **Params**: `messaging_service_sid` — path `MessagingServiceSid` · `brand_registration_sid` — query `BrandRegistrationSid`
- **Returns (parsed)**: `MessagingV1ServiceUsAppToPersonUsecase`
- **Returns (raw)**: `ApiResult[MessagingV1ServiceUsAppToPersonUsecase, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MessagingV1ServiceUsAppToPersonUsecase` | `twilio_sdk/models/messaging_v1_service_us_app_to_person_usecase.py` |

