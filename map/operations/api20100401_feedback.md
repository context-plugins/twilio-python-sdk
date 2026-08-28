<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401Feedback — operations

Accessor: `client.api20100401_feedback` · Source: `twilio_sdk/apis/api20100401_feedback.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.api20100401_feedback.create_message_feedback

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/Messages/{MessageSid}/Feedback.json`
- **Server**: `default`
- **Signature**: `def create_message_feedback(account_sid: str, message_sid: str, *, outcome: MessageFeedbackEnumOutcomeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `message_sid`
- **Params**: `account_sid` — path `AccountSid` · `message_sid` — path `MessageSid` · `outcome` — form field `Outcome`
- **Returns (parsed)**: `ApiV2010AccountMessageMessageFeedback`
- **Returns (raw)**: `ApiResult[ApiV2010AccountMessageMessageFeedback, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MessageFeedbackEnumOutcomeOrStr` | `twilio_sdk/models/enums/message_feedback_enum_outcome.py` |
| `ApiV2010AccountMessageMessageFeedback` | `twilio_sdk/models/api_v2010_account_message_message_feedback.py` |

