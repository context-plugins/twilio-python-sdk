<!-- Generated file — do not edit; regenerated with the SDK. -->

# ConversationsV2ConfigurationApi — operations

Accessor: `client.conversations_v2_configuration_api` · Source: `twilio_sdk/apis/conversations_v2_configuration_api.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.conversations_v2_configuration_api.create_configuration

- **Route**: `POST /v2/ControlPlane/Configurations`
- **Server**: `default7`
- **Signature**: `def create_configuration(*, idempotency_key: str | None = None, body: V2ControlPlaneConfigurationsRequest | V2ControlPlaneConfigurationsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `idempotency_key` — header `Idempotency-Key` · `body` — JSON body
- **Returns (parsed)**: `ConversationsV2OperationAccepted`
- **Returns (raw)**: `ApiResult[ConversationsV2OperationAccepted, CreateConfigurationErrorBody]`
- **Error**: `CreateConfigurationErrorBody` — **Case A (typed)**
- **Error arms**: `AccountsCallsRecordingsSidJson201041408Error1` [400, 409, 429, 500, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V2ControlPlaneConfigurationsRequest` | `twilio_sdk/models/v2_control_plane_configurations_request.py` |
| `V2ControlPlaneConfigurationsRequestDict` | `twilio_sdk/models/v2_control_plane_configurations_request.py` |
| `ConversationsV2OperationAccepted` | `twilio_sdk/models/conversations_v2_operation_accepted.py` |
| `CreateConfigurationErrorBody` | `twilio_sdk/errors/create_configuration_error.py` |
| `AccountsCallsRecordingsSidJson201041408Error1` | `twilio_sdk/models/accounts_calls_recordings_sid_json201041408_error1.py` |

### client.conversations_v2_configuration_api.delete_configuration

- **Route**: `DELETE /v2/ControlPlane/Configurations/{Sid}`
- **Server**: `default7`
- **Signature**: `def delete_configuration(sid: str, *, idempotency_key: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid` · `idempotency_key` — header `Idempotency-Key`
- **Returns (parsed)**: `ConversationsV2OperationAccepted`
- **Returns (raw)**: `ApiResult[ConversationsV2OperationAccepted, DeleteConfigurationErrorBody]`
- **Error**: `DeleteConfigurationErrorBody` — **Case A (typed)**
- **Error arms**: `AccountsCallsRecordingsSidJson201041408Error1` [404, 409, 429, 500, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ConversationsV2OperationAccepted` | `twilio_sdk/models/conversations_v2_operation_accepted.py` |
| `DeleteConfigurationErrorBody` | `twilio_sdk/errors/delete_configuration_error.py` |
| `AccountsCallsRecordingsSidJson201041408Error1` | `twilio_sdk/models/accounts_calls_recordings_sid_json201041408_error1.py` |

### client.conversations_v2_configuration_api.fetch_configuration2

- **Route**: `GET /v2/ControlPlane/Configurations/{Sid}`
- **Server**: `default7`
- **Signature**: `def fetch_configuration2(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `ConversationsV2Configuration`
- **Returns (raw)**: `ApiResult[ConversationsV2Configuration, FetchConfiguration2ErrorBody]`
- **Error**: `FetchConfiguration2ErrorBody` — **Case A (typed)**
- **Error arms**: `AccountsCallsRecordingsSidJson201041408Error1` [404, 429, 500, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ConversationsV2Configuration` | `twilio_sdk/models/conversations_v2_configuration.py` |
| `FetchConfiguration2ErrorBody` | `twilio_sdk/errors/fetch_configuration2_error.py` |
| `AccountsCallsRecordingsSidJson201041408Error1` | `twilio_sdk/models/accounts_calls_recordings_sid_json201041408_error1.py` |

### client.conversations_v2_configuration_api.list_configuration

- **Route**: `GET /v2/ControlPlane/Configurations`
- **Server**: `default7`
- **Signature**: `def list_configuration(*, page_size: int | None = 50, page_token: str | None = None, memory_store_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page_size` — query `pageSize` · `page_token` — query `pageToken` · `memory_store_id` — query `memoryStoreId`
- **Returns (parsed)**: `V2ControlPlaneConfigurationsResponse`
- **Returns (raw)**: `ApiResult[V2ControlPlaneConfigurationsResponse, ListConfigurationErrorBody]`
- **Error**: `ListConfigurationErrorBody` — **Case A (typed)**
- **Error arms**: `AccountsCallsRecordingsSidJson201041408Error1` [400, 404, 429, 500, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V2ControlPlaneConfigurationsResponse` | `twilio_sdk/models/v2_control_plane_configurations_response.py` |
| `ListConfigurationErrorBody` | `twilio_sdk/errors/list_configuration_error.py` |
| `AccountsCallsRecordingsSidJson201041408Error1` | `twilio_sdk/models/accounts_calls_recordings_sid_json201041408_error1.py` |

### client.conversations_v2_configuration_api.update_configuration2

- **Route**: `PUT /v2/ControlPlane/Configurations/{Sid}`
- **Server**: `default7`
- **Signature**: `def update_configuration2(sid: str, *, idempotency_key: str | None = None, body: V2ControlPlaneConfigurationsRequest1 | V2ControlPlaneConfigurationsRequest1Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid` · `idempotency_key` — header `Idempotency-Key` · `body` — JSON body
- **Returns (parsed)**: `ConversationsV2OperationAccepted`
- **Returns (raw)**: `ApiResult[ConversationsV2OperationAccepted, UpdateConfiguration2ErrorBody]`
- **Error**: `UpdateConfiguration2ErrorBody` — **Case A (typed)**
- **Error arms**: `AccountsCallsRecordingsSidJson201041408Error1` [400, 404, 409, 429, 500, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V2ControlPlaneConfigurationsRequest1` | `twilio_sdk/models/v2_control_plane_configurations_request1.py` |
| `V2ControlPlaneConfigurationsRequest1Dict` | `twilio_sdk/models/v2_control_plane_configurations_request1.py` |
| `ConversationsV2OperationAccepted` | `twilio_sdk/models/conversations_v2_operation_accepted.py` |
| `UpdateConfiguration2ErrorBody` | `twilio_sdk/errors/update_configuration2_error.py` |
| `AccountsCallsRecordingsSidJson201041408Error1` | `twilio_sdk/models/accounts_calls_recordings_sid_json201041408_error1.py` |

