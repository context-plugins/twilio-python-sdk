from __future__ import annotations

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
from ..models.enums.annotation_enum_answered_by import AnnotationEnumAnsweredByOrStr
from ..models.enums.annotation_enum_connectivity_issue import AnnotationEnumConnectivityIssueOrStr
from ..models.insights_v1_call_annotation import InsightsV1CallAnnotation
from ..server.server import Server


class InsightsV1Annotation:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = InsightsV1AnnotationWithRawResponse(client, server, auth)

    def fetch_annotation(
        self, call_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> InsightsV1CallAnnotation:
        """Get the Annotation for a specific Call.

        Args:
            call_sid: The unique SID identifier of the Call.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_annotation(call_sid, request_options=request_options).unwrap()

    def update_annotation(
        self,
        call_sid: str,
        *,
        answered_by: AnnotationEnumAnsweredByOrStr | None = None,
        connectivity_issue: AnnotationEnumConnectivityIssueOrStr | None = None,
        quality_issues: str | None = None,
        spam: bool | None = None,
        call_score: int | None = None,
        comment: str | None = None,
        incident: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> InsightsV1CallAnnotation:
        """Update an Annotation for a specific Call.

        Args:
            call_sid: The unique string that Twilio created to identify this Call resource. It always starts with a CA.
            answered_by: Value sent with the request.
            connectivity_issue: Value sent with the request.
            quality_issues: Specify if the call had any subjective quality issues. Possible values, one or more of
                ``no_quality_issue``, ``low_volume``, ``choppy_robotic``, ``echo``, ``dtmf``, ``latency``, ``owa``,
                ``static_noise``. Use comma separated values to indicate multiple quality issues for the same call.
            spam: A boolean flag to indicate if the call was a spam call. Use this to provide feedback on whether calls
                placed from your account were marked as spam, or if inbound calls received by your account were unwanted
                spam. Use ``true`` if the call was a spam call.
            call_score: Specify the call score. This is of type integer. Use a range of 1-5 to indicate the call
                experience score, with the following mapping as a reference for rating the call [5: Excellent, 4: Good,
                3 : Fair, 2 : Poor, 1: Bad].
            comment: Specify any comments pertaining to the call. ``comment`` has a maximum character limit of 100.
                Twilio does not treat this field as PII, so no PII should be included in the ``comment``.
            incident: Associate this call with an incident or support ticket. The ``incident`` parameter is of type
                string with a maximum character limit of 100. Twilio does not treat this field as PII, so no PII should
                be included in ``incident``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_annotation(
            call_sid,
            answered_by=answered_by,
            connectivity_issue=connectivity_issue,
            quality_issues=quality_issues,
            spam=spam,
            call_score=call_score,
            comment=comment,
            incident=incident,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> InsightsV1AnnotationWithRawResponse:
        return self._with_raw_response


class AsyncInsightsV1Annotation:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncInsightsV1AnnotationWithRawResponse(client, server, auth)

    async def fetch_annotation(
        self, call_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> InsightsV1CallAnnotation:
        """Get the Annotation for a specific Call.

        Args:
            call_sid: The unique SID identifier of the Call.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_annotation(call_sid, request_options=request_options)).unwrap()

    async def update_annotation(
        self,
        call_sid: str,
        *,
        answered_by: AnnotationEnumAnsweredByOrStr | None = None,
        connectivity_issue: AnnotationEnumConnectivityIssueOrStr | None = None,
        quality_issues: str | None = None,
        spam: bool | None = None,
        call_score: int | None = None,
        comment: str | None = None,
        incident: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> InsightsV1CallAnnotation:
        """Update an Annotation for a specific Call.

        Args:
            call_sid: The unique string that Twilio created to identify this Call resource. It always starts with a CA.
            answered_by: Value sent with the request.
            connectivity_issue: Value sent with the request.
            quality_issues: Specify if the call had any subjective quality issues. Possible values, one or more of
                ``no_quality_issue``, ``low_volume``, ``choppy_robotic``, ``echo``, ``dtmf``, ``latency``, ``owa``,
                ``static_noise``. Use comma separated values to indicate multiple quality issues for the same call.
            spam: A boolean flag to indicate if the call was a spam call. Use this to provide feedback on whether calls
                placed from your account were marked as spam, or if inbound calls received by your account were unwanted
                spam. Use ``true`` if the call was a spam call.
            call_score: Specify the call score. This is of type integer. Use a range of 1-5 to indicate the call
                experience score, with the following mapping as a reference for rating the call [5: Excellent, 4: Good,
                3 : Fair, 2 : Poor, 1: Bad].
            comment: Specify any comments pertaining to the call. ``comment`` has a maximum character limit of 100.
                Twilio does not treat this field as PII, so no PII should be included in the ``comment``.
            incident: Associate this call with an incident or support ticket. The ``incident`` parameter is of type
                string with a maximum character limit of 100. Twilio does not treat this field as PII, so no PII should
                be included in ``incident``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_annotation(
                call_sid,
                answered_by=answered_by,
                connectivity_issue=connectivity_issue,
                quality_issues=quality_issues,
                spam=spam,
                call_score=call_score,
                comment=comment,
                incident=incident,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncInsightsV1AnnotationWithRawResponse:
        return self._with_raw_response


class InsightsV1AnnotationWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_annotation(
        self, call_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InsightsV1CallAnnotation, RawError]:
        """Get the Annotation for a specific Call.

        Args:
            call_sid: The unique SID identifier of the Call.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/v1/Voice/{CallSid}/Annotation"),
            path_params=[param[str]("CallSid", call_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[InsightsV1CallAnnotation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_annotation(
        self,
        call_sid: str,
        *,
        answered_by: AnnotationEnumAnsweredByOrStr | None = None,
        connectivity_issue: AnnotationEnumConnectivityIssueOrStr | None = None,
        quality_issues: str | None = None,
        spam: bool | None = None,
        call_score: int | None = None,
        comment: str | None = None,
        incident: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[InsightsV1CallAnnotation, RawError]:
        """Update an Annotation for a specific Call.

        Args:
            call_sid: The unique string that Twilio created to identify this Call resource. It always starts with a CA.
            answered_by: Value sent with the request.
            connectivity_issue: Value sent with the request.
            quality_issues: Specify if the call had any subjective quality issues. Possible values, one or more of
                ``no_quality_issue``, ``low_volume``, ``choppy_robotic``, ``echo``, ``dtmf``, ``latency``, ``owa``,
                ``static_noise``. Use comma separated values to indicate multiple quality issues for the same call.
            spam: A boolean flag to indicate if the call was a spam call. Use this to provide feedback on whether calls
                placed from your account were marked as spam, or if inbound calls received by your account were unwanted
                spam. Use ``true`` if the call was a spam call.
            call_score: Specify the call score. This is of type integer. Use a range of 1-5 to indicate the call
                experience score, with the following mapping as a reference for rating the call [5: Excellent, 4: Good,
                3 : Fair, 2 : Poor, 1: Bad].
            comment: Specify any comments pertaining to the call. ``comment`` has a maximum character limit of 100.
                Twilio does not treat this field as PII, so no PII should be included in the ``comment``.
            incident: Associate this call with an incident or support ticket. The ``incident`` parameter is of type
                string with a maximum character limit of 100. Twilio does not treat this field as PII, so no PII should
                be included in ``incident``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default14("/v1/Voice/{CallSid}/Annotation"),
            path_params=[param[str]("CallSid", call_sid)],
            body=form_body(
                [
                    param[AnnotationEnumAnsweredByOrStr | None]("AnsweredBy", answered_by),
                    param[AnnotationEnumConnectivityIssueOrStr | None]("ConnectivityIssue", connectivity_issue),
                    param[str | None]("QualityIssues", quality_issues),
                    param[bool | None]("Spam", spam),
                    param[int | None]("CallScore", call_score),
                    param[str | None]("Comment", comment),
                    param[str | None]("Incident", incident),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[InsightsV1CallAnnotation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncInsightsV1AnnotationWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_annotation(
        self, call_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InsightsV1CallAnnotation, RawError]:
        """Get the Annotation for a specific Call.

        Args:
            call_sid: The unique SID identifier of the Call.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/v1/Voice/{CallSid}/Annotation"),
            path_params=[param[str]("CallSid", call_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[InsightsV1CallAnnotation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_annotation(
        self,
        call_sid: str,
        *,
        answered_by: AnnotationEnumAnsweredByOrStr | None = None,
        connectivity_issue: AnnotationEnumConnectivityIssueOrStr | None = None,
        quality_issues: str | None = None,
        spam: bool | None = None,
        call_score: int | None = None,
        comment: str | None = None,
        incident: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[InsightsV1CallAnnotation, RawError]:
        """Update an Annotation for a specific Call.

        Args:
            call_sid: The unique string that Twilio created to identify this Call resource. It always starts with a CA.
            answered_by: Value sent with the request.
            connectivity_issue: Value sent with the request.
            quality_issues: Specify if the call had any subjective quality issues. Possible values, one or more of
                ``no_quality_issue``, ``low_volume``, ``choppy_robotic``, ``echo``, ``dtmf``, ``latency``, ``owa``,
                ``static_noise``. Use comma separated values to indicate multiple quality issues for the same call.
            spam: A boolean flag to indicate if the call was a spam call. Use this to provide feedback on whether calls
                placed from your account were marked as spam, or if inbound calls received by your account were unwanted
                spam. Use ``true`` if the call was a spam call.
            call_score: Specify the call score. This is of type integer. Use a range of 1-5 to indicate the call
                experience score, with the following mapping as a reference for rating the call [5: Excellent, 4: Good,
                3 : Fair, 2 : Poor, 1: Bad].
            comment: Specify any comments pertaining to the call. ``comment`` has a maximum character limit of 100.
                Twilio does not treat this field as PII, so no PII should be included in the ``comment``.
            incident: Associate this call with an incident or support ticket. The ``incident`` parameter is of type
                string with a maximum character limit of 100. Twilio does not treat this field as PII, so no PII should
                be included in ``incident``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default14("/v1/Voice/{CallSid}/Annotation"),
            path_params=[param[str]("CallSid", call_sid)],
            body=form_body(
                [
                    param[AnnotationEnumAnsweredByOrStr | None]("AnsweredBy", answered_by),
                    param[AnnotationEnumConnectivityIssueOrStr | None]("ConnectivityIssue", connectivity_issue),
                    param[str | None]("QualityIssues", quality_issues),
                    param[bool | None]("Spam", spam),
                    param[int | None]("CallScore", call_score),
                    param[str | None]("Comment", comment),
                    param[str | None]("Incident", incident),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[InsightsV1CallAnnotation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
