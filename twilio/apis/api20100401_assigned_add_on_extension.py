from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.incoming_phone_number_assigned_add_on_extension import IncomingPhoneNumberAssignedAddOnExtension
from ..models.list_incoming_phone_number_assigned_add_on_extension_response import (
    ListIncomingPhoneNumberAssignedAddOnExtensionResponse,
)
from ..server.server import Server


class Api20100401AssignedAddOnExtension:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401AssignedAddOnExtensionWithRawResponse(client, server, auth)

    def fetch_incoming_phone_number_assigned_add_on_extension(
        self,
        account_sid: str,
        resource_sid: str,
        assigned_add_on_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> IncomingPhoneNumberAssignedAddOnExtension:
        """Fetch an instance of an Extension for the Assigned Add-on.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                resource to fetch.
            resource_sid: The SID of the Phone Number to which the Add-on is assigned.
            assigned_add_on_sid: The SID that uniquely identifies the assigned Add-on installation.
            sid: The Twilio-provided string that uniquely identifies the resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_incoming_phone_number_assigned_add_on_extension(
            account_sid, resource_sid, assigned_add_on_sid, sid, request_options=request_options
        ).unwrap()

    def list_incoming_phone_number_assigned_add_on_extension(
        self,
        account_sid: str,
        resource_sid: str,
        assigned_add_on_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListIncomingPhoneNumberAssignedAddOnExtensionResponse:
        """Retrieve a list of Extensions for the Assigned Add-on.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                resources to read.
            resource_sid: The SID of the Phone Number to which the Add-on is assigned.
            assigned_add_on_sid: The SID that uniquely identifies the assigned Add-on installation.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_incoming_phone_number_assigned_add_on_extension(
            account_sid,
            resource_sid,
            assigned_add_on_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401AssignedAddOnExtensionWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401AssignedAddOnExtension:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401AssignedAddOnExtensionWithRawResponse(client, server, auth)

    async def fetch_incoming_phone_number_assigned_add_on_extension(
        self,
        account_sid: str,
        resource_sid: str,
        assigned_add_on_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> IncomingPhoneNumberAssignedAddOnExtension:
        """Fetch an instance of an Extension for the Assigned Add-on.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                resource to fetch.
            resource_sid: The SID of the Phone Number to which the Add-on is assigned.
            assigned_add_on_sid: The SID that uniquely identifies the assigned Add-on installation.
            sid: The Twilio-provided string that uniquely identifies the resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_incoming_phone_number_assigned_add_on_extension(
                account_sid, resource_sid, assigned_add_on_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def list_incoming_phone_number_assigned_add_on_extension(
        self,
        account_sid: str,
        resource_sid: str,
        assigned_add_on_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListIncomingPhoneNumberAssignedAddOnExtensionResponse:
        """Retrieve a list of Extensions for the Assigned Add-on.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                resources to read.
            resource_sid: The SID of the Phone Number to which the Add-on is assigned.
            assigned_add_on_sid: The SID that uniquely identifies the assigned Add-on installation.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_incoming_phone_number_assigned_add_on_extension(
                account_sid,
                resource_sid,
                assigned_add_on_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401AssignedAddOnExtensionWithRawResponse:
        return self._with_raw_response


class Api20100401AssignedAddOnExtensionWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_incoming_phone_number_assigned_add_on_extension(
        self,
        account_sid: str,
        resource_sid: str,
        assigned_add_on_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[IncomingPhoneNumberAssignedAddOnExtension, RawError]:
        """Fetch an instance of an Extension for the Assigned Add-on.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                resource to fetch.
            resource_sid: The SID of the Phone Number to which the Add-on is assigned.
            assigned_add_on_sid: The SID that uniquely identifies the assigned Add-on installation.
            sid: The Twilio-provided string that uniquely identifies the resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns/{AssignedAddOnSid}/Extensions/{Sid}.json",
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("ResourceSid", resource_sid),
                param[str]("AssignedAddOnSid", assigned_add_on_sid),
                param[str]("Sid", sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[IncomingPhoneNumberAssignedAddOnExtension],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_incoming_phone_number_assigned_add_on_extension(
        self,
        account_sid: str,
        resource_sid: str,
        assigned_add_on_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListIncomingPhoneNumberAssignedAddOnExtensionResponse, RawError]:
        """Retrieve a list of Extensions for the Assigned Add-on.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                resources to read.
            resource_sid: The SID of the Phone Number to which the Add-on is assigned.
            assigned_add_on_sid: The SID that uniquely identifies the assigned Add-on installation.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns/{AssignedAddOnSid}/Extensions.json",
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("ResourceSid", resource_sid),
                param[str]("AssignedAddOnSid", assigned_add_on_sid),
            ],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListIncomingPhoneNumberAssignedAddOnExtensionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401AssignedAddOnExtensionWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def fetch_incoming_phone_number_assigned_add_on_extension(
        self,
        account_sid: str,
        resource_sid: str,
        assigned_add_on_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[IncomingPhoneNumberAssignedAddOnExtension, RawError]:
        """Fetch an instance of an Extension for the Assigned Add-on.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                resource to fetch.
            resource_sid: The SID of the Phone Number to which the Add-on is assigned.
            assigned_add_on_sid: The SID that uniquely identifies the assigned Add-on installation.
            sid: The Twilio-provided string that uniquely identifies the resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns/{AssignedAddOnSid}/Extensions/{Sid}.json",
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("ResourceSid", resource_sid),
                param[str]("AssignedAddOnSid", assigned_add_on_sid),
                param[str]("Sid", sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[IncomingPhoneNumberAssignedAddOnExtension],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_incoming_phone_number_assigned_add_on_extension(
        self,
        account_sid: str,
        resource_sid: str,
        assigned_add_on_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListIncomingPhoneNumberAssignedAddOnExtensionResponse, RawError]:
        """Retrieve a list of Extensions for the Assigned Add-on.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                resources to read.
            resource_sid: The SID of the Phone Number to which the Add-on is assigned.
            assigned_add_on_sid: The SID that uniquely identifies the assigned Add-on installation.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns/{AssignedAddOnSid}/Extensions.json",
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("ResourceSid", resource_sid),
                param[str]("AssignedAddOnSid", assigned_add_on_sid),
            ],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListIncomingPhoneNumberAssignedAddOnExtensionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
