from __future__ import annotations

from typing import Any
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
from ..models.list_engagement_response import ListEngagementResponse
from ..models.studio_v1_flow_engagement import StudioV1FlowEngagement
from ..server.server import Server


class StudioV1Engagement:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = StudioV1EngagementWithRawResponse(client, server, auth)

    def create_engagement(
        self,
        flow_sid: str,
        to: str,
        from_: str,
        *,
        parameters: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StudioV1FlowEngagement:
        """Triggers a new Engagement for the Flow

        Args:
            flow_sid: The SID of the Flow.
            to: The Contact phone number to start a Studio Flow Engagement, available as variable
                ``{{contact.channel.address}}``.
            from_: The Twilio phone number to send messages or initiate calls from during the Flow Engagement. Available
                as variable ``{{flow.channel.address}}``
            parameters: A JSON string we will add to your flow's context and that you can access as variables inside
                your flow. For example, if you pass in ``Parameters={'name':'Zeke'}`` then inside a widget you can
                reference the variable ``{{flow.data.name}}`` which will return the string 'Zeke'. Note: the JSON value
                must explicitly be passed as a string, not as a hash object. Depending on your particular HTTP library,
                you may need to add quotes or URL encode your JSON string.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_engagement(
            flow_sid, to, from_, parameters=parameters, request_options=request_options
        ).unwrap()

    def delete_engagement(
        self, flow_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete this Engagement and all Steps relating to it.

        Args:
            flow_sid: The SID of the Flow to delete Engagements from.
            sid: The SID of the Engagement resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_engagement(flow_sid, sid, request_options=request_options).unwrap()

    def fetch_engagement(
        self, flow_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> StudioV1FlowEngagement:
        """Retrieve an Engagement

        Args:
            flow_sid: The SID of the Flow.
            sid: The SID of the Engagement resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_engagement(flow_sid, sid, request_options=request_options).unwrap()

    def list_engagement(
        self,
        flow_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListEngagementResponse:
        """Retrieve a list of all Engagements for the Flow.

        Args:
            flow_sid: The SID of the Flow to read Engagements from.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_engagement(
            flow_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> StudioV1EngagementWithRawResponse:
        return self._with_raw_response


class AsyncStudioV1Engagement:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncStudioV1EngagementWithRawResponse(client, server, auth)

    async def create_engagement(
        self,
        flow_sid: str,
        to: str,
        from_: str,
        *,
        parameters: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StudioV1FlowEngagement:
        """Triggers a new Engagement for the Flow

        Args:
            flow_sid: The SID of the Flow.
            to: The Contact phone number to start a Studio Flow Engagement, available as variable
                ``{{contact.channel.address}}``.
            from_: The Twilio phone number to send messages or initiate calls from during the Flow Engagement. Available
                as variable ``{{flow.channel.address}}``
            parameters: A JSON string we will add to your flow's context and that you can access as variables inside
                your flow. For example, if you pass in ``Parameters={'name':'Zeke'}`` then inside a widget you can
                reference the variable ``{{flow.data.name}}`` which will return the string 'Zeke'. Note: the JSON value
                must explicitly be passed as a string, not as a hash object. Depending on your particular HTTP library,
                you may need to add quotes or URL encode your JSON string.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_engagement(
                flow_sid, to, from_, parameters=parameters, request_options=request_options
            )
        ).unwrap()

    async def delete_engagement(
        self, flow_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete this Engagement and all Steps relating to it.

        Args:
            flow_sid: The SID of the Flow to delete Engagements from.
            sid: The SID of the Engagement resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_engagement(flow_sid, sid, request_options=request_options)
        ).unwrap()

    async def fetch_engagement(
        self, flow_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> StudioV1FlowEngagement:
        """Retrieve an Engagement

        Args:
            flow_sid: The SID of the Flow.
            sid: The SID of the Engagement resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_engagement(flow_sid, sid, request_options=request_options)).unwrap()

    async def list_engagement(
        self,
        flow_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListEngagementResponse:
        """Retrieve a list of all Engagements for the Flow.

        Args:
            flow_sid: The SID of the Flow to read Engagements from.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_engagement(
                flow_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncStudioV1EngagementWithRawResponse:
        return self._with_raw_response


class StudioV1EngagementWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_engagement(
        self,
        flow_sid: str,
        to: str,
        from_: str,
        *,
        parameters: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StudioV1FlowEngagement, RawError]:
        """Triggers a new Engagement for the Flow

        Args:
            flow_sid: The SID of the Flow.
            to: The Contact phone number to start a Studio Flow Engagement, available as variable
                ``{{contact.channel.address}}``.
            from_: The Twilio phone number to send messages or initiate calls from during the Flow Engagement. Available
                as variable ``{{flow.channel.address}}``
            parameters: A JSON string we will add to your flow's context and that you can access as variables inside
                your flow. For example, if you pass in ``Parameters={'name':'Zeke'}`` then inside a widget you can
                reference the variable ``{{flow.data.name}}`` which will return the string 'Zeke'. Note: the JSON value
                must explicitly be passed as a string, not as a hash object. Depending on your particular HTTP library,
                you may need to add quotes or URL encode your JSON string.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default11("/v1/Flows/{FlowSid}/Engagements"),
            path_params=[param[str]("FlowSid", flow_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [param[str]("To", to), param[str]("From", from_), param[Any | None]("Parameters", parameters)]
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[StudioV1FlowEngagement],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_engagement(
        self, flow_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete this Engagement and all Steps relating to it.

        Args:
            flow_sid: The SID of the Flow to delete Engagements from.
            sid: The SID of the Engagement resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default11("/v1/Flows/{FlowSid}/Engagements/{Sid}"),
            path_params=[param[str]("FlowSid", flow_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_engagement(
        self, flow_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[StudioV1FlowEngagement, RawError]:
        """Retrieve an Engagement

        Args:
            flow_sid: The SID of the Flow.
            sid: The SID of the Engagement resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default11("/v1/Flows/{FlowSid}/Engagements/{Sid}"),
            path_params=[param[str]("FlowSid", flow_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[StudioV1FlowEngagement],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_engagement(
        self,
        flow_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListEngagementResponse, RawError]:
        """Retrieve a list of all Engagements for the Flow.

        Args:
            flow_sid: The SID of the Flow to read Engagements from.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default11("/v1/Flows/{FlowSid}/Engagements"),
            path_params=[param[str]("FlowSid", flow_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListEngagementResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncStudioV1EngagementWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_engagement(
        self,
        flow_sid: str,
        to: str,
        from_: str,
        *,
        parameters: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StudioV1FlowEngagement, RawError]:
        """Triggers a new Engagement for the Flow

        Args:
            flow_sid: The SID of the Flow.
            to: The Contact phone number to start a Studio Flow Engagement, available as variable
                ``{{contact.channel.address}}``.
            from_: The Twilio phone number to send messages or initiate calls from during the Flow Engagement. Available
                as variable ``{{flow.channel.address}}``
            parameters: A JSON string we will add to your flow's context and that you can access as variables inside
                your flow. For example, if you pass in ``Parameters={'name':'Zeke'}`` then inside a widget you can
                reference the variable ``{{flow.data.name}}`` which will return the string 'Zeke'. Note: the JSON value
                must explicitly be passed as a string, not as a hash object. Depending on your particular HTTP library,
                you may need to add quotes or URL encode your JSON string.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default11("/v1/Flows/{FlowSid}/Engagements"),
            path_params=[param[str]("FlowSid", flow_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [param[str]("To", to), param[str]("From", from_), param[Any | None]("Parameters", parameters)]
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[StudioV1FlowEngagement],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_engagement(
        self, flow_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete this Engagement and all Steps relating to it.

        Args:
            flow_sid: The SID of the Flow to delete Engagements from.
            sid: The SID of the Engagement resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default11("/v1/Flows/{FlowSid}/Engagements/{Sid}"),
            path_params=[param[str]("FlowSid", flow_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_engagement(
        self, flow_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[StudioV1FlowEngagement, RawError]:
        """Retrieve an Engagement

        Args:
            flow_sid: The SID of the Flow.
            sid: The SID of the Engagement resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default11("/v1/Flows/{FlowSid}/Engagements/{Sid}"),
            path_params=[param[str]("FlowSid", flow_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[StudioV1FlowEngagement],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_engagement(
        self,
        flow_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListEngagementResponse, RawError]:
        """Retrieve a list of all Engagements for the Flow.

        Args:
            flow_sid: The SID of the Flow to read Engagements from.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default11("/v1/Flows/{FlowSid}/Engagements"),
            path_params=[param[str]("FlowSid", flow_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListEngagementResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
