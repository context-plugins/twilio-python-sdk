<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401UserDefinedMessage — operations

Accessor: `client.api20100401_user_defined_message` · Source: `twilio/apis/api20100401_user_defined_message.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.api20100401_user_defined_message.create_user_defined_message

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/UserDefinedMessages.json`
- **Server**: `default`
- **Signature**: `def create_user_defined_message(account_sid: str, call_sid: str, content: str, *, idempotency_key: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `call_sid`, `content`
- **Params**: `account_sid` — path `AccountSid` · `call_sid` — path `CallSid` · `content` — form field `Content` · `idempotency_key` — form field `IdempotencyKey`
- **Returns (parsed)**: `ApiV2010AccountCallUserDefinedMessage`
- **Returns (raw)**: `ApiResult[ApiV2010AccountCallUserDefinedMessage, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountCallUserDefinedMessage` | `twilio/models/api_v2010_account_call_user_defined_message.py` |

