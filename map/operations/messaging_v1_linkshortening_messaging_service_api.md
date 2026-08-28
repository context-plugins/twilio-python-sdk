<!-- Generated file — do not edit; regenerated with the SDK. -->

# MessagingV1LinkshorteningMessagingServiceApi — operations

Accessor: `client.messaging_v1_linkshortening_messaging_service_api` · Source: `twilio_sdk/apis/messaging_v1_linkshortening_messaging_service_api.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.messaging_v1_linkshortening_messaging_service_api.create_linkshortening_messaging_service

- **Route**: `POST /v1/LinkShortening/Domains/{DomainSid}/MessagingServices/{MessagingServiceSid}`
- **Server**: `default1`
- **Signature**: `def create_linkshortening_messaging_service(domain_sid: str, messaging_service_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `domain_sid`, `messaging_service_sid`
- **Params**: `domain_sid` — path `DomainSid` · `messaging_service_sid` — path `MessagingServiceSid`
- **Returns (parsed)**: `MessagingV1LinkshorteningMessagingService`
- **Returns (raw)**: `ApiResult[MessagingV1LinkshorteningMessagingService, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MessagingV1LinkshorteningMessagingService` | `twilio_sdk/models/messaging_v1_linkshortening_messaging_service.py` |

### client.messaging_v1_linkshortening_messaging_service_api.delete_linkshortening_messaging_service

- **Route**: `DELETE /v1/LinkShortening/Domains/{DomainSid}/MessagingServices/{MessagingServiceSid}`
- **Server**: `default1`
- **Signature**: `def delete_linkshortening_messaging_service(domain_sid: str, messaging_service_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `domain_sid`, `messaging_service_sid`
- **Params**: `domain_sid` — path `DomainSid` · `messaging_service_sid` — path `MessagingServiceSid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

