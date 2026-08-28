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
from ..models.list_alpha_sender_response import ListAlphaSenderResponse
from ..models.messaging_v1_service_alpha_sender import MessagingV1ServiceAlphaSender
from ..server.server import Server


class MessagingV1AlphaSender:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MessagingV1AlphaSenderWithRawResponse(client, server, auth)

    def create_alpha_sender(
        self, service_sid: str, alpha_sender: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MessagingV1ServiceAlphaSender:
        """A Messaging Service resource to add, fetch or remove an Alpha Sender ID from a Messaging Service.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__ to create
                the resource under.
            alpha_sender: The Alphanumeric Sender ID string. Can be up to 11 characters long. Valid characters are A-Z,
                a-z, 0-9, space, hyphen ``-``, plus ``+``, underscore ``_`` and ampersand ``&``. This value cannot
                contain only numbers.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_alpha_sender(
            service_sid, alpha_sender, request_options=request_options
        ).unwrap()

    def delete_alpha_sender(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """A Messaging Service resource to add, fetch or remove an Alpha Sender ID from a Messaging Service.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__ to delete
                the resource from.
            sid: The SID of the AlphaSender resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_alpha_sender(service_sid, sid, request_options=request_options).unwrap()

    def fetch_alpha_sender(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MessagingV1ServiceAlphaSender:
        """A Messaging Service resource to add, fetch or remove an Alpha Sender ID from a Messaging Service.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__ to fetch
                the resource from.
            sid: The SID of the AlphaSender resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_alpha_sender(service_sid, sid, request_options=request_options).unwrap()

    def list_alpha_sender(
        self,
        service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListAlphaSenderResponse:
        """A Messaging Service resource to add, fetch or remove an Alpha Sender ID from a Messaging Service.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__ to read the
                resources from.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_alpha_sender(
            service_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> MessagingV1AlphaSenderWithRawResponse:
        return self._with_raw_response


class AsyncMessagingV1AlphaSender:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMessagingV1AlphaSenderWithRawResponse(client, server, auth)

    async def create_alpha_sender(
        self, service_sid: str, alpha_sender: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MessagingV1ServiceAlphaSender:
        """A Messaging Service resource to add, fetch or remove an Alpha Sender ID from a Messaging Service.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__ to create
                the resource under.
            alpha_sender: The Alphanumeric Sender ID string. Can be up to 11 characters long. Valid characters are A-Z,
                a-z, 0-9, space, hyphen ``-``, plus ``+``, underscore ``_`` and ampersand ``&``. This value cannot
                contain only numbers.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_alpha_sender(
                service_sid, alpha_sender, request_options=request_options
            )
        ).unwrap()

    async def delete_alpha_sender(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """A Messaging Service resource to add, fetch or remove an Alpha Sender ID from a Messaging Service.

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
            await self._with_raw_response.delete_alpha_sender(service_sid, sid, request_options=request_options)
        ).unwrap()

    async def fetch_alpha_sender(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MessagingV1ServiceAlphaSender:
        """A Messaging Service resource to add, fetch or remove an Alpha Sender ID from a Messaging Service.

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
            await self._with_raw_response.fetch_alpha_sender(service_sid, sid, request_options=request_options)
        ).unwrap()

    async def list_alpha_sender(
        self,
        service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListAlphaSenderResponse:
        """A Messaging Service resource to add, fetch or remove an Alpha Sender ID from a Messaging Service.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__ to read the
                resources from.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_alpha_sender(
                service_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncMessagingV1AlphaSenderWithRawResponse:
        return self._with_raw_response


class MessagingV1AlphaSenderWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_alpha_sender(
        self, service_sid: str, alpha_sender: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV1ServiceAlphaSender, RawError]:
        """A Messaging Service resource to add, fetch or remove an Alpha Sender ID from a Messaging Service.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__ to create
                the resource under.
            alpha_sender: The Alphanumeric Sender ID string. Can be up to 11 characters long. Valid characters are A-Z,
                a-z, 0-9, space, hyphen ``-``, plus ``+``, underscore ``_`` and ampersand ``&``. This value cannot
                contain only numbers.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v1/Services/{ServiceSid}/AlphaSenders"),
            path_params=[param[str]("ServiceSid", service_sid)],
            body=form_body([param[str]("AlphaSender", alpha_sender)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1ServiceAlphaSender],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_alpha_sender(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """A Messaging Service resource to add, fetch or remove an Alpha Sender ID from a Messaging Service.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__ to delete
                the resource from.
            sid: The SID of the AlphaSender resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default1("/v1/Services/{ServiceSid}/AlphaSenders/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_alpha_sender(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV1ServiceAlphaSender, RawError]:
        """A Messaging Service resource to add, fetch or remove an Alpha Sender ID from a Messaging Service.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__ to fetch
                the resource from.
            sid: The SID of the AlphaSender resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/Services/{ServiceSid}/AlphaSenders/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1ServiceAlphaSender],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_alpha_sender(
        self,
        service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListAlphaSenderResponse, RawError]:
        """A Messaging Service resource to add, fetch or remove an Alpha Sender ID from a Messaging Service.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__ to read the
                resources from.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/Services/{ServiceSid}/AlphaSenders"),
            path_params=[param[str]("ServiceSid", service_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListAlphaSenderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncMessagingV1AlphaSenderWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_alpha_sender(
        self, service_sid: str, alpha_sender: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV1ServiceAlphaSender, RawError]:
        """A Messaging Service resource to add, fetch or remove an Alpha Sender ID from a Messaging Service.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__ to create
                the resource under.
            alpha_sender: The Alphanumeric Sender ID string. Can be up to 11 characters long. Valid characters are A-Z,
                a-z, 0-9, space, hyphen ``-``, plus ``+``, underscore ``_`` and ampersand ``&``. This value cannot
                contain only numbers.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v1/Services/{ServiceSid}/AlphaSenders"),
            path_params=[param[str]("ServiceSid", service_sid)],
            body=form_body([param[str]("AlphaSender", alpha_sender)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1ServiceAlphaSender],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_alpha_sender(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """A Messaging Service resource to add, fetch or remove an Alpha Sender ID from a Messaging Service.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__ to delete
                the resource from.
            sid: The SID of the AlphaSender resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default1("/v1/Services/{ServiceSid}/AlphaSenders/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_alpha_sender(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV1ServiceAlphaSender, RawError]:
        """A Messaging Service resource to add, fetch or remove an Alpha Sender ID from a Messaging Service.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__ to fetch
                the resource from.
            sid: The SID of the AlphaSender resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/Services/{ServiceSid}/AlphaSenders/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1ServiceAlphaSender],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_alpha_sender(
        self,
        service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListAlphaSenderResponse, RawError]:
        """A Messaging Service resource to add, fetch or remove an Alpha Sender ID from a Messaging Service.

        Args:
            service_sid: The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__ to read the
                resources from.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/Services/{ServiceSid}/AlphaSenders"),
            path_params=[param[str]("ServiceSid", service_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListAlphaSenderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
