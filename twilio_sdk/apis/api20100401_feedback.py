from __future__ import annotations

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
from ..models.api_v2010_account_message_message_feedback import ApiV2010AccountMessageMessageFeedback
from ..models.enums.message_feedback_enum_outcome import MessageFeedbackEnumOutcomeOrStr
from ..server.server import Server


class Api20100401Feedback:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401FeedbackWithRawResponse(client, server, auth)

    def create_message_feedback(
        self,
        account_sid: str,
        message_sid: str,
        *,
        outcome: MessageFeedbackEnumOutcomeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountMessageMessageFeedback:
        """Create Message Feedback to confirm a tracked user action was performed by the recipient of the associated
        Message

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ associated with the
                Message resource for which to create MessageFeedback.
            message_sid: The SID of the Message resource for which to create MessageFeedback.
            outcome: Reported outcome indicating whether there is confirmation that the Message recipient performed a
                tracked user action. Can be: ``unconfirmed`` or ``confirmed``. For more details see `How to Optimize
                Message Deliverability with Message Feedback
                <https://www.twilio.com/docs/messaging/guides/send-message-feedback-to-twilio>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_message_feedback(
            account_sid, message_sid, outcome=outcome, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401FeedbackWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401Feedback:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401FeedbackWithRawResponse(client, server, auth)

    async def create_message_feedback(
        self,
        account_sid: str,
        message_sid: str,
        *,
        outcome: MessageFeedbackEnumOutcomeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountMessageMessageFeedback:
        """Create Message Feedback to confirm a tracked user action was performed by the recipient of the associated
        Message

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ associated with the
                Message resource for which to create MessageFeedback.
            message_sid: The SID of the Message resource for which to create MessageFeedback.
            outcome: Reported outcome indicating whether there is confirmation that the Message recipient performed a
                tracked user action. Can be: ``unconfirmed`` or ``confirmed``. For more details see `How to Optimize
                Message Deliverability with Message Feedback
                <https://www.twilio.com/docs/messaging/guides/send-message-feedback-to-twilio>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_message_feedback(
                account_sid, message_sid, outcome=outcome, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401FeedbackWithRawResponse:
        return self._with_raw_response


class Api20100401FeedbackWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_message_feedback(
        self,
        account_sid: str,
        message_sid: str,
        *,
        outcome: MessageFeedbackEnumOutcomeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountMessageMessageFeedback, RawError]:
        """Create Message Feedback to confirm a tracked user action was performed by the recipient of the associated
        Message

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ associated with the
                Message resource for which to create MessageFeedback.
            message_sid: The SID of the Message resource for which to create MessageFeedback.
            outcome: Reported outcome indicating whether there is confirmation that the Message recipient performed a
                tracked user action. Can be: ``unconfirmed`` or ``confirmed``. For more details see `How to Optimize
                Message Deliverability with Message Feedback
                <https://www.twilio.com/docs/messaging/guides/send-message-feedback-to-twilio>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Messages/{MessageSid}/Feedback.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("MessageSid", message_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[MessageFeedbackEnumOutcomeOrStr | None]("Outcome", outcome)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountMessageMessageFeedback],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401FeedbackWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_message_feedback(
        self,
        account_sid: str,
        message_sid: str,
        *,
        outcome: MessageFeedbackEnumOutcomeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountMessageMessageFeedback, RawError]:
        """Create Message Feedback to confirm a tracked user action was performed by the recipient of the associated
        Message

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ associated with the
                Message resource for which to create MessageFeedback.
            message_sid: The SID of the Message resource for which to create MessageFeedback.
            outcome: Reported outcome indicating whether there is confirmation that the Message recipient performed a
                tracked user action. Can be: ``unconfirmed`` or ``confirmed``. For more details see `How to Optimize
                Message Deliverability with Message Feedback
                <https://www.twilio.com/docs/messaging/guides/send-message-feedback-to-twilio>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Messages/{MessageSid}/Feedback.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("MessageSid", message_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[MessageFeedbackEnumOutcomeOrStr | None]("Outcome", outcome)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountMessageMessageFeedback],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
