<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401Payment — operations

Accessor: `client.api20100401_payment` · Source: `twilio_sdk/apis/api20100401_payment.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.api20100401_payment.create_payments

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Payments.json`
- **Auth**: `account_sid_auth_token`
- **Server**: `default`
- **Signature**: `def create_payments(account_sid: str, call_sid: str, idempotency_key: str, status_callback: str, *, bank_account_type: PaymentsEnumBankAccountTypeOrStr | None = None, charge_amount: float | None = None, currency: str | None = None, description: str | None = None, input: str | None = None, min_postal_code_length: int | None = None, parameter: Any | None = None, payment_connector: str | None = None, payment_method: PaymentsEnumPaymentMethodOrStr | None = None, postal_code: bool | None = None, security_code: bool | None = None, timeout: int | None = None, token_type: PaymentsEnumTokenTypeOrStr | None = None, valid_card_types: str | None = None, require_matching_inputs: str | None = None, confirmation: ConfirmationOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `call_sid`, `idempotency_key`, `status_callback`
- **Params**: `account_sid` — path `AccountSid` · `call_sid` — path `CallSid` · `idempotency_key` — form field `IdempotencyKey` · `status_callback` — form field `StatusCallback` · `bank_account_type` — form field `BankAccountType` · `charge_amount` — form field `ChargeAmount` · `currency` — form field `Currency` · `description` — form field `Description` · `input` — form field `Input` · `min_postal_code_length` — form field `MinPostalCodeLength` · `parameter` — form field `Parameter` · `payment_connector` — form field `PaymentConnector` · `payment_method` — form field `PaymentMethod` · `postal_code` — form field `PostalCode` · `security_code` — form field `SecurityCode` · `timeout` — form field `Timeout` · `token_type` — form field `TokenType` · `valid_card_types` — form field `ValidCardTypes` · `require_matching_inputs` — form field `RequireMatchingInputs` · `confirmation` — form field `Confirmation`
- **Returns (parsed)**: `ApiV2010AccountCallPayments`
- **Returns (raw)**: `ApiResult[ApiV2010AccountCallPayments, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PaymentsEnumBankAccountTypeOrStr` | `twilio_sdk/models/enums/payments_enum_bank_account_type.py` |
| `PaymentsEnumPaymentMethodOrStr` | `twilio_sdk/models/enums/payments_enum_payment_method.py` |
| `PaymentsEnumTokenTypeOrStr` | `twilio_sdk/models/enums/payments_enum_token_type.py` |
| `ConfirmationOrStr` | `twilio_sdk/models/enums/confirmation.py` |
| `ApiV2010AccountCallPayments` | `twilio_sdk/models/api_v2010_account_call_payments.py` |

### client.api20100401_payment.update_payments

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Payments/{Sid}.json`
- **Auth**: `account_sid_auth_token`
- **Server**: `default`
- **Signature**: `def update_payments(account_sid: str, call_sid: str, sid: str, idempotency_key: str, status_callback: str, *, capture: PaymentsEnumCaptureOrStr | None = None, status: PaymentsEnumStatusOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `call_sid`, `sid`, `idempotency_key`, `status_callback`
- **Params**: `account_sid` — path `AccountSid` · `call_sid` — path `CallSid` · `sid` — path `Sid` · `idempotency_key` — form field `IdempotencyKey` · `status_callback` — form field `StatusCallback` · `capture` — form field `Capture` · `status` — form field `Status`
- **Returns (parsed)**: `ApiV2010AccountCallPayments`
- **Returns (raw)**: `ApiResult[ApiV2010AccountCallPayments, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PaymentsEnumCaptureOrStr` | `twilio_sdk/models/enums/payments_enum_capture.py` |
| `PaymentsEnumStatusOrStr` | `twilio_sdk/models/enums/payments_enum_status.py` |
| `ApiV2010AccountCallPayments` | `twilio_sdk/models/api_v2010_account_call_payments.py` |

