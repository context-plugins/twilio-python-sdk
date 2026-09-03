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
from ..models.api_v2010_account_sip_sip_credential_list_sip_credential import (
    ApiV2010AccountSipSipCredentialListSipCredential,
)
from ..models.list_sip_credential_response import ListSipCredentialResponse
from ..server.server import Server


class Api20100401Credential:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401CredentialWithRawResponse(client, server, auth)

    def create_sip_credential(
        self,
        account_sid: str,
        credential_list_sid: str,
        username: str,
        password: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountSipSipCredentialListSipCredential:
        """Create a new credential resource.

        Args:
            account_sid: The unique id of the Account that is responsible for this resource.
            credential_list_sid: The unique id that identifies the credential list to include the created credential.
            username: The username that will be passed when authenticating SIP requests. The username should be sent in
                response to Twilio's challenge of the initial INVITE. It can be up to 32 characters long.
            password: The password that the username will use when authenticating SIP requests. The password must be a
                minimum of 12 characters, contain at least 1 digit, and have mixed case. (eg ``IWasAtSignal2018``)
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_sip_credential(
            account_sid, credential_list_sid, username, password, request_options=request_options
        ).unwrap()

    def delete_sip_credential(
        self,
        account_sid: str,
        credential_list_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Delete a credential resource.

        Args:
            account_sid: The unique id of the Account that is responsible for this resource.
            credential_list_sid: The unique id that identifies the credential list that contains the desired
                credentials.
            sid: The unique id that identifies the resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_sip_credential(
            account_sid, credential_list_sid, sid, request_options=request_options
        ).unwrap()

    def fetch_sip_credential(
        self,
        account_sid: str,
        credential_list_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountSipSipCredentialListSipCredential:
        """Fetch a single credential.

        Args:
            account_sid: The unique id of the Account that is responsible for this resource.
            credential_list_sid: The unique id that identifies the credential list that contains the desired credential.
            sid: The unique id that identifies the resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_sip_credential(
            account_sid, credential_list_sid, sid, request_options=request_options
        ).unwrap()

    def list_sip_credential(
        self,
        account_sid: str,
        credential_list_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSipCredentialResponse:
        """Retrieve a list of credentials.

        Args:
            account_sid: The unique id of the Account that is responsible for this resource.
            credential_list_sid: The unique id that identifies the credential list that contains the desired
                credentials.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_sip_credential(
            account_sid,
            credential_list_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_sip_credential(
        self,
        account_sid: str,
        credential_list_sid: str,
        sid: str,
        *,
        password: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountSipSipCredentialListSipCredential:
        """Update a credential resource.

        Args:
            account_sid: The unique id of the Account that is responsible for this resource.
            credential_list_sid: The unique id that identifies the credential list that includes this credential.
            sid: The unique id that identifies the resource to update.
            password: The password that the username will use when authenticating SIP requests. The password must be a
                minimum of 12 characters, contain at least 1 digit, and have mixed case. (eg ``IWasAtSignal2018``)
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_sip_credential(
            account_sid, credential_list_sid, sid, password=password, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401CredentialWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401Credential:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401CredentialWithRawResponse(client, server, auth)

    async def create_sip_credential(
        self,
        account_sid: str,
        credential_list_sid: str,
        username: str,
        password: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountSipSipCredentialListSipCredential:
        """Create a new credential resource.

        Args:
            account_sid: The unique id of the Account that is responsible for this resource.
            credential_list_sid: The unique id that identifies the credential list to include the created credential.
            username: The username that will be passed when authenticating SIP requests. The username should be sent in
                response to Twilio's challenge of the initial INVITE. It can be up to 32 characters long.
            password: The password that the username will use when authenticating SIP requests. The password must be a
                minimum of 12 characters, contain at least 1 digit, and have mixed case. (eg ``IWasAtSignal2018``)
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_sip_credential(
                account_sid, credential_list_sid, username, password, request_options=request_options
            )
        ).unwrap()

    async def delete_sip_credential(
        self,
        account_sid: str,
        credential_list_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Delete a credential resource.

        Args:
            account_sid: The unique id of the Account that is responsible for this resource.
            credential_list_sid: The unique id that identifies the credential list that contains the desired
                credentials.
            sid: The unique id that identifies the resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_sip_credential(
                account_sid, credential_list_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def fetch_sip_credential(
        self,
        account_sid: str,
        credential_list_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountSipSipCredentialListSipCredential:
        """Fetch a single credential.

        Args:
            account_sid: The unique id of the Account that is responsible for this resource.
            credential_list_sid: The unique id that identifies the credential list that contains the desired credential.
            sid: The unique id that identifies the resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_sip_credential(
                account_sid, credential_list_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def list_sip_credential(
        self,
        account_sid: str,
        credential_list_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSipCredentialResponse:
        """Retrieve a list of credentials.

        Args:
            account_sid: The unique id of the Account that is responsible for this resource.
            credential_list_sid: The unique id that identifies the credential list that contains the desired
                credentials.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_sip_credential(
                account_sid,
                credential_list_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_sip_credential(
        self,
        account_sid: str,
        credential_list_sid: str,
        sid: str,
        *,
        password: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountSipSipCredentialListSipCredential:
        """Update a credential resource.

        Args:
            account_sid: The unique id of the Account that is responsible for this resource.
            credential_list_sid: The unique id that identifies the credential list that includes this credential.
            sid: The unique id that identifies the resource to update.
            password: The password that the username will use when authenticating SIP requests. The password must be a
                minimum of 12 characters, contain at least 1 digit, and have mixed case. (eg ``IWasAtSignal2018``)
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_sip_credential(
                account_sid, credential_list_sid, sid, password=password, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401CredentialWithRawResponse:
        return self._with_raw_response


class Api20100401CredentialWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_sip_credential(
        self,
        account_sid: str,
        credential_list_sid: str,
        username: str,
        password: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountSipSipCredentialListSipCredential, RawError]:
        """Create a new credential resource.

        Args:
            account_sid: The unique id of the Account that is responsible for this resource.
            credential_list_sid: The unique id that identifies the credential list to include the created credential.
            username: The username that will be passed when authenticating SIP requests. The username should be sent in
                response to Twilio's challenge of the initial INVITE. It can be up to 32 characters long.
            password: The password that the username will use when authenticating SIP requests. The password must be a
                minimum of 12 characters, contain at least 1 digit, and have mixed case. (eg ``IWasAtSignal2018``)
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{CredentialListSid}/Credentials.json"
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("CredentialListSid", credential_list_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str]("Username", username), param[str]("Password", password)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountSipSipCredentialListSipCredential],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_sip_credential(
        self,
        account_sid: str,
        credential_list_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Delete a credential resource.

        Args:
            account_sid: The unique id of the Account that is responsible for this resource.
            credential_list_sid: The unique id that identifies the credential list that contains the desired
                credentials.
            sid: The unique id that identifies the resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{CredentialListSid}/Credentials/{Sid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("CredentialListSid", credential_list_sid),
                param[str]("Sid", sid),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_sip_credential(
        self,
        account_sid: str,
        credential_list_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountSipSipCredentialListSipCredential, RawError]:
        """Fetch a single credential.

        Args:
            account_sid: The unique id of the Account that is responsible for this resource.
            credential_list_sid: The unique id that identifies the credential list that contains the desired credential.
            sid: The unique id that identifies the resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{CredentialListSid}/Credentials/{Sid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("CredentialListSid", credential_list_sid),
                param[str]("Sid", sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountSipSipCredentialListSipCredential],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_sip_credential(
        self,
        account_sid: str,
        credential_list_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSipCredentialResponse, RawError]:
        """Retrieve a list of credentials.

        Args:
            account_sid: The unique id of the Account that is responsible for this resource.
            credential_list_sid: The unique id that identifies the credential list that contains the desired
                credentials.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{CredentialListSid}/Credentials.json"
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("CredentialListSid", credential_list_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListSipCredentialResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_sip_credential(
        self,
        account_sid: str,
        credential_list_sid: str,
        sid: str,
        *,
        password: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountSipSipCredentialListSipCredential, RawError]:
        """Update a credential resource.

        Args:
            account_sid: The unique id of the Account that is responsible for this resource.
            credential_list_sid: The unique id that identifies the credential list that includes this credential.
            sid: The unique id that identifies the resource to update.
            password: The password that the username will use when authenticating SIP requests. The password must be a
                minimum of 12 characters, contain at least 1 digit, and have mixed case. (eg ``IWasAtSignal2018``)
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{CredentialListSid}/Credentials/{Sid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("CredentialListSid", credential_list_sid),
                param[str]("Sid", sid),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str | None]("Password", password)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountSipSipCredentialListSipCredential],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401CredentialWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_sip_credential(
        self,
        account_sid: str,
        credential_list_sid: str,
        username: str,
        password: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountSipSipCredentialListSipCredential, RawError]:
        """Create a new credential resource.

        Args:
            account_sid: The unique id of the Account that is responsible for this resource.
            credential_list_sid: The unique id that identifies the credential list to include the created credential.
            username: The username that will be passed when authenticating SIP requests. The username should be sent in
                response to Twilio's challenge of the initial INVITE. It can be up to 32 characters long.
            password: The password that the username will use when authenticating SIP requests. The password must be a
                minimum of 12 characters, contain at least 1 digit, and have mixed case. (eg ``IWasAtSignal2018``)
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{CredentialListSid}/Credentials.json"
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("CredentialListSid", credential_list_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str]("Username", username), param[str]("Password", password)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountSipSipCredentialListSipCredential],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_sip_credential(
        self,
        account_sid: str,
        credential_list_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Delete a credential resource.

        Args:
            account_sid: The unique id of the Account that is responsible for this resource.
            credential_list_sid: The unique id that identifies the credential list that contains the desired
                credentials.
            sid: The unique id that identifies the resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{CredentialListSid}/Credentials/{Sid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("CredentialListSid", credential_list_sid),
                param[str]("Sid", sid),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_sip_credential(
        self,
        account_sid: str,
        credential_list_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountSipSipCredentialListSipCredential, RawError]:
        """Fetch a single credential.

        Args:
            account_sid: The unique id of the Account that is responsible for this resource.
            credential_list_sid: The unique id that identifies the credential list that contains the desired credential.
            sid: The unique id that identifies the resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{CredentialListSid}/Credentials/{Sid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("CredentialListSid", credential_list_sid),
                param[str]("Sid", sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountSipSipCredentialListSipCredential],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_sip_credential(
        self,
        account_sid: str,
        credential_list_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSipCredentialResponse, RawError]:
        """Retrieve a list of credentials.

        Args:
            account_sid: The unique id of the Account that is responsible for this resource.
            credential_list_sid: The unique id that identifies the credential list that contains the desired
                credentials.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{CredentialListSid}/Credentials.json"
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("CredentialListSid", credential_list_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListSipCredentialResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_sip_credential(
        self,
        account_sid: str,
        credential_list_sid: str,
        sid: str,
        *,
        password: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountSipSipCredentialListSipCredential, RawError]:
        """Update a credential resource.

        Args:
            account_sid: The unique id of the Account that is responsible for this resource.
            credential_list_sid: The unique id that identifies the credential list that includes this credential.
            sid: The unique id that identifies the resource to update.
            password: The password that the username will use when authenticating SIP requests. The password must be a
                minimum of 12 characters, contain at least 1 digit, and have mixed case. (eg ``IWasAtSignal2018``)
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{CredentialListSid}/Credentials/{Sid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("CredentialListSid", credential_list_sid),
                param[str]("Sid", sid),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str | None]("Password", password)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountSipSipCredentialListSipCredential],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
