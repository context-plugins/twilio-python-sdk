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
from ..models.list_trust_product_evaluation_response import ListTrustProductEvaluationResponse
from ..models.trusthub_v1_trust_product_trust_product_evaluation import TrusthubV1TrustProductTrustProductEvaluation
from ..server.server import Server


class TrusthubV1TrustProductsEvaluations:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TrusthubV1TrustProductsEvaluationsWithRawResponse(client, server, auth)

    def create_trust_product_evaluation(
        self, trust_product_sid: str, policy_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TrusthubV1TrustProductTrustProductEvaluation:
        """Create a new Evaluation

        Args:
            trust_product_sid: The unique string that we created to identify the trust_product resource.
            policy_sid: The unique string of a policy that is associated to the customer_profile resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_trust_product_evaluation(
            trust_product_sid, policy_sid, request_options=request_options
        ).unwrap()

    def fetch_trust_product_evaluation(
        self, trust_product_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TrusthubV1TrustProductTrustProductEvaluation:
        """Fetch specific Evaluation Instance.

        Args:
            trust_product_sid: The unique string that we created to identify the trust_product resource.
            sid: The unique string that identifies the Evaluation resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_trust_product_evaluation(
            trust_product_sid, sid, request_options=request_options
        ).unwrap()

    def list_trust_product_evaluation(
        self,
        trust_product_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListTrustProductEvaluationResponse:
        """Retrieve a list of Evaluations associated to the trust_product resource.

        Args:
            trust_product_sid: The unique string that we created to identify the trust_product resource.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_trust_product_evaluation(
            trust_product_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> TrusthubV1TrustProductsEvaluationsWithRawResponse:
        return self._with_raw_response


class AsyncTrusthubV1TrustProductsEvaluations:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTrusthubV1TrustProductsEvaluationsWithRawResponse(client, server, auth)

    async def create_trust_product_evaluation(
        self, trust_product_sid: str, policy_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TrusthubV1TrustProductTrustProductEvaluation:
        """Create a new Evaluation

        Args:
            trust_product_sid: The unique string that we created to identify the trust_product resource.
            policy_sid: The unique string of a policy that is associated to the customer_profile resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_trust_product_evaluation(
                trust_product_sid, policy_sid, request_options=request_options
            )
        ).unwrap()

    async def fetch_trust_product_evaluation(
        self, trust_product_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TrusthubV1TrustProductTrustProductEvaluation:
        """Fetch specific Evaluation Instance.

        Args:
            trust_product_sid: The unique string that we created to identify the trust_product resource.
            sid: The unique string that identifies the Evaluation resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_trust_product_evaluation(
                trust_product_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def list_trust_product_evaluation(
        self,
        trust_product_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListTrustProductEvaluationResponse:
        """Retrieve a list of Evaluations associated to the trust_product resource.

        Args:
            trust_product_sid: The unique string that we created to identify the trust_product resource.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_trust_product_evaluation(
                trust_product_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTrusthubV1TrustProductsEvaluationsWithRawResponse:
        return self._with_raw_response


class TrusthubV1TrustProductsEvaluationsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_trust_product_evaluation(
        self, trust_product_sid: str, policy_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TrusthubV1TrustProductTrustProductEvaluation, RawError]:
        """Create a new Evaluation

        Args:
            trust_product_sid: The unique string that we created to identify the trust_product resource.
            policy_sid: The unique string of a policy that is associated to the customer_profile resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/v1/TrustProducts/{TrustProductSid}/Evaluations"),
            path_params=[param[str]("TrustProductSid", trust_product_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str]("PolicySid", policy_sid)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1TrustProductTrustProductEvaluation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_trust_product_evaluation(
        self, trust_product_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TrusthubV1TrustProductTrustProductEvaluation, RawError]:
        """Fetch specific Evaluation Instance.

        Args:
            trust_product_sid: The unique string that we created to identify the trust_product resource.
            sid: The unique string that identifies the Evaluation resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/v1/TrustProducts/{TrustProductSid}/Evaluations/{Sid}"),
            path_params=[param[str]("TrustProductSid", trust_product_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1TrustProductTrustProductEvaluation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_trust_product_evaluation(
        self,
        trust_product_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListTrustProductEvaluationResponse, RawError]:
        """Retrieve a list of Evaluations associated to the trust_product resource.

        Args:
            trust_product_sid: The unique string that we created to identify the trust_product resource.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/v1/TrustProducts/{TrustProductSid}/Evaluations"),
            path_params=[param[str]("TrustProductSid", trust_product_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListTrustProductEvaluationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTrusthubV1TrustProductsEvaluationsWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def create_trust_product_evaluation(
        self, trust_product_sid: str, policy_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TrusthubV1TrustProductTrustProductEvaluation, RawError]:
        """Create a new Evaluation

        Args:
            trust_product_sid: The unique string that we created to identify the trust_product resource.
            policy_sid: The unique string of a policy that is associated to the customer_profile resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/v1/TrustProducts/{TrustProductSid}/Evaluations"),
            path_params=[param[str]("TrustProductSid", trust_product_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str]("PolicySid", policy_sid)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1TrustProductTrustProductEvaluation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_trust_product_evaluation(
        self, trust_product_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TrusthubV1TrustProductTrustProductEvaluation, RawError]:
        """Fetch specific Evaluation Instance.

        Args:
            trust_product_sid: The unique string that we created to identify the trust_product resource.
            sid: The unique string that identifies the Evaluation resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/v1/TrustProducts/{TrustProductSid}/Evaluations/{Sid}"),
            path_params=[param[str]("TrustProductSid", trust_product_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TrusthubV1TrustProductTrustProductEvaluation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_trust_product_evaluation(
        self,
        trust_product_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListTrustProductEvaluationResponse, RawError]:
        """Retrieve a list of Evaluations associated to the trust_product resource.

        Args:
            trust_product_sid: The unique string that we created to identify the trust_product resource.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/v1/TrustProducts/{TrustProductSid}/Evaluations"),
            path_params=[param[str]("TrustProductSid", trust_product_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListTrustProductEvaluationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
