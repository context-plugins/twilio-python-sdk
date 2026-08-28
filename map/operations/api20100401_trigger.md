<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401Trigger — operations

Accessor: `client.api20100401_trigger` · Source: `twilio/apis/api20100401_trigger.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.api20100401_trigger.create_usage_trigger

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/Usage/Triggers.json`
- **Server**: `default`
- **Signature**: `def create_usage_trigger(account_sid: str, callback_url: str, trigger_value: str, usage_category: str, *, callback_method: CallbackMethod1OrStr | None = None, friendly_name: str | None = None, recurring: UsageTriggerEnumRecurringOrStr | None = None, trigger_by: UsageTriggerEnumTriggerFieldOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `callback_url`, `trigger_value`, `usage_category`
- **Params**: `account_sid` — path `AccountSid` · `callback_url` — form field `CallbackUrl` · `trigger_value` — form field `TriggerValue` · `usage_category` — form field `UsageCategory` · `callback_method` — form field `CallbackMethod` · `friendly_name` — form field `FriendlyName` · `recurring` — form field `Recurring` · `trigger_by` — form field `TriggerBy`
- **Returns (parsed)**: `ApiV2010AccountUsageUsageTrigger`
- **Returns (raw)**: `ApiResult[ApiV2010AccountUsageUsageTrigger, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CallbackMethod1OrStr` | `twilio/models/enums/callback_method1.py` |
| `UsageTriggerEnumRecurringOrStr` | `twilio/models/enums/usage_trigger_enum_recurring.py` |
| `UsageTriggerEnumTriggerFieldOrStr` | `twilio/models/enums/usage_trigger_enum_trigger_field.py` |
| `ApiV2010AccountUsageUsageTrigger` | `twilio/models/api_v2010_account_usage_usage_trigger.py` |

### client.api20100401_trigger.delete_usage_trigger

- **Route**: `DELETE /2010-04-01/Accounts/{AccountSid}/Usage/Triggers/{Sid}.json`
- **Server**: `default`
- **Signature**: `def delete_usage_trigger(account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.api20100401_trigger.fetch_usage_trigger

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/Usage/Triggers/{Sid}.json`
- **Server**: `default`
- **Signature**: `def fetch_usage_trigger(account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ApiV2010AccountUsageUsageTrigger`
- **Returns (raw)**: `ApiResult[ApiV2010AccountUsageUsageTrigger, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountUsageUsageTrigger` | `twilio/models/api_v2010_account_usage_usage_trigger.py` |

### client.api20100401_trigger.list_usage_trigger

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/Usage/Triggers.json`
- **Server**: `default`
- **Signature**: `def list_usage_trigger(account_sid: str, *, recurring: UsageTriggerEnumRecurringOrStr | None = None, trigger_by: UsageTriggerEnumTriggerFieldOrStr | None = None, usage_category: str | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`
- **Params**: `account_sid` — path `AccountSid` · `recurring` — query `Recurring` · `trigger_by` — query `TriggerBy` · `usage_category` — query `UsageCategory` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListUsageTriggerResponse`
- **Returns (raw)**: `ApiResult[ListUsageTriggerResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UsageTriggerEnumRecurringOrStr` | `twilio/models/enums/usage_trigger_enum_recurring.py` |
| `UsageTriggerEnumTriggerFieldOrStr` | `twilio/models/enums/usage_trigger_enum_trigger_field.py` |
| `ListUsageTriggerResponse` | `twilio/models/list_usage_trigger_response.py` |

### client.api20100401_trigger.update_usage_trigger

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/Usage/Triggers/{Sid}.json`
- **Server**: `default`
- **Signature**: `def update_usage_trigger(account_sid: str, sid: str, *, callback_method: CallbackMethod1OrStr | None = None, callback_url: str | None = None, friendly_name: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid` · `callback_method` — form field `CallbackMethod` · `callback_url` — form field `CallbackUrl` · `friendly_name` — form field `FriendlyName`
- **Returns (parsed)**: `ApiV2010AccountUsageUsageTrigger`
- **Returns (raw)**: `ApiResult[ApiV2010AccountUsageUsageTrigger, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CallbackMethod1OrStr` | `twilio/models/enums/callback_method1.py` |
| `ApiV2010AccountUsageUsageTrigger` | `twilio/models/api_v2010_account_usage_usage_trigger.py` |

