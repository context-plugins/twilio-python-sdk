<!-- Generated file — do not edit; regenerated with the SDK. -->

# MessagingV1DomainCerts — operations

Accessor: `client.messaging_v1_domain_certs` · Source: `twilio/apis/messaging_v1_domain_certs.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.messaging_v1_domain_certs.delete_domain_cert_v4

- **Route**: `DELETE /v1/LinkShortening/Domains/{DomainSid}/Certificate`
- **Server**: `default1`
- **Signature**: `def delete_domain_cert_v4(domain_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `domain_sid`
- **Params**: `domain_sid` — path `DomainSid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.messaging_v1_domain_certs.fetch_domain_cert_v4

- **Route**: `GET /v1/LinkShortening/Domains/{DomainSid}/Certificate`
- **Server**: `default1`
- **Signature**: `def fetch_domain_cert_v4(domain_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `domain_sid`
- **Params**: `domain_sid` — path `DomainSid`
- **Returns (parsed)**: `MessagingV1DomainCertV4`
- **Returns (raw)**: `ApiResult[MessagingV1DomainCertV4, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MessagingV1DomainCertV4` | `twilio/models/messaging_v1_domain_cert_v4.py` |

### client.messaging_v1_domain_certs.update_domain_cert_v4

- **Route**: `POST /v1/LinkShortening/Domains/{DomainSid}/Certificate`
- **Server**: `default1`
- **Signature**: `def update_domain_cert_v4(domain_sid: str, tls_cert: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `domain_sid`, `tls_cert`
- **Params**: `domain_sid` — path `DomainSid` · `tls_cert` — form field `TlsCert`
- **Returns (parsed)**: `MessagingV1DomainCertV4`
- **Returns (raw)**: `ApiResult[MessagingV1DomainCertV4, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MessagingV1DomainCertV4` | `twilio/models/messaging_v1_domain_cert_v4.py` |

