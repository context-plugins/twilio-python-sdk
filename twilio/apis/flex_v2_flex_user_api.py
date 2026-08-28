from __future__ import annotations

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
from ..models.flex_v2_flex_user import FlexV2FlexUser
from ..server.server import Server


class FlexV2FlexUserApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FlexV2FlexUserApiWithRawResponse(client, server, auth)

    def fetch_flex_user(
        self, instance_sid: str, flex_user_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FlexV2FlexUser:
        """Fetch flex user for the given flex user sid

        Args:
            instance_sid: The unique ID created by Twilio to identify a Flex instance.
            flex_user_sid: The unique id for the flex user to be retrieved.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_flex_user(
            instance_sid, flex_user_sid, request_options=request_options
        ).unwrap()

    def update_flex_user(
        self,
        instance_sid: str,
        flex_user_sid: str,
        *,
        email: str | None = None,
        user_sid: str | None = None,
        locale: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV2FlexUser:
        """Update flex user for the given flex user sid

        Args:
            instance_sid: The unique ID created by Twilio to identify a Flex instance.
            flex_user_sid: The unique id for the flex user.
            email: Email of the User.
            user_sid: The unique SID identifier of the Twilio Unified User.
            locale: The locale preference of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_flex_user(
            instance_sid, flex_user_sid, email=email, user_sid=user_sid, locale=locale, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> FlexV2FlexUserApiWithRawResponse:
        return self._with_raw_response


class AsyncFlexV2FlexUserApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFlexV2FlexUserApiWithRawResponse(client, server, auth)

    async def fetch_flex_user(
        self, instance_sid: str, flex_user_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FlexV2FlexUser:
        """Fetch flex user for the given flex user sid

        Args:
            instance_sid: The unique ID created by Twilio to identify a Flex instance.
            flex_user_sid: The unique id for the flex user to be retrieved.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_flex_user(instance_sid, flex_user_sid, request_options=request_options)
        ).unwrap()

    async def update_flex_user(
        self,
        instance_sid: str,
        flex_user_sid: str,
        *,
        email: str | None = None,
        user_sid: str | None = None,
        locale: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV2FlexUser:
        """Update flex user for the given flex user sid

        Args:
            instance_sid: The unique ID created by Twilio to identify a Flex instance.
            flex_user_sid: The unique id for the flex user.
            email: Email of the User.
            user_sid: The unique SID identifier of the Twilio Unified User.
            locale: The locale preference of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_flex_user(
                instance_sid,
                flex_user_sid,
                email=email,
                user_sid=user_sid,
                locale=locale,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncFlexV2FlexUserApiWithRawResponse:
        return self._with_raw_response


class FlexV2FlexUserApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_flex_user(
        self, instance_sid: str, flex_user_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FlexV2FlexUser, RawError]:
        """Fetch flex user for the given flex user sid

        Args:
            instance_sid: The unique ID created by Twilio to identify a Flex instance.
            flex_user_sid: The unique id for the flex user to be retrieved.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v2/Instances/{InstanceSid}/Users/{FlexUserSid}"),
            path_params=[param[str]("InstanceSid", instance_sid), param[str]("FlexUserSid", flex_user_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV2FlexUser],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_flex_user(
        self,
        instance_sid: str,
        flex_user_sid: str,
        *,
        email: str | None = None,
        user_sid: str | None = None,
        locale: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV2FlexUser, RawError]:
        """Update flex user for the given flex user sid

        Args:
            instance_sid: The unique ID created by Twilio to identify a Flex instance.
            flex_user_sid: The unique id for the flex user.
            email: Email of the User.
            user_sid: The unique SID identifier of the Twilio Unified User.
            locale: The locale preference of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v2/Instances/{InstanceSid}/Users/{FlexUserSid}"),
            path_params=[param[str]("InstanceSid", instance_sid), param[str]("FlexUserSid", flex_user_sid)],
            body=form_body(
                [
                    param[str | None]("Email", email),
                    param[str | None]("UserSid", user_sid),
                    param[str | None]("Locale", locale),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV2FlexUser],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncFlexV2FlexUserApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_flex_user(
        self, instance_sid: str, flex_user_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FlexV2FlexUser, RawError]:
        """Fetch flex user for the given flex user sid

        Args:
            instance_sid: The unique ID created by Twilio to identify a Flex instance.
            flex_user_sid: The unique id for the flex user to be retrieved.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v2/Instances/{InstanceSid}/Users/{FlexUserSid}"),
            path_params=[param[str]("InstanceSid", instance_sid), param[str]("FlexUserSid", flex_user_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV2FlexUser],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_flex_user(
        self,
        instance_sid: str,
        flex_user_sid: str,
        *,
        email: str | None = None,
        user_sid: str | None = None,
        locale: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV2FlexUser, RawError]:
        """Update flex user for the given flex user sid

        Args:
            instance_sid: The unique ID created by Twilio to identify a Flex instance.
            flex_user_sid: The unique id for the flex user.
            email: Email of the User.
            user_sid: The unique SID identifier of the Twilio Unified User.
            locale: The locale preference of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v2/Instances/{InstanceSid}/Users/{FlexUserSid}"),
            path_params=[param[str]("InstanceSid", instance_sid), param[str]("FlexUserSid", flex_user_sid)],
            body=form_body(
                [
                    param[str | None]("Email", email),
                    param[str | None]("UserSid", user_sid),
                    param[str | None]("Locale", locale),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV2FlexUser],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
