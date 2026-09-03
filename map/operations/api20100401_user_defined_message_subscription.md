<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401UserDefinedMessageSubscription — operations

Accessor: `client.api20100401_user_defined_message_subscription` · Source: `twilio_sdk/apis/api20100401_user_defined_message_subscription.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.api20100401_user_defined_message_subscription.create_user_defined_message_subscription

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/UserDefinedMessageSubscriptions.json`
- **Auth**: `account_sid_auth_token`
- **Server**: `default`
- **Signature**: `def create_user_defined_message_subscription(account_sid: str, call_sid: str, callback: str, *, idempotency_key: str | None = None, method: Method3OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `call_sid`, `callback`
- **Params**: `account_sid` — path `AccountSid` · `call_sid` — path `CallSid` · `callback` — form field `Callback` · `idempotency_key` — form field `IdempotencyKey` · `method` — form field `Method`
- **Returns (parsed)**: `ApiV2010AccountCallUserDefinedMessageSubscription`
- **Returns (raw)**: `ApiResult[ApiV2010AccountCallUserDefinedMessageSubscription, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Method3OrStr` | `twilio_sdk/models/enums/method3.py` |
| `ApiV2010AccountCallUserDefinedMessageSubscription` | `twilio_sdk/models/api_v2010_account_call_user_defined_message_subscription.py` |

### client.api20100401_user_defined_message_subscription.delete_user_defined_message_subscription

- **Route**: `DELETE /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/UserDefinedMessageSubscriptions/{Sid}.json`
- **Auth**: `account_sid_auth_token`
- **Server**: `default`
- **Signature**: `def delete_user_defined_message_subscription(account_sid: str, call_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `call_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `call_sid` — path `CallSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

