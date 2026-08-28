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
from ..models.list_phone_number_response1 import ListPhoneNumberResponse1
from ..models.proxy_v1_service_phone_number import ProxyV1ServicePhoneNumber
from ..server.server import Server


class ProxyV1PhoneNumber:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ProxyV1PhoneNumberWithRawResponse(client, server, auth)

    def create_phone_number2(
        self,
        service_sid: str,
        *,
        sid: str | None = None,
        phone_number: str | None = None,
        is_reserved: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProxyV1ServicePhoneNumber:
        """Add a Phone Number to a Service's Proxy Number Pool.

        Args:
            service_sid: The SID parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ resource of the new
                PhoneNumber resource.
            sid: The SID of a Twilio `IncomingPhoneNumber
                <https://www.twilio.com/docs/phone-numbers/api/incomingphonenumber-resource>`__ resource that represents
                the Twilio Number you would like to assign to your Proxy Service.
            phone_number: The phone number in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__ format. E.164
                phone numbers consist of a + followed by the country code and subscriber number without punctuation
                characters. For example, +14155551234.
            is_reserved: Whether the new phone number should be reserved and not be assigned to a participant using
                proxy pool logic. See `Reserved Phone Numbers
                <https://www.twilio.com/docs/proxy/reserved-phone-numbers>`__ for more information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_phone_number2(
            service_sid, sid=sid, phone_number=phone_number, is_reserved=is_reserved, request_options=request_options
        ).unwrap()

    def delete_phone_number2(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a specific Phone Number from a Service.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                PhoneNumber resource to delete.
            sid: The Twilio-provided string that uniquely identifies the PhoneNumber resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_phone_number2(service_sid, sid, request_options=request_options).unwrap()

    def fetch_phone_number4(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ProxyV1ServicePhoneNumber:
        """Fetch a specific Phone Number.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                PhoneNumber resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the PhoneNumber resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_phone_number4(service_sid, sid, request_options=request_options).unwrap()

    def list_phone_number2(
        self,
        service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListPhoneNumberResponse1:
        """Retrieve a list of all Phone Numbers in the Proxy Number Pool for a Service. A maximum of 100 records will be
        returned per page.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                PhoneNumber resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_phone_number2(
            service_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    def update_phone_number(
        self,
        service_sid: str,
        sid: str,
        *,
        is_reserved: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProxyV1ServicePhoneNumber:
        """Update a specific Proxy Number.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                PhoneNumber resource to update.
            sid: The Twilio-provided string that uniquely identifies the PhoneNumber resource to update.
            is_reserved: Whether the phone number should be reserved and not be assigned to a participant using proxy
                pool logic. See `Reserved Phone Numbers <https://www.twilio.com/docs/proxy/reserved-phone-numbers>`__
                for more information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_phone_number(
            service_sid, sid, is_reserved=is_reserved, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ProxyV1PhoneNumberWithRawResponse:
        return self._with_raw_response


class AsyncProxyV1PhoneNumber:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncProxyV1PhoneNumberWithRawResponse(client, server, auth)

    async def create_phone_number2(
        self,
        service_sid: str,
        *,
        sid: str | None = None,
        phone_number: str | None = None,
        is_reserved: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProxyV1ServicePhoneNumber:
        """Add a Phone Number to a Service's Proxy Number Pool.

        Args:
            service_sid: The SID parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ resource of the new
                PhoneNumber resource.
            sid: The SID of a Twilio `IncomingPhoneNumber
                <https://www.twilio.com/docs/phone-numbers/api/incomingphonenumber-resource>`__ resource that represents
                the Twilio Number you would like to assign to your Proxy Service.
            phone_number: The phone number in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__ format. E.164
                phone numbers consist of a + followed by the country code and subscriber number without punctuation
                characters. For example, +14155551234.
            is_reserved: Whether the new phone number should be reserved and not be assigned to a participant using
                proxy pool logic. See `Reserved Phone Numbers
                <https://www.twilio.com/docs/proxy/reserved-phone-numbers>`__ for more information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_phone_number2(
                service_sid,
                sid=sid,
                phone_number=phone_number,
                is_reserved=is_reserved,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_phone_number2(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a specific Phone Number from a Service.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                PhoneNumber resource to delete.
            sid: The Twilio-provided string that uniquely identifies the PhoneNumber resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_phone_number2(service_sid, sid, request_options=request_options)
        ).unwrap()

    async def fetch_phone_number4(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ProxyV1ServicePhoneNumber:
        """Fetch a specific Phone Number.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                PhoneNumber resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the PhoneNumber resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_phone_number4(service_sid, sid, request_options=request_options)
        ).unwrap()

    async def list_phone_number2(
        self,
        service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListPhoneNumberResponse1:
        """Retrieve a list of all Phone Numbers in the Proxy Number Pool for a Service. A maximum of 100 records will be
        returned per page.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                PhoneNumber resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_phone_number2(
                service_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    async def update_phone_number(
        self,
        service_sid: str,
        sid: str,
        *,
        is_reserved: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProxyV1ServicePhoneNumber:
        """Update a specific Proxy Number.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                PhoneNumber resource to update.
            sid: The Twilio-provided string that uniquely identifies the PhoneNumber resource to update.
            is_reserved: Whether the phone number should be reserved and not be assigned to a participant using proxy
                pool logic. See `Reserved Phone Numbers <https://www.twilio.com/docs/proxy/reserved-phone-numbers>`__
                for more information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_phone_number(
                service_sid, sid, is_reserved=is_reserved, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncProxyV1PhoneNumberWithRawResponse:
        return self._with_raw_response


class ProxyV1PhoneNumberWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_phone_number2(
        self,
        service_sid: str,
        *,
        sid: str | None = None,
        phone_number: str | None = None,
        is_reserved: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProxyV1ServicePhoneNumber, RawError]:
        """Add a Phone Number to a Service's Proxy Number Pool.

        Args:
            service_sid: The SID parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ resource of the new
                PhoneNumber resource.
            sid: The SID of a Twilio `IncomingPhoneNumber
                <https://www.twilio.com/docs/phone-numbers/api/incomingphonenumber-resource>`__ resource that represents
                the Twilio Number you would like to assign to your Proxy Service.
            phone_number: The phone number in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__ format. E.164
                phone numbers consist of a + followed by the country code and subscriber number without punctuation
                characters. For example, +14155551234.
            is_reserved: Whether the new phone number should be reserved and not be assigned to a participant using
                proxy pool logic. See `Reserved Phone Numbers
                <https://www.twilio.com/docs/proxy/reserved-phone-numbers>`__ for more information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/v1/Services/{ServiceSid}/PhoneNumbers"),
            path_params=[param[str]("ServiceSid", service_sid)],
            body=form_body(
                [
                    param[str | None]("Sid", sid),
                    param[str | None]("PhoneNumber", phone_number),
                    param[bool | None]("IsReserved", is_reserved),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ProxyV1ServicePhoneNumber],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_phone_number2(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Phone Number from a Service.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                PhoneNumber resource to delete.
            sid: The Twilio-provided string that uniquely identifies the PhoneNumber resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default10("/v1/Services/{ServiceSid}/PhoneNumbers/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_phone_number4(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ProxyV1ServicePhoneNumber, RawError]:
        """Fetch a specific Phone Number.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                PhoneNumber resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the PhoneNumber resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default10("/v1/Services/{ServiceSid}/PhoneNumbers/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ProxyV1ServicePhoneNumber],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_phone_number2(
        self,
        service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListPhoneNumberResponse1, RawError]:
        """Retrieve a list of all Phone Numbers in the Proxy Number Pool for a Service. A maximum of 100 records will be
        returned per page.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                PhoneNumber resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default10("/v1/Services/{ServiceSid}/PhoneNumbers"),
            path_params=[param[str]("ServiceSid", service_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListPhoneNumberResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_phone_number(
        self,
        service_sid: str,
        sid: str,
        *,
        is_reserved: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProxyV1ServicePhoneNumber, RawError]:
        """Update a specific Proxy Number.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                PhoneNumber resource to update.
            sid: The Twilio-provided string that uniquely identifies the PhoneNumber resource to update.
            is_reserved: Whether the phone number should be reserved and not be assigned to a participant using proxy
                pool logic. See `Reserved Phone Numbers <https://www.twilio.com/docs/proxy/reserved-phone-numbers>`__
                for more information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/v1/Services/{ServiceSid}/PhoneNumbers/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            body=form_body([param[bool | None]("IsReserved", is_reserved)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ProxyV1ServicePhoneNumber],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncProxyV1PhoneNumberWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_phone_number2(
        self,
        service_sid: str,
        *,
        sid: str | None = None,
        phone_number: str | None = None,
        is_reserved: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProxyV1ServicePhoneNumber, RawError]:
        """Add a Phone Number to a Service's Proxy Number Pool.

        Args:
            service_sid: The SID parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ resource of the new
                PhoneNumber resource.
            sid: The SID of a Twilio `IncomingPhoneNumber
                <https://www.twilio.com/docs/phone-numbers/api/incomingphonenumber-resource>`__ resource that represents
                the Twilio Number you would like to assign to your Proxy Service.
            phone_number: The phone number in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__ format. E.164
                phone numbers consist of a + followed by the country code and subscriber number without punctuation
                characters. For example, +14155551234.
            is_reserved: Whether the new phone number should be reserved and not be assigned to a participant using
                proxy pool logic. See `Reserved Phone Numbers
                <https://www.twilio.com/docs/proxy/reserved-phone-numbers>`__ for more information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/v1/Services/{ServiceSid}/PhoneNumbers"),
            path_params=[param[str]("ServiceSid", service_sid)],
            body=form_body(
                [
                    param[str | None]("Sid", sid),
                    param[str | None]("PhoneNumber", phone_number),
                    param[bool | None]("IsReserved", is_reserved),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ProxyV1ServicePhoneNumber],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_phone_number2(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Phone Number from a Service.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                PhoneNumber resource to delete.
            sid: The Twilio-provided string that uniquely identifies the PhoneNumber resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default10("/v1/Services/{ServiceSid}/PhoneNumbers/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_phone_number4(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ProxyV1ServicePhoneNumber, RawError]:
        """Fetch a specific Phone Number.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                PhoneNumber resource to fetch.
            sid: The Twilio-provided string that uniquely identifies the PhoneNumber resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default10("/v1/Services/{ServiceSid}/PhoneNumbers/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ProxyV1ServicePhoneNumber],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_phone_number2(
        self,
        service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListPhoneNumberResponse1, RawError]:
        """Retrieve a list of all Phone Numbers in the Proxy Number Pool for a Service. A maximum of 100 records will be
        returned per page.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                PhoneNumber resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default10("/v1/Services/{ServiceSid}/PhoneNumbers"),
            path_params=[param[str]("ServiceSid", service_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListPhoneNumberResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_phone_number(
        self,
        service_sid: str,
        sid: str,
        *,
        is_reserved: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProxyV1ServicePhoneNumber, RawError]:
        """Update a specific Proxy Number.

        Args:
            service_sid: The SID of the parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ of the
                PhoneNumber resource to update.
            sid: The Twilio-provided string that uniquely identifies the PhoneNumber resource to update.
            is_reserved: Whether the phone number should be reserved and not be assigned to a participant using proxy
                pool logic. See `Reserved Phone Numbers <https://www.twilio.com/docs/proxy/reserved-phone-numbers>`__
                for more information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/v1/Services/{ServiceSid}/PhoneNumbers/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            body=form_body([param[bool | None]("IsReserved", is_reserved)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ProxyV1ServicePhoneNumber],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
