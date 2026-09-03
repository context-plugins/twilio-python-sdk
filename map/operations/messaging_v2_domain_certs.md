<!-- Generated file — do not edit; regenerated with the SDK. -->

# MessagingV2DomainCerts — operations

Accessor: `client.messaging_v2_domain_certs` · Source: `twilio_sdk/apis/messaging_v2_domain_certs.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.messaging_v2_domain_certs.fetch_domain_cert_v42

- **Route**: `GET /v2/LinkShortening/Domains/{DomainSid}/Certificate`
- **Auth**: `account_sid_auth_token`
- **Server**: `default1`
- **Signature**: `def fetch_domain_cert_v42(domain_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `domain_sid`
- **Params**: `domain_sid` — path `DomainSid`
- **Returns (parsed)**: `MessagingV2DomainCertV4`
- **Returns (raw)**: `ApiResult[MessagingV2DomainCertV4, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MessagingV2DomainCertV4` | `twilio_sdk/models/messaging_v2_domain_cert_v4.py` |

