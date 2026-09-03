<!-- Generated file — do not edit; regenerated with the SDK. -->

# ConversationsV1CredentialApi — operations

Accessor: `client.conversations_v1_credential_api` · Source: `twilio_sdk/apis/conversations_v1_credential_api.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.conversations_v1_credential_api.create_credential

- **Route**: `POST /v1/Credentials`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def create_credential(type_: CredentialEnumPushTypeOrStr, *, friendly_name: str | None = None, certificate: str | None = None, private_key: str | None = None, sandbox: bool | None = None, api_key: str | None = None, secret: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `type_`
- **Params**: `type_` — form field `Type` · `friendly_name` — form field `FriendlyName` · `certificate` — form field `Certificate` · `private_key` — form field `PrivateKey` · `sandbox` — form field `Sandbox` · `api_key` — form field `ApiKey` · `secret` — form field `Secret`
- **Returns (parsed)**: `ConversationsV1Credential`
- **Returns (raw)**: `ApiResult[ConversationsV1Credential, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CredentialEnumPushTypeOrStr` | `twilio_sdk/models/enums/credential_enum_push_type.py` |
| `ConversationsV1Credential` | `twilio_sdk/models/conversations_v1_credential.py` |

### client.conversations_v1_credential_api.delete_credential

- **Route**: `DELETE /v1/Credentials/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def delete_credential(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.conversations_v1_credential_api.fetch_credential

- **Route**: `GET /v1/Credentials/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def fetch_credential(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `ConversationsV1Credential`
- **Returns (raw)**: `ApiResult[ConversationsV1Credential, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConversationsV1Credential` | `twilio_sdk/models/conversations_v1_credential.py` |

### client.conversations_v1_credential_api.list_credential

- **Route**: `GET /v1/Credentials`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def list_credential(*, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListCredentialResponse`
- **Returns (raw)**: `ApiResult[ListCredentialResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListCredentialResponse` | `twilio_sdk/models/list_credential_response.py` |

### client.conversations_v1_credential_api.update_credential

- **Route**: `POST /v1/Credentials/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def update_credential(sid: str, *, type_: CredentialEnumPushTypeOrStr | None = None, friendly_name: str | None = None, certificate: str | None = None, private_key: str | None = None, sandbox: bool | None = None, api_key: str | None = None, secret: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid` · `type_` — form field `Type` · `friendly_name` — form field `FriendlyName` · `certificate` — form field `Certificate` · `private_key` — form field `PrivateKey` · `sandbox` — form field `Sandbox` · `api_key` — form field `ApiKey` · `secret` — form field `Secret`
- **Returns (parsed)**: `ConversationsV1Credential`
- **Returns (raw)**: `ApiResult[ConversationsV1Credential, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CredentialEnumPushTypeOrStr` | `twilio_sdk/models/enums/credential_enum_push_type.py` |
| `ConversationsV1Credential` | `twilio_sdk/models/conversations_v1_credential.py` |

