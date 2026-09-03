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
from ..models.verify_v2_safelist import VerifyV2Safelist
from ..server.server import Server


class VerifyV2SafelistApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VerifyV2SafelistApiWithRawResponse(client, server, auth)

    def create_safelist(
        self, phone_number: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VerifyV2Safelist:
        """Add a new phone number to SafeList.

        Args:
            phone_number: The phone number to be added in SafeList. Phone numbers must be in `E.164 format
                <https://www.twilio.com/docs/glossary/what-e164>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_safelist(phone_number, request_options=request_options).unwrap()

    def delete_safelist(self, phone_number: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Remove a phone number from SafeList.

        Args:
            phone_number: The phone number to be removed from SafeList. Phone numbers must be in `E.164 format
                <https://www.twilio.com/docs/glossary/what-e164>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_safelist(phone_number, request_options=request_options).unwrap()

    def fetch_safelist(
        self, phone_number: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VerifyV2Safelist:
        """Check if a phone number exists in SafeList.

        Args:
            phone_number: The phone number to be fetched from SafeList. Phone numbers must be in `E.164 format
                <https://www.twilio.com/docs/glossary/what-e164>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_safelist(phone_number, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> VerifyV2SafelistApiWithRawResponse:
        return self._with_raw_response


class AsyncVerifyV2SafelistApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVerifyV2SafelistApiWithRawResponse(client, server, auth)

    async def create_safelist(
        self, phone_number: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VerifyV2Safelist:
        """Add a new phone number to SafeList.

        Args:
            phone_number: The phone number to be added in SafeList. Phone numbers must be in `E.164 format
                <https://www.twilio.com/docs/glossary/what-e164>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_safelist(phone_number, request_options=request_options)).unwrap()

    async def delete_safelist(self, phone_number: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Remove a phone number from SafeList.

        Args:
            phone_number: The phone number to be removed from SafeList. Phone numbers must be in `E.164 format
                <https://www.twilio.com/docs/glossary/what-e164>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_safelist(phone_number, request_options=request_options)).unwrap()

    async def fetch_safelist(
        self, phone_number: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VerifyV2Safelist:
        """Check if a phone number exists in SafeList.

        Args:
            phone_number: The phone number to be fetched from SafeList. Phone numbers must be in `E.164 format
                <https://www.twilio.com/docs/glossary/what-e164>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_safelist(phone_number, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncVerifyV2SafelistApiWithRawResponse:
        return self._with_raw_response


class VerifyV2SafelistApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_safelist(
        self, phone_number: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VerifyV2Safelist, RawError]:
        """Add a new phone number to SafeList.

        Args:
            phone_number: The phone number to be added in SafeList. Phone numbers must be in `E.164 format
                <https://www.twilio.com/docs/glossary/what-e164>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/v2/SafeList/Numbers"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str]("PhoneNumber", phone_number)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2Safelist],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_safelist(
        self, phone_number: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Remove a phone number from SafeList.

        Args:
            phone_number: The phone number to be removed from SafeList. Phone numbers must be in `E.164 format
                <https://www.twilio.com/docs/glossary/what-e164>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default3("/v2/SafeList/Numbers/{PhoneNumber}"),
            path_params=[param[str]("PhoneNumber", phone_number)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_safelist(
        self, phone_number: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VerifyV2Safelist, RawError]:
        """Check if a phone number exists in SafeList.

        Args:
            phone_number: The phone number to be fetched from SafeList. Phone numbers must be in `E.164 format
                <https://www.twilio.com/docs/glossary/what-e164>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default3("/v2/SafeList/Numbers/{PhoneNumber}"),
            path_params=[param[str]("PhoneNumber", phone_number)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2Safelist],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncVerifyV2SafelistApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_safelist(
        self, phone_number: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VerifyV2Safelist, RawError]:
        """Add a new phone number to SafeList.

        Args:
            phone_number: The phone number to be added in SafeList. Phone numbers must be in `E.164 format
                <https://www.twilio.com/docs/glossary/what-e164>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/v2/SafeList/Numbers"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str]("PhoneNumber", phone_number)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2Safelist],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_safelist(
        self, phone_number: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Remove a phone number from SafeList.

        Args:
            phone_number: The phone number to be removed from SafeList. Phone numbers must be in `E.164 format
                <https://www.twilio.com/docs/glossary/what-e164>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default3("/v2/SafeList/Numbers/{PhoneNumber}"),
            path_params=[param[str]("PhoneNumber", phone_number)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_safelist(
        self, phone_number: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VerifyV2Safelist, RawError]:
        """Check if a phone number exists in SafeList.

        Args:
            phone_number: The phone number to be fetched from SafeList. Phone numbers must be in `E.164 format
                <https://www.twilio.com/docs/glossary/what-e164>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default3("/v2/SafeList/Numbers/{PhoneNumber}"),
            path_params=[param[str]("PhoneNumber", phone_number)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2Safelist],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
