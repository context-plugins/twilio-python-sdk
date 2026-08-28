from __future__ import annotations

from typing import Any

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
from ..models.list_supporting_document_response import ListSupportingDocumentResponse
from ..models.numbers_v2_regulatory_compliance_supporting_document import (
    NumbersV2RegulatoryComplianceSupportingDocument,
)
from ..server.server import Server


class NumbersV2SupportingDocument:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NumbersV2SupportingDocumentWithRawResponse(client, server, auth)

    def create_supporting_document(
        self,
        friendly_name: str,
        type_: str,
        *,
        attributes: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> NumbersV2RegulatoryComplianceSupportingDocument:
        """Create a new Supporting Document.

        Args:
            friendly_name: The string that you assigned to describe the resource.
            type_: The type of the Supporting Document.
            attributes: The set of parameters that are the attributes of the Supporting Documents resource which are
                derived Supporting Document Types.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_supporting_document(
            friendly_name, type_, attributes=attributes, request_options=request_options
        ).unwrap()

    def delete_supporting_document(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Delete a specific Supporting Document.

        Args:
            sid: The unique string created by Twilio to identify the Supporting Document resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_supporting_document(sid, request_options=request_options).unwrap()

    def fetch_supporting_document(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV2RegulatoryComplianceSupportingDocument:
        """Fetch specific Supporting Document Instance.

        Args:
            sid: The unique string created by Twilio to identify the Supporting Document resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_supporting_document(sid, request_options=request_options).unwrap()

    def list_supporting_document(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSupportingDocumentResponse:
        """Retrieve a list of all Supporting Document for an account.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_supporting_document(
            page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    def update_supporting_document(
        self,
        sid: str,
        *,
        friendly_name: str | None = None,
        attributes: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> NumbersV2RegulatoryComplianceSupportingDocument:
        """Update an existing Supporting Document.

        Args:
            sid: The unique string created by Twilio to identify the Supporting Document resource.
            friendly_name: The string that you assigned to describe the resource.
            attributes: The set of parameters that are the attributes of the Supporting Document resource which are
                derived Supporting Document Types.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_supporting_document(
            sid, friendly_name=friendly_name, attributes=attributes, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> NumbersV2SupportingDocumentWithRawResponse:
        return self._with_raw_response


class AsyncNumbersV2SupportingDocument:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNumbersV2SupportingDocumentWithRawResponse(client, server, auth)

    async def create_supporting_document(
        self,
        friendly_name: str,
        type_: str,
        *,
        attributes: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> NumbersV2RegulatoryComplianceSupportingDocument:
        """Create a new Supporting Document.

        Args:
            friendly_name: The string that you assigned to describe the resource.
            type_: The type of the Supporting Document.
            attributes: The set of parameters that are the attributes of the Supporting Documents resource which are
                derived Supporting Document Types.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_supporting_document(
                friendly_name, type_, attributes=attributes, request_options=request_options
            )
        ).unwrap()

    async def delete_supporting_document(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a specific Supporting Document.

        Args:
            sid: The unique string created by Twilio to identify the Supporting Document resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_supporting_document(sid, request_options=request_options)).unwrap()

    async def fetch_supporting_document(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV2RegulatoryComplianceSupportingDocument:
        """Fetch specific Supporting Document Instance.

        Args:
            sid: The unique string created by Twilio to identify the Supporting Document resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_supporting_document(sid, request_options=request_options)).unwrap()

    async def list_supporting_document(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSupportingDocumentResponse:
        """Retrieve a list of all Supporting Document for an account.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_supporting_document(
                page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    async def update_supporting_document(
        self,
        sid: str,
        *,
        friendly_name: str | None = None,
        attributes: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> NumbersV2RegulatoryComplianceSupportingDocument:
        """Update an existing Supporting Document.

        Args:
            sid: The unique string created by Twilio to identify the Supporting Document resource.
            friendly_name: The string that you assigned to describe the resource.
            attributes: The set of parameters that are the attributes of the Supporting Document resource which are
                derived Supporting Document Types.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_supporting_document(
                sid, friendly_name=friendly_name, attributes=attributes, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncNumbersV2SupportingDocumentWithRawResponse:
        return self._with_raw_response


class NumbersV2SupportingDocumentWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_supporting_document(
        self,
        friendly_name: str,
        type_: str,
        *,
        attributes: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[NumbersV2RegulatoryComplianceSupportingDocument, RawError]:
        """Create a new Supporting Document.

        Args:
            friendly_name: The string that you assigned to describe the resource.
            type_: The type of the Supporting Document.
            attributes: The set of parameters that are the attributes of the Supporting Documents resource which are
                derived Supporting Document Types.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v2/RegulatoryCompliance/SupportingDocuments"),
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[str]("Type", type_),
                    param[Any | None]("Attributes", attributes),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2RegulatoryComplianceSupportingDocument],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_supporting_document(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Supporting Document.

        Args:
            sid: The unique string created by Twilio to identify the Supporting Document resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default5("/v2/RegulatoryCompliance/SupportingDocuments/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_supporting_document(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV2RegulatoryComplianceSupportingDocument, RawError]:
        """Fetch specific Supporting Document Instance.

        Args:
            sid: The unique string created by Twilio to identify the Supporting Document resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/RegulatoryCompliance/SupportingDocuments/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2RegulatoryComplianceSupportingDocument],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_supporting_document(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSupportingDocumentResponse, RawError]:
        """Retrieve a list of all Supporting Document for an account.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/RegulatoryCompliance/SupportingDocuments"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListSupportingDocumentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_supporting_document(
        self,
        sid: str,
        *,
        friendly_name: str | None = None,
        attributes: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[NumbersV2RegulatoryComplianceSupportingDocument, RawError]:
        """Update an existing Supporting Document.

        Args:
            sid: The unique string created by Twilio to identify the Supporting Document resource.
            friendly_name: The string that you assigned to describe the resource.
            attributes: The set of parameters that are the attributes of the Supporting Document resource which are
                derived Supporting Document Types.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v2/RegulatoryCompliance/SupportingDocuments/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            body=form_body(
                [param[str | None]("FriendlyName", friendly_name), param[Any | None]("Attributes", attributes)]
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2RegulatoryComplianceSupportingDocument],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncNumbersV2SupportingDocumentWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_supporting_document(
        self,
        friendly_name: str,
        type_: str,
        *,
        attributes: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[NumbersV2RegulatoryComplianceSupportingDocument, RawError]:
        """Create a new Supporting Document.

        Args:
            friendly_name: The string that you assigned to describe the resource.
            type_: The type of the Supporting Document.
            attributes: The set of parameters that are the attributes of the Supporting Documents resource which are
                derived Supporting Document Types.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v2/RegulatoryCompliance/SupportingDocuments"),
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[str]("Type", type_),
                    param[Any | None]("Attributes", attributes),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2RegulatoryComplianceSupportingDocument],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_supporting_document(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Supporting Document.

        Args:
            sid: The unique string created by Twilio to identify the Supporting Document resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default5("/v2/RegulatoryCompliance/SupportingDocuments/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_supporting_document(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV2RegulatoryComplianceSupportingDocument, RawError]:
        """Fetch specific Supporting Document Instance.

        Args:
            sid: The unique string created by Twilio to identify the Supporting Document resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/RegulatoryCompliance/SupportingDocuments/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2RegulatoryComplianceSupportingDocument],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_supporting_document(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSupportingDocumentResponse, RawError]:
        """Retrieve a list of all Supporting Document for an account.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/RegulatoryCompliance/SupportingDocuments"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListSupportingDocumentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_supporting_document(
        self,
        sid: str,
        *,
        friendly_name: str | None = None,
        attributes: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[NumbersV2RegulatoryComplianceSupportingDocument, RawError]:
        """Update an existing Supporting Document.

        Args:
            sid: The unique string created by Twilio to identify the Supporting Document resource.
            friendly_name: The string that you assigned to describe the resource.
            attributes: The set of parameters that are the attributes of the Supporting Document resource which are
                derived Supporting Document Types.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v2/RegulatoryCompliance/SupportingDocuments/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            body=form_body(
                [param[str | None]("FriendlyName", friendly_name), param[Any | None]("Attributes", attributes)]
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2RegulatoryComplianceSupportingDocument],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
