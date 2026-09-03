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
from ..models.enums.trust_product_enum_status import TrustProductEnumStatusOrStr
from ..models.list_trust_product_response import ListTrustProductResponse
from ..models.trusthub_v1_trust_product import TrusthubV1TrustProduct
from ..server.server import Server


class TrusthubV1TrustProducts:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TrusthubV1TrustProductsWithRawResponse(client, server, auth)

    def create_trust_product(
        self,
        friendly_name: str,
        email: str,
        policy_sid: str,
        *,
        status_callback: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TrusthubV1TrustProduct:
        """Create a new Trust Product.

        Args:
            friendly_name: The string that you assigned to describe the resource.
            email: The email address that will receive updates when the Trust Product resource changes status.
            policy_sid: The unique string of a policy that is associated to the Trust Product resource.
            status_callback: The URL we call to inform your application of status changes.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_trust_product(
            friendly_name, email, policy_sid, status_callback=status_callback, request_options=request_options
        ).unwrap()

    def delete_trust_product(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Delete a specific Trust Product.

        Args:
            sid: The unique string that we created to identify the Trust Product resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_trust_product(sid, request_options=request_options).unwrap()

    def fetch_trust_product(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TrusthubV1TrustProduct:
        """Fetch a specific Trust Product instance.

        Args:
            sid: The unique string that we created to identify the Trust Product resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_trust_product(sid, request_options=request_options).unwrap()

    def list_trust_product(
        self,
        *,
        status: TrustProductEnumStatusOrStr | None = None,
        friendly_name: str | None = None,
        policy_sid: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListTrustProductResponse:
        """Retrieve a list of all Trust Products for an account.

        Args:
            status: The verification status of the Trust Product resource.
            friendly_name: The string that you assigned to describe the resource.
            policy_sid: The unique string of a policy that is associated to the Trust Product resource.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_trust_product(
            status=status,
            friendly_name=friendly_name,
            policy_sid=policy_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_trust_product(
        self,
        sid: str,
        *,
        status: TrustProductEnumStatusOrStr | None = None,
        status_callback: str | None = None,
        friendly_name: str | None = None,
        email: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TrusthubV1TrustProduct:
        """Updates a Trust Product in an account.

        Args:
            sid: The unique string that we created to identify the Trust Product resource.
            status: The verification status of the Trust Product resource.
            status_callback: The URL we call to inform your application of status changes.
            friendly_name: The string that you assigned to describe the resource.
            email: The email address that will receive updates when the Trust Product resource changes status.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_trust_product(
            sid,
            status=status,
            status_callback=status_callback,
            friendly_name=friendly_name,
            email=email,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> TrusthubV1TrustProductsWithRawResponse:
        return self._with_raw_response


class AsyncTrusthubV1TrustProducts:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTrusthubV1TrustProductsWithRawResponse(client, server, auth)

    async def create_trust_product(
        self,
        friendly_name: str,
        email: str,
        policy_sid: str,
        *,
        status_callback: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TrusthubV1TrustProduct:
        """Create a new Trust Product.

        Args:
            friendly_name: The string that you assigned to describe the resource.
            email: The email address that will receive updates when the Trust Product resource changes status.
            policy_sid: The unique string of a policy that is associated to the Trust Product resource.
            status_callback: The URL we call to inform your application of status changes.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_trust_product(
                friendly_name, email, policy_sid, status_callback=status_callback, request_options=request_options
            )
        ).unwrap()

    async def delete_trust_product(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Delete a specific Trust Product.

        Args:
            sid: The unique string that we created to identify the Trust Product resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_trust_product(sid, request_options=request_options)).unwrap()

    async def fetch_trust_product(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TrusthubV1TrustProduct:
        """Fetch a specific Trust Product instance.

        Args:
            sid: The unique string that we created to identify the Trust Product resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_trust_product(sid, request_options=request_options)).unwrap()

    async def list_trust_product(
        self,
        *,
        status: TrustProductEnumStatusOrStr | None = None,
        friendly_name: str | None = None,
        policy_sid: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListTrustProductResponse:
        """Retrieve a list of all Trust Products for an account.

        Args:
            status: The verification status of the Trust Product resource.
            friendly_name: The string that you assigned to describe the resource.
            policy_sid: The unique string of a policy that is associated to the Trust Product resource.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_trust_product(
                status=status,
                friendly_name=friendly_name,
                policy_sid=policy_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_trust_product(
        self,
        sid: str,
        *,
        status: TrustProductEnumStatusOrStr | None = None,
        status_callback: str | None = None,
        friendly_name: str | None = None,
        email: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TrusthubV1TrustProduct:
        """Updates a Trust Product in an account.

        Args:
            sid: The unique string that we created to identify the Trust Product resource.
            status: The verification status of the Trust Product resource.
            status_callback: The URL we call to inform your application of status changes.
            friendly_name: The string that you assigned to describe the resource.
            email: The email address that will receive updates when the Trust Product resource changes status.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_trust_product(
                sid,
                status=status,
                status_callback=status_callback,
                friendly_name=friendly_name,
                email=email,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTrusthubV1TrustProductsWithRawResponse:
        return self._with_raw_response


class TrusthubV1TrustProductsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_trust_product(
        self,
        friendly_name: str,
        email: str,
        policy_sid: str,
        *,
        status_callback: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TrusthubV1TrustProduct, RawError]:
        """Create a new Trust Product.

        Args:
            friendly_name: The string that you assigned to describe the resource.
            email: The email address that will receive updates when the Trust Product resource changes status.
            policy_sid: The unique string of a policy that is associated to the Trust Product resource.
            status_callback: The URL we call to inform your application of status changes.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/v1/TrustProducts"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[str]("Email", email),
                    param[str]("PolicySid", policy_sid),
                    param[str | None]("StatusCallback", status_callback),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1TrustProduct],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_trust_product(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Trust Product.

        Args:
            sid: The unique string that we created to identify the Trust Product resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default9("/v1/TrustProducts/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_trust_product(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TrusthubV1TrustProduct, RawError]:
        """Fetch a specific Trust Product instance.

        Args:
            sid: The unique string that we created to identify the Trust Product resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/v1/TrustProducts/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1TrustProduct],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_trust_product(
        self,
        *,
        status: TrustProductEnumStatusOrStr | None = None,
        friendly_name: str | None = None,
        policy_sid: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListTrustProductResponse, RawError]:
        """Retrieve a list of all Trust Products for an account.

        Args:
            status: The verification status of the Trust Product resource.
            friendly_name: The string that you assigned to describe the resource.
            policy_sid: The unique string of a policy that is associated to the Trust Product resource.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/v1/TrustProducts"),
            query_params=[
                param[TrustProductEnumStatusOrStr | None]("Status", status),
                param[str | None]("FriendlyName", friendly_name),
                param[str | None]("PolicySid", policy_sid),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListTrustProductResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_trust_product(
        self,
        sid: str,
        *,
        status: TrustProductEnumStatusOrStr | None = None,
        status_callback: str | None = None,
        friendly_name: str | None = None,
        email: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TrusthubV1TrustProduct, RawError]:
        """Updates a Trust Product in an account.

        Args:
            sid: The unique string that we created to identify the Trust Product resource.
            status: The verification status of the Trust Product resource.
            status_callback: The URL we call to inform your application of status changes.
            friendly_name: The string that you assigned to describe the resource.
            email: The email address that will receive updates when the Trust Product resource changes status.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/v1/TrustProducts/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[TrustProductEnumStatusOrStr | None]("Status", status),
                    param[str | None]("StatusCallback", status_callback),
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("Email", email),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1TrustProduct],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTrusthubV1TrustProductsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_trust_product(
        self,
        friendly_name: str,
        email: str,
        policy_sid: str,
        *,
        status_callback: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TrusthubV1TrustProduct, RawError]:
        """Create a new Trust Product.

        Args:
            friendly_name: The string that you assigned to describe the resource.
            email: The email address that will receive updates when the Trust Product resource changes status.
            policy_sid: The unique string of a policy that is associated to the Trust Product resource.
            status_callback: The URL we call to inform your application of status changes.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/v1/TrustProducts"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[str]("Email", email),
                    param[str]("PolicySid", policy_sid),
                    param[str | None]("StatusCallback", status_callback),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1TrustProduct],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_trust_product(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Trust Product.

        Args:
            sid: The unique string that we created to identify the Trust Product resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default9("/v1/TrustProducts/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_trust_product(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TrusthubV1TrustProduct, RawError]:
        """Fetch a specific Trust Product instance.

        Args:
            sid: The unique string that we created to identify the Trust Product resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/v1/TrustProducts/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1TrustProduct],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_trust_product(
        self,
        *,
        status: TrustProductEnumStatusOrStr | None = None,
        friendly_name: str | None = None,
        policy_sid: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListTrustProductResponse, RawError]:
        """Retrieve a list of all Trust Products for an account.

        Args:
            status: The verification status of the Trust Product resource.
            friendly_name: The string that you assigned to describe the resource.
            policy_sid: The unique string of a policy that is associated to the Trust Product resource.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/v1/TrustProducts"),
            query_params=[
                param[TrustProductEnumStatusOrStr | None]("Status", status),
                param[str | None]("FriendlyName", friendly_name),
                param[str | None]("PolicySid", policy_sid),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListTrustProductResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_trust_product(
        self,
        sid: str,
        *,
        status: TrustProductEnumStatusOrStr | None = None,
        status_callback: str | None = None,
        friendly_name: str | None = None,
        email: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TrusthubV1TrustProduct, RawError]:
        """Updates a Trust Product in an account.

        Args:
            sid: The unique string that we created to identify the Trust Product resource.
            status: The verification status of the Trust Product resource.
            status_callback: The URL we call to inform your application of status changes.
            friendly_name: The string that you assigned to describe the resource.
            email: The email address that will receive updates when the Trust Product resource changes status.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/v1/TrustProducts/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[TrustProductEnumStatusOrStr | None]("Status", status),
                    param[str | None]("StatusCallback", status_callback),
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("Email", email),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1TrustProduct],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
