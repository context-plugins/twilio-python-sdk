<!-- Generated file — do not edit; regenerated with the SDK. -->

# VerifyV2Notification — operations

Accessor: `client.verify_v2_notification` · Source: `twilio_sdk/apis/verify_v2_notification.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.verify_v2_notification.create_notification

- **Route**: `POST /v2/Services/{ServiceSid}/Entities/{Identity}/Challenges/{ChallengeSid}/Notifications`
- **Auth**: `account_sid_auth_token`
- **Server**: `default3`
- **Signature**: `def create_notification(service_sid: str, identity: str, challenge_sid: str, *, ttl: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `identity`, `challenge_sid`
- **Params**: `service_sid` — path `ServiceSid` · `identity` — path `Identity` · `challenge_sid` — path `ChallengeSid` · `ttl` — form field `Ttl`
- **Returns (parsed)**: `VerifyV2ServiceEntityChallengeNotification`
- **Returns (raw)**: `ApiResult[VerifyV2ServiceEntityChallengeNotification, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VerifyV2ServiceEntityChallengeNotification` | `twilio_sdk/models/verify_v2_service_entity_challenge_notification.py` |

