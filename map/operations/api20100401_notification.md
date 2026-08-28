<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401Notification — operations

Accessor: `client.api20100401_notification` · Source: `twilio/apis/api20100401_notification.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.api20100401_notification.fetch_notification

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/Notifications/{Sid}.json`
- **Server**: `default`
- **Signature**: `def fetch_notification(account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ApiV2010AccountNotificationInstance`
- **Returns (raw)**: `ApiResult[ApiV2010AccountNotificationInstance, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountNotificationInstance` | `twilio/models/api_v2010_account_notification_instance.py` |

### client.api20100401_notification.list_notification

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/Notifications.json`
- **Server**: `default`
- **Signature**: `def list_notification(account_sid: str, *, log: int | None = None, message_date: Date | None = None, message_date_query: Date | None = None, message_date_query_query: Date | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`
- **Params**: `account_sid` — path `AccountSid` · `log` — query `Log` · `message_date` — query `MessageDate` · `message_date_query` — query `MessageDate<` · `message_date_query_query` — query `MessageDate>` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListNotificationResponse`
- **Returns (raw)**: `ApiResult[ListNotificationResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListNotificationResponse` | `twilio/models/list_notification_response.py` |

