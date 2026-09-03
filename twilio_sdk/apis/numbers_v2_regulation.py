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
from ..models.enums.regulation_enum_end_user_type import RegulationEnumEndUserTypeOrStr
from ..models.list_regulation_response import ListRegulationResponse
from ..models.numbers_v2_regulatory_compliance_regulation import NumbersV2RegulatoryComplianceRegulation
from ..server.server import Server


class NumbersV2Regulation:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NumbersV2RegulationWithRawResponse(client, server, auth)

    def fetch_regulation(
        self, sid: str, *, include_constraints: bool | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV2RegulatoryComplianceRegulation:
        """Fetch specific Regulation Instance.

        Args:
            sid: The unique string that identifies the Regulation resource.
            include_constraints: A boolean parameter indicating whether to include constraints or not for supporting end
                user, documents and their fields
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_regulation(
            sid, include_constraints=include_constraints, request_options=request_options
        ).unwrap()

    def list_regulation(
        self,
        *,
        end_user_type: RegulationEnumEndUserTypeOrStr | None = None,
        iso_country: str | None = None,
        number_type: str | None = None,
        include_constraints: bool | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListRegulationResponse:
        """Retrieve a list of all Regulations.

        Args:
            end_user_type: The type of End User the regulation requires - can be ``individual`` or ``business``.
            iso_country: The ISO country code of the phone number's country.
            number_type: The type of phone number that the regulatory requiremnt is restricting.
            include_constraints: A boolean parameter indicating whether to include constraints or not for supporting end
                user, documents and their fields
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_regulation(
            end_user_type=end_user_type,
            iso_country=iso_country,
            number_type=number_type,
            include_constraints=include_constraints,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> NumbersV2RegulationWithRawResponse:
        return self._with_raw_response


class AsyncNumbersV2Regulation:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNumbersV2RegulationWithRawResponse(client, server, auth)

    async def fetch_regulation(
        self, sid: str, *, include_constraints: bool | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV2RegulatoryComplianceRegulation:
        """Fetch specific Regulation Instance.

        Args:
            sid: The unique string that identifies the Regulation resource.
            include_constraints: A boolean parameter indicating whether to include constraints or not for supporting end
                user, documents and their fields
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_regulation(
                sid, include_constraints=include_constraints, request_options=request_options
            )
        ).unwrap()

    async def list_regulation(
        self,
        *,
        end_user_type: RegulationEnumEndUserTypeOrStr | None = None,
        iso_country: str | None = None,
        number_type: str | None = None,
        include_constraints: bool | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListRegulationResponse:
        """Retrieve a list of all Regulations.

        Args:
            end_user_type: The type of End User the regulation requires - can be ``individual`` or ``business``.
            iso_country: The ISO country code of the phone number's country.
            number_type: The type of phone number that the regulatory requiremnt is restricting.
            include_constraints: A boolean parameter indicating whether to include constraints or not for supporting end
                user, documents and their fields
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_regulation(
                end_user_type=end_user_type,
                iso_country=iso_country,
                number_type=number_type,
                include_constraints=include_constraints,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncNumbersV2RegulationWithRawResponse:
        return self._with_raw_response


class NumbersV2RegulationWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_regulation(
        self, sid: str, *, include_constraints: bool | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV2RegulatoryComplianceRegulation, RawError]:
        """Fetch specific Regulation Instance.

        Args:
            sid: The unique string that identifies the Regulation resource.
            include_constraints: A boolean parameter indicating whether to include constraints or not for supporting end
                user, documents and their fields
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/RegulatoryCompliance/Regulations/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            query_params=[param[bool | None]("IncludeConstraints", include_constraints)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2RegulatoryComplianceRegulation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_regulation(
        self,
        *,
        end_user_type: RegulationEnumEndUserTypeOrStr | None = None,
        iso_country: str | None = None,
        number_type: str | None = None,
        include_constraints: bool | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListRegulationResponse, RawError]:
        """Retrieve a list of all Regulations.

        Args:
            end_user_type: The type of End User the regulation requires - can be ``individual`` or ``business``.
            iso_country: The ISO country code of the phone number's country.
            number_type: The type of phone number that the regulatory requiremnt is restricting.
            include_constraints: A boolean parameter indicating whether to include constraints or not for supporting end
                user, documents and their fields
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/RegulatoryCompliance/Regulations"),
            query_params=[
                param[RegulationEnumEndUserTypeOrStr | None]("EndUserType", end_user_type),
                param[str | None]("IsoCountry", iso_country),
                param[str | None]("NumberType", number_type),
                param[bool | None]("IncludeConstraints", include_constraints),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListRegulationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncNumbersV2RegulationWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_regulation(
        self, sid: str, *, include_constraints: bool | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV2RegulatoryComplianceRegulation, RawError]:
        """Fetch specific Regulation Instance.

        Args:
            sid: The unique string that identifies the Regulation resource.
            include_constraints: A boolean parameter indicating whether to include constraints or not for supporting end
                user, documents and their fields
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/RegulatoryCompliance/Regulations/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            query_params=[param[bool | None]("IncludeConstraints", include_constraints)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2RegulatoryComplianceRegulation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_regulation(
        self,
        *,
        end_user_type: RegulationEnumEndUserTypeOrStr | None = None,
        iso_country: str | None = None,
        number_type: str | None = None,
        include_constraints: bool | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListRegulationResponse, RawError]:
        """Retrieve a list of all Regulations.

        Args:
            end_user_type: The type of End User the regulation requires - can be ``individual`` or ``business``.
            iso_country: The ISO country code of the phone number's country.
            number_type: The type of phone number that the regulatory requiremnt is restricting.
            include_constraints: A boolean parameter indicating whether to include constraints or not for supporting end
                user, documents and their fields
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/RegulatoryCompliance/Regulations"),
            query_params=[
                param[RegulationEnumEndUserTypeOrStr | None]("EndUserType", end_user_type),
                param[str | None]("IsoCountry", iso_country),
                param[str | None]("NumberType", number_type),
                param[bool | None]("IncludeConstraints", include_constraints),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListRegulationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
