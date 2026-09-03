<!-- Generated file — do not edit; regenerated with the SDK. -->

# VerifyV2NewChallenge — operations

Accessor: `client.verify_v2_new_challenge` · Source: `twilio_sdk/apis/verify_v2_new_challenge.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.verify_v2_new_challenge.create_challenge_passkeys

- **Route**: `POST /v2/Services/{ServiceSid}/Passkeys/Challenges`
- **Auth**: `account_sid_auth_token`
- **Server**: `default3`
- **Signature**: `def create_challenge_passkeys(service_sid: str, body: CreatePasskeysChallengeRequest | CreatePasskeysChallengeRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `body`
- **Params**: `service_sid` — path `ServiceSid` · `body` — JSON body
- **Returns (parsed)**: `V2ServicesPasskeysChallengesResponse`
- **Returns (raw)**: `ApiResult[V2ServicesPasskeysChallengesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreatePasskeysChallengeRequest` | `twilio_sdk/models/create_passkeys_challenge_request.py` |
| `CreatePasskeysChallengeRequestDict` | `twilio_sdk/models/create_passkeys_challenge_request.py` |
| `V2ServicesPasskeysChallengesResponse` | `twilio_sdk/models/v2_services_passkeys_challenges_response.py` |

