from __future__ import annotations

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
from ..models.enums.webhook_enum_status import WebhookEnumStatusOrStr
from ..models.enums.webhook_enum_version import WebhookEnumVersionOrStr
from ..models.list_webhook_response import ListWebhookResponse
from ..models.verify_v2_service_webhook import VerifyV2ServiceWebhook
from ..server.server import Server


class VerifyV2Webhook:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VerifyV2WebhookWithRawResponse(client, server, auth)

    def create_webhook(
        self,
        service_sid: str,
        friendly_name: str,
        event_types: list[str],
        webhook_url: str,
        *,
        status: WebhookEnumStatusOrStr | None = None,
        version: WebhookEnumVersionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VerifyV2ServiceWebhook:
        """Create a new Webhook for the Service

        Args:
            service_sid: The unique SID identifier of the Service.
            friendly_name: The string that you assigned to describe the webhook. **This value should not contain PII.**
            event_types: The array of events that this Webhook is subscribed to. Possible event types: ``*,
                factor.deleted, factor.created, factor.verified, challenge.approved, challenge.denied``
            webhook_url: The URL associated with this Webhook.
            status: The webhook status. Default value is ``enabled``. One of: ``enabled`` or ``disabled``
            version: The webhook version. Default value is ``v2`` which includes all the latest fields. Version ``v1``
                is legacy and may be removed in the future.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_webhook(
            service_sid,
            friendly_name,
            event_types,
            webhook_url,
            status=status,
            version=version,
            request_options=request_options,
        ).unwrap()

    def delete_webhook(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a specific Webhook.

        Args:
            service_sid: The unique SID identifier of the Service.
            sid: The Twilio-provided string that uniquely identifies the Webhook resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_webhook(service_sid, sid, request_options=request_options).unwrap()

    def fetch_webhook(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VerifyV2ServiceWebhook:
        """Fetch a specific Webhook.

        Args:
            service_sid: The unique SID identifier of the Service.
            sid: The Twilio-provided string that uniquely identifies the Webhook resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_webhook(service_sid, sid, request_options=request_options).unwrap()

    def list_webhook(
        self,
        service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListWebhookResponse:
        """Retrieve a list of all Webhooks for a Service.

        Args:
            service_sid: The unique SID identifier of the Service.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_webhook(
            service_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    def update_webhook(
        self,
        service_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        event_types: list[str] | None = None,
        webhook_url: str | None = None,
        status: WebhookEnumStatusOrStr | None = None,
        version: WebhookEnumVersionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VerifyV2ServiceWebhook:
        """Send a ``POST`` request.

        Args:
            service_sid: The unique SID identifier of the Service.
            sid: The Twilio-provided string that uniquely identifies the Webhook resource to update.
            friendly_name: The string that you assigned to describe the webhook. **This value should not contain PII.**
            event_types: The array of events that this Webhook is subscribed to. Possible event types: ``*,
                factor.deleted, factor.created, factor.verified, challenge.approved, challenge.denied``
            webhook_url: The URL associated with this Webhook.
            status: The webhook status. Default value is ``enabled``. One of: ``enabled`` or ``disabled``
            version: The webhook version. Default value is ``v2`` which includes all the latest fields. Version ``v1``
                is legacy and may be removed in the future.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_webhook(
            service_sid,
            sid,
            friendly_name=friendly_name,
            event_types=event_types,
            webhook_url=webhook_url,
            status=status,
            version=version,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> VerifyV2WebhookWithRawResponse:
        return self._with_raw_response


class AsyncVerifyV2Webhook:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVerifyV2WebhookWithRawResponse(client, server, auth)

    async def create_webhook(
        self,
        service_sid: str,
        friendly_name: str,
        event_types: list[str],
        webhook_url: str,
        *,
        status: WebhookEnumStatusOrStr | None = None,
        version: WebhookEnumVersionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VerifyV2ServiceWebhook:
        """Create a new Webhook for the Service

        Args:
            service_sid: The unique SID identifier of the Service.
            friendly_name: The string that you assigned to describe the webhook. **This value should not contain PII.**
            event_types: The array of events that this Webhook is subscribed to. Possible event types: ``*,
                factor.deleted, factor.created, factor.verified, challenge.approved, challenge.denied``
            webhook_url: The URL associated with this Webhook.
            status: The webhook status. Default value is ``enabled``. One of: ``enabled`` or ``disabled``
            version: The webhook version. Default value is ``v2`` which includes all the latest fields. Version ``v1``
                is legacy and may be removed in the future.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_webhook(
                service_sid,
                friendly_name,
                event_types,
                webhook_url,
                status=status,
                version=version,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_webhook(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a specific Webhook.

        Args:
            service_sid: The unique SID identifier of the Service.
            sid: The Twilio-provided string that uniquely identifies the Webhook resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_webhook(service_sid, sid, request_options=request_options)
        ).unwrap()

    async def fetch_webhook(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VerifyV2ServiceWebhook:
        """Fetch a specific Webhook.

        Args:
            service_sid: The unique SID identifier of the Service.
            sid: The Twilio-provided string that uniquely identifies the Webhook resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_webhook(service_sid, sid, request_options=request_options)).unwrap()

    async def list_webhook(
        self,
        service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListWebhookResponse:
        """Retrieve a list of all Webhooks for a Service.

        Args:
            service_sid: The unique SID identifier of the Service.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_webhook(
                service_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    async def update_webhook(
        self,
        service_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        event_types: list[str] | None = None,
        webhook_url: str | None = None,
        status: WebhookEnumStatusOrStr | None = None,
        version: WebhookEnumVersionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VerifyV2ServiceWebhook:
        """Send a ``POST`` request.

        Args:
            service_sid: The unique SID identifier of the Service.
            sid: The Twilio-provided string that uniquely identifies the Webhook resource to update.
            friendly_name: The string that you assigned to describe the webhook. **This value should not contain PII.**
            event_types: The array of events that this Webhook is subscribed to. Possible event types: ``*,
                factor.deleted, factor.created, factor.verified, challenge.approved, challenge.denied``
            webhook_url: The URL associated with this Webhook.
            status: The webhook status. Default value is ``enabled``. One of: ``enabled`` or ``disabled``
            version: The webhook version. Default value is ``v2`` which includes all the latest fields. Version ``v1``
                is legacy and may be removed in the future.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_webhook(
                service_sid,
                sid,
                friendly_name=friendly_name,
                event_types=event_types,
                webhook_url=webhook_url,
                status=status,
                version=version,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVerifyV2WebhookWithRawResponse:
        return self._with_raw_response


class VerifyV2WebhookWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_webhook(
        self,
        service_sid: str,
        friendly_name: str,
        event_types: list[str],
        webhook_url: str,
        *,
        status: WebhookEnumStatusOrStr | None = None,
        version: WebhookEnumVersionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VerifyV2ServiceWebhook, RawError]:
        """Create a new Webhook for the Service

        Args:
            service_sid: The unique SID identifier of the Service.
            friendly_name: The string that you assigned to describe the webhook. **This value should not contain PII.**
            event_types: The array of events that this Webhook is subscribed to. Possible event types: ``*,
                factor.deleted, factor.created, factor.verified, challenge.approved, challenge.denied``
            webhook_url: The URL associated with this Webhook.
            status: The webhook status. Default value is ``enabled``. One of: ``enabled`` or ``disabled``
            version: The webhook version. Default value is ``v2`` which includes all the latest fields. Version ``v1``
                is legacy and may be removed in the future.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/Webhooks"),
            path_params=[param[str]("ServiceSid", service_sid)],
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[list[str]]("EventTypes", event_types),
                    param[str]("WebhookUrl", webhook_url),
                    param[WebhookEnumStatusOrStr | None]("Status", status),
                    param[WebhookEnumVersionOrStr | None]("Version", version),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2ServiceWebhook],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_webhook(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Webhook.

        Args:
            service_sid: The unique SID identifier of the Service.
            sid: The Twilio-provided string that uniquely identifies the Webhook resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/Webhooks/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_webhook(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VerifyV2ServiceWebhook, RawError]:
        """Fetch a specific Webhook.

        Args:
            service_sid: The unique SID identifier of the Service.
            sid: The Twilio-provided string that uniquely identifies the Webhook resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/Webhooks/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2ServiceWebhook],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_webhook(
        self,
        service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListWebhookResponse, RawError]:
        """Retrieve a list of all Webhooks for a Service.

        Args:
            service_sid: The unique SID identifier of the Service.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/Webhooks"),
            path_params=[param[str]("ServiceSid", service_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListWebhookResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_webhook(
        self,
        service_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        event_types: list[str] | None = None,
        webhook_url: str | None = None,
        status: WebhookEnumStatusOrStr | None = None,
        version: WebhookEnumVersionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VerifyV2ServiceWebhook, RawError]:
        """Send a ``POST`` request.

        Args:
            service_sid: The unique SID identifier of the Service.
            sid: The Twilio-provided string that uniquely identifies the Webhook resource to update.
            friendly_name: The string that you assigned to describe the webhook. **This value should not contain PII.**
            event_types: The array of events that this Webhook is subscribed to. Possible event types: ``*,
                factor.deleted, factor.created, factor.verified, challenge.approved, challenge.denied``
            webhook_url: The URL associated with this Webhook.
            status: The webhook status. Default value is ``enabled``. One of: ``enabled`` or ``disabled``
            version: The webhook version. Default value is ``v2`` which includes all the latest fields. Version ``v1``
                is legacy and may be removed in the future.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/Webhooks/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[list[str] | None]("EventTypes", event_types),
                    param[str | None]("WebhookUrl", webhook_url),
                    param[WebhookEnumStatusOrStr | None]("Status", status),
                    param[WebhookEnumVersionOrStr | None]("Version", version),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2ServiceWebhook],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncVerifyV2WebhookWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_webhook(
        self,
        service_sid: str,
        friendly_name: str,
        event_types: list[str],
        webhook_url: str,
        *,
        status: WebhookEnumStatusOrStr | None = None,
        version: WebhookEnumVersionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VerifyV2ServiceWebhook, RawError]:
        """Create a new Webhook for the Service

        Args:
            service_sid: The unique SID identifier of the Service.
            friendly_name: The string that you assigned to describe the webhook. **This value should not contain PII.**
            event_types: The array of events that this Webhook is subscribed to. Possible event types: ``*,
                factor.deleted, factor.created, factor.verified, challenge.approved, challenge.denied``
            webhook_url: The URL associated with this Webhook.
            status: The webhook status. Default value is ``enabled``. One of: ``enabled`` or ``disabled``
            version: The webhook version. Default value is ``v2`` which includes all the latest fields. Version ``v1``
                is legacy and may be removed in the future.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/Webhooks"),
            path_params=[param[str]("ServiceSid", service_sid)],
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[list[str]]("EventTypes", event_types),
                    param[str]("WebhookUrl", webhook_url),
                    param[WebhookEnumStatusOrStr | None]("Status", status),
                    param[WebhookEnumVersionOrStr | None]("Version", version),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2ServiceWebhook],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_webhook(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Webhook.

        Args:
            service_sid: The unique SID identifier of the Service.
            sid: The Twilio-provided string that uniquely identifies the Webhook resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/Webhooks/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_webhook(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VerifyV2ServiceWebhook, RawError]:
        """Fetch a specific Webhook.

        Args:
            service_sid: The unique SID identifier of the Service.
            sid: The Twilio-provided string that uniquely identifies the Webhook resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/Webhooks/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2ServiceWebhook],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_webhook(
        self,
        service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListWebhookResponse, RawError]:
        """Retrieve a list of all Webhooks for a Service.

        Args:
            service_sid: The unique SID identifier of the Service.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/Webhooks"),
            path_params=[param[str]("ServiceSid", service_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListWebhookResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_webhook(
        self,
        service_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        event_types: list[str] | None = None,
        webhook_url: str | None = None,
        status: WebhookEnumStatusOrStr | None = None,
        version: WebhookEnumVersionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VerifyV2ServiceWebhook, RawError]:
        """Send a ``POST`` request.

        Args:
            service_sid: The unique SID identifier of the Service.
            sid: The Twilio-provided string that uniquely identifies the Webhook resource to update.
            friendly_name: The string that you assigned to describe the webhook. **This value should not contain PII.**
            event_types: The array of events that this Webhook is subscribed to. Possible event types: ``*,
                factor.deleted, factor.created, factor.verified, challenge.approved, challenge.denied``
            webhook_url: The URL associated with this Webhook.
            status: The webhook status. Default value is ``enabled``. One of: ``enabled`` or ``disabled``
            version: The webhook version. Default value is ``v2`` which includes all the latest fields. Version ``v1``
                is legacy and may be removed in the future.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/Webhooks/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[list[str] | None]("EventTypes", event_types),
                    param[str | None]("WebhookUrl", webhook_url),
                    param[WebhookEnumStatusOrStr | None]("Status", status),
                    param[WebhookEnumVersionOrStr | None]("Version", version),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2ServiceWebhook],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
