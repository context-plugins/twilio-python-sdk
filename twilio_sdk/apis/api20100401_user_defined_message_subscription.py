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
    empty_response,
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.api_v2010_account_call_user_defined_message_subscription import (
    ApiV2010AccountCallUserDefinedMessageSubscription,
)
from ..models.enums.method3 import Method3OrStr
from ..server.server import Server


class Api20100401UserDefinedMessageSubscription:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401UserDefinedMessageSubscriptionWithRawResponse(client, server, auth)

    def create_user_defined_message_subscription(
        self,
        account_sid: str,
        call_sid: str,
        callback: str,
        *,
        idempotency_key: str | None = None,
        method: Method3OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountCallUserDefinedMessageSubscription:
        """Subscribe to User Defined Messages for a given Call SID.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that subscribed to the
                User Defined Messages.
            call_sid: The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the User Defined
                Messages subscription is associated with. This refers to the Call SID that is producing the user defined
                messages.
            callback: The URL we should call using the ``method`` to send user defined events to your application. URLs
                must contain a valid hostname (underscores are not permitted).
            idempotency_key: A unique string value to identify API call. This should be a unique string value per API
                call and can be a randomly generated.
            method: The HTTP method Twilio will use when requesting the above ``Url``. Either ``GET`` or ``POST``.
                Default is ``POST``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_user_defined_message_subscription(
            account_sid,
            call_sid,
            callback,
            idempotency_key=idempotency_key,
            method=method,
            request_options=request_options,
        ).unwrap()

    def delete_user_defined_message_subscription(
        self, account_sid: str, call_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a specific User Defined Message Subscription.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that subscribed to the
                User Defined Messages.
            call_sid: The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the User Defined
                Message Subscription is associated with. This refers to the Call SID that is producing the User Defined
                Messages.
            sid: The SID that uniquely identifies this User Defined Message Subscription.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_user_defined_message_subscription(
            account_sid, call_sid, sid, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401UserDefinedMessageSubscriptionWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401UserDefinedMessageSubscription:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401UserDefinedMessageSubscriptionWithRawResponse(client, server, auth)

    async def create_user_defined_message_subscription(
        self,
        account_sid: str,
        call_sid: str,
        callback: str,
        *,
        idempotency_key: str | None = None,
        method: Method3OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountCallUserDefinedMessageSubscription:
        """Subscribe to User Defined Messages for a given Call SID.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that subscribed to the
                User Defined Messages.
            call_sid: The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the User Defined
                Messages subscription is associated with. This refers to the Call SID that is producing the user defined
                messages.
            callback: The URL we should call using the ``method`` to send user defined events to your application. URLs
                must contain a valid hostname (underscores are not permitted).
            idempotency_key: A unique string value to identify API call. This should be a unique string value per API
                call and can be a randomly generated.
            method: The HTTP method Twilio will use when requesting the above ``Url``. Either ``GET`` or ``POST``.
                Default is ``POST``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_user_defined_message_subscription(
                account_sid,
                call_sid,
                callback,
                idempotency_key=idempotency_key,
                method=method,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_user_defined_message_subscription(
        self, account_sid: str, call_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a specific User Defined Message Subscription.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that subscribed to the
                User Defined Messages.
            call_sid: The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the User Defined
                Message Subscription is associated with. This refers to the Call SID that is producing the User Defined
                Messages.
            sid: The SID that uniquely identifies this User Defined Message Subscription.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_user_defined_message_subscription(
                account_sid, call_sid, sid, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401UserDefinedMessageSubscriptionWithRawResponse:
        return self._with_raw_response


class Api20100401UserDefinedMessageSubscriptionWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_user_defined_message_subscription(
        self,
        account_sid: str,
        call_sid: str,
        callback: str,
        *,
        idempotency_key: str | None = None,
        method: Method3OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountCallUserDefinedMessageSubscription, RawError]:
        """Subscribe to User Defined Messages for a given Call SID.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that subscribed to the
                User Defined Messages.
            call_sid: The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the User Defined
                Messages subscription is associated with. This refers to the Call SID that is producing the user defined
                messages.
            callback: The URL we should call using the ``method`` to send user defined events to your application. URLs
                must contain a valid hostname (underscores are not permitted).
            idempotency_key: A unique string value to identify API call. This should be a unique string value per API
                call and can be a randomly generated.
            method: The HTTP method Twilio will use when requesting the above ``Url``. Either ``GET`` or ``POST``.
                Default is ``POST``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/UserDefinedMessageSubscriptions.json"
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("CallSid", call_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("Callback", callback),
                    param[str | None]("IdempotencyKey", idempotency_key),
                    param[Method3OrStr | None]("Method", method),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountCallUserDefinedMessageSubscription],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_user_defined_message_subscription(
        self, account_sid: str, call_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific User Defined Message Subscription.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that subscribed to the
                User Defined Messages.
            call_sid: The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the User Defined
                Message Subscription is associated with. This refers to the Call SID that is producing the User Defined
                Messages.
            sid: The SID that uniquely identifies this User Defined Message Subscription.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/UserDefinedMessageSubscriptions/{Sid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid), param[str]("CallSid", call_sid), param[str]("Sid", sid)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401UserDefinedMessageSubscriptionWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def create_user_defined_message_subscription(
        self,
        account_sid: str,
        call_sid: str,
        callback: str,
        *,
        idempotency_key: str | None = None,
        method: Method3OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountCallUserDefinedMessageSubscription, RawError]:
        """Subscribe to User Defined Messages for a given Call SID.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that subscribed to the
                User Defined Messages.
            call_sid: The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the User Defined
                Messages subscription is associated with. This refers to the Call SID that is producing the user defined
                messages.
            callback: The URL we should call using the ``method`` to send user defined events to your application. URLs
                must contain a valid hostname (underscores are not permitted).
            idempotency_key: A unique string value to identify API call. This should be a unique string value per API
                call and can be a randomly generated.
            method: The HTTP method Twilio will use when requesting the above ``Url``. Either ``GET`` or ``POST``.
                Default is ``POST``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/UserDefinedMessageSubscriptions.json"
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("CallSid", call_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("Callback", callback),
                    param[str | None]("IdempotencyKey", idempotency_key),
                    param[Method3OrStr | None]("Method", method),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountCallUserDefinedMessageSubscription],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_user_defined_message_subscription(
        self, account_sid: str, call_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific User Defined Message Subscription.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that subscribed to the
                User Defined Messages.
            call_sid: The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the User Defined
                Message Subscription is associated with. This refers to the Call SID that is producing the User Defined
                Messages.
            sid: The SID that uniquely identifies this User Defined Message Subscription.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/UserDefinedMessageSubscriptions/{Sid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid), param[str]("CallSid", call_sid), param[str]("Sid", sid)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )
