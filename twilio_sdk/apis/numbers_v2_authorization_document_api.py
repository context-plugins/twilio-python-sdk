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
from ..models.enums.authorization_document_enum_status import AuthorizationDocumentEnumStatusOrStr
from ..models.list_authorization_document_response import ListAuthorizationDocumentResponse
from ..models.numbers_v2_authorization_document import NumbersV2AuthorizationDocument
from ..server.server import Server


class NumbersV2AuthorizationDocumentApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NumbersV2AuthorizationDocumentApiWithRawResponse(client, server, auth)

    def create_authorization_document(
        self,
        address_sid: str,
        email: str,
        contact_phone_number: str,
        hosted_number_order_sids: list[str],
        *,
        contact_title: str | None = None,
        cc_emails: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> NumbersV2AuthorizationDocument:
        """Create an AuthorizationDocument for authorizing the hosting of phone number capabilities on Twilio's
        platform.

        Args:
            address_sid: A 34 character string that uniquely identifies the Address resource that is associated with
                this AuthorizationDocument.
            email: Email that this AuthorizationDocument will be sent to for signing.
            contact_phone_number: The contact phone number of the person authorized to sign the Authorization Document.
            hosted_number_order_sids: A list of HostedNumberOrder sids that this AuthorizationDocument will authorize
                for hosting phone number capabilities on Twilio's platform.
            contact_title: The title of the person authorized to sign the Authorization Document for this phone number.
            cc_emails: Email recipients who will be informed when an Authorization Document has been sent and signed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_authorization_document(
            address_sid,
            email,
            contact_phone_number,
            hosted_number_order_sids,
            contact_title=contact_title,
            cc_emails=cc_emails,
            request_options=request_options,
        ).unwrap()

    def delete_authorization_document(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Cancel the AuthorizationDocument request.

        Args:
            sid: A 34 character string that uniquely identifies this AuthorizationDocument.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_authorization_document(sid, request_options=request_options).unwrap()

    def fetch_authorization_document(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV2AuthorizationDocument:
        """Fetch a specific AuthorizationDocument.

        Args:
            sid: A 34 character string that uniquely identifies this AuthorizationDocument.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_authorization_document(sid, request_options=request_options).unwrap()

    def list_authorization_document(
        self,
        *,
        email: str | None = None,
        status: AuthorizationDocumentEnumStatusOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListAuthorizationDocumentResponse:
        """Retrieve a list of AuthorizationDocuments belonging to the account initiating the request.

        Args:
            email: Email that this AuthorizationDocument will be sent to for signing.
            status: Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA,
                4. canceled, 5. failed. See the section entitled `Status Values
                <https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource#status-values>`__
                for more information on each of these statuses.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_authorization_document(
            email=email,
            status=status,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> NumbersV2AuthorizationDocumentApiWithRawResponse:
        return self._with_raw_response


class AsyncNumbersV2AuthorizationDocumentApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNumbersV2AuthorizationDocumentApiWithRawResponse(client, server, auth)

    async def create_authorization_document(
        self,
        address_sid: str,
        email: str,
        contact_phone_number: str,
        hosted_number_order_sids: list[str],
        *,
        contact_title: str | None = None,
        cc_emails: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> NumbersV2AuthorizationDocument:
        """Create an AuthorizationDocument for authorizing the hosting of phone number capabilities on Twilio's
        platform.

        Args:
            address_sid: A 34 character string that uniquely identifies the Address resource that is associated with
                this AuthorizationDocument.
            email: Email that this AuthorizationDocument will be sent to for signing.
            contact_phone_number: The contact phone number of the person authorized to sign the Authorization Document.
            hosted_number_order_sids: A list of HostedNumberOrder sids that this AuthorizationDocument will authorize
                for hosting phone number capabilities on Twilio's platform.
            contact_title: The title of the person authorized to sign the Authorization Document for this phone number.
            cc_emails: Email recipients who will be informed when an Authorization Document has been sent and signed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_authorization_document(
                address_sid,
                email,
                contact_phone_number,
                hosted_number_order_sids,
                contact_title=contact_title,
                cc_emails=cc_emails,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_authorization_document(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Cancel the AuthorizationDocument request.

        Args:
            sid: A 34 character string that uniquely identifies this AuthorizationDocument.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_authorization_document(sid, request_options=request_options)
        ).unwrap()

    async def fetch_authorization_document(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV2AuthorizationDocument:
        """Fetch a specific AuthorizationDocument.

        Args:
            sid: A 34 character string that uniquely identifies this AuthorizationDocument.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_authorization_document(sid, request_options=request_options)
        ).unwrap()

    async def list_authorization_document(
        self,
        *,
        email: str | None = None,
        status: AuthorizationDocumentEnumStatusOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListAuthorizationDocumentResponse:
        """Retrieve a list of AuthorizationDocuments belonging to the account initiating the request.

        Args:
            email: Email that this AuthorizationDocument will be sent to for signing.
            status: Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA,
                4. canceled, 5. failed. See the section entitled `Status Values
                <https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource#status-values>`__
                for more information on each of these statuses.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_authorization_document(
                email=email,
                status=status,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncNumbersV2AuthorizationDocumentApiWithRawResponse:
        return self._with_raw_response


class NumbersV2AuthorizationDocumentApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_authorization_document(
        self,
        address_sid: str,
        email: str,
        contact_phone_number: str,
        hosted_number_order_sids: list[str],
        *,
        contact_title: str | None = None,
        cc_emails: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[NumbersV2AuthorizationDocument, RawError]:
        """Create an AuthorizationDocument for authorizing the hosting of phone number capabilities on Twilio's
        platform.

        Args:
            address_sid: A 34 character string that uniquely identifies the Address resource that is associated with
                this AuthorizationDocument.
            email: Email that this AuthorizationDocument will be sent to for signing.
            contact_phone_number: The contact phone number of the person authorized to sign the Authorization Document.
            hosted_number_order_sids: A list of HostedNumberOrder sids that this AuthorizationDocument will authorize
                for hosting phone number capabilities on Twilio's platform.
            contact_title: The title of the person authorized to sign the Authorization Document for this phone number.
            cc_emails: Email recipients who will be informed when an Authorization Document has been sent and signed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v2/HostedNumber/AuthorizationDocuments"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("AddressSid", address_sid),
                    param[str]("Email", email),
                    param[str]("ContactPhoneNumber", contact_phone_number),
                    param[list[str]]("HostedNumberOrderSids", hosted_number_order_sids),
                    param[str | None]("ContactTitle", contact_title),
                    param[list[str] | None]("CcEmails", cc_emails),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2AuthorizationDocument],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_authorization_document(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Cancel the AuthorizationDocument request.

        Args:
            sid: A 34 character string that uniquely identifies this AuthorizationDocument.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default5("/v2/HostedNumber/AuthorizationDocuments/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_authorization_document(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV2AuthorizationDocument, RawError]:
        """Fetch a specific AuthorizationDocument.

        Args:
            sid: A 34 character string that uniquely identifies this AuthorizationDocument.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/HostedNumber/AuthorizationDocuments/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2AuthorizationDocument],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_authorization_document(
        self,
        *,
        email: str | None = None,
        status: AuthorizationDocumentEnumStatusOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListAuthorizationDocumentResponse, RawError]:
        """Retrieve a list of AuthorizationDocuments belonging to the account initiating the request.

        Args:
            email: Email that this AuthorizationDocument will be sent to for signing.
            status: Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA,
                4. canceled, 5. failed. See the section entitled `Status Values
                <https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource#status-values>`__
                for more information on each of these statuses.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/HostedNumber/AuthorizationDocuments"),
            query_params=[
                param[str | None]("Email", email),
                param[AuthorizationDocumentEnumStatusOrStr | None]("Status", status),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListAuthorizationDocumentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncNumbersV2AuthorizationDocumentApiWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def create_authorization_document(
        self,
        address_sid: str,
        email: str,
        contact_phone_number: str,
        hosted_number_order_sids: list[str],
        *,
        contact_title: str | None = None,
        cc_emails: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[NumbersV2AuthorizationDocument, RawError]:
        """Create an AuthorizationDocument for authorizing the hosting of phone number capabilities on Twilio's
        platform.

        Args:
            address_sid: A 34 character string that uniquely identifies the Address resource that is associated with
                this AuthorizationDocument.
            email: Email that this AuthorizationDocument will be sent to for signing.
            contact_phone_number: The contact phone number of the person authorized to sign the Authorization Document.
            hosted_number_order_sids: A list of HostedNumberOrder sids that this AuthorizationDocument will authorize
                for hosting phone number capabilities on Twilio's platform.
            contact_title: The title of the person authorized to sign the Authorization Document for this phone number.
            cc_emails: Email recipients who will be informed when an Authorization Document has been sent and signed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v2/HostedNumber/AuthorizationDocuments"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("AddressSid", address_sid),
                    param[str]("Email", email),
                    param[str]("ContactPhoneNumber", contact_phone_number),
                    param[list[str]]("HostedNumberOrderSids", hosted_number_order_sids),
                    param[str | None]("ContactTitle", contact_title),
                    param[list[str] | None]("CcEmails", cc_emails),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2AuthorizationDocument],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_authorization_document(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Cancel the AuthorizationDocument request.

        Args:
            sid: A 34 character string that uniquely identifies this AuthorizationDocument.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default5("/v2/HostedNumber/AuthorizationDocuments/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_authorization_document(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV2AuthorizationDocument, RawError]:
        """Fetch a specific AuthorizationDocument.

        Args:
            sid: A 34 character string that uniquely identifies this AuthorizationDocument.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/HostedNumber/AuthorizationDocuments/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2AuthorizationDocument],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_authorization_document(
        self,
        *,
        email: str | None = None,
        status: AuthorizationDocumentEnumStatusOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListAuthorizationDocumentResponse, RawError]:
        """Retrieve a list of AuthorizationDocuments belonging to the account initiating the request.

        Args:
            email: Email that this AuthorizationDocument will be sent to for signing.
            status: Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA,
                4. canceled, 5. failed. See the section entitled `Status Values
                <https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource#status-values>`__
                for more information on each of these statuses.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/HostedNumber/AuthorizationDocuments"),
            query_params=[
                param[str | None]("Email", email),
                param[AuthorizationDocumentEnumStatusOrStr | None]("Status", status),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListAuthorizationDocumentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
