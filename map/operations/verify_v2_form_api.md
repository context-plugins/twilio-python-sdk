<!-- Generated file — do not edit; regenerated with the SDK. -->

# VerifyV2FormApi — operations

Accessor: `client.verify_v2_form_api` · Source: `twilio/apis/verify_v2_form_api.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.verify_v2_form_api.fetch_form

- **Route**: `GET /v2/Forms/{FormType}`
- **Server**: `default3`
- **Signature**: `def fetch_form(form_type: FormEnumFormTypesOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `form_type`
- **Params**: `form_type` — path `FormType`
- **Returns (parsed)**: `VerifyV2Form`
- **Returns (raw)**: `ApiResult[VerifyV2Form, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FormEnumFormTypesOrStr` | `twilio/models/enums/form_enum_form_types.py` |
| `VerifyV2Form` | `twilio/models/verify_v2_form.py` |

