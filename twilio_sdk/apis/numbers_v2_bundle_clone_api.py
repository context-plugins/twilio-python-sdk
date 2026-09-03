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
from ..models.numbers_v2_bundle_clone import NumbersV2BundleClone
from ..server.server import Server


class NumbersV2BundleCloneApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NumbersV2BundleCloneApiWithRawResponse(client, server, auth)

    def create_bundle_clone(
        self,
        bundle_sid: str,
        target_account_sid: str,
        *,
        move_to_draft: bool | None = None,
        friendly_name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> NumbersV2BundleClone:
        """Creates a new clone of the Bundle in target Account. It will internally create clones of all the bundle items
        (identities and documents) of the original bundle

        Args:
            bundle_sid: The unique string that identifies the Bundle to be cloned.
            target_account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ where the
                bundle needs to be cloned.
            move_to_draft: If set to true, the cloned bundle will be in the DRAFT state, else it will be twilio-approved
            friendly_name: The string that you assigned to describe the cloned bundle.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_bundle_clone(
            bundle_sid,
            target_account_sid,
            move_to_draft=move_to_draft,
            friendly_name=friendly_name,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> NumbersV2BundleCloneApiWithRawResponse:
        return self._with_raw_response


class AsyncNumbersV2BundleCloneApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNumbersV2BundleCloneApiWithRawResponse(client, server, auth)

    async def create_bundle_clone(
        self,
        bundle_sid: str,
        target_account_sid: str,
        *,
        move_to_draft: bool | None = None,
        friendly_name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> NumbersV2BundleClone:
        """Creates a new clone of the Bundle in target Account. It will internally create clones of all the bundle items
        (identities and documents) of the original bundle

        Args:
            bundle_sid: The unique string that identifies the Bundle to be cloned.
            target_account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ where the
                bundle needs to be cloned.
            move_to_draft: If set to true, the cloned bundle will be in the DRAFT state, else it will be twilio-approved
            friendly_name: The string that you assigned to describe the cloned bundle.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_bundle_clone(
                bundle_sid,
                target_account_sid,
                move_to_draft=move_to_draft,
                friendly_name=friendly_name,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncNumbersV2BundleCloneApiWithRawResponse:
        return self._with_raw_response


class NumbersV2BundleCloneApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_bundle_clone(
        self,
        bundle_sid: str,
        target_account_sid: str,
        *,
        move_to_draft: bool | None = None,
        friendly_name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[NumbersV2BundleClone, RawError]:
        """Creates a new clone of the Bundle in target Account. It will internally create clones of all the bundle items
        (identities and documents) of the original bundle

        Args:
            bundle_sid: The unique string that identifies the Bundle to be cloned.
            target_account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ where the
                bundle needs to be cloned.
            move_to_draft: If set to true, the cloned bundle will be in the DRAFT state, else it will be twilio-approved
            friendly_name: The string that you assigned to describe the cloned bundle.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v2/RegulatoryCompliance/Bundles/{BundleSid}/Clones"),
            path_params=[param[str]("BundleSid", bundle_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("TargetAccountSid", target_account_sid),
                    param[bool | None]("MoveToDraft", move_to_draft),
                    param[str | None]("FriendlyName", friendly_name),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2BundleClone],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncNumbersV2BundleCloneApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_bundle_clone(
        self,
        bundle_sid: str,
        target_account_sid: str,
        *,
        move_to_draft: bool | None = None,
        friendly_name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[NumbersV2BundleClone, RawError]:
        """Creates a new clone of the Bundle in target Account. It will internally create clones of all the bundle items
        (identities and documents) of the original bundle

        Args:
            bundle_sid: The unique string that identifies the Bundle to be cloned.
            target_account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ where the
                bundle needs to be cloned.
            move_to_draft: If set to true, the cloned bundle will be in the DRAFT state, else it will be twilio-approved
            friendly_name: The string that you assigned to describe the cloned bundle.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v2/RegulatoryCompliance/Bundles/{BundleSid}/Clones"),
            path_params=[param[str]("BundleSid", bundle_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("TargetAccountSid", target_account_sid),
                    param[bool | None]("MoveToDraft", move_to_draft),
                    param[str | None]("FriendlyName", friendly_name),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2BundleClone],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
