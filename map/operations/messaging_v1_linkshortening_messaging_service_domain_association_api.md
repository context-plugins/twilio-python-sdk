<!-- Generated file — do not edit; regenerated with the SDK. -->

# MessagingV1LinkshorteningMessagingServiceDomainAssociationApi — operations

Accessor: `client.messaging_v1_linkshortening_messaging_service_domain_association_api` · Source: `twilio_sdk/apis/messaging_v1_linkshortening_messaging_service_domain_association_api.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.messaging_v1_linkshortening_messaging_service_domain_association_api.fetch_linkshortening_messaging_service_domain_association

- **Route**: `GET /v1/LinkShortening/MessagingServices/{MessagingServiceSid}/Domain`
- **Server**: `default1`
- **Signature**: `def fetch_linkshortening_messaging_service_domain_association(messaging_service_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `messaging_service_sid`
- **Params**: `messaging_service_sid` — path `MessagingServiceSid`
- **Returns (parsed)**: `MessagingV1LinkshorteningMessagingServiceDomainAssociation`
- **Returns (raw)**: `ApiResult[MessagingV1LinkshorteningMessagingServiceDomainAssociation, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MessagingV1LinkshorteningMessagingServiceDomainAssociation` | `twilio_sdk/models/messaging_v1_linkshortening_messaging_service_domain_association.py` |

