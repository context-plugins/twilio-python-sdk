from __future__ import annotations

from typing import Any
from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.api_v2010_account_call_payments import ApiV2010AccountCallPayments
from ..models.enums.confirmation import ConfirmationOrStr
from ..models.enums.payments_enum_bank_account_type import PaymentsEnumBankAccountTypeOrStr
from ..models.enums.payments_enum_capture import PaymentsEnumCaptureOrStr
from ..models.enums.payments_enum_payment_method import PaymentsEnumPaymentMethodOrStr
from ..models.enums.payments_enum_status import PaymentsEnumStatusOrStr
from ..models.enums.payments_enum_token_type import PaymentsEnumTokenTypeOrStr
from ..server.server import Server


class Api20100401Payment:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401PaymentWithRawResponse(client, server, auth)

    def create_payments(
        self,
        account_sid: str,
        call_sid: str,
        idempotency_key: str,
        status_callback: str,
        *,
        bank_account_type: PaymentsEnumBankAccountTypeOrStr | None = None,
        charge_amount: float | None = None,
        currency: str | None = None,
        description: str | None = None,
        input: str | None = None,
        min_postal_code_length: int | None = None,
        parameter: Any | None = None,
        payment_connector: str | None = None,
        payment_method: PaymentsEnumPaymentMethodOrStr | None = None,
        postal_code: bool | None = None,
        security_code: bool | None = None,
        timeout: int | None = None,
        token_type: PaymentsEnumTokenTypeOrStr | None = None,
        valid_card_types: str | None = None,
        require_matching_inputs: str | None = None,
        confirmation: ConfirmationOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountCallPayments:
        """create an instance of payments. This will start a new payments session

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            call_sid: The SID of the call that will create the resource. Call leg associated with this sid is expected
                to provide payment information thru DTMF.
            idempotency_key: A unique token that will be used to ensure that multiple API calls with the same
                information do not result in multiple transactions. This should be a unique string value per API call
                and can be a randomly generated.
            status_callback: Provide an absolute or relative URL to receive status updates regarding your Pay session.
                Read more about the `expected StatusCallback values
                <https://www.twilio.com/docs/voice/api/payment-resource#statuscallback>`__
            bank_account_type: Type of bank account if payment source is ACH. One of ``consumer-checking``,
                ``consumer-savings``, or ``commercial-checking``. The default value is ``consumer-checking``.
            charge_amount: A positive decimal value less than 1,000,000 to charge against the credit card or bank
                account. Default currency can be overwritten with ``currency`` field. Leave blank or set to 0 to
                tokenize.
            currency: The currency of the ``charge_amount``, formatted as `ISO 4127
                <http://www.iso.org/iso/home/standards/currency_codes.htm>`__ format. The default value is ``USD`` and
                all values allowed from the Pay Connector are accepted.
            description: The description can be used to provide more details regarding the transaction. This information
                is submitted along with the payment details to the Payment Connector which are then posted on the
                transactions.
            input: A list of inputs that should be accepted. Currently only ``dtmf`` is supported. All digits captured
                during a pay session are redacted from the logs.
            min_postal_code_length: A positive integer that is used to validate the length of the ``PostalCode``
                inputted by the user. User must enter this many digits.
            parameter: A single-level JSON object used to pass custom parameters to payment processors. (Required for
                ACH payments). The information that has to be included here depends on the <Pay> Connector. `Read more
                <https://www.twilio.com/console/voice/pay-connectors>`__.
            payment_connector: This is the unique name corresponding to the Pay Connector installed in the Twilio
                Add-ons. Learn more about https://www.twilio.com/console/voice/pay-connectors. The default value is
                ``Default``.
            payment_method: Type of payment being captured. One of ``credit-card`` or ``ach-debit``. The default value
                is ``credit-card``.
            postal_code: Indicates whether the credit card postal code (zip code) is a required piece of payment
                information that must be provided by the caller. The default is ``true``.
            security_code: Indicates whether the credit card security code is a required piece of payment information
                that must be provided by the caller. The default is ``true``.
            timeout: The number of seconds that <Pay> should wait for the caller to press a digit between each
                subsequent digit, after the first one, before moving on to validate the digits captured. The default is
                ``5``, maximum is ``600``.
            token_type: Indicates whether the payment method should be tokenized as a ``one-time``, ``reusable``, or
                ``payment-method`` token. The default value is ``reusable``. Do not enter a charge amount when
                tokenizing. If a charge amount is entered, the payment method will be charged and not tokenized.
            valid_card_types: Credit card types separated by space that Pay should accept. The default value is ``visa
                mastercard amex``
            require_matching_inputs: A comma-separated list of payment information fields that require the caller to
                enter the same value twice for confirmation. Supported values are ``payment-card-number``,
                ``expiration-date``, ``security-code``, and ``postal-code``.
            confirmation: Whether to prompt the caller to confirm their payment information before submitting to the
                payment gateway. If ``true``, the caller will hear the last 4 digits of their card or account number and
                must press 1 to confirm or 2 to cancel. Default is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_payments(
            account_sid,
            call_sid,
            idempotency_key,
            status_callback,
            bank_account_type=bank_account_type,
            charge_amount=charge_amount,
            currency=currency,
            description=description,
            input=input,
            min_postal_code_length=min_postal_code_length,
            parameter=parameter,
            payment_connector=payment_connector,
            payment_method=payment_method,
            postal_code=postal_code,
            security_code=security_code,
            timeout=timeout,
            token_type=token_type,
            valid_card_types=valid_card_types,
            require_matching_inputs=require_matching_inputs,
            confirmation=confirmation,
            request_options=request_options,
        ).unwrap()

    def update_payments(
        self,
        account_sid: str,
        call_sid: str,
        sid: str,
        idempotency_key: str,
        status_callback: str,
        *,
        capture: PaymentsEnumCaptureOrStr | None = None,
        status: PaymentsEnumStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountCallPayments:
        """update an instance of payments with different phases of payment flows.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will update the
                resource.
            call_sid: The SID of the call that will update the resource. This should be the same call sid that was used
                to create payments resource.
            sid: The SID of Payments session that needs to be updated.
            idempotency_key: A unique token that will be used to ensure that multiple API calls with the same
                information do not result in multiple transactions. This should be a unique string value per API call
                and can be a randomly generated.
            status_callback: Provide an absolute or relative URL to receive status updates regarding your Pay session.
                Read more about the `Update
                <https://www.twilio.com/docs/voice/api/payment-resource#statuscallback-update>`__ and `Complete/Cancel
                <https://www.twilio.com/docs/voice/api/payment-resource#statuscallback-cancelcomplete>`__ POST requests.
            capture: The piece of payment information that you wish the caller to enter. Must be one of
                ``payment-card-number``, ``expiration-date``, ``security-code``, ``postal-code``,
                ``bank-routing-number``, ``bank-account-number``, or their ``-matcher`` variants for input confirmation
                when ``RequireMatchingInputs`` is enabled.
            status: Indicates whether the current payment session should be cancelled or completed. When ``cancel`` the
                payment session is cancelled. When ``complete``, Twilio sends the payment information to the selected
                Pay Connector for processing.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Accepted

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_payments(
            account_sid,
            call_sid,
            sid,
            idempotency_key,
            status_callback,
            capture=capture,
            status=status,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401PaymentWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401Payment:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401PaymentWithRawResponse(client, server, auth)

    async def create_payments(
        self,
        account_sid: str,
        call_sid: str,
        idempotency_key: str,
        status_callback: str,
        *,
        bank_account_type: PaymentsEnumBankAccountTypeOrStr | None = None,
        charge_amount: float | None = None,
        currency: str | None = None,
        description: str | None = None,
        input: str | None = None,
        min_postal_code_length: int | None = None,
        parameter: Any | None = None,
        payment_connector: str | None = None,
        payment_method: PaymentsEnumPaymentMethodOrStr | None = None,
        postal_code: bool | None = None,
        security_code: bool | None = None,
        timeout: int | None = None,
        token_type: PaymentsEnumTokenTypeOrStr | None = None,
        valid_card_types: str | None = None,
        require_matching_inputs: str | None = None,
        confirmation: ConfirmationOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountCallPayments:
        """create an instance of payments. This will start a new payments session

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            call_sid: The SID of the call that will create the resource. Call leg associated with this sid is expected
                to provide payment information thru DTMF.
            idempotency_key: A unique token that will be used to ensure that multiple API calls with the same
                information do not result in multiple transactions. This should be a unique string value per API call
                and can be a randomly generated.
            status_callback: Provide an absolute or relative URL to receive status updates regarding your Pay session.
                Read more about the `expected StatusCallback values
                <https://www.twilio.com/docs/voice/api/payment-resource#statuscallback>`__
            bank_account_type: Type of bank account if payment source is ACH. One of ``consumer-checking``,
                ``consumer-savings``, or ``commercial-checking``. The default value is ``consumer-checking``.
            charge_amount: A positive decimal value less than 1,000,000 to charge against the credit card or bank
                account. Default currency can be overwritten with ``currency`` field. Leave blank or set to 0 to
                tokenize.
            currency: The currency of the ``charge_amount``, formatted as `ISO 4127
                <http://www.iso.org/iso/home/standards/currency_codes.htm>`__ format. The default value is ``USD`` and
                all values allowed from the Pay Connector are accepted.
            description: The description can be used to provide more details regarding the transaction. This information
                is submitted along with the payment details to the Payment Connector which are then posted on the
                transactions.
            input: A list of inputs that should be accepted. Currently only ``dtmf`` is supported. All digits captured
                during a pay session are redacted from the logs.
            min_postal_code_length: A positive integer that is used to validate the length of the ``PostalCode``
                inputted by the user. User must enter this many digits.
            parameter: A single-level JSON object used to pass custom parameters to payment processors. (Required for
                ACH payments). The information that has to be included here depends on the <Pay> Connector. `Read more
                <https://www.twilio.com/console/voice/pay-connectors>`__.
            payment_connector: This is the unique name corresponding to the Pay Connector installed in the Twilio
                Add-ons. Learn more about https://www.twilio.com/console/voice/pay-connectors. The default value is
                ``Default``.
            payment_method: Type of payment being captured. One of ``credit-card`` or ``ach-debit``. The default value
                is ``credit-card``.
            postal_code: Indicates whether the credit card postal code (zip code) is a required piece of payment
                information that must be provided by the caller. The default is ``true``.
            security_code: Indicates whether the credit card security code is a required piece of payment information
                that must be provided by the caller. The default is ``true``.
            timeout: The number of seconds that <Pay> should wait for the caller to press a digit between each
                subsequent digit, after the first one, before moving on to validate the digits captured. The default is
                ``5``, maximum is ``600``.
            token_type: Indicates whether the payment method should be tokenized as a ``one-time``, ``reusable``, or
                ``payment-method`` token. The default value is ``reusable``. Do not enter a charge amount when
                tokenizing. If a charge amount is entered, the payment method will be charged and not tokenized.
            valid_card_types: Credit card types separated by space that Pay should accept. The default value is ``visa
                mastercard amex``
            require_matching_inputs: A comma-separated list of payment information fields that require the caller to
                enter the same value twice for confirmation. Supported values are ``payment-card-number``,
                ``expiration-date``, ``security-code``, and ``postal-code``.
            confirmation: Whether to prompt the caller to confirm their payment information before submitting to the
                payment gateway. If ``true``, the caller will hear the last 4 digits of their card or account number and
                must press 1 to confirm or 2 to cancel. Default is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_payments(
                account_sid,
                call_sid,
                idempotency_key,
                status_callback,
                bank_account_type=bank_account_type,
                charge_amount=charge_amount,
                currency=currency,
                description=description,
                input=input,
                min_postal_code_length=min_postal_code_length,
                parameter=parameter,
                payment_connector=payment_connector,
                payment_method=payment_method,
                postal_code=postal_code,
                security_code=security_code,
                timeout=timeout,
                token_type=token_type,
                valid_card_types=valid_card_types,
                require_matching_inputs=require_matching_inputs,
                confirmation=confirmation,
                request_options=request_options,
            )
        ).unwrap()

    async def update_payments(
        self,
        account_sid: str,
        call_sid: str,
        sid: str,
        idempotency_key: str,
        status_callback: str,
        *,
        capture: PaymentsEnumCaptureOrStr | None = None,
        status: PaymentsEnumStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountCallPayments:
        """update an instance of payments with different phases of payment flows.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will update the
                resource.
            call_sid: The SID of the call that will update the resource. This should be the same call sid that was used
                to create payments resource.
            sid: The SID of Payments session that needs to be updated.
            idempotency_key: A unique token that will be used to ensure that multiple API calls with the same
                information do not result in multiple transactions. This should be a unique string value per API call
                and can be a randomly generated.
            status_callback: Provide an absolute or relative URL to receive status updates regarding your Pay session.
                Read more about the `Update
                <https://www.twilio.com/docs/voice/api/payment-resource#statuscallback-update>`__ and `Complete/Cancel
                <https://www.twilio.com/docs/voice/api/payment-resource#statuscallback-cancelcomplete>`__ POST requests.
            capture: The piece of payment information that you wish the caller to enter. Must be one of
                ``payment-card-number``, ``expiration-date``, ``security-code``, ``postal-code``,
                ``bank-routing-number``, ``bank-account-number``, or their ``-matcher`` variants for input confirmation
                when ``RequireMatchingInputs`` is enabled.
            status: Indicates whether the current payment session should be cancelled or completed. When ``cancel`` the
                payment session is cancelled. When ``complete``, Twilio sends the payment information to the selected
                Pay Connector for processing.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Accepted

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_payments(
                account_sid,
                call_sid,
                sid,
                idempotency_key,
                status_callback,
                capture=capture,
                status=status,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401PaymentWithRawResponse:
        return self._with_raw_response


class Api20100401PaymentWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_payments(
        self,
        account_sid: str,
        call_sid: str,
        idempotency_key: str,
        status_callback: str,
        *,
        bank_account_type: PaymentsEnumBankAccountTypeOrStr | None = None,
        charge_amount: float | None = None,
        currency: str | None = None,
        description: str | None = None,
        input: str | None = None,
        min_postal_code_length: int | None = None,
        parameter: Any | None = None,
        payment_connector: str | None = None,
        payment_method: PaymentsEnumPaymentMethodOrStr | None = None,
        postal_code: bool | None = None,
        security_code: bool | None = None,
        timeout: int | None = None,
        token_type: PaymentsEnumTokenTypeOrStr | None = None,
        valid_card_types: str | None = None,
        require_matching_inputs: str | None = None,
        confirmation: ConfirmationOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountCallPayments, RawError]:
        """create an instance of payments. This will start a new payments session

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            call_sid: The SID of the call that will create the resource. Call leg associated with this sid is expected
                to provide payment information thru DTMF.
            idempotency_key: A unique token that will be used to ensure that multiple API calls with the same
                information do not result in multiple transactions. This should be a unique string value per API call
                and can be a randomly generated.
            status_callback: Provide an absolute or relative URL to receive status updates regarding your Pay session.
                Read more about the `expected StatusCallback values
                <https://www.twilio.com/docs/voice/api/payment-resource#statuscallback>`__
            bank_account_type: Type of bank account if payment source is ACH. One of ``consumer-checking``,
                ``consumer-savings``, or ``commercial-checking``. The default value is ``consumer-checking``.
            charge_amount: A positive decimal value less than 1,000,000 to charge against the credit card or bank
                account. Default currency can be overwritten with ``currency`` field. Leave blank or set to 0 to
                tokenize.
            currency: The currency of the ``charge_amount``, formatted as `ISO 4127
                <http://www.iso.org/iso/home/standards/currency_codes.htm>`__ format. The default value is ``USD`` and
                all values allowed from the Pay Connector are accepted.
            description: The description can be used to provide more details regarding the transaction. This information
                is submitted along with the payment details to the Payment Connector which are then posted on the
                transactions.
            input: A list of inputs that should be accepted. Currently only ``dtmf`` is supported. All digits captured
                during a pay session are redacted from the logs.
            min_postal_code_length: A positive integer that is used to validate the length of the ``PostalCode``
                inputted by the user. User must enter this many digits.
            parameter: A single-level JSON object used to pass custom parameters to payment processors. (Required for
                ACH payments). The information that has to be included here depends on the <Pay> Connector. `Read more
                <https://www.twilio.com/console/voice/pay-connectors>`__.
            payment_connector: This is the unique name corresponding to the Pay Connector installed in the Twilio
                Add-ons. Learn more about https://www.twilio.com/console/voice/pay-connectors. The default value is
                ``Default``.
            payment_method: Type of payment being captured. One of ``credit-card`` or ``ach-debit``. The default value
                is ``credit-card``.
            postal_code: Indicates whether the credit card postal code (zip code) is a required piece of payment
                information that must be provided by the caller. The default is ``true``.
            security_code: Indicates whether the credit card security code is a required piece of payment information
                that must be provided by the caller. The default is ``true``.
            timeout: The number of seconds that <Pay> should wait for the caller to press a digit between each
                subsequent digit, after the first one, before moving on to validate the digits captured. The default is
                ``5``, maximum is ``600``.
            token_type: Indicates whether the payment method should be tokenized as a ``one-time``, ``reusable``, or
                ``payment-method`` token. The default value is ``reusable``. Do not enter a charge amount when
                tokenizing. If a charge amount is entered, the payment method will be charged and not tokenized.
            valid_card_types: Credit card types separated by space that Pay should accept. The default value is ``visa
                mastercard amex``
            require_matching_inputs: A comma-separated list of payment information fields that require the caller to
                enter the same value twice for confirmation. Supported values are ``payment-card-number``,
                ``expiration-date``, ``security-code``, and ``postal-code``.
            confirmation: Whether to prompt the caller to confirm their payment information before submitting to the
                payment gateway. If ``true``, the caller will hear the last 4 digits of their card or account number and
                must press 1 to confirm or 2 to cancel. Default is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Payments.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("CallSid", call_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("IdempotencyKey", idempotency_key),
                    param[str]("StatusCallback", status_callback),
                    param[PaymentsEnumBankAccountTypeOrStr | None]("BankAccountType", bank_account_type),
                    param[float | None]("ChargeAmount", charge_amount),
                    param[str | None]("Currency", currency),
                    param[str | None]("Description", description),
                    param[str | None]("Input", input),
                    param[int | None]("MinPostalCodeLength", min_postal_code_length),
                    param[Any | None]("Parameter", parameter),
                    param[str | None]("PaymentConnector", payment_connector),
                    param[PaymentsEnumPaymentMethodOrStr | None]("PaymentMethod", payment_method),
                    param[bool | None]("PostalCode", postal_code),
                    param[bool | None]("SecurityCode", security_code),
                    param[int | None]("Timeout", timeout),
                    param[PaymentsEnumTokenTypeOrStr | None]("TokenType", token_type),
                    param[str | None]("ValidCardTypes", valid_card_types),
                    param[str | None]("RequireMatchingInputs", require_matching_inputs),
                    param[ConfirmationOrStr | None]("Confirmation", confirmation),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountCallPayments],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_payments(
        self,
        account_sid: str,
        call_sid: str,
        sid: str,
        idempotency_key: str,
        status_callback: str,
        *,
        capture: PaymentsEnumCaptureOrStr | None = None,
        status: PaymentsEnumStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountCallPayments, RawError]:
        """update an instance of payments with different phases of payment flows.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will update the
                resource.
            call_sid: The SID of the call that will update the resource. This should be the same call sid that was used
                to create payments resource.
            sid: The SID of Payments session that needs to be updated.
            idempotency_key: A unique token that will be used to ensure that multiple API calls with the same
                information do not result in multiple transactions. This should be a unique string value per API call
                and can be a randomly generated.
            status_callback: Provide an absolute or relative URL to receive status updates regarding your Pay session.
                Read more about the `Update
                <https://www.twilio.com/docs/voice/api/payment-resource#statuscallback-update>`__ and `Complete/Cancel
                <https://www.twilio.com/docs/voice/api/payment-resource#statuscallback-cancelcomplete>`__ POST requests.
            capture: The piece of payment information that you wish the caller to enter. Must be one of
                ``payment-card-number``, ``expiration-date``, ``security-code``, ``postal-code``,
                ``bank-routing-number``, ``bank-account-number``, or their ``-matcher`` variants for input confirmation
                when ``RequireMatchingInputs`` is enabled.
            status: Indicates whether the current payment session should be cancelled or completed. When ``cancel`` the
                payment session is cancelled. When ``complete``, Twilio sends the payment information to the selected
                Pay Connector for processing.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Payments/{Sid}.json"),
            path_params=[
                param[str]("AccountSid", account_sid), param[str]("CallSid", call_sid), param[str]("Sid", sid)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("IdempotencyKey", idempotency_key),
                    param[str]("StatusCallback", status_callback),
                    param[PaymentsEnumCaptureOrStr | None]("Capture", capture),
                    param[PaymentsEnumStatusOrStr | None]("Status", status),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountCallPayments],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401PaymentWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_payments(
        self,
        account_sid: str,
        call_sid: str,
        idempotency_key: str,
        status_callback: str,
        *,
        bank_account_type: PaymentsEnumBankAccountTypeOrStr | None = None,
        charge_amount: float | None = None,
        currency: str | None = None,
        description: str | None = None,
        input: str | None = None,
        min_postal_code_length: int | None = None,
        parameter: Any | None = None,
        payment_connector: str | None = None,
        payment_method: PaymentsEnumPaymentMethodOrStr | None = None,
        postal_code: bool | None = None,
        security_code: bool | None = None,
        timeout: int | None = None,
        token_type: PaymentsEnumTokenTypeOrStr | None = None,
        valid_card_types: str | None = None,
        require_matching_inputs: str | None = None,
        confirmation: ConfirmationOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountCallPayments, RawError]:
        """create an instance of payments. This will start a new payments session

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            call_sid: The SID of the call that will create the resource. Call leg associated with this sid is expected
                to provide payment information thru DTMF.
            idempotency_key: A unique token that will be used to ensure that multiple API calls with the same
                information do not result in multiple transactions. This should be a unique string value per API call
                and can be a randomly generated.
            status_callback: Provide an absolute or relative URL to receive status updates regarding your Pay session.
                Read more about the `expected StatusCallback values
                <https://www.twilio.com/docs/voice/api/payment-resource#statuscallback>`__
            bank_account_type: Type of bank account if payment source is ACH. One of ``consumer-checking``,
                ``consumer-savings``, or ``commercial-checking``. The default value is ``consumer-checking``.
            charge_amount: A positive decimal value less than 1,000,000 to charge against the credit card or bank
                account. Default currency can be overwritten with ``currency`` field. Leave blank or set to 0 to
                tokenize.
            currency: The currency of the ``charge_amount``, formatted as `ISO 4127
                <http://www.iso.org/iso/home/standards/currency_codes.htm>`__ format. The default value is ``USD`` and
                all values allowed from the Pay Connector are accepted.
            description: The description can be used to provide more details regarding the transaction. This information
                is submitted along with the payment details to the Payment Connector which are then posted on the
                transactions.
            input: A list of inputs that should be accepted. Currently only ``dtmf`` is supported. All digits captured
                during a pay session are redacted from the logs.
            min_postal_code_length: A positive integer that is used to validate the length of the ``PostalCode``
                inputted by the user. User must enter this many digits.
            parameter: A single-level JSON object used to pass custom parameters to payment processors. (Required for
                ACH payments). The information that has to be included here depends on the <Pay> Connector. `Read more
                <https://www.twilio.com/console/voice/pay-connectors>`__.
            payment_connector: This is the unique name corresponding to the Pay Connector installed in the Twilio
                Add-ons. Learn more about https://www.twilio.com/console/voice/pay-connectors. The default value is
                ``Default``.
            payment_method: Type of payment being captured. One of ``credit-card`` or ``ach-debit``. The default value
                is ``credit-card``.
            postal_code: Indicates whether the credit card postal code (zip code) is a required piece of payment
                information that must be provided by the caller. The default is ``true``.
            security_code: Indicates whether the credit card security code is a required piece of payment information
                that must be provided by the caller. The default is ``true``.
            timeout: The number of seconds that <Pay> should wait for the caller to press a digit between each
                subsequent digit, after the first one, before moving on to validate the digits captured. The default is
                ``5``, maximum is ``600``.
            token_type: Indicates whether the payment method should be tokenized as a ``one-time``, ``reusable``, or
                ``payment-method`` token. The default value is ``reusable``. Do not enter a charge amount when
                tokenizing. If a charge amount is entered, the payment method will be charged and not tokenized.
            valid_card_types: Credit card types separated by space that Pay should accept. The default value is ``visa
                mastercard amex``
            require_matching_inputs: A comma-separated list of payment information fields that require the caller to
                enter the same value twice for confirmation. Supported values are ``payment-card-number``,
                ``expiration-date``, ``security-code``, and ``postal-code``.
            confirmation: Whether to prompt the caller to confirm their payment information before submitting to the
                payment gateway. If ``true``, the caller will hear the last 4 digits of their card or account number and
                must press 1 to confirm or 2 to cancel. Default is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Payments.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("CallSid", call_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("IdempotencyKey", idempotency_key),
                    param[str]("StatusCallback", status_callback),
                    param[PaymentsEnumBankAccountTypeOrStr | None]("BankAccountType", bank_account_type),
                    param[float | None]("ChargeAmount", charge_amount),
                    param[str | None]("Currency", currency),
                    param[str | None]("Description", description),
                    param[str | None]("Input", input),
                    param[int | None]("MinPostalCodeLength", min_postal_code_length),
                    param[Any | None]("Parameter", parameter),
                    param[str | None]("PaymentConnector", payment_connector),
                    param[PaymentsEnumPaymentMethodOrStr | None]("PaymentMethod", payment_method),
                    param[bool | None]("PostalCode", postal_code),
                    param[bool | None]("SecurityCode", security_code),
                    param[int | None]("Timeout", timeout),
                    param[PaymentsEnumTokenTypeOrStr | None]("TokenType", token_type),
                    param[str | None]("ValidCardTypes", valid_card_types),
                    param[str | None]("RequireMatchingInputs", require_matching_inputs),
                    param[ConfirmationOrStr | None]("Confirmation", confirmation),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountCallPayments],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_payments(
        self,
        account_sid: str,
        call_sid: str,
        sid: str,
        idempotency_key: str,
        status_callback: str,
        *,
        capture: PaymentsEnumCaptureOrStr | None = None,
        status: PaymentsEnumStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountCallPayments, RawError]:
        """update an instance of payments with different phases of payment flows.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will update the
                resource.
            call_sid: The SID of the call that will update the resource. This should be the same call sid that was used
                to create payments resource.
            sid: The SID of Payments session that needs to be updated.
            idempotency_key: A unique token that will be used to ensure that multiple API calls with the same
                information do not result in multiple transactions. This should be a unique string value per API call
                and can be a randomly generated.
            status_callback: Provide an absolute or relative URL to receive status updates regarding your Pay session.
                Read more about the `Update
                <https://www.twilio.com/docs/voice/api/payment-resource#statuscallback-update>`__ and `Complete/Cancel
                <https://www.twilio.com/docs/voice/api/payment-resource#statuscallback-cancelcomplete>`__ POST requests.
            capture: The piece of payment information that you wish the caller to enter. Must be one of
                ``payment-card-number``, ``expiration-date``, ``security-code``, ``postal-code``,
                ``bank-routing-number``, ``bank-account-number``, or their ``-matcher`` variants for input confirmation
                when ``RequireMatchingInputs`` is enabled.
            status: Indicates whether the current payment session should be cancelled or completed. When ``cancel`` the
                payment session is cancelled. When ``complete``, Twilio sends the payment information to the selected
                Pay Connector for processing.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Payments/{Sid}.json"),
            path_params=[
                param[str]("AccountSid", account_sid), param[str]("CallSid", call_sid), param[str]("Sid", sid)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("IdempotencyKey", idempotency_key),
                    param[str]("StatusCallback", status_callback),
                    param[PaymentsEnumCaptureOrStr | None]("Capture", capture),
                    param[PaymentsEnumStatusOrStr | None]("Status", status),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountCallPayments],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
