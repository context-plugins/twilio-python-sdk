from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    empty_response,
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.list_service_response1 import ListServiceResponse1
from ..models.verify_v2_service import VerifyV2Service
from ..server.server import Server


class VerifyV2ServiceApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VerifyV2ServiceApiWithRawResponse(client, server, auth)

    def create_service2(
        self,
        friendly_name: str,
        *,
        code_length: int | None = None,
        lookup_enabled: bool | None = None,
        skip_sms_to_landlines: bool | None = None,
        dtmf_input_required: bool | None = None,
        tts_name: str | None = None,
        psd2_enabled: bool | None = None,
        do_not_share_warning_enabled: bool | None = None,
        custom_code_enabled: bool | None = None,
        push_include_date: bool | None = None,
        push_apn_credential_sid: str | None = None,
        push_fcm_credential_sid: str | None = None,
        totp_issuer: str | None = None,
        totp_time_step: int | None = None,
        totp_code_length: int | None = None,
        totp_skew: int | None = None,
        default_template_sid: str | None = None,
        whatsapp_msg_service_sid: str | None = None,
        whatsapp_from: str | None = None,
        passkeys_relying_party_id: str | None = None,
        passkeys_relying_party_name: str | None = None,
        passkeys_relying_party_origins: str | None = None,
        passkeys_authenticator_attachment: str | None = None,
        passkeys_discoverable_credentials: str | None = None,
        passkeys_user_verification: str | None = None,
        verify_event_subscription_enabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VerifyV2Service:
        """Create a new Verification Service.

        Args:
            friendly_name: A descriptive string that you create to describe the verification service. It can be up to 32
                characters long. **This value should not contain PII.**
            code_length: The length of the verification code to generate. Must be an integer value between 4 and 10,
                inclusive.
            lookup_enabled: Whether to perform a lookup with each verification started and return info about the phone
                number.
            skip_sms_to_landlines: Whether to skip sending SMS verifications to landlines. Requires ``lookup_enabled``.
            dtmf_input_required: Whether to ask the user to press a number before delivering the verify code in a phone
                call.
            tts_name: The name of an alternative text-to-speech service to use in phone calls. Applies only to TTS
                languages.
            psd2_enabled: Whether to pass PSD2 transaction parameters when starting a verification.
            do_not_share_warning_enabled: Whether to add a security warning at the end of an SMS verification body.
                Disabled by default and applies only to SMS. Example SMS body: ``Your AppName verification code is:
                1234. Don’t share this code with anyone; our employees will never ask for the code``
            custom_code_enabled: Whether to allow sending verifications with a custom code instead of a randomly
                generated one.
            push_include_date: Optional configuration for the Push factors. If true, include the date in the Challenge's
                response. Otherwise, the date is omitted from the response. See `Challenge
                <https://www.twilio.com/docs/verify/api/challenge>`__ resource’s details parameter for more info.
                Default: false. **Deprecated** do not use this parameter. This timestamp value is the same one as the
                one found in ``date_created``, please use that one instead.
            push_apn_credential_sid: Optional configuration for the Push factors. Set the APN Credential for this
                service. This will allow to send push notifications to iOS devices. See `Credential Resource
                <https://www.twilio.com/docs/notify/api/credential-resource>`__
            push_fcm_credential_sid: Optional configuration for the Push factors. Set the FCM Credential for this
                service. This will allow to send push notifications to Android devices. See `Credential Resource
                <https://www.twilio.com/docs/notify/api/credential-resource>`__
            totp_issuer: Optional configuration for the TOTP factors. Set TOTP Issuer for this service. This will allow
                to configure the issuer of the TOTP URI. Defaults to the service friendly name if not provided.
            totp_time_step: Optional configuration for the TOTP factors. Defines how often, in seconds, are TOTP codes
                generated. i.e, a new TOTP code is generated every time_step seconds. Must be between 20 and 60 seconds,
                inclusive. Defaults to 30 seconds
            totp_code_length: Optional configuration for the TOTP factors. Number of digits for generated TOTP codes.
                Must be between 3 and 8, inclusive. Defaults to 6
            totp_skew: Optional configuration for the TOTP factors. The number of time-steps, past and future, that are
                valid for validation of TOTP codes. Must be between 0 and 2, inclusive. Defaults to 1
            default_template_sid: The default message `template <https://www.twilio.com/docs/verify/api/templates>`__.
                Will be used for all SMS verifications unless explicitly overriden. SMS channel only.
            whatsapp_msg_service_sid: The SID of the Messaging Service containing WhatsApp Sender(s) that Verify will
                use to send WhatsApp messages to your users.
            whatsapp_from: The number to use as the WhatsApp Sender that Verify will use to send WhatsApp messages to
                your users.This WhatsApp Sender must be associated with a Messaging Service SID.
            passkeys_relying_party_id: The Relying Party ID for Passkeys. This is the domain of your application, e.g.
                ``example.com``. It is used to identify your application when creating Passkeys.
            passkeys_relying_party_name: The Relying Party Name for Passkeys. This is the name of your application, e.g.
                ``Example App``. It is used to identify your application when creating Passkeys.
            passkeys_relying_party_origins: The Relying Party Origins for Passkeys. This is the origin of your
                application, e.g. ``login.example.com,www.example.com``. It is used to identify your application when
                creating Passkeys, it can have multiple origins split by ``,``.
            passkeys_authenticator_attachment: The Authenticator Attachment for Passkeys. This is the type of
                authenticator that will be used to create Passkeys. It can be empty or it can have the values
                ``platform``, ``cross-platform`` or ``any``.
            passkeys_discoverable_credentials: Indicates whether credentials must be discoverable by the authenticator.
                It can be empty or it can have the values ``required``, ``preferred`` or ``discouraged``.
            passkeys_user_verification: The User Verification for Passkeys. This is the type of user verification that
                will be used to create Passkeys. It can be empty or it can have the values ``required``, ``preferred``
                or ``discouraged``.
            verify_event_subscription_enabled: Whether to allow verifications from the service to reach the
                stream-events sinks if configured
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_service2(
            friendly_name,
            code_length=code_length,
            lookup_enabled=lookup_enabled,
            skip_sms_to_landlines=skip_sms_to_landlines,
            dtmf_input_required=dtmf_input_required,
            tts_name=tts_name,
            psd2_enabled=psd2_enabled,
            do_not_share_warning_enabled=do_not_share_warning_enabled,
            custom_code_enabled=custom_code_enabled,
            push_include_date=push_include_date,
            push_apn_credential_sid=push_apn_credential_sid,
            push_fcm_credential_sid=push_fcm_credential_sid,
            totp_issuer=totp_issuer,
            totp_time_step=totp_time_step,
            totp_code_length=totp_code_length,
            totp_skew=totp_skew,
            default_template_sid=default_template_sid,
            whatsapp_msg_service_sid=whatsapp_msg_service_sid,
            whatsapp_from=whatsapp_from,
            passkeys_relying_party_id=passkeys_relying_party_id,
            passkeys_relying_party_name=passkeys_relying_party_name,
            passkeys_relying_party_origins=passkeys_relying_party_origins,
            passkeys_authenticator_attachment=passkeys_authenticator_attachment,
            passkeys_discoverable_credentials=passkeys_discoverable_credentials,
            passkeys_user_verification=passkeys_user_verification,
            verify_event_subscription_enabled=verify_event_subscription_enabled,
            request_options=request_options,
        ).unwrap()

    def delete_service2(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Delete a specific Verification Service Instance.

        Args:
            sid: The Twilio-provided string that uniquely identifies the Verification Service resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_service2(sid, request_options=request_options).unwrap()

    def fetch_service2(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> VerifyV2Service:
        """Fetch specific Verification Service Instance.

        Args:
            sid: The Twilio-provided string that uniquely identifies the Verification Service resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_service2(sid, request_options=request_options).unwrap()

    def list_service2(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListServiceResponse1:
        """Retrieve a list of all Verification Services for an account.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_service2(
            page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    def update_service2(
        self,
        sid: str,
        *,
        friendly_name: str | None = None,
        code_length: int | None = None,
        lookup_enabled: bool | None = None,
        skip_sms_to_landlines: bool | None = None,
        dtmf_input_required: bool | None = None,
        tts_name: str | None = None,
        psd2_enabled: bool | None = None,
        do_not_share_warning_enabled: bool | None = None,
        custom_code_enabled: bool | None = None,
        push_include_date: bool | None = None,
        push_apn_credential_sid: str | None = None,
        push_fcm_credential_sid: str | None = None,
        totp_issuer: str | None = None,
        totp_time_step: int | None = None,
        totp_code_length: int | None = None,
        totp_skew: int | None = None,
        default_template_sid: str | None = None,
        whatsapp_msg_service_sid: str | None = None,
        whatsapp_from: str | None = None,
        passkeys_relying_party_id: str | None = None,
        passkeys_relying_party_name: str | None = None,
        passkeys_relying_party_origins: str | None = None,
        passkeys_authenticator_attachment: str | None = None,
        passkeys_discoverable_credentials: str | None = None,
        passkeys_user_verification: str | None = None,
        verify_event_subscription_enabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VerifyV2Service:
        """Update a specific Verification Service.

        Args:
            sid: The Twilio-provided string that uniquely identifies the Service resource to update.
            friendly_name: A descriptive string that you create to describe the verification service. It can be up to 32
                characters long. **This value should not contain PII.**
            code_length: The length of the verification code to generate. Must be an integer value between 4 and 10,
                inclusive.
            lookup_enabled: Whether to perform a lookup with each verification started and return info about the phone
                number.
            skip_sms_to_landlines: Whether to skip sending SMS verifications to landlines. Requires ``lookup_enabled``.
            dtmf_input_required: Whether to ask the user to press a number before delivering the verify code in a phone
                call.
            tts_name: The name of an alternative text-to-speech service to use in phone calls. Applies only to TTS
                languages.
            psd2_enabled: Whether to pass PSD2 transaction parameters when starting a verification.
            do_not_share_warning_enabled: Whether to add a privacy warning at the end of an SMS. **Disabled by default
                and applies only for SMS.**
            custom_code_enabled: Whether to allow sending verifications with a custom code instead of a randomly
                generated one.
            push_include_date: Optional configuration for the Push factors. If true, include the date in the Challenge's
                response. Otherwise, the date is omitted from the response. See `Challenge
                <https://www.twilio.com/docs/verify/api/challenge>`__ resource’s details parameter for more info.
                Default: false. **Deprecated** do not use this parameter.
            push_apn_credential_sid: Optional configuration for the Push factors. Set the APN Credential for this
                service. This will allow to send push notifications to iOS devices. See `Credential Resource
                <https://www.twilio.com/docs/notify/api/credential-resource>`__
            push_fcm_credential_sid: Optional configuration for the Push factors. Set the FCM Credential for this
                service. This will allow to send push notifications to Android devices. See `Credential Resource
                <https://www.twilio.com/docs/notify/api/credential-resource>`__
            totp_issuer: Optional configuration for the TOTP factors. Set TOTP Issuer for this service. This will allow
                to configure the issuer of the TOTP URI.
            totp_time_step: Optional configuration for the TOTP factors. Defines how often, in seconds, are TOTP codes
                generated. i.e, a new TOTP code is generated every time_step seconds. Must be between 20 and 60 seconds,
                inclusive. Defaults to 30 seconds
            totp_code_length: Optional configuration for the TOTP factors. Number of digits for generated TOTP codes.
                Must be between 3 and 8, inclusive. Defaults to 6
            totp_skew: Optional configuration for the TOTP factors. The number of time-steps, past and future, that are
                valid for validation of TOTP codes. Must be between 0 and 2, inclusive. Defaults to 1
            default_template_sid: The default message `template <https://www.twilio.com/docs/verify/api/templates>`__.
                Will be used for all SMS verifications unless explicitly overriden. SMS channel only.
            whatsapp_msg_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/services>`__ to associate with the Verification Service.
            whatsapp_from: The WhatsApp number to use as the sender of the verification messages. This number must be
                associated with the WhatsApp Message Service.
            passkeys_relying_party_id: The Relying Party ID for Passkeys. This is the domain of your application, e.g.
                ``example.com``. It is used to identify your application when creating Passkeys.
            passkeys_relying_party_name: The Relying Party Name for Passkeys. This is the name of your application, e.g.
                ``Example App``. It is used to identify your application when creating Passkeys.
            passkeys_relying_party_origins: The Relying Party Origins for Passkeys. This is the origin of your
                application, e.g. ``login.example.com,www.example.com``. It is used to identify your application when
                creating Passkeys, it can have multiple origins split by ``,``.
            passkeys_authenticator_attachment: The Authenticator Attachment for Passkeys. This is the type of
                authenticator that will be used to create Passkeys. It can be empty or it can have the values
                ``platform``, ``cross-platform`` or ``any``.
            passkeys_discoverable_credentials: Indicates whether credentials must be discoverable by the authenticator.
                It can be empty or it can have the values ``required``, ``preferred`` or ``discouraged``.
            passkeys_user_verification: The User Verification for Passkeys. This is the type of user verification that
                will be used to create Passkeys. It can be empty or it can have the values ``required``, ``preferred``
                or ``discouraged``.
            verify_event_subscription_enabled: Whether to allow verifications from the service to reach the
                stream-events sinks if configured
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_service2(
            sid,
            friendly_name=friendly_name,
            code_length=code_length,
            lookup_enabled=lookup_enabled,
            skip_sms_to_landlines=skip_sms_to_landlines,
            dtmf_input_required=dtmf_input_required,
            tts_name=tts_name,
            psd2_enabled=psd2_enabled,
            do_not_share_warning_enabled=do_not_share_warning_enabled,
            custom_code_enabled=custom_code_enabled,
            push_include_date=push_include_date,
            push_apn_credential_sid=push_apn_credential_sid,
            push_fcm_credential_sid=push_fcm_credential_sid,
            totp_issuer=totp_issuer,
            totp_time_step=totp_time_step,
            totp_code_length=totp_code_length,
            totp_skew=totp_skew,
            default_template_sid=default_template_sid,
            whatsapp_msg_service_sid=whatsapp_msg_service_sid,
            whatsapp_from=whatsapp_from,
            passkeys_relying_party_id=passkeys_relying_party_id,
            passkeys_relying_party_name=passkeys_relying_party_name,
            passkeys_relying_party_origins=passkeys_relying_party_origins,
            passkeys_authenticator_attachment=passkeys_authenticator_attachment,
            passkeys_discoverable_credentials=passkeys_discoverable_credentials,
            passkeys_user_verification=passkeys_user_verification,
            verify_event_subscription_enabled=verify_event_subscription_enabled,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> VerifyV2ServiceApiWithRawResponse:
        return self._with_raw_response


class AsyncVerifyV2ServiceApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVerifyV2ServiceApiWithRawResponse(client, server, auth)

    async def create_service2(
        self,
        friendly_name: str,
        *,
        code_length: int | None = None,
        lookup_enabled: bool | None = None,
        skip_sms_to_landlines: bool | None = None,
        dtmf_input_required: bool | None = None,
        tts_name: str | None = None,
        psd2_enabled: bool | None = None,
        do_not_share_warning_enabled: bool | None = None,
        custom_code_enabled: bool | None = None,
        push_include_date: bool | None = None,
        push_apn_credential_sid: str | None = None,
        push_fcm_credential_sid: str | None = None,
        totp_issuer: str | None = None,
        totp_time_step: int | None = None,
        totp_code_length: int | None = None,
        totp_skew: int | None = None,
        default_template_sid: str | None = None,
        whatsapp_msg_service_sid: str | None = None,
        whatsapp_from: str | None = None,
        passkeys_relying_party_id: str | None = None,
        passkeys_relying_party_name: str | None = None,
        passkeys_relying_party_origins: str | None = None,
        passkeys_authenticator_attachment: str | None = None,
        passkeys_discoverable_credentials: str | None = None,
        passkeys_user_verification: str | None = None,
        verify_event_subscription_enabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VerifyV2Service:
        """Create a new Verification Service.

        Args:
            friendly_name: A descriptive string that you create to describe the verification service. It can be up to 32
                characters long. **This value should not contain PII.**
            code_length: The length of the verification code to generate. Must be an integer value between 4 and 10,
                inclusive.
            lookup_enabled: Whether to perform a lookup with each verification started and return info about the phone
                number.
            skip_sms_to_landlines: Whether to skip sending SMS verifications to landlines. Requires ``lookup_enabled``.
            dtmf_input_required: Whether to ask the user to press a number before delivering the verify code in a phone
                call.
            tts_name: The name of an alternative text-to-speech service to use in phone calls. Applies only to TTS
                languages.
            psd2_enabled: Whether to pass PSD2 transaction parameters when starting a verification.
            do_not_share_warning_enabled: Whether to add a security warning at the end of an SMS verification body.
                Disabled by default and applies only to SMS. Example SMS body: ``Your AppName verification code is:
                1234. Don’t share this code with anyone; our employees will never ask for the code``
            custom_code_enabled: Whether to allow sending verifications with a custom code instead of a randomly
                generated one.
            push_include_date: Optional configuration for the Push factors. If true, include the date in the Challenge's
                response. Otherwise, the date is omitted from the response. See `Challenge
                <https://www.twilio.com/docs/verify/api/challenge>`__ resource’s details parameter for more info.
                Default: false. **Deprecated** do not use this parameter. This timestamp value is the same one as the
                one found in ``date_created``, please use that one instead.
            push_apn_credential_sid: Optional configuration for the Push factors. Set the APN Credential for this
                service. This will allow to send push notifications to iOS devices. See `Credential Resource
                <https://www.twilio.com/docs/notify/api/credential-resource>`__
            push_fcm_credential_sid: Optional configuration for the Push factors. Set the FCM Credential for this
                service. This will allow to send push notifications to Android devices. See `Credential Resource
                <https://www.twilio.com/docs/notify/api/credential-resource>`__
            totp_issuer: Optional configuration for the TOTP factors. Set TOTP Issuer for this service. This will allow
                to configure the issuer of the TOTP URI. Defaults to the service friendly name if not provided.
            totp_time_step: Optional configuration for the TOTP factors. Defines how often, in seconds, are TOTP codes
                generated. i.e, a new TOTP code is generated every time_step seconds. Must be between 20 and 60 seconds,
                inclusive. Defaults to 30 seconds
            totp_code_length: Optional configuration for the TOTP factors. Number of digits for generated TOTP codes.
                Must be between 3 and 8, inclusive. Defaults to 6
            totp_skew: Optional configuration for the TOTP factors. The number of time-steps, past and future, that are
                valid for validation of TOTP codes. Must be between 0 and 2, inclusive. Defaults to 1
            default_template_sid: The default message `template <https://www.twilio.com/docs/verify/api/templates>`__.
                Will be used for all SMS verifications unless explicitly overriden. SMS channel only.
            whatsapp_msg_service_sid: The SID of the Messaging Service containing WhatsApp Sender(s) that Verify will
                use to send WhatsApp messages to your users.
            whatsapp_from: The number to use as the WhatsApp Sender that Verify will use to send WhatsApp messages to
                your users.This WhatsApp Sender must be associated with a Messaging Service SID.
            passkeys_relying_party_id: The Relying Party ID for Passkeys. This is the domain of your application, e.g.
                ``example.com``. It is used to identify your application when creating Passkeys.
            passkeys_relying_party_name: The Relying Party Name for Passkeys. This is the name of your application, e.g.
                ``Example App``. It is used to identify your application when creating Passkeys.
            passkeys_relying_party_origins: The Relying Party Origins for Passkeys. This is the origin of your
                application, e.g. ``login.example.com,www.example.com``. It is used to identify your application when
                creating Passkeys, it can have multiple origins split by ``,``.
            passkeys_authenticator_attachment: The Authenticator Attachment for Passkeys. This is the type of
                authenticator that will be used to create Passkeys. It can be empty or it can have the values
                ``platform``, ``cross-platform`` or ``any``.
            passkeys_discoverable_credentials: Indicates whether credentials must be discoverable by the authenticator.
                It can be empty or it can have the values ``required``, ``preferred`` or ``discouraged``.
            passkeys_user_verification: The User Verification for Passkeys. This is the type of user verification that
                will be used to create Passkeys. It can be empty or it can have the values ``required``, ``preferred``
                or ``discouraged``.
            verify_event_subscription_enabled: Whether to allow verifications from the service to reach the
                stream-events sinks if configured
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_service2(
                friendly_name,
                code_length=code_length,
                lookup_enabled=lookup_enabled,
                skip_sms_to_landlines=skip_sms_to_landlines,
                dtmf_input_required=dtmf_input_required,
                tts_name=tts_name,
                psd2_enabled=psd2_enabled,
                do_not_share_warning_enabled=do_not_share_warning_enabled,
                custom_code_enabled=custom_code_enabled,
                push_include_date=push_include_date,
                push_apn_credential_sid=push_apn_credential_sid,
                push_fcm_credential_sid=push_fcm_credential_sid,
                totp_issuer=totp_issuer,
                totp_time_step=totp_time_step,
                totp_code_length=totp_code_length,
                totp_skew=totp_skew,
                default_template_sid=default_template_sid,
                whatsapp_msg_service_sid=whatsapp_msg_service_sid,
                whatsapp_from=whatsapp_from,
                passkeys_relying_party_id=passkeys_relying_party_id,
                passkeys_relying_party_name=passkeys_relying_party_name,
                passkeys_relying_party_origins=passkeys_relying_party_origins,
                passkeys_authenticator_attachment=passkeys_authenticator_attachment,
                passkeys_discoverable_credentials=passkeys_discoverable_credentials,
                passkeys_user_verification=passkeys_user_verification,
                verify_event_subscription_enabled=verify_event_subscription_enabled,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_service2(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Delete a specific Verification Service Instance.

        Args:
            sid: The Twilio-provided string that uniquely identifies the Verification Service resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_service2(sid, request_options=request_options)).unwrap()

    async def fetch_service2(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> VerifyV2Service:
        """Fetch specific Verification Service Instance.

        Args:
            sid: The Twilio-provided string that uniquely identifies the Verification Service resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_service2(sid, request_options=request_options)).unwrap()

    async def list_service2(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListServiceResponse1:
        """Retrieve a list of all Verification Services for an account.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_service2(
                page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    async def update_service2(
        self,
        sid: str,
        *,
        friendly_name: str | None = None,
        code_length: int | None = None,
        lookup_enabled: bool | None = None,
        skip_sms_to_landlines: bool | None = None,
        dtmf_input_required: bool | None = None,
        tts_name: str | None = None,
        psd2_enabled: bool | None = None,
        do_not_share_warning_enabled: bool | None = None,
        custom_code_enabled: bool | None = None,
        push_include_date: bool | None = None,
        push_apn_credential_sid: str | None = None,
        push_fcm_credential_sid: str | None = None,
        totp_issuer: str | None = None,
        totp_time_step: int | None = None,
        totp_code_length: int | None = None,
        totp_skew: int | None = None,
        default_template_sid: str | None = None,
        whatsapp_msg_service_sid: str | None = None,
        whatsapp_from: str | None = None,
        passkeys_relying_party_id: str | None = None,
        passkeys_relying_party_name: str | None = None,
        passkeys_relying_party_origins: str | None = None,
        passkeys_authenticator_attachment: str | None = None,
        passkeys_discoverable_credentials: str | None = None,
        passkeys_user_verification: str | None = None,
        verify_event_subscription_enabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VerifyV2Service:
        """Update a specific Verification Service.

        Args:
            sid: The Twilio-provided string that uniquely identifies the Service resource to update.
            friendly_name: A descriptive string that you create to describe the verification service. It can be up to 32
                characters long. **This value should not contain PII.**
            code_length: The length of the verification code to generate. Must be an integer value between 4 and 10,
                inclusive.
            lookup_enabled: Whether to perform a lookup with each verification started and return info about the phone
                number.
            skip_sms_to_landlines: Whether to skip sending SMS verifications to landlines. Requires ``lookup_enabled``.
            dtmf_input_required: Whether to ask the user to press a number before delivering the verify code in a phone
                call.
            tts_name: The name of an alternative text-to-speech service to use in phone calls. Applies only to TTS
                languages.
            psd2_enabled: Whether to pass PSD2 transaction parameters when starting a verification.
            do_not_share_warning_enabled: Whether to add a privacy warning at the end of an SMS. **Disabled by default
                and applies only for SMS.**
            custom_code_enabled: Whether to allow sending verifications with a custom code instead of a randomly
                generated one.
            push_include_date: Optional configuration for the Push factors. If true, include the date in the Challenge's
                response. Otherwise, the date is omitted from the response. See `Challenge
                <https://www.twilio.com/docs/verify/api/challenge>`__ resource’s details parameter for more info.
                Default: false. **Deprecated** do not use this parameter.
            push_apn_credential_sid: Optional configuration for the Push factors. Set the APN Credential for this
                service. This will allow to send push notifications to iOS devices. See `Credential Resource
                <https://www.twilio.com/docs/notify/api/credential-resource>`__
            push_fcm_credential_sid: Optional configuration for the Push factors. Set the FCM Credential for this
                service. This will allow to send push notifications to Android devices. See `Credential Resource
                <https://www.twilio.com/docs/notify/api/credential-resource>`__
            totp_issuer: Optional configuration for the TOTP factors. Set TOTP Issuer for this service. This will allow
                to configure the issuer of the TOTP URI.
            totp_time_step: Optional configuration for the TOTP factors. Defines how often, in seconds, are TOTP codes
                generated. i.e, a new TOTP code is generated every time_step seconds. Must be between 20 and 60 seconds,
                inclusive. Defaults to 30 seconds
            totp_code_length: Optional configuration for the TOTP factors. Number of digits for generated TOTP codes.
                Must be between 3 and 8, inclusive. Defaults to 6
            totp_skew: Optional configuration for the TOTP factors. The number of time-steps, past and future, that are
                valid for validation of TOTP codes. Must be between 0 and 2, inclusive. Defaults to 1
            default_template_sid: The default message `template <https://www.twilio.com/docs/verify/api/templates>`__.
                Will be used for all SMS verifications unless explicitly overriden. SMS channel only.
            whatsapp_msg_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/services>`__ to associate with the Verification Service.
            whatsapp_from: The WhatsApp number to use as the sender of the verification messages. This number must be
                associated with the WhatsApp Message Service.
            passkeys_relying_party_id: The Relying Party ID for Passkeys. This is the domain of your application, e.g.
                ``example.com``. It is used to identify your application when creating Passkeys.
            passkeys_relying_party_name: The Relying Party Name for Passkeys. This is the name of your application, e.g.
                ``Example App``. It is used to identify your application when creating Passkeys.
            passkeys_relying_party_origins: The Relying Party Origins for Passkeys. This is the origin of your
                application, e.g. ``login.example.com,www.example.com``. It is used to identify your application when
                creating Passkeys, it can have multiple origins split by ``,``.
            passkeys_authenticator_attachment: The Authenticator Attachment for Passkeys. This is the type of
                authenticator that will be used to create Passkeys. It can be empty or it can have the values
                ``platform``, ``cross-platform`` or ``any``.
            passkeys_discoverable_credentials: Indicates whether credentials must be discoverable by the authenticator.
                It can be empty or it can have the values ``required``, ``preferred`` or ``discouraged``.
            passkeys_user_verification: The User Verification for Passkeys. This is the type of user verification that
                will be used to create Passkeys. It can be empty or it can have the values ``required``, ``preferred``
                or ``discouraged``.
            verify_event_subscription_enabled: Whether to allow verifications from the service to reach the
                stream-events sinks if configured
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_service2(
                sid,
                friendly_name=friendly_name,
                code_length=code_length,
                lookup_enabled=lookup_enabled,
                skip_sms_to_landlines=skip_sms_to_landlines,
                dtmf_input_required=dtmf_input_required,
                tts_name=tts_name,
                psd2_enabled=psd2_enabled,
                do_not_share_warning_enabled=do_not_share_warning_enabled,
                custom_code_enabled=custom_code_enabled,
                push_include_date=push_include_date,
                push_apn_credential_sid=push_apn_credential_sid,
                push_fcm_credential_sid=push_fcm_credential_sid,
                totp_issuer=totp_issuer,
                totp_time_step=totp_time_step,
                totp_code_length=totp_code_length,
                totp_skew=totp_skew,
                default_template_sid=default_template_sid,
                whatsapp_msg_service_sid=whatsapp_msg_service_sid,
                whatsapp_from=whatsapp_from,
                passkeys_relying_party_id=passkeys_relying_party_id,
                passkeys_relying_party_name=passkeys_relying_party_name,
                passkeys_relying_party_origins=passkeys_relying_party_origins,
                passkeys_authenticator_attachment=passkeys_authenticator_attachment,
                passkeys_discoverable_credentials=passkeys_discoverable_credentials,
                passkeys_user_verification=passkeys_user_verification,
                verify_event_subscription_enabled=verify_event_subscription_enabled,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVerifyV2ServiceApiWithRawResponse:
        return self._with_raw_response


class VerifyV2ServiceApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_service2(
        self,
        friendly_name: str,
        *,
        code_length: int | None = None,
        lookup_enabled: bool | None = None,
        skip_sms_to_landlines: bool | None = None,
        dtmf_input_required: bool | None = None,
        tts_name: str | None = None,
        psd2_enabled: bool | None = None,
        do_not_share_warning_enabled: bool | None = None,
        custom_code_enabled: bool | None = None,
        push_include_date: bool | None = None,
        push_apn_credential_sid: str | None = None,
        push_fcm_credential_sid: str | None = None,
        totp_issuer: str | None = None,
        totp_time_step: int | None = None,
        totp_code_length: int | None = None,
        totp_skew: int | None = None,
        default_template_sid: str | None = None,
        whatsapp_msg_service_sid: str | None = None,
        whatsapp_from: str | None = None,
        passkeys_relying_party_id: str | None = None,
        passkeys_relying_party_name: str | None = None,
        passkeys_relying_party_origins: str | None = None,
        passkeys_authenticator_attachment: str | None = None,
        passkeys_discoverable_credentials: str | None = None,
        passkeys_user_verification: str | None = None,
        verify_event_subscription_enabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VerifyV2Service, RawError]:
        """Create a new Verification Service.

        Args:
            friendly_name: A descriptive string that you create to describe the verification service. It can be up to 32
                characters long. **This value should not contain PII.**
            code_length: The length of the verification code to generate. Must be an integer value between 4 and 10,
                inclusive.
            lookup_enabled: Whether to perform a lookup with each verification started and return info about the phone
                number.
            skip_sms_to_landlines: Whether to skip sending SMS verifications to landlines. Requires ``lookup_enabled``.
            dtmf_input_required: Whether to ask the user to press a number before delivering the verify code in a phone
                call.
            tts_name: The name of an alternative text-to-speech service to use in phone calls. Applies only to TTS
                languages.
            psd2_enabled: Whether to pass PSD2 transaction parameters when starting a verification.
            do_not_share_warning_enabled: Whether to add a security warning at the end of an SMS verification body.
                Disabled by default and applies only to SMS. Example SMS body: ``Your AppName verification code is:
                1234. Don’t share this code with anyone; our employees will never ask for the code``
            custom_code_enabled: Whether to allow sending verifications with a custom code instead of a randomly
                generated one.
            push_include_date: Optional configuration for the Push factors. If true, include the date in the Challenge's
                response. Otherwise, the date is omitted from the response. See `Challenge
                <https://www.twilio.com/docs/verify/api/challenge>`__ resource’s details parameter for more info.
                Default: false. **Deprecated** do not use this parameter. This timestamp value is the same one as the
                one found in ``date_created``, please use that one instead.
            push_apn_credential_sid: Optional configuration for the Push factors. Set the APN Credential for this
                service. This will allow to send push notifications to iOS devices. See `Credential Resource
                <https://www.twilio.com/docs/notify/api/credential-resource>`__
            push_fcm_credential_sid: Optional configuration for the Push factors. Set the FCM Credential for this
                service. This will allow to send push notifications to Android devices. See `Credential Resource
                <https://www.twilio.com/docs/notify/api/credential-resource>`__
            totp_issuer: Optional configuration for the TOTP factors. Set TOTP Issuer for this service. This will allow
                to configure the issuer of the TOTP URI. Defaults to the service friendly name if not provided.
            totp_time_step: Optional configuration for the TOTP factors. Defines how often, in seconds, are TOTP codes
                generated. i.e, a new TOTP code is generated every time_step seconds. Must be between 20 and 60 seconds,
                inclusive. Defaults to 30 seconds
            totp_code_length: Optional configuration for the TOTP factors. Number of digits for generated TOTP codes.
                Must be between 3 and 8, inclusive. Defaults to 6
            totp_skew: Optional configuration for the TOTP factors. The number of time-steps, past and future, that are
                valid for validation of TOTP codes. Must be between 0 and 2, inclusive. Defaults to 1
            default_template_sid: The default message `template <https://www.twilio.com/docs/verify/api/templates>`__.
                Will be used for all SMS verifications unless explicitly overriden. SMS channel only.
            whatsapp_msg_service_sid: The SID of the Messaging Service containing WhatsApp Sender(s) that Verify will
                use to send WhatsApp messages to your users.
            whatsapp_from: The number to use as the WhatsApp Sender that Verify will use to send WhatsApp messages to
                your users.This WhatsApp Sender must be associated with a Messaging Service SID.
            passkeys_relying_party_id: The Relying Party ID for Passkeys. This is the domain of your application, e.g.
                ``example.com``. It is used to identify your application when creating Passkeys.
            passkeys_relying_party_name: The Relying Party Name for Passkeys. This is the name of your application, e.g.
                ``Example App``. It is used to identify your application when creating Passkeys.
            passkeys_relying_party_origins: The Relying Party Origins for Passkeys. This is the origin of your
                application, e.g. ``login.example.com,www.example.com``. It is used to identify your application when
                creating Passkeys, it can have multiple origins split by ``,``.
            passkeys_authenticator_attachment: The Authenticator Attachment for Passkeys. This is the type of
                authenticator that will be used to create Passkeys. It can be empty or it can have the values
                ``platform``, ``cross-platform`` or ``any``.
            passkeys_discoverable_credentials: Indicates whether credentials must be discoverable by the authenticator.
                It can be empty or it can have the values ``required``, ``preferred`` or ``discouraged``.
            passkeys_user_verification: The User Verification for Passkeys. This is the type of user verification that
                will be used to create Passkeys. It can be empty or it can have the values ``required``, ``preferred``
                or ``discouraged``.
            verify_event_subscription_enabled: Whether to allow verifications from the service to reach the
                stream-events sinks if configured
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/v2/Services"),
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[int | None]("CodeLength", code_length),
                    param[bool | None]("LookupEnabled", lookup_enabled),
                    param[bool | None]("SkipSmsToLandlines", skip_sms_to_landlines),
                    param[bool | None]("DtmfInputRequired", dtmf_input_required),
                    param[str | None]("TtsName", tts_name),
                    param[bool | None]("Psd2Enabled", psd2_enabled),
                    param[bool | None]("DoNotShareWarningEnabled", do_not_share_warning_enabled),
                    param[bool | None]("CustomCodeEnabled", custom_code_enabled),
                    param[bool | None]("Push.IncludeDate", push_include_date),
                    param[str | None]("Push.ApnCredentialSid", push_apn_credential_sid),
                    param[str | None]("Push.FcmCredentialSid", push_fcm_credential_sid),
                    param[str | None]("Totp.Issuer", totp_issuer),
                    param[int | None]("Totp.TimeStep", totp_time_step),
                    param[int | None]("Totp.CodeLength", totp_code_length),
                    param[int | None]("Totp.Skew", totp_skew),
                    param[str | None]("DefaultTemplateSid", default_template_sid),
                    param[str | None]("Whatsapp.MsgServiceSid", whatsapp_msg_service_sid),
                    param[str | None]("Whatsapp.From", whatsapp_from),
                    param[str | None]("Passkeys.RelyingParty.Id", passkeys_relying_party_id),
                    param[str | None]("Passkeys.RelyingParty.Name", passkeys_relying_party_name),
                    param[str | None]("Passkeys.RelyingParty.Origins", passkeys_relying_party_origins),
                    param[str | None]("Passkeys.AuthenticatorAttachment", passkeys_authenticator_attachment),
                    param[str | None]("Passkeys.DiscoverableCredentials", passkeys_discoverable_credentials),
                    param[str | None]("Passkeys.UserVerification", passkeys_user_verification),
                    param[bool | None]("VerifyEventSubscriptionEnabled", verify_event_subscription_enabled),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2Service],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_service2(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Verification Service Instance.

        Args:
            sid: The Twilio-provided string that uniquely identifies the Verification Service resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default3("/v2/Services/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_service2(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VerifyV2Service, RawError]:
        """Fetch specific Verification Service Instance.

        Args:
            sid: The Twilio-provided string that uniquely identifies the Verification Service resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default3("/v2/Services/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2Service],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_service2(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListServiceResponse1, RawError]:
        """Retrieve a list of all Verification Services for an account.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default3("/v2/Services"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListServiceResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_service2(
        self,
        sid: str,
        *,
        friendly_name: str | None = None,
        code_length: int | None = None,
        lookup_enabled: bool | None = None,
        skip_sms_to_landlines: bool | None = None,
        dtmf_input_required: bool | None = None,
        tts_name: str | None = None,
        psd2_enabled: bool | None = None,
        do_not_share_warning_enabled: bool | None = None,
        custom_code_enabled: bool | None = None,
        push_include_date: bool | None = None,
        push_apn_credential_sid: str | None = None,
        push_fcm_credential_sid: str | None = None,
        totp_issuer: str | None = None,
        totp_time_step: int | None = None,
        totp_code_length: int | None = None,
        totp_skew: int | None = None,
        default_template_sid: str | None = None,
        whatsapp_msg_service_sid: str | None = None,
        whatsapp_from: str | None = None,
        passkeys_relying_party_id: str | None = None,
        passkeys_relying_party_name: str | None = None,
        passkeys_relying_party_origins: str | None = None,
        passkeys_authenticator_attachment: str | None = None,
        passkeys_discoverable_credentials: str | None = None,
        passkeys_user_verification: str | None = None,
        verify_event_subscription_enabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VerifyV2Service, RawError]:
        """Update a specific Verification Service.

        Args:
            sid: The Twilio-provided string that uniquely identifies the Service resource to update.
            friendly_name: A descriptive string that you create to describe the verification service. It can be up to 32
                characters long. **This value should not contain PII.**
            code_length: The length of the verification code to generate. Must be an integer value between 4 and 10,
                inclusive.
            lookup_enabled: Whether to perform a lookup with each verification started and return info about the phone
                number.
            skip_sms_to_landlines: Whether to skip sending SMS verifications to landlines. Requires ``lookup_enabled``.
            dtmf_input_required: Whether to ask the user to press a number before delivering the verify code in a phone
                call.
            tts_name: The name of an alternative text-to-speech service to use in phone calls. Applies only to TTS
                languages.
            psd2_enabled: Whether to pass PSD2 transaction parameters when starting a verification.
            do_not_share_warning_enabled: Whether to add a privacy warning at the end of an SMS. **Disabled by default
                and applies only for SMS.**
            custom_code_enabled: Whether to allow sending verifications with a custom code instead of a randomly
                generated one.
            push_include_date: Optional configuration for the Push factors. If true, include the date in the Challenge's
                response. Otherwise, the date is omitted from the response. See `Challenge
                <https://www.twilio.com/docs/verify/api/challenge>`__ resource’s details parameter for more info.
                Default: false. **Deprecated** do not use this parameter.
            push_apn_credential_sid: Optional configuration for the Push factors. Set the APN Credential for this
                service. This will allow to send push notifications to iOS devices. See `Credential Resource
                <https://www.twilio.com/docs/notify/api/credential-resource>`__
            push_fcm_credential_sid: Optional configuration for the Push factors. Set the FCM Credential for this
                service. This will allow to send push notifications to Android devices. See `Credential Resource
                <https://www.twilio.com/docs/notify/api/credential-resource>`__
            totp_issuer: Optional configuration for the TOTP factors. Set TOTP Issuer for this service. This will allow
                to configure the issuer of the TOTP URI.
            totp_time_step: Optional configuration for the TOTP factors. Defines how often, in seconds, are TOTP codes
                generated. i.e, a new TOTP code is generated every time_step seconds. Must be between 20 and 60 seconds,
                inclusive. Defaults to 30 seconds
            totp_code_length: Optional configuration for the TOTP factors. Number of digits for generated TOTP codes.
                Must be between 3 and 8, inclusive. Defaults to 6
            totp_skew: Optional configuration for the TOTP factors. The number of time-steps, past and future, that are
                valid for validation of TOTP codes. Must be between 0 and 2, inclusive. Defaults to 1
            default_template_sid: The default message `template <https://www.twilio.com/docs/verify/api/templates>`__.
                Will be used for all SMS verifications unless explicitly overriden. SMS channel only.
            whatsapp_msg_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/services>`__ to associate with the Verification Service.
            whatsapp_from: The WhatsApp number to use as the sender of the verification messages. This number must be
                associated with the WhatsApp Message Service.
            passkeys_relying_party_id: The Relying Party ID for Passkeys. This is the domain of your application, e.g.
                ``example.com``. It is used to identify your application when creating Passkeys.
            passkeys_relying_party_name: The Relying Party Name for Passkeys. This is the name of your application, e.g.
                ``Example App``. It is used to identify your application when creating Passkeys.
            passkeys_relying_party_origins: The Relying Party Origins for Passkeys. This is the origin of your
                application, e.g. ``login.example.com,www.example.com``. It is used to identify your application when
                creating Passkeys, it can have multiple origins split by ``,``.
            passkeys_authenticator_attachment: The Authenticator Attachment for Passkeys. This is the type of
                authenticator that will be used to create Passkeys. It can be empty or it can have the values
                ``platform``, ``cross-platform`` or ``any``.
            passkeys_discoverable_credentials: Indicates whether credentials must be discoverable by the authenticator.
                It can be empty or it can have the values ``required``, ``preferred`` or ``discouraged``.
            passkeys_user_verification: The User Verification for Passkeys. This is the type of user verification that
                will be used to create Passkeys. It can be empty or it can have the values ``required``, ``preferred``
                or ``discouraged``.
            verify_event_subscription_enabled: Whether to allow verifications from the service to reach the
                stream-events sinks if configured
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/v2/Services/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[int | None]("CodeLength", code_length),
                    param[bool | None]("LookupEnabled", lookup_enabled),
                    param[bool | None]("SkipSmsToLandlines", skip_sms_to_landlines),
                    param[bool | None]("DtmfInputRequired", dtmf_input_required),
                    param[str | None]("TtsName", tts_name),
                    param[bool | None]("Psd2Enabled", psd2_enabled),
                    param[bool | None]("DoNotShareWarningEnabled", do_not_share_warning_enabled),
                    param[bool | None]("CustomCodeEnabled", custom_code_enabled),
                    param[bool | None]("Push.IncludeDate", push_include_date),
                    param[str | None]("Push.ApnCredentialSid", push_apn_credential_sid),
                    param[str | None]("Push.FcmCredentialSid", push_fcm_credential_sid),
                    param[str | None]("Totp.Issuer", totp_issuer),
                    param[int | None]("Totp.TimeStep", totp_time_step),
                    param[int | None]("Totp.CodeLength", totp_code_length),
                    param[int | None]("Totp.Skew", totp_skew),
                    param[str | None]("DefaultTemplateSid", default_template_sid),
                    param[str | None]("Whatsapp.MsgServiceSid", whatsapp_msg_service_sid),
                    param[str | None]("Whatsapp.From", whatsapp_from),
                    param[str | None]("Passkeys.RelyingParty.Id", passkeys_relying_party_id),
                    param[str | None]("Passkeys.RelyingParty.Name", passkeys_relying_party_name),
                    param[str | None]("Passkeys.RelyingParty.Origins", passkeys_relying_party_origins),
                    param[str | None]("Passkeys.AuthenticatorAttachment", passkeys_authenticator_attachment),
                    param[str | None]("Passkeys.DiscoverableCredentials", passkeys_discoverable_credentials),
                    param[str | None]("Passkeys.UserVerification", passkeys_user_verification),
                    param[bool | None]("VerifyEventSubscriptionEnabled", verify_event_subscription_enabled),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2Service],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncVerifyV2ServiceApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_service2(
        self,
        friendly_name: str,
        *,
        code_length: int | None = None,
        lookup_enabled: bool | None = None,
        skip_sms_to_landlines: bool | None = None,
        dtmf_input_required: bool | None = None,
        tts_name: str | None = None,
        psd2_enabled: bool | None = None,
        do_not_share_warning_enabled: bool | None = None,
        custom_code_enabled: bool | None = None,
        push_include_date: bool | None = None,
        push_apn_credential_sid: str | None = None,
        push_fcm_credential_sid: str | None = None,
        totp_issuer: str | None = None,
        totp_time_step: int | None = None,
        totp_code_length: int | None = None,
        totp_skew: int | None = None,
        default_template_sid: str | None = None,
        whatsapp_msg_service_sid: str | None = None,
        whatsapp_from: str | None = None,
        passkeys_relying_party_id: str | None = None,
        passkeys_relying_party_name: str | None = None,
        passkeys_relying_party_origins: str | None = None,
        passkeys_authenticator_attachment: str | None = None,
        passkeys_discoverable_credentials: str | None = None,
        passkeys_user_verification: str | None = None,
        verify_event_subscription_enabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VerifyV2Service, RawError]:
        """Create a new Verification Service.

        Args:
            friendly_name: A descriptive string that you create to describe the verification service. It can be up to 32
                characters long. **This value should not contain PII.**
            code_length: The length of the verification code to generate. Must be an integer value between 4 and 10,
                inclusive.
            lookup_enabled: Whether to perform a lookup with each verification started and return info about the phone
                number.
            skip_sms_to_landlines: Whether to skip sending SMS verifications to landlines. Requires ``lookup_enabled``.
            dtmf_input_required: Whether to ask the user to press a number before delivering the verify code in a phone
                call.
            tts_name: The name of an alternative text-to-speech service to use in phone calls. Applies only to TTS
                languages.
            psd2_enabled: Whether to pass PSD2 transaction parameters when starting a verification.
            do_not_share_warning_enabled: Whether to add a security warning at the end of an SMS verification body.
                Disabled by default and applies only to SMS. Example SMS body: ``Your AppName verification code is:
                1234. Don’t share this code with anyone; our employees will never ask for the code``
            custom_code_enabled: Whether to allow sending verifications with a custom code instead of a randomly
                generated one.
            push_include_date: Optional configuration for the Push factors. If true, include the date in the Challenge's
                response. Otherwise, the date is omitted from the response. See `Challenge
                <https://www.twilio.com/docs/verify/api/challenge>`__ resource’s details parameter for more info.
                Default: false. **Deprecated** do not use this parameter. This timestamp value is the same one as the
                one found in ``date_created``, please use that one instead.
            push_apn_credential_sid: Optional configuration for the Push factors. Set the APN Credential for this
                service. This will allow to send push notifications to iOS devices. See `Credential Resource
                <https://www.twilio.com/docs/notify/api/credential-resource>`__
            push_fcm_credential_sid: Optional configuration for the Push factors. Set the FCM Credential for this
                service. This will allow to send push notifications to Android devices. See `Credential Resource
                <https://www.twilio.com/docs/notify/api/credential-resource>`__
            totp_issuer: Optional configuration for the TOTP factors. Set TOTP Issuer for this service. This will allow
                to configure the issuer of the TOTP URI. Defaults to the service friendly name if not provided.
            totp_time_step: Optional configuration for the TOTP factors. Defines how often, in seconds, are TOTP codes
                generated. i.e, a new TOTP code is generated every time_step seconds. Must be between 20 and 60 seconds,
                inclusive. Defaults to 30 seconds
            totp_code_length: Optional configuration for the TOTP factors. Number of digits for generated TOTP codes.
                Must be between 3 and 8, inclusive. Defaults to 6
            totp_skew: Optional configuration for the TOTP factors. The number of time-steps, past and future, that are
                valid for validation of TOTP codes. Must be between 0 and 2, inclusive. Defaults to 1
            default_template_sid: The default message `template <https://www.twilio.com/docs/verify/api/templates>`__.
                Will be used for all SMS verifications unless explicitly overriden. SMS channel only.
            whatsapp_msg_service_sid: The SID of the Messaging Service containing WhatsApp Sender(s) that Verify will
                use to send WhatsApp messages to your users.
            whatsapp_from: The number to use as the WhatsApp Sender that Verify will use to send WhatsApp messages to
                your users.This WhatsApp Sender must be associated with a Messaging Service SID.
            passkeys_relying_party_id: The Relying Party ID for Passkeys. This is the domain of your application, e.g.
                ``example.com``. It is used to identify your application when creating Passkeys.
            passkeys_relying_party_name: The Relying Party Name for Passkeys. This is the name of your application, e.g.
                ``Example App``. It is used to identify your application when creating Passkeys.
            passkeys_relying_party_origins: The Relying Party Origins for Passkeys. This is the origin of your
                application, e.g. ``login.example.com,www.example.com``. It is used to identify your application when
                creating Passkeys, it can have multiple origins split by ``,``.
            passkeys_authenticator_attachment: The Authenticator Attachment for Passkeys. This is the type of
                authenticator that will be used to create Passkeys. It can be empty or it can have the values
                ``platform``, ``cross-platform`` or ``any``.
            passkeys_discoverable_credentials: Indicates whether credentials must be discoverable by the authenticator.
                It can be empty or it can have the values ``required``, ``preferred`` or ``discouraged``.
            passkeys_user_verification: The User Verification for Passkeys. This is the type of user verification that
                will be used to create Passkeys. It can be empty or it can have the values ``required``, ``preferred``
                or ``discouraged``.
            verify_event_subscription_enabled: Whether to allow verifications from the service to reach the
                stream-events sinks if configured
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/v2/Services"),
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[int | None]("CodeLength", code_length),
                    param[bool | None]("LookupEnabled", lookup_enabled),
                    param[bool | None]("SkipSmsToLandlines", skip_sms_to_landlines),
                    param[bool | None]("DtmfInputRequired", dtmf_input_required),
                    param[str | None]("TtsName", tts_name),
                    param[bool | None]("Psd2Enabled", psd2_enabled),
                    param[bool | None]("DoNotShareWarningEnabled", do_not_share_warning_enabled),
                    param[bool | None]("CustomCodeEnabled", custom_code_enabled),
                    param[bool | None]("Push.IncludeDate", push_include_date),
                    param[str | None]("Push.ApnCredentialSid", push_apn_credential_sid),
                    param[str | None]("Push.FcmCredentialSid", push_fcm_credential_sid),
                    param[str | None]("Totp.Issuer", totp_issuer),
                    param[int | None]("Totp.TimeStep", totp_time_step),
                    param[int | None]("Totp.CodeLength", totp_code_length),
                    param[int | None]("Totp.Skew", totp_skew),
                    param[str | None]("DefaultTemplateSid", default_template_sid),
                    param[str | None]("Whatsapp.MsgServiceSid", whatsapp_msg_service_sid),
                    param[str | None]("Whatsapp.From", whatsapp_from),
                    param[str | None]("Passkeys.RelyingParty.Id", passkeys_relying_party_id),
                    param[str | None]("Passkeys.RelyingParty.Name", passkeys_relying_party_name),
                    param[str | None]("Passkeys.RelyingParty.Origins", passkeys_relying_party_origins),
                    param[str | None]("Passkeys.AuthenticatorAttachment", passkeys_authenticator_attachment),
                    param[str | None]("Passkeys.DiscoverableCredentials", passkeys_discoverable_credentials),
                    param[str | None]("Passkeys.UserVerification", passkeys_user_verification),
                    param[bool | None]("VerifyEventSubscriptionEnabled", verify_event_subscription_enabled),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2Service],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_service2(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Verification Service Instance.

        Args:
            sid: The Twilio-provided string that uniquely identifies the Verification Service resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default3("/v2/Services/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_service2(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VerifyV2Service, RawError]:
        """Fetch specific Verification Service Instance.

        Args:
            sid: The Twilio-provided string that uniquely identifies the Verification Service resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default3("/v2/Services/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2Service],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_service2(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListServiceResponse1, RawError]:
        """Retrieve a list of all Verification Services for an account.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default3("/v2/Services"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListServiceResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_service2(
        self,
        sid: str,
        *,
        friendly_name: str | None = None,
        code_length: int | None = None,
        lookup_enabled: bool | None = None,
        skip_sms_to_landlines: bool | None = None,
        dtmf_input_required: bool | None = None,
        tts_name: str | None = None,
        psd2_enabled: bool | None = None,
        do_not_share_warning_enabled: bool | None = None,
        custom_code_enabled: bool | None = None,
        push_include_date: bool | None = None,
        push_apn_credential_sid: str | None = None,
        push_fcm_credential_sid: str | None = None,
        totp_issuer: str | None = None,
        totp_time_step: int | None = None,
        totp_code_length: int | None = None,
        totp_skew: int | None = None,
        default_template_sid: str | None = None,
        whatsapp_msg_service_sid: str | None = None,
        whatsapp_from: str | None = None,
        passkeys_relying_party_id: str | None = None,
        passkeys_relying_party_name: str | None = None,
        passkeys_relying_party_origins: str | None = None,
        passkeys_authenticator_attachment: str | None = None,
        passkeys_discoverable_credentials: str | None = None,
        passkeys_user_verification: str | None = None,
        verify_event_subscription_enabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VerifyV2Service, RawError]:
        """Update a specific Verification Service.

        Args:
            sid: The Twilio-provided string that uniquely identifies the Service resource to update.
            friendly_name: A descriptive string that you create to describe the verification service. It can be up to 32
                characters long. **This value should not contain PII.**
            code_length: The length of the verification code to generate. Must be an integer value between 4 and 10,
                inclusive.
            lookup_enabled: Whether to perform a lookup with each verification started and return info about the phone
                number.
            skip_sms_to_landlines: Whether to skip sending SMS verifications to landlines. Requires ``lookup_enabled``.
            dtmf_input_required: Whether to ask the user to press a number before delivering the verify code in a phone
                call.
            tts_name: The name of an alternative text-to-speech service to use in phone calls. Applies only to TTS
                languages.
            psd2_enabled: Whether to pass PSD2 transaction parameters when starting a verification.
            do_not_share_warning_enabled: Whether to add a privacy warning at the end of an SMS. **Disabled by default
                and applies only for SMS.**
            custom_code_enabled: Whether to allow sending verifications with a custom code instead of a randomly
                generated one.
            push_include_date: Optional configuration for the Push factors. If true, include the date in the Challenge's
                response. Otherwise, the date is omitted from the response. See `Challenge
                <https://www.twilio.com/docs/verify/api/challenge>`__ resource’s details parameter for more info.
                Default: false. **Deprecated** do not use this parameter.
            push_apn_credential_sid: Optional configuration for the Push factors. Set the APN Credential for this
                service. This will allow to send push notifications to iOS devices. See `Credential Resource
                <https://www.twilio.com/docs/notify/api/credential-resource>`__
            push_fcm_credential_sid: Optional configuration for the Push factors. Set the FCM Credential for this
                service. This will allow to send push notifications to Android devices. See `Credential Resource
                <https://www.twilio.com/docs/notify/api/credential-resource>`__
            totp_issuer: Optional configuration for the TOTP factors. Set TOTP Issuer for this service. This will allow
                to configure the issuer of the TOTP URI.
            totp_time_step: Optional configuration for the TOTP factors. Defines how often, in seconds, are TOTP codes
                generated. i.e, a new TOTP code is generated every time_step seconds. Must be between 20 and 60 seconds,
                inclusive. Defaults to 30 seconds
            totp_code_length: Optional configuration for the TOTP factors. Number of digits for generated TOTP codes.
                Must be between 3 and 8, inclusive. Defaults to 6
            totp_skew: Optional configuration for the TOTP factors. The number of time-steps, past and future, that are
                valid for validation of TOTP codes. Must be between 0 and 2, inclusive. Defaults to 1
            default_template_sid: The default message `template <https://www.twilio.com/docs/verify/api/templates>`__.
                Will be used for all SMS verifications unless explicitly overriden. SMS channel only.
            whatsapp_msg_service_sid: The SID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/services>`__ to associate with the Verification Service.
            whatsapp_from: The WhatsApp number to use as the sender of the verification messages. This number must be
                associated with the WhatsApp Message Service.
            passkeys_relying_party_id: The Relying Party ID for Passkeys. This is the domain of your application, e.g.
                ``example.com``. It is used to identify your application when creating Passkeys.
            passkeys_relying_party_name: The Relying Party Name for Passkeys. This is the name of your application, e.g.
                ``Example App``. It is used to identify your application when creating Passkeys.
            passkeys_relying_party_origins: The Relying Party Origins for Passkeys. This is the origin of your
                application, e.g. ``login.example.com,www.example.com``. It is used to identify your application when
                creating Passkeys, it can have multiple origins split by ``,``.
            passkeys_authenticator_attachment: The Authenticator Attachment for Passkeys. This is the type of
                authenticator that will be used to create Passkeys. It can be empty or it can have the values
                ``platform``, ``cross-platform`` or ``any``.
            passkeys_discoverable_credentials: Indicates whether credentials must be discoverable by the authenticator.
                It can be empty or it can have the values ``required``, ``preferred`` or ``discouraged``.
            passkeys_user_verification: The User Verification for Passkeys. This is the type of user verification that
                will be used to create Passkeys. It can be empty or it can have the values ``required``, ``preferred``
                or ``discouraged``.
            verify_event_subscription_enabled: Whether to allow verifications from the service to reach the
                stream-events sinks if configured
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/v2/Services/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[int | None]("CodeLength", code_length),
                    param[bool | None]("LookupEnabled", lookup_enabled),
                    param[bool | None]("SkipSmsToLandlines", skip_sms_to_landlines),
                    param[bool | None]("DtmfInputRequired", dtmf_input_required),
                    param[str | None]("TtsName", tts_name),
                    param[bool | None]("Psd2Enabled", psd2_enabled),
                    param[bool | None]("DoNotShareWarningEnabled", do_not_share_warning_enabled),
                    param[bool | None]("CustomCodeEnabled", custom_code_enabled),
                    param[bool | None]("Push.IncludeDate", push_include_date),
                    param[str | None]("Push.ApnCredentialSid", push_apn_credential_sid),
                    param[str | None]("Push.FcmCredentialSid", push_fcm_credential_sid),
                    param[str | None]("Totp.Issuer", totp_issuer),
                    param[int | None]("Totp.TimeStep", totp_time_step),
                    param[int | None]("Totp.CodeLength", totp_code_length),
                    param[int | None]("Totp.Skew", totp_skew),
                    param[str | None]("DefaultTemplateSid", default_template_sid),
                    param[str | None]("Whatsapp.MsgServiceSid", whatsapp_msg_service_sid),
                    param[str | None]("Whatsapp.From", whatsapp_from),
                    param[str | None]("Passkeys.RelyingParty.Id", passkeys_relying_party_id),
                    param[str | None]("Passkeys.RelyingParty.Name", passkeys_relying_party_name),
                    param[str | None]("Passkeys.RelyingParty.Origins", passkeys_relying_party_origins),
                    param[str | None]("Passkeys.AuthenticatorAttachment", passkeys_authenticator_attachment),
                    param[str | None]("Passkeys.DiscoverableCredentials", passkeys_discoverable_credentials),
                    param[str | None]("Passkeys.UserVerification", passkeys_user_verification),
                    param[bool | None]("VerifyEventSubscriptionEnabled", verify_event_subscription_enabled),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2Service],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
