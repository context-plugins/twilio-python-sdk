<!-- Generated file — do not edit; regenerated with the SDK. -->

# ConversationsV1AddressConfiguration — operations

Accessor: `client.conversations_v1_address_configuration` · Source: `twilio_sdk/apis/conversations_v1_address_configuration.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.conversations_v1_address_configuration.create_configuration_address

- **Route**: `POST /v1/Configuration/Addresses`
- **Server**: `default7`
- **Signature**: `def create_configuration_address(type_: ConfigurationAddressEnumTypeOrStr, address: str, *, friendly_name: str | None = None, auto_creation_enabled: bool | None = None, auto_creation_type: ConfigurationAddressEnumAutoCreationTypeOrStr | None = None, auto_creation_conversation_service_sid: str | None = None, auto_creation_webhook_url: str | None = None, auto_creation_webhook_method: ConfigurationAddressEnumMethodOrStr | None = None, auto_creation_webhook_filters: list[str] | None = None, auto_creation_studio_flow_sid: str | None = None, auto_creation_studio_retry_count: int | None = None, address_country: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `type_`, `address`
- **Params**: `type_` — form field `Type` · `address` — form field `Address` · `friendly_name` — form field `FriendlyName` · `auto_creation_enabled` — form field `AutoCreation.Enabled` · `auto_creation_type` — form field `AutoCreation.Type` · `auto_creation_conversation_service_sid` — form field `AutoCreation.ConversationServiceSid` · `auto_creation_webhook_url` — form field `AutoCreation.WebhookUrl` · `auto_creation_webhook_method` — form field `AutoCreation.WebhookMethod` · `auto_creation_webhook_filters` — form field `AutoCreation.WebhookFilters` · `auto_creation_studio_flow_sid` — form field `AutoCreation.StudioFlowSid` · `auto_creation_studio_retry_count` — form field `AutoCreation.StudioRetryCount` · `address_country` — form field `AddressCountry`
- **Returns (parsed)**: `ConversationsV1ConfigurationAddress`
- **Returns (raw)**: `ApiResult[ConversationsV1ConfigurationAddress, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConfigurationAddressEnumTypeOrStr` | `twilio_sdk/models/enums/configuration_address_enum_type.py` |
| `ConfigurationAddressEnumAutoCreationTypeOrStr` | `twilio_sdk/models/enums/configuration_address_enum_auto_creation_type.py` |
| `ConfigurationAddressEnumMethodOrStr` | `twilio_sdk/models/enums/configuration_address_enum_method.py` |
| `ConversationsV1ConfigurationAddress` | `twilio_sdk/models/conversations_v1_configuration_address.py` |

### client.conversations_v1_address_configuration.delete_configuration_address

- **Route**: `DELETE /v1/Configuration/Addresses/{Sid}`
- **Server**: `default7`
- **Signature**: `def delete_configuration_address(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.conversations_v1_address_configuration.fetch_configuration_address

- **Route**: `GET /v1/Configuration/Addresses/{Sid}`
- **Server**: `default7`
- **Signature**: `def fetch_configuration_address(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `ConversationsV1ConfigurationAddress`
- **Returns (raw)**: `ApiResult[ConversationsV1ConfigurationAddress, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConversationsV1ConfigurationAddress` | `twilio_sdk/models/conversations_v1_configuration_address.py` |

### client.conversations_v1_address_configuration.list_configuration_address

- **Route**: `GET /v1/Configuration/Addresses`
- **Server**: `default7`
- **Signature**: `def list_configuration_address(*, type_: str | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `type_` — query `Type` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListConfigurationAddressResponse`
- **Returns (raw)**: `ApiResult[ListConfigurationAddressResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListConfigurationAddressResponse` | `twilio_sdk/models/list_configuration_address_response.py` |

### client.conversations_v1_address_configuration.update_configuration_address

- **Route**: `POST /v1/Configuration/Addresses/{Sid}`
- **Server**: `default7`
- **Signature**: `def update_configuration_address(sid: str, *, friendly_name: str | None = None, auto_creation_enabled: bool | None = None, auto_creation_type: ConfigurationAddressEnumAutoCreationTypeOrStr | None = None, auto_creation_conversation_service_sid: str | None = None, auto_creation_webhook_url: str | None = None, auto_creation_webhook_method: ConfigurationAddressEnumMethodOrStr | None = None, auto_creation_webhook_filters: list[str] | None = None, auto_creation_studio_flow_sid: str | None = None, auto_creation_studio_retry_count: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid` · `friendly_name` — form field `FriendlyName` · `auto_creation_enabled` — form field `AutoCreation.Enabled` · `auto_creation_type` — form field `AutoCreation.Type` · `auto_creation_conversation_service_sid` — form field `AutoCreation.ConversationServiceSid` · `auto_creation_webhook_url` — form field `AutoCreation.WebhookUrl` · `auto_creation_webhook_method` — form field `AutoCreation.WebhookMethod` · `auto_creation_webhook_filters` — form field `AutoCreation.WebhookFilters` · `auto_creation_studio_flow_sid` — form field `AutoCreation.StudioFlowSid` · `auto_creation_studio_retry_count` — form field `AutoCreation.StudioRetryCount`
- **Returns (parsed)**: `ConversationsV1ConfigurationAddress`
- **Returns (raw)**: `ApiResult[ConversationsV1ConfigurationAddress, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConfigurationAddressEnumAutoCreationTypeOrStr` | `twilio_sdk/models/enums/configuration_address_enum_auto_creation_type.py` |
| `ConfigurationAddressEnumMethodOrStr` | `twilio_sdk/models/enums/configuration_address_enum_method.py` |
| `ConversationsV1ConfigurationAddress` | `twilio_sdk/models/conversations_v1_configuration_address.py` |

