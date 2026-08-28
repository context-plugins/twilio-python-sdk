<!-- Generated file — do not edit; regenerated with the SDK. -->

# SDK map — Twilio SDK (Python)

> A generated table of contents for this SDK. Consult this map and its sub-pages to learn signatures, error types, and server/auth wiring **by lookup**. Model shapes and enum values are *not* duplicated here — the map names the module declaring each type; read the shape there. Every name is the emitted spelling, so a wrong one fails at import rather than working silently.

|  |  |
| --- | --- |
| SDK display name | Twilio SDK |
| Root package | `twilio_sdk` |
| Distribution name | `twilio-sdk` |
| Requires | Python 3.10 or later |
| API spec version | `1.0.0` |
| Generator | APIMatic |

Staleness check: the API spec version above changes when the SDK is regenerated from a new spec, and the package version is what `pip show` reports for the installed SDK. If a lookup here fails at import, re-read the module named in the row.

All `Source` paths on this map and its sub-pages are relative to the **SDK root** — the directory holding this file and `pyproject.toml` — never to the page that carries them. Open them as-is from the SDK root; if the SDK sits under a subdirectory of a larger repo, prefix that subdirectory.

---

## Getting a client

### Synchronous client

```python
from twilio_sdk import TwilioSdkClient
from twilio_sdk.core import BasicAuthCredentials

client = TwilioSdkClient(
    account_sid_auth_token=BasicAuthCredentials(username="YOUR_USERNAME", password="YOUR_PASSWORD")
)

# TODO: call endpoints here -- see api-reference.md

client.close()
```

Alternatively, scope it — `with TwilioSdkClient(...) as client:` closes the pool on exit.

### Asynchronous client

```python
from asyncio import run

from twilio_sdk import AsyncTwilioSdkClient
from twilio_sdk.core import BasicAuthCredentials


async def main() -> None:
    client = AsyncTwilioSdkClient(
        account_sid_auth_token=BasicAuthCredentials(username="YOUR_USERNAME", password="YOUR_PASSWORD")
    )
    # TODO: call endpoints here, awaiting each -- see api-reference.md
    await client.aclose()


run(main())
```

Alternatively, scope it — `async with AsyncTwilioSdkClient(...) as client:` closes the pool on exit.

`AsyncClient` (`twilio_sdk/async_client.py`) mirrors `Client` method for method, each endpoint method a coroutine. It takes the same keywords, except that each client accepts only its own transport and — where the **Async Type** column differs — only its own flavor.

`Client` and `AsyncClient` are aliases of `TwilioSdkClient` and `AsyncTwilioSdkClient` — the names tracebacks and `repr()` show; all four import from the root.

`close()` / `aclose()` closes the transport even when you supplied one via `custom_http_client=` / `custom_async_http_client=`, and a closed client cannot be reused.

Every API group is a property on the client (e.g. `client.api20100401_account`). Every constructor argument is optional and keyword-only. Sources: `twilio_sdk/client.py`, `twilio_sdk/async_client.py`:

| Keyword | Sync Type | Async Type | Default |
| --- | --- | --- | --- |
| `server_config` | `ServerConfigOrDict \| None` | `ServerConfigOrDict \| None` | `None` |
| `timeout` | `float` | `float` | `30.0` seconds |
| `custom_http_client` | `HttpClient \| None` | — | `None` |
| `custom_async_http_client` | — | `AsyncHttpClient \| None` | `None` |
| `account_sid_auth_token` | `BasicAuthCredentialsOrDict \| None` | `BasicAuthCredentialsOrDict \| None` | `None` |

The types those columns name — where each imports from and, for a credentials dict, its keys:

| Type | Import from | Shape |
| --- | --- | --- |
| `ServerConfigOrDict` | `twilio_sdk.server` | keys as the Servers & auth tables read |
| `HttpClient` | `twilio_sdk.core` | protocol — `send(request: HttpRequest) -> HttpResponse` · `close()` |
| `BasicAuthCredentialsOrDict` | `twilio_sdk.core` | `BasicAuthCredentials` or a dict: `username: str` · `password: str` |
| `AsyncHttpClient` | `twilio_sdk.core` | protocol — `async send(request: HttpRequest) -> HttpResponse` · `async aclose()` |

---

## Error-handling model (read once — applies to every operation)

Every operation is reached in two response modes:

- **Parsed call.** Returns the decoded payload and raises `ApiError` on an error status, with the decoded body on `.error` and the status on `.status_code`.
- **Raw call.** Reached through `.with_raw_response`; returns `ApiResult` — `Success` or `Failure` — and never raises for an API error. Read `.payload` on a `Success` or `.error` on a `Failure`; both carry `.response`.

What `.error` holds is fixed per operation. There are two cases:

- **Case A — typed error.** The operation documents at least one error status, so `twilio_sdk/errors/` declares a union alias over the bodies those statuses map to — `RawError` is always its last arm, for any undocumented status — and `.error` is annotated with that alias. Narrow it with `isinstance`. The operation blocks name the alias and the status each arm maps from.
- **Case B — raw error.** The operation documents no error status; `.error` is `RawError` (`twilio_sdk/core/results.py`): `status_code: int` · `content: bytes` · `text(encoding="utf-8"): str` · `json(): Any` · `response: HttpResponse`.

Core runtime types (`twilio_sdk/core/`) — public members with their **declared types**, verbatim from source:

| Type | Public members | Source |
| --- | --- | --- |
| `ApiError` — raised by every parsed call; `.error` is a Case A alias from `twilio_sdk/errors/` or `RawError` | `error: E` · `status_code: int` · `response: HttpResponse` | `twilio_sdk/core/exceptions.py` |
| `ApiResult[T, E]` — returned by every raw call; the `Success[T] \| Failure[E]` union | `payload: T` (on `Success`) · `error: E` (on `Failure`) · `response: HttpResponse` (on both) | `twilio_sdk/core/results.py` |
| `RawError` | `status_code: int` · `content: bytes` · `text(encoding="utf-8"): str` · `json(): Any` · `response: HttpResponse` | `twilio_sdk/core/results.py` |

Typed error bodies (the arms of a Case A alias) are ordinary models — no special handling. The operation's **Type sources** table gives the module that declares each one; read field names, declared types and JSON aliases there, as for any other model.

```python
from twilio_sdk.core import ApiError, RawError
from twilio_sdk.models import AccountsCallsRecordingsSidJson201041408Error1

try:
    response = client.create_lookup_phone_number_overrides(field, phone_number)
except ApiError as e:
    # Case A — typed error: e.error is CreateLookupPhoneNumberOverridesErrorBody
    if isinstance(e.error, AccountsCallsRecordingsSidJson201041408Error1):
        # Handle 400
        print(e.error)
    if isinstance(e.error, RawError):
        # Any other error status
        print(e.status_code, e.error.text())
```

**Raw (`.with_raw_response`) variants: present on every operation** — the same call returns `ApiResult` instead of raising, with the same body on `Failure.error`. Of **898 operations**, **37 are Case A (typed)** and **861 are Case B (raw)**.

---

## Operations — by controller (319 pages, 898 operations)

Each links to a sub-page with one block per operation, headed by its full accessor path: the HTTP verb and route (for a mock, a raw request or a provider-side log — never reconstruct it from the method name), the sync parsed signature with its required positional parameters, each parameter's role and — where it differs — wire name, both return types, and its error case — **Case A** names the alias and the status each arm maps from, **Case B** names `RawError`. Every block also carries a **Type sources** table — every type it names, with the module that declares it.

**Each block states what is specific to its operation. Everything below holds for every operation, and blocks never restate it — silence means the default applies.**

| Applies to every operation | Stated where |
| --- | --- |
| **Four spellings, one signature** — the same method name and parameters on `Client` and `AsyncClient`, each also reachable through `.with_raw_response`; the async twin is a coroutine to `await`, with the same return types and error case, and where the **Async Type** column differs, pass the type it names | Getting a client |
| **Parsed raises, raw returns** — `ApiError` versus `ApiResult` | Error-handling model |
| **Case B error is always `RawError`** — also the last arm of every Case A alias, where a block's **Error arms** bullet ends in it | Error-handling model |
| **A trailing `request_options`** — keyword-only and optional, for per-call overrides such as a timeout or extra headers; every signature ends with it | here (`twilio_sdk/core/request_options.py`) |
| **Each operation names its own server** — this SDK declares several, so every block carries a **Server** bullet with the server's key in `server_config=` | its block |
| **Parameter names are literal** — signatures are generated code verbatim, and everything behind the bare `*` must be passed by name | here |
| **A parameter's wire name is its Python name** — sent as-is on the path, query string, header or body, unless the block's **Params** bullet carries a wire name beside the role | here |

**The operation's behavioural prose lives on the operation itself**, as the method's docstring in the module named at the top of its page, and again in `api-reference.md` with a per-parameter description and a usage sample. Blocks here give you the contract — names, types, shapes, errors. Where an operation's *semantics* decide what you must pass, that is what the docstring settles; read it there rather than filling it in from memory.

Sub-pages chunk per `###` block: each block is self-contained given the table above, and assumes this page is loaded beside it.

| Controller | Ops | Page |
| --- | --- | --- |
| `client` (root) | 11 | [map/operations/client.md](map/operations/client.md) |
| `client.api20100401_account` | 4 | [map/operations/api20100401_account.md](map/operations/api20100401_account.md) |
| `client.api20100401_add_on_result` | 3 | [map/operations/api20100401_add_on_result.md](map/operations/api20100401_add_on_result.md) |
| `client.api20100401_address` | 5 | [map/operations/api20100401_address.md](map/operations/api20100401_address.md) |
| `client.api20100401_all_time` | 1 | [map/operations/api20100401_all_time.md](map/operations/api20100401_all_time.md) |
| `client.api20100401_application` | 5 | [map/operations/api20100401_application.md](map/operations/api20100401_application.md) |
| `client.api20100401_assigned_add_on` | 4 | [map/operations/api20100401_assigned_add_on.md](map/operations/api20100401_assigned_add_on.md) |
| `client.api20100401_assigned_add_on_extension` | 2 | [map/operations/api20100401_assigned_add_on_extension.md](map/operations/api20100401_assigned_add_on_extension.md) |
| `client.api20100401_auth_calls_credential_list_mapping` | 4 | [map/operations/api20100401_auth_calls_credential_list_mapping.md](map/operations/api20100401_auth_calls_credential_list_mapping.md) |
| `client.api20100401_auth_calls_ip_access_control_list_mapping` | 4 | [map/operations/api20100401_auth_calls_ip_access_control_list_mapping.md](map/operations/api20100401_auth_calls_ip_access_control_list_mapping.md) |
| `client.api20100401_auth_registrations_credential_list_mapping` | 4 | [map/operations/api20100401_auth_registrations_credential_list_mapping.md](map/operations/api20100401_auth_registrations_credential_list_mapping.md) |
| `client.api20100401_authorized_connect_app` | 2 | [map/operations/api20100401_authorized_connect_app.md](map/operations/api20100401_authorized_connect_app.md) |
| `client.api20100401_available_phone_number_country` | 2 | [map/operations/api20100401_available_phone_number_country.md](map/operations/api20100401_available_phone_number_country.md) |
| `client.api20100401_balance` | 1 | [map/operations/api20100401_balance.md](map/operations/api20100401_balance.md) |
| `client.api20100401_call` | 5 | [map/operations/api20100401_call.md](map/operations/api20100401_call.md) |
| `client.api20100401_call_notification` | 2 | [map/operations/api20100401_call_notification.md](map/operations/api20100401_call_notification.md) |
| `client.api20100401_call_recording` | 5 | [map/operations/api20100401_call_recording.md](map/operations/api20100401_call_recording.md) |
| `client.api20100401_call_transcription` | 2 | [map/operations/api20100401_call_transcription.md](map/operations/api20100401_call_transcription.md) |
| `client.api20100401_conference` | 3 | [map/operations/api20100401_conference.md](map/operations/api20100401_conference.md) |
| `client.api20100401_conference_recording` | 4 | [map/operations/api20100401_conference_recording.md](map/operations/api20100401_conference_recording.md) |
| `client.api20100401_connect_app` | 4 | [map/operations/api20100401_connect_app.md](map/operations/api20100401_connect_app.md) |
| `client.api20100401_credential` | 5 | [map/operations/api20100401_credential.md](map/operations/api20100401_credential.md) |
| `client.api20100401_credential_list` | 5 | [map/operations/api20100401_credential_list.md](map/operations/api20100401_credential_list.md) |
| `client.api20100401_credential_list_mapping` | 4 | [map/operations/api20100401_credential_list_mapping.md](map/operations/api20100401_credential_list_mapping.md) |
| `client.api20100401_daily` | 1 | [map/operations/api20100401_daily.md](map/operations/api20100401_daily.md) |
| `client.api20100401_data` | 1 | [map/operations/api20100401_data.md](map/operations/api20100401_data.md) |
| `client.api20100401_dependent_phone_number` | 1 | [map/operations/api20100401_dependent_phone_number.md](map/operations/api20100401_dependent_phone_number.md) |
| `client.api20100401_domain` | 5 | [map/operations/api20100401_domain.md](map/operations/api20100401_domain.md) |
| `client.api20100401_event` | 1 | [map/operations/api20100401_event.md](map/operations/api20100401_event.md) |
| `client.api20100401_feedback` | 1 | [map/operations/api20100401_feedback.md](map/operations/api20100401_feedback.md) |
| `client.api20100401_incoming_phone_number` | 5 | [map/operations/api20100401_incoming_phone_number.md](map/operations/api20100401_incoming_phone_number.md) |
| `client.api20100401_incoming_phone_number_local` | 2 | [map/operations/api20100401_incoming_phone_number_local.md](map/operations/api20100401_incoming_phone_number_local.md) |
| `client.api20100401_incoming_phone_number_mobile` | 2 | [map/operations/api20100401_incoming_phone_number_mobile.md](map/operations/api20100401_incoming_phone_number_mobile.md) |
| `client.api20100401_incoming_phone_number_toll_free` | 2 | [map/operations/api20100401_incoming_phone_number_toll_free.md](map/operations/api20100401_incoming_phone_number_toll_free.md) |
| `client.api20100401_ip_access_control_list` | 5 | [map/operations/api20100401_ip_access_control_list.md](map/operations/api20100401_ip_access_control_list.md) |
| `client.api20100401_ip_access_control_list_mapping` | 4 | [map/operations/api20100401_ip_access_control_list_mapping.md](map/operations/api20100401_ip_access_control_list_mapping.md) |
| `client.api20100401_key` | 4 | [map/operations/api20100401_key.md](map/operations/api20100401_key.md) |
| `client.api20100401_last_month` | 1 | [map/operations/api20100401_last_month.md](map/operations/api20100401_last_month.md) |
| `client.api20100401_local` | 1 | [map/operations/api20100401_local.md](map/operations/api20100401_local.md) |
| `client.api20100401_machine_to_machine` | 1 | [map/operations/api20100401_machine_to_machine.md](map/operations/api20100401_machine_to_machine.md) |
| `client.api20100401_media` | 1 | [map/operations/api20100401_media.md](map/operations/api20100401_media.md) |
| `client.api20100401_media_instance` | 2 | [map/operations/api20100401_media_instance.md](map/operations/api20100401_media_instance.md) |
| `client.api20100401_member` | 3 | [map/operations/api20100401_member.md](map/operations/api20100401_member.md) |
| `client.api20100401_message` | 5 | [map/operations/api20100401_message.md](map/operations/api20100401_message.md) |
| `client.api20100401_mobile` | 1 | [map/operations/api20100401_mobile.md](map/operations/api20100401_mobile.md) |
| `client.api20100401_monthly` | 1 | [map/operations/api20100401_monthly.md](map/operations/api20100401_monthly.md) |
| `client.api20100401_national` | 1 | [map/operations/api20100401_national.md](map/operations/api20100401_national.md) |
| `client.api20100401_new_key` | 1 | [map/operations/api20100401_new_key.md](map/operations/api20100401_new_key.md) |
| `client.api20100401_new_signing_key` | 1 | [map/operations/api20100401_new_signing_key.md](map/operations/api20100401_new_signing_key.md) |
| `client.api20100401_notification` | 2 | [map/operations/api20100401_notification.md](map/operations/api20100401_notification.md) |
| `client.api20100401_outgoing_caller_id` | 4 | [map/operations/api20100401_outgoing_caller_id.md](map/operations/api20100401_outgoing_caller_id.md) |
| `client.api20100401_participant` | 5 | [map/operations/api20100401_participant.md](map/operations/api20100401_participant.md) |
| `client.api20100401_payload` | 3 | [map/operations/api20100401_payload.md](map/operations/api20100401_payload.md) |
| `client.api20100401_payment` | 2 | [map/operations/api20100401_payment.md](map/operations/api20100401_payment.md) |
| `client.api20100401_queue` | 5 | [map/operations/api20100401_queue.md](map/operations/api20100401_queue.md) |
| `client.api20100401_record` | 1 | [map/operations/api20100401_record.md](map/operations/api20100401_record.md) |
| `client.api20100401_recording` | 3 | [map/operations/api20100401_recording.md](map/operations/api20100401_recording.md) |
| `client.api20100401_recording_transcription` | 3 | [map/operations/api20100401_recording_transcription.md](map/operations/api20100401_recording_transcription.md) |
| `client.api20100401_shared_cost` | 1 | [map/operations/api20100401_shared_cost.md](map/operations/api20100401_shared_cost.md) |
| `client.api20100401_short_code` | 3 | [map/operations/api20100401_short_code.md](map/operations/api20100401_short_code.md) |
| `client.api20100401_signing_key` | 4 | [map/operations/api20100401_signing_key.md](map/operations/api20100401_signing_key.md) |
| `client.api20100401_sip_ip_address` | 5 | [map/operations/api20100401_sip_ip_address.md](map/operations/api20100401_sip_ip_address.md) |
| `client.api20100401_siprec` | 2 | [map/operations/api20100401_siprec.md](map/operations/api20100401_siprec.md) |
| `client.api20100401_stream` | 2 | [map/operations/api20100401_stream.md](map/operations/api20100401_stream.md) |
| `client.api20100401_this_month` | 1 | [map/operations/api20100401_this_month.md](map/operations/api20100401_this_month.md) |
| `client.api20100401_today` | 1 | [map/operations/api20100401_today.md](map/operations/api20100401_today.md) |
| `client.api20100401_token` | 1 | [map/operations/api20100401_token.md](map/operations/api20100401_token.md) |
| `client.api20100401_toll_free` | 1 | [map/operations/api20100401_toll_free.md](map/operations/api20100401_toll_free.md) |
| `client.api20100401_transcription` | 3 | [map/operations/api20100401_transcription.md](map/operations/api20100401_transcription.md) |
| `client.api20100401_trigger` | 5 | [map/operations/api20100401_trigger.md](map/operations/api20100401_trigger.md) |
| `client.api20100401_user_defined_message` | 1 | [map/operations/api20100401_user_defined_message.md](map/operations/api20100401_user_defined_message.md) |
| `client.api20100401_user_defined_message_subscription` | 2 | [map/operations/api20100401_user_defined_message_subscription.md](map/operations/api20100401_user_defined_message_subscription.md) |
| `client.api20100401_validation_request` | 1 | [map/operations/api20100401_validation_request.md](map/operations/api20100401_validation_request.md) |
| `client.api20100401_voip` | 1 | [map/operations/api20100401_voip.md](map/operations/api20100401_voip.md) |
| `client.api20100401_yearly` | 1 | [map/operations/api20100401_yearly.md](map/operations/api20100401_yearly.md) |
| `client.api20100401_yesterday` | 1 | [map/operations/api20100401_yesterday.md](map/operations/api20100401_yesterday.md) |
| `client.content_v2_content` | 1 | [map/operations/content_v2_content.md](map/operations/content_v2_content.md) |
| `client.content_v2_content_and_approvals` | 1 | [map/operations/content_v2_content_and_approvals.md](map/operations/content_v2_content_and_approvals.md) |
| `client.contentv1_approval_create` | 1 | [map/operations/contentv1_approval_create.md](map/operations/contentv1_approval_create.md) |
| `client.contentv1_approval_fetch` | 1 | [map/operations/contentv1_approval_fetch.md](map/operations/contentv1_approval_fetch.md) |
| `client.contentv1_content_api` | 5 | [map/operations/contentv1_content_api.md](map/operations/contentv1_content_api.md) |
| `client.contentv1_content_and_approvals_api` | 1 | [map/operations/contentv1_content_and_approvals_api.md](map/operations/contentv1_content_and_approvals_api.md) |
| `client.contentv1_legacy_content_api` | 1 | [map/operations/contentv1_legacy_content_api.md](map/operations/contentv1_legacy_content_api.md) |
| `client.conversations_v1_address_configuration` | 5 | [map/operations/conversations_v1_address_configuration.md](map/operations/conversations_v1_address_configuration.md) |
| `client.conversations_v1_binding` | 3 | [map/operations/conversations_v1_binding.md](map/operations/conversations_v1_binding.md) |
| `client.conversations_v1_configuration_api` | 4 | [map/operations/conversations_v1_configuration_api.md](map/operations/conversations_v1_configuration_api.md) |
| `client.conversations_v1_conversation_api` | 10 | [map/operations/conversations_v1_conversation_api.md](map/operations/conversations_v1_conversation_api.md) |
| `client.conversations_v1_conversation_with_participants_api` | 2 | [map/operations/conversations_v1_conversation_with_participants_api.md](map/operations/conversations_v1_conversation_with_participants_api.md) |
| `client.conversations_v1_credential_api` | 5 | [map/operations/conversations_v1_credential_api.md](map/operations/conversations_v1_credential_api.md) |
| `client.conversations_v1_delivery_receipt` | 4 | [map/operations/conversations_v1_delivery_receipt.md](map/operations/conversations_v1_delivery_receipt.md) |
| `client.conversations_v1_message` | 10 | [map/operations/conversations_v1_message.md](map/operations/conversations_v1_message.md) |
| `client.conversations_v1_notification` | 2 | [map/operations/conversations_v1_notification.md](map/operations/conversations_v1_notification.md) |
| `client.conversations_v1_participant` | 10 | [map/operations/conversations_v1_participant.md](map/operations/conversations_v1_participant.md) |
| `client.conversations_v1_participant_conversation_api` | 2 | [map/operations/conversations_v1_participant_conversation_api.md](map/operations/conversations_v1_participant_conversation_api.md) |
| `client.conversations_v1_role_api` | 10 | [map/operations/conversations_v1_role_api.md](map/operations/conversations_v1_role_api.md) |
| `client.conversations_v1_service_api` | 4 | [map/operations/conversations_v1_service_api.md](map/operations/conversations_v1_service_api.md) |
| `client.conversations_v1_user_api` | 10 | [map/operations/conversations_v1_user_api.md](map/operations/conversations_v1_user_api.md) |
| `client.conversations_v1_user_conversation` | 8 | [map/operations/conversations_v1_user_conversation.md](map/operations/conversations_v1_user_conversation.md) |
| `client.conversations_v1_webhook` | 14 | [map/operations/conversations_v1_webhook.md](map/operations/conversations_v1_webhook.md) |
| `client.conversations_v2_action_api` | 2 | [map/operations/conversations_v2_action_api.md](map/operations/conversations_v2_action_api.md) |
| `client.conversations_v2_communication_api` | 3 | [map/operations/conversations_v2_communication_api.md](map/operations/conversations_v2_communication_api.md) |
| `client.conversations_v2_configuration_api` | 5 | [map/operations/conversations_v2_configuration_api.md](map/operations/conversations_v2_configuration_api.md) |
| `client.conversations_v2_conversation_api` | 6 | [map/operations/conversations_v2_conversation_api.md](map/operations/conversations_v2_conversation_api.md) |
| `client.conversations_v2_operation` | 1 | [map/operations/conversations_v2_operation.md](map/operations/conversations_v2_operation.md) |
| `client.conversations_v2_participant_api` | 4 | [map/operations/conversations_v2_participant_api.md](map/operations/conversations_v2_participant_api.md) |
| `client.flex_v1_assessments` | 3 | [map/operations/flex_v1_assessments.md](map/operations/flex_v1_assessments.md) |
| `client.flex_v1_channel_api` | 4 | [map/operations/flex_v1_channel_api.md](map/operations/flex_v1_channel_api.md) |
| `client.flex_v1_configuration_api` | 2 | [map/operations/flex_v1_configuration_api.md](map/operations/flex_v1_configuration_api.md) |
| `client.flex_v1_configured_plugin` | 2 | [map/operations/flex_v1_configured_plugin.md](map/operations/flex_v1_configured_plugin.md) |
| `client.flex_v1_flex_flow_api` | 5 | [map/operations/flex_v1_flex_flow_api.md](map/operations/flex_v1_flex_flow_api.md) |
| `client.flex_v1_insights_assessments_comment_api` | 2 | [map/operations/flex_v1_insights_assessments_comment_api.md](map/operations/flex_v1_insights_assessments_comment_api.md) |
| `client.flex_v1_insights_conversations_api` | 1 | [map/operations/flex_v1_insights_conversations_api.md](map/operations/flex_v1_insights_conversations_api.md) |
| `client.flex_v1_insights_questionnaires_api` | 5 | [map/operations/flex_v1_insights_questionnaires_api.md](map/operations/flex_v1_insights_questionnaires_api.md) |
| `client.flex_v1_insights_questionnaires_category_api` | 4 | [map/operations/flex_v1_insights_questionnaires_category_api.md](map/operations/flex_v1_insights_questionnaires_category_api.md) |
| `client.flex_v1_insights_questionnaires_question_api` | 4 | [map/operations/flex_v1_insights_questionnaires_question_api.md](map/operations/flex_v1_insights_questionnaires_question_api.md) |
| `client.flex_v1_insights_segments_api` | 1 | [map/operations/flex_v1_insights_segments_api.md](map/operations/flex_v1_insights_segments_api.md) |
| `client.flex_v1_insights_session_api` | 1 | [map/operations/flex_v1_insights_session_api.md](map/operations/flex_v1_insights_session_api.md) |
| `client.flex_v1_insights_settings_answer_sets_api` | 1 | [map/operations/flex_v1_insights_settings_answer_sets_api.md](map/operations/flex_v1_insights_settings_answer_sets_api.md) |
| `client.flex_v1_insights_settings_comment_api` | 1 | [map/operations/flex_v1_insights_settings_comment_api.md](map/operations/flex_v1_insights_settings_comment_api.md) |
| `client.flex_v1_insights_user_roles_api` | 1 | [map/operations/flex_v1_insights_user_roles_api.md](map/operations/flex_v1_insights_user_roles_api.md) |
| `client.flex_v1_interaction_api` | 3 | [map/operations/flex_v1_interaction_api.md](map/operations/flex_v1_interaction_api.md) |
| `client.flex_v1_interaction_channel` | 3 | [map/operations/flex_v1_interaction_channel.md](map/operations/flex_v1_interaction_channel.md) |
| `client.flex_v1_interaction_channel_invite` | 2 | [map/operations/flex_v1_interaction_channel_invite.md](map/operations/flex_v1_interaction_channel_invite.md) |
| `client.flex_v1_interaction_channel_participant` | 3 | [map/operations/flex_v1_interaction_channel_participant.md](map/operations/flex_v1_interaction_channel_participant.md) |
| `client.flex_v1_interaction_transfer` | 3 | [map/operations/flex_v1_interaction_transfer.md](map/operations/flex_v1_interaction_transfer.md) |
| `client.flex_v1_plugin_api` | 4 | [map/operations/flex_v1_plugin_api.md](map/operations/flex_v1_plugin_api.md) |
| `client.flex_v1_plugin_archive_api` | 1 | [map/operations/flex_v1_plugin_archive_api.md](map/operations/flex_v1_plugin_archive_api.md) |
| `client.flex_v1_plugin_configuration_api` | 3 | [map/operations/flex_v1_plugin_configuration_api.md](map/operations/flex_v1_plugin_configuration_api.md) |
| `client.flex_v1_plugin_configuration_archive_api` | 1 | [map/operations/flex_v1_plugin_configuration_archive_api.md](map/operations/flex_v1_plugin_configuration_archive_api.md) |
| `client.flex_v1_plugin_release_api` | 3 | [map/operations/flex_v1_plugin_release_api.md](map/operations/flex_v1_plugin_release_api.md) |
| `client.flex_v1_plugin_version_archive_api` | 1 | [map/operations/flex_v1_plugin_version_archive_api.md](map/operations/flex_v1_plugin_version_archive_api.md) |
| `client.flex_v1_plugin_versions` | 3 | [map/operations/flex_v1_plugin_versions.md](map/operations/flex_v1_plugin_versions.md) |
| `client.flex_v1_provisioning_status_api` | 1 | [map/operations/flex_v1_provisioning_status_api.md](map/operations/flex_v1_provisioning_status_api.md) |
| `client.flex_v1_web_channel_api` | 5 | [map/operations/flex_v1_web_channel_api.md](map/operations/flex_v1_web_channel_api.md) |
| `client.flex_v2_flex_user_api` | 2 | [map/operations/flex_v2_flex_user_api.md](map/operations/flex_v2_flex_user_api.md) |
| `client.flex_v2_web_channels` | 1 | [map/operations/flex_v2_web_channels.md](map/operations/flex_v2_web_channels.md) |
| `client.insights_v1_annotation` | 2 | [map/operations/insights_v1_annotation.md](map/operations/insights_v1_annotation.md) |
| `client.insights_v1_call_api` | 1 | [map/operations/insights_v1_call_api.md](map/operations/insights_v1_call_api.md) |
| `client.insights_v1_call_summaries_api` | 1 | [map/operations/insights_v1_call_summaries_api.md](map/operations/insights_v1_call_summaries_api.md) |
| `client.insights_v1_call_summary_api` | 1 | [map/operations/insights_v1_call_summary_api.md](map/operations/insights_v1_call_summary_api.md) |
| `client.insights_v1_conference_api` | 2 | [map/operations/insights_v1_conference_api.md](map/operations/insights_v1_conference_api.md) |
| `client.insights_v1_conference_participant` | 2 | [map/operations/insights_v1_conference_participant.md](map/operations/insights_v1_conference_participant.md) |
| `client.insights_v1_create_account_report` | 1 | [map/operations/insights_v1_create_account_report.md](map/operations/insights_v1_create_account_report.md) |
| `client.insights_v1_create_inbound_phone_numbers_report` | 1 | [map/operations/insights_v1_create_inbound_phone_numbers_report.md](map/operations/insights_v1_create_inbound_phone_numbers_report.md) |
| `client.insights_v1_create_outbound_phone_numbers_report` | 1 | [map/operations/insights_v1_create_outbound_phone_numbers_report.md](map/operations/insights_v1_create_outbound_phone_numbers_report.md) |
| `client.insights_v1_event` | 1 | [map/operations/insights_v1_event.md](map/operations/insights_v1_event.md) |
| `client.insights_v1_get_account_report` | 1 | [map/operations/insights_v1_get_account_report.md](map/operations/insights_v1_get_account_report.md) |
| `client.insights_v1_get_inbound_phone_numbers_report` | 1 | [map/operations/insights_v1_get_inbound_phone_numbers_report.md](map/operations/insights_v1_get_inbound_phone_numbers_report.md) |
| `client.insights_v1_get_outbound_phone_numbers_report` | 1 | [map/operations/insights_v1_get_outbound_phone_numbers_report.md](map/operations/insights_v1_get_outbound_phone_numbers_report.md) |
| `client.insights_v1_metric` | 1 | [map/operations/insights_v1_metric.md](map/operations/insights_v1_metric.md) |
| `client.insights_v1_participant` | 2 | [map/operations/insights_v1_participant.md](map/operations/insights_v1_participant.md) |
| `client.insights_v1_room` | 2 | [map/operations/insights_v1_room.md](map/operations/insights_v1_room.md) |
| `client.insights_v1_setting` | 2 | [map/operations/insights_v1_setting.md](map/operations/insights_v1_setting.md) |
| `client.lookups_v1_phone_number_api` | 1 | [map/operations/lookups_v1_phone_number_api.md](map/operations/lookups_v1_phone_number_api.md) |
| `client.lookups_v2_phone_number` | 1 | [map/operations/lookups_v2_phone_number.md](map/operations/lookups_v2_phone_number.md) |
| `client.messaging_v1_alpha_sender` | 4 | [map/operations/messaging_v1_alpha_sender.md](map/operations/messaging_v1_alpha_sender.md) |
| `client.messaging_v1_brand_registration` | 4 | [map/operations/messaging_v1_brand_registration.md](map/operations/messaging_v1_brand_registration.md) |
| `client.messaging_v1_brand_registration_otp` | 1 | [map/operations/messaging_v1_brand_registration_otp.md](map/operations/messaging_v1_brand_registration_otp.md) |
| `client.messaging_v1_brand_vetting` | 3 | [map/operations/messaging_v1_brand_vetting.md](map/operations/messaging_v1_brand_vetting.md) |
| `client.messaging_v1_channel_sender` | 4 | [map/operations/messaging_v1_channel_sender.md](map/operations/messaging_v1_channel_sender.md) |
| `client.messaging_v1_deactivations` | 1 | [map/operations/messaging_v1_deactivations.md](map/operations/messaging_v1_deactivations.md) |
| `client.messaging_v1_destination_alpha_sender` | 4 | [map/operations/messaging_v1_destination_alpha_sender.md](map/operations/messaging_v1_destination_alpha_sender.md) |
| `client.messaging_v1_domain_certs` | 3 | [map/operations/messaging_v1_domain_certs.md](map/operations/messaging_v1_domain_certs.md) |
| `client.messaging_v1_domain_config_api` | 2 | [map/operations/messaging_v1_domain_config_api.md](map/operations/messaging_v1_domain_config_api.md) |
| `client.messaging_v1_domain_config_messaging_service_api` | 1 | [map/operations/messaging_v1_domain_config_messaging_service_api.md](map/operations/messaging_v1_domain_config_messaging_service_api.md) |
| `client.messaging_v1_domain_validate_dns` | 1 | [map/operations/messaging_v1_domain_validate_dns.md](map/operations/messaging_v1_domain_validate_dns.md) |
| `client.messaging_v1_external_campaign_api` | 1 | [map/operations/messaging_v1_external_campaign_api.md](map/operations/messaging_v1_external_campaign_api.md) |
| `client.messaging_v1_linkshortening_messaging_service_api` | 2 | [map/operations/messaging_v1_linkshortening_messaging_service_api.md](map/operations/messaging_v1_linkshortening_messaging_service_api.md) |
| `client.messaging_v1_linkshortening_messaging_service_domain_association_api` | 1 | [map/operations/messaging_v1_linkshortening_messaging_service_domain_association_api.md](map/operations/messaging_v1_linkshortening_messaging_service_domain_association_api.md) |
| `client.messaging_v1_phone_number` | 4 | [map/operations/messaging_v1_phone_number.md](map/operations/messaging_v1_phone_number.md) |
| `client.messaging_v1_request_managed_cert_api` | 1 | [map/operations/messaging_v1_request_managed_cert_api.md](map/operations/messaging_v1_request_managed_cert_api.md) |
| `client.messaging_v1_service_api` | 5 | [map/operations/messaging_v1_service_api.md](map/operations/messaging_v1_service_api.md) |
| `client.messaging_v1_short_code` | 4 | [map/operations/messaging_v1_short_code.md](map/operations/messaging_v1_short_code.md) |
| `client.messaging_v1_tollfree_verification_api` | 5 | [map/operations/messaging_v1_tollfree_verification_api.md](map/operations/messaging_v1_tollfree_verification_api.md) |
| `client.messaging_v1_us_app_to_person` | 5 | [map/operations/messaging_v1_us_app_to_person.md](map/operations/messaging_v1_us_app_to_person.md) |
| `client.messaging_v1_us_app_to_person_usecase` | 1 | [map/operations/messaging_v1_us_app_to_person_usecase.md](map/operations/messaging_v1_us_app_to_person_usecase.md) |
| `client.messaging_v1_usecase_api` | 1 | [map/operations/messaging_v1_usecase_api.md](map/operations/messaging_v1_usecase_api.md) |
| `client.messaging_v2_channels_sender` | 5 | [map/operations/messaging_v2_channels_sender.md](map/operations/messaging_v2_channels_sender.md) |
| `client.messaging_v2_domain_certs` | 1 | [map/operations/messaging_v2_domain_certs.md](map/operations/messaging_v2_domain_certs.md) |
| `client.messaging_v2_typing_indicator` | 1 | [map/operations/messaging_v2_typing_indicator.md](map/operations/messaging_v2_typing_indicator.md) |
| `client.messaging_v3_typing_indicator` | 1 | [map/operations/messaging_v3_typing_indicator.md](map/operations/messaging_v3_typing_indicator.md) |
| `client.numbers_v1_bulk_eligibility_api` | 2 | [map/operations/numbers_v1_bulk_eligibility_api.md](map/operations/numbers_v1_bulk_eligibility_api.md) |
| `client.numbers_v1_eligibility_api` | 1 | [map/operations/numbers_v1_eligibility_api.md](map/operations/numbers_v1_eligibility_api.md) |
| `client.numbers_v1_porting_port_in_api` | 4 | [map/operations/numbers_v1_porting_port_in_api.md](map/operations/numbers_v1_porting_port_in_api.md) |
| `client.numbers_v1_porting_port_in_phone_number_api` | 2 | [map/operations/numbers_v1_porting_port_in_phone_number_api.md](map/operations/numbers_v1_porting_port_in_phone_number_api.md) |
| `client.numbers_v1_porting_portability_api` | 1 | [map/operations/numbers_v1_porting_portability_api.md](map/operations/numbers_v1_porting_portability_api.md) |
| `client.numbers_v1_porting_webhook_configuration_api` | 1 | [map/operations/numbers_v1_porting_webhook_configuration_api.md](map/operations/numbers_v1_porting_webhook_configuration_api.md) |
| `client.numbers_v1_porting_webhook_configuration_delete_api` | 1 | [map/operations/numbers_v1_porting_webhook_configuration_delete_api.md](map/operations/numbers_v1_porting_webhook_configuration_delete_api.md) |
| `client.numbers_v1_porting_webhook_configuration_fetch_api` | 1 | [map/operations/numbers_v1_porting_webhook_configuration_fetch_api.md](map/operations/numbers_v1_porting_webhook_configuration_fetch_api.md) |
| `client.numbers_v1_sender_id_registration` | 1 | [map/operations/numbers_v1_sender_id_registration.md](map/operations/numbers_v1_sender_id_registration.md) |
| `client.numbers_v1_sender_id_registration_embedded_session` | 1 | [map/operations/numbers_v1_sender_id_registration_embedded_session.md](map/operations/numbers_v1_sender_id_registration_embedded_session.md) |
| `client.numbers_v1_signing_request_configuration_api` | 2 | [map/operations/numbers_v1_signing_request_configuration_api.md](map/operations/numbers_v1_signing_request_configuration_api.md) |
| `client.numbers_v2_authorization_document_api` | 4 | [map/operations/numbers_v2_authorization_document_api.md](map/operations/numbers_v2_authorization_document_api.md) |
| `client.numbers_v2_bulk_hosted_number_order_api` | 2 | [map/operations/numbers_v2_bulk_hosted_number_order_api.md](map/operations/numbers_v2_bulk_hosted_number_order_api.md) |
| `client.numbers_v2_bundle` | 5 | [map/operations/numbers_v2_bundle.md](map/operations/numbers_v2_bundle.md) |
| `client.numbers_v2_bundle_clone_api` | 1 | [map/operations/numbers_v2_bundle_clone_api.md](map/operations/numbers_v2_bundle_clone_api.md) |
| `client.numbers_v2_bundle_copy` | 2 | [map/operations/numbers_v2_bundle_copy.md](map/operations/numbers_v2_bundle_copy.md) |
| `client.numbers_v2_dependent_hosted_number_order` | 1 | [map/operations/numbers_v2_dependent_hosted_number_order.md](map/operations/numbers_v2_dependent_hosted_number_order.md) |
| `client.numbers_v2_end_user` | 5 | [map/operations/numbers_v2_end_user.md](map/operations/numbers_v2_end_user.md) |
| `client.numbers_v2_end_user_type` | 2 | [map/operations/numbers_v2_end_user_type.md](map/operations/numbers_v2_end_user_type.md) |
| `client.numbers_v2_evaluation` | 3 | [map/operations/numbers_v2_evaluation.md](map/operations/numbers_v2_evaluation.md) |
| `client.numbers_v2_hosted_number_order_api` | 5 | [map/operations/numbers_v2_hosted_number_order_api.md](map/operations/numbers_v2_hosted_number_order_api.md) |
| `client.numbers_v2_item_assignment` | 4 | [map/operations/numbers_v2_item_assignment.md](map/operations/numbers_v2_item_assignment.md) |
| `client.numbers_v2_regulation` | 2 | [map/operations/numbers_v2_regulation.md](map/operations/numbers_v2_regulation.md) |
| `client.numbers_v2_replace_items` | 1 | [map/operations/numbers_v2_replace_items.md](map/operations/numbers_v2_replace_items.md) |
| `client.numbers_v2_supporting_document` | 5 | [map/operations/numbers_v2_supporting_document.md](map/operations/numbers_v2_supporting_document.md) |
| `client.numbers_v2_supporting_document_type` | 2 | [map/operations/numbers_v2_supporting_document_type.md](map/operations/numbers_v2_supporting_document_type.md) |
| `client.numbers_v3_hosted_numbers_hosted_number_order_api` | 1 | [map/operations/numbers_v3_hosted_numbers_hosted_number_order_api.md](map/operations/numbers_v3_hosted_numbers_hosted_number_order_api.md) |
| `client.proxy_v1_interaction` | 3 | [map/operations/proxy_v1_interaction.md](map/operations/proxy_v1_interaction.md) |
| `client.proxy_v1_message_interaction` | 3 | [map/operations/proxy_v1_message_interaction.md](map/operations/proxy_v1_message_interaction.md) |
| `client.proxy_v1_participant` | 4 | [map/operations/proxy_v1_participant.md](map/operations/proxy_v1_participant.md) |
| `client.proxy_v1_phone_number` | 5 | [map/operations/proxy_v1_phone_number.md](map/operations/proxy_v1_phone_number.md) |
| `client.proxy_v1_service_api` | 5 | [map/operations/proxy_v1_service_api.md](map/operations/proxy_v1_service_api.md) |
| `client.proxy_v1_session` | 5 | [map/operations/proxy_v1_session.md](map/operations/proxy_v1_session.md) |
| `client.studio_v1_engagement` | 4 | [map/operations/studio_v1_engagement.md](map/operations/studio_v1_engagement.md) |
| `client.studio_v1_engagement_context` | 1 | [map/operations/studio_v1_engagement_context.md](map/operations/studio_v1_engagement_context.md) |
| `client.studio_v1_execution` | 5 | [map/operations/studio_v1_execution.md](map/operations/studio_v1_execution.md) |
| `client.studio_v1_execution_context` | 1 | [map/operations/studio_v1_execution_context.md](map/operations/studio_v1_execution_context.md) |
| `client.studio_v1_execution_step` | 2 | [map/operations/studio_v1_execution_step.md](map/operations/studio_v1_execution_step.md) |
| `client.studio_v1_execution_step_context` | 1 | [map/operations/studio_v1_execution_step_context.md](map/operations/studio_v1_execution_step_context.md) |
| `client.studio_v1_flow_api` | 3 | [map/operations/studio_v1_flow_api.md](map/operations/studio_v1_flow_api.md) |
| `client.studio_v1_step` | 2 | [map/operations/studio_v1_step.md](map/operations/studio_v1_step.md) |
| `client.studio_v1_step_context` | 1 | [map/operations/studio_v1_step_context.md](map/operations/studio_v1_step_context.md) |
| `client.studio_v2_execution` | 5 | [map/operations/studio_v2_execution.md](map/operations/studio_v2_execution.md) |
| `client.studio_v2_execution_context` | 1 | [map/operations/studio_v2_execution_context.md](map/operations/studio_v2_execution_context.md) |
| `client.studio_v2_execution_step` | 2 | [map/operations/studio_v2_execution_step.md](map/operations/studio_v2_execution_step.md) |
| `client.studio_v2_execution_step_context` | 1 | [map/operations/studio_v2_execution_step_context.md](map/operations/studio_v2_execution_step_context.md) |
| `client.studio_v2_flow_api` | 5 | [map/operations/studio_v2_flow_api.md](map/operations/studio_v2_flow_api.md) |
| `client.studio_v2_flow_revision` | 2 | [map/operations/studio_v2_flow_revision.md](map/operations/studio_v2_flow_revision.md) |
| `client.studio_v2_flow_test_user_api` | 2 | [map/operations/studio_v2_flow_test_user_api.md](map/operations/studio_v2_flow_test_user_api.md) |
| `client.studio_v2_flow_validate_api` | 1 | [map/operations/studio_v2_flow_validate_api.md](map/operations/studio_v2_flow_validate_api.md) |
| `client.sync_v1_document` | 5 | [map/operations/sync_v1_document.md](map/operations/sync_v1_document.md) |
| `client.sync_v1_document_permission` | 4 | [map/operations/sync_v1_document_permission.md](map/operations/sync_v1_document_permission.md) |
| `client.sync_v1_service_api` | 5 | [map/operations/sync_v1_service_api.md](map/operations/sync_v1_service_api.md) |
| `client.sync_v1_stream_message` | 1 | [map/operations/sync_v1_stream_message.md](map/operations/sync_v1_stream_message.md) |
| `client.sync_v1_sync_list` | 5 | [map/operations/sync_v1_sync_list.md](map/operations/sync_v1_sync_list.md) |
| `client.sync_v1_sync_list_item` | 5 | [map/operations/sync_v1_sync_list_item.md](map/operations/sync_v1_sync_list_item.md) |
| `client.sync_v1_sync_list_permission` | 4 | [map/operations/sync_v1_sync_list_permission.md](map/operations/sync_v1_sync_list_permission.md) |
| `client.sync_v1_sync_map` | 5 | [map/operations/sync_v1_sync_map.md](map/operations/sync_v1_sync_map.md) |
| `client.sync_v1_sync_map_item` | 5 | [map/operations/sync_v1_sync_map_item.md](map/operations/sync_v1_sync_map_item.md) |
| `client.sync_v1_sync_map_permission` | 4 | [map/operations/sync_v1_sync_map_permission.md](map/operations/sync_v1_sync_map_permission.md) |
| `client.sync_v1_sync_stream` | 5 | [map/operations/sync_v1_sync_stream.md](map/operations/sync_v1_sync_stream.md) |
| `client.taskrouter_v1_activity` | 5 | [map/operations/taskrouter_v1_activity.md](map/operations/taskrouter_v1_activity.md) |
| `client.taskrouter_v1_event` | 2 | [map/operations/taskrouter_v1_event.md](map/operations/taskrouter_v1_event.md) |
| `client.taskrouter_v1_task` | 5 | [map/operations/taskrouter_v1_task.md](map/operations/taskrouter_v1_task.md) |
| `client.taskrouter_v1_task_channel` | 5 | [map/operations/taskrouter_v1_task_channel.md](map/operations/taskrouter_v1_task_channel.md) |
| `client.taskrouter_v1_task_queue` | 5 | [map/operations/taskrouter_v1_task_queue.md](map/operations/taskrouter_v1_task_queue.md) |
| `client.taskrouter_v1_task_queue_bulk_real_time_statistics` | 1 | [map/operations/taskrouter_v1_task_queue_bulk_real_time_statistics.md](map/operations/taskrouter_v1_task_queue_bulk_real_time_statistics.md) |
| `client.taskrouter_v1_task_queue_cumulative_statistics` | 1 | [map/operations/taskrouter_v1_task_queue_cumulative_statistics.md](map/operations/taskrouter_v1_task_queue_cumulative_statistics.md) |
| `client.taskrouter_v1_task_queue_real_time_statistics` | 1 | [map/operations/taskrouter_v1_task_queue_real_time_statistics.md](map/operations/taskrouter_v1_task_queue_real_time_statistics.md) |
| `client.taskrouter_v1_task_queue_statistics` | 1 | [map/operations/taskrouter_v1_task_queue_statistics.md](map/operations/taskrouter_v1_task_queue_statistics.md) |
| `client.taskrouter_v1_task_queues_statistics` | 1 | [map/operations/taskrouter_v1_task_queues_statistics.md](map/operations/taskrouter_v1_task_queues_statistics.md) |
| `client.taskrouter_v1_task_reservation` | 3 | [map/operations/taskrouter_v1_task_reservation.md](map/operations/taskrouter_v1_task_reservation.md) |
| `client.taskrouter_v1_worker` | 5 | [map/operations/taskrouter_v1_worker.md](map/operations/taskrouter_v1_worker.md) |
| `client.taskrouter_v1_worker_channel` | 3 | [map/operations/taskrouter_v1_worker_channel.md](map/operations/taskrouter_v1_worker_channel.md) |
| `client.taskrouter_v1_worker_reservation` | 3 | [map/operations/taskrouter_v1_worker_reservation.md](map/operations/taskrouter_v1_worker_reservation.md) |
| `client.taskrouter_v1_worker_statistics` | 1 | [map/operations/taskrouter_v1_worker_statistics.md](map/operations/taskrouter_v1_worker_statistics.md) |
| `client.taskrouter_v1_workers_cumulative_statistics` | 1 | [map/operations/taskrouter_v1_workers_cumulative_statistics.md](map/operations/taskrouter_v1_workers_cumulative_statistics.md) |
| `client.taskrouter_v1_workers_real_time_statistics` | 1 | [map/operations/taskrouter_v1_workers_real_time_statistics.md](map/operations/taskrouter_v1_workers_real_time_statistics.md) |
| `client.taskrouter_v1_workers_statistics` | 1 | [map/operations/taskrouter_v1_workers_statistics.md](map/operations/taskrouter_v1_workers_statistics.md) |
| `client.taskrouter_v1_workflow` | 5 | [map/operations/taskrouter_v1_workflow.md](map/operations/taskrouter_v1_workflow.md) |
| `client.taskrouter_v1_workflow_cumulative_statistics` | 1 | [map/operations/taskrouter_v1_workflow_cumulative_statistics.md](map/operations/taskrouter_v1_workflow_cumulative_statistics.md) |
| `client.taskrouter_v1_workflow_real_time_statistics` | 1 | [map/operations/taskrouter_v1_workflow_real_time_statistics.md](map/operations/taskrouter_v1_workflow_real_time_statistics.md) |
| `client.taskrouter_v1_workflow_statistics` | 1 | [map/operations/taskrouter_v1_workflow_statistics.md](map/operations/taskrouter_v1_workflow_statistics.md) |
| `client.taskrouter_v1_workspace_api` | 5 | [map/operations/taskrouter_v1_workspace_api.md](map/operations/taskrouter_v1_workspace_api.md) |
| `client.taskrouter_v1_workspace_cumulative_statistics` | 1 | [map/operations/taskrouter_v1_workspace_cumulative_statistics.md](map/operations/taskrouter_v1_workspace_cumulative_statistics.md) |
| `client.taskrouter_v1_workspace_real_time_statistics` | 1 | [map/operations/taskrouter_v1_workspace_real_time_statistics.md](map/operations/taskrouter_v1_workspace_real_time_statistics.md) |
| `client.taskrouter_v1_workspace_statistics` | 1 | [map/operations/taskrouter_v1_workspace_statistics.md](map/operations/taskrouter_v1_workspace_statistics.md) |
| `client.trusthub_v1_compliance_inquiries` | 2 | [map/operations/trusthub_v1_compliance_inquiries.md](map/operations/trusthub_v1_compliance_inquiries.md) |
| `client.trusthub_v1_compliance_registration_inquiries` | 2 | [map/operations/trusthub_v1_compliance_registration_inquiries.md](map/operations/trusthub_v1_compliance_registration_inquiries.md) |
| `client.trusthub_v1_compliance_tollfree_inquiries` | 1 | [map/operations/trusthub_v1_compliance_tollfree_inquiries.md](map/operations/trusthub_v1_compliance_tollfree_inquiries.md) |
| `client.trusthub_v1_customer_profiles` | 5 | [map/operations/trusthub_v1_customer_profiles.md](map/operations/trusthub_v1_customer_profiles.md) |
| `client.trusthub_v1_customer_profiles_channel_endpoint_assignment` | 4 | [map/operations/trusthub_v1_customer_profiles_channel_endpoint_assignment.md](map/operations/trusthub_v1_customer_profiles_channel_endpoint_assignment.md) |
| `client.trusthub_v1_customer_profiles_entity_assignments` | 4 | [map/operations/trusthub_v1_customer_profiles_entity_assignments.md](map/operations/trusthub_v1_customer_profiles_entity_assignments.md) |
| `client.trusthub_v1_customer_profiles_evaluations` | 3 | [map/operations/trusthub_v1_customer_profiles_evaluations.md](map/operations/trusthub_v1_customer_profiles_evaluations.md) |
| `client.trusthub_v1_end_user_api` | 5 | [map/operations/trusthub_v1_end_user_api.md](map/operations/trusthub_v1_end_user_api.md) |
| `client.trusthub_v1_end_user_type` | 2 | [map/operations/trusthub_v1_end_user_type.md](map/operations/trusthub_v1_end_user_type.md) |
| `client.trusthub_v1_policies_api` | 2 | [map/operations/trusthub_v1_policies_api.md](map/operations/trusthub_v1_policies_api.md) |
| `client.trusthub_v1_supporting_document_api` | 5 | [map/operations/trusthub_v1_supporting_document_api.md](map/operations/trusthub_v1_supporting_document_api.md) |
| `client.trusthub_v1_supporting_document_type` | 2 | [map/operations/trusthub_v1_supporting_document_type.md](map/operations/trusthub_v1_supporting_document_type.md) |
| `client.trusthub_v1_trust_products` | 5 | [map/operations/trusthub_v1_trust_products.md](map/operations/trusthub_v1_trust_products.md) |
| `client.trusthub_v1_trust_products_channel_endpoint_assignment` | 4 | [map/operations/trusthub_v1_trust_products_channel_endpoint_assignment.md](map/operations/trusthub_v1_trust_products_channel_endpoint_assignment.md) |
| `client.trusthub_v1_trust_products_entity_assignments` | 4 | [map/operations/trusthub_v1_trust_products_entity_assignments.md](map/operations/trusthub_v1_trust_products_entity_assignments.md) |
| `client.trusthub_v1_trust_products_evaluations` | 3 | [map/operations/trusthub_v1_trust_products_evaluations.md](map/operations/trusthub_v1_trust_products_evaluations.md) |
| `client.twilio_insights` | 3 | [map/operations/twilio_insights.md](map/operations/twilio_insights.md) |
| `client.v2_short_code_applications` | 3 | [map/operations/v2_short_code_applications.md](map/operations/v2_short_code_applications.md) |
| `client.verify_v2_access_token` | 2 | [map/operations/verify_v2_access_token.md](map/operations/verify_v2_access_token.md) |
| `client.verify_v2_bucket` | 5 | [map/operations/verify_v2_bucket.md](map/operations/verify_v2_bucket.md) |
| `client.verify_v2_challenge` | 4 | [map/operations/verify_v2_challenge.md](map/operations/verify_v2_challenge.md) |
| `client.verify_v2_entity` | 4 | [map/operations/verify_v2_entity.md](map/operations/verify_v2_entity.md) |
| `client.verify_v2_factor` | 4 | [map/operations/verify_v2_factor.md](map/operations/verify_v2_factor.md) |
| `client.verify_v2_form_api` | 1 | [map/operations/verify_v2_form_api.md](map/operations/verify_v2_form_api.md) |
| `client.verify_v2_messaging_configuration` | 5 | [map/operations/verify_v2_messaging_configuration.md](map/operations/verify_v2_messaging_configuration.md) |
| `client.verify_v2_new_challenge` | 1 | [map/operations/verify_v2_new_challenge.md](map/operations/verify_v2_new_challenge.md) |
| `client.verify_v2_new_factor` | 2 | [map/operations/verify_v2_new_factor.md](map/operations/verify_v2_new_factor.md) |
| `client.verify_v2_notification` | 1 | [map/operations/verify_v2_notification.md](map/operations/verify_v2_notification.md) |
| `client.verify_v2_rate_limit` | 5 | [map/operations/verify_v2_rate_limit.md](map/operations/verify_v2_rate_limit.md) |
| `client.verify_v2_safelist_api` | 3 | [map/operations/verify_v2_safelist_api.md](map/operations/verify_v2_safelist_api.md) |
| `client.verify_v2_service_api` | 5 | [map/operations/verify_v2_service_api.md](map/operations/verify_v2_service_api.md) |
| `client.verify_v2_template` | 1 | [map/operations/verify_v2_template.md](map/operations/verify_v2_template.md) |
| `client.verify_v2_verification` | 3 | [map/operations/verify_v2_verification.md](map/operations/verify_v2_verification.md) |
| `client.verify_v2_verification_attempt_api` | 2 | [map/operations/verify_v2_verification_attempt_api.md](map/operations/verify_v2_verification_attempt_api.md) |
| `client.verify_v2_verification_attempts_summary_api` | 1 | [map/operations/verify_v2_verification_attempts_summary_api.md](map/operations/verify_v2_verification_attempts_summary_api.md) |
| `client.verify_v2_verification_check` | 1 | [map/operations/verify_v2_verification_check.md](map/operations/verify_v2_verification_check.md) |
| `client.verify_v2_webhook` | 5 | [map/operations/verify_v2_webhook.md](map/operations/verify_v2_webhook.md) |
| `client.video_v1_anonymize` | 1 | [map/operations/video_v1_anonymize.md](map/operations/video_v1_anonymize.md) |
| `client.video_v1_composition_api` | 4 | [map/operations/video_v1_composition_api.md](map/operations/video_v1_composition_api.md) |
| `client.video_v1_composition_hook_api` | 5 | [map/operations/video_v1_composition_hook_api.md](map/operations/video_v1_composition_hook_api.md) |
| `client.video_v1_composition_settings_api` | 2 | [map/operations/video_v1_composition_settings_api.md](map/operations/video_v1_composition_settings_api.md) |
| `client.video_v1_participant` | 3 | [map/operations/video_v1_participant.md](map/operations/video_v1_participant.md) |
| `client.video_v1_published_track` | 2 | [map/operations/video_v1_published_track.md](map/operations/video_v1_published_track.md) |
| `client.video_v1_recording_api` | 3 | [map/operations/video_v1_recording_api.md](map/operations/video_v1_recording_api.md) |
| `client.video_v1_recording_rules` | 2 | [map/operations/video_v1_recording_rules.md](map/operations/video_v1_recording_rules.md) |
| `client.video_v1_recording_settings_api` | 2 | [map/operations/video_v1_recording_settings_api.md](map/operations/video_v1_recording_settings_api.md) |
| `client.video_v1_room_api` | 4 | [map/operations/video_v1_room_api.md](map/operations/video_v1_room_api.md) |
| `client.video_v1_room_recording` | 3 | [map/operations/video_v1_room_recording.md](map/operations/video_v1_room_recording.md) |
| `client.video_v1_subscribe_rules` | 2 | [map/operations/video_v1_subscribe_rules.md](map/operations/video_v1_subscribe_rules.md) |
| `client.video_v1_subscribed_track` | 2 | [map/operations/video_v1_subscribed_track.md](map/operations/video_v1_subscribed_track.md) |
| `client.video_v1_transcriptions` | 4 | [map/operations/video_v1_transcriptions.md](map/operations/video_v1_transcriptions.md) |

---

## Models — where they live, how to build them

**Shapes live only in the source.** Every module under `twilio_sdk/models/` declares one type plus its input companion, and every module under `twilio_sdk/errors/` one alias plus the mapper that builds it; no two share a name. Take a type's module from the operation's **Type sources** table. When no retrieved chunk names it, the module is the type name in snake_case under the kind's directory below (`AccountsCallsRecordingsSidJson201041408Error` ↔ `accounts_calls_recordings_sid_json201041408_error.py`; an error alias drops its `Body` suffix: `CreateCommunicationInConversationErrorBody` ↔ `create_communication_in_conversation_error.py`). Never grep for a type.

| Group | Count | Directory (module = `<type_name>.py`) |
| --- | --- | --- |
| Models (`SdkBaseModel` pydantic classes) | 838 | `twilio_sdk/models/` |
| Enums (`Enum` over `str`) — Python member names + wire values | 399 | `twilio_sdk/models/enums/` |
| Unions (discriminated) — `TypeAlias` over the arms, tagged via `Field(discriminator=…)` | 1 | `twilio_sdk/models/unions/` |
| Unions (plain) — `TypeAlias` over the arms | 3 | `twilio_sdk/models/unions/` |
| Error aliases (one per Case A operation) | 37 | `twilio_sdk/errors/` |

Conventions: a model is a `SdkBaseModel` (pydantic) class; a field whose wire name differs from its Python name carries it as `Field(alias=…)` (`channel_id` ↔ `"channelId"`) — read the alias off the field rather than deriving it. An omittable field is annotated `Optional[T]` and defaults to `UNSET`, and one that may also be explicitly null is `OptionalNullable[T]`; both come from `core` and neither is `typing.Optional` — there is no `None` arm unless the spec declared the property nullable, so passing `None` to the first is a type error rather than a value that serializes.

Every model, enum and union also has an **input companion**, exported beside it from the same package (`AccountsCallsRecordingsSidJson201041408Error` ↔ `AccountsCallsRecordingsSidJson201041408ErrorDict`). Wherever a signature names the companion you may pass either the model instance or a plain dict with the same keys, whichever reads better at the call site. An enum is a real `Enum` subclass over `str`; its companion is spelled `<Name>OrStr` or `<Name>OrInt` (`AccountType` ↔ `AccountTypeOrStr`) and additionally accepts a wire value this SDK version does not know. A union is a `TypeAlias` over its arms — a discriminated one carries `Field(discriminator=…)`, so build the arm you mean and the tag is written for you.

Import paths by content type (`from <package> import <Name>`):

| Contents | Import from |
| --- | --- |
| Client (root) | `twilio_sdk` |
| Operation controllers | `twilio_sdk.apis` |
| Models | `twilio_sdk.models` |
| Enums | `twilio_sdk.models.enums` |
| Unions | `twilio_sdk.models.unions`, `twilio_sdk.models` |
| Error aliases | `twilio_sdk.errors` |
| Core runtime (`ApiError`, `ApiResult`, `RawError`, …) | `twilio_sdk.core` |

---

## Servers & auth

**Basic auth.** Pass `account_sid_auth_token={"username": …, "password": …}`, or a `BasicAuthCredentials`.

**One environment.** The spec declares a single environment, so no `environment` keyword exists and there is nothing to select.

**15 servers.** Base-URL templates and override points (`twilio_sdk/server/server_config.py`):

| Server | Base URL | Override point |
| --- | --- | --- |
| `default` | `https://api.twilio.com` | `{"default": {"base_url": …}}` |
| `default1` | `https://messaging.twilio.com` | `{"default1": {"base_url": …}}` |
| `default2` | `https://content.twilio.com` | `{"default2": {"base_url": …}}` |
| `default3` | `https://verify.twilio.com` | `{"default3": {"base_url": …}}` |
| `default4` | `https://lookups.twilio.com` | `{"default4": {"base_url": …}}` |
| `default5` | `https://numbers.twilio.com` | `{"default5": {"base_url": …}}` |
| `default6` | `https://video.twilio.com` | `{"default6": {"base_url": …}}` |
| `default7` | `https://conversations.twilio.com` | `{"default7": {"base_url": …}}` |
| `default8` | `https://taskrouter.twilio.com` | `{"default8": {"base_url": …}}` |
| `default9` | `https://trusthub.twilio.com` | `{"default9": {"base_url": …}}` |
| `default10` | `https://proxy.twilio.com` | `{"default10": {"base_url": …}}` |
| `default11` | `https://studio.twilio.com` | `{"default11": {"base_url": …}}` |
| `default12` | `https://sync.twilio.com` | `{"default12": {"base_url": …}}` |
| `default13` | `https://flex-api.twilio.com` | `{"default13": {"base_url": …}}` |
| `default14` | `https://insights.twilio.com` | `{"default14": {"base_url": …}}` |

Override any of these by passing `server_config=` a dict nested exactly as the columns above read — `{"default": {"base_url": …}}` — with each row's variables sitting beside its `base_url`.

