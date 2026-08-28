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
from ..models.insights_v1_conference import InsightsV1Conference
from ..models.list_conference_response1 import ListConferenceResponse1
from ..server.server import Server


class InsightsV1ConferenceApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = InsightsV1ConferenceApiWithRawResponse(client, server, auth)

    def fetch_conference2(
        self, conference_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> InsightsV1Conference:
        """Get a specific Conference Summary.

        Args:
            conference_sid: The unique SID identifier of the Conference.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_conference2(conference_sid, request_options=request_options).unwrap()

    def list_conference2(
        self,
        *,
        conference_sid: str | None = None,
        friendly_name: str | None = None,
        status: str | None = None,
        created_after: str | None = None,
        created_before: str | None = None,
        mixer_region: str | None = None,
        tags: str | None = None,
        subaccount: str | None = None,
        detected_issues: str | None = None,
        end_reason: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListConferenceResponse1:
        """Get a list of Conference Summaries.

        Args:
            conference_sid: The SID of the conference.
            friendly_name: Custom label for the conference resource, up to 64 characters.
            status: Conference status.
            created_after: Conferences created after the provided timestamp specified in ISO 8601 format
            created_before: Conferences created before the provided timestamp specified in ISO 8601 format.
            mixer_region: Twilio region where the conference media was mixed.
            tags: Tags applied by Twilio for common potential configuration, quality, or performance issues.
            subaccount: Account SID for the subaccount whose resources you wish to retrieve.
            detected_issues: Potential configuration, behavior, or performance issues detected during the conference.
            end_reason: Conference end reason; e.g. last participant left, modified by API, etc.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_conference2(
            conference_sid=conference_sid,
            friendly_name=friendly_name,
            status=status,
            created_after=created_after,
            created_before=created_before,
            mixer_region=mixer_region,
            tags=tags,
            subaccount=subaccount,
            detected_issues=detected_issues,
            end_reason=end_reason,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> InsightsV1ConferenceApiWithRawResponse:
        return self._with_raw_response


class AsyncInsightsV1ConferenceApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncInsightsV1ConferenceApiWithRawResponse(client, server, auth)

    async def fetch_conference2(
        self, conference_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> InsightsV1Conference:
        """Get a specific Conference Summary.

        Args:
            conference_sid: The unique SID identifier of the Conference.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_conference2(conference_sid, request_options=request_options)
        ).unwrap()

    async def list_conference2(
        self,
        *,
        conference_sid: str | None = None,
        friendly_name: str | None = None,
        status: str | None = None,
        created_after: str | None = None,
        created_before: str | None = None,
        mixer_region: str | None = None,
        tags: str | None = None,
        subaccount: str | None = None,
        detected_issues: str | None = None,
        end_reason: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListConferenceResponse1:
        """Get a list of Conference Summaries.

        Args:
            conference_sid: The SID of the conference.
            friendly_name: Custom label for the conference resource, up to 64 characters.
            status: Conference status.
            created_after: Conferences created after the provided timestamp specified in ISO 8601 format
            created_before: Conferences created before the provided timestamp specified in ISO 8601 format.
            mixer_region: Twilio region where the conference media was mixed.
            tags: Tags applied by Twilio for common potential configuration, quality, or performance issues.
            subaccount: Account SID for the subaccount whose resources you wish to retrieve.
            detected_issues: Potential configuration, behavior, or performance issues detected during the conference.
            end_reason: Conference end reason; e.g. last participant left, modified by API, etc.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_conference2(
                conference_sid=conference_sid,
                friendly_name=friendly_name,
                status=status,
                created_after=created_after,
                created_before=created_before,
                mixer_region=mixer_region,
                tags=tags,
                subaccount=subaccount,
                detected_issues=detected_issues,
                end_reason=end_reason,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncInsightsV1ConferenceApiWithRawResponse:
        return self._with_raw_response


class InsightsV1ConferenceApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_conference2(
        self, conference_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InsightsV1Conference, RawError]:
        """Get a specific Conference Summary.

        Args:
            conference_sid: The unique SID identifier of the Conference.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/v1/Conferences/{ConferenceSid}"),
            path_params=[param[str]("ConferenceSid", conference_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[InsightsV1Conference],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_conference2(
        self,
        *,
        conference_sid: str | None = None,
        friendly_name: str | None = None,
        status: str | None = None,
        created_after: str | None = None,
        created_before: str | None = None,
        mixer_region: str | None = None,
        tags: str | None = None,
        subaccount: str | None = None,
        detected_issues: str | None = None,
        end_reason: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListConferenceResponse1, RawError]:
        """Get a list of Conference Summaries.

        Args:
            conference_sid: The SID of the conference.
            friendly_name: Custom label for the conference resource, up to 64 characters.
            status: Conference status.
            created_after: Conferences created after the provided timestamp specified in ISO 8601 format
            created_before: Conferences created before the provided timestamp specified in ISO 8601 format.
            mixer_region: Twilio region where the conference media was mixed.
            tags: Tags applied by Twilio for common potential configuration, quality, or performance issues.
            subaccount: Account SID for the subaccount whose resources you wish to retrieve.
            detected_issues: Potential configuration, behavior, or performance issues detected during the conference.
            end_reason: Conference end reason; e.g. last participant left, modified by API, etc.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/v1/Conferences"),
            query_params=[
                param[str | None]("ConferenceSid", conference_sid),
                param[str | None]("FriendlyName", friendly_name),
                param[str | None]("Status", status),
                param[str | None]("CreatedAfter", created_after),
                param[str | None]("CreatedBefore", created_before),
                param[str | None]("MixerRegion", mixer_region),
                param[str | None]("Tags", tags),
                param[str | None]("Subaccount", subaccount),
                param[str | None]("DetectedIssues", detected_issues),
                param[str | None]("EndReason", end_reason),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListConferenceResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncInsightsV1ConferenceApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_conference2(
        self, conference_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InsightsV1Conference, RawError]:
        """Get a specific Conference Summary.

        Args:
            conference_sid: The unique SID identifier of the Conference.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/v1/Conferences/{ConferenceSid}"),
            path_params=[param[str]("ConferenceSid", conference_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[InsightsV1Conference],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_conference2(
        self,
        *,
        conference_sid: str | None = None,
        friendly_name: str | None = None,
        status: str | None = None,
        created_after: str | None = None,
        created_before: str | None = None,
        mixer_region: str | None = None,
        tags: str | None = None,
        subaccount: str | None = None,
        detected_issues: str | None = None,
        end_reason: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListConferenceResponse1, RawError]:
        """Get a list of Conference Summaries.

        Args:
            conference_sid: The SID of the conference.
            friendly_name: Custom label for the conference resource, up to 64 characters.
            status: Conference status.
            created_after: Conferences created after the provided timestamp specified in ISO 8601 format
            created_before: Conferences created before the provided timestamp specified in ISO 8601 format.
            mixer_region: Twilio region where the conference media was mixed.
            tags: Tags applied by Twilio for common potential configuration, quality, or performance issues.
            subaccount: Account SID for the subaccount whose resources you wish to retrieve.
            detected_issues: Potential configuration, behavior, or performance issues detected during the conference.
            end_reason: Conference end reason; e.g. last participant left, modified by API, etc.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/v1/Conferences"),
            query_params=[
                param[str | None]("ConferenceSid", conference_sid),
                param[str | None]("FriendlyName", friendly_name),
                param[str | None]("Status", status),
                param[str | None]("CreatedAfter", created_after),
                param[str | None]("CreatedBefore", created_before),
                param[str | None]("MixerRegion", mixer_region),
                param[str | None]("Tags", tags),
                param[str | None]("Subaccount", subaccount),
                param[str | None]("DetectedIssues", detected_issues),
                param[str | None]("EndReason", end_reason),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListConferenceResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
