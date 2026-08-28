from __future__ import annotations

from pydantic import AnyUrl

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
from ..models.enums.customer_profile_enum_status import CustomerProfileEnumStatusOrStr
from ..models.list_customer_profile_response import ListCustomerProfileResponse
from ..models.trusthub_v1_customer_profile import TrusthubV1CustomerProfile
from ..server.server import Server


class TrusthubV1CustomerProfiles:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TrusthubV1CustomerProfilesWithRawResponse(client, server, auth)

    def create_customer_profile(
        self,
        friendly_name: str,
        email: str,
        policy_sid: str,
        *,
        status_callback: AnyUrl | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TrusthubV1CustomerProfile:
        """Create a new Customer-Profile.

        Args:
            friendly_name: The string that you assigned to describe the resource.
            email: The email address that will receive updates when the Customer-Profile resource changes status.
            policy_sid: The unique string of a policy that is associated to the Customer-Profile resource.
            status_callback: The URL we call to inform your application of status changes.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_customer_profile(
            friendly_name, email, policy_sid, status_callback=status_callback, request_options=request_options
        ).unwrap()

    def delete_customer_profile(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Delete a specific Customer-Profile.

        Args:
            sid: The unique string that we created to identify the Customer-Profile resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_customer_profile(sid, request_options=request_options).unwrap()

    def fetch_customer_profile(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TrusthubV1CustomerProfile:
        """Fetch a specific Customer-Profile instance.

        Args:
            sid: The unique string that we created to identify the Customer-Profile resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_customer_profile(sid, request_options=request_options).unwrap()

    def list_customer_profile(
        self,
        *,
        status: CustomerProfileEnumStatusOrStr | None = None,
        friendly_name: str | None = None,
        policy_sid: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCustomerProfileResponse:
        """Retrieve a list of all Customer-Profiles for an account.

        Args:
            status: The verification status of the Customer-Profile resource.
            friendly_name: The string that you assigned to describe the resource.
            policy_sid: The unique string of a policy that is associated to the Customer-Profile resource.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_customer_profile(
            status=status,
            friendly_name=friendly_name,
            policy_sid=policy_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_customer_profile(
        self,
        sid: str,
        *,
        status: CustomerProfileEnumStatusOrStr | None = None,
        status_callback: AnyUrl | None = None,
        friendly_name: str | None = None,
        email: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TrusthubV1CustomerProfile:
        """Updates a Customer-Profile in an account.

        Args:
            sid: The unique string that we created to identify the Customer-Profile resource.
            status: The verification status of the Customer-Profile resource.
            status_callback: The URL we call to inform your application of status changes.
            friendly_name: The string that you assigned to describe the resource.
            email: The email address that will receive updates when the Customer-Profile resource changes status.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_customer_profile(
            sid,
            status=status,
            status_callback=status_callback,
            friendly_name=friendly_name,
            email=email,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> TrusthubV1CustomerProfilesWithRawResponse:
        return self._with_raw_response


class AsyncTrusthubV1CustomerProfiles:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTrusthubV1CustomerProfilesWithRawResponse(client, server, auth)

    async def create_customer_profile(
        self,
        friendly_name: str,
        email: str,
        policy_sid: str,
        *,
        status_callback: AnyUrl | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TrusthubV1CustomerProfile:
        """Create a new Customer-Profile.

        Args:
            friendly_name: The string that you assigned to describe the resource.
            email: The email address that will receive updates when the Customer-Profile resource changes status.
            policy_sid: The unique string of a policy that is associated to the Customer-Profile resource.
            status_callback: The URL we call to inform your application of status changes.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_customer_profile(
                friendly_name, email, policy_sid, status_callback=status_callback, request_options=request_options
            )
        ).unwrap()

    async def delete_customer_profile(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Delete a specific Customer-Profile.

        Args:
            sid: The unique string that we created to identify the Customer-Profile resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_customer_profile(sid, request_options=request_options)).unwrap()

    async def fetch_customer_profile(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TrusthubV1CustomerProfile:
        """Fetch a specific Customer-Profile instance.

        Args:
            sid: The unique string that we created to identify the Customer-Profile resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_customer_profile(sid, request_options=request_options)).unwrap()

    async def list_customer_profile(
        self,
        *,
        status: CustomerProfileEnumStatusOrStr | None = None,
        friendly_name: str | None = None,
        policy_sid: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCustomerProfileResponse:
        """Retrieve a list of all Customer-Profiles for an account.

        Args:
            status: The verification status of the Customer-Profile resource.
            friendly_name: The string that you assigned to describe the resource.
            policy_sid: The unique string of a policy that is associated to the Customer-Profile resource.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_customer_profile(
                status=status,
                friendly_name=friendly_name,
                policy_sid=policy_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_customer_profile(
        self,
        sid: str,
        *,
        status: CustomerProfileEnumStatusOrStr | None = None,
        status_callback: AnyUrl | None = None,
        friendly_name: str | None = None,
        email: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TrusthubV1CustomerProfile:
        """Updates a Customer-Profile in an account.

        Args:
            sid: The unique string that we created to identify the Customer-Profile resource.
            status: The verification status of the Customer-Profile resource.
            status_callback: The URL we call to inform your application of status changes.
            friendly_name: The string that you assigned to describe the resource.
            email: The email address that will receive updates when the Customer-Profile resource changes status.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_customer_profile(
                sid,
                status=status,
                status_callback=status_callback,
                friendly_name=friendly_name,
                email=email,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTrusthubV1CustomerProfilesWithRawResponse:
        return self._with_raw_response


class TrusthubV1CustomerProfilesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_customer_profile(
        self,
        friendly_name: str,
        email: str,
        policy_sid: str,
        *,
        status_callback: AnyUrl | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TrusthubV1CustomerProfile, RawError]:
        """Create a new Customer-Profile.

        Args:
            friendly_name: The string that you assigned to describe the resource.
            email: The email address that will receive updates when the Customer-Profile resource changes status.
            policy_sid: The unique string of a policy that is associated to the Customer-Profile resource.
            status_callback: The URL we call to inform your application of status changes.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/v1/CustomerProfiles"),
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[str]("Email", email),
                    param[str]("PolicySid", policy_sid),
                    param[AnyUrl | None]("StatusCallback", status_callback),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1CustomerProfile],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_customer_profile(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Customer-Profile.

        Args:
            sid: The unique string that we created to identify the Customer-Profile resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default9("/v1/CustomerProfiles/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_customer_profile(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TrusthubV1CustomerProfile, RawError]:
        """Fetch a specific Customer-Profile instance.

        Args:
            sid: The unique string that we created to identify the Customer-Profile resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/v1/CustomerProfiles/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1CustomerProfile],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_customer_profile(
        self,
        *,
        status: CustomerProfileEnumStatusOrStr | None = None,
        friendly_name: str | None = None,
        policy_sid: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCustomerProfileResponse, RawError]:
        """Retrieve a list of all Customer-Profiles for an account.

        Args:
            status: The verification status of the Customer-Profile resource.
            friendly_name: The string that you assigned to describe the resource.
            policy_sid: The unique string of a policy that is associated to the Customer-Profile resource.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/v1/CustomerProfiles"),
            query_params=[
                param[CustomerProfileEnumStatusOrStr | None]("Status", status),
                param[str | None]("FriendlyName", friendly_name),
                param[str | None]("PolicySid", policy_sid),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListCustomerProfileResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_customer_profile(
        self,
        sid: str,
        *,
        status: CustomerProfileEnumStatusOrStr | None = None,
        status_callback: AnyUrl | None = None,
        friendly_name: str | None = None,
        email: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TrusthubV1CustomerProfile, RawError]:
        """Updates a Customer-Profile in an account.

        Args:
            sid: The unique string that we created to identify the Customer-Profile resource.
            status: The verification status of the Customer-Profile resource.
            status_callback: The URL we call to inform your application of status changes.
            friendly_name: The string that you assigned to describe the resource.
            email: The email address that will receive updates when the Customer-Profile resource changes status.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/v1/CustomerProfiles/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            body=form_body(
                [
                    param[CustomerProfileEnumStatusOrStr | None]("Status", status),
                    param[AnyUrl | None]("StatusCallback", status_callback),
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("Email", email),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1CustomerProfile],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTrusthubV1CustomerProfilesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_customer_profile(
        self,
        friendly_name: str,
        email: str,
        policy_sid: str,
        *,
        status_callback: AnyUrl | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TrusthubV1CustomerProfile, RawError]:
        """Create a new Customer-Profile.

        Args:
            friendly_name: The string that you assigned to describe the resource.
            email: The email address that will receive updates when the Customer-Profile resource changes status.
            policy_sid: The unique string of a policy that is associated to the Customer-Profile resource.
            status_callback: The URL we call to inform your application of status changes.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/v1/CustomerProfiles"),
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[str]("Email", email),
                    param[str]("PolicySid", policy_sid),
                    param[AnyUrl | None]("StatusCallback", status_callback),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1CustomerProfile],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_customer_profile(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Customer-Profile.

        Args:
            sid: The unique string that we created to identify the Customer-Profile resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default9("/v1/CustomerProfiles/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_customer_profile(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TrusthubV1CustomerProfile, RawError]:
        """Fetch a specific Customer-Profile instance.

        Args:
            sid: The unique string that we created to identify the Customer-Profile resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/v1/CustomerProfiles/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1CustomerProfile],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_customer_profile(
        self,
        *,
        status: CustomerProfileEnumStatusOrStr | None = None,
        friendly_name: str | None = None,
        policy_sid: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCustomerProfileResponse, RawError]:
        """Retrieve a list of all Customer-Profiles for an account.

        Args:
            status: The verification status of the Customer-Profile resource.
            friendly_name: The string that you assigned to describe the resource.
            policy_sid: The unique string of a policy that is associated to the Customer-Profile resource.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/v1/CustomerProfiles"),
            query_params=[
                param[CustomerProfileEnumStatusOrStr | None]("Status", status),
                param[str | None]("FriendlyName", friendly_name),
                param[str | None]("PolicySid", policy_sid),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListCustomerProfileResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_customer_profile(
        self,
        sid: str,
        *,
        status: CustomerProfileEnumStatusOrStr | None = None,
        status_callback: AnyUrl | None = None,
        friendly_name: str | None = None,
        email: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TrusthubV1CustomerProfile, RawError]:
        """Updates a Customer-Profile in an account.

        Args:
            sid: The unique string that we created to identify the Customer-Profile resource.
            status: The verification status of the Customer-Profile resource.
            status_callback: The URL we call to inform your application of status changes.
            friendly_name: The string that you assigned to describe the resource.
            email: The email address that will receive updates when the Customer-Profile resource changes status.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/v1/CustomerProfiles/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            body=form_body(
                [
                    param[CustomerProfileEnumStatusOrStr | None]("Status", status),
                    param[AnyUrl | None]("StatusCallback", status_callback),
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("Email", email),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1CustomerProfile],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
