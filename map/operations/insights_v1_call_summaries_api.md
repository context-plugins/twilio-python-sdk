<!-- Generated file — do not edit; regenerated with the SDK. -->

# InsightsV1CallSummariesApi — operations

Accessor: `client.insights_v1_call_summaries_api` · Source: `twilio/apis/insights_v1_call_summaries_api.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.insights_v1_call_summaries_api.list_call_summaries

- **Route**: `GET /v1/Voice/Summaries`
- **Server**: `default14`
- **Signature**: `def list_call_summaries(*, from_: str | None = None, to: str | None = None, from_carrier: str | None = None, to_carrier: str | None = None, from_country_code: str | None = None, to_country_code: str | None = None, verified_caller: bool | None = None, has_tag: bool | None = None, start_time: str | None = None, end_time: str | None = None, call_type: str | None = None, call_state: str | None = None, direction: str | None = None, processing_state: CallSummariesEnumProcessingStateRequestOrStr | None = None, sort_by: CallSummariesEnumSortByOrStr | None = None, subaccount: str | None = None, abnormal_session: bool | None = None, answered_by: CallSummariesEnumAnsweredByOrStr | None = None, answered_by_annotation: str | None = None, connectivity_issue_annotation: str | None = None, quality_issue_annotation: str | None = None, spam_annotation: bool | None = None, call_score_annotation: str | None = None, branded_enabled: bool | None = None, voice_integrity_enabled: bool | None = None, branded_bundle_sid: str | None = None, branded_logo: bool | None = None, branded_type: str | None = None, branded_use_case: str | None = None, branded_call_reason: str | None = None, voice_integrity_bundle_sid: str | None = None, voice_integrity_use_case: str | None = None, business_profile_identity: str | None = None, business_profile_industry: str | None = None, business_profile_bundle_sid: str | None = None, business_profile_type: str | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `from_` — query `From` · `to` — query `To` · `from_carrier` — query `FromCarrier` · `to_carrier` — query `ToCarrier` · `from_country_code` — query `FromCountryCode` · `to_country_code` — query `ToCountryCode` · `verified_caller` — query `VerifiedCaller` · `has_tag` — query `HasTag` · `start_time` — query `StartTime` · `end_time` — query `EndTime` · `call_type` — query `CallType` · `call_state` — query `CallState` · `direction` — query `Direction` · `processing_state` — query `ProcessingState` · `sort_by` — query `SortBy` · `subaccount` — query `Subaccount` · `abnormal_session` — query `AbnormalSession` · `answered_by` — query `AnsweredBy` · `answered_by_annotation` — query `AnsweredByAnnotation` · `connectivity_issue_annotation` — query `ConnectivityIssueAnnotation` · `quality_issue_annotation` — query `QualityIssueAnnotation` · `spam_annotation` — query `SpamAnnotation` · `call_score_annotation` — query `CallScoreAnnotation` · `branded_enabled` — query `BrandedEnabled` · `voice_integrity_enabled` — query `VoiceIntegrityEnabled` · `branded_bundle_sid` — query `BrandedBundleSid` · `branded_logo` — query `BrandedLogo` · `branded_type` — query `BrandedType` · `branded_use_case` — query `BrandedUseCase` · `branded_call_reason` — query `BrandedCallReason` · `voice_integrity_bundle_sid` — query `VoiceIntegrityBundleSid` · `voice_integrity_use_case` — query `VoiceIntegrityUseCase` · `business_profile_identity` — query `BusinessProfileIdentity` · `business_profile_industry` — query `BusinessProfileIndustry` · `business_profile_bundle_sid` — query `BusinessProfileBundleSid` · `business_profile_type` — query `BusinessProfileType` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListCallSummariesResponse`
- **Returns (raw)**: `ApiResult[ListCallSummariesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CallSummariesEnumProcessingStateRequestOrStr` | `twilio/models/enums/call_summaries_enum_processing_state_request.py` |
| `CallSummariesEnumSortByOrStr` | `twilio/models/enums/call_summaries_enum_sort_by.py` |
| `CallSummariesEnumAnsweredByOrStr` | `twilio/models/enums/call_summaries_enum_answered_by.py` |
| `ListCallSummariesResponse` | `twilio/models/list_call_summaries_response.py` |

