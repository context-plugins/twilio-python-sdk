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
from ..models.list_evaluation_response import ListEvaluationResponse
from ..models.numbers_v2_regulatory_compliance_bundle_evaluation import NumbersV2RegulatoryComplianceBundleEvaluation
from ..server.server import Server


class NumbersV2Evaluation:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NumbersV2EvaluationWithRawResponse(client, server, auth)

    def create_evaluation(
        self, bundle_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV2RegulatoryComplianceBundleEvaluation:
        """Creates an evaluation for a bundle

        Args:
            bundle_sid: The unique string that identifies the Bundle resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_evaluation(bundle_sid, request_options=request_options).unwrap()

    def fetch_evaluation(
        self, bundle_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV2RegulatoryComplianceBundleEvaluation:
        """Fetch specific Evaluation Instance.

        Args:
            bundle_sid: The unique string that we created to identify the Bundle resource.
            sid: The unique string that identifies the Evaluation resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_evaluation(bundle_sid, sid, request_options=request_options).unwrap()

    def list_evaluation(
        self,
        bundle_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListEvaluationResponse:
        """Retrieve a list of Evaluations associated to the Bundle resource.

        Args:
            bundle_sid: The unique string that identifies the Bundle resource.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_evaluation(
            bundle_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> NumbersV2EvaluationWithRawResponse:
        return self._with_raw_response


class AsyncNumbersV2Evaluation:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNumbersV2EvaluationWithRawResponse(client, server, auth)

    async def create_evaluation(
        self, bundle_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV2RegulatoryComplianceBundleEvaluation:
        """Creates an evaluation for a bundle

        Args:
            bundle_sid: The unique string that identifies the Bundle resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_evaluation(bundle_sid, request_options=request_options)).unwrap()

    async def fetch_evaluation(
        self, bundle_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV2RegulatoryComplianceBundleEvaluation:
        """Fetch specific Evaluation Instance.

        Args:
            bundle_sid: The unique string that we created to identify the Bundle resource.
            sid: The unique string that identifies the Evaluation resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_evaluation(bundle_sid, sid, request_options=request_options)
        ).unwrap()

    async def list_evaluation(
        self,
        bundle_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListEvaluationResponse:
        """Retrieve a list of Evaluations associated to the Bundle resource.

        Args:
            bundle_sid: The unique string that identifies the Bundle resource.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_evaluation(
                bundle_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncNumbersV2EvaluationWithRawResponse:
        return self._with_raw_response


class NumbersV2EvaluationWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_evaluation(
        self, bundle_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV2RegulatoryComplianceBundleEvaluation, RawError]:
        """Creates an evaluation for a bundle

        Args:
            bundle_sid: The unique string that identifies the Bundle resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v2/RegulatoryCompliance/Bundles/{BundleSid}/Evaluations"),
            path_params=[param[str]("BundleSid", bundle_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2RegulatoryComplianceBundleEvaluation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_evaluation(
        self, bundle_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV2RegulatoryComplianceBundleEvaluation, RawError]:
        """Fetch specific Evaluation Instance.

        Args:
            bundle_sid: The unique string that we created to identify the Bundle resource.
            sid: The unique string that identifies the Evaluation resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/RegulatoryCompliance/Bundles/{BundleSid}/Evaluations/{Sid}"),
            path_params=[param[str]("BundleSid", bundle_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2RegulatoryComplianceBundleEvaluation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_evaluation(
        self,
        bundle_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListEvaluationResponse, RawError]:
        """Retrieve a list of Evaluations associated to the Bundle resource.

        Args:
            bundle_sid: The unique string that identifies the Bundle resource.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/RegulatoryCompliance/Bundles/{BundleSid}/Evaluations"),
            path_params=[param[str]("BundleSid", bundle_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListEvaluationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncNumbersV2EvaluationWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_evaluation(
        self, bundle_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV2RegulatoryComplianceBundleEvaluation, RawError]:
        """Creates an evaluation for a bundle

        Args:
            bundle_sid: The unique string that identifies the Bundle resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v2/RegulatoryCompliance/Bundles/{BundleSid}/Evaluations"),
            path_params=[param[str]("BundleSid", bundle_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2RegulatoryComplianceBundleEvaluation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_evaluation(
        self, bundle_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV2RegulatoryComplianceBundleEvaluation, RawError]:
        """Fetch specific Evaluation Instance.

        Args:
            bundle_sid: The unique string that we created to identify the Bundle resource.
            sid: The unique string that identifies the Evaluation resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/RegulatoryCompliance/Bundles/{BundleSid}/Evaluations/{Sid}"),
            path_params=[param[str]("BundleSid", bundle_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2RegulatoryComplianceBundleEvaluation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_evaluation(
        self,
        bundle_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListEvaluationResponse, RawError]:
        """Retrieve a list of Evaluations associated to the Bundle resource.

        Args:
            bundle_sid: The unique string that identifies the Bundle resource.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/RegulatoryCompliance/Bundles/{BundleSid}/Evaluations"),
            path_params=[param[str]("BundleSid", bundle_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListEvaluationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
