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
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.trusthub_v1_compliance_inquiry import TrusthubV1ComplianceInquiry
from ..server.server import Server


class TrusthubV1ComplianceInquiries:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TrusthubV1ComplianceInquiriesWithRawResponse(client, server, auth)

    def create_compliance_inquiry(
        self,
        *,
        notification_email: str | None = None,
        theme_set_id: str | None = None,
        primary_profile_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TrusthubV1ComplianceInquiry:
        """Create a new Compliance Inquiry for the authenticated account. This is necessary to start a new embedded
        session.

        Args:
            notification_email: The email address that approval status updates will be sent to. If not specified, the
                email address associated with your primary customer profile will be used.
            theme_set_id: Theme id for styling the inquiry form.
            primary_profile_sid: The unique SID identifier of the Primary Customer Profile that should be used as a
                parent. Only necessary when creating a secondary Customer Profile.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_compliance_inquiry(
            notification_email=notification_email,
            theme_set_id=theme_set_id,
            primary_profile_sid=primary_profile_sid,
            request_options=request_options,
        ).unwrap()

    def update_compliance_inquiry(
        self,
        customer_id: str,
        primary_profile_sid: str,
        *,
        theme_set_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TrusthubV1ComplianceInquiry:
        """Resume a specific Compliance Inquiry that has expired, or re-open a rejected Compliance Inquiry for editing.

        Args:
            customer_id: The unique CustomerId matching the Customer Profile/Compliance Inquiry that should be resumed
                or resubmitted. This value will have been returned by the initial Compliance Inquiry creation call.
            primary_profile_sid: The unique SID identifier of the Primary Customer Profile that should be used as a
                parent. Only necessary when creating a secondary Customer Profile.
            theme_set_id: Theme id for styling the inquiry form.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_compliance_inquiry(
            customer_id, primary_profile_sid, theme_set_id=theme_set_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> TrusthubV1ComplianceInquiriesWithRawResponse:
        return self._with_raw_response


class AsyncTrusthubV1ComplianceInquiries:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTrusthubV1ComplianceInquiriesWithRawResponse(client, server, auth)

    async def create_compliance_inquiry(
        self,
        *,
        notification_email: str | None = None,
        theme_set_id: str | None = None,
        primary_profile_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TrusthubV1ComplianceInquiry:
        """Create a new Compliance Inquiry for the authenticated account. This is necessary to start a new embedded
        session.

        Args:
            notification_email: The email address that approval status updates will be sent to. If not specified, the
                email address associated with your primary customer profile will be used.
            theme_set_id: Theme id for styling the inquiry form.
            primary_profile_sid: The unique SID identifier of the Primary Customer Profile that should be used as a
                parent. Only necessary when creating a secondary Customer Profile.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_compliance_inquiry(
                notification_email=notification_email,
                theme_set_id=theme_set_id,
                primary_profile_sid=primary_profile_sid,
                request_options=request_options,
            )
        ).unwrap()

    async def update_compliance_inquiry(
        self,
        customer_id: str,
        primary_profile_sid: str,
        *,
        theme_set_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TrusthubV1ComplianceInquiry:
        """Resume a specific Compliance Inquiry that has expired, or re-open a rejected Compliance Inquiry for editing.

        Args:
            customer_id: The unique CustomerId matching the Customer Profile/Compliance Inquiry that should be resumed
                or resubmitted. This value will have been returned by the initial Compliance Inquiry creation call.
            primary_profile_sid: The unique SID identifier of the Primary Customer Profile that should be used as a
                parent. Only necessary when creating a secondary Customer Profile.
            theme_set_id: Theme id for styling the inquiry form.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_compliance_inquiry(
                customer_id, primary_profile_sid, theme_set_id=theme_set_id, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTrusthubV1ComplianceInquiriesWithRawResponse:
        return self._with_raw_response


class TrusthubV1ComplianceInquiriesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_compliance_inquiry(
        self,
        *,
        notification_email: str | None = None,
        theme_set_id: str | None = None,
        primary_profile_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TrusthubV1ComplianceInquiry, RawError]:
        """Create a new Compliance Inquiry for the authenticated account. This is necessary to start a new embedded
        session.

        Args:
            notification_email: The email address that approval status updates will be sent to. If not specified, the
                email address associated with your primary customer profile will be used.
            theme_set_id: Theme id for styling the inquiry form.
            primary_profile_sid: The unique SID identifier of the Primary Customer Profile that should be used as a
                parent. Only necessary when creating a secondary Customer Profile.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/v1/ComplianceInquiries/Customers/Initialize"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("NotificationEmail", notification_email),
                    param[str | None]("ThemeSetId", theme_set_id),
                    param[str | None]("PrimaryProfileSid", primary_profile_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1ComplianceInquiry],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_compliance_inquiry(
        self,
        customer_id: str,
        primary_profile_sid: str,
        *,
        theme_set_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TrusthubV1ComplianceInquiry, RawError]:
        """Resume a specific Compliance Inquiry that has expired, or re-open a rejected Compliance Inquiry for editing.

        Args:
            customer_id: The unique CustomerId matching the Customer Profile/Compliance Inquiry that should be resumed
                or resubmitted. This value will have been returned by the initial Compliance Inquiry creation call.
            primary_profile_sid: The unique SID identifier of the Primary Customer Profile that should be used as a
                parent. Only necessary when creating a secondary Customer Profile.
            theme_set_id: Theme id for styling the inquiry form.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/v1/ComplianceInquiries/Customers/{CustomerId}/Initialize"),
            path_params=[param[str]("CustomerId", customer_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [param[str]("PrimaryProfileSid", primary_profile_sid), param[str | None]("ThemeSetId", theme_set_id)]
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1ComplianceInquiry],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTrusthubV1ComplianceInquiriesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_compliance_inquiry(
        self,
        *,
        notification_email: str | None = None,
        theme_set_id: str | None = None,
        primary_profile_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TrusthubV1ComplianceInquiry, RawError]:
        """Create a new Compliance Inquiry for the authenticated account. This is necessary to start a new embedded
        session.

        Args:
            notification_email: The email address that approval status updates will be sent to. If not specified, the
                email address associated with your primary customer profile will be used.
            theme_set_id: Theme id for styling the inquiry form.
            primary_profile_sid: The unique SID identifier of the Primary Customer Profile that should be used as a
                parent. Only necessary when creating a secondary Customer Profile.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/v1/ComplianceInquiries/Customers/Initialize"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("NotificationEmail", notification_email),
                    param[str | None]("ThemeSetId", theme_set_id),
                    param[str | None]("PrimaryProfileSid", primary_profile_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1ComplianceInquiry],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_compliance_inquiry(
        self,
        customer_id: str,
        primary_profile_sid: str,
        *,
        theme_set_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TrusthubV1ComplianceInquiry, RawError]:
        """Resume a specific Compliance Inquiry that has expired, or re-open a rejected Compliance Inquiry for editing.

        Args:
            customer_id: The unique CustomerId matching the Customer Profile/Compliance Inquiry that should be resumed
                or resubmitted. This value will have been returned by the initial Compliance Inquiry creation call.
            primary_profile_sid: The unique SID identifier of the Primary Customer Profile that should be used as a
                parent. Only necessary when creating a secondary Customer Profile.
            theme_set_id: Theme id for styling the inquiry form.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/v1/ComplianceInquiries/Customers/{CustomerId}/Initialize"),
            path_params=[param[str]("CustomerId", customer_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [param[str]("PrimaryProfileSid", primary_profile_sid), param[str | None]("ThemeSetId", theme_set_id)]
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1ComplianceInquiry],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
