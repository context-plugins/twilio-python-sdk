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
from ..models.conversations_v1_credential import ConversationsV1Credential
from ..models.enums.credential_enum_push_type import CredentialEnumPushTypeOrStr
from ..models.list_credential_response import ListCredentialResponse
from ..server.server import Server


class ConversationsV1CredentialApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ConversationsV1CredentialApiWithRawResponse(client, server, auth)

    def create_credential(
        self,
        type_: CredentialEnumPushTypeOrStr,
        *,
        friendly_name: str | None = None,
        certificate: str | None = None,
        private_key: str | None = None,
        sandbox: bool | None = None,
        api_key: str | None = None,
        secret: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1Credential:
        """Add a new push notification credential to your account

        Args:
            type_: The type of push-notification service the credential is for. Can be: ``fcm``, ``gcm``, or ``apn``.
            friendly_name: A descriptive string that you create to describe the new resource. It can be up to 64
                characters long.
            certificate: [APN only] The URL encoded representation of the certificate. For example, `-----BEGIN
                CERTIFICATE----- MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEF.....A== -----END CERTIFICATE-----`.
            private_key: [APN only] The URL encoded representation of the private key. For example, `-----BEGIN RSA
                PRIVATE KEY----- MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fG... -----END RSA PRIVATE KEY-----`.
            sandbox: [APN only] Whether to send the credential to sandbox APNs. Can be ``true`` to send to sandbox APNs
                or ``false`` to send to production.
            api_key: [GCM only] The API key for the project that was obtained from the Google Developer console for your
                GCM Service application credential.
            secret: [FCM only] The **Server key** of your project from the Firebase console, found under Settings /
                Cloud messaging.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_credential(
            type_,
            friendly_name=friendly_name,
            certificate=certificate,
            private_key=private_key,
            sandbox=sandbox,
            api_key=api_key,
            secret=secret,
            request_options=request_options,
        ).unwrap()

    def delete_credential(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Remove a push notification credential from your account

        Args:
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_credential(sid, request_options=request_options).unwrap()

    def fetch_credential(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1Credential:
        """Fetch a push notification credential from your account

        Args:
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_credential(sid, request_options=request_options).unwrap()

    def list_credential(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCredentialResponse:
        """Retrieve a list of all push notification credentials on your account

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_credential(
            page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    def update_credential(
        self,
        sid: str,
        *,
        type_: CredentialEnumPushTypeOrStr | None = None,
        friendly_name: str | None = None,
        certificate: str | None = None,
        private_key: str | None = None,
        sandbox: bool | None = None,
        api_key: str | None = None,
        secret: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1Credential:
        """Update an existing push notification credential on your account

        Args:
            sid: A 34 character string that uniquely identifies this resource.
            type_: The type of push-notification service the credential is for. Can be: ``fcm``, ``gcm``, or ``apn``.
            friendly_name: A descriptive string that you create to describe the new resource. It can be up to 64
                characters long.
            certificate: [APN only] The URL encoded representation of the certificate. For example, `-----BEGIN
                CERTIFICATE----- MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEF.....A== -----END CERTIFICATE-----`.
            private_key: [APN only] The URL encoded representation of the private key. For example, `-----BEGIN RSA
                PRIVATE KEY----- MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fG... -----END RSA PRIVATE KEY-----`.
            sandbox: [APN only] Whether to send the credential to sandbox APNs. Can be ``true`` to send to sandbox APNs
                or ``false`` to send to production.
            api_key: [GCM only] The API key for the project that was obtained from the Google Developer console for your
                GCM Service application credential.
            secret: [FCM only] The **Server key** of your project from the Firebase console, found under Settings /
                Cloud messaging.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_credential(
            sid,
            type_=type_,
            friendly_name=friendly_name,
            certificate=certificate,
            private_key=private_key,
            sandbox=sandbox,
            api_key=api_key,
            secret=secret,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> ConversationsV1CredentialApiWithRawResponse:
        return self._with_raw_response


class AsyncConversationsV1CredentialApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncConversationsV1CredentialApiWithRawResponse(client, server, auth)

    async def create_credential(
        self,
        type_: CredentialEnumPushTypeOrStr,
        *,
        friendly_name: str | None = None,
        certificate: str | None = None,
        private_key: str | None = None,
        sandbox: bool | None = None,
        api_key: str | None = None,
        secret: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1Credential:
        """Add a new push notification credential to your account

        Args:
            type_: The type of push-notification service the credential is for. Can be: ``fcm``, ``gcm``, or ``apn``.
            friendly_name: A descriptive string that you create to describe the new resource. It can be up to 64
                characters long.
            certificate: [APN only] The URL encoded representation of the certificate. For example, `-----BEGIN
                CERTIFICATE----- MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEF.....A== -----END CERTIFICATE-----`.
            private_key: [APN only] The URL encoded representation of the private key. For example, `-----BEGIN RSA
                PRIVATE KEY----- MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fG... -----END RSA PRIVATE KEY-----`.
            sandbox: [APN only] Whether to send the credential to sandbox APNs. Can be ``true`` to send to sandbox APNs
                or ``false`` to send to production.
            api_key: [GCM only] The API key for the project that was obtained from the Google Developer console for your
                GCM Service application credential.
            secret: [FCM only] The **Server key** of your project from the Firebase console, found under Settings /
                Cloud messaging.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_credential(
                type_,
                friendly_name=friendly_name,
                certificate=certificate,
                private_key=private_key,
                sandbox=sandbox,
                api_key=api_key,
                secret=secret,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_credential(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Remove a push notification credential from your account

        Args:
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_credential(sid, request_options=request_options)).unwrap()

    async def fetch_credential(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1Credential:
        """Fetch a push notification credential from your account

        Args:
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_credential(sid, request_options=request_options)).unwrap()

    async def list_credential(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCredentialResponse:
        """Retrieve a list of all push notification credentials on your account

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_credential(
                page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    async def update_credential(
        self,
        sid: str,
        *,
        type_: CredentialEnumPushTypeOrStr | None = None,
        friendly_name: str | None = None,
        certificate: str | None = None,
        private_key: str | None = None,
        sandbox: bool | None = None,
        api_key: str | None = None,
        secret: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1Credential:
        """Update an existing push notification credential on your account

        Args:
            sid: A 34 character string that uniquely identifies this resource.
            type_: The type of push-notification service the credential is for. Can be: ``fcm``, ``gcm``, or ``apn``.
            friendly_name: A descriptive string that you create to describe the new resource. It can be up to 64
                characters long.
            certificate: [APN only] The URL encoded representation of the certificate. For example, `-----BEGIN
                CERTIFICATE----- MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEF.....A== -----END CERTIFICATE-----`.
            private_key: [APN only] The URL encoded representation of the private key. For example, `-----BEGIN RSA
                PRIVATE KEY----- MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fG... -----END RSA PRIVATE KEY-----`.
            sandbox: [APN only] Whether to send the credential to sandbox APNs. Can be ``true`` to send to sandbox APNs
                or ``false`` to send to production.
            api_key: [GCM only] The API key for the project that was obtained from the Google Developer console for your
                GCM Service application credential.
            secret: [FCM only] The **Server key** of your project from the Firebase console, found under Settings /
                Cloud messaging.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_credential(
                sid,
                type_=type_,
                friendly_name=friendly_name,
                certificate=certificate,
                private_key=private_key,
                sandbox=sandbox,
                api_key=api_key,
                secret=secret,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncConversationsV1CredentialApiWithRawResponse:
        return self._with_raw_response


class ConversationsV1CredentialApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_credential(
        self,
        type_: CredentialEnumPushTypeOrStr,
        *,
        friendly_name: str | None = None,
        certificate: str | None = None,
        private_key: str | None = None,
        sandbox: bool | None = None,
        api_key: str | None = None,
        secret: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1Credential, RawError]:
        """Add a new push notification credential to your account

        Args:
            type_: The type of push-notification service the credential is for. Can be: ``fcm``, ``gcm``, or ``apn``.
            friendly_name: A descriptive string that you create to describe the new resource. It can be up to 64
                characters long.
            certificate: [APN only] The URL encoded representation of the certificate. For example, `-----BEGIN
                CERTIFICATE----- MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEF.....A== -----END CERTIFICATE-----`.
            private_key: [APN only] The URL encoded representation of the private key. For example, `-----BEGIN RSA
                PRIVATE KEY----- MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fG... -----END RSA PRIVATE KEY-----`.
            sandbox: [APN only] Whether to send the credential to sandbox APNs. Can be ``true`` to send to sandbox APNs
                or ``false`` to send to production.
            api_key: [GCM only] The API key for the project that was obtained from the Google Developer console for your
                GCM Service application credential.
            secret: [FCM only] The **Server key** of your project from the Firebase console, found under Settings /
                Cloud messaging.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Credentials"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[CredentialEnumPushTypeOrStr]("Type", type_),
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("Certificate", certificate),
                    param[str | None]("PrivateKey", private_key),
                    param[bool | None]("Sandbox", sandbox),
                    param[str | None]("ApiKey", api_key),
                    param[str | None]("Secret", secret),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1Credential],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_credential(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Remove a push notification credential from your account

        Args:
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7("/v1/Credentials/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_credential(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1Credential, RawError]:
        """Fetch a push notification credential from your account

        Args:
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Credentials/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1Credential],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_credential(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCredentialResponse, RawError]:
        """Retrieve a list of all push notification credentials on your account

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Credentials"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListCredentialResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_credential(
        self,
        sid: str,
        *,
        type_: CredentialEnumPushTypeOrStr | None = None,
        friendly_name: str | None = None,
        certificate: str | None = None,
        private_key: str | None = None,
        sandbox: bool | None = None,
        api_key: str | None = None,
        secret: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1Credential, RawError]:
        """Update an existing push notification credential on your account

        Args:
            sid: A 34 character string that uniquely identifies this resource.
            type_: The type of push-notification service the credential is for. Can be: ``fcm``, ``gcm``, or ``apn``.
            friendly_name: A descriptive string that you create to describe the new resource. It can be up to 64
                characters long.
            certificate: [APN only] The URL encoded representation of the certificate. For example, `-----BEGIN
                CERTIFICATE----- MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEF.....A== -----END CERTIFICATE-----`.
            private_key: [APN only] The URL encoded representation of the private key. For example, `-----BEGIN RSA
                PRIVATE KEY----- MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fG... -----END RSA PRIVATE KEY-----`.
            sandbox: [APN only] Whether to send the credential to sandbox APNs. Can be ``true`` to send to sandbox APNs
                or ``false`` to send to production.
            api_key: [GCM only] The API key for the project that was obtained from the Google Developer console for your
                GCM Service application credential.
            secret: [FCM only] The **Server key** of your project from the Firebase console, found under Settings /
                Cloud messaging.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Credentials/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[CredentialEnumPushTypeOrStr | None]("Type", type_),
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("Certificate", certificate),
                    param[str | None]("PrivateKey", private_key),
                    param[bool | None]("Sandbox", sandbox),
                    param[str | None]("ApiKey", api_key),
                    param[str | None]("Secret", secret),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1Credential],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncConversationsV1CredentialApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_credential(
        self,
        type_: CredentialEnumPushTypeOrStr,
        *,
        friendly_name: str | None = None,
        certificate: str | None = None,
        private_key: str | None = None,
        sandbox: bool | None = None,
        api_key: str | None = None,
        secret: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1Credential, RawError]:
        """Add a new push notification credential to your account

        Args:
            type_: The type of push-notification service the credential is for. Can be: ``fcm``, ``gcm``, or ``apn``.
            friendly_name: A descriptive string that you create to describe the new resource. It can be up to 64
                characters long.
            certificate: [APN only] The URL encoded representation of the certificate. For example, `-----BEGIN
                CERTIFICATE----- MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEF.....A== -----END CERTIFICATE-----`.
            private_key: [APN only] The URL encoded representation of the private key. For example, `-----BEGIN RSA
                PRIVATE KEY----- MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fG... -----END RSA PRIVATE KEY-----`.
            sandbox: [APN only] Whether to send the credential to sandbox APNs. Can be ``true`` to send to sandbox APNs
                or ``false`` to send to production.
            api_key: [GCM only] The API key for the project that was obtained from the Google Developer console for your
                GCM Service application credential.
            secret: [FCM only] The **Server key** of your project from the Firebase console, found under Settings /
                Cloud messaging.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Credentials"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[CredentialEnumPushTypeOrStr]("Type", type_),
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("Certificate", certificate),
                    param[str | None]("PrivateKey", private_key),
                    param[bool | None]("Sandbox", sandbox),
                    param[str | None]("ApiKey", api_key),
                    param[str | None]("Secret", secret),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1Credential],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_credential(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Remove a push notification credential from your account

        Args:
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7("/v1/Credentials/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_credential(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1Credential, RawError]:
        """Fetch a push notification credential from your account

        Args:
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Credentials/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1Credential],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_credential(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCredentialResponse, RawError]:
        """Retrieve a list of all push notification credentials on your account

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Credentials"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListCredentialResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_credential(
        self,
        sid: str,
        *,
        type_: CredentialEnumPushTypeOrStr | None = None,
        friendly_name: str | None = None,
        certificate: str | None = None,
        private_key: str | None = None,
        sandbox: bool | None = None,
        api_key: str | None = None,
        secret: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1Credential, RawError]:
        """Update an existing push notification credential on your account

        Args:
            sid: A 34 character string that uniquely identifies this resource.
            type_: The type of push-notification service the credential is for. Can be: ``fcm``, ``gcm``, or ``apn``.
            friendly_name: A descriptive string that you create to describe the new resource. It can be up to 64
                characters long.
            certificate: [APN only] The URL encoded representation of the certificate. For example, `-----BEGIN
                CERTIFICATE----- MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEF.....A== -----END CERTIFICATE-----`.
            private_key: [APN only] The URL encoded representation of the private key. For example, `-----BEGIN RSA
                PRIVATE KEY----- MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fG... -----END RSA PRIVATE KEY-----`.
            sandbox: [APN only] Whether to send the credential to sandbox APNs. Can be ``true`` to send to sandbox APNs
                or ``false`` to send to production.
            api_key: [GCM only] The API key for the project that was obtained from the Google Developer console for your
                GCM Service application credential.
            secret: [FCM only] The **Server key** of your project from the Firebase console, found under Settings /
                Cloud messaging.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Credentials/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[CredentialEnumPushTypeOrStr | None]("Type", type_),
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("Certificate", certificate),
                    param[str | None]("PrivateKey", private_key),
                    param[bool | None]("Sandbox", sandbox),
                    param[str | None]("ApiKey", api_key),
                    param[str | None]("Secret", secret),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1Credential],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
