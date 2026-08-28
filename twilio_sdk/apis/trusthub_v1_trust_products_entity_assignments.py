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
from ..models.list_trust_product_entity_assignment_response import ListTrustProductEntityAssignmentResponse
from ..models.trusthub_v1_trust_product_trust_product_entity_assignment import (
    TrusthubV1TrustProductTrustProductEntityAssignment,
)
from ..server.server import Server


class TrusthubV1TrustProductsEntityAssignments:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TrusthubV1TrustProductsEntityAssignmentsWithRawResponse(client, server, auth)

    def create_trust_product_entity_assignment(
        self, trust_product_sid: str, object_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TrusthubV1TrustProductTrustProductEntityAssignment:
        """Create a new Assigned Item.

        Args:
            trust_product_sid: The unique string that we created to identify the TrustProduct resource.
            object_sid: The SID of an object bag that holds information of the different items.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_trust_product_entity_assignment(
            trust_product_sid, object_sid, request_options=request_options
        ).unwrap()

    def delete_trust_product_entity_assignment(
        self, trust_product_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Remove an Assignment Item Instance.

        Args:
            trust_product_sid: The unique string that we created to identify the TrustProduct resource.
            sid: The unique string that we created to identify the Identity resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_trust_product_entity_assignment(
            trust_product_sid, sid, request_options=request_options
        ).unwrap()

    def fetch_trust_product_entity_assignment(
        self, trust_product_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TrusthubV1TrustProductTrustProductEntityAssignment:
        """Fetch specific Assigned Item Instance.

        Args:
            trust_product_sid: The unique string that we created to identify the TrustProduct resource.
            sid: The unique string that we created to identify the Identity resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_trust_product_entity_assignment(
            trust_product_sid, sid, request_options=request_options
        ).unwrap()

    def list_trust_product_entity_assignment(
        self,
        trust_product_sid: str,
        *,
        object_type: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListTrustProductEntityAssignmentResponse:
        """Retrieve a list of all Assigned Items for an account.

        Args:
            trust_product_sid: The unique string that we created to identify the TrustProduct resource.
            object_type: A string to filter the results by (EndUserType or SupportingDocumentType) machine-name. This is
                useful when you want to retrieve the entity-assignment of a specific end-user or supporting document.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_trust_product_entity_assignment(
            trust_product_sid,
            object_type=object_type,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> TrusthubV1TrustProductsEntityAssignmentsWithRawResponse:
        return self._with_raw_response


class AsyncTrusthubV1TrustProductsEntityAssignments:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTrusthubV1TrustProductsEntityAssignmentsWithRawResponse(client, server, auth)

    async def create_trust_product_entity_assignment(
        self, trust_product_sid: str, object_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TrusthubV1TrustProductTrustProductEntityAssignment:
        """Create a new Assigned Item.

        Args:
            trust_product_sid: The unique string that we created to identify the TrustProduct resource.
            object_sid: The SID of an object bag that holds information of the different items.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_trust_product_entity_assignment(
                trust_product_sid, object_sid, request_options=request_options
            )
        ).unwrap()

    async def delete_trust_product_entity_assignment(
        self, trust_product_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Remove an Assignment Item Instance.

        Args:
            trust_product_sid: The unique string that we created to identify the TrustProduct resource.
            sid: The unique string that we created to identify the Identity resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_trust_product_entity_assignment(
                trust_product_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def fetch_trust_product_entity_assignment(
        self, trust_product_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TrusthubV1TrustProductTrustProductEntityAssignment:
        """Fetch specific Assigned Item Instance.

        Args:
            trust_product_sid: The unique string that we created to identify the TrustProduct resource.
            sid: The unique string that we created to identify the Identity resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_trust_product_entity_assignment(
                trust_product_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def list_trust_product_entity_assignment(
        self,
        trust_product_sid: str,
        *,
        object_type: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListTrustProductEntityAssignmentResponse:
        """Retrieve a list of all Assigned Items for an account.

        Args:
            trust_product_sid: The unique string that we created to identify the TrustProduct resource.
            object_type: A string to filter the results by (EndUserType or SupportingDocumentType) machine-name. This is
                useful when you want to retrieve the entity-assignment of a specific end-user or supporting document.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_trust_product_entity_assignment(
                trust_product_sid,
                object_type=object_type,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTrusthubV1TrustProductsEntityAssignmentsWithRawResponse:
        return self._with_raw_response


class TrusthubV1TrustProductsEntityAssignmentsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_trust_product_entity_assignment(
        self, trust_product_sid: str, object_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TrusthubV1TrustProductTrustProductEntityAssignment, RawError]:
        """Create a new Assigned Item.

        Args:
            trust_product_sid: The unique string that we created to identify the TrustProduct resource.
            object_sid: The SID of an object bag that holds information of the different items.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/v1/TrustProducts/{TrustProductSid}/EntityAssignments"),
            path_params=[param[str]("TrustProductSid", trust_product_sid)],
            body=form_body([param[str]("ObjectSid", object_sid)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1TrustProductTrustProductEntityAssignment],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_trust_product_entity_assignment(
        self, trust_product_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Remove an Assignment Item Instance.

        Args:
            trust_product_sid: The unique string that we created to identify the TrustProduct resource.
            sid: The unique string that we created to identify the Identity resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default9("/v1/TrustProducts/{TrustProductSid}/EntityAssignments/{Sid}"),
            path_params=[param[str]("TrustProductSid", trust_product_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_trust_product_entity_assignment(
        self, trust_product_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TrusthubV1TrustProductTrustProductEntityAssignment, RawError]:
        """Fetch specific Assigned Item Instance.

        Args:
            trust_product_sid: The unique string that we created to identify the TrustProduct resource.
            sid: The unique string that we created to identify the Identity resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/v1/TrustProducts/{TrustProductSid}/EntityAssignments/{Sid}"),
            path_params=[param[str]("TrustProductSid", trust_product_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1TrustProductTrustProductEntityAssignment],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_trust_product_entity_assignment(
        self,
        trust_product_sid: str,
        *,
        object_type: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListTrustProductEntityAssignmentResponse, RawError]:
        """Retrieve a list of all Assigned Items for an account.

        Args:
            trust_product_sid: The unique string that we created to identify the TrustProduct resource.
            object_type: A string to filter the results by (EndUserType or SupportingDocumentType) machine-name. This is
                useful when you want to retrieve the entity-assignment of a specific end-user or supporting document.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/v1/TrustProducts/{TrustProductSid}/EntityAssignments"),
            path_params=[param[str]("TrustProductSid", trust_product_sid)],
            query_params=[
                param[str | None]("ObjectType", object_type),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListTrustProductEntityAssignmentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTrusthubV1TrustProductsEntityAssignmentsWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def create_trust_product_entity_assignment(
        self, trust_product_sid: str, object_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TrusthubV1TrustProductTrustProductEntityAssignment, RawError]:
        """Create a new Assigned Item.

        Args:
            trust_product_sid: The unique string that we created to identify the TrustProduct resource.
            object_sid: The SID of an object bag that holds information of the different items.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/v1/TrustProducts/{TrustProductSid}/EntityAssignments"),
            path_params=[param[str]("TrustProductSid", trust_product_sid)],
            body=form_body([param[str]("ObjectSid", object_sid)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1TrustProductTrustProductEntityAssignment],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_trust_product_entity_assignment(
        self, trust_product_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Remove an Assignment Item Instance.

        Args:
            trust_product_sid: The unique string that we created to identify the TrustProduct resource.
            sid: The unique string that we created to identify the Identity resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default9("/v1/TrustProducts/{TrustProductSid}/EntityAssignments/{Sid}"),
            path_params=[param[str]("TrustProductSid", trust_product_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_trust_product_entity_assignment(
        self, trust_product_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TrusthubV1TrustProductTrustProductEntityAssignment, RawError]:
        """Fetch specific Assigned Item Instance.

        Args:
            trust_product_sid: The unique string that we created to identify the TrustProduct resource.
            sid: The unique string that we created to identify the Identity resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/v1/TrustProducts/{TrustProductSid}/EntityAssignments/{Sid}"),
            path_params=[param[str]("TrustProductSid", trust_product_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1TrustProductTrustProductEntityAssignment],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_trust_product_entity_assignment(
        self,
        trust_product_sid: str,
        *,
        object_type: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListTrustProductEntityAssignmentResponse, RawError]:
        """Retrieve a list of all Assigned Items for an account.

        Args:
            trust_product_sid: The unique string that we created to identify the TrustProduct resource.
            object_type: A string to filter the results by (EndUserType or SupportingDocumentType) machine-name. This is
                useful when you want to retrieve the entity-assignment of a specific end-user or supporting document.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/v1/TrustProducts/{TrustProductSid}/EntityAssignments"),
            path_params=[param[str]("TrustProductSid", trust_product_sid)],
            query_params=[
                param[str | None]("ObjectType", object_type),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListTrustProductEntityAssignmentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
