<!-- Generated file — do not edit; regenerated with the SDK. -->

# NumbersV2DependentHostedNumberOrder — operations

Accessor: `client.numbers_v2_dependent_hosted_number_order` · Source: `twilio_sdk/apis/numbers_v2_dependent_hosted_number_order.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.numbers_v2_dependent_hosted_number_order.list_dependent_hosted_number_order

- **Route**: `GET /v2/HostedNumber/AuthorizationDocuments/{SigningDocumentSid}/DependentHostedNumberOrders`
- **Server**: `default5`
- **Signature**: `def list_dependent_hosted_number_order(signing_document_sid: str, *, status: DependentHostedNumberOrderEnumStatusOrStr | None = None, phone_number: str | None = None, incoming_phone_number_sid: str | None = None, friendly_name: str | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `signing_document_sid`
- **Params**: `signing_document_sid` — path `SigningDocumentSid` · `status` — query `Status` · `phone_number` — query `PhoneNumber` · `incoming_phone_number_sid` — query `IncomingPhoneNumberSid` · `friendly_name` — query `FriendlyName` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListDependentHostedNumberOrderResponse`
- **Returns (raw)**: `ApiResult[ListDependentHostedNumberOrderResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DependentHostedNumberOrderEnumStatusOrStr` | `twilio_sdk/models/enums/dependent_hosted_number_order_enum_status.py` |
| `ListDependentHostedNumberOrderResponse` | `twilio_sdk/models/list_dependent_hosted_number_order_response.py` |

