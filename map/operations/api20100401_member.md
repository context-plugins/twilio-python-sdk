<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401Member — operations

Accessor: `client.api20100401_member` · Source: `twilio/apis/api20100401_member.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.api20100401_member.fetch_member

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/Queues/{QueueSid}/Members/{CallSid}.json`
- **Server**: `default`
- **Signature**: `def fetch_member(account_sid: str, queue_sid: str, call_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `queue_sid`, `call_sid`
- **Params**: `account_sid` — path `AccountSid` · `queue_sid` — path `QueueSid` · `call_sid` — path `CallSid`
- **Returns (parsed)**: `ApiV2010AccountQueueMember`
- **Returns (raw)**: `ApiResult[ApiV2010AccountQueueMember, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountQueueMember` | `twilio/models/api_v2010_account_queue_member.py` |

### client.api20100401_member.list_member

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/Queues/{QueueSid}/Members.json`
- **Server**: `default`
- **Signature**: `def list_member(account_sid: str, queue_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `queue_sid`
- **Params**: `account_sid` — path `AccountSid` · `queue_sid` — path `QueueSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListMemberResponse`
- **Returns (raw)**: `ApiResult[ListMemberResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListMemberResponse` | `twilio/models/list_member_response.py` |

### client.api20100401_member.update_member

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/Queues/{QueueSid}/Members/{CallSid}.json`
- **Server**: `default`
- **Signature**: `def update_member(account_sid: str, queue_sid: str, call_sid: str, url: str, *, method: Method2OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `queue_sid`, `call_sid`, `url`
- **Params**: `account_sid` — path `AccountSid` · `queue_sid` — path `QueueSid` · `call_sid` — path `CallSid` · `url` — form field `Url` · `method` — form field `Method`
- **Returns (parsed)**: `ApiV2010AccountQueueMember`
- **Returns (raw)**: `ApiResult[ApiV2010AccountQueueMember, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Method2OrStr` | `twilio/models/enums/method2.py` |
| `ApiV2010AccountQueueMember` | `twilio/models/api_v2010_account_queue_member.py` |

