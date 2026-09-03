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
    RFC3339DateTime,
    SecuredRawResponse,
    empty_response,
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.enums.engagement_enum_status import EngagementEnumStatusOrStr
from ..models.list_execution_response1 import ListExecutionResponse1
from ..models.studio_v2_flow_execution import StudioV2FlowExecution
from ..server.server import Server


class StudioV2Execution:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = StudioV2ExecutionWithRawResponse(client, server, auth)

    def create_execution2(
        self,
        flow_sid: str,
        to: str,
        from_: str,
        *,
        parameters: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StudioV2FlowExecution:
        """Triggers a new Execution for the Flow

        Args:
            flow_sid: The SID of the Excecution's Flow.
            to: The Contact phone number to start a Studio Flow Execution, available as variable
                ``{{contact.channel.address}}``.
            from_: The Twilio phone number to send messages or initiate calls from during the Flow's Execution.
                Available as variable ``{{flow.channel.address}}``. For SMS, this can also be a Messaging Service SID.
            parameters: JSON data that will be added to the Flow's context and that can be accessed as variables inside
                your Flow. For example, if you pass in ``Parameters={"name":"Zeke"}``, a widget in your Flow can
                reference the variable ``{{flow.data.name}}``, which returns "Zeke". Note: the JSON value must
                explicitly be passed as a string, not as a hash object. Depending on your particular HTTP library, you
                may need to add quotes or URL encode the JSON string.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_execution2(
            flow_sid, to, from_, parameters=parameters, request_options=request_options
        ).unwrap()

    def delete_execution2(
        self, flow_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete the Execution and all Steps relating to it.

        Args:
            flow_sid: The SID of the Flow with the Execution resources to delete.
            sid: The SID of the Execution resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_execution2(flow_sid, sid, request_options=request_options).unwrap()

    def fetch_execution2(
        self, flow_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> StudioV2FlowExecution:
        """Retrieve an Execution

        Args:
            flow_sid: The SID of the Flow with the Execution resource to fetch
            sid: The SID of the Execution resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_execution2(flow_sid, sid, request_options=request_options).unwrap()

    def list_execution2(
        self,
        flow_sid: str,
        *,
        status: EngagementEnumStatusOrStr | None = None,
        date_created_from: RFC3339DateTime | None = None,
        date_created_to: RFC3339DateTime | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListExecutionResponse1:
        """Retrieve a list of all Executions for the Flow.

        Args:
            flow_sid: The SID of the Flow with the Execution resources to read.
            status: Only show Execution resources with the given status. Can be: ``active`` or ``ended``.
            date_created_from: Only show Execution resources starting on or after this `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time, given as ``YYYY-MM-DDThh:mm:ss-hh:mm``.
            date_created_to: Only show Execution resources starting before this `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time, given as ``YYYY-MM-DDThh:mm:ss-hh:mm``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_execution2(
            flow_sid,
            status=status,
            date_created_from=date_created_from,
            date_created_to=date_created_to,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_execution2(
        self,
        flow_sid: str,
        sid: str,
        status: EngagementEnumStatusOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StudioV2FlowExecution:
        """Update the status of an Execution to ``ended``.

        Args:
            flow_sid: The SID of the Flow with the Execution resources to update.
            sid: The SID of the Execution resource to update.
            status: The status of the Execution. Can be: ``active`` or ``ended``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_execution2(
            flow_sid, sid, status, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> StudioV2ExecutionWithRawResponse:
        return self._with_raw_response


class AsyncStudioV2Execution:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncStudioV2ExecutionWithRawResponse(client, server, auth)

    async def create_execution2(
        self,
        flow_sid: str,
        to: str,
        from_: str,
        *,
        parameters: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StudioV2FlowExecution:
        """Triggers a new Execution for the Flow

        Args:
            flow_sid: The SID of the Excecution's Flow.
            to: The Contact phone number to start a Studio Flow Execution, available as variable
                ``{{contact.channel.address}}``.
            from_: The Twilio phone number to send messages or initiate calls from during the Flow's Execution.
                Available as variable ``{{flow.channel.address}}``. For SMS, this can also be a Messaging Service SID.
            parameters: JSON data that will be added to the Flow's context and that can be accessed as variables inside
                your Flow. For example, if you pass in ``Parameters={"name":"Zeke"}``, a widget in your Flow can
                reference the variable ``{{flow.data.name}}``, which returns "Zeke". Note: the JSON value must
                explicitly be passed as a string, not as a hash object. Depending on your particular HTTP library, you
                may need to add quotes or URL encode the JSON string.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_execution2(
                flow_sid, to, from_, parameters=parameters, request_options=request_options
            )
        ).unwrap()

    async def delete_execution2(
        self, flow_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete the Execution and all Steps relating to it.

        Args:
            flow_sid: The SID of the Flow with the Execution resources to delete.
            sid: The SID of the Execution resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_execution2(flow_sid, sid, request_options=request_options)
        ).unwrap()

    async def fetch_execution2(
        self, flow_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> StudioV2FlowExecution:
        """Retrieve an Execution

        Args:
            flow_sid: The SID of the Flow with the Execution resource to fetch
            sid: The SID of the Execution resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_execution2(flow_sid, sid, request_options=request_options)).unwrap()

    async def list_execution2(
        self,
        flow_sid: str,
        *,
        status: EngagementEnumStatusOrStr | None = None,
        date_created_from: RFC3339DateTime | None = None,
        date_created_to: RFC3339DateTime | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListExecutionResponse1:
        """Retrieve a list of all Executions for the Flow.

        Args:
            flow_sid: The SID of the Flow with the Execution resources to read.
            status: Only show Execution resources with the given status. Can be: ``active`` or ``ended``.
            date_created_from: Only show Execution resources starting on or after this `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time, given as ``YYYY-MM-DDThh:mm:ss-hh:mm``.
            date_created_to: Only show Execution resources starting before this `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time, given as ``YYYY-MM-DDThh:mm:ss-hh:mm``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_execution2(
                flow_sid,
                status=status,
                date_created_from=date_created_from,
                date_created_to=date_created_to,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_execution2(
        self,
        flow_sid: str,
        sid: str,
        status: EngagementEnumStatusOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StudioV2FlowExecution:
        """Update the status of an Execution to ``ended``.

        Args:
            flow_sid: The SID of the Flow with the Execution resources to update.
            sid: The SID of the Execution resource to update.
            status: The status of the Execution. Can be: ``active`` or ``ended``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_execution2(flow_sid, sid, status, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncStudioV2ExecutionWithRawResponse:
        return self._with_raw_response


class StudioV2ExecutionWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_execution2(
        self,
        flow_sid: str,
        to: str,
        from_: str,
        *,
        parameters: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StudioV2FlowExecution, RawError]:
        """Triggers a new Execution for the Flow

        Args:
            flow_sid: The SID of the Excecution's Flow.
            to: The Contact phone number to start a Studio Flow Execution, available as variable
                ``{{contact.channel.address}}``.
            from_: The Twilio phone number to send messages or initiate calls from during the Flow's Execution.
                Available as variable ``{{flow.channel.address}}``. For SMS, this can also be a Messaging Service SID.
            parameters: JSON data that will be added to the Flow's context and that can be accessed as variables inside
                your Flow. For example, if you pass in ``Parameters={"name":"Zeke"}``, a widget in your Flow can
                reference the variable ``{{flow.data.name}}``, which returns "Zeke". Note: the JSON value must
                explicitly be passed as a string, not as a hash object. Depending on your particular HTTP library, you
                may need to add quotes or URL encode the JSON string.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default11("/v2/Flows/{FlowSid}/Executions"),
            path_params=[param[str]("FlowSid", flow_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [param[str]("To", to), param[str]("From", from_), param[Any | None]("Parameters", parameters)]
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[StudioV2FlowExecution],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_execution2(
        self, flow_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete the Execution and all Steps relating to it.

        Args:
            flow_sid: The SID of the Flow with the Execution resources to delete.
            sid: The SID of the Execution resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default11("/v2/Flows/{FlowSid}/Executions/{Sid}"),
            path_params=[param[str]("FlowSid", flow_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_execution2(
        self, flow_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[StudioV2FlowExecution, RawError]:
        """Retrieve an Execution

        Args:
            flow_sid: The SID of the Flow with the Execution resource to fetch
            sid: The SID of the Execution resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default11("/v2/Flows/{FlowSid}/Executions/{Sid}"),
            path_params=[param[str]("FlowSid", flow_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[StudioV2FlowExecution],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_execution2(
        self,
        flow_sid: str,
        *,
        status: EngagementEnumStatusOrStr | None = None,
        date_created_from: RFC3339DateTime | None = None,
        date_created_to: RFC3339DateTime | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListExecutionResponse1, RawError]:
        """Retrieve a list of all Executions for the Flow.

        Args:
            flow_sid: The SID of the Flow with the Execution resources to read.
            status: Only show Execution resources with the given status. Can be: ``active`` or ``ended``.
            date_created_from: Only show Execution resources starting on or after this `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time, given as ``YYYY-MM-DDThh:mm:ss-hh:mm``.
            date_created_to: Only show Execution resources starting before this `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time, given as ``YYYY-MM-DDThh:mm:ss-hh:mm``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default11("/v2/Flows/{FlowSid}/Executions"),
            path_params=[param[str]("FlowSid", flow_sid)],
            query_params=[
                param[EngagementEnumStatusOrStr | None]("status", status),
                param[RFC3339DateTime | None]("DateCreatedFrom", date_created_from),
                param[RFC3339DateTime | None]("DateCreatedTo", date_created_to),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListExecutionResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_execution2(
        self,
        flow_sid: str,
        sid: str,
        status: EngagementEnumStatusOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StudioV2FlowExecution, RawError]:
        """Update the status of an Execution to ``ended``.

        Args:
            flow_sid: The SID of the Flow with the Execution resources to update.
            sid: The SID of the Execution resource to update.
            status: The status of the Execution. Can be: ``active`` or ``ended``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default11("/v2/Flows/{FlowSid}/Executions/{Sid}"),
            path_params=[param[str]("FlowSid", flow_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[EngagementEnumStatusOrStr]("Status", status)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[StudioV2FlowExecution],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncStudioV2ExecutionWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_execution2(
        self,
        flow_sid: str,
        to: str,
        from_: str,
        *,
        parameters: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StudioV2FlowExecution, RawError]:
        """Triggers a new Execution for the Flow

        Args:
            flow_sid: The SID of the Excecution's Flow.
            to: The Contact phone number to start a Studio Flow Execution, available as variable
                ``{{contact.channel.address}}``.
            from_: The Twilio phone number to send messages or initiate calls from during the Flow's Execution.
                Available as variable ``{{flow.channel.address}}``. For SMS, this can also be a Messaging Service SID.
            parameters: JSON data that will be added to the Flow's context and that can be accessed as variables inside
                your Flow. For example, if you pass in ``Parameters={"name":"Zeke"}``, a widget in your Flow can
                reference the variable ``{{flow.data.name}}``, which returns "Zeke". Note: the JSON value must
                explicitly be passed as a string, not as a hash object. Depending on your particular HTTP library, you
                may need to add quotes or URL encode the JSON string.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default11("/v2/Flows/{FlowSid}/Executions"),
            path_params=[param[str]("FlowSid", flow_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [param[str]("To", to), param[str]("From", from_), param[Any | None]("Parameters", parameters)]
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[StudioV2FlowExecution],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_execution2(
        self, flow_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete the Execution and all Steps relating to it.

        Args:
            flow_sid: The SID of the Flow with the Execution resources to delete.
            sid: The SID of the Execution resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default11("/v2/Flows/{FlowSid}/Executions/{Sid}"),
            path_params=[param[str]("FlowSid", flow_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_execution2(
        self, flow_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[StudioV2FlowExecution, RawError]:
        """Retrieve an Execution

        Args:
            flow_sid: The SID of the Flow with the Execution resource to fetch
            sid: The SID of the Execution resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default11("/v2/Flows/{FlowSid}/Executions/{Sid}"),
            path_params=[param[str]("FlowSid", flow_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[StudioV2FlowExecution],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_execution2(
        self,
        flow_sid: str,
        *,
        status: EngagementEnumStatusOrStr | None = None,
        date_created_from: RFC3339DateTime | None = None,
        date_created_to: RFC3339DateTime | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListExecutionResponse1, RawError]:
        """Retrieve a list of all Executions for the Flow.

        Args:
            flow_sid: The SID of the Flow with the Execution resources to read.
            status: Only show Execution resources with the given status. Can be: ``active`` or ``ended``.
            date_created_from: Only show Execution resources starting on or after this `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time, given as ``YYYY-MM-DDThh:mm:ss-hh:mm``.
            date_created_to: Only show Execution resources starting before this `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time, given as ``YYYY-MM-DDThh:mm:ss-hh:mm``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default11("/v2/Flows/{FlowSid}/Executions"),
            path_params=[param[str]("FlowSid", flow_sid)],
            query_params=[
                param[EngagementEnumStatusOrStr | None]("status", status),
                param[RFC3339DateTime | None]("DateCreatedFrom", date_created_from),
                param[RFC3339DateTime | None]("DateCreatedTo", date_created_to),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListExecutionResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_execution2(
        self,
        flow_sid: str,
        sid: str,
        status: EngagementEnumStatusOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StudioV2FlowExecution, RawError]:
        """Update the status of an Execution to ``ended``.

        Args:
            flow_sid: The SID of the Flow with the Execution resources to update.
            sid: The SID of the Execution resource to update.
            status: The status of the Execution. Can be: ``active`` or ``ended``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default11("/v2/Flows/{FlowSid}/Executions/{Sid}"),
            path_params=[param[str]("FlowSid", flow_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[EngagementEnumStatusOrStr]("Status", status)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[StudioV2FlowExecution],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
