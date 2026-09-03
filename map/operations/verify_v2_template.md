<!-- Generated file — do not edit; regenerated with the SDK. -->

# VerifyV2Template — operations

Accessor: `client.verify_v2_template` · Source: `twilio_sdk/apis/verify_v2_template.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.verify_v2_template.list_verification_template

- **Route**: `GET /v2/Templates`
- **Auth**: `account_sid_auth_token`
- **Server**: `default3`
- **Signature**: `def list_verification_template(*, friendly_name: str | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `friendly_name` — query `FriendlyName` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListVerificationTemplateResponse`
- **Returns (raw)**: `ApiResult[ListVerificationTemplateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListVerificationTemplateResponse` | `twilio_sdk/models/list_verification_template_response.py` |

