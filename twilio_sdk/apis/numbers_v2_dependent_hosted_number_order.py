from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.enums.dependent_hosted_number_order_enum_status import DependentHostedNumberOrderEnumStatusOrStr
from ..models.list_dependent_hosted_number_order_response import ListDependentHostedNumberOrderResponse
from ..server.server import Server


class NumbersV2DependentHostedNumberOrder:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NumbersV2DependentHostedNumberOrderWithRawResponse(client, server, auth)

    def list_dependent_hosted_number_order(
        self,
        signing_document_sid: str,
        *,
        status: DependentHostedNumberOrderEnumStatusOrStr | None = None,
        phone_number: str | None = None,
        incoming_phone_number_sid: str | None = None,
        friendly_name: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListDependentHostedNumberOrderResponse:
        """Retrieve a list of dependent HostedNumberOrders belonging to the AuthorizationDocument.

        Args:
            signing_document_sid: A 34 character string that uniquely identifies the LOA document associated with this
                HostedNumberOrder.
            status: Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA,
                4. canceled, 5. failed. See the section entitled `Status Values
                <https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource#status-values>`__
                for more information on each of these statuses.
            phone_number: An E164 formatted phone number hosted by this HostedNumberOrder.
            incoming_phone_number_sid: A 34 character string that uniquely identifies the IncomingPhoneNumber resource
                created by this HostedNumberOrder.
            friendly_name: A human readable description of this resource, up to 128 characters.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_dependent_hosted_number_order(
            signing_document_sid,
            status=status,
            phone_number=phone_number,
            incoming_phone_number_sid=incoming_phone_number_sid,
            friendly_name=friendly_name,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> NumbersV2DependentHostedNumberOrderWithRawResponse:
        return self._with_raw_response


class AsyncNumbersV2DependentHostedNumberOrder:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNumbersV2DependentHostedNumberOrderWithRawResponse(client, server, auth)

    async def list_dependent_hosted_number_order(
        self,
        signing_document_sid: str,
        *,
        status: DependentHostedNumberOrderEnumStatusOrStr | None = None,
        phone_number: str | None = None,
        incoming_phone_number_sid: str | None = None,
        friendly_name: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListDependentHostedNumberOrderResponse:
        """Retrieve a list of dependent HostedNumberOrders belonging to the AuthorizationDocument.

        Args:
            signing_document_sid: A 34 character string that uniquely identifies the LOA document associated with this
                HostedNumberOrder.
            status: Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA,
                4. canceled, 5. failed. See the section entitled `Status Values
                <https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource#status-values>`__
                for more information on each of these statuses.
            phone_number: An E164 formatted phone number hosted by this HostedNumberOrder.
            incoming_phone_number_sid: A 34 character string that uniquely identifies the IncomingPhoneNumber resource
                created by this HostedNumberOrder.
            friendly_name: A human readable description of this resource, up to 128 characters.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_dependent_hosted_number_order(
                signing_document_sid,
                status=status,
                phone_number=phone_number,
                incoming_phone_number_sid=incoming_phone_number_sid,
                friendly_name=friendly_name,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncNumbersV2DependentHostedNumberOrderWithRawResponse:
        return self._with_raw_response


class NumbersV2DependentHostedNumberOrderWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def list_dependent_hosted_number_order(
        self,
        signing_document_sid: str,
        *,
        status: DependentHostedNumberOrderEnumStatusOrStr | None = None,
        phone_number: str | None = None,
        incoming_phone_number_sid: str | None = None,
        friendly_name: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListDependentHostedNumberOrderResponse, RawError]:
        """Retrieve a list of dependent HostedNumberOrders belonging to the AuthorizationDocument.

        Args:
            signing_document_sid: A 34 character string that uniquely identifies the LOA document associated with this
                HostedNumberOrder.
            status: Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA,
                4. canceled, 5. failed. See the section entitled `Status Values
                <https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource#status-values>`__
                for more information on each of these statuses.
            phone_number: An E164 formatted phone number hosted by this HostedNumberOrder.
            incoming_phone_number_sid: A 34 character string that uniquely identifies the IncomingPhoneNumber resource
                created by this HostedNumberOrder.
            friendly_name: A human readable description of this resource, up to 128 characters.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default5(
                "/v2/HostedNumber/AuthorizationDocuments/{SigningDocumentSid}/DependentHostedNumberOrders"
            ),
            path_params=[param[str]("SigningDocumentSid", signing_document_sid)],
            query_params=[
                param[DependentHostedNumberOrderEnumStatusOrStr | None]("Status", status),
                param[str | None]("PhoneNumber", phone_number),
                param[str | None]("IncomingPhoneNumberSid", incoming_phone_number_sid),
                param[str | None]("FriendlyName", friendly_name),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListDependentHostedNumberOrderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncNumbersV2DependentHostedNumberOrderWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def list_dependent_hosted_number_order(
        self,
        signing_document_sid: str,
        *,
        status: DependentHostedNumberOrderEnumStatusOrStr | None = None,
        phone_number: str | None = None,
        incoming_phone_number_sid: str | None = None,
        friendly_name: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListDependentHostedNumberOrderResponse, RawError]:
        """Retrieve a list of dependent HostedNumberOrders belonging to the AuthorizationDocument.

        Args:
            signing_document_sid: A 34 character string that uniquely identifies the LOA document associated with this
                HostedNumberOrder.
            status: Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA,
                4. canceled, 5. failed. See the section entitled `Status Values
                <https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource#status-values>`__
                for more information on each of these statuses.
            phone_number: An E164 formatted phone number hosted by this HostedNumberOrder.
            incoming_phone_number_sid: A 34 character string that uniquely identifies the IncomingPhoneNumber resource
                created by this HostedNumberOrder.
            friendly_name: A human readable description of this resource, up to 128 characters.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default5(
                "/v2/HostedNumber/AuthorizationDocuments/{SigningDocumentSid}/DependentHostedNumberOrders"
            ),
            path_params=[param[str]("SigningDocumentSid", signing_document_sid)],
            query_params=[
                param[DependentHostedNumberOrderEnumStatusOrStr | None]("Status", status),
                param[str | None]("PhoneNumber", phone_number),
                param[str | None]("IncomingPhoneNumberSid", incoming_phone_number_sid),
                param[str | None]("FriendlyName", friendly_name),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListDependentHostedNumberOrderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
