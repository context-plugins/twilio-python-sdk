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
from ..models.enums.end_user_enum_type import EndUserEnumTypeOrStr
from ..models.list_end_user_response import ListEndUserResponse
from ..models.numbers_v2_regulatory_compliance_end_user import NumbersV2RegulatoryComplianceEndUser
from ..server.server import Server


class NumbersV2EndUser:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NumbersV2EndUserWithRawResponse(client, server, auth)

    def create_end_user(
        self,
        friendly_name: str,
        type_: EndUserEnumTypeOrStr,
        *,
        attributes: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> NumbersV2RegulatoryComplianceEndUser:
        """Create a new End User.

        Args:
            friendly_name: The string that you assigned to describe the resource.
            type_: The type of end user of the Bundle resource - can be ``individual`` or ``business``.
            attributes: The set of parameters that are the attributes of the End User resource which are derived End
                User Types.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_end_user(
            friendly_name, type_, attributes=attributes, request_options=request_options
        ).unwrap()

    def delete_end_user(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Delete a specific End User.

        Args:
            sid: The unique string created by Twilio to identify the End User resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_end_user(sid, request_options=request_options).unwrap()

    def fetch_end_user(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV2RegulatoryComplianceEndUser:
        """Fetch specific End User Instance.

        Args:
            sid: The unique string created by Twilio to identify the End User resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_end_user(sid, request_options=request_options).unwrap()

    def list_end_user(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListEndUserResponse:
        """Retrieve a list of all End User for an account.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_end_user(
            page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    def update_end_user(
        self,
        sid: str,
        *,
        friendly_name: str | None = None,
        attributes: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> NumbersV2RegulatoryComplianceEndUser:
        """Update an existing End User.

        Args:
            sid: The unique string created by Twilio to identify the End User resource.
            friendly_name: The string that you assigned to describe the resource.
            attributes: The set of parameters that are the attributes of the End User resource which are derived End
                User Types.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_end_user(
            sid, friendly_name=friendly_name, attributes=attributes, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> NumbersV2EndUserWithRawResponse:
        return self._with_raw_response


class AsyncNumbersV2EndUser:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNumbersV2EndUserWithRawResponse(client, server, auth)

    async def create_end_user(
        self,
        friendly_name: str,
        type_: EndUserEnumTypeOrStr,
        *,
        attributes: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> NumbersV2RegulatoryComplianceEndUser:
        """Create a new End User.

        Args:
            friendly_name: The string that you assigned to describe the resource.
            type_: The type of end user of the Bundle resource - can be ``individual`` or ``business``.
            attributes: The set of parameters that are the attributes of the End User resource which are derived End
                User Types.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_end_user(
                friendly_name, type_, attributes=attributes, request_options=request_options
            )
        ).unwrap()

    async def delete_end_user(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Delete a specific End User.

        Args:
            sid: The unique string created by Twilio to identify the End User resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_end_user(sid, request_options=request_options)).unwrap()

    async def fetch_end_user(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV2RegulatoryComplianceEndUser:
        """Fetch specific End User Instance.

        Args:
            sid: The unique string created by Twilio to identify the End User resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_end_user(sid, request_options=request_options)).unwrap()

    async def list_end_user(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListEndUserResponse:
        """Retrieve a list of all End User for an account.

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
            await self._with_raw_response.list_end_user(
                page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    async def update_end_user(
        self,
        sid: str,
        *,
        friendly_name: str | None = None,
        attributes: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> NumbersV2RegulatoryComplianceEndUser:
        """Update an existing End User.

        Args:
            sid: The unique string created by Twilio to identify the End User resource.
            friendly_name: The string that you assigned to describe the resource.
            attributes: The set of parameters that are the attributes of the End User resource which are derived End
                User Types.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_end_user(
                sid, friendly_name=friendly_name, attributes=attributes, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncNumbersV2EndUserWithRawResponse:
        return self._with_raw_response


class NumbersV2EndUserWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_end_user(
        self,
        friendly_name: str,
        type_: EndUserEnumTypeOrStr,
        *,
        attributes: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[NumbersV2RegulatoryComplianceEndUser, RawError]:
        """Create a new End User.

        Args:
            friendly_name: The string that you assigned to describe the resource.
            type_: The type of end user of the Bundle resource - can be ``individual`` or ``business``.
            attributes: The set of parameters that are the attributes of the End User resource which are derived End
                User Types.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v2/RegulatoryCompliance/EndUsers"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[EndUserEnumTypeOrStr]("Type", type_),
                    param[Any | None]("Attributes", attributes),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2RegulatoryComplianceEndUser],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_end_user(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific End User.

        Args:
            sid: The unique string created by Twilio to identify the End User resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default5("/v2/RegulatoryCompliance/EndUsers/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_end_user(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV2RegulatoryComplianceEndUser, RawError]:
        """Fetch specific End User Instance.

        Args:
            sid: The unique string created by Twilio to identify the End User resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/RegulatoryCompliance/EndUsers/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2RegulatoryComplianceEndUser],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_end_user(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListEndUserResponse, RawError]:
        """Retrieve a list of all End User for an account.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/RegulatoryCompliance/EndUsers"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListEndUserResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_end_user(
        self,
        sid: str,
        *,
        friendly_name: str | None = None,
        attributes: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[NumbersV2RegulatoryComplianceEndUser, RawError]:
        """Update an existing End User.

        Args:
            sid: The unique string created by Twilio to identify the End User resource.
            friendly_name: The string that you assigned to describe the resource.
            attributes: The set of parameters that are the attributes of the End User resource which are derived End
                User Types.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v2/RegulatoryCompliance/EndUsers/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [param[str | None]("FriendlyName", friendly_name), param[Any | None]("Attributes", attributes)]
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2RegulatoryComplianceEndUser],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncNumbersV2EndUserWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_end_user(
        self,
        friendly_name: str,
        type_: EndUserEnumTypeOrStr,
        *,
        attributes: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[NumbersV2RegulatoryComplianceEndUser, RawError]:
        """Create a new End User.

        Args:
            friendly_name: The string that you assigned to describe the resource.
            type_: The type of end user of the Bundle resource - can be ``individual`` or ``business``.
            attributes: The set of parameters that are the attributes of the End User resource which are derived End
                User Types.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v2/RegulatoryCompliance/EndUsers"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[EndUserEnumTypeOrStr]("Type", type_),
                    param[Any | None]("Attributes", attributes),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2RegulatoryComplianceEndUser],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_end_user(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific End User.

        Args:
            sid: The unique string created by Twilio to identify the End User resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default5("/v2/RegulatoryCompliance/EndUsers/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_end_user(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV2RegulatoryComplianceEndUser, RawError]:
        """Fetch specific End User Instance.

        Args:
            sid: The unique string created by Twilio to identify the End User resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/RegulatoryCompliance/EndUsers/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2RegulatoryComplianceEndUser],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_end_user(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListEndUserResponse, RawError]:
        """Retrieve a list of all End User for an account.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/RegulatoryCompliance/EndUsers"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListEndUserResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_end_user(
        self,
        sid: str,
        *,
        friendly_name: str | None = None,
        attributes: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[NumbersV2RegulatoryComplianceEndUser, RawError]:
        """Update an existing End User.

        Args:
            sid: The unique string created by Twilio to identify the End User resource.
            friendly_name: The string that you assigned to describe the resource.
            attributes: The set of parameters that are the attributes of the End User resource which are derived End
                User Types.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v2/RegulatoryCompliance/EndUsers/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [param[str | None]("FriendlyName", friendly_name), param[Any | None]("Attributes", attributes)]
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2RegulatoryComplianceEndUser],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
