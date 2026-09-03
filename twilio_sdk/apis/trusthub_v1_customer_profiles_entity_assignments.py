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
from ..models.list_customer_profile_entity_assignment_response import ListCustomerProfileEntityAssignmentResponse
from ..models.trusthub_v1_customer_profile_customer_profile_entity_assignment import (
    TrusthubV1CustomerProfileCustomerProfileEntityAssignment,
)
from ..server.server import Server


class TrusthubV1CustomerProfilesEntityAssignments:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TrusthubV1CustomerProfilesEntityAssignmentsWithRawResponse(client, server, auth)

    def create_customer_profile_entity_assignment(
        self, customer_profile_sid: str, object_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TrusthubV1CustomerProfileCustomerProfileEntityAssignment:
        """Create a new Assigned Item.

        Args:
            customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
            object_sid: The SID of an object bag that holds information of the different items.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_customer_profile_entity_assignment(
            customer_profile_sid, object_sid, request_options=request_options
        ).unwrap()

    def delete_customer_profile_entity_assignment(
        self, customer_profile_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Remove an Assignment Item Instance.

        Args:
            customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
            sid: The unique string that we created to identify the Identity resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_customer_profile_entity_assignment(
            customer_profile_sid, sid, request_options=request_options
        ).unwrap()

    def fetch_customer_profile_entity_assignment(
        self, customer_profile_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TrusthubV1CustomerProfileCustomerProfileEntityAssignment:
        """Fetch specific Assigned Item Instance.

        Args:
            customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
            sid: The unique string that we created to identify the Identity resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_customer_profile_entity_assignment(
            customer_profile_sid, sid, request_options=request_options
        ).unwrap()

    def list_customer_profile_entity_assignment(
        self,
        customer_profile_sid: str,
        *,
        object_type: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCustomerProfileEntityAssignmentResponse:
        """Retrieve a list of all Assigned Items for an account.

        Args:
            customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
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
        return self._with_raw_response.list_customer_profile_entity_assignment(
            customer_profile_sid,
            object_type=object_type,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> TrusthubV1CustomerProfilesEntityAssignmentsWithRawResponse:
        return self._with_raw_response


class AsyncTrusthubV1CustomerProfilesEntityAssignments:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTrusthubV1CustomerProfilesEntityAssignmentsWithRawResponse(client, server, auth)

    async def create_customer_profile_entity_assignment(
        self, customer_profile_sid: str, object_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TrusthubV1CustomerProfileCustomerProfileEntityAssignment:
        """Create a new Assigned Item.

        Args:
            customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
            object_sid: The SID of an object bag that holds information of the different items.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_customer_profile_entity_assignment(
                customer_profile_sid, object_sid, request_options=request_options
            )
        ).unwrap()

    async def delete_customer_profile_entity_assignment(
        self, customer_profile_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Remove an Assignment Item Instance.

        Args:
            customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
            sid: The unique string that we created to identify the Identity resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_customer_profile_entity_assignment(
                customer_profile_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def fetch_customer_profile_entity_assignment(
        self, customer_profile_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TrusthubV1CustomerProfileCustomerProfileEntityAssignment:
        """Fetch specific Assigned Item Instance.

        Args:
            customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
            sid: The unique string that we created to identify the Identity resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_customer_profile_entity_assignment(
                customer_profile_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def list_customer_profile_entity_assignment(
        self,
        customer_profile_sid: str,
        *,
        object_type: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCustomerProfileEntityAssignmentResponse:
        """Retrieve a list of all Assigned Items for an account.

        Args:
            customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
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
            await self._with_raw_response.list_customer_profile_entity_assignment(
                customer_profile_sid,
                object_type=object_type,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTrusthubV1CustomerProfilesEntityAssignmentsWithRawResponse:
        return self._with_raw_response


class TrusthubV1CustomerProfilesEntityAssignmentsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_customer_profile_entity_assignment(
        self, customer_profile_sid: str, object_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TrusthubV1CustomerProfileCustomerProfileEntityAssignment, RawError]:
        """Create a new Assigned Item.

        Args:
            customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
            object_sid: The SID of an object bag that holds information of the different items.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/v1/CustomerProfiles/{CustomerProfileSid}/EntityAssignments"),
            path_params=[param[str]("CustomerProfileSid", customer_profile_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str]("ObjectSid", object_sid)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1CustomerProfileCustomerProfileEntityAssignment],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_customer_profile_entity_assignment(
        self, customer_profile_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Remove an Assignment Item Instance.

        Args:
            customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
            sid: The unique string that we created to identify the Identity resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default9("/v1/CustomerProfiles/{CustomerProfileSid}/EntityAssignments/{Sid}"),
            path_params=[param[str]("CustomerProfileSid", customer_profile_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_customer_profile_entity_assignment(
        self, customer_profile_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TrusthubV1CustomerProfileCustomerProfileEntityAssignment, RawError]:
        """Fetch specific Assigned Item Instance.

        Args:
            customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
            sid: The unique string that we created to identify the Identity resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/v1/CustomerProfiles/{CustomerProfileSid}/EntityAssignments/{Sid}"),
            path_params=[param[str]("CustomerProfileSid", customer_profile_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1CustomerProfileCustomerProfileEntityAssignment],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_customer_profile_entity_assignment(
        self,
        customer_profile_sid: str,
        *,
        object_type: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCustomerProfileEntityAssignmentResponse, RawError]:
        """Retrieve a list of all Assigned Items for an account.

        Args:
            customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
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
            url_template=self._server.default9("/v1/CustomerProfiles/{CustomerProfileSid}/EntityAssignments"),
            path_params=[param[str]("CustomerProfileSid", customer_profile_sid)],
            query_params=[
                param[str | None]("ObjectType", object_type),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListCustomerProfileEntityAssignmentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTrusthubV1CustomerProfilesEntityAssignmentsWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def create_customer_profile_entity_assignment(
        self, customer_profile_sid: str, object_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TrusthubV1CustomerProfileCustomerProfileEntityAssignment, RawError]:
        """Create a new Assigned Item.

        Args:
            customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
            object_sid: The SID of an object bag that holds information of the different items.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/v1/CustomerProfiles/{CustomerProfileSid}/EntityAssignments"),
            path_params=[param[str]("CustomerProfileSid", customer_profile_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str]("ObjectSid", object_sid)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1CustomerProfileCustomerProfileEntityAssignment],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_customer_profile_entity_assignment(
        self, customer_profile_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Remove an Assignment Item Instance.

        Args:
            customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
            sid: The unique string that we created to identify the Identity resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default9("/v1/CustomerProfiles/{CustomerProfileSid}/EntityAssignments/{Sid}"),
            path_params=[param[str]("CustomerProfileSid", customer_profile_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_customer_profile_entity_assignment(
        self, customer_profile_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TrusthubV1CustomerProfileCustomerProfileEntityAssignment, RawError]:
        """Fetch specific Assigned Item Instance.

        Args:
            customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
            sid: The unique string that we created to identify the Identity resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/v1/CustomerProfiles/{CustomerProfileSid}/EntityAssignments/{Sid}"),
            path_params=[param[str]("CustomerProfileSid", customer_profile_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1CustomerProfileCustomerProfileEntityAssignment],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_customer_profile_entity_assignment(
        self,
        customer_profile_sid: str,
        *,
        object_type: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCustomerProfileEntityAssignmentResponse, RawError]:
        """Retrieve a list of all Assigned Items for an account.

        Args:
            customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
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
            url_template=self._server.default9("/v1/CustomerProfiles/{CustomerProfileSid}/EntityAssignments"),
            path_params=[param[str]("CustomerProfileSid", customer_profile_sid)],
            query_params=[
                param[str | None]("ObjectType", object_type),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListCustomerProfileEntityAssignmentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
