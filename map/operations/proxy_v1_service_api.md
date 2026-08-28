<!-- Generated file — do not edit; regenerated with the SDK. -->

# ProxyV1ServiceApi — operations

Accessor: `client.proxy_v1_service_api` · Source: `twilio_sdk/apis/proxy_v1_service_api.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.proxy_v1_service_api.create_service4

- **Route**: `POST /v1/Services`
- **Server**: `default10`
- **Signature**: `def create_service4(unique_name: str, *, default_ttl: int | None = None, callback_url: AnyUrl | None = None, geo_match_level: ServiceEnumGeoMatchLevelOrStr | None = None, number_selection_behavior: ServiceEnumNumberSelectionBehaviorOrStr | None = None, intercept_callback_url: AnyUrl | None = None, out_of_session_callback_url: AnyUrl | None = None, chat_instance_sid: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `unique_name`
- **Params**: `unique_name` — form field `UniqueName` · `default_ttl` — form field `DefaultTtl` · `callback_url` — form field `CallbackUrl` · `geo_match_level` — form field `GeoMatchLevel` · `number_selection_behavior` — form field `NumberSelectionBehavior` · `intercept_callback_url` — form field `InterceptCallbackUrl` · `out_of_session_callback_url` — form field `OutOfSessionCallbackUrl` · `chat_instance_sid` — form field `ChatInstanceSid`
- **Returns (parsed)**: `ProxyV1Service`
- **Returns (raw)**: `ApiResult[ProxyV1Service, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ServiceEnumGeoMatchLevelOrStr` | `twilio_sdk/models/enums/service_enum_geo_match_level.py` |
| `ServiceEnumNumberSelectionBehaviorOrStr` | `twilio_sdk/models/enums/service_enum_number_selection_behavior.py` |
| `ProxyV1Service` | `twilio_sdk/models/proxy_v1_service.py` |

### client.proxy_v1_service_api.delete_service4

- **Route**: `DELETE /v1/Services/{Sid}`
- **Server**: `default10`
- **Signature**: `def delete_service4(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.proxy_v1_service_api.fetch_service4

- **Route**: `GET /v1/Services/{Sid}`
- **Server**: `default10`
- **Signature**: `def fetch_service4(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `ProxyV1Service`
- **Returns (raw)**: `ApiResult[ProxyV1Service, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProxyV1Service` | `twilio_sdk/models/proxy_v1_service.py` |

### client.proxy_v1_service_api.list_service4

- **Route**: `GET /v1/Services`
- **Server**: `default10`
- **Signature**: `def list_service4(*, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListServiceResponse3`
- **Returns (raw)**: `ApiResult[ListServiceResponse3, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListServiceResponse3` | `twilio_sdk/models/list_service_response3.py` |

### client.proxy_v1_service_api.update_service3

- **Route**: `POST /v1/Services/{Sid}`
- **Server**: `default10`
- **Signature**: `def update_service3(sid: str, *, unique_name: str | None = None, default_ttl: int | None = None, callback_url: AnyUrl | None = None, geo_match_level: ServiceEnumGeoMatchLevelOrStr | None = None, number_selection_behavior: ServiceEnumNumberSelectionBehaviorOrStr | None = None, intercept_callback_url: AnyUrl | None = None, out_of_session_callback_url: AnyUrl | None = None, chat_instance_sid: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid` · `unique_name` — form field `UniqueName` · `default_ttl` — form field `DefaultTtl` · `callback_url` — form field `CallbackUrl` · `geo_match_level` — form field `GeoMatchLevel` · `number_selection_behavior` — form field `NumberSelectionBehavior` · `intercept_callback_url` — form field `InterceptCallbackUrl` · `out_of_session_callback_url` — form field `OutOfSessionCallbackUrl` · `chat_instance_sid` — form field `ChatInstanceSid`
- **Returns (parsed)**: `ProxyV1Service`
- **Returns (raw)**: `ApiResult[ProxyV1Service, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ServiceEnumGeoMatchLevelOrStr` | `twilio_sdk/models/enums/service_enum_geo_match_level.py` |
| `ServiceEnumNumberSelectionBehaviorOrStr` | `twilio_sdk/models/enums/service_enum_number_selection_behavior.py` |
| `ProxyV1Service` | `twilio_sdk/models/proxy_v1_service.py` |

