<!-- Generated file — do not edit; regenerated with the SDK. -->

# NumbersV1SigningRequestConfigurationApi — operations

Accessor: `client.numbers_v1_signing_request_configuration_api` · Source: `twilio/apis/numbers_v1_signing_request_configuration_api.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.numbers_v1_signing_request_configuration_api.create_signing_request_configuration

- **Route**: `POST /v1/SigningRequest/Configuration`
- **Server**: `default5`
- **Signature**: `def create_signing_request_configuration(*, body: Any | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `NumbersV1SigningRequestConfiguration`
- **Returns (raw)**: `ApiResult[NumbersV1SigningRequestConfiguration, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NumbersV1SigningRequestConfiguration` | `twilio/models/numbers_v1_signing_request_configuration.py` |

### client.numbers_v1_signing_request_configuration_api.list_signing_request_configuration

- **Route**: `GET /v1/SigningRequest/Configuration`
- **Server**: `default5`
- **Signature**: `def list_signing_request_configuration(*, country: str | None = None, product: str | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `country` — query `Country` · `product` — query `Product` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListSigningRequestConfigurationResponse`
- **Returns (raw)**: `ApiResult[ListSigningRequestConfigurationResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListSigningRequestConfigurationResponse` | `twilio/models/list_signing_request_configuration_response.py` |

