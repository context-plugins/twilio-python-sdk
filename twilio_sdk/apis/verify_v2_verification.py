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
from ..errors.create_verification_error import CreateVerificationErrorBody, create_verification_error_mapper
from ..models.enums.message_enum_risk_check import MessageEnumRiskCheckOrStr
from ..models.enums.verification_enum_status import VerificationEnumStatusOrStr
from ..models.verify_v2_service_verification import VerifyV2ServiceVerification
from ..server.server import Server


class VerifyV2Verification:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VerifyV2VerificationWithRawResponse(client, server, auth)

    def create_verification(
        self,
        service_sid: str,
        to: str,
        channel: str,
        *,
        custom_friendly_name: str | None = None,
        custom_message: str | None = None,
        send_digits: str | None = None,
        locale: str | None = None,
        custom_code: str | None = None,
        amount: str | None = None,
        payee: str | None = None,
        rate_limits: Any | None = None,
        channel_configuration: Any | None = None,
        app_hash: str | None = None,
        template_sid: str | None = None,
        template_custom_substitutions: str | None = None,
        device_ip: str | None = None,
        enable_sna_client_token: bool | None = None,
        risk_check: MessageEnumRiskCheckOrStr | None = None,
        tags: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VerifyV2ServiceVerification:
        """Create a new Verification using a Service

        Args:
            service_sid: The SID of the verification `Service <https://www.twilio.com/docs/verify/api/service>`__ to
                create the resource under.
            to: The phone number or `email <https://www.twilio.com/docs/verify/email>`__ to verify. Phone numbers must
                be in `E.164 format <https://www.twilio.com/docs/glossary/what-e164>`__.
            channel: The verification method to use. One of: https://www.twilio.com/docs/verify/email, ``sms``,
                ``whatsapp``, ``call``, ``sna`` or ``auto``.
            custom_friendly_name: A custom user defined friendly name that overwrites the existing one in the
                verification message
            custom_message: The text of a custom message to use for the verification [DEPRECATED].
            send_digits: The digits to send after a phone call is answered, for example, to dial an extension. For more
                information, see the Programmable Voice documentation of `sendDigits
                <https://www.twilio.com/docs/voice/twiml/number#attributes-sendDigits>`__.
            locale: Locale will automatically resolve based on phone number country code for SMS, WhatsApp, and call
                channel verifications. It will fallback to English or the template’s default translation if the selected
                translation is not available. This parameter will override the automatic locale resolution. `See
                supported languages and more information here
                <https://www.twilio.com/docs/verify/supported-languages>`__.
            custom_code: A pre-generated code to use for verification. The code can be between 4 and 10 characters,
                inclusive.
            amount: The amount of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
            payee: The payee of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
            rate_limits: The custom key-value pairs of Programmable Rate Limits. Keys correspond to ``unique_name``
                fields defined when `creating your Rate Limit
                <https://www.twilio.com/docs/verify/api/service-rate-limits>`__. Associated value pairs represent values
                in the request that you are rate limiting on. You may include multiple Rate Limit values in each
                request.
            channel_configuration: https://www.twilio.com/docs/verify/email channel configuration in json format. The
                fields 'from' and 'from_name' are optional but if included the 'from' field must have a valid email
                address.
            app_hash: Your `App Hash
                <https://developers.google.com/identity/sms-retriever/verify#computing_your_apps_hash_string>`__ to be
                appended at the end of your verification SMS body. Applies only to SMS. Example SMS body: ``<#> Your
                AppName verification code is: 1234 He42w354ol9``.
            template_sid: The message `template <https://www.twilio.com/docs/verify/api/templates>`__. If provided, will
                override the default template for the Service. SMS and Voice channels only.
            template_custom_substitutions: A stringified JSON object in which the keys are the template's special
                variables and the values are the variables substitutions.
            device_ip: Strongly encouraged if using the auto channel. The IP address of the client's device. If
                provided, it has to be a valid IPv4 or IPv6 address.
            enable_sna_client_token: An optional Boolean value to indicate the requirement of sna client token in the
                SNA URL invocation response for added security. This token must match in the Verification Check request
                to confirm phone number verification.
            risk_check: Risk_check overrides Fraud Prevention measures like Fraud Guard, Geo Permissions etc per
                verification attempt basis, allowing Verify to block traffic considered fraudulent if enabled or bypass
                active protections if disabled. Can be: ``enable``(default) or ``disable``. For SMS channel only.
            tags: A string containing a JSON map of key value pairs of tags to be recorded as metadata for the message.
                The tags will also be included as part of the verification and message status event type payloads. The
                object may contain up to 10 tags. Keys and values can each be up to 128 characters in length. **This
                value should not contain PII.**
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: Too Many Requests ``error`` is ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return self._with_raw_response.create_verification(
            service_sid,
            to,
            channel,
            custom_friendly_name=custom_friendly_name,
            custom_message=custom_message,
            send_digits=send_digits,
            locale=locale,
            custom_code=custom_code,
            amount=amount,
            payee=payee,
            rate_limits=rate_limits,
            channel_configuration=channel_configuration,
            app_hash=app_hash,
            template_sid=template_sid,
            template_custom_substitutions=template_custom_substitutions,
            device_ip=device_ip,
            enable_sna_client_token=enable_sna_client_token,
            risk_check=risk_check,
            tags=tags,
            request_options=request_options,
        ).unwrap()

    def fetch_verification(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VerifyV2ServiceVerification:
        """Fetch a specific Verification

        Args:
            service_sid: The SID of the verification `Service <https://www.twilio.com/docs/verify/api/service>`__ to
                fetch the resource from.
            sid: The Twilio-provided string that uniquely identifies the Verification resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_verification(service_sid, sid, request_options=request_options).unwrap()

    def update_verification(
        self,
        service_sid: str,
        sid: str,
        status: VerificationEnumStatusOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VerifyV2ServiceVerification:
        """Update a Verification status

        Args:
            service_sid: The SID of the verification `Service <https://www.twilio.com/docs/verify/api/service>`__ to
                update the resource from.
            sid: The Twilio-provided string that uniquely identifies the Verification resource to update.
            status: The status of the verification. Can be: ``pending``, ``approved``, ``canceled``,
                ``max_attempts_reached``, ``deleted``, ``failed`` or ``expired``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_verification(
            service_sid, sid, status, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> VerifyV2VerificationWithRawResponse:
        return self._with_raw_response


class AsyncVerifyV2Verification:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVerifyV2VerificationWithRawResponse(client, server, auth)

    async def create_verification(
        self,
        service_sid: str,
        to: str,
        channel: str,
        *,
        custom_friendly_name: str | None = None,
        custom_message: str | None = None,
        send_digits: str | None = None,
        locale: str | None = None,
        custom_code: str | None = None,
        amount: str | None = None,
        payee: str | None = None,
        rate_limits: Any | None = None,
        channel_configuration: Any | None = None,
        app_hash: str | None = None,
        template_sid: str | None = None,
        template_custom_substitutions: str | None = None,
        device_ip: str | None = None,
        enable_sna_client_token: bool | None = None,
        risk_check: MessageEnumRiskCheckOrStr | None = None,
        tags: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VerifyV2ServiceVerification:
        """Create a new Verification using a Service

        Args:
            service_sid: The SID of the verification `Service <https://www.twilio.com/docs/verify/api/service>`__ to
                create the resource under.
            to: The phone number or `email <https://www.twilio.com/docs/verify/email>`__ to verify. Phone numbers must
                be in `E.164 format <https://www.twilio.com/docs/glossary/what-e164>`__.
            channel: The verification method to use. One of: https://www.twilio.com/docs/verify/email, ``sms``,
                ``whatsapp``, ``call``, ``sna`` or ``auto``.
            custom_friendly_name: A custom user defined friendly name that overwrites the existing one in the
                verification message
            custom_message: The text of a custom message to use for the verification [DEPRECATED].
            send_digits: The digits to send after a phone call is answered, for example, to dial an extension. For more
                information, see the Programmable Voice documentation of `sendDigits
                <https://www.twilio.com/docs/voice/twiml/number#attributes-sendDigits>`__.
            locale: Locale will automatically resolve based on phone number country code for SMS, WhatsApp, and call
                channel verifications. It will fallback to English or the template’s default translation if the selected
                translation is not available. This parameter will override the automatic locale resolution. `See
                supported languages and more information here
                <https://www.twilio.com/docs/verify/supported-languages>`__.
            custom_code: A pre-generated code to use for verification. The code can be between 4 and 10 characters,
                inclusive.
            amount: The amount of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
            payee: The payee of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
            rate_limits: The custom key-value pairs of Programmable Rate Limits. Keys correspond to ``unique_name``
                fields defined when `creating your Rate Limit
                <https://www.twilio.com/docs/verify/api/service-rate-limits>`__. Associated value pairs represent values
                in the request that you are rate limiting on. You may include multiple Rate Limit values in each
                request.
            channel_configuration: https://www.twilio.com/docs/verify/email channel configuration in json format. The
                fields 'from' and 'from_name' are optional but if included the 'from' field must have a valid email
                address.
            app_hash: Your `App Hash
                <https://developers.google.com/identity/sms-retriever/verify#computing_your_apps_hash_string>`__ to be
                appended at the end of your verification SMS body. Applies only to SMS. Example SMS body: ``<#> Your
                AppName verification code is: 1234 He42w354ol9``.
            template_sid: The message `template <https://www.twilio.com/docs/verify/api/templates>`__. If provided, will
                override the default template for the Service. SMS and Voice channels only.
            template_custom_substitutions: A stringified JSON object in which the keys are the template's special
                variables and the values are the variables substitutions.
            device_ip: Strongly encouraged if using the auto channel. The IP address of the client's device. If
                provided, it has to be a valid IPv4 or IPv6 address.
            enable_sna_client_token: An optional Boolean value to indicate the requirement of sna client token in the
                SNA URL invocation response for added security. This token must match in the Verification Check request
                to confirm phone number verification.
            risk_check: Risk_check overrides Fraud Prevention measures like Fraud Guard, Geo Permissions etc per
                verification attempt basis, allowing Verify to block traffic considered fraudulent if enabled or bypass
                active protections if disabled. Can be: ``enable``(default) or ``disable``. For SMS channel only.
            tags: A string containing a JSON map of key value pairs of tags to be recorded as metadata for the message.
                The tags will also be included as part of the verification and message status event type payloads. The
                object may contain up to 10 tags. Keys and values can each be up to 128 characters in length. **This
                value should not contain PII.**
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: Too Many Requests ``error`` is ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return (
            await self._with_raw_response.create_verification(
                service_sid,
                to,
                channel,
                custom_friendly_name=custom_friendly_name,
                custom_message=custom_message,
                send_digits=send_digits,
                locale=locale,
                custom_code=custom_code,
                amount=amount,
                payee=payee,
                rate_limits=rate_limits,
                channel_configuration=channel_configuration,
                app_hash=app_hash,
                template_sid=template_sid,
                template_custom_substitutions=template_custom_substitutions,
                device_ip=device_ip,
                enable_sna_client_token=enable_sna_client_token,
                risk_check=risk_check,
                tags=tags,
                request_options=request_options,
            )
        ).unwrap()

    async def fetch_verification(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VerifyV2ServiceVerification:
        """Fetch a specific Verification

        Args:
            service_sid: The SID of the verification `Service <https://www.twilio.com/docs/verify/api/service>`__ to
                fetch the resource from.
            sid: The Twilio-provided string that uniquely identifies the Verification resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_verification(service_sid, sid, request_options=request_options)
        ).unwrap()

    async def update_verification(
        self,
        service_sid: str,
        sid: str,
        status: VerificationEnumStatusOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VerifyV2ServiceVerification:
        """Update a Verification status

        Args:
            service_sid: The SID of the verification `Service <https://www.twilio.com/docs/verify/api/service>`__ to
                update the resource from.
            sid: The Twilio-provided string that uniquely identifies the Verification resource to update.
            status: The status of the verification. Can be: ``pending``, ``approved``, ``canceled``,
                ``max_attempts_reached``, ``deleted``, ``failed`` or ``expired``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_verification(service_sid, sid, status, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVerifyV2VerificationWithRawResponse:
        return self._with_raw_response


class VerifyV2VerificationWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_verification(
        self,
        service_sid: str,
        to: str,
        channel: str,
        *,
        custom_friendly_name: str | None = None,
        custom_message: str | None = None,
        send_digits: str | None = None,
        locale: str | None = None,
        custom_code: str | None = None,
        amount: str | None = None,
        payee: str | None = None,
        rate_limits: Any | None = None,
        channel_configuration: Any | None = None,
        app_hash: str | None = None,
        template_sid: str | None = None,
        template_custom_substitutions: str | None = None,
        device_ip: str | None = None,
        enable_sna_client_token: bool | None = None,
        risk_check: MessageEnumRiskCheckOrStr | None = None,
        tags: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VerifyV2ServiceVerification, CreateVerificationErrorBody]:
        """Create a new Verification using a Service

        Args:
            service_sid: The SID of the verification `Service <https://www.twilio.com/docs/verify/api/service>`__ to
                create the resource under.
            to: The phone number or `email <https://www.twilio.com/docs/verify/email>`__ to verify. Phone numbers must
                be in `E.164 format <https://www.twilio.com/docs/glossary/what-e164>`__.
            channel: The verification method to use. One of: https://www.twilio.com/docs/verify/email, ``sms``,
                ``whatsapp``, ``call``, ``sna`` or ``auto``.
            custom_friendly_name: A custom user defined friendly name that overwrites the existing one in the
                verification message
            custom_message: The text of a custom message to use for the verification [DEPRECATED].
            send_digits: The digits to send after a phone call is answered, for example, to dial an extension. For more
                information, see the Programmable Voice documentation of `sendDigits
                <https://www.twilio.com/docs/voice/twiml/number#attributes-sendDigits>`__.
            locale: Locale will automatically resolve based on phone number country code for SMS, WhatsApp, and call
                channel verifications. It will fallback to English or the template’s default translation if the selected
                translation is not available. This parameter will override the automatic locale resolution. `See
                supported languages and more information here
                <https://www.twilio.com/docs/verify/supported-languages>`__.
            custom_code: A pre-generated code to use for verification. The code can be between 4 and 10 characters,
                inclusive.
            amount: The amount of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
            payee: The payee of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
            rate_limits: The custom key-value pairs of Programmable Rate Limits. Keys correspond to ``unique_name``
                fields defined when `creating your Rate Limit
                <https://www.twilio.com/docs/verify/api/service-rate-limits>`__. Associated value pairs represent values
                in the request that you are rate limiting on. You may include multiple Rate Limit values in each
                request.
            channel_configuration: https://www.twilio.com/docs/verify/email channel configuration in json format. The
                fields 'from' and 'from_name' are optional but if included the 'from' field must have a valid email
                address.
            app_hash: Your `App Hash
                <https://developers.google.com/identity/sms-retriever/verify#computing_your_apps_hash_string>`__ to be
                appended at the end of your verification SMS body. Applies only to SMS. Example SMS body: ``<#> Your
                AppName verification code is: 1234 He42w354ol9``.
            template_sid: The message `template <https://www.twilio.com/docs/verify/api/templates>`__. If provided, will
                override the default template for the Service. SMS and Voice channels only.
            template_custom_substitutions: A stringified JSON object in which the keys are the template's special
                variables and the values are the variables substitutions.
            device_ip: Strongly encouraged if using the auto channel. The IP address of the client's device. If
                provided, it has to be a valid IPv4 or IPv6 address.
            enable_sna_client_token: An optional Boolean value to indicate the requirement of sna client token in the
                SNA URL invocation response for added security. This token must match in the Verification Check request
                to confirm phone number verification.
            risk_check: Risk_check overrides Fraud Prevention measures like Fraud Guard, Geo Permissions etc per
                verification attempt basis, allowing Verify to block traffic considered fraudulent if enabled or bypass
                active protections if disabled. Can be: ``enable``(default) or ``disable``. For SMS channel only.
            tags: A string containing a JSON map of key value pairs of tags to be recorded as metadata for the message.
                The tags will also be included as part of the verification and message status event type payloads. The
                object may contain up to 10 tags. Keys and values can each be up to 128 characters in length. **This
                value should not contain PII.**
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/Verifications"),
            path_params=[param[str]("ServiceSid", service_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("To", to),
                    param[str]("Channel", channel),
                    param[str | None]("CustomFriendlyName", custom_friendly_name),
                    param[str | None]("CustomMessage", custom_message),
                    param[str | None]("SendDigits", send_digits),
                    param[str | None]("Locale", locale),
                    param[str | None]("CustomCode", custom_code),
                    param[str | None]("Amount", amount),
                    param[str | None]("Payee", payee),
                    param[Any | None]("RateLimits", rate_limits),
                    param[Any | None]("ChannelConfiguration", channel_configuration),
                    param[str | None]("AppHash", app_hash),
                    param[str | None]("TemplateSid", template_sid),
                    param[str | None]("TemplateCustomSubstitutions", template_custom_substitutions),
                    param[str | None]("DeviceIp", device_ip),
                    param[bool | None]("EnableSnaClientToken", enable_sna_client_token),
                    param[MessageEnumRiskCheckOrStr | None]("RiskCheck", risk_check),
                    param[str | None]("Tags", tags),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2ServiceVerification],
            error_mapper=create_verification_error_mapper,
            request_options=request_options,
        )

    def fetch_verification(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VerifyV2ServiceVerification, RawError]:
        """Fetch a specific Verification

        Args:
            service_sid: The SID of the verification `Service <https://www.twilio.com/docs/verify/api/service>`__ to
                fetch the resource from.
            sid: The Twilio-provided string that uniquely identifies the Verification resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/Verifications/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2ServiceVerification],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_verification(
        self,
        service_sid: str,
        sid: str,
        status: VerificationEnumStatusOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VerifyV2ServiceVerification, RawError]:
        """Update a Verification status

        Args:
            service_sid: The SID of the verification `Service <https://www.twilio.com/docs/verify/api/service>`__ to
                update the resource from.
            sid: The Twilio-provided string that uniquely identifies the Verification resource to update.
            status: The status of the verification. Can be: ``pending``, ``approved``, ``canceled``,
                ``max_attempts_reached``, ``deleted``, ``failed`` or ``expired``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/Verifications/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[VerificationEnumStatusOrStr]("Status", status)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2ServiceVerification],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncVerifyV2VerificationWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_verification(
        self,
        service_sid: str,
        to: str,
        channel: str,
        *,
        custom_friendly_name: str | None = None,
        custom_message: str | None = None,
        send_digits: str | None = None,
        locale: str | None = None,
        custom_code: str | None = None,
        amount: str | None = None,
        payee: str | None = None,
        rate_limits: Any | None = None,
        channel_configuration: Any | None = None,
        app_hash: str | None = None,
        template_sid: str | None = None,
        template_custom_substitutions: str | None = None,
        device_ip: str | None = None,
        enable_sna_client_token: bool | None = None,
        risk_check: MessageEnumRiskCheckOrStr | None = None,
        tags: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VerifyV2ServiceVerification, CreateVerificationErrorBody]:
        """Create a new Verification using a Service

        Args:
            service_sid: The SID of the verification `Service <https://www.twilio.com/docs/verify/api/service>`__ to
                create the resource under.
            to: The phone number or `email <https://www.twilio.com/docs/verify/email>`__ to verify. Phone numbers must
                be in `E.164 format <https://www.twilio.com/docs/glossary/what-e164>`__.
            channel: The verification method to use. One of: https://www.twilio.com/docs/verify/email, ``sms``,
                ``whatsapp``, ``call``, ``sna`` or ``auto``.
            custom_friendly_name: A custom user defined friendly name that overwrites the existing one in the
                verification message
            custom_message: The text of a custom message to use for the verification [DEPRECATED].
            send_digits: The digits to send after a phone call is answered, for example, to dial an extension. For more
                information, see the Programmable Voice documentation of `sendDigits
                <https://www.twilio.com/docs/voice/twiml/number#attributes-sendDigits>`__.
            locale: Locale will automatically resolve based on phone number country code for SMS, WhatsApp, and call
                channel verifications. It will fallback to English or the template’s default translation if the selected
                translation is not available. This parameter will override the automatic locale resolution. `See
                supported languages and more information here
                <https://www.twilio.com/docs/verify/supported-languages>`__.
            custom_code: A pre-generated code to use for verification. The code can be between 4 and 10 characters,
                inclusive.
            amount: The amount of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
            payee: The payee of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
            rate_limits: The custom key-value pairs of Programmable Rate Limits. Keys correspond to ``unique_name``
                fields defined when `creating your Rate Limit
                <https://www.twilio.com/docs/verify/api/service-rate-limits>`__. Associated value pairs represent values
                in the request that you are rate limiting on. You may include multiple Rate Limit values in each
                request.
            channel_configuration: https://www.twilio.com/docs/verify/email channel configuration in json format. The
                fields 'from' and 'from_name' are optional but if included the 'from' field must have a valid email
                address.
            app_hash: Your `App Hash
                <https://developers.google.com/identity/sms-retriever/verify#computing_your_apps_hash_string>`__ to be
                appended at the end of your verification SMS body. Applies only to SMS. Example SMS body: ``<#> Your
                AppName verification code is: 1234 He42w354ol9``.
            template_sid: The message `template <https://www.twilio.com/docs/verify/api/templates>`__. If provided, will
                override the default template for the Service. SMS and Voice channels only.
            template_custom_substitutions: A stringified JSON object in which the keys are the template's special
                variables and the values are the variables substitutions.
            device_ip: Strongly encouraged if using the auto channel. The IP address of the client's device. If
                provided, it has to be a valid IPv4 or IPv6 address.
            enable_sna_client_token: An optional Boolean value to indicate the requirement of sna client token in the
                SNA URL invocation response for added security. This token must match in the Verification Check request
                to confirm phone number verification.
            risk_check: Risk_check overrides Fraud Prevention measures like Fraud Guard, Geo Permissions etc per
                verification attempt basis, allowing Verify to block traffic considered fraudulent if enabled or bypass
                active protections if disabled. Can be: ``enable``(default) or ``disable``. For SMS channel only.
            tags: A string containing a JSON map of key value pairs of tags to be recorded as metadata for the message.
                The tags will also be included as part of the verification and message status event type payloads. The
                object may contain up to 10 tags. Keys and values can each be up to 128 characters in length. **This
                value should not contain PII.**
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/Verifications"),
            path_params=[param[str]("ServiceSid", service_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("To", to),
                    param[str]("Channel", channel),
                    param[str | None]("CustomFriendlyName", custom_friendly_name),
                    param[str | None]("CustomMessage", custom_message),
                    param[str | None]("SendDigits", send_digits),
                    param[str | None]("Locale", locale),
                    param[str | None]("CustomCode", custom_code),
                    param[str | None]("Amount", amount),
                    param[str | None]("Payee", payee),
                    param[Any | None]("RateLimits", rate_limits),
                    param[Any | None]("ChannelConfiguration", channel_configuration),
                    param[str | None]("AppHash", app_hash),
                    param[str | None]("TemplateSid", template_sid),
                    param[str | None]("TemplateCustomSubstitutions", template_custom_substitutions),
                    param[str | None]("DeviceIp", device_ip),
                    param[bool | None]("EnableSnaClientToken", enable_sna_client_token),
                    param[MessageEnumRiskCheckOrStr | None]("RiskCheck", risk_check),
                    param[str | None]("Tags", tags),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2ServiceVerification],
            error_mapper=create_verification_error_mapper,
            request_options=request_options,
        )

    async def fetch_verification(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VerifyV2ServiceVerification, RawError]:
        """Fetch a specific Verification

        Args:
            service_sid: The SID of the verification `Service <https://www.twilio.com/docs/verify/api/service>`__ to
                fetch the resource from.
            sid: The Twilio-provided string that uniquely identifies the Verification resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/Verifications/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2ServiceVerification],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_verification(
        self,
        service_sid: str,
        sid: str,
        status: VerificationEnumStatusOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VerifyV2ServiceVerification, RawError]:
        """Update a Verification status

        Args:
            service_sid: The SID of the verification `Service <https://www.twilio.com/docs/verify/api/service>`__ to
                update the resource from.
            sid: The Twilio-provided string that uniquely identifies the Verification resource to update.
            status: The status of the verification. Can be: ``pending``, ``approved``, ``canceled``,
                ``max_attempts_reached``, ``deleted``, ``failed`` or ``expired``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/Verifications/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[VerificationEnumStatusOrStr]("Status", status)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2ServiceVerification],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
