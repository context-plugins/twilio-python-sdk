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
from ..models.api_v2010_account_incoming_phone_number_incoming_phone_number_assigned_add_on import (
    ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn,
)
from ..models.list_incoming_phone_number_assigned_add_on_response import ListIncomingPhoneNumberAssignedAddOnResponse
from ..server.server import Server


class Api20100401AssignedAddOn:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401AssignedAddOnWithRawResponse(client, server, auth)

    def create_incoming_phone_number_assigned_add_on(
        self,
        account_sid: str,
        resource_sid: str,
        installed_add_on_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn:
        """Assign an Add-on installation to the Number specified.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            resource_sid: The SID of the Phone Number to assign the Add-on.
            installed_add_on_sid: The SID that identifies the Add-on installation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_incoming_phone_number_assigned_add_on(
            account_sid, resource_sid, installed_add_on_sid, request_options=request_options
        ).unwrap()

    def delete_incoming_phone_number_assigned_add_on(
        self, account_sid: str, resource_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Remove the assignment of an Add-on installation from the Number specified.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                resources to delete.
            resource_sid: The SID of the Phone Number to which the Add-on is assigned.
            sid: The Twilio-provided string that uniquely identifies the resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_incoming_phone_number_assigned_add_on(
            account_sid, resource_sid, sid, request_options=request_options
        ).unwrap()

    def fetch_incoming_phone_number_assigned_add_on(
        self, account_sid: str, resource_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn:
        """Fetch an instance of an Add-on installation currently assigned to this Number.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                resource to fetch.
            resource_sid: The SID of the Phone Number to which the Add-on is assigned.
            sid: The Twilio-provided string that uniquely identifies the resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_incoming_phone_number_assigned_add_on(
            account_sid, resource_sid, sid, request_options=request_options
        ).unwrap()

    def list_incoming_phone_number_assigned_add_on(
        self,
        account_sid: str,
        resource_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListIncomingPhoneNumberAssignedAddOnResponse:
        """Retrieve a list of Add-on installations currently assigned to this Number.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                resources to read.
            resource_sid: The SID of the Phone Number to which the Add-on is assigned.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_incoming_phone_number_assigned_add_on(
            account_sid,
            resource_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401AssignedAddOnWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401AssignedAddOn:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401AssignedAddOnWithRawResponse(client, server, auth)

    async def create_incoming_phone_number_assigned_add_on(
        self,
        account_sid: str,
        resource_sid: str,
        installed_add_on_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn:
        """Assign an Add-on installation to the Number specified.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            resource_sid: The SID of the Phone Number to assign the Add-on.
            installed_add_on_sid: The SID that identifies the Add-on installation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_incoming_phone_number_assigned_add_on(
                account_sid, resource_sid, installed_add_on_sid, request_options=request_options
            )
        ).unwrap()

    async def delete_incoming_phone_number_assigned_add_on(
        self, account_sid: str, resource_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Remove the assignment of an Add-on installation from the Number specified.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                resources to delete.
            resource_sid: The SID of the Phone Number to which the Add-on is assigned.
            sid: The Twilio-provided string that uniquely identifies the resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_incoming_phone_number_assigned_add_on(
                account_sid, resource_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def fetch_incoming_phone_number_assigned_add_on(
        self, account_sid: str, resource_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn:
        """Fetch an instance of an Add-on installation currently assigned to this Number.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                resource to fetch.
            resource_sid: The SID of the Phone Number to which the Add-on is assigned.
            sid: The Twilio-provided string that uniquely identifies the resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_incoming_phone_number_assigned_add_on(
                account_sid, resource_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def list_incoming_phone_number_assigned_add_on(
        self,
        account_sid: str,
        resource_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListIncomingPhoneNumberAssignedAddOnResponse:
        """Retrieve a list of Add-on installations currently assigned to this Number.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                resources to read.
            resource_sid: The SID of the Phone Number to which the Add-on is assigned.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_incoming_phone_number_assigned_add_on(
                account_sid,
                resource_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401AssignedAddOnWithRawResponse:
        return self._with_raw_response


class Api20100401AssignedAddOnWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_incoming_phone_number_assigned_add_on(
        self,
        account_sid: str,
        resource_sid: str,
        installed_add_on_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn, RawError]:
        """Assign an Add-on installation to the Number specified.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            resource_sid: The SID of the Phone Number to assign the Add-on.
            installed_add_on_sid: The SID that identifies the Add-on installation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns.json"
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("ResourceSid", resource_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str]("InstalledAddOnSid", installed_add_on_sid)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_incoming_phone_number_assigned_add_on(
        self, account_sid: str, resource_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Remove the assignment of an Add-on installation from the Number specified.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                resources to delete.
            resource_sid: The SID of the Phone Number to which the Add-on is assigned.
            sid: The Twilio-provided string that uniquely identifies the resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns/{Sid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid), param[str]("ResourceSid", resource_sid), param[str]("Sid", sid)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_incoming_phone_number_assigned_add_on(
        self, account_sid: str, resource_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn, RawError]:
        """Fetch an instance of an Add-on installation currently assigned to this Number.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                resource to fetch.
            resource_sid: The SID of the Phone Number to which the Add-on is assigned.
            sid: The Twilio-provided string that uniquely identifies the resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns/{Sid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid), param[str]("ResourceSid", resource_sid), param[str]("Sid", sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_incoming_phone_number_assigned_add_on(
        self,
        account_sid: str,
        resource_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListIncomingPhoneNumberAssignedAddOnResponse, RawError]:
        """Retrieve a list of Add-on installations currently assigned to this Number.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                resources to read.
            resource_sid: The SID of the Phone Number to which the Add-on is assigned.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns.json"
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("ResourceSid", resource_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListIncomingPhoneNumberAssignedAddOnResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401AssignedAddOnWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_incoming_phone_number_assigned_add_on(
        self,
        account_sid: str,
        resource_sid: str,
        installed_add_on_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn, RawError]:
        """Assign an Add-on installation to the Number specified.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            resource_sid: The SID of the Phone Number to assign the Add-on.
            installed_add_on_sid: The SID that identifies the Add-on installation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns.json"
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("ResourceSid", resource_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str]("InstalledAddOnSid", installed_add_on_sid)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_incoming_phone_number_assigned_add_on(
        self, account_sid: str, resource_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Remove the assignment of an Add-on installation from the Number specified.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                resources to delete.
            resource_sid: The SID of the Phone Number to which the Add-on is assigned.
            sid: The Twilio-provided string that uniquely identifies the resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns/{Sid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid), param[str]("ResourceSid", resource_sid), param[str]("Sid", sid)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_incoming_phone_number_assigned_add_on(
        self, account_sid: str, resource_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn, RawError]:
        """Fetch an instance of an Add-on installation currently assigned to this Number.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                resource to fetch.
            resource_sid: The SID of the Phone Number to which the Add-on is assigned.
            sid: The Twilio-provided string that uniquely identifies the resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns/{Sid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid), param[str]("ResourceSid", resource_sid), param[str]("Sid", sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_incoming_phone_number_assigned_add_on(
        self,
        account_sid: str,
        resource_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListIncomingPhoneNumberAssignedAddOnResponse, RawError]:
        """Retrieve a list of Add-on installations currently assigned to this Number.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                resources to read.
            resource_sid: The SID of the Phone Number to which the Add-on is assigned.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns.json"
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("ResourceSid", resource_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListIncomingPhoneNumberAssignedAddOnResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
