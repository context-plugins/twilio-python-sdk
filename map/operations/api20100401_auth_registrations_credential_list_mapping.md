<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401AuthRegistrationsCredentialListMapping — operations

Accessor: `client.api20100401_auth_registrations_credential_list_mapping` · Source: `twilio/apis/api20100401_auth_registrations_credential_list_mapping.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.api20100401_auth_registrations_credential_list_mapping.create_sip_auth_registrations_credential_list_mapping

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Registrations/CredentialListMappings.json`
- **Server**: `default`
- **Signature**: `def create_sip_auth_registrations_credential_list_mapping(account_sid: str, domain_sid: str, credential_list_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `domain_sid`, `credential_list_sid`
- **Params**: `account_sid` — path `AccountSid` · `domain_sid` — path `DomainSid` · `credential_list_sid` — form field `CredentialListSid`
- **Returns (parsed)**: `SipAuthRegistrationsCredentialListMapping`
- **Returns (raw)**: `ApiResult[SipAuthRegistrationsCredentialListMapping, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SipAuthRegistrationsCredentialListMapping` | `twilio/models/sip_auth_registrations_credential_list_mapping.py` |

### client.api20100401_auth_registrations_credential_list_mapping.delete_sip_auth_registrations_credential_list_mapping

- **Route**: `DELETE /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Registrations/CredentialListMappings/{Sid}.json`
- **Server**: `default`
- **Signature**: `def delete_sip_auth_registrations_credential_list_mapping(account_sid: str, domain_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `domain_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `domain_sid` — path `DomainSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.api20100401_auth_registrations_credential_list_mapping.fetch_sip_auth_registrations_credential_list_mapping

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Registrations/CredentialListMappings/{Sid}.json`
- **Server**: `default`
- **Signature**: `def fetch_sip_auth_registrations_credential_list_mapping(account_sid: str, domain_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `domain_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `domain_sid` — path `DomainSid` · `sid` — path `Sid`
- **Returns (parsed)**: `SipAuthRegistrationsCredentialListMapping`
- **Returns (raw)**: `ApiResult[SipAuthRegistrationsCredentialListMapping, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SipAuthRegistrationsCredentialListMapping` | `twilio/models/sip_auth_registrations_credential_list_mapping.py` |

### client.api20100401_auth_registrations_credential_list_mapping.list_sip_auth_registrations_credential_list_mapping

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Registrations/CredentialListMappings.json`
- **Server**: `default`
- **Signature**: `def list_sip_auth_registrations_credential_list_mapping(account_sid: str, domain_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `domain_sid`
- **Params**: `account_sid` — path `AccountSid` · `domain_sid` — path `DomainSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListSipAuthRegistrationsCredentialListMappingResponse`
- **Returns (raw)**: `ApiResult[ListSipAuthRegistrationsCredentialListMappingResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListSipAuthRegistrationsCredentialListMappingResponse` | `twilio/models/list_sip_auth_registrations_credential_list_mapping_response.py` |

