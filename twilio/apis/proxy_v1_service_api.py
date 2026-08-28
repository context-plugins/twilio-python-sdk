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
from ..models.enums.service_enum_geo_match_level import ServiceEnumGeoMatchLevelOrStr
from ..models.enums.service_enum_number_selection_behavior import ServiceEnumNumberSelectionBehaviorOrStr
from ..models.list_service_response3 import ListServiceResponse3
from ..models.proxy_v1_service import ProxyV1Service
from ..server.server import Server


class ProxyV1ServiceApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ProxyV1ServiceApiWithRawResponse(client, server, auth)

    def create_service4(
        self,
        unique_name: str,
        *,
        default_ttl: int | None = None,
        callback_url: str | None = None,
        geo_match_level: ServiceEnumGeoMatchLevelOrStr | None = None,
        number_selection_behavior: ServiceEnumNumberSelectionBehaviorOrStr | None = None,
        intercept_callback_url: str | None = None,
        out_of_session_callback_url: str | None = None,
        chat_instance_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProxyV1Service:
        """Create a new Service for Twilio Proxy

        Args:
            unique_name: An application-defined string that uniquely identifies the resource. This value must be 191
                characters or fewer in length and be unique. **This value should not have PII.**
            default_ttl: The default ``ttl`` value to set for Sessions created in the Service. The TTL (time to live) is
                measured in seconds after the Session's last create or last Interaction. The default value of ``0``
                indicates an unlimited Session length. You can override a Session's default TTL value by setting its
                ``ttl`` value.
            callback_url: The URL we should call when the interaction status changes.
            geo_match_level: Where a proxy number must be located relative to the participant identifier. Can be:
                ``country``, ``area-code``, or ``extended-area-code``. The default value is ``country`` and more
                specific areas than ``country`` are only available in North America.
            number_selection_behavior: The preference for Proxy Number selection in the Service instance. Can be:
                ``prefer-sticky`` or ``avoid-sticky``. ``prefer-sticky`` means that we will try and select the same
                Proxy Number for a given participant if they have previous `Sessions
                <https://www.twilio.com/docs/proxy/api/session>`__, but we will not fail if that Proxy Number cannot be
                used. ``avoid-sticky`` means that we will try to use different Proxy Numbers as long as that is possible
                within a given pool rather than try and use a previously assigned number.
            intercept_callback_url: The URL we call on each interaction. If we receive a 403 status, we block the
                interaction; otherwise the interaction continues.
            out_of_session_callback_url: The URL we should call when an inbound call or SMS action occurs on a closed or
                non-existent Session. If your server (or a Twilio `function
                <https://www.twilio.com/en-us/serverless/functions>`__) responds with valid `TwiML
                <https://www.twilio.com/docs/voice/twiml>`__, we will process it. This means it is possible, for
                example, to play a message for a call, send an automated text message response, or redirect a call to
                another Phone Number. See `Out-of-Session Callback Response Guide
                <https://www.twilio.com/docs/proxy/out-session-callback-response-guide>`__ for more information.
            chat_instance_sid: The SID of the Chat Service Instance managed by Proxy Service. The Chat Service enables
                Proxy to forward SMS and channel messages to this chat instance. This is a one-to-one relationship.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_service4(
            unique_name,
            default_ttl=default_ttl,
            callback_url=callback_url,
            geo_match_level=geo_match_level,
            number_selection_behavior=number_selection_behavior,
            intercept_callback_url=intercept_callback_url,
            out_of_session_callback_url=out_of_session_callback_url,
            chat_instance_sid=chat_instance_sid,
            request_options=request_options,
        ).unwrap()

    def delete_service4(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Delete a specific Service.

        Args:
            sid: The Twilio-provided string that uniquely identifies the Service resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_service4(sid, request_options=request_options).unwrap()

    def fetch_service4(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> ProxyV1Service:
        """Fetch a specific Service.

        Args:
            sid: The Twilio-provided string that uniquely identifies the Service resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_service4(sid, request_options=request_options).unwrap()

    def list_service4(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListServiceResponse3:
        """Retrieve a list of all Services for Twilio Proxy. A maximum of 100 records will be returned per page.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_service4(
            page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    def update_service3(
        self,
        sid: str,
        *,
        unique_name: str | None = None,
        default_ttl: int | None = None,
        callback_url: str | None = None,
        geo_match_level: ServiceEnumGeoMatchLevelOrStr | None = None,
        number_selection_behavior: ServiceEnumNumberSelectionBehaviorOrStr | None = None,
        intercept_callback_url: str | None = None,
        out_of_session_callback_url: str | None = None,
        chat_instance_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProxyV1Service:
        """Update a specific Service.

        Args:
            sid: The Twilio-provided string that uniquely identifies the Service resource to update.
            unique_name: An application-defined string that uniquely identifies the resource. This value must be 191
                characters or fewer in length and be unique. **This value should not have PII.**
            default_ttl: The default ``ttl`` value to set for Sessions created in the Service. The TTL (time to live) is
                measured in seconds after the Session's last create or last Interaction. The default value of ``0``
                indicates an unlimited Session length. You can override a Session's default TTL value by setting its
                ``ttl`` value.
            callback_url: The URL we should call when the interaction status changes.
            geo_match_level: Where a proxy number must be located relative to the participant identifier. Can be:
                ``country``, ``area-code``, or ``extended-area-code``. The default value is ``country`` and more
                specific areas than ``country`` are only available in North America.
            number_selection_behavior: The preference for Proxy Number selection in the Service instance. Can be:
                ``prefer-sticky`` or ``avoid-sticky``. ``prefer-sticky`` means that we will try and select the same
                Proxy Number for a given participant if they have previous `Sessions
                <https://www.twilio.com/docs/proxy/api/session>`__, but we will not fail if that Proxy Number cannot be
                used. ``avoid-sticky`` means that we will try to use different Proxy Numbers as long as that is possible
                within a given pool rather than try and use a previously assigned number.
            intercept_callback_url: The URL we call on each interaction. If we receive a 403 status, we block the
                interaction; otherwise the interaction continues.
            out_of_session_callback_url: The URL we should call when an inbound call or SMS action occurs on a closed or
                non-existent Session. If your server (or a Twilio `function
                <https://www.twilio.com/en-us/serverless/functions>`__) responds with valid `TwiML
                <https://www.twilio.com/docs/voice/twiml>`__, we will process it. This means it is possible, for
                example, to play a message for a call, send an automated text message response, or redirect a call to
                another Phone Number. See `Out-of-Session Callback Response Guide
                <https://www.twilio.com/docs/proxy/out-session-callback-response-guide>`__ for more information.
            chat_instance_sid: The SID of the Chat Service Instance managed by Proxy Service. The Chat Service enables
                Proxy to forward SMS and channel messages to this chat instance. This is a one-to-one relationship.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_service3(
            sid,
            unique_name=unique_name,
            default_ttl=default_ttl,
            callback_url=callback_url,
            geo_match_level=geo_match_level,
            number_selection_behavior=number_selection_behavior,
            intercept_callback_url=intercept_callback_url,
            out_of_session_callback_url=out_of_session_callback_url,
            chat_instance_sid=chat_instance_sid,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> ProxyV1ServiceApiWithRawResponse:
        return self._with_raw_response


class AsyncProxyV1ServiceApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncProxyV1ServiceApiWithRawResponse(client, server, auth)

    async def create_service4(
        self,
        unique_name: str,
        *,
        default_ttl: int | None = None,
        callback_url: str | None = None,
        geo_match_level: ServiceEnumGeoMatchLevelOrStr | None = None,
        number_selection_behavior: ServiceEnumNumberSelectionBehaviorOrStr | None = None,
        intercept_callback_url: str | None = None,
        out_of_session_callback_url: str | None = None,
        chat_instance_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProxyV1Service:
        """Create a new Service for Twilio Proxy

        Args:
            unique_name: An application-defined string that uniquely identifies the resource. This value must be 191
                characters or fewer in length and be unique. **This value should not have PII.**
            default_ttl: The default ``ttl`` value to set for Sessions created in the Service. The TTL (time to live) is
                measured in seconds after the Session's last create or last Interaction. The default value of ``0``
                indicates an unlimited Session length. You can override a Session's default TTL value by setting its
                ``ttl`` value.
            callback_url: The URL we should call when the interaction status changes.
            geo_match_level: Where a proxy number must be located relative to the participant identifier. Can be:
                ``country``, ``area-code``, or ``extended-area-code``. The default value is ``country`` and more
                specific areas than ``country`` are only available in North America.
            number_selection_behavior: The preference for Proxy Number selection in the Service instance. Can be:
                ``prefer-sticky`` or ``avoid-sticky``. ``prefer-sticky`` means that we will try and select the same
                Proxy Number for a given participant if they have previous `Sessions
                <https://www.twilio.com/docs/proxy/api/session>`__, but we will not fail if that Proxy Number cannot be
                used. ``avoid-sticky`` means that we will try to use different Proxy Numbers as long as that is possible
                within a given pool rather than try and use a previously assigned number.
            intercept_callback_url: The URL we call on each interaction. If we receive a 403 status, we block the
                interaction; otherwise the interaction continues.
            out_of_session_callback_url: The URL we should call when an inbound call or SMS action occurs on a closed or
                non-existent Session. If your server (or a Twilio `function
                <https://www.twilio.com/en-us/serverless/functions>`__) responds with valid `TwiML
                <https://www.twilio.com/docs/voice/twiml>`__, we will process it. This means it is possible, for
                example, to play a message for a call, send an automated text message response, or redirect a call to
                another Phone Number. See `Out-of-Session Callback Response Guide
                <https://www.twilio.com/docs/proxy/out-session-callback-response-guide>`__ for more information.
            chat_instance_sid: The SID of the Chat Service Instance managed by Proxy Service. The Chat Service enables
                Proxy to forward SMS and channel messages to this chat instance. This is a one-to-one relationship.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_service4(
                unique_name,
                default_ttl=default_ttl,
                callback_url=callback_url,
                geo_match_level=geo_match_level,
                number_selection_behavior=number_selection_behavior,
                intercept_callback_url=intercept_callback_url,
                out_of_session_callback_url=out_of_session_callback_url,
                chat_instance_sid=chat_instance_sid,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_service4(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Delete a specific Service.

        Args:
            sid: The Twilio-provided string that uniquely identifies the Service resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_service4(sid, request_options=request_options)).unwrap()

    async def fetch_service4(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> ProxyV1Service:
        """Fetch a specific Service.

        Args:
            sid: The Twilio-provided string that uniquely identifies the Service resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_service4(sid, request_options=request_options)).unwrap()

    async def list_service4(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListServiceResponse3:
        """Retrieve a list of all Services for Twilio Proxy. A maximum of 100 records will be returned per page.

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
            await self._with_raw_response.list_service4(
                page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    async def update_service3(
        self,
        sid: str,
        *,
        unique_name: str | None = None,
        default_ttl: int | None = None,
        callback_url: str | None = None,
        geo_match_level: ServiceEnumGeoMatchLevelOrStr | None = None,
        number_selection_behavior: ServiceEnumNumberSelectionBehaviorOrStr | None = None,
        intercept_callback_url: str | None = None,
        out_of_session_callback_url: str | None = None,
        chat_instance_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProxyV1Service:
        """Update a specific Service.

        Args:
            sid: The Twilio-provided string that uniquely identifies the Service resource to update.
            unique_name: An application-defined string that uniquely identifies the resource. This value must be 191
                characters or fewer in length and be unique. **This value should not have PII.**
            default_ttl: The default ``ttl`` value to set for Sessions created in the Service. The TTL (time to live) is
                measured in seconds after the Session's last create or last Interaction. The default value of ``0``
                indicates an unlimited Session length. You can override a Session's default TTL value by setting its
                ``ttl`` value.
            callback_url: The URL we should call when the interaction status changes.
            geo_match_level: Where a proxy number must be located relative to the participant identifier. Can be:
                ``country``, ``area-code``, or ``extended-area-code``. The default value is ``country`` and more
                specific areas than ``country`` are only available in North America.
            number_selection_behavior: The preference for Proxy Number selection in the Service instance. Can be:
                ``prefer-sticky`` or ``avoid-sticky``. ``prefer-sticky`` means that we will try and select the same
                Proxy Number for a given participant if they have previous `Sessions
                <https://www.twilio.com/docs/proxy/api/session>`__, but we will not fail if that Proxy Number cannot be
                used. ``avoid-sticky`` means that we will try to use different Proxy Numbers as long as that is possible
                within a given pool rather than try and use a previously assigned number.
            intercept_callback_url: The URL we call on each interaction. If we receive a 403 status, we block the
                interaction; otherwise the interaction continues.
            out_of_session_callback_url: The URL we should call when an inbound call or SMS action occurs on a closed or
                non-existent Session. If your server (or a Twilio `function
                <https://www.twilio.com/en-us/serverless/functions>`__) responds with valid `TwiML
                <https://www.twilio.com/docs/voice/twiml>`__, we will process it. This means it is possible, for
                example, to play a message for a call, send an automated text message response, or redirect a call to
                another Phone Number. See `Out-of-Session Callback Response Guide
                <https://www.twilio.com/docs/proxy/out-session-callback-response-guide>`__ for more information.
            chat_instance_sid: The SID of the Chat Service Instance managed by Proxy Service. The Chat Service enables
                Proxy to forward SMS and channel messages to this chat instance. This is a one-to-one relationship.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_service3(
                sid,
                unique_name=unique_name,
                default_ttl=default_ttl,
                callback_url=callback_url,
                geo_match_level=geo_match_level,
                number_selection_behavior=number_selection_behavior,
                intercept_callback_url=intercept_callback_url,
                out_of_session_callback_url=out_of_session_callback_url,
                chat_instance_sid=chat_instance_sid,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncProxyV1ServiceApiWithRawResponse:
        return self._with_raw_response


class ProxyV1ServiceApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_service4(
        self,
        unique_name: str,
        *,
        default_ttl: int | None = None,
        callback_url: str | None = None,
        geo_match_level: ServiceEnumGeoMatchLevelOrStr | None = None,
        number_selection_behavior: ServiceEnumNumberSelectionBehaviorOrStr | None = None,
        intercept_callback_url: str | None = None,
        out_of_session_callback_url: str | None = None,
        chat_instance_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProxyV1Service, RawError]:
        """Create a new Service for Twilio Proxy

        Args:
            unique_name: An application-defined string that uniquely identifies the resource. This value must be 191
                characters or fewer in length and be unique. **This value should not have PII.**
            default_ttl: The default ``ttl`` value to set for Sessions created in the Service. The TTL (time to live) is
                measured in seconds after the Session's last create or last Interaction. The default value of ``0``
                indicates an unlimited Session length. You can override a Session's default TTL value by setting its
                ``ttl`` value.
            callback_url: The URL we should call when the interaction status changes.
            geo_match_level: Where a proxy number must be located relative to the participant identifier. Can be:
                ``country``, ``area-code``, or ``extended-area-code``. The default value is ``country`` and more
                specific areas than ``country`` are only available in North America.
            number_selection_behavior: The preference for Proxy Number selection in the Service instance. Can be:
                ``prefer-sticky`` or ``avoid-sticky``. ``prefer-sticky`` means that we will try and select the same
                Proxy Number for a given participant if they have previous `Sessions
                <https://www.twilio.com/docs/proxy/api/session>`__, but we will not fail if that Proxy Number cannot be
                used. ``avoid-sticky`` means that we will try to use different Proxy Numbers as long as that is possible
                within a given pool rather than try and use a previously assigned number.
            intercept_callback_url: The URL we call on each interaction. If we receive a 403 status, we block the
                interaction; otherwise the interaction continues.
            out_of_session_callback_url: The URL we should call when an inbound call or SMS action occurs on a closed or
                non-existent Session. If your server (or a Twilio `function
                <https://www.twilio.com/en-us/serverless/functions>`__) responds with valid `TwiML
                <https://www.twilio.com/docs/voice/twiml>`__, we will process it. This means it is possible, for
                example, to play a message for a call, send an automated text message response, or redirect a call to
                another Phone Number. See `Out-of-Session Callback Response Guide
                <https://www.twilio.com/docs/proxy/out-session-callback-response-guide>`__ for more information.
            chat_instance_sid: The SID of the Chat Service Instance managed by Proxy Service. The Chat Service enables
                Proxy to forward SMS and channel messages to this chat instance. This is a one-to-one relationship.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/v1/Services"),
            body=form_body(
                [
                    param[str]("UniqueName", unique_name),
                    param[int | None]("DefaultTtl", default_ttl),
                    param[str | None]("CallbackUrl", callback_url),
                    param[ServiceEnumGeoMatchLevelOrStr | None]("GeoMatchLevel", geo_match_level),
                    param[ServiceEnumNumberSelectionBehaviorOrStr | None](
                        "NumberSelectionBehavior", number_selection_behavior
                    ),
                    param[str | None]("InterceptCallbackUrl", intercept_callback_url),
                    param[str | None]("OutOfSessionCallbackUrl", out_of_session_callback_url),
                    param[str | None]("ChatInstanceSid", chat_instance_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ProxyV1Service],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_service4(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Service.

        Args:
            sid: The Twilio-provided string that uniquely identifies the Service resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default10("/v1/Services/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_service4(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ProxyV1Service, RawError]:
        """Fetch a specific Service.

        Args:
            sid: The Twilio-provided string that uniquely identifies the Service resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default10("/v1/Services/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ProxyV1Service],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_service4(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListServiceResponse3, RawError]:
        """Retrieve a list of all Services for Twilio Proxy. A maximum of 100 records will be returned per page.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default10("/v1/Services"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListServiceResponse3],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_service3(
        self,
        sid: str,
        *,
        unique_name: str | None = None,
        default_ttl: int | None = None,
        callback_url: str | None = None,
        geo_match_level: ServiceEnumGeoMatchLevelOrStr | None = None,
        number_selection_behavior: ServiceEnumNumberSelectionBehaviorOrStr | None = None,
        intercept_callback_url: str | None = None,
        out_of_session_callback_url: str | None = None,
        chat_instance_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProxyV1Service, RawError]:
        """Update a specific Service.

        Args:
            sid: The Twilio-provided string that uniquely identifies the Service resource to update.
            unique_name: An application-defined string that uniquely identifies the resource. This value must be 191
                characters or fewer in length and be unique. **This value should not have PII.**
            default_ttl: The default ``ttl`` value to set for Sessions created in the Service. The TTL (time to live) is
                measured in seconds after the Session's last create or last Interaction. The default value of ``0``
                indicates an unlimited Session length. You can override a Session's default TTL value by setting its
                ``ttl`` value.
            callback_url: The URL we should call when the interaction status changes.
            geo_match_level: Where a proxy number must be located relative to the participant identifier. Can be:
                ``country``, ``area-code``, or ``extended-area-code``. The default value is ``country`` and more
                specific areas than ``country`` are only available in North America.
            number_selection_behavior: The preference for Proxy Number selection in the Service instance. Can be:
                ``prefer-sticky`` or ``avoid-sticky``. ``prefer-sticky`` means that we will try and select the same
                Proxy Number for a given participant if they have previous `Sessions
                <https://www.twilio.com/docs/proxy/api/session>`__, but we will not fail if that Proxy Number cannot be
                used. ``avoid-sticky`` means that we will try to use different Proxy Numbers as long as that is possible
                within a given pool rather than try and use a previously assigned number.
            intercept_callback_url: The URL we call on each interaction. If we receive a 403 status, we block the
                interaction; otherwise the interaction continues.
            out_of_session_callback_url: The URL we should call when an inbound call or SMS action occurs on a closed or
                non-existent Session. If your server (or a Twilio `function
                <https://www.twilio.com/en-us/serverless/functions>`__) responds with valid `TwiML
                <https://www.twilio.com/docs/voice/twiml>`__, we will process it. This means it is possible, for
                example, to play a message for a call, send an automated text message response, or redirect a call to
                another Phone Number. See `Out-of-Session Callback Response Guide
                <https://www.twilio.com/docs/proxy/out-session-callback-response-guide>`__ for more information.
            chat_instance_sid: The SID of the Chat Service Instance managed by Proxy Service. The Chat Service enables
                Proxy to forward SMS and channel messages to this chat instance. This is a one-to-one relationship.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/v1/Services/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            body=form_body(
                [
                    param[str | None]("UniqueName", unique_name),
                    param[int | None]("DefaultTtl", default_ttl),
                    param[str | None]("CallbackUrl", callback_url),
                    param[ServiceEnumGeoMatchLevelOrStr | None]("GeoMatchLevel", geo_match_level),
                    param[ServiceEnumNumberSelectionBehaviorOrStr | None](
                        "NumberSelectionBehavior", number_selection_behavior
                    ),
                    param[str | None]("InterceptCallbackUrl", intercept_callback_url),
                    param[str | None]("OutOfSessionCallbackUrl", out_of_session_callback_url),
                    param[str | None]("ChatInstanceSid", chat_instance_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ProxyV1Service],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncProxyV1ServiceApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_service4(
        self,
        unique_name: str,
        *,
        default_ttl: int | None = None,
        callback_url: str | None = None,
        geo_match_level: ServiceEnumGeoMatchLevelOrStr | None = None,
        number_selection_behavior: ServiceEnumNumberSelectionBehaviorOrStr | None = None,
        intercept_callback_url: str | None = None,
        out_of_session_callback_url: str | None = None,
        chat_instance_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProxyV1Service, RawError]:
        """Create a new Service for Twilio Proxy

        Args:
            unique_name: An application-defined string that uniquely identifies the resource. This value must be 191
                characters or fewer in length and be unique. **This value should not have PII.**
            default_ttl: The default ``ttl`` value to set for Sessions created in the Service. The TTL (time to live) is
                measured in seconds after the Session's last create or last Interaction. The default value of ``0``
                indicates an unlimited Session length. You can override a Session's default TTL value by setting its
                ``ttl`` value.
            callback_url: The URL we should call when the interaction status changes.
            geo_match_level: Where a proxy number must be located relative to the participant identifier. Can be:
                ``country``, ``area-code``, or ``extended-area-code``. The default value is ``country`` and more
                specific areas than ``country`` are only available in North America.
            number_selection_behavior: The preference for Proxy Number selection in the Service instance. Can be:
                ``prefer-sticky`` or ``avoid-sticky``. ``prefer-sticky`` means that we will try and select the same
                Proxy Number for a given participant if they have previous `Sessions
                <https://www.twilio.com/docs/proxy/api/session>`__, but we will not fail if that Proxy Number cannot be
                used. ``avoid-sticky`` means that we will try to use different Proxy Numbers as long as that is possible
                within a given pool rather than try and use a previously assigned number.
            intercept_callback_url: The URL we call on each interaction. If we receive a 403 status, we block the
                interaction; otherwise the interaction continues.
            out_of_session_callback_url: The URL we should call when an inbound call or SMS action occurs on a closed or
                non-existent Session. If your server (or a Twilio `function
                <https://www.twilio.com/en-us/serverless/functions>`__) responds with valid `TwiML
                <https://www.twilio.com/docs/voice/twiml>`__, we will process it. This means it is possible, for
                example, to play a message for a call, send an automated text message response, or redirect a call to
                another Phone Number. See `Out-of-Session Callback Response Guide
                <https://www.twilio.com/docs/proxy/out-session-callback-response-guide>`__ for more information.
            chat_instance_sid: The SID of the Chat Service Instance managed by Proxy Service. The Chat Service enables
                Proxy to forward SMS and channel messages to this chat instance. This is a one-to-one relationship.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/v1/Services"),
            body=form_body(
                [
                    param[str]("UniqueName", unique_name),
                    param[int | None]("DefaultTtl", default_ttl),
                    param[str | None]("CallbackUrl", callback_url),
                    param[ServiceEnumGeoMatchLevelOrStr | None]("GeoMatchLevel", geo_match_level),
                    param[ServiceEnumNumberSelectionBehaviorOrStr | None](
                        "NumberSelectionBehavior", number_selection_behavior
                    ),
                    param[str | None]("InterceptCallbackUrl", intercept_callback_url),
                    param[str | None]("OutOfSessionCallbackUrl", out_of_session_callback_url),
                    param[str | None]("ChatInstanceSid", chat_instance_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ProxyV1Service],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_service4(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Service.

        Args:
            sid: The Twilio-provided string that uniquely identifies the Service resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default10("/v1/Services/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_service4(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ProxyV1Service, RawError]:
        """Fetch a specific Service.

        Args:
            sid: The Twilio-provided string that uniquely identifies the Service resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default10("/v1/Services/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ProxyV1Service],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_service4(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListServiceResponse3, RawError]:
        """Retrieve a list of all Services for Twilio Proxy. A maximum of 100 records will be returned per page.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default10("/v1/Services"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListServiceResponse3],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_service3(
        self,
        sid: str,
        *,
        unique_name: str | None = None,
        default_ttl: int | None = None,
        callback_url: str | None = None,
        geo_match_level: ServiceEnumGeoMatchLevelOrStr | None = None,
        number_selection_behavior: ServiceEnumNumberSelectionBehaviorOrStr | None = None,
        intercept_callback_url: str | None = None,
        out_of_session_callback_url: str | None = None,
        chat_instance_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProxyV1Service, RawError]:
        """Update a specific Service.

        Args:
            sid: The Twilio-provided string that uniquely identifies the Service resource to update.
            unique_name: An application-defined string that uniquely identifies the resource. This value must be 191
                characters or fewer in length and be unique. **This value should not have PII.**
            default_ttl: The default ``ttl`` value to set for Sessions created in the Service. The TTL (time to live) is
                measured in seconds after the Session's last create or last Interaction. The default value of ``0``
                indicates an unlimited Session length. You can override a Session's default TTL value by setting its
                ``ttl`` value.
            callback_url: The URL we should call when the interaction status changes.
            geo_match_level: Where a proxy number must be located relative to the participant identifier. Can be:
                ``country``, ``area-code``, or ``extended-area-code``. The default value is ``country`` and more
                specific areas than ``country`` are only available in North America.
            number_selection_behavior: The preference for Proxy Number selection in the Service instance. Can be:
                ``prefer-sticky`` or ``avoid-sticky``. ``prefer-sticky`` means that we will try and select the same
                Proxy Number for a given participant if they have previous `Sessions
                <https://www.twilio.com/docs/proxy/api/session>`__, but we will not fail if that Proxy Number cannot be
                used. ``avoid-sticky`` means that we will try to use different Proxy Numbers as long as that is possible
                within a given pool rather than try and use a previously assigned number.
            intercept_callback_url: The URL we call on each interaction. If we receive a 403 status, we block the
                interaction; otherwise the interaction continues.
            out_of_session_callback_url: The URL we should call when an inbound call or SMS action occurs on a closed or
                non-existent Session. If your server (or a Twilio `function
                <https://www.twilio.com/en-us/serverless/functions>`__) responds with valid `TwiML
                <https://www.twilio.com/docs/voice/twiml>`__, we will process it. This means it is possible, for
                example, to play a message for a call, send an automated text message response, or redirect a call to
                another Phone Number. See `Out-of-Session Callback Response Guide
                <https://www.twilio.com/docs/proxy/out-session-callback-response-guide>`__ for more information.
            chat_instance_sid: The SID of the Chat Service Instance managed by Proxy Service. The Chat Service enables
                Proxy to forward SMS and channel messages to this chat instance. This is a one-to-one relationship.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/v1/Services/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            body=form_body(
                [
                    param[str | None]("UniqueName", unique_name),
                    param[int | None]("DefaultTtl", default_ttl),
                    param[str | None]("CallbackUrl", callback_url),
                    param[ServiceEnumGeoMatchLevelOrStr | None]("GeoMatchLevel", geo_match_level),
                    param[ServiceEnumNumberSelectionBehaviorOrStr | None](
                        "NumberSelectionBehavior", number_selection_behavior
                    ),
                    param[str | None]("InterceptCallbackUrl", intercept_callback_url),
                    param[str | None]("OutOfSessionCallbackUrl", out_of_session_callback_url),
                    param[str | None]("ChatInstanceSid", chat_instance_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ProxyV1Service],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
