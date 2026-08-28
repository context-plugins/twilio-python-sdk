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
from ..models.enums.flow_enum_status import FlowEnumStatusOrStr
from ..models.list_flow_response1 import ListFlowResponse1
from ..models.studio_v2_flow import StudioV2Flow
from ..server.server import Server


class StudioV2FlowApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = StudioV2FlowApiWithRawResponse(client, server, auth)

    def create_flow(
        self,
        friendly_name: str,
        status: FlowEnumStatusOrStr,
        definition: Any,
        *,
        commit_message: str | None = None,
        author_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StudioV2Flow:
        """Create a Flow.

        Args:
            friendly_name: The string that you assigned to describe the Flow.
            status: The status of the Flow. Can be: ``draft`` or ``published``.
            definition: JSON representation of flow definition.
            commit_message: Description of change made in the revision.
            author_sid: The SID of the User that created the Flow.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_flow(
            friendly_name,
            status,
            definition,
            commit_message=commit_message,
            author_sid=author_sid,
            request_options=request_options,
        ).unwrap()

    def delete_flow2(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Delete a specific Flow.

        Args:
            sid: The SID of the Flow resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_flow2(sid, request_options=request_options).unwrap()

    def fetch_flow2(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> StudioV2Flow:
        """Retrieve a specific Flow.

        Args:
            sid: The SID of the Flow resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_flow2(sid, request_options=request_options).unwrap()

    def list_flow2(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListFlowResponse1:
        """Retrieve a list of all Flows.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_flow2(
            page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    def update_flow(
        self,
        sid: str,
        status: FlowEnumStatusOrStr,
        *,
        friendly_name: str | None = None,
        definition: Any | None = None,
        commit_message: str | None = None,
        author_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StudioV2Flow:
        """Update a Flow.

        Args:
            sid: The SID of the Flow resource to fetch.
            status: The status of the Flow. Can be: ``draft`` or ``published``.
            friendly_name: The string that you assigned to describe the Flow.
            definition: JSON representation of flow definition.
            commit_message: Description of change made in the revision.
            author_sid: The SID of the User that created or last updated the Flow.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_flow(
            sid,
            status,
            friendly_name=friendly_name,
            definition=definition,
            commit_message=commit_message,
            author_sid=author_sid,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> StudioV2FlowApiWithRawResponse:
        return self._with_raw_response


class AsyncStudioV2FlowApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncStudioV2FlowApiWithRawResponse(client, server, auth)

    async def create_flow(
        self,
        friendly_name: str,
        status: FlowEnumStatusOrStr,
        definition: Any,
        *,
        commit_message: str | None = None,
        author_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StudioV2Flow:
        """Create a Flow.

        Args:
            friendly_name: The string that you assigned to describe the Flow.
            status: The status of the Flow. Can be: ``draft`` or ``published``.
            definition: JSON representation of flow definition.
            commit_message: Description of change made in the revision.
            author_sid: The SID of the User that created the Flow.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_flow(
                friendly_name,
                status,
                definition,
                commit_message=commit_message,
                author_sid=author_sid,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_flow2(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Delete a specific Flow.

        Args:
            sid: The SID of the Flow resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_flow2(sid, request_options=request_options)).unwrap()

    async def fetch_flow2(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> StudioV2Flow:
        """Retrieve a specific Flow.

        Args:
            sid: The SID of the Flow resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_flow2(sid, request_options=request_options)).unwrap()

    async def list_flow2(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListFlowResponse1:
        """Retrieve a list of all Flows.

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
            await self._with_raw_response.list_flow2(
                page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    async def update_flow(
        self,
        sid: str,
        status: FlowEnumStatusOrStr,
        *,
        friendly_name: str | None = None,
        definition: Any | None = None,
        commit_message: str | None = None,
        author_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StudioV2Flow:
        """Update a Flow.

        Args:
            sid: The SID of the Flow resource to fetch.
            status: The status of the Flow. Can be: ``draft`` or ``published``.
            friendly_name: The string that you assigned to describe the Flow.
            definition: JSON representation of flow definition.
            commit_message: Description of change made in the revision.
            author_sid: The SID of the User that created or last updated the Flow.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_flow(
                sid,
                status,
                friendly_name=friendly_name,
                definition=definition,
                commit_message=commit_message,
                author_sid=author_sid,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncStudioV2FlowApiWithRawResponse:
        return self._with_raw_response


class StudioV2FlowApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_flow(
        self,
        friendly_name: str,
        status: FlowEnumStatusOrStr,
        definition: Any,
        *,
        commit_message: str | None = None,
        author_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StudioV2Flow, RawError]:
        """Create a Flow.

        Args:
            friendly_name: The string that you assigned to describe the Flow.
            status: The status of the Flow. Can be: ``draft`` or ``published``.
            definition: JSON representation of flow definition.
            commit_message: Description of change made in the revision.
            author_sid: The SID of the User that created the Flow.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default11("/v2/Flows"),
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[FlowEnumStatusOrStr]("Status", status),
                    param[Any]("Definition", definition),
                    param[str | None]("CommitMessage", commit_message),
                    param[str | None]("AuthorSid", author_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[StudioV2Flow],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_flow2(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Flow.

        Args:
            sid: The SID of the Flow resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default11("/v2/Flows/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_flow2(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[StudioV2Flow, RawError]:
        """Retrieve a specific Flow.

        Args:
            sid: The SID of the Flow resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default11("/v2/Flows/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[StudioV2Flow],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_flow2(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListFlowResponse1, RawError]:
        """Retrieve a list of all Flows.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default11("/v2/Flows"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListFlowResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_flow(
        self,
        sid: str,
        status: FlowEnumStatusOrStr,
        *,
        friendly_name: str | None = None,
        definition: Any | None = None,
        commit_message: str | None = None,
        author_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StudioV2Flow, RawError]:
        """Update a Flow.

        Args:
            sid: The SID of the Flow resource to fetch.
            status: The status of the Flow. Can be: ``draft`` or ``published``.
            friendly_name: The string that you assigned to describe the Flow.
            definition: JSON representation of flow definition.
            commit_message: Description of change made in the revision.
            author_sid: The SID of the User that created or last updated the Flow.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default11("/v2/Flows/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            body=form_body(
                [
                    param[FlowEnumStatusOrStr]("Status", status),
                    param[str | None]("FriendlyName", friendly_name),
                    param[Any | None]("Definition", definition),
                    param[str | None]("CommitMessage", commit_message),
                    param[str | None]("AuthorSid", author_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[StudioV2Flow],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncStudioV2FlowApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_flow(
        self,
        friendly_name: str,
        status: FlowEnumStatusOrStr,
        definition: Any,
        *,
        commit_message: str | None = None,
        author_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StudioV2Flow, RawError]:
        """Create a Flow.

        Args:
            friendly_name: The string that you assigned to describe the Flow.
            status: The status of the Flow. Can be: ``draft`` or ``published``.
            definition: JSON representation of flow definition.
            commit_message: Description of change made in the revision.
            author_sid: The SID of the User that created the Flow.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default11("/v2/Flows"),
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[FlowEnumStatusOrStr]("Status", status),
                    param[Any]("Definition", definition),
                    param[str | None]("CommitMessage", commit_message),
                    param[str | None]("AuthorSid", author_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[StudioV2Flow],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_flow2(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Flow.

        Args:
            sid: The SID of the Flow resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default11("/v2/Flows/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_flow2(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[StudioV2Flow, RawError]:
        """Retrieve a specific Flow.

        Args:
            sid: The SID of the Flow resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default11("/v2/Flows/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[StudioV2Flow],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_flow2(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListFlowResponse1, RawError]:
        """Retrieve a list of all Flows.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default11("/v2/Flows"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListFlowResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_flow(
        self,
        sid: str,
        status: FlowEnumStatusOrStr,
        *,
        friendly_name: str | None = None,
        definition: Any | None = None,
        commit_message: str | None = None,
        author_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StudioV2Flow, RawError]:
        """Update a Flow.

        Args:
            sid: The SID of the Flow resource to fetch.
            status: The status of the Flow. Can be: ``draft`` or ``published``.
            friendly_name: The string that you assigned to describe the Flow.
            definition: JSON representation of flow definition.
            commit_message: Description of change made in the revision.
            author_sid: The SID of the User that created or last updated the Flow.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default11("/v2/Flows/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            body=form_body(
                [
                    param[FlowEnumStatusOrStr]("Status", status),
                    param[str | None]("FriendlyName", friendly_name),
                    param[Any | None]("Definition", definition),
                    param[str | None]("CommitMessage", commit_message),
                    param[str | None]("AuthorSid", author_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[StudioV2Flow],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
