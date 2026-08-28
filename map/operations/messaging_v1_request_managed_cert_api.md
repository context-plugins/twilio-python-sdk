<!-- Generated file — do not edit; regenerated with the SDK. -->

# MessagingV1RequestManagedCertApi — operations

Accessor: `client.messaging_v1_request_managed_cert_api` · Source: `twilio_sdk/apis/messaging_v1_request_managed_cert_api.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.messaging_v1_request_managed_cert_api.update_request_managed_cert

- **Route**: `POST /v1/LinkShortening/Domains/{DomainSid}/RequestManagedCert`
- **Server**: `default1`
- **Signature**: `def update_request_managed_cert(domain_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `domain_sid`
- **Params**: `domain_sid` — path `DomainSid`
- **Returns (parsed)**: `MessagingV1RequestManagedCert`
- **Returns (raw)**: `ApiResult[MessagingV1RequestManagedCert, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MessagingV1RequestManagedCert` | `twilio_sdk/models/messaging_v1_request_managed_cert.py` |

