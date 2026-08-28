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
from ..models.list_customer_profile_channel_endpoint_assignment_response import (
    ListCustomerProfileChannelEndpointAssignmentResponse,
)
from ..models.trusthub_v1_customer_profile_customer_profile_channel_endpoint_assignment import (
    TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment,
)
from ..server.server import Server


class TrusthubV1CustomerProfilesChannelEndpointAssignment:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TrusthubV1CustomerProfilesChannelEndpointAssignmentWithRawResponse(
            client, server, auth
        )

    def create_customer_profile_channel_endpoint_assignment(
        self,
        customer_profile_sid: str,
        channel_endpoint_type: str,
        channel_endpoint_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment:
        """Create a new Assigned Item.

        Args:
            customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
            channel_endpoint_type: The type of channel endpoint. eg: phone-number
            channel_endpoint_sid: The SID of an channel endpoint
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_customer_profile_channel_endpoint_assignment(
            customer_profile_sid, channel_endpoint_type, channel_endpoint_sid, request_options=request_options
        ).unwrap()

    def delete_customer_profile_channel_endpoint_assignment(
        self, customer_profile_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Remove an Assignment Item Instance.

        Args:
            customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
            sid: The unique string that we created to identify the resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_customer_profile_channel_endpoint_assignment(
            customer_profile_sid, sid, request_options=request_options
        ).unwrap()

    def fetch_customer_profile_channel_endpoint_assignment(
        self, customer_profile_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment:
        """Fetch specific Assigned Item Instance.

        Args:
            customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
            sid: The unique string that we created to identify the resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_customer_profile_channel_endpoint_assignment(
            customer_profile_sid, sid, request_options=request_options
        ).unwrap()

    def list_customer_profile_channel_endpoint_assignment(
        self,
        customer_profile_sid: str,
        *,
        channel_endpoint_sid: str | None = None,
        channel_endpoint_sids: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCustomerProfileChannelEndpointAssignmentResponse:
        """Retrieve a list of all Assigned Items for an account.

        Args:
            customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
            channel_endpoint_sid: The SID of an channel endpoint
            channel_endpoint_sids: comma separated list of channel endpoint sids
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_customer_profile_channel_endpoint_assignment(
            customer_profile_sid,
            channel_endpoint_sid=channel_endpoint_sid,
            channel_endpoint_sids=channel_endpoint_sids,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> TrusthubV1CustomerProfilesChannelEndpointAssignmentWithRawResponse:
        return self._with_raw_response


class AsyncTrusthubV1CustomerProfilesChannelEndpointAssignment:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTrusthubV1CustomerProfilesChannelEndpointAssignmentWithRawResponse(
            client, server, auth
        )

    async def create_customer_profile_channel_endpoint_assignment(
        self,
        customer_profile_sid: str,
        channel_endpoint_type: str,
        channel_endpoint_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment:
        """Create a new Assigned Item.

        Args:
            customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
            channel_endpoint_type: The type of channel endpoint. eg: phone-number
            channel_endpoint_sid: The SID of an channel endpoint
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_customer_profile_channel_endpoint_assignment(
                customer_profile_sid, channel_endpoint_type, channel_endpoint_sid, request_options=request_options
            )
        ).unwrap()

    async def delete_customer_profile_channel_endpoint_assignment(
        self, customer_profile_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Remove an Assignment Item Instance.

        Args:
            customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
            sid: The unique string that we created to identify the resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_customer_profile_channel_endpoint_assignment(
                customer_profile_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def fetch_customer_profile_channel_endpoint_assignment(
        self, customer_profile_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment:
        """Fetch specific Assigned Item Instance.

        Args:
            customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
            sid: The unique string that we created to identify the resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_customer_profile_channel_endpoint_assignment(
                customer_profile_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def list_customer_profile_channel_endpoint_assignment(
        self,
        customer_profile_sid: str,
        *,
        channel_endpoint_sid: str | None = None,
        channel_endpoint_sids: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCustomerProfileChannelEndpointAssignmentResponse:
        """Retrieve a list of all Assigned Items for an account.

        Args:
            customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
            channel_endpoint_sid: The SID of an channel endpoint
            channel_endpoint_sids: comma separated list of channel endpoint sids
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_customer_profile_channel_endpoint_assignment(
                customer_profile_sid,
                channel_endpoint_sid=channel_endpoint_sid,
                channel_endpoint_sids=channel_endpoint_sids,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTrusthubV1CustomerProfilesChannelEndpointAssignmentWithRawResponse:
        return self._with_raw_response


class TrusthubV1CustomerProfilesChannelEndpointAssignmentWithRawResponse(
    SecuredRawResponse[RawClient, Server, AuthSchemes]
):
    def create_customer_profile_channel_endpoint_assignment(
        self,
        customer_profile_sid: str,
        channel_endpoint_type: str,
        channel_endpoint_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment, RawError]:
        """Create a new Assigned Item.

        Args:
            customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
            channel_endpoint_type: The type of channel endpoint. eg: phone-number
            channel_endpoint_sid: The SID of an channel endpoint
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/v1/CustomerProfiles/{CustomerProfileSid}/ChannelEndpointAssignments"),
            path_params=[param[str]("CustomerProfileSid", customer_profile_sid)],
            body=form_body(
                [
                    param[str]("ChannelEndpointType", channel_endpoint_type),
                    param[str]("ChannelEndpointSid", channel_endpoint_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_customer_profile_channel_endpoint_assignment(
        self, customer_profile_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Remove an Assignment Item Instance.

        Args:
            customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
            sid: The unique string that we created to identify the resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default9(
                "/v1/CustomerProfiles/{CustomerProfileSid}/ChannelEndpointAssignments/{Sid}"
            ),
            path_params=[param[str]("CustomerProfileSid", customer_profile_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_customer_profile_channel_endpoint_assignment(
        self, customer_profile_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment, RawError]:
        """Fetch specific Assigned Item Instance.

        Args:
            customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
            sid: The unique string that we created to identify the resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9(
                "/v1/CustomerProfiles/{CustomerProfileSid}/ChannelEndpointAssignments/{Sid}"
            ),
            path_params=[param[str]("CustomerProfileSid", customer_profile_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_customer_profile_channel_endpoint_assignment(
        self,
        customer_profile_sid: str,
        *,
        channel_endpoint_sid: str | None = None,
        channel_endpoint_sids: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCustomerProfileChannelEndpointAssignmentResponse, RawError]:
        """Retrieve a list of all Assigned Items for an account.

        Args:
            customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
            channel_endpoint_sid: The SID of an channel endpoint
            channel_endpoint_sids: comma separated list of channel endpoint sids
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/v1/CustomerProfiles/{CustomerProfileSid}/ChannelEndpointAssignments"),
            path_params=[param[str]("CustomerProfileSid", customer_profile_sid)],
            query_params=[
                param[str | None]("ChannelEndpointSid", channel_endpoint_sid),
                param[str | None]("ChannelEndpointSids", channel_endpoint_sids),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListCustomerProfileChannelEndpointAssignmentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTrusthubV1CustomerProfilesChannelEndpointAssignmentWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def create_customer_profile_channel_endpoint_assignment(
        self,
        customer_profile_sid: str,
        channel_endpoint_type: str,
        channel_endpoint_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment, RawError]:
        """Create a new Assigned Item.

        Args:
            customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
            channel_endpoint_type: The type of channel endpoint. eg: phone-number
            channel_endpoint_sid: The SID of an channel endpoint
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/v1/CustomerProfiles/{CustomerProfileSid}/ChannelEndpointAssignments"),
            path_params=[param[str]("CustomerProfileSid", customer_profile_sid)],
            body=form_body(
                [
                    param[str]("ChannelEndpointType", channel_endpoint_type),
                    param[str]("ChannelEndpointSid", channel_endpoint_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_customer_profile_channel_endpoint_assignment(
        self, customer_profile_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Remove an Assignment Item Instance.

        Args:
            customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
            sid: The unique string that we created to identify the resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default9(
                "/v1/CustomerProfiles/{CustomerProfileSid}/ChannelEndpointAssignments/{Sid}"
            ),
            path_params=[param[str]("CustomerProfileSid", customer_profile_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_customer_profile_channel_endpoint_assignment(
        self, customer_profile_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment, RawError]:
        """Fetch specific Assigned Item Instance.

        Args:
            customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
            sid: The unique string that we created to identify the resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9(
                "/v1/CustomerProfiles/{CustomerProfileSid}/ChannelEndpointAssignments/{Sid}"
            ),
            path_params=[param[str]("CustomerProfileSid", customer_profile_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_customer_profile_channel_endpoint_assignment(
        self,
        customer_profile_sid: str,
        *,
        channel_endpoint_sid: str | None = None,
        channel_endpoint_sids: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCustomerProfileChannelEndpointAssignmentResponse, RawError]:
        """Retrieve a list of all Assigned Items for an account.

        Args:
            customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
            channel_endpoint_sid: The SID of an channel endpoint
            channel_endpoint_sids: comma separated list of channel endpoint sids
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/v1/CustomerProfiles/{CustomerProfileSid}/ChannelEndpointAssignments"),
            path_params=[param[str]("CustomerProfileSid", customer_profile_sid)],
            query_params=[
                param[str | None]("ChannelEndpointSid", channel_endpoint_sid),
                param[str | None]("ChannelEndpointSids", channel_endpoint_sids),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListCustomerProfileChannelEndpointAssignmentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
