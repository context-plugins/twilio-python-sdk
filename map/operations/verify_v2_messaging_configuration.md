<!-- Generated file — do not edit; regenerated with the SDK. -->

# VerifyV2MessagingConfiguration — operations

Accessor: `client.verify_v2_messaging_configuration` · Source: `twilio_sdk/apis/verify_v2_messaging_configuration.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.verify_v2_messaging_configuration.create_messaging_configuration

- **Route**: `POST /v2/Services/{ServiceSid}/MessagingConfigurations`
- **Server**: `default3`
- **Signature**: `def create_messaging_configuration(service_sid: str, country: str, messaging_service_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `country`, `messaging_service_sid`
- **Params**: `service_sid` — path `ServiceSid` · `country` — form field `Country` · `messaging_service_sid` — form field `MessagingServiceSid`
- **Returns (parsed)**: `VerifyV2ServiceMessagingConfiguration`
- **Returns (raw)**: `ApiResult[VerifyV2ServiceMessagingConfiguration, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VerifyV2ServiceMessagingConfiguration` | `twilio_sdk/models/verify_v2_service_messaging_configuration.py` |

### client.verify_v2_messaging_configuration.delete_messaging_configuration

- **Route**: `DELETE /v2/Services/{ServiceSid}/MessagingConfigurations/{Country}`
- **Server**: `default3`
- **Signature**: `def delete_messaging_configuration(service_sid: str, country: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `country`
- **Params**: `service_sid` — path `ServiceSid` · `country` — path `Country`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.verify_v2_messaging_configuration.fetch_messaging_configuration

- **Route**: `GET /v2/Services/{ServiceSid}/MessagingConfigurations/{Country}`
- **Server**: `default3`
- **Signature**: `def fetch_messaging_configuration(service_sid: str, country: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `country`
- **Params**: `service_sid` — path `ServiceSid` · `country` — path `Country`
- **Returns (parsed)**: `VerifyV2ServiceMessagingConfiguration`
- **Returns (raw)**: `ApiResult[VerifyV2ServiceMessagingConfiguration, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VerifyV2ServiceMessagingConfiguration` | `twilio_sdk/models/verify_v2_service_messaging_configuration.py` |

### client.verify_v2_messaging_configuration.list_messaging_configuration

- **Route**: `GET /v2/Services/{ServiceSid}/MessagingConfigurations`
- **Server**: `default3`
- **Signature**: `def list_messaging_configuration(service_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`
- **Params**: `service_sid` — path `ServiceSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListMessagingConfigurationResponse`
- **Returns (raw)**: `ApiResult[ListMessagingConfigurationResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListMessagingConfigurationResponse` | `twilio_sdk/models/list_messaging_configuration_response.py` |

### client.verify_v2_messaging_configuration.update_messaging_configuration

- **Route**: `POST /v2/Services/{ServiceSid}/MessagingConfigurations/{Country}`
- **Server**: `default3`
- **Signature**: `def update_messaging_configuration(service_sid: str, country: str, messaging_service_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `country`, `messaging_service_sid`
- **Params**: `service_sid` — path `ServiceSid` · `country` — path `Country` · `messaging_service_sid` — form field `MessagingServiceSid`
- **Returns (parsed)**: `VerifyV2ServiceMessagingConfiguration`
- **Returns (raw)**: `ApiResult[VerifyV2ServiceMessagingConfiguration, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VerifyV2ServiceMessagingConfiguration` | `twilio_sdk/models/verify_v2_service_messaging_configuration.py` |

