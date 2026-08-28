<!-- Generated file — do not edit; regenerated with the SDK. -->

# MessagingV1ExternalCampaignApi — operations

Accessor: `client.messaging_v1_external_campaign_api` · Source: `twilio/apis/messaging_v1_external_campaign_api.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.messaging_v1_external_campaign_api.create_external_campaign

- **Route**: `POST /v1/Services/PreregisteredUsa2p`
- **Server**: `default1`
- **Signature**: `def create_external_campaign(campaign_id: str, messaging_service_sid: str, *, cnp_migration: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `campaign_id`, `messaging_service_sid`
- **Params**: `campaign_id` — form field `CampaignId` · `messaging_service_sid` — form field `MessagingServiceSid` · `cnp_migration` — form field `CnpMigration`
- **Returns (parsed)**: `MessagingV1ExternalCampaign`
- **Returns (raw)**: `ApiResult[MessagingV1ExternalCampaign, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MessagingV1ExternalCampaign` | `twilio/models/messaging_v1_external_campaign.py` |

