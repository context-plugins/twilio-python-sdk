<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401Message — operations

Accessor: `client.api20100401_message` · Source: `twilio/apis/api20100401_message.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.api20100401_message.create_message

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/Messages.json`
- **Server**: `default`
- **Signature**: `def create_message(account_sid: str, to: str, *, status_callback: str | None = None, application_sid: str | None = None, max_price: float | None = None, provide_feedback: bool | None = None, attempt: int | None = None, validity_period: int | None = None, force_delivery: bool | None = None, content_retention: MessageEnumContentRetentionOrStr | None = None, address_retention: MessageEnumAddressRetentionOrStr | None = None, smart_encoded: bool | None = None, persistent_action: list[str] | None = None, traffic_type: MessageEnumTrafficTypeOrStr | None = None, shorten_urls: bool | None = None, schedule_type: MessageEnumScheduleTypeOrStr | None = None, send_at: RFC3339DateTime | None = None, send_as_mms: bool | None = None, content_variables: str | None = None, risk_check: MessageEnumRiskCheckOrStr | None = None, from_: str | None = None, fallback_from: str | None = None, messaging_service_sid: str | None = None, body: str | None = None, media_url: list[str] | None = None, content_sid: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `to`
- **Params**: `account_sid` — path `AccountSid` · `to` — form field `To` · `status_callback` — form field `StatusCallback` · `application_sid` — form field `ApplicationSid` · `max_price` — form field `MaxPrice` · `provide_feedback` — form field `ProvideFeedback` · `attempt` — form field `Attempt` · `validity_period` — form field `ValidityPeriod` · `force_delivery` — form field `ForceDelivery` · `content_retention` — form field `ContentRetention` · `address_retention` — form field `AddressRetention` · `smart_encoded` — form field `SmartEncoded` · `persistent_action` — form field `PersistentAction` · `traffic_type` — form field `TrafficType` · `shorten_urls` — form field `ShortenUrls` · `schedule_type` — form field `ScheduleType` · `send_at` — form field `SendAt` · `send_as_mms` — form field `SendAsMms` · `content_variables` — form field `ContentVariables` · `risk_check` — form field `RiskCheck` · `from_` — form field `From` · `fallback_from` — form field `FallbackFrom` · `messaging_service_sid` — form field `MessagingServiceSid` · `body` — form field `Body` · `media_url` — form field `MediaUrl` · `content_sid` — form field `ContentSid`
- **Returns (parsed)**: `ApiV2010AccountMessage`
- **Returns (raw)**: `ApiResult[ApiV2010AccountMessage, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MessageEnumContentRetentionOrStr` | `twilio/models/enums/message_enum_content_retention.py` |
| `MessageEnumAddressRetentionOrStr` | `twilio/models/enums/message_enum_address_retention.py` |
| `MessageEnumTrafficTypeOrStr` | `twilio/models/enums/message_enum_traffic_type.py` |
| `MessageEnumScheduleTypeOrStr` | `twilio/models/enums/message_enum_schedule_type.py` |
| `MessageEnumRiskCheckOrStr` | `twilio/models/enums/message_enum_risk_check.py` |
| `ApiV2010AccountMessage` | `twilio/models/api_v2010_account_message.py` |

### client.api20100401_message.delete_message

- **Route**: `DELETE /2010-04-01/Accounts/{AccountSid}/Messages/{Sid}.json`
- **Server**: `default`
- **Signature**: `def delete_message(account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.api20100401_message.fetch_message

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/Messages/{Sid}.json`
- **Server**: `default`
- **Signature**: `def fetch_message(account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ApiV2010AccountMessage`
- **Returns (raw)**: `ApiResult[ApiV2010AccountMessage, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountMessage` | `twilio/models/api_v2010_account_message.py` |

### client.api20100401_message.list_message

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/Messages.json`
- **Server**: `default`
- **Signature**: `def list_message(account_sid: str, *, to: str | None = None, from_: str | None = None, date_sent: RFC3339DateTime | None = None, date_sent_query: RFC3339DateTime | None = None, date_sent_query_query: RFC3339DateTime | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`
- **Params**: `account_sid` — path `AccountSid` · `to` — query `To` · `from_` — query `From` · `date_sent` — query `DateSent` · `date_sent_query` — query `DateSent<` · `date_sent_query_query` — query `DateSent>` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListMessageResponse`
- **Returns (raw)**: `ApiResult[ListMessageResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListMessageResponse` | `twilio/models/list_message_response.py` |

### client.api20100401_message.update_message

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/Messages/{Sid}.json`
- **Server**: `default`
- **Signature**: `def update_message(account_sid: str, sid: str, *, body: str | None = None, status: MessageEnumUpdateStatusOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid` · `body` — form field `Body` · `status` — form field `Status`
- **Returns (parsed)**: `ApiV2010AccountMessage`
- **Returns (raw)**: `ApiResult[ApiV2010AccountMessage, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MessageEnumUpdateStatusOrStr` | `twilio/models/enums/message_enum_update_status.py` |
| `ApiV2010AccountMessage` | `twilio/models/api_v2010_account_message.py` |

