<!-- Generated file — do not edit; regenerated with the SDK. -->

# MessagingV1DomainConfigApi — operations

Accessor: `client.messaging_v1_domain_config_api` · Source: `twilio_sdk/apis/messaging_v1_domain_config_api.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.messaging_v1_domain_config_api.fetch_domain_config

- **Route**: `GET /v1/LinkShortening/Domains/{DomainSid}/Config`
- **Auth**: `account_sid_auth_token`
- **Server**: `default1`
- **Signature**: `def fetch_domain_config(domain_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `domain_sid`
- **Params**: `domain_sid` — path `DomainSid`
- **Returns (parsed)**: `MessagingV1DomainConfig`
- **Returns (raw)**: `ApiResult[MessagingV1DomainConfig, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MessagingV1DomainConfig` | `twilio_sdk/models/messaging_v1_domain_config.py` |

### client.messaging_v1_domain_config_api.update_domain_config

- **Route**: `POST /v1/LinkShortening/Domains/{DomainSid}/Config`
- **Auth**: `account_sid_auth_token`
- **Server**: `default1`
- **Signature**: `def update_domain_config(domain_sid: str, *, fallback_url: str | None = None, callback_url: str | None = None, continue_on_failure: bool | None = None, disable_https: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `domain_sid`
- **Params**: `domain_sid` — path `DomainSid` · `fallback_url` — form field `FallbackUrl` · `callback_url` — form field `CallbackUrl` · `continue_on_failure` — form field `ContinueOnFailure` · `disable_https` — form field `DisableHttps`
- **Returns (parsed)**: `MessagingV1DomainConfig`
- **Returns (raw)**: `ApiResult[MessagingV1DomainConfig, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MessagingV1DomainConfig` | `twilio_sdk/models/messaging_v1_domain_config.py` |

