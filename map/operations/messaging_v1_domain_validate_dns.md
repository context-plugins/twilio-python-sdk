<!-- Generated file — do not edit; regenerated with the SDK. -->

# MessagingV1DomainValidateDns — operations

Accessor: `client.messaging_v1_domain_validate_dns` · Source: `twilio/apis/messaging_v1_domain_validate_dns.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.messaging_v1_domain_validate_dns.fetch_domain_dns_validation

- **Route**: `GET /v1/LinkShortening/Domains/{DomainSid}/ValidateDns`
- **Server**: `default1`
- **Signature**: `def fetch_domain_dns_validation(domain_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `domain_sid`
- **Params**: `domain_sid` — path `DomainSid`
- **Returns (parsed)**: `MessagingV1DomainDnsValidation`
- **Returns (raw)**: `ApiResult[MessagingV1DomainDnsValidation, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MessagingV1DomainDnsValidation` | `twilio/models/messaging_v1_domain_dns_validation.py` |

