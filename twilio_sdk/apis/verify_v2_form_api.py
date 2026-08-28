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
from ..models.enums.form_enum_form_types import FormEnumFormTypesOrStr
from ..models.verify_v2_form import VerifyV2Form
from ..server.server import Server


class VerifyV2FormApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VerifyV2FormApiWithRawResponse(client, server, auth)

    def fetch_form(
        self, form_type: FormEnumFormTypesOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> VerifyV2Form:
        """Fetch the forms for a specific Form Type.

        Args:
            form_type: The Type of this Form. Currently only ``form-push`` is supported.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_form(form_type, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> VerifyV2FormApiWithRawResponse:
        return self._with_raw_response


class AsyncVerifyV2FormApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVerifyV2FormApiWithRawResponse(client, server, auth)

    async def fetch_form(
        self, form_type: FormEnumFormTypesOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> VerifyV2Form:
        """Fetch the forms for a specific Form Type.

        Args:
            form_type: The Type of this Form. Currently only ``form-push`` is supported.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_form(form_type, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncVerifyV2FormApiWithRawResponse:
        return self._with_raw_response


class VerifyV2FormApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_form(
        self, form_type: FormEnumFormTypesOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VerifyV2Form, RawError]:
        """Fetch the forms for a specific Form Type.

        Args:
            form_type: The Type of this Form. Currently only ``form-push`` is supported.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default3("/v2/Forms/{FormType}"),
            path_params=[param[FormEnumFormTypesOrStr]("FormType", form_type)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2Form],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncVerifyV2FormApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_form(
        self, form_type: FormEnumFormTypesOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VerifyV2Form, RawError]:
        """Fetch the forms for a specific Form Type.

        Args:
            form_type: The Type of this Form. Currently only ``form-push`` is supported.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default3("/v2/Forms/{FormType}"),
            path_params=[param[FormEnumFormTypesOrStr]("FormType", form_type)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[VerifyV2Form],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
