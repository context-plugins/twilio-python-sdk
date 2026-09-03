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
from ..models.list_destination_alpha_sender_response import ListDestinationAlphaSenderResponse
from ..models.messaging_v1_service_destination_alpha_sender import MessagingV1ServiceDestinationAlphaSender
from ..server.server import Server


class MessagingV1DestinationAlphaSender:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MessagingV1DestinationAlphaSenderWithRawResponse(client, server, auth)

    def create_destination_alpha_sender(
        self,
        service_sid: str,
        alpha_sender: str,
        *,
        iso_country_code: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MessagingV1ServiceDestinationAlphaSender:
        """A Messaging Service resource to add, fetch or remove Destination and Default Alpha Sender IDs from a
        Messaging Service. Destination Alpha Sender can send to a particular ISO country code. Default Alpha Senders can
        send to all countries.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__ to create
                the resource under.
            alpha_sender: The Alphanumeric Sender ID string. Can be up to 11 characters long. Valid characters are A-Z,
                a-z, 0-9, space, hyphen ``-``, plus ``+``, underscore ``_`` and ampersand ``&``. This value cannot
                contain only numbers.
            iso_country_code: The Optional Two Character ISO Country Code the Alphanumeric Sender ID will be used for.
                If the IsoCountryCode is not provided, a default Alpha Sender will be created that can be used across
                all countries.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_destination_alpha_sender(
            service_sid, alpha_sender, iso_country_code=iso_country_code, request_options=request_options
        ).unwrap()

    def delete_destination_alpha_sender(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """A Messaging Service resource to add, fetch or remove Destination and Default Alpha Sender IDs from a
        Messaging Service. Destination Alpha Sender can send to a particular ISO country code. Default Alpha Senders can
        send to all countries.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__ to delete
                the resource from.
            sid: The SID of the AlphaSender resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_destination_alpha_sender(
            service_sid, sid, request_options=request_options
        ).unwrap()

    def fetch_destination_alpha_sender(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MessagingV1ServiceDestinationAlphaSender:
        """A Messaging Service resource to add, fetch or remove Destination and Default Alpha Sender IDs from a
        Messaging Service. Destination Alpha Sender can send to a particular ISO country code. Default Alpha Senders can
        send to all countries.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__ to fetch
                the resource from.
            sid: The SID of the AlphaSender resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_destination_alpha_sender(
            service_sid, sid, request_options=request_options
        ).unwrap()

    def list_destination_alpha_sender(
        self,
        service_sid: str,
        *,
        iso_country_code: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListDestinationAlphaSenderResponse:
        """A Messaging Service resource to add, fetch or remove Destination and Default Alpha Sender IDs from a
        Messaging Service. Destination Alpha Sender can send to a particular ISO country code. Default Alpha Senders can
        send to all countries.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__ to read the
                resources from.
            iso_country_code: Optional filter to return only alphanumeric sender IDs associated with the specified
                two-character ISO country code.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_destination_alpha_sender(
            service_sid,
            iso_country_code=iso_country_code,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> MessagingV1DestinationAlphaSenderWithRawResponse:
        return self._with_raw_response


class AsyncMessagingV1DestinationAlphaSender:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMessagingV1DestinationAlphaSenderWithRawResponse(client, server, auth)

    async def create_destination_alpha_sender(
        self,
        service_sid: str,
        alpha_sender: str,
        *,
        iso_country_code: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MessagingV1ServiceDestinationAlphaSender:
        """A Messaging Service resource to add, fetch or remove Destination and Default Alpha Sender IDs from a
        Messaging Service. Destination Alpha Sender can send to a particular ISO country code. Default Alpha Senders can
        send to all countries.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__ to create
                the resource under.
            alpha_sender: The Alphanumeric Sender ID string. Can be up to 11 characters long. Valid characters are A-Z,
                a-z, 0-9, space, hyphen ``-``, plus ``+``, underscore ``_`` and ampersand ``&``. This value cannot
                contain only numbers.
            iso_country_code: The Optional Two Character ISO Country Code the Alphanumeric Sender ID will be used for.
                If the IsoCountryCode is not provided, a default Alpha Sender will be created that can be used across
                all countries.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_destination_alpha_sender(
                service_sid, alpha_sender, iso_country_code=iso_country_code, request_options=request_options
            )
        ).unwrap()

    async def delete_destination_alpha_sender(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """A Messaging Service resource to add, fetch or remove Destination and Default Alpha Sender IDs from a
        Messaging Service. Destination Alpha Sender can send to a particular ISO country code. Default Alpha Senders can
        send to all countries.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__ to delete
                the resource from.
            sid: The SID of the AlphaSender resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_destination_alpha_sender(
                service_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def fetch_destination_alpha_sender(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MessagingV1ServiceDestinationAlphaSender:
        """A Messaging Service resource to add, fetch or remove Destination and Default Alpha Sender IDs from a
        Messaging Service. Destination Alpha Sender can send to a particular ISO country code. Default Alpha Senders can
        send to all countries.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__ to fetch
                the resource from.
            sid: The SID of the AlphaSender resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_destination_alpha_sender(
                service_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def list_destination_alpha_sender(
        self,
        service_sid: str,
        *,
        iso_country_code: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListDestinationAlphaSenderResponse:
        """A Messaging Service resource to add, fetch or remove Destination and Default Alpha Sender IDs from a
        Messaging Service. Destination Alpha Sender can send to a particular ISO country code. Default Alpha Senders can
        send to all countries.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__ to read the
                resources from.
            iso_country_code: Optional filter to return only alphanumeric sender IDs associated with the specified
                two-character ISO country code.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_destination_alpha_sender(
                service_sid,
                iso_country_code=iso_country_code,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncMessagingV1DestinationAlphaSenderWithRawResponse:
        return self._with_raw_response


class MessagingV1DestinationAlphaSenderWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_destination_alpha_sender(
        self,
        service_sid: str,
        alpha_sender: str,
        *,
        iso_country_code: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MessagingV1ServiceDestinationAlphaSender, RawError]:
        """A Messaging Service resource to add, fetch or remove Destination and Default Alpha Sender IDs from a
        Messaging Service. Destination Alpha Sender can send to a particular ISO country code. Default Alpha Senders can
        send to all countries.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__ to create
                the resource under.
            alpha_sender: The Alphanumeric Sender ID string. Can be up to 11 characters long. Valid characters are A-Z,
                a-z, 0-9, space, hyphen ``-``, plus ``+``, underscore ``_`` and ampersand ``&``. This value cannot
                contain only numbers.
            iso_country_code: The Optional Two Character ISO Country Code the Alphanumeric Sender ID will be used for.
                If the IsoCountryCode is not provided, a default Alpha Sender will be created that can be used across
                all countries.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v1/Services/{ServiceSid}/DestinationAlphaSenders"),
            path_params=[param[str]("ServiceSid", service_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [param[str]("AlphaSender", alpha_sender), param[str | None]("IsoCountryCode", iso_country_code)]
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1ServiceDestinationAlphaSender],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_destination_alpha_sender(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """A Messaging Service resource to add, fetch or remove Destination and Default Alpha Sender IDs from a
        Messaging Service. Destination Alpha Sender can send to a particular ISO country code. Default Alpha Senders can
        send to all countries.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__ to delete
                the resource from.
            sid: The SID of the AlphaSender resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default1("/v1/Services/{ServiceSid}/DestinationAlphaSenders/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_destination_alpha_sender(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV1ServiceDestinationAlphaSender, RawError]:
        """A Messaging Service resource to add, fetch or remove Destination and Default Alpha Sender IDs from a
        Messaging Service. Destination Alpha Sender can send to a particular ISO country code. Default Alpha Senders can
        send to all countries.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__ to fetch
                the resource from.
            sid: The SID of the AlphaSender resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/Services/{ServiceSid}/DestinationAlphaSenders/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1ServiceDestinationAlphaSender],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_destination_alpha_sender(
        self,
        service_sid: str,
        *,
        iso_country_code: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListDestinationAlphaSenderResponse, RawError]:
        """A Messaging Service resource to add, fetch or remove Destination and Default Alpha Sender IDs from a
        Messaging Service. Destination Alpha Sender can send to a particular ISO country code. Default Alpha Senders can
        send to all countries.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__ to read the
                resources from.
            iso_country_code: Optional filter to return only alphanumeric sender IDs associated with the specified
                two-character ISO country code.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/Services/{ServiceSid}/DestinationAlphaSenders"),
            path_params=[param[str]("ServiceSid", service_sid)],
            query_params=[
                param[str | None]("IsoCountryCode", iso_country_code),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListDestinationAlphaSenderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncMessagingV1DestinationAlphaSenderWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def create_destination_alpha_sender(
        self,
        service_sid: str,
        alpha_sender: str,
        *,
        iso_country_code: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MessagingV1ServiceDestinationAlphaSender, RawError]:
        """A Messaging Service resource to add, fetch or remove Destination and Default Alpha Sender IDs from a
        Messaging Service. Destination Alpha Sender can send to a particular ISO country code. Default Alpha Senders can
        send to all countries.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__ to create
                the resource under.
            alpha_sender: The Alphanumeric Sender ID string. Can be up to 11 characters long. Valid characters are A-Z,
                a-z, 0-9, space, hyphen ``-``, plus ``+``, underscore ``_`` and ampersand ``&``. This value cannot
                contain only numbers.
            iso_country_code: The Optional Two Character ISO Country Code the Alphanumeric Sender ID will be used for.
                If the IsoCountryCode is not provided, a default Alpha Sender will be created that can be used across
                all countries.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v1/Services/{ServiceSid}/DestinationAlphaSenders"),
            path_params=[param[str]("ServiceSid", service_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [param[str]("AlphaSender", alpha_sender), param[str | None]("IsoCountryCode", iso_country_code)]
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1ServiceDestinationAlphaSender],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_destination_alpha_sender(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """A Messaging Service resource to add, fetch or remove Destination and Default Alpha Sender IDs from a
        Messaging Service. Destination Alpha Sender can send to a particular ISO country code. Default Alpha Senders can
        send to all countries.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__ to delete
                the resource from.
            sid: The SID of the AlphaSender resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default1("/v1/Services/{ServiceSid}/DestinationAlphaSenders/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_destination_alpha_sender(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV1ServiceDestinationAlphaSender, RawError]:
        """A Messaging Service resource to add, fetch or remove Destination and Default Alpha Sender IDs from a
        Messaging Service. Destination Alpha Sender can send to a particular ISO country code. Default Alpha Senders can
        send to all countries.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__ to fetch
                the resource from.
            sid: The SID of the AlphaSender resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/Services/{ServiceSid}/DestinationAlphaSenders/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1ServiceDestinationAlphaSender],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_destination_alpha_sender(
        self,
        service_sid: str,
        *,
        iso_country_code: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListDestinationAlphaSenderResponse, RawError]:
        """A Messaging Service resource to add, fetch or remove Destination and Default Alpha Sender IDs from a
        Messaging Service. Destination Alpha Sender can send to a particular ISO country code. Default Alpha Senders can
        send to all countries.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__ to read the
                resources from.
            iso_country_code: Optional filter to return only alphanumeric sender IDs associated with the specified
                two-character ISO country code.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/Services/{ServiceSid}/DestinationAlphaSenders"),
            path_params=[param[str]("ServiceSid", service_sid)],
            query_params=[
                param[str | None]("IsoCountryCode", iso_country_code),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListDestinationAlphaSenderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
