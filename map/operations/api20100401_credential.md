<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401Credential — operations

Accessor: `client.api20100401_credential` · Source: `twilio_sdk/apis/api20100401_credential.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.api20100401_credential.create_sip_credential

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{CredentialListSid}/Credentials.json`
- **Server**: `default`
- **Signature**: `def create_sip_credential(account_sid: str, credential_list_sid: str, username: str, password: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `credential_list_sid`, `username`, `password`
- **Params**: `account_sid` — path `AccountSid` · `credential_list_sid` — path `CredentialListSid` · `username` — form field `Username` · `password` — form field `Password`
- **Returns (parsed)**: `ApiV2010AccountSipSipCredentialListSipCredential`
- **Returns (raw)**: `ApiResult[ApiV2010AccountSipSipCredentialListSipCredential, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountSipSipCredentialListSipCredential` | `twilio_sdk/models/api_v2010_account_sip_sip_credential_list_sip_credential.py` |

### client.api20100401_credential.delete_sip_credential

- **Route**: `DELETE /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{CredentialListSid}/Credentials/{Sid}.json`
- **Server**: `default`
- **Signature**: `def delete_sip_credential(account_sid: str, credential_list_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `credential_list_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `credential_list_sid` — path `CredentialListSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.api20100401_credential.fetch_sip_credential

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{CredentialListSid}/Credentials/{Sid}.json`
- **Server**: `default`
- **Signature**: `def fetch_sip_credential(account_sid: str, credential_list_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `credential_list_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `credential_list_sid` — path `CredentialListSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ApiV2010AccountSipSipCredentialListSipCredential`
- **Returns (raw)**: `ApiResult[ApiV2010AccountSipSipCredentialListSipCredential, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountSipSipCredentialListSipCredential` | `twilio_sdk/models/api_v2010_account_sip_sip_credential_list_sip_credential.py` |

### client.api20100401_credential.list_sip_credential

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{CredentialListSid}/Credentials.json`
- **Server**: `default`
- **Signature**: `def list_sip_credential(account_sid: str, credential_list_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `credential_list_sid`
- **Params**: `account_sid` — path `AccountSid` · `credential_list_sid` — path `CredentialListSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListSipCredentialResponse`
- **Returns (raw)**: `ApiResult[ListSipCredentialResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListSipCredentialResponse` | `twilio_sdk/models/list_sip_credential_response.py` |

### client.api20100401_credential.update_sip_credential

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{CredentialListSid}/Credentials/{Sid}.json`
- **Server**: `default`
- **Signature**: `def update_sip_credential(account_sid: str, credential_list_sid: str, sid: str, *, password: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `credential_list_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `credential_list_sid` — path `CredentialListSid` · `sid` — path `Sid` · `password` — form field `Password`
- **Returns (parsed)**: `ApiV2010AccountSipSipCredentialListSipCredential`
- **Returns (raw)**: `ApiResult[ApiV2010AccountSipSipCredentialListSipCredential, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountSipSipCredentialListSipCredential` | `twilio_sdk/models/api_v2010_account_sip_sip_credential_list_sip_credential.py` |

