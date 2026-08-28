<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401ValidationRequest — operations

Accessor: `client.api20100401_validation_request` · Source: `twilio_sdk/apis/api20100401_validation_request.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.api20100401_validation_request.create_validation_request

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/OutgoingCallerIds.json`
- **Server**: `default`
- **Signature**: `def create_validation_request(account_sid: str, phone_number: str, *, friendly_name: str | None = None, call_delay: int | None = None, extension: str | None = None, status_callback: AnyUrl | None = None, status_callback_method: StatusCallbackMethod15OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `phone_number`
- **Params**: `account_sid` — path `AccountSid` · `phone_number` — form field `PhoneNumber` · `friendly_name` — form field `FriendlyName` · `call_delay` — form field `CallDelay` · `extension` — form field `Extension` · `status_callback` — form field `StatusCallback` · `status_callback_method` — form field `StatusCallbackMethod`
- **Returns (parsed)**: `ApiV2010AccountValidationRequest`
- **Returns (raw)**: `ApiResult[ApiV2010AccountValidationRequest, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StatusCallbackMethod15OrStr` | `twilio_sdk/models/enums/status_callback_method15.py` |
| `ApiV2010AccountValidationRequest` | `twilio_sdk/models/api_v2010_account_validation_request.py` |

