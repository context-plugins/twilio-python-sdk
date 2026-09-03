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
from ..models.numbers_v2_regulatory_compliance_bundle_replace_items import (
    NumbersV2RegulatoryComplianceBundleReplaceItems,
)
from ..server.server import Server


class NumbersV2ReplaceItems:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NumbersV2ReplaceItemsWithRawResponse(client, server, auth)

    def create_replace_items(
        self, bundle_sid: str, from_bundle_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV2RegulatoryComplianceBundleReplaceItems:
        """Replaces all bundle items in the target bundle (specified in the path) with all the bundle items of the
        source bundle (specified by the from_bundle_sid body param)

        Args:
            bundle_sid: The unique string that identifies the Bundle where the item assignments are going to be
                replaced.
            from_bundle_sid: The source bundle sid to copy the item assignments from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_replace_items(
            bundle_sid, from_bundle_sid, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> NumbersV2ReplaceItemsWithRawResponse:
        return self._with_raw_response


class AsyncNumbersV2ReplaceItems:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNumbersV2ReplaceItemsWithRawResponse(client, server, auth)

    async def create_replace_items(
        self, bundle_sid: str, from_bundle_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV2RegulatoryComplianceBundleReplaceItems:
        """Replaces all bundle items in the target bundle (specified in the path) with all the bundle items of the
        source bundle (specified by the from_bundle_sid body param)

        Args:
            bundle_sid: The unique string that identifies the Bundle where the item assignments are going to be
                replaced.
            from_bundle_sid: The source bundle sid to copy the item assignments from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_replace_items(
                bundle_sid, from_bundle_sid, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncNumbersV2ReplaceItemsWithRawResponse:
        return self._with_raw_response


class NumbersV2ReplaceItemsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_replace_items(
        self, bundle_sid: str, from_bundle_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV2RegulatoryComplianceBundleReplaceItems, RawError]:
        """Replaces all bundle items in the target bundle (specified in the path) with all the bundle items of the
        source bundle (specified by the from_bundle_sid body param)

        Args:
            bundle_sid: The unique string that identifies the Bundle where the item assignments are going to be
                replaced.
            from_bundle_sid: The source bundle sid to copy the item assignments from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v2/RegulatoryCompliance/Bundles/{BundleSid}/ReplaceItems"),
            path_params=[param[str]("BundleSid", bundle_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str]("FromBundleSid", from_bundle_sid)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2RegulatoryComplianceBundleReplaceItems],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncNumbersV2ReplaceItemsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_replace_items(
        self, bundle_sid: str, from_bundle_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV2RegulatoryComplianceBundleReplaceItems, RawError]:
        """Replaces all bundle items in the target bundle (specified in the path) with all the bundle items of the
        source bundle (specified by the from_bundle_sid body param)

        Args:
            bundle_sid: The unique string that identifies the Bundle where the item assignments are going to be
                replaced.
            from_bundle_sid: The source bundle sid to copy the item assignments from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v2/RegulatoryCompliance/Bundles/{BundleSid}/ReplaceItems"),
            path_params=[param[str]("BundleSid", bundle_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str]("FromBundleSid", from_bundle_sid)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2RegulatoryComplianceBundleReplaceItems],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
