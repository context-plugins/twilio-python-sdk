from __future__ import annotations

from pydantic import AnyUrl

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    RFC3339DateTime,
    SecuredRawResponse,
    empty_response,
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.enums.bundle_enum_end_user_type import BundleEnumEndUserTypeOrStr
from ..models.enums.bundle_enum_sort_by import BundleEnumSortByOrStr
from ..models.enums.bundle_enum_sort_direction import BundleEnumSortDirectionOrStr
from ..models.enums.bundle_enum_status import BundleEnumStatusOrStr
from ..models.list_bundle_response import ListBundleResponse
from ..models.numbers_v2_regulatory_compliance_bundle import NumbersV2RegulatoryComplianceBundle
from ..server.server import Server


class NumbersV2Bundle:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NumbersV2BundleWithRawResponse(client, server, auth)

    def create_bundle(
        self,
        friendly_name: str,
        email: str,
        *,
        status_callback: AnyUrl | None = None,
        regulation_sid: str | None = None,
        iso_country: str | None = None,
        end_user_type: BundleEnumEndUserTypeOrStr | None = None,
        number_type: str | None = None,
        is_test: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> NumbersV2RegulatoryComplianceBundle:
        """Create a new Bundle.

        Args:
            friendly_name: The string that you assigned to describe the resource.
            email: The email address that will receive updates when the Bundle resource changes status.
            status_callback: The URL we call to inform your application of status changes.
            regulation_sid: The unique string of a regulation that is associated to the Bundle resource.
            iso_country: The `ISO country code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ of the Bundle's
                phone number country ownership request.
            end_user_type: Value sent with the request.
            number_type: The type of phone number of the Bundle's ownership request. Can be ``local``, ``mobile``,
                ``national``, or ``toll-free``.
            is_test: Indicates that Bundle is a Test Bundle and will be Auto-Rejected
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_bundle(
            friendly_name,
            email,
            status_callback=status_callback,
            regulation_sid=regulation_sid,
            iso_country=iso_country,
            end_user_type=end_user_type,
            number_type=number_type,
            is_test=is_test,
            request_options=request_options,
        ).unwrap()

    def delete_bundle(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Delete a specific Bundle.

        Args:
            sid: The unique string that we created to identify the Bundle resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_bundle(sid, request_options=request_options).unwrap()

    def fetch_bundle(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV2RegulatoryComplianceBundle:
        """Fetch a specific Bundle instance.

        Args:
            sid: The unique string that we created to identify the Bundle resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_bundle(sid, request_options=request_options).unwrap()

    def list_bundle(
        self,
        *,
        status: BundleEnumStatusOrStr | None = None,
        bundle_sids: str | None = None,
        friendly_name: str | None = None,
        regulation_sid: str | None = None,
        iso_country: str | None = None,
        number_type: str | None = None,
        end_user_type: BundleEnumEndUserTypeOrStr | None = None,
        has_valid_until_date: bool | None = None,
        sort_by: BundleEnumSortByOrStr | None = None,
        sort_direction: BundleEnumSortDirectionOrStr | None = None,
        valid_until_date: RFC3339DateTime | None = None,
        valid_until_date_query: RFC3339DateTime | None = None,
        valid_until_date_query_query: RFC3339DateTime | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListBundleResponse:
        """Retrieve a list of all Bundles for an account.

        Args:
            status: The verification status of the Bundle resource. Please refer to `Bundle Statuses
                <https://www.twilio.com/docs/phone-numbers/regulatory/api/bundles#bundle-statuses>`__ for more details.
            bundle_sids: A comma-separated list of Bundle SIDs to filter the results (maximum 20). Each Bundle SID must
                match ``^BU[0-9a-fA-F]{32}$``.
            friendly_name: The string that you assigned to describe the resource. The column can contain 255 variable
                characters.
            regulation_sid: The unique string of a `Regulation resource
                <https://www.twilio.com/docs/phone-numbers/regulatory/api/regulations>`__ that is associated to the
                Bundle resource.
            iso_country: The 2-digit `ISO country code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ of the
                Bundle's phone number country ownership request.
            number_type: The type of phone number of the Bundle's ownership request. Can be ``local``, ``mobile``,
                ``national``, or ``toll-free``.
            end_user_type: The end user type of the regulation of the Bundle. Can be ``business`` or ``individual``.
            has_valid_until_date: Indicates that the Bundle is a valid Bundle until a specified expiration date.
            sort_by: Can be ``valid-until`` or ``date-updated``. Defaults to ``date-created``.
            sort_direction: Default is ``DESC``. Can be ``ASC`` or ``DESC``.
            valid_until_date: Date to filter Bundles having their ``valid_until_date`` before or after the specified
                date. Can be ``ValidUntilDate>=`` or ``ValidUntilDate<=``. Both can be used in conjunction as well. `ISO
                8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ is the acceptable date format.
            valid_until_date_query: Date to filter Bundles having their ``valid_until_date`` before or after the
                specified date. Can be ``ValidUntilDate>=`` or ``ValidUntilDate<=``. Both can be used in conjunction as
                well. `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ is the acceptable date format.
            valid_until_date_query_query: Date to filter Bundles having their ``valid_until_date`` before or after the
                specified date. Can be ``ValidUntilDate>=`` or ``ValidUntilDate<=``. Both can be used in conjunction as
                well. `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ is the acceptable date format.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_bundle(
            status=status,
            bundle_sids=bundle_sids,
            friendly_name=friendly_name,
            regulation_sid=regulation_sid,
            iso_country=iso_country,
            number_type=number_type,
            end_user_type=end_user_type,
            has_valid_until_date=has_valid_until_date,
            sort_by=sort_by,
            sort_direction=sort_direction,
            valid_until_date=valid_until_date,
            valid_until_date_query=valid_until_date_query,
            valid_until_date_query_query=valid_until_date_query_query,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_bundle(
        self,
        sid: str,
        *,
        status: BundleEnumStatusOrStr | None = None,
        status_callback: AnyUrl | None = None,
        friendly_name: str | None = None,
        email: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> NumbersV2RegulatoryComplianceBundle:
        """Updates a Bundle in an account.

        Args:
            sid: The unique string that we created to identify the Bundle resource.
            status: The verification status of the Bundle resource.
            status_callback: The URL we call to inform your application of status changes.
            friendly_name: The string that you assigned to describe the resource.
            email: The email address that will receive updates when the Bundle resource changes status.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_bundle(
            sid,
            status=status,
            status_callback=status_callback,
            friendly_name=friendly_name,
            email=email,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> NumbersV2BundleWithRawResponse:
        return self._with_raw_response


class AsyncNumbersV2Bundle:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNumbersV2BundleWithRawResponse(client, server, auth)

    async def create_bundle(
        self,
        friendly_name: str,
        email: str,
        *,
        status_callback: AnyUrl | None = None,
        regulation_sid: str | None = None,
        iso_country: str | None = None,
        end_user_type: BundleEnumEndUserTypeOrStr | None = None,
        number_type: str | None = None,
        is_test: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> NumbersV2RegulatoryComplianceBundle:
        """Create a new Bundle.

        Args:
            friendly_name: The string that you assigned to describe the resource.
            email: The email address that will receive updates when the Bundle resource changes status.
            status_callback: The URL we call to inform your application of status changes.
            regulation_sid: The unique string of a regulation that is associated to the Bundle resource.
            iso_country: The `ISO country code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ of the Bundle's
                phone number country ownership request.
            end_user_type: Value sent with the request.
            number_type: The type of phone number of the Bundle's ownership request. Can be ``local``, ``mobile``,
                ``national``, or ``toll-free``.
            is_test: Indicates that Bundle is a Test Bundle and will be Auto-Rejected
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_bundle(
                friendly_name,
                email,
                status_callback=status_callback,
                regulation_sid=regulation_sid,
                iso_country=iso_country,
                end_user_type=end_user_type,
                number_type=number_type,
                is_test=is_test,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_bundle(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Delete a specific Bundle.

        Args:
            sid: The unique string that we created to identify the Bundle resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_bundle(sid, request_options=request_options)).unwrap()

    async def fetch_bundle(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV2RegulatoryComplianceBundle:
        """Fetch a specific Bundle instance.

        Args:
            sid: The unique string that we created to identify the Bundle resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_bundle(sid, request_options=request_options)).unwrap()

    async def list_bundle(
        self,
        *,
        status: BundleEnumStatusOrStr | None = None,
        bundle_sids: str | None = None,
        friendly_name: str | None = None,
        regulation_sid: str | None = None,
        iso_country: str | None = None,
        number_type: str | None = None,
        end_user_type: BundleEnumEndUserTypeOrStr | None = None,
        has_valid_until_date: bool | None = None,
        sort_by: BundleEnumSortByOrStr | None = None,
        sort_direction: BundleEnumSortDirectionOrStr | None = None,
        valid_until_date: RFC3339DateTime | None = None,
        valid_until_date_query: RFC3339DateTime | None = None,
        valid_until_date_query_query: RFC3339DateTime | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListBundleResponse:
        """Retrieve a list of all Bundles for an account.

        Args:
            status: The verification status of the Bundle resource. Please refer to `Bundle Statuses
                <https://www.twilio.com/docs/phone-numbers/regulatory/api/bundles#bundle-statuses>`__ for more details.
            bundle_sids: A comma-separated list of Bundle SIDs to filter the results (maximum 20). Each Bundle SID must
                match ``^BU[0-9a-fA-F]{32}$``.
            friendly_name: The string that you assigned to describe the resource. The column can contain 255 variable
                characters.
            regulation_sid: The unique string of a `Regulation resource
                <https://www.twilio.com/docs/phone-numbers/regulatory/api/regulations>`__ that is associated to the
                Bundle resource.
            iso_country: The 2-digit `ISO country code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ of the
                Bundle's phone number country ownership request.
            number_type: The type of phone number of the Bundle's ownership request. Can be ``local``, ``mobile``,
                ``national``, or ``toll-free``.
            end_user_type: The end user type of the regulation of the Bundle. Can be ``business`` or ``individual``.
            has_valid_until_date: Indicates that the Bundle is a valid Bundle until a specified expiration date.
            sort_by: Can be ``valid-until`` or ``date-updated``. Defaults to ``date-created``.
            sort_direction: Default is ``DESC``. Can be ``ASC`` or ``DESC``.
            valid_until_date: Date to filter Bundles having their ``valid_until_date`` before or after the specified
                date. Can be ``ValidUntilDate>=`` or ``ValidUntilDate<=``. Both can be used in conjunction as well. `ISO
                8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ is the acceptable date format.
            valid_until_date_query: Date to filter Bundles having their ``valid_until_date`` before or after the
                specified date. Can be ``ValidUntilDate>=`` or ``ValidUntilDate<=``. Both can be used in conjunction as
                well. `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ is the acceptable date format.
            valid_until_date_query_query: Date to filter Bundles having their ``valid_until_date`` before or after the
                specified date. Can be ``ValidUntilDate>=`` or ``ValidUntilDate<=``. Both can be used in conjunction as
                well. `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ is the acceptable date format.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_bundle(
                status=status,
                bundle_sids=bundle_sids,
                friendly_name=friendly_name,
                regulation_sid=regulation_sid,
                iso_country=iso_country,
                number_type=number_type,
                end_user_type=end_user_type,
                has_valid_until_date=has_valid_until_date,
                sort_by=sort_by,
                sort_direction=sort_direction,
                valid_until_date=valid_until_date,
                valid_until_date_query=valid_until_date_query,
                valid_until_date_query_query=valid_until_date_query_query,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_bundle(
        self,
        sid: str,
        *,
        status: BundleEnumStatusOrStr | None = None,
        status_callback: AnyUrl | None = None,
        friendly_name: str | None = None,
        email: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> NumbersV2RegulatoryComplianceBundle:
        """Updates a Bundle in an account.

        Args:
            sid: The unique string that we created to identify the Bundle resource.
            status: The verification status of the Bundle resource.
            status_callback: The URL we call to inform your application of status changes.
            friendly_name: The string that you assigned to describe the resource.
            email: The email address that will receive updates when the Bundle resource changes status.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_bundle(
                sid,
                status=status,
                status_callback=status_callback,
                friendly_name=friendly_name,
                email=email,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncNumbersV2BundleWithRawResponse:
        return self._with_raw_response


class NumbersV2BundleWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_bundle(
        self,
        friendly_name: str,
        email: str,
        *,
        status_callback: AnyUrl | None = None,
        regulation_sid: str | None = None,
        iso_country: str | None = None,
        end_user_type: BundleEnumEndUserTypeOrStr | None = None,
        number_type: str | None = None,
        is_test: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[NumbersV2RegulatoryComplianceBundle, RawError]:
        """Create a new Bundle.

        Args:
            friendly_name: The string that you assigned to describe the resource.
            email: The email address that will receive updates when the Bundle resource changes status.
            status_callback: The URL we call to inform your application of status changes.
            regulation_sid: The unique string of a regulation that is associated to the Bundle resource.
            iso_country: The `ISO country code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ of the Bundle's
                phone number country ownership request.
            end_user_type: Value sent with the request.
            number_type: The type of phone number of the Bundle's ownership request. Can be ``local``, ``mobile``,
                ``national``, or ``toll-free``.
            is_test: Indicates that Bundle is a Test Bundle and will be Auto-Rejected
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v2/RegulatoryCompliance/Bundles"),
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[str]("Email", email),
                    param[AnyUrl | None]("StatusCallback", status_callback),
                    param[str | None]("RegulationSid", regulation_sid),
                    param[str | None]("IsoCountry", iso_country),
                    param[BundleEnumEndUserTypeOrStr | None]("EndUserType", end_user_type),
                    param[str | None]("NumberType", number_type),
                    param[bool | None]("IsTest", is_test),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2RegulatoryComplianceBundle],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_bundle(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Bundle.

        Args:
            sid: The unique string that we created to identify the Bundle resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default5("/v2/RegulatoryCompliance/Bundles/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_bundle(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV2RegulatoryComplianceBundle, RawError]:
        """Fetch a specific Bundle instance.

        Args:
            sid: The unique string that we created to identify the Bundle resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/RegulatoryCompliance/Bundles/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2RegulatoryComplianceBundle],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_bundle(
        self,
        *,
        status: BundleEnumStatusOrStr | None = None,
        bundle_sids: str | None = None,
        friendly_name: str | None = None,
        regulation_sid: str | None = None,
        iso_country: str | None = None,
        number_type: str | None = None,
        end_user_type: BundleEnumEndUserTypeOrStr | None = None,
        has_valid_until_date: bool | None = None,
        sort_by: BundleEnumSortByOrStr | None = None,
        sort_direction: BundleEnumSortDirectionOrStr | None = None,
        valid_until_date: RFC3339DateTime | None = None,
        valid_until_date_query: RFC3339DateTime | None = None,
        valid_until_date_query_query: RFC3339DateTime | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListBundleResponse, RawError]:
        """Retrieve a list of all Bundles for an account.

        Args:
            status: The verification status of the Bundle resource. Please refer to `Bundle Statuses
                <https://www.twilio.com/docs/phone-numbers/regulatory/api/bundles#bundle-statuses>`__ for more details.
            bundle_sids: A comma-separated list of Bundle SIDs to filter the results (maximum 20). Each Bundle SID must
                match ``^BU[0-9a-fA-F]{32}$``.
            friendly_name: The string that you assigned to describe the resource. The column can contain 255 variable
                characters.
            regulation_sid: The unique string of a `Regulation resource
                <https://www.twilio.com/docs/phone-numbers/regulatory/api/regulations>`__ that is associated to the
                Bundle resource.
            iso_country: The 2-digit `ISO country code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ of the
                Bundle's phone number country ownership request.
            number_type: The type of phone number of the Bundle's ownership request. Can be ``local``, ``mobile``,
                ``national``, or ``toll-free``.
            end_user_type: The end user type of the regulation of the Bundle. Can be ``business`` or ``individual``.
            has_valid_until_date: Indicates that the Bundle is a valid Bundle until a specified expiration date.
            sort_by: Can be ``valid-until`` or ``date-updated``. Defaults to ``date-created``.
            sort_direction: Default is ``DESC``. Can be ``ASC`` or ``DESC``.
            valid_until_date: Date to filter Bundles having their ``valid_until_date`` before or after the specified
                date. Can be ``ValidUntilDate>=`` or ``ValidUntilDate<=``. Both can be used in conjunction as well. `ISO
                8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ is the acceptable date format.
            valid_until_date_query: Date to filter Bundles having their ``valid_until_date`` before or after the
                specified date. Can be ``ValidUntilDate>=`` or ``ValidUntilDate<=``. Both can be used in conjunction as
                well. `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ is the acceptable date format.
            valid_until_date_query_query: Date to filter Bundles having their ``valid_until_date`` before or after the
                specified date. Can be ``ValidUntilDate>=`` or ``ValidUntilDate<=``. Both can be used in conjunction as
                well. `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ is the acceptable date format.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/RegulatoryCompliance/Bundles"),
            query_params=[
                param[BundleEnumStatusOrStr | None]("Status", status),
                param[str | None]("BundleSids", bundle_sids),
                param[str | None]("FriendlyName", friendly_name),
                param[str | None]("RegulationSid", regulation_sid),
                param[str | None]("IsoCountry", iso_country),
                param[str | None]("NumberType", number_type),
                param[BundleEnumEndUserTypeOrStr | None]("EndUserType", end_user_type),
                param[bool | None]("HasValidUntilDate", has_valid_until_date),
                param[BundleEnumSortByOrStr | None]("SortBy", sort_by),
                param[BundleEnumSortDirectionOrStr | None]("SortDirection", sort_direction),
                param[RFC3339DateTime | None]("ValidUntilDate", valid_until_date),
                param[RFC3339DateTime | None]("ValidUntilDate<", valid_until_date_query),
                param[RFC3339DateTime | None]("ValidUntilDate>", valid_until_date_query_query),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListBundleResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_bundle(
        self,
        sid: str,
        *,
        status: BundleEnumStatusOrStr | None = None,
        status_callback: AnyUrl | None = None,
        friendly_name: str | None = None,
        email: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[NumbersV2RegulatoryComplianceBundle, RawError]:
        """Updates a Bundle in an account.

        Args:
            sid: The unique string that we created to identify the Bundle resource.
            status: The verification status of the Bundle resource.
            status_callback: The URL we call to inform your application of status changes.
            friendly_name: The string that you assigned to describe the resource.
            email: The email address that will receive updates when the Bundle resource changes status.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v2/RegulatoryCompliance/Bundles/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            body=form_body(
                [
                    param[BundleEnumStatusOrStr | None]("Status", status),
                    param[AnyUrl | None]("StatusCallback", status_callback),
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("Email", email),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2RegulatoryComplianceBundle],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncNumbersV2BundleWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_bundle(
        self,
        friendly_name: str,
        email: str,
        *,
        status_callback: AnyUrl | None = None,
        regulation_sid: str | None = None,
        iso_country: str | None = None,
        end_user_type: BundleEnumEndUserTypeOrStr | None = None,
        number_type: str | None = None,
        is_test: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[NumbersV2RegulatoryComplianceBundle, RawError]:
        """Create a new Bundle.

        Args:
            friendly_name: The string that you assigned to describe the resource.
            email: The email address that will receive updates when the Bundle resource changes status.
            status_callback: The URL we call to inform your application of status changes.
            regulation_sid: The unique string of a regulation that is associated to the Bundle resource.
            iso_country: The `ISO country code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ of the Bundle's
                phone number country ownership request.
            end_user_type: Value sent with the request.
            number_type: The type of phone number of the Bundle's ownership request. Can be ``local``, ``mobile``,
                ``national``, or ``toll-free``.
            is_test: Indicates that Bundle is a Test Bundle and will be Auto-Rejected
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v2/RegulatoryCompliance/Bundles"),
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[str]("Email", email),
                    param[AnyUrl | None]("StatusCallback", status_callback),
                    param[str | None]("RegulationSid", regulation_sid),
                    param[str | None]("IsoCountry", iso_country),
                    param[BundleEnumEndUserTypeOrStr | None]("EndUserType", end_user_type),
                    param[str | None]("NumberType", number_type),
                    param[bool | None]("IsTest", is_test),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2RegulatoryComplianceBundle],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_bundle(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Bundle.

        Args:
            sid: The unique string that we created to identify the Bundle resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default5("/v2/RegulatoryCompliance/Bundles/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_bundle(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV2RegulatoryComplianceBundle, RawError]:
        """Fetch a specific Bundle instance.

        Args:
            sid: The unique string that we created to identify the Bundle resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/RegulatoryCompliance/Bundles/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2RegulatoryComplianceBundle],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_bundle(
        self,
        *,
        status: BundleEnumStatusOrStr | None = None,
        bundle_sids: str | None = None,
        friendly_name: str | None = None,
        regulation_sid: str | None = None,
        iso_country: str | None = None,
        number_type: str | None = None,
        end_user_type: BundleEnumEndUserTypeOrStr | None = None,
        has_valid_until_date: bool | None = None,
        sort_by: BundleEnumSortByOrStr | None = None,
        sort_direction: BundleEnumSortDirectionOrStr | None = None,
        valid_until_date: RFC3339DateTime | None = None,
        valid_until_date_query: RFC3339DateTime | None = None,
        valid_until_date_query_query: RFC3339DateTime | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListBundleResponse, RawError]:
        """Retrieve a list of all Bundles for an account.

        Args:
            status: The verification status of the Bundle resource. Please refer to `Bundle Statuses
                <https://www.twilio.com/docs/phone-numbers/regulatory/api/bundles#bundle-statuses>`__ for more details.
            bundle_sids: A comma-separated list of Bundle SIDs to filter the results (maximum 20). Each Bundle SID must
                match ``^BU[0-9a-fA-F]{32}$``.
            friendly_name: The string that you assigned to describe the resource. The column can contain 255 variable
                characters.
            regulation_sid: The unique string of a `Regulation resource
                <https://www.twilio.com/docs/phone-numbers/regulatory/api/regulations>`__ that is associated to the
                Bundle resource.
            iso_country: The 2-digit `ISO country code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ of the
                Bundle's phone number country ownership request.
            number_type: The type of phone number of the Bundle's ownership request. Can be ``local``, ``mobile``,
                ``national``, or ``toll-free``.
            end_user_type: The end user type of the regulation of the Bundle. Can be ``business`` or ``individual``.
            has_valid_until_date: Indicates that the Bundle is a valid Bundle until a specified expiration date.
            sort_by: Can be ``valid-until`` or ``date-updated``. Defaults to ``date-created``.
            sort_direction: Default is ``DESC``. Can be ``ASC`` or ``DESC``.
            valid_until_date: Date to filter Bundles having their ``valid_until_date`` before or after the specified
                date. Can be ``ValidUntilDate>=`` or ``ValidUntilDate<=``. Both can be used in conjunction as well. `ISO
                8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ is the acceptable date format.
            valid_until_date_query: Date to filter Bundles having their ``valid_until_date`` before or after the
                specified date. Can be ``ValidUntilDate>=`` or ``ValidUntilDate<=``. Both can be used in conjunction as
                well. `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ is the acceptable date format.
            valid_until_date_query_query: Date to filter Bundles having their ``valid_until_date`` before or after the
                specified date. Can be ``ValidUntilDate>=`` or ``ValidUntilDate<=``. Both can be used in conjunction as
                well. `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ is the acceptable date format.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/RegulatoryCompliance/Bundles"),
            query_params=[
                param[BundleEnumStatusOrStr | None]("Status", status),
                param[str | None]("BundleSids", bundle_sids),
                param[str | None]("FriendlyName", friendly_name),
                param[str | None]("RegulationSid", regulation_sid),
                param[str | None]("IsoCountry", iso_country),
                param[str | None]("NumberType", number_type),
                param[BundleEnumEndUserTypeOrStr | None]("EndUserType", end_user_type),
                param[bool | None]("HasValidUntilDate", has_valid_until_date),
                param[BundleEnumSortByOrStr | None]("SortBy", sort_by),
                param[BundleEnumSortDirectionOrStr | None]("SortDirection", sort_direction),
                param[RFC3339DateTime | None]("ValidUntilDate", valid_until_date),
                param[RFC3339DateTime | None]("ValidUntilDate<", valid_until_date_query),
                param[RFC3339DateTime | None]("ValidUntilDate>", valid_until_date_query_query),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListBundleResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_bundle(
        self,
        sid: str,
        *,
        status: BundleEnumStatusOrStr | None = None,
        status_callback: AnyUrl | None = None,
        friendly_name: str | None = None,
        email: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[NumbersV2RegulatoryComplianceBundle, RawError]:
        """Updates a Bundle in an account.

        Args:
            sid: The unique string that we created to identify the Bundle resource.
            status: The verification status of the Bundle resource.
            status_callback: The URL we call to inform your application of status changes.
            friendly_name: The string that you assigned to describe the resource.
            email: The email address that will receive updates when the Bundle resource changes status.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v2/RegulatoryCompliance/Bundles/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            body=form_body(
                [
                    param[BundleEnumStatusOrStr | None]("Status", status),
                    param[AnyUrl | None]("StatusCallback", status_callback),
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("Email", email),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2RegulatoryComplianceBundle],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
