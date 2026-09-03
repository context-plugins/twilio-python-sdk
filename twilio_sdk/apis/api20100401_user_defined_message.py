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
from ..models.api_v2010_account_call_user_defined_message import ApiV2010AccountCallUserDefinedMessage
from ..server.server import Server


class Api20100401UserDefinedMessage:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401UserDefinedMessageWithRawResponse(client, server, auth)

    def create_user_defined_message(
        self,
        account_sid: str,
        call_sid: str,
        content: str,
        *,
        idempotency_key: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountCallUserDefinedMessage:
        """Create a new User Defined Message for the given Call SID.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created User
                Defined Message.
            call_sid: The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the User Defined
                Message is associated with.
            content: The User Defined Message in the form of URL-encoded JSON string.
            idempotency_key: A unique string value to identify API call. This should be a unique string value per API
                call and can be a randomly generated.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_user_defined_message(
            account_sid, call_sid, content, idempotency_key=idempotency_key, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401UserDefinedMessageWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401UserDefinedMessage:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401UserDefinedMessageWithRawResponse(client, server, auth)

    async def create_user_defined_message(
        self,
        account_sid: str,
        call_sid: str,
        content: str,
        *,
        idempotency_key: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountCallUserDefinedMessage:
        """Create a new User Defined Message for the given Call SID.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created User
                Defined Message.
            call_sid: The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the User Defined
                Message is associated with.
            content: The User Defined Message in the form of URL-encoded JSON string.
            idempotency_key: A unique string value to identify API call. This should be a unique string value per API
                call and can be a randomly generated.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_user_defined_message(
                account_sid, call_sid, content, idempotency_key=idempotency_key, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401UserDefinedMessageWithRawResponse:
        return self._with_raw_response


class Api20100401UserDefinedMessageWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_user_defined_message(
        self,
        account_sid: str,
        call_sid: str,
        content: str,
        *,
        idempotency_key: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountCallUserDefinedMessage, RawError]:
        """Create a new User Defined Message for the given Call SID.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created User
                Defined Message.
            call_sid: The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the User Defined
                Message is associated with.
            content: The User Defined Message in the form of URL-encoded JSON string.
            idempotency_key: A unique string value to identify API call. This should be a unique string value per API
                call and can be a randomly generated.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/UserDefinedMessages.json"
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("CallSid", call_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str]("Content", content), param[str | None]("IdempotencyKey", idempotency_key)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountCallUserDefinedMessage],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401UserDefinedMessageWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_user_defined_message(
        self,
        account_sid: str,
        call_sid: str,
        content: str,
        *,
        idempotency_key: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountCallUserDefinedMessage, RawError]:
        """Create a new User Defined Message for the given Call SID.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created User
                Defined Message.
            call_sid: The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the User Defined
                Message is associated with.
            content: The User Defined Message in the form of URL-encoded JSON string.
            idempotency_key: A unique string value to identify API call. This should be a unique string value per API
                call and can be a randomly generated.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/UserDefinedMessages.json"
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("CallSid", call_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str]("Content", content), param[str | None]("IdempotencyKey", idempotency_key)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountCallUserDefinedMessage],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
