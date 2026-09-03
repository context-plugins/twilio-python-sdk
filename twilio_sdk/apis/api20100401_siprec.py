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
from ..models.api_v2010_account_call_siprec import ApiV2010AccountCallSiprec
from ..models.enums.siprec_enum_track import SiprecEnumTrackOrStr
from ..models.enums.siprec_enum_update_status import SiprecEnumUpdateStatusOrStr
from ..models.enums.status_callback_method17 import StatusCallbackMethod17OrStr
from ..server.server import Server


class Api20100401Siprec:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401SiprecWithRawResponse(client, server, auth)

    def create_siprec(
        self,
        account_sid: str,
        call_sid: str,
        *,
        name: str | None = None,
        connector_name: str | None = None,
        track: SiprecEnumTrackOrStr | None = None,
        status_callback: str | None = None,
        status_callback_method: StatusCallbackMethod17OrStr | None = None,
        parameter1_name: str | None = None,
        parameter1_value: str | None = None,
        parameter2_name: str | None = None,
        parameter2_value: str | None = None,
        parameter3_name: str | None = None,
        parameter3_value: str | None = None,
        parameter4_name: str | None = None,
        parameter4_value: str | None = None,
        parameter5_name: str | None = None,
        parameter5_value: str | None = None,
        parameter6_name: str | None = None,
        parameter6_value: str | None = None,
        parameter7_name: str | None = None,
        parameter7_value: str | None = None,
        parameter8_name: str | None = None,
        parameter8_value: str | None = None,
        parameter9_name: str | None = None,
        parameter9_value: str | None = None,
        parameter10_name: str | None = None,
        parameter10_value: str | None = None,
        parameter11_name: str | None = None,
        parameter11_value: str | None = None,
        parameter12_name: str | None = None,
        parameter12_value: str | None = None,
        parameter13_name: str | None = None,
        parameter13_value: str | None = None,
        parameter14_name: str | None = None,
        parameter14_value: str | None = None,
        parameter15_name: str | None = None,
        parameter15_value: str | None = None,
        parameter16_name: str | None = None,
        parameter16_value: str | None = None,
        parameter17_name: str | None = None,
        parameter17_value: str | None = None,
        parameter18_name: str | None = None,
        parameter18_value: str | None = None,
        parameter19_name: str | None = None,
        parameter19_value: str | None = None,
        parameter20_name: str | None = None,
        parameter20_value: str | None = None,
        parameter21_name: str | None = None,
        parameter21_value: str | None = None,
        parameter22_name: str | None = None,
        parameter22_value: str | None = None,
        parameter23_name: str | None = None,
        parameter23_value: str | None = None,
        parameter24_name: str | None = None,
        parameter24_value: str | None = None,
        parameter25_name: str | None = None,
        parameter25_value: str | None = None,
        parameter26_name: str | None = None,
        parameter26_value: str | None = None,
        parameter27_name: str | None = None,
        parameter27_value: str | None = None,
        parameter28_name: str | None = None,
        parameter28_value: str | None = None,
        parameter29_name: str | None = None,
        parameter29_value: str | None = None,
        parameter30_name: str | None = None,
        parameter30_value: str | None = None,
        parameter31_name: str | None = None,
        parameter31_value: str | None = None,
        parameter32_name: str | None = None,
        parameter32_value: str | None = None,
        parameter33_name: str | None = None,
        parameter33_value: str | None = None,
        parameter34_name: str | None = None,
        parameter34_value: str | None = None,
        parameter35_name: str | None = None,
        parameter35_value: str | None = None,
        parameter36_name: str | None = None,
        parameter36_value: str | None = None,
        parameter37_name: str | None = None,
        parameter37_value: str | None = None,
        parameter38_name: str | None = None,
        parameter38_value: str | None = None,
        parameter39_name: str | None = None,
        parameter39_value: str | None = None,
        parameter40_name: str | None = None,
        parameter40_value: str | None = None,
        parameter41_name: str | None = None,
        parameter41_value: str | None = None,
        parameter42_name: str | None = None,
        parameter42_value: str | None = None,
        parameter43_name: str | None = None,
        parameter43_value: str | None = None,
        parameter44_name: str | None = None,
        parameter44_value: str | None = None,
        parameter45_name: str | None = None,
        parameter45_value: str | None = None,
        parameter46_name: str | None = None,
        parameter46_value: str | None = None,
        parameter47_name: str | None = None,
        parameter47_value: str | None = None,
        parameter48_name: str | None = None,
        parameter48_value: str | None = None,
        parameter49_name: str | None = None,
        parameter49_value: str | None = None,
        parameter50_name: str | None = None,
        parameter50_value: str | None = None,
        parameter51_name: str | None = None,
        parameter51_value: str | None = None,
        parameter52_name: str | None = None,
        parameter52_value: str | None = None,
        parameter53_name: str | None = None,
        parameter53_value: str | None = None,
        parameter54_name: str | None = None,
        parameter54_value: str | None = None,
        parameter55_name: str | None = None,
        parameter55_value: str | None = None,
        parameter56_name: str | None = None,
        parameter56_value: str | None = None,
        parameter57_name: str | None = None,
        parameter57_value: str | None = None,
        parameter58_name: str | None = None,
        parameter58_value: str | None = None,
        parameter59_name: str | None = None,
        parameter59_value: str | None = None,
        parameter60_name: str | None = None,
        parameter60_value: str | None = None,
        parameter61_name: str | None = None,
        parameter61_value: str | None = None,
        parameter62_name: str | None = None,
        parameter62_value: str | None = None,
        parameter63_name: str | None = None,
        parameter63_value: str | None = None,
        parameter64_name: str | None = None,
        parameter64_value: str | None = None,
        parameter65_name: str | None = None,
        parameter65_value: str | None = None,
        parameter66_name: str | None = None,
        parameter66_value: str | None = None,
        parameter67_name: str | None = None,
        parameter67_value: str | None = None,
        parameter68_name: str | None = None,
        parameter68_value: str | None = None,
        parameter69_name: str | None = None,
        parameter69_value: str | None = None,
        parameter70_name: str | None = None,
        parameter70_value: str | None = None,
        parameter71_name: str | None = None,
        parameter71_value: str | None = None,
        parameter72_name: str | None = None,
        parameter72_value: str | None = None,
        parameter73_name: str | None = None,
        parameter73_value: str | None = None,
        parameter74_name: str | None = None,
        parameter74_value: str | None = None,
        parameter75_name: str | None = None,
        parameter75_value: str | None = None,
        parameter76_name: str | None = None,
        parameter76_value: str | None = None,
        parameter77_name: str | None = None,
        parameter77_value: str | None = None,
        parameter78_name: str | None = None,
        parameter78_value: str | None = None,
        parameter79_name: str | None = None,
        parameter79_value: str | None = None,
        parameter80_name: str | None = None,
        parameter80_value: str | None = None,
        parameter81_name: str | None = None,
        parameter81_value: str | None = None,
        parameter82_name: str | None = None,
        parameter82_value: str | None = None,
        parameter83_name: str | None = None,
        parameter83_value: str | None = None,
        parameter84_name: str | None = None,
        parameter84_value: str | None = None,
        parameter85_name: str | None = None,
        parameter85_value: str | None = None,
        parameter86_name: str | None = None,
        parameter86_value: str | None = None,
        parameter87_name: str | None = None,
        parameter87_value: str | None = None,
        parameter88_name: str | None = None,
        parameter88_value: str | None = None,
        parameter89_name: str | None = None,
        parameter89_value: str | None = None,
        parameter90_name: str | None = None,
        parameter90_value: str | None = None,
        parameter91_name: str | None = None,
        parameter91_value: str | None = None,
        parameter92_name: str | None = None,
        parameter92_value: str | None = None,
        parameter93_name: str | None = None,
        parameter93_value: str | None = None,
        parameter94_name: str | None = None,
        parameter94_value: str | None = None,
        parameter95_name: str | None = None,
        parameter95_value: str | None = None,
        parameter96_name: str | None = None,
        parameter96_value: str | None = None,
        parameter97_name: str | None = None,
        parameter97_value: str | None = None,
        parameter98_name: str | None = None,
        parameter98_value: str | None = None,
        parameter99_name: str | None = None,
        parameter99_value: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountCallSiprec:
        """Create a Siprec

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created this
                Siprec resource.
            call_sid: The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the Siprec resource
                is associated with.
            name: The user-specified name of this Siprec, if one was given when the Siprec was created. This may be used
                to stop the Siprec.
            connector_name: Unique name used when configuring the connector via Marketplace Add-on.
            track: One of ``inbound_track``, ``outbound_track``, ``both_tracks``.
            status_callback: Absolute URL of the status callback.
            status_callback_method: The http method for the status_callback (one of GET, POST).
            parameter1_name: Parameter name
            parameter1_value: Parameter value
            parameter2_name: Parameter name
            parameter2_value: Parameter value
            parameter3_name: Parameter name
            parameter3_value: Parameter value
            parameter4_name: Parameter name
            parameter4_value: Parameter value
            parameter5_name: Parameter name
            parameter5_value: Parameter value
            parameter6_name: Parameter name
            parameter6_value: Parameter value
            parameter7_name: Parameter name
            parameter7_value: Parameter value
            parameter8_name: Parameter name
            parameter8_value: Parameter value
            parameter9_name: Parameter name
            parameter9_value: Parameter value
            parameter10_name: Parameter name
            parameter10_value: Parameter value
            parameter11_name: Parameter name
            parameter11_value: Parameter value
            parameter12_name: Parameter name
            parameter12_value: Parameter value
            parameter13_name: Parameter name
            parameter13_value: Parameter value
            parameter14_name: Parameter name
            parameter14_value: Parameter value
            parameter15_name: Parameter name
            parameter15_value: Parameter value
            parameter16_name: Parameter name
            parameter16_value: Parameter value
            parameter17_name: Parameter name
            parameter17_value: Parameter value
            parameter18_name: Parameter name
            parameter18_value: Parameter value
            parameter19_name: Parameter name
            parameter19_value: Parameter value
            parameter20_name: Parameter name
            parameter20_value: Parameter value
            parameter21_name: Parameter name
            parameter21_value: Parameter value
            parameter22_name: Parameter name
            parameter22_value: Parameter value
            parameter23_name: Parameter name
            parameter23_value: Parameter value
            parameter24_name: Parameter name
            parameter24_value: Parameter value
            parameter25_name: Parameter name
            parameter25_value: Parameter value
            parameter26_name: Parameter name
            parameter26_value: Parameter value
            parameter27_name: Parameter name
            parameter27_value: Parameter value
            parameter28_name: Parameter name
            parameter28_value: Parameter value
            parameter29_name: Parameter name
            parameter29_value: Parameter value
            parameter30_name: Parameter name
            parameter30_value: Parameter value
            parameter31_name: Parameter name
            parameter31_value: Parameter value
            parameter32_name: Parameter name
            parameter32_value: Parameter value
            parameter33_name: Parameter name
            parameter33_value: Parameter value
            parameter34_name: Parameter name
            parameter34_value: Parameter value
            parameter35_name: Parameter name
            parameter35_value: Parameter value
            parameter36_name: Parameter name
            parameter36_value: Parameter value
            parameter37_name: Parameter name
            parameter37_value: Parameter value
            parameter38_name: Parameter name
            parameter38_value: Parameter value
            parameter39_name: Parameter name
            parameter39_value: Parameter value
            parameter40_name: Parameter name
            parameter40_value: Parameter value
            parameter41_name: Parameter name
            parameter41_value: Parameter value
            parameter42_name: Parameter name
            parameter42_value: Parameter value
            parameter43_name: Parameter name
            parameter43_value: Parameter value
            parameter44_name: Parameter name
            parameter44_value: Parameter value
            parameter45_name: Parameter name
            parameter45_value: Parameter value
            parameter46_name: Parameter name
            parameter46_value: Parameter value
            parameter47_name: Parameter name
            parameter47_value: Parameter value
            parameter48_name: Parameter name
            parameter48_value: Parameter value
            parameter49_name: Parameter name
            parameter49_value: Parameter value
            parameter50_name: Parameter name
            parameter50_value: Parameter value
            parameter51_name: Parameter name
            parameter51_value: Parameter value
            parameter52_name: Parameter name
            parameter52_value: Parameter value
            parameter53_name: Parameter name
            parameter53_value: Parameter value
            parameter54_name: Parameter name
            parameter54_value: Parameter value
            parameter55_name: Parameter name
            parameter55_value: Parameter value
            parameter56_name: Parameter name
            parameter56_value: Parameter value
            parameter57_name: Parameter name
            parameter57_value: Parameter value
            parameter58_name: Parameter name
            parameter58_value: Parameter value
            parameter59_name: Parameter name
            parameter59_value: Parameter value
            parameter60_name: Parameter name
            parameter60_value: Parameter value
            parameter61_name: Parameter name
            parameter61_value: Parameter value
            parameter62_name: Parameter name
            parameter62_value: Parameter value
            parameter63_name: Parameter name
            parameter63_value: Parameter value
            parameter64_name: Parameter name
            parameter64_value: Parameter value
            parameter65_name: Parameter name
            parameter65_value: Parameter value
            parameter66_name: Parameter name
            parameter66_value: Parameter value
            parameter67_name: Parameter name
            parameter67_value: Parameter value
            parameter68_name: Parameter name
            parameter68_value: Parameter value
            parameter69_name: Parameter name
            parameter69_value: Parameter value
            parameter70_name: Parameter name
            parameter70_value: Parameter value
            parameter71_name: Parameter name
            parameter71_value: Parameter value
            parameter72_name: Parameter name
            parameter72_value: Parameter value
            parameter73_name: Parameter name
            parameter73_value: Parameter value
            parameter74_name: Parameter name
            parameter74_value: Parameter value
            parameter75_name: Parameter name
            parameter75_value: Parameter value
            parameter76_name: Parameter name
            parameter76_value: Parameter value
            parameter77_name: Parameter name
            parameter77_value: Parameter value
            parameter78_name: Parameter name
            parameter78_value: Parameter value
            parameter79_name: Parameter name
            parameter79_value: Parameter value
            parameter80_name: Parameter name
            parameter80_value: Parameter value
            parameter81_name: Parameter name
            parameter81_value: Parameter value
            parameter82_name: Parameter name
            parameter82_value: Parameter value
            parameter83_name: Parameter name
            parameter83_value: Parameter value
            parameter84_name: Parameter name
            parameter84_value: Parameter value
            parameter85_name: Parameter name
            parameter85_value: Parameter value
            parameter86_name: Parameter name
            parameter86_value: Parameter value
            parameter87_name: Parameter name
            parameter87_value: Parameter value
            parameter88_name: Parameter name
            parameter88_value: Parameter value
            parameter89_name: Parameter name
            parameter89_value: Parameter value
            parameter90_name: Parameter name
            parameter90_value: Parameter value
            parameter91_name: Parameter name
            parameter91_value: Parameter value
            parameter92_name: Parameter name
            parameter92_value: Parameter value
            parameter93_name: Parameter name
            parameter93_value: Parameter value
            parameter94_name: Parameter name
            parameter94_value: Parameter value
            parameter95_name: Parameter name
            parameter95_value: Parameter value
            parameter96_name: Parameter name
            parameter96_value: Parameter value
            parameter97_name: Parameter name
            parameter97_value: Parameter value
            parameter98_name: Parameter name
            parameter98_value: Parameter value
            parameter99_name: Parameter name
            parameter99_value: Parameter value
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_siprec(
            account_sid,
            call_sid,
            name=name,
            connector_name=connector_name,
            track=track,
            status_callback=status_callback,
            status_callback_method=status_callback_method,
            parameter1_name=parameter1_name,
            parameter1_value=parameter1_value,
            parameter2_name=parameter2_name,
            parameter2_value=parameter2_value,
            parameter3_name=parameter3_name,
            parameter3_value=parameter3_value,
            parameter4_name=parameter4_name,
            parameter4_value=parameter4_value,
            parameter5_name=parameter5_name,
            parameter5_value=parameter5_value,
            parameter6_name=parameter6_name,
            parameter6_value=parameter6_value,
            parameter7_name=parameter7_name,
            parameter7_value=parameter7_value,
            parameter8_name=parameter8_name,
            parameter8_value=parameter8_value,
            parameter9_name=parameter9_name,
            parameter9_value=parameter9_value,
            parameter10_name=parameter10_name,
            parameter10_value=parameter10_value,
            parameter11_name=parameter11_name,
            parameter11_value=parameter11_value,
            parameter12_name=parameter12_name,
            parameter12_value=parameter12_value,
            parameter13_name=parameter13_name,
            parameter13_value=parameter13_value,
            parameter14_name=parameter14_name,
            parameter14_value=parameter14_value,
            parameter15_name=parameter15_name,
            parameter15_value=parameter15_value,
            parameter16_name=parameter16_name,
            parameter16_value=parameter16_value,
            parameter17_name=parameter17_name,
            parameter17_value=parameter17_value,
            parameter18_name=parameter18_name,
            parameter18_value=parameter18_value,
            parameter19_name=parameter19_name,
            parameter19_value=parameter19_value,
            parameter20_name=parameter20_name,
            parameter20_value=parameter20_value,
            parameter21_name=parameter21_name,
            parameter21_value=parameter21_value,
            parameter22_name=parameter22_name,
            parameter22_value=parameter22_value,
            parameter23_name=parameter23_name,
            parameter23_value=parameter23_value,
            parameter24_name=parameter24_name,
            parameter24_value=parameter24_value,
            parameter25_name=parameter25_name,
            parameter25_value=parameter25_value,
            parameter26_name=parameter26_name,
            parameter26_value=parameter26_value,
            parameter27_name=parameter27_name,
            parameter27_value=parameter27_value,
            parameter28_name=parameter28_name,
            parameter28_value=parameter28_value,
            parameter29_name=parameter29_name,
            parameter29_value=parameter29_value,
            parameter30_name=parameter30_name,
            parameter30_value=parameter30_value,
            parameter31_name=parameter31_name,
            parameter31_value=parameter31_value,
            parameter32_name=parameter32_name,
            parameter32_value=parameter32_value,
            parameter33_name=parameter33_name,
            parameter33_value=parameter33_value,
            parameter34_name=parameter34_name,
            parameter34_value=parameter34_value,
            parameter35_name=parameter35_name,
            parameter35_value=parameter35_value,
            parameter36_name=parameter36_name,
            parameter36_value=parameter36_value,
            parameter37_name=parameter37_name,
            parameter37_value=parameter37_value,
            parameter38_name=parameter38_name,
            parameter38_value=parameter38_value,
            parameter39_name=parameter39_name,
            parameter39_value=parameter39_value,
            parameter40_name=parameter40_name,
            parameter40_value=parameter40_value,
            parameter41_name=parameter41_name,
            parameter41_value=parameter41_value,
            parameter42_name=parameter42_name,
            parameter42_value=parameter42_value,
            parameter43_name=parameter43_name,
            parameter43_value=parameter43_value,
            parameter44_name=parameter44_name,
            parameter44_value=parameter44_value,
            parameter45_name=parameter45_name,
            parameter45_value=parameter45_value,
            parameter46_name=parameter46_name,
            parameter46_value=parameter46_value,
            parameter47_name=parameter47_name,
            parameter47_value=parameter47_value,
            parameter48_name=parameter48_name,
            parameter48_value=parameter48_value,
            parameter49_name=parameter49_name,
            parameter49_value=parameter49_value,
            parameter50_name=parameter50_name,
            parameter50_value=parameter50_value,
            parameter51_name=parameter51_name,
            parameter51_value=parameter51_value,
            parameter52_name=parameter52_name,
            parameter52_value=parameter52_value,
            parameter53_name=parameter53_name,
            parameter53_value=parameter53_value,
            parameter54_name=parameter54_name,
            parameter54_value=parameter54_value,
            parameter55_name=parameter55_name,
            parameter55_value=parameter55_value,
            parameter56_name=parameter56_name,
            parameter56_value=parameter56_value,
            parameter57_name=parameter57_name,
            parameter57_value=parameter57_value,
            parameter58_name=parameter58_name,
            parameter58_value=parameter58_value,
            parameter59_name=parameter59_name,
            parameter59_value=parameter59_value,
            parameter60_name=parameter60_name,
            parameter60_value=parameter60_value,
            parameter61_name=parameter61_name,
            parameter61_value=parameter61_value,
            parameter62_name=parameter62_name,
            parameter62_value=parameter62_value,
            parameter63_name=parameter63_name,
            parameter63_value=parameter63_value,
            parameter64_name=parameter64_name,
            parameter64_value=parameter64_value,
            parameter65_name=parameter65_name,
            parameter65_value=parameter65_value,
            parameter66_name=parameter66_name,
            parameter66_value=parameter66_value,
            parameter67_name=parameter67_name,
            parameter67_value=parameter67_value,
            parameter68_name=parameter68_name,
            parameter68_value=parameter68_value,
            parameter69_name=parameter69_name,
            parameter69_value=parameter69_value,
            parameter70_name=parameter70_name,
            parameter70_value=parameter70_value,
            parameter71_name=parameter71_name,
            parameter71_value=parameter71_value,
            parameter72_name=parameter72_name,
            parameter72_value=parameter72_value,
            parameter73_name=parameter73_name,
            parameter73_value=parameter73_value,
            parameter74_name=parameter74_name,
            parameter74_value=parameter74_value,
            parameter75_name=parameter75_name,
            parameter75_value=parameter75_value,
            parameter76_name=parameter76_name,
            parameter76_value=parameter76_value,
            parameter77_name=parameter77_name,
            parameter77_value=parameter77_value,
            parameter78_name=parameter78_name,
            parameter78_value=parameter78_value,
            parameter79_name=parameter79_name,
            parameter79_value=parameter79_value,
            parameter80_name=parameter80_name,
            parameter80_value=parameter80_value,
            parameter81_name=parameter81_name,
            parameter81_value=parameter81_value,
            parameter82_name=parameter82_name,
            parameter82_value=parameter82_value,
            parameter83_name=parameter83_name,
            parameter83_value=parameter83_value,
            parameter84_name=parameter84_name,
            parameter84_value=parameter84_value,
            parameter85_name=parameter85_name,
            parameter85_value=parameter85_value,
            parameter86_name=parameter86_name,
            parameter86_value=parameter86_value,
            parameter87_name=parameter87_name,
            parameter87_value=parameter87_value,
            parameter88_name=parameter88_name,
            parameter88_value=parameter88_value,
            parameter89_name=parameter89_name,
            parameter89_value=parameter89_value,
            parameter90_name=parameter90_name,
            parameter90_value=parameter90_value,
            parameter91_name=parameter91_name,
            parameter91_value=parameter91_value,
            parameter92_name=parameter92_name,
            parameter92_value=parameter92_value,
            parameter93_name=parameter93_name,
            parameter93_value=parameter93_value,
            parameter94_name=parameter94_name,
            parameter94_value=parameter94_value,
            parameter95_name=parameter95_name,
            parameter95_value=parameter95_value,
            parameter96_name=parameter96_name,
            parameter96_value=parameter96_value,
            parameter97_name=parameter97_name,
            parameter97_value=parameter97_value,
            parameter98_name=parameter98_name,
            parameter98_value=parameter98_value,
            parameter99_name=parameter99_name,
            parameter99_value=parameter99_value,
            request_options=request_options,
        ).unwrap()

    def update_siprec(
        self,
        account_sid: str,
        call_sid: str,
        sid: str,
        status: SiprecEnumUpdateStatusOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountCallSiprec:
        """Stop a Siprec using either the SID of the Siprec resource or the ``name`` used when creating the resource

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created this
                Siprec resource.
            call_sid: The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the Siprec resource
                is associated with.
            sid: The SID of the Siprec resource, or the ``name`` used when creating the resource
            status: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_siprec(
            account_sid, call_sid, sid, status, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401SiprecWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401Siprec:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401SiprecWithRawResponse(client, server, auth)

    async def create_siprec(
        self,
        account_sid: str,
        call_sid: str,
        *,
        name: str | None = None,
        connector_name: str | None = None,
        track: SiprecEnumTrackOrStr | None = None,
        status_callback: str | None = None,
        status_callback_method: StatusCallbackMethod17OrStr | None = None,
        parameter1_name: str | None = None,
        parameter1_value: str | None = None,
        parameter2_name: str | None = None,
        parameter2_value: str | None = None,
        parameter3_name: str | None = None,
        parameter3_value: str | None = None,
        parameter4_name: str | None = None,
        parameter4_value: str | None = None,
        parameter5_name: str | None = None,
        parameter5_value: str | None = None,
        parameter6_name: str | None = None,
        parameter6_value: str | None = None,
        parameter7_name: str | None = None,
        parameter7_value: str | None = None,
        parameter8_name: str | None = None,
        parameter8_value: str | None = None,
        parameter9_name: str | None = None,
        parameter9_value: str | None = None,
        parameter10_name: str | None = None,
        parameter10_value: str | None = None,
        parameter11_name: str | None = None,
        parameter11_value: str | None = None,
        parameter12_name: str | None = None,
        parameter12_value: str | None = None,
        parameter13_name: str | None = None,
        parameter13_value: str | None = None,
        parameter14_name: str | None = None,
        parameter14_value: str | None = None,
        parameter15_name: str | None = None,
        parameter15_value: str | None = None,
        parameter16_name: str | None = None,
        parameter16_value: str | None = None,
        parameter17_name: str | None = None,
        parameter17_value: str | None = None,
        parameter18_name: str | None = None,
        parameter18_value: str | None = None,
        parameter19_name: str | None = None,
        parameter19_value: str | None = None,
        parameter20_name: str | None = None,
        parameter20_value: str | None = None,
        parameter21_name: str | None = None,
        parameter21_value: str | None = None,
        parameter22_name: str | None = None,
        parameter22_value: str | None = None,
        parameter23_name: str | None = None,
        parameter23_value: str | None = None,
        parameter24_name: str | None = None,
        parameter24_value: str | None = None,
        parameter25_name: str | None = None,
        parameter25_value: str | None = None,
        parameter26_name: str | None = None,
        parameter26_value: str | None = None,
        parameter27_name: str | None = None,
        parameter27_value: str | None = None,
        parameter28_name: str | None = None,
        parameter28_value: str | None = None,
        parameter29_name: str | None = None,
        parameter29_value: str | None = None,
        parameter30_name: str | None = None,
        parameter30_value: str | None = None,
        parameter31_name: str | None = None,
        parameter31_value: str | None = None,
        parameter32_name: str | None = None,
        parameter32_value: str | None = None,
        parameter33_name: str | None = None,
        parameter33_value: str | None = None,
        parameter34_name: str | None = None,
        parameter34_value: str | None = None,
        parameter35_name: str | None = None,
        parameter35_value: str | None = None,
        parameter36_name: str | None = None,
        parameter36_value: str | None = None,
        parameter37_name: str | None = None,
        parameter37_value: str | None = None,
        parameter38_name: str | None = None,
        parameter38_value: str | None = None,
        parameter39_name: str | None = None,
        parameter39_value: str | None = None,
        parameter40_name: str | None = None,
        parameter40_value: str | None = None,
        parameter41_name: str | None = None,
        parameter41_value: str | None = None,
        parameter42_name: str | None = None,
        parameter42_value: str | None = None,
        parameter43_name: str | None = None,
        parameter43_value: str | None = None,
        parameter44_name: str | None = None,
        parameter44_value: str | None = None,
        parameter45_name: str | None = None,
        parameter45_value: str | None = None,
        parameter46_name: str | None = None,
        parameter46_value: str | None = None,
        parameter47_name: str | None = None,
        parameter47_value: str | None = None,
        parameter48_name: str | None = None,
        parameter48_value: str | None = None,
        parameter49_name: str | None = None,
        parameter49_value: str | None = None,
        parameter50_name: str | None = None,
        parameter50_value: str | None = None,
        parameter51_name: str | None = None,
        parameter51_value: str | None = None,
        parameter52_name: str | None = None,
        parameter52_value: str | None = None,
        parameter53_name: str | None = None,
        parameter53_value: str | None = None,
        parameter54_name: str | None = None,
        parameter54_value: str | None = None,
        parameter55_name: str | None = None,
        parameter55_value: str | None = None,
        parameter56_name: str | None = None,
        parameter56_value: str | None = None,
        parameter57_name: str | None = None,
        parameter57_value: str | None = None,
        parameter58_name: str | None = None,
        parameter58_value: str | None = None,
        parameter59_name: str | None = None,
        parameter59_value: str | None = None,
        parameter60_name: str | None = None,
        parameter60_value: str | None = None,
        parameter61_name: str | None = None,
        parameter61_value: str | None = None,
        parameter62_name: str | None = None,
        parameter62_value: str | None = None,
        parameter63_name: str | None = None,
        parameter63_value: str | None = None,
        parameter64_name: str | None = None,
        parameter64_value: str | None = None,
        parameter65_name: str | None = None,
        parameter65_value: str | None = None,
        parameter66_name: str | None = None,
        parameter66_value: str | None = None,
        parameter67_name: str | None = None,
        parameter67_value: str | None = None,
        parameter68_name: str | None = None,
        parameter68_value: str | None = None,
        parameter69_name: str | None = None,
        parameter69_value: str | None = None,
        parameter70_name: str | None = None,
        parameter70_value: str | None = None,
        parameter71_name: str | None = None,
        parameter71_value: str | None = None,
        parameter72_name: str | None = None,
        parameter72_value: str | None = None,
        parameter73_name: str | None = None,
        parameter73_value: str | None = None,
        parameter74_name: str | None = None,
        parameter74_value: str | None = None,
        parameter75_name: str | None = None,
        parameter75_value: str | None = None,
        parameter76_name: str | None = None,
        parameter76_value: str | None = None,
        parameter77_name: str | None = None,
        parameter77_value: str | None = None,
        parameter78_name: str | None = None,
        parameter78_value: str | None = None,
        parameter79_name: str | None = None,
        parameter79_value: str | None = None,
        parameter80_name: str | None = None,
        parameter80_value: str | None = None,
        parameter81_name: str | None = None,
        parameter81_value: str | None = None,
        parameter82_name: str | None = None,
        parameter82_value: str | None = None,
        parameter83_name: str | None = None,
        parameter83_value: str | None = None,
        parameter84_name: str | None = None,
        parameter84_value: str | None = None,
        parameter85_name: str | None = None,
        parameter85_value: str | None = None,
        parameter86_name: str | None = None,
        parameter86_value: str | None = None,
        parameter87_name: str | None = None,
        parameter87_value: str | None = None,
        parameter88_name: str | None = None,
        parameter88_value: str | None = None,
        parameter89_name: str | None = None,
        parameter89_value: str | None = None,
        parameter90_name: str | None = None,
        parameter90_value: str | None = None,
        parameter91_name: str | None = None,
        parameter91_value: str | None = None,
        parameter92_name: str | None = None,
        parameter92_value: str | None = None,
        parameter93_name: str | None = None,
        parameter93_value: str | None = None,
        parameter94_name: str | None = None,
        parameter94_value: str | None = None,
        parameter95_name: str | None = None,
        parameter95_value: str | None = None,
        parameter96_name: str | None = None,
        parameter96_value: str | None = None,
        parameter97_name: str | None = None,
        parameter97_value: str | None = None,
        parameter98_name: str | None = None,
        parameter98_value: str | None = None,
        parameter99_name: str | None = None,
        parameter99_value: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountCallSiprec:
        """Create a Siprec

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created this
                Siprec resource.
            call_sid: The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the Siprec resource
                is associated with.
            name: The user-specified name of this Siprec, if one was given when the Siprec was created. This may be used
                to stop the Siprec.
            connector_name: Unique name used when configuring the connector via Marketplace Add-on.
            track: One of ``inbound_track``, ``outbound_track``, ``both_tracks``.
            status_callback: Absolute URL of the status callback.
            status_callback_method: The http method for the status_callback (one of GET, POST).
            parameter1_name: Parameter name
            parameter1_value: Parameter value
            parameter2_name: Parameter name
            parameter2_value: Parameter value
            parameter3_name: Parameter name
            parameter3_value: Parameter value
            parameter4_name: Parameter name
            parameter4_value: Parameter value
            parameter5_name: Parameter name
            parameter5_value: Parameter value
            parameter6_name: Parameter name
            parameter6_value: Parameter value
            parameter7_name: Parameter name
            parameter7_value: Parameter value
            parameter8_name: Parameter name
            parameter8_value: Parameter value
            parameter9_name: Parameter name
            parameter9_value: Parameter value
            parameter10_name: Parameter name
            parameter10_value: Parameter value
            parameter11_name: Parameter name
            parameter11_value: Parameter value
            parameter12_name: Parameter name
            parameter12_value: Parameter value
            parameter13_name: Parameter name
            parameter13_value: Parameter value
            parameter14_name: Parameter name
            parameter14_value: Parameter value
            parameter15_name: Parameter name
            parameter15_value: Parameter value
            parameter16_name: Parameter name
            parameter16_value: Parameter value
            parameter17_name: Parameter name
            parameter17_value: Parameter value
            parameter18_name: Parameter name
            parameter18_value: Parameter value
            parameter19_name: Parameter name
            parameter19_value: Parameter value
            parameter20_name: Parameter name
            parameter20_value: Parameter value
            parameter21_name: Parameter name
            parameter21_value: Parameter value
            parameter22_name: Parameter name
            parameter22_value: Parameter value
            parameter23_name: Parameter name
            parameter23_value: Parameter value
            parameter24_name: Parameter name
            parameter24_value: Parameter value
            parameter25_name: Parameter name
            parameter25_value: Parameter value
            parameter26_name: Parameter name
            parameter26_value: Parameter value
            parameter27_name: Parameter name
            parameter27_value: Parameter value
            parameter28_name: Parameter name
            parameter28_value: Parameter value
            parameter29_name: Parameter name
            parameter29_value: Parameter value
            parameter30_name: Parameter name
            parameter30_value: Parameter value
            parameter31_name: Parameter name
            parameter31_value: Parameter value
            parameter32_name: Parameter name
            parameter32_value: Parameter value
            parameter33_name: Parameter name
            parameter33_value: Parameter value
            parameter34_name: Parameter name
            parameter34_value: Parameter value
            parameter35_name: Parameter name
            parameter35_value: Parameter value
            parameter36_name: Parameter name
            parameter36_value: Parameter value
            parameter37_name: Parameter name
            parameter37_value: Parameter value
            parameter38_name: Parameter name
            parameter38_value: Parameter value
            parameter39_name: Parameter name
            parameter39_value: Parameter value
            parameter40_name: Parameter name
            parameter40_value: Parameter value
            parameter41_name: Parameter name
            parameter41_value: Parameter value
            parameter42_name: Parameter name
            parameter42_value: Parameter value
            parameter43_name: Parameter name
            parameter43_value: Parameter value
            parameter44_name: Parameter name
            parameter44_value: Parameter value
            parameter45_name: Parameter name
            parameter45_value: Parameter value
            parameter46_name: Parameter name
            parameter46_value: Parameter value
            parameter47_name: Parameter name
            parameter47_value: Parameter value
            parameter48_name: Parameter name
            parameter48_value: Parameter value
            parameter49_name: Parameter name
            parameter49_value: Parameter value
            parameter50_name: Parameter name
            parameter50_value: Parameter value
            parameter51_name: Parameter name
            parameter51_value: Parameter value
            parameter52_name: Parameter name
            parameter52_value: Parameter value
            parameter53_name: Parameter name
            parameter53_value: Parameter value
            parameter54_name: Parameter name
            parameter54_value: Parameter value
            parameter55_name: Parameter name
            parameter55_value: Parameter value
            parameter56_name: Parameter name
            parameter56_value: Parameter value
            parameter57_name: Parameter name
            parameter57_value: Parameter value
            parameter58_name: Parameter name
            parameter58_value: Parameter value
            parameter59_name: Parameter name
            parameter59_value: Parameter value
            parameter60_name: Parameter name
            parameter60_value: Parameter value
            parameter61_name: Parameter name
            parameter61_value: Parameter value
            parameter62_name: Parameter name
            parameter62_value: Parameter value
            parameter63_name: Parameter name
            parameter63_value: Parameter value
            parameter64_name: Parameter name
            parameter64_value: Parameter value
            parameter65_name: Parameter name
            parameter65_value: Parameter value
            parameter66_name: Parameter name
            parameter66_value: Parameter value
            parameter67_name: Parameter name
            parameter67_value: Parameter value
            parameter68_name: Parameter name
            parameter68_value: Parameter value
            parameter69_name: Parameter name
            parameter69_value: Parameter value
            parameter70_name: Parameter name
            parameter70_value: Parameter value
            parameter71_name: Parameter name
            parameter71_value: Parameter value
            parameter72_name: Parameter name
            parameter72_value: Parameter value
            parameter73_name: Parameter name
            parameter73_value: Parameter value
            parameter74_name: Parameter name
            parameter74_value: Parameter value
            parameter75_name: Parameter name
            parameter75_value: Parameter value
            parameter76_name: Parameter name
            parameter76_value: Parameter value
            parameter77_name: Parameter name
            parameter77_value: Parameter value
            parameter78_name: Parameter name
            parameter78_value: Parameter value
            parameter79_name: Parameter name
            parameter79_value: Parameter value
            parameter80_name: Parameter name
            parameter80_value: Parameter value
            parameter81_name: Parameter name
            parameter81_value: Parameter value
            parameter82_name: Parameter name
            parameter82_value: Parameter value
            parameter83_name: Parameter name
            parameter83_value: Parameter value
            parameter84_name: Parameter name
            parameter84_value: Parameter value
            parameter85_name: Parameter name
            parameter85_value: Parameter value
            parameter86_name: Parameter name
            parameter86_value: Parameter value
            parameter87_name: Parameter name
            parameter87_value: Parameter value
            parameter88_name: Parameter name
            parameter88_value: Parameter value
            parameter89_name: Parameter name
            parameter89_value: Parameter value
            parameter90_name: Parameter name
            parameter90_value: Parameter value
            parameter91_name: Parameter name
            parameter91_value: Parameter value
            parameter92_name: Parameter name
            parameter92_value: Parameter value
            parameter93_name: Parameter name
            parameter93_value: Parameter value
            parameter94_name: Parameter name
            parameter94_value: Parameter value
            parameter95_name: Parameter name
            parameter95_value: Parameter value
            parameter96_name: Parameter name
            parameter96_value: Parameter value
            parameter97_name: Parameter name
            parameter97_value: Parameter value
            parameter98_name: Parameter name
            parameter98_value: Parameter value
            parameter99_name: Parameter name
            parameter99_value: Parameter value
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_siprec(
                account_sid,
                call_sid,
                name=name,
                connector_name=connector_name,
                track=track,
                status_callback=status_callback,
                status_callback_method=status_callback_method,
                parameter1_name=parameter1_name,
                parameter1_value=parameter1_value,
                parameter2_name=parameter2_name,
                parameter2_value=parameter2_value,
                parameter3_name=parameter3_name,
                parameter3_value=parameter3_value,
                parameter4_name=parameter4_name,
                parameter4_value=parameter4_value,
                parameter5_name=parameter5_name,
                parameter5_value=parameter5_value,
                parameter6_name=parameter6_name,
                parameter6_value=parameter6_value,
                parameter7_name=parameter7_name,
                parameter7_value=parameter7_value,
                parameter8_name=parameter8_name,
                parameter8_value=parameter8_value,
                parameter9_name=parameter9_name,
                parameter9_value=parameter9_value,
                parameter10_name=parameter10_name,
                parameter10_value=parameter10_value,
                parameter11_name=parameter11_name,
                parameter11_value=parameter11_value,
                parameter12_name=parameter12_name,
                parameter12_value=parameter12_value,
                parameter13_name=parameter13_name,
                parameter13_value=parameter13_value,
                parameter14_name=parameter14_name,
                parameter14_value=parameter14_value,
                parameter15_name=parameter15_name,
                parameter15_value=parameter15_value,
                parameter16_name=parameter16_name,
                parameter16_value=parameter16_value,
                parameter17_name=parameter17_name,
                parameter17_value=parameter17_value,
                parameter18_name=parameter18_name,
                parameter18_value=parameter18_value,
                parameter19_name=parameter19_name,
                parameter19_value=parameter19_value,
                parameter20_name=parameter20_name,
                parameter20_value=parameter20_value,
                parameter21_name=parameter21_name,
                parameter21_value=parameter21_value,
                parameter22_name=parameter22_name,
                parameter22_value=parameter22_value,
                parameter23_name=parameter23_name,
                parameter23_value=parameter23_value,
                parameter24_name=parameter24_name,
                parameter24_value=parameter24_value,
                parameter25_name=parameter25_name,
                parameter25_value=parameter25_value,
                parameter26_name=parameter26_name,
                parameter26_value=parameter26_value,
                parameter27_name=parameter27_name,
                parameter27_value=parameter27_value,
                parameter28_name=parameter28_name,
                parameter28_value=parameter28_value,
                parameter29_name=parameter29_name,
                parameter29_value=parameter29_value,
                parameter30_name=parameter30_name,
                parameter30_value=parameter30_value,
                parameter31_name=parameter31_name,
                parameter31_value=parameter31_value,
                parameter32_name=parameter32_name,
                parameter32_value=parameter32_value,
                parameter33_name=parameter33_name,
                parameter33_value=parameter33_value,
                parameter34_name=parameter34_name,
                parameter34_value=parameter34_value,
                parameter35_name=parameter35_name,
                parameter35_value=parameter35_value,
                parameter36_name=parameter36_name,
                parameter36_value=parameter36_value,
                parameter37_name=parameter37_name,
                parameter37_value=parameter37_value,
                parameter38_name=parameter38_name,
                parameter38_value=parameter38_value,
                parameter39_name=parameter39_name,
                parameter39_value=parameter39_value,
                parameter40_name=parameter40_name,
                parameter40_value=parameter40_value,
                parameter41_name=parameter41_name,
                parameter41_value=parameter41_value,
                parameter42_name=parameter42_name,
                parameter42_value=parameter42_value,
                parameter43_name=parameter43_name,
                parameter43_value=parameter43_value,
                parameter44_name=parameter44_name,
                parameter44_value=parameter44_value,
                parameter45_name=parameter45_name,
                parameter45_value=parameter45_value,
                parameter46_name=parameter46_name,
                parameter46_value=parameter46_value,
                parameter47_name=parameter47_name,
                parameter47_value=parameter47_value,
                parameter48_name=parameter48_name,
                parameter48_value=parameter48_value,
                parameter49_name=parameter49_name,
                parameter49_value=parameter49_value,
                parameter50_name=parameter50_name,
                parameter50_value=parameter50_value,
                parameter51_name=parameter51_name,
                parameter51_value=parameter51_value,
                parameter52_name=parameter52_name,
                parameter52_value=parameter52_value,
                parameter53_name=parameter53_name,
                parameter53_value=parameter53_value,
                parameter54_name=parameter54_name,
                parameter54_value=parameter54_value,
                parameter55_name=parameter55_name,
                parameter55_value=parameter55_value,
                parameter56_name=parameter56_name,
                parameter56_value=parameter56_value,
                parameter57_name=parameter57_name,
                parameter57_value=parameter57_value,
                parameter58_name=parameter58_name,
                parameter58_value=parameter58_value,
                parameter59_name=parameter59_name,
                parameter59_value=parameter59_value,
                parameter60_name=parameter60_name,
                parameter60_value=parameter60_value,
                parameter61_name=parameter61_name,
                parameter61_value=parameter61_value,
                parameter62_name=parameter62_name,
                parameter62_value=parameter62_value,
                parameter63_name=parameter63_name,
                parameter63_value=parameter63_value,
                parameter64_name=parameter64_name,
                parameter64_value=parameter64_value,
                parameter65_name=parameter65_name,
                parameter65_value=parameter65_value,
                parameter66_name=parameter66_name,
                parameter66_value=parameter66_value,
                parameter67_name=parameter67_name,
                parameter67_value=parameter67_value,
                parameter68_name=parameter68_name,
                parameter68_value=parameter68_value,
                parameter69_name=parameter69_name,
                parameter69_value=parameter69_value,
                parameter70_name=parameter70_name,
                parameter70_value=parameter70_value,
                parameter71_name=parameter71_name,
                parameter71_value=parameter71_value,
                parameter72_name=parameter72_name,
                parameter72_value=parameter72_value,
                parameter73_name=parameter73_name,
                parameter73_value=parameter73_value,
                parameter74_name=parameter74_name,
                parameter74_value=parameter74_value,
                parameter75_name=parameter75_name,
                parameter75_value=parameter75_value,
                parameter76_name=parameter76_name,
                parameter76_value=parameter76_value,
                parameter77_name=parameter77_name,
                parameter77_value=parameter77_value,
                parameter78_name=parameter78_name,
                parameter78_value=parameter78_value,
                parameter79_name=parameter79_name,
                parameter79_value=parameter79_value,
                parameter80_name=parameter80_name,
                parameter80_value=parameter80_value,
                parameter81_name=parameter81_name,
                parameter81_value=parameter81_value,
                parameter82_name=parameter82_name,
                parameter82_value=parameter82_value,
                parameter83_name=parameter83_name,
                parameter83_value=parameter83_value,
                parameter84_name=parameter84_name,
                parameter84_value=parameter84_value,
                parameter85_name=parameter85_name,
                parameter85_value=parameter85_value,
                parameter86_name=parameter86_name,
                parameter86_value=parameter86_value,
                parameter87_name=parameter87_name,
                parameter87_value=parameter87_value,
                parameter88_name=parameter88_name,
                parameter88_value=parameter88_value,
                parameter89_name=parameter89_name,
                parameter89_value=parameter89_value,
                parameter90_name=parameter90_name,
                parameter90_value=parameter90_value,
                parameter91_name=parameter91_name,
                parameter91_value=parameter91_value,
                parameter92_name=parameter92_name,
                parameter92_value=parameter92_value,
                parameter93_name=parameter93_name,
                parameter93_value=parameter93_value,
                parameter94_name=parameter94_name,
                parameter94_value=parameter94_value,
                parameter95_name=parameter95_name,
                parameter95_value=parameter95_value,
                parameter96_name=parameter96_name,
                parameter96_value=parameter96_value,
                parameter97_name=parameter97_name,
                parameter97_value=parameter97_value,
                parameter98_name=parameter98_name,
                parameter98_value=parameter98_value,
                parameter99_name=parameter99_name,
                parameter99_value=parameter99_value,
                request_options=request_options,
            )
        ).unwrap()

    async def update_siprec(
        self,
        account_sid: str,
        call_sid: str,
        sid: str,
        status: SiprecEnumUpdateStatusOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountCallSiprec:
        """Stop a Siprec using either the SID of the Siprec resource or the ``name`` used when creating the resource

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created this
                Siprec resource.
            call_sid: The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the Siprec resource
                is associated with.
            sid: The SID of the Siprec resource, or the ``name`` used when creating the resource
            status: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_siprec(
                account_sid, call_sid, sid, status, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401SiprecWithRawResponse:
        return self._with_raw_response


class Api20100401SiprecWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_siprec(
        self,
        account_sid: str,
        call_sid: str,
        *,
        name: str | None = None,
        connector_name: str | None = None,
        track: SiprecEnumTrackOrStr | None = None,
        status_callback: str | None = None,
        status_callback_method: StatusCallbackMethod17OrStr | None = None,
        parameter1_name: str | None = None,
        parameter1_value: str | None = None,
        parameter2_name: str | None = None,
        parameter2_value: str | None = None,
        parameter3_name: str | None = None,
        parameter3_value: str | None = None,
        parameter4_name: str | None = None,
        parameter4_value: str | None = None,
        parameter5_name: str | None = None,
        parameter5_value: str | None = None,
        parameter6_name: str | None = None,
        parameter6_value: str | None = None,
        parameter7_name: str | None = None,
        parameter7_value: str | None = None,
        parameter8_name: str | None = None,
        parameter8_value: str | None = None,
        parameter9_name: str | None = None,
        parameter9_value: str | None = None,
        parameter10_name: str | None = None,
        parameter10_value: str | None = None,
        parameter11_name: str | None = None,
        parameter11_value: str | None = None,
        parameter12_name: str | None = None,
        parameter12_value: str | None = None,
        parameter13_name: str | None = None,
        parameter13_value: str | None = None,
        parameter14_name: str | None = None,
        parameter14_value: str | None = None,
        parameter15_name: str | None = None,
        parameter15_value: str | None = None,
        parameter16_name: str | None = None,
        parameter16_value: str | None = None,
        parameter17_name: str | None = None,
        parameter17_value: str | None = None,
        parameter18_name: str | None = None,
        parameter18_value: str | None = None,
        parameter19_name: str | None = None,
        parameter19_value: str | None = None,
        parameter20_name: str | None = None,
        parameter20_value: str | None = None,
        parameter21_name: str | None = None,
        parameter21_value: str | None = None,
        parameter22_name: str | None = None,
        parameter22_value: str | None = None,
        parameter23_name: str | None = None,
        parameter23_value: str | None = None,
        parameter24_name: str | None = None,
        parameter24_value: str | None = None,
        parameter25_name: str | None = None,
        parameter25_value: str | None = None,
        parameter26_name: str | None = None,
        parameter26_value: str | None = None,
        parameter27_name: str | None = None,
        parameter27_value: str | None = None,
        parameter28_name: str | None = None,
        parameter28_value: str | None = None,
        parameter29_name: str | None = None,
        parameter29_value: str | None = None,
        parameter30_name: str | None = None,
        parameter30_value: str | None = None,
        parameter31_name: str | None = None,
        parameter31_value: str | None = None,
        parameter32_name: str | None = None,
        parameter32_value: str | None = None,
        parameter33_name: str | None = None,
        parameter33_value: str | None = None,
        parameter34_name: str | None = None,
        parameter34_value: str | None = None,
        parameter35_name: str | None = None,
        parameter35_value: str | None = None,
        parameter36_name: str | None = None,
        parameter36_value: str | None = None,
        parameter37_name: str | None = None,
        parameter37_value: str | None = None,
        parameter38_name: str | None = None,
        parameter38_value: str | None = None,
        parameter39_name: str | None = None,
        parameter39_value: str | None = None,
        parameter40_name: str | None = None,
        parameter40_value: str | None = None,
        parameter41_name: str | None = None,
        parameter41_value: str | None = None,
        parameter42_name: str | None = None,
        parameter42_value: str | None = None,
        parameter43_name: str | None = None,
        parameter43_value: str | None = None,
        parameter44_name: str | None = None,
        parameter44_value: str | None = None,
        parameter45_name: str | None = None,
        parameter45_value: str | None = None,
        parameter46_name: str | None = None,
        parameter46_value: str | None = None,
        parameter47_name: str | None = None,
        parameter47_value: str | None = None,
        parameter48_name: str | None = None,
        parameter48_value: str | None = None,
        parameter49_name: str | None = None,
        parameter49_value: str | None = None,
        parameter50_name: str | None = None,
        parameter50_value: str | None = None,
        parameter51_name: str | None = None,
        parameter51_value: str | None = None,
        parameter52_name: str | None = None,
        parameter52_value: str | None = None,
        parameter53_name: str | None = None,
        parameter53_value: str | None = None,
        parameter54_name: str | None = None,
        parameter54_value: str | None = None,
        parameter55_name: str | None = None,
        parameter55_value: str | None = None,
        parameter56_name: str | None = None,
        parameter56_value: str | None = None,
        parameter57_name: str | None = None,
        parameter57_value: str | None = None,
        parameter58_name: str | None = None,
        parameter58_value: str | None = None,
        parameter59_name: str | None = None,
        parameter59_value: str | None = None,
        parameter60_name: str | None = None,
        parameter60_value: str | None = None,
        parameter61_name: str | None = None,
        parameter61_value: str | None = None,
        parameter62_name: str | None = None,
        parameter62_value: str | None = None,
        parameter63_name: str | None = None,
        parameter63_value: str | None = None,
        parameter64_name: str | None = None,
        parameter64_value: str | None = None,
        parameter65_name: str | None = None,
        parameter65_value: str | None = None,
        parameter66_name: str | None = None,
        parameter66_value: str | None = None,
        parameter67_name: str | None = None,
        parameter67_value: str | None = None,
        parameter68_name: str | None = None,
        parameter68_value: str | None = None,
        parameter69_name: str | None = None,
        parameter69_value: str | None = None,
        parameter70_name: str | None = None,
        parameter70_value: str | None = None,
        parameter71_name: str | None = None,
        parameter71_value: str | None = None,
        parameter72_name: str | None = None,
        parameter72_value: str | None = None,
        parameter73_name: str | None = None,
        parameter73_value: str | None = None,
        parameter74_name: str | None = None,
        parameter74_value: str | None = None,
        parameter75_name: str | None = None,
        parameter75_value: str | None = None,
        parameter76_name: str | None = None,
        parameter76_value: str | None = None,
        parameter77_name: str | None = None,
        parameter77_value: str | None = None,
        parameter78_name: str | None = None,
        parameter78_value: str | None = None,
        parameter79_name: str | None = None,
        parameter79_value: str | None = None,
        parameter80_name: str | None = None,
        parameter80_value: str | None = None,
        parameter81_name: str | None = None,
        parameter81_value: str | None = None,
        parameter82_name: str | None = None,
        parameter82_value: str | None = None,
        parameter83_name: str | None = None,
        parameter83_value: str | None = None,
        parameter84_name: str | None = None,
        parameter84_value: str | None = None,
        parameter85_name: str | None = None,
        parameter85_value: str | None = None,
        parameter86_name: str | None = None,
        parameter86_value: str | None = None,
        parameter87_name: str | None = None,
        parameter87_value: str | None = None,
        parameter88_name: str | None = None,
        parameter88_value: str | None = None,
        parameter89_name: str | None = None,
        parameter89_value: str | None = None,
        parameter90_name: str | None = None,
        parameter90_value: str | None = None,
        parameter91_name: str | None = None,
        parameter91_value: str | None = None,
        parameter92_name: str | None = None,
        parameter92_value: str | None = None,
        parameter93_name: str | None = None,
        parameter93_value: str | None = None,
        parameter94_name: str | None = None,
        parameter94_value: str | None = None,
        parameter95_name: str | None = None,
        parameter95_value: str | None = None,
        parameter96_name: str | None = None,
        parameter96_value: str | None = None,
        parameter97_name: str | None = None,
        parameter97_value: str | None = None,
        parameter98_name: str | None = None,
        parameter98_value: str | None = None,
        parameter99_name: str | None = None,
        parameter99_value: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountCallSiprec, RawError]:
        """Create a Siprec

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created this
                Siprec resource.
            call_sid: The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the Siprec resource
                is associated with.
            name: The user-specified name of this Siprec, if one was given when the Siprec was created. This may be used
                to stop the Siprec.
            connector_name: Unique name used when configuring the connector via Marketplace Add-on.
            track: One of ``inbound_track``, ``outbound_track``, ``both_tracks``.
            status_callback: Absolute URL of the status callback.
            status_callback_method: The http method for the status_callback (one of GET, POST).
            parameter1_name: Parameter name
            parameter1_value: Parameter value
            parameter2_name: Parameter name
            parameter2_value: Parameter value
            parameter3_name: Parameter name
            parameter3_value: Parameter value
            parameter4_name: Parameter name
            parameter4_value: Parameter value
            parameter5_name: Parameter name
            parameter5_value: Parameter value
            parameter6_name: Parameter name
            parameter6_value: Parameter value
            parameter7_name: Parameter name
            parameter7_value: Parameter value
            parameter8_name: Parameter name
            parameter8_value: Parameter value
            parameter9_name: Parameter name
            parameter9_value: Parameter value
            parameter10_name: Parameter name
            parameter10_value: Parameter value
            parameter11_name: Parameter name
            parameter11_value: Parameter value
            parameter12_name: Parameter name
            parameter12_value: Parameter value
            parameter13_name: Parameter name
            parameter13_value: Parameter value
            parameter14_name: Parameter name
            parameter14_value: Parameter value
            parameter15_name: Parameter name
            parameter15_value: Parameter value
            parameter16_name: Parameter name
            parameter16_value: Parameter value
            parameter17_name: Parameter name
            parameter17_value: Parameter value
            parameter18_name: Parameter name
            parameter18_value: Parameter value
            parameter19_name: Parameter name
            parameter19_value: Parameter value
            parameter20_name: Parameter name
            parameter20_value: Parameter value
            parameter21_name: Parameter name
            parameter21_value: Parameter value
            parameter22_name: Parameter name
            parameter22_value: Parameter value
            parameter23_name: Parameter name
            parameter23_value: Parameter value
            parameter24_name: Parameter name
            parameter24_value: Parameter value
            parameter25_name: Parameter name
            parameter25_value: Parameter value
            parameter26_name: Parameter name
            parameter26_value: Parameter value
            parameter27_name: Parameter name
            parameter27_value: Parameter value
            parameter28_name: Parameter name
            parameter28_value: Parameter value
            parameter29_name: Parameter name
            parameter29_value: Parameter value
            parameter30_name: Parameter name
            parameter30_value: Parameter value
            parameter31_name: Parameter name
            parameter31_value: Parameter value
            parameter32_name: Parameter name
            parameter32_value: Parameter value
            parameter33_name: Parameter name
            parameter33_value: Parameter value
            parameter34_name: Parameter name
            parameter34_value: Parameter value
            parameter35_name: Parameter name
            parameter35_value: Parameter value
            parameter36_name: Parameter name
            parameter36_value: Parameter value
            parameter37_name: Parameter name
            parameter37_value: Parameter value
            parameter38_name: Parameter name
            parameter38_value: Parameter value
            parameter39_name: Parameter name
            parameter39_value: Parameter value
            parameter40_name: Parameter name
            parameter40_value: Parameter value
            parameter41_name: Parameter name
            parameter41_value: Parameter value
            parameter42_name: Parameter name
            parameter42_value: Parameter value
            parameter43_name: Parameter name
            parameter43_value: Parameter value
            parameter44_name: Parameter name
            parameter44_value: Parameter value
            parameter45_name: Parameter name
            parameter45_value: Parameter value
            parameter46_name: Parameter name
            parameter46_value: Parameter value
            parameter47_name: Parameter name
            parameter47_value: Parameter value
            parameter48_name: Parameter name
            parameter48_value: Parameter value
            parameter49_name: Parameter name
            parameter49_value: Parameter value
            parameter50_name: Parameter name
            parameter50_value: Parameter value
            parameter51_name: Parameter name
            parameter51_value: Parameter value
            parameter52_name: Parameter name
            parameter52_value: Parameter value
            parameter53_name: Parameter name
            parameter53_value: Parameter value
            parameter54_name: Parameter name
            parameter54_value: Parameter value
            parameter55_name: Parameter name
            parameter55_value: Parameter value
            parameter56_name: Parameter name
            parameter56_value: Parameter value
            parameter57_name: Parameter name
            parameter57_value: Parameter value
            parameter58_name: Parameter name
            parameter58_value: Parameter value
            parameter59_name: Parameter name
            parameter59_value: Parameter value
            parameter60_name: Parameter name
            parameter60_value: Parameter value
            parameter61_name: Parameter name
            parameter61_value: Parameter value
            parameter62_name: Parameter name
            parameter62_value: Parameter value
            parameter63_name: Parameter name
            parameter63_value: Parameter value
            parameter64_name: Parameter name
            parameter64_value: Parameter value
            parameter65_name: Parameter name
            parameter65_value: Parameter value
            parameter66_name: Parameter name
            parameter66_value: Parameter value
            parameter67_name: Parameter name
            parameter67_value: Parameter value
            parameter68_name: Parameter name
            parameter68_value: Parameter value
            parameter69_name: Parameter name
            parameter69_value: Parameter value
            parameter70_name: Parameter name
            parameter70_value: Parameter value
            parameter71_name: Parameter name
            parameter71_value: Parameter value
            parameter72_name: Parameter name
            parameter72_value: Parameter value
            parameter73_name: Parameter name
            parameter73_value: Parameter value
            parameter74_name: Parameter name
            parameter74_value: Parameter value
            parameter75_name: Parameter name
            parameter75_value: Parameter value
            parameter76_name: Parameter name
            parameter76_value: Parameter value
            parameter77_name: Parameter name
            parameter77_value: Parameter value
            parameter78_name: Parameter name
            parameter78_value: Parameter value
            parameter79_name: Parameter name
            parameter79_value: Parameter value
            parameter80_name: Parameter name
            parameter80_value: Parameter value
            parameter81_name: Parameter name
            parameter81_value: Parameter value
            parameter82_name: Parameter name
            parameter82_value: Parameter value
            parameter83_name: Parameter name
            parameter83_value: Parameter value
            parameter84_name: Parameter name
            parameter84_value: Parameter value
            parameter85_name: Parameter name
            parameter85_value: Parameter value
            parameter86_name: Parameter name
            parameter86_value: Parameter value
            parameter87_name: Parameter name
            parameter87_value: Parameter value
            parameter88_name: Parameter name
            parameter88_value: Parameter value
            parameter89_name: Parameter name
            parameter89_value: Parameter value
            parameter90_name: Parameter name
            parameter90_value: Parameter value
            parameter91_name: Parameter name
            parameter91_value: Parameter value
            parameter92_name: Parameter name
            parameter92_value: Parameter value
            parameter93_name: Parameter name
            parameter93_value: Parameter value
            parameter94_name: Parameter name
            parameter94_value: Parameter value
            parameter95_name: Parameter name
            parameter95_value: Parameter value
            parameter96_name: Parameter name
            parameter96_value: Parameter value
            parameter97_name: Parameter name
            parameter97_value: Parameter value
            parameter98_name: Parameter name
            parameter98_value: Parameter value
            parameter99_name: Parameter name
            parameter99_value: Parameter value
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Siprec.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("CallSid", call_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("Name", name),
                    param[str | None]("ConnectorName", connector_name),
                    param[SiprecEnumTrackOrStr | None]("Track", track),
                    param[str | None]("StatusCallback", status_callback),
                    param[StatusCallbackMethod17OrStr | None]("StatusCallbackMethod", status_callback_method),
                    param[str | None]("Parameter1.Name", parameter1_name),
                    param[str | None]("Parameter1.Value", parameter1_value),
                    param[str | None]("Parameter2.Name", parameter2_name),
                    param[str | None]("Parameter2.Value", parameter2_value),
                    param[str | None]("Parameter3.Name", parameter3_name),
                    param[str | None]("Parameter3.Value", parameter3_value),
                    param[str | None]("Parameter4.Name", parameter4_name),
                    param[str | None]("Parameter4.Value", parameter4_value),
                    param[str | None]("Parameter5.Name", parameter5_name),
                    param[str | None]("Parameter5.Value", parameter5_value),
                    param[str | None]("Parameter6.Name", parameter6_name),
                    param[str | None]("Parameter6.Value", parameter6_value),
                    param[str | None]("Parameter7.Name", parameter7_name),
                    param[str | None]("Parameter7.Value", parameter7_value),
                    param[str | None]("Parameter8.Name", parameter8_name),
                    param[str | None]("Parameter8.Value", parameter8_value),
                    param[str | None]("Parameter9.Name", parameter9_name),
                    param[str | None]("Parameter9.Value", parameter9_value),
                    param[str | None]("Parameter10.Name", parameter10_name),
                    param[str | None]("Parameter10.Value", parameter10_value),
                    param[str | None]("Parameter11.Name", parameter11_name),
                    param[str | None]("Parameter11.Value", parameter11_value),
                    param[str | None]("Parameter12.Name", parameter12_name),
                    param[str | None]("Parameter12.Value", parameter12_value),
                    param[str | None]("Parameter13.Name", parameter13_name),
                    param[str | None]("Parameter13.Value", parameter13_value),
                    param[str | None]("Parameter14.Name", parameter14_name),
                    param[str | None]("Parameter14.Value", parameter14_value),
                    param[str | None]("Parameter15.Name", parameter15_name),
                    param[str | None]("Parameter15.Value", parameter15_value),
                    param[str | None]("Parameter16.Name", parameter16_name),
                    param[str | None]("Parameter16.Value", parameter16_value),
                    param[str | None]("Parameter17.Name", parameter17_name),
                    param[str | None]("Parameter17.Value", parameter17_value),
                    param[str | None]("Parameter18.Name", parameter18_name),
                    param[str | None]("Parameter18.Value", parameter18_value),
                    param[str | None]("Parameter19.Name", parameter19_name),
                    param[str | None]("Parameter19.Value", parameter19_value),
                    param[str | None]("Parameter20.Name", parameter20_name),
                    param[str | None]("Parameter20.Value", parameter20_value),
                    param[str | None]("Parameter21.Name", parameter21_name),
                    param[str | None]("Parameter21.Value", parameter21_value),
                    param[str | None]("Parameter22.Name", parameter22_name),
                    param[str | None]("Parameter22.Value", parameter22_value),
                    param[str | None]("Parameter23.Name", parameter23_name),
                    param[str | None]("Parameter23.Value", parameter23_value),
                    param[str | None]("Parameter24.Name", parameter24_name),
                    param[str | None]("Parameter24.Value", parameter24_value),
                    param[str | None]("Parameter25.Name", parameter25_name),
                    param[str | None]("Parameter25.Value", parameter25_value),
                    param[str | None]("Parameter26.Name", parameter26_name),
                    param[str | None]("Parameter26.Value", parameter26_value),
                    param[str | None]("Parameter27.Name", parameter27_name),
                    param[str | None]("Parameter27.Value", parameter27_value),
                    param[str | None]("Parameter28.Name", parameter28_name),
                    param[str | None]("Parameter28.Value", parameter28_value),
                    param[str | None]("Parameter29.Name", parameter29_name),
                    param[str | None]("Parameter29.Value", parameter29_value),
                    param[str | None]("Parameter30.Name", parameter30_name),
                    param[str | None]("Parameter30.Value", parameter30_value),
                    param[str | None]("Parameter31.Name", parameter31_name),
                    param[str | None]("Parameter31.Value", parameter31_value),
                    param[str | None]("Parameter32.Name", parameter32_name),
                    param[str | None]("Parameter32.Value", parameter32_value),
                    param[str | None]("Parameter33.Name", parameter33_name),
                    param[str | None]("Parameter33.Value", parameter33_value),
                    param[str | None]("Parameter34.Name", parameter34_name),
                    param[str | None]("Parameter34.Value", parameter34_value),
                    param[str | None]("Parameter35.Name", parameter35_name),
                    param[str | None]("Parameter35.Value", parameter35_value),
                    param[str | None]("Parameter36.Name", parameter36_name),
                    param[str | None]("Parameter36.Value", parameter36_value),
                    param[str | None]("Parameter37.Name", parameter37_name),
                    param[str | None]("Parameter37.Value", parameter37_value),
                    param[str | None]("Parameter38.Name", parameter38_name),
                    param[str | None]("Parameter38.Value", parameter38_value),
                    param[str | None]("Parameter39.Name", parameter39_name),
                    param[str | None]("Parameter39.Value", parameter39_value),
                    param[str | None]("Parameter40.Name", parameter40_name),
                    param[str | None]("Parameter40.Value", parameter40_value),
                    param[str | None]("Parameter41.Name", parameter41_name),
                    param[str | None]("Parameter41.Value", parameter41_value),
                    param[str | None]("Parameter42.Name", parameter42_name),
                    param[str | None]("Parameter42.Value", parameter42_value),
                    param[str | None]("Parameter43.Name", parameter43_name),
                    param[str | None]("Parameter43.Value", parameter43_value),
                    param[str | None]("Parameter44.Name", parameter44_name),
                    param[str | None]("Parameter44.Value", parameter44_value),
                    param[str | None]("Parameter45.Name", parameter45_name),
                    param[str | None]("Parameter45.Value", parameter45_value),
                    param[str | None]("Parameter46.Name", parameter46_name),
                    param[str | None]("Parameter46.Value", parameter46_value),
                    param[str | None]("Parameter47.Name", parameter47_name),
                    param[str | None]("Parameter47.Value", parameter47_value),
                    param[str | None]("Parameter48.Name", parameter48_name),
                    param[str | None]("Parameter48.Value", parameter48_value),
                    param[str | None]("Parameter49.Name", parameter49_name),
                    param[str | None]("Parameter49.Value", parameter49_value),
                    param[str | None]("Parameter50.Name", parameter50_name),
                    param[str | None]("Parameter50.Value", parameter50_value),
                    param[str | None]("Parameter51.Name", parameter51_name),
                    param[str | None]("Parameter51.Value", parameter51_value),
                    param[str | None]("Parameter52.Name", parameter52_name),
                    param[str | None]("Parameter52.Value", parameter52_value),
                    param[str | None]("Parameter53.Name", parameter53_name),
                    param[str | None]("Parameter53.Value", parameter53_value),
                    param[str | None]("Parameter54.Name", parameter54_name),
                    param[str | None]("Parameter54.Value", parameter54_value),
                    param[str | None]("Parameter55.Name", parameter55_name),
                    param[str | None]("Parameter55.Value", parameter55_value),
                    param[str | None]("Parameter56.Name", parameter56_name),
                    param[str | None]("Parameter56.Value", parameter56_value),
                    param[str | None]("Parameter57.Name", parameter57_name),
                    param[str | None]("Parameter57.Value", parameter57_value),
                    param[str | None]("Parameter58.Name", parameter58_name),
                    param[str | None]("Parameter58.Value", parameter58_value),
                    param[str | None]("Parameter59.Name", parameter59_name),
                    param[str | None]("Parameter59.Value", parameter59_value),
                    param[str | None]("Parameter60.Name", parameter60_name),
                    param[str | None]("Parameter60.Value", parameter60_value),
                    param[str | None]("Parameter61.Name", parameter61_name),
                    param[str | None]("Parameter61.Value", parameter61_value),
                    param[str | None]("Parameter62.Name", parameter62_name),
                    param[str | None]("Parameter62.Value", parameter62_value),
                    param[str | None]("Parameter63.Name", parameter63_name),
                    param[str | None]("Parameter63.Value", parameter63_value),
                    param[str | None]("Parameter64.Name", parameter64_name),
                    param[str | None]("Parameter64.Value", parameter64_value),
                    param[str | None]("Parameter65.Name", parameter65_name),
                    param[str | None]("Parameter65.Value", parameter65_value),
                    param[str | None]("Parameter66.Name", parameter66_name),
                    param[str | None]("Parameter66.Value", parameter66_value),
                    param[str | None]("Parameter67.Name", parameter67_name),
                    param[str | None]("Parameter67.Value", parameter67_value),
                    param[str | None]("Parameter68.Name", parameter68_name),
                    param[str | None]("Parameter68.Value", parameter68_value),
                    param[str | None]("Parameter69.Name", parameter69_name),
                    param[str | None]("Parameter69.Value", parameter69_value),
                    param[str | None]("Parameter70.Name", parameter70_name),
                    param[str | None]("Parameter70.Value", parameter70_value),
                    param[str | None]("Parameter71.Name", parameter71_name),
                    param[str | None]("Parameter71.Value", parameter71_value),
                    param[str | None]("Parameter72.Name", parameter72_name),
                    param[str | None]("Parameter72.Value", parameter72_value),
                    param[str | None]("Parameter73.Name", parameter73_name),
                    param[str | None]("Parameter73.Value", parameter73_value),
                    param[str | None]("Parameter74.Name", parameter74_name),
                    param[str | None]("Parameter74.Value", parameter74_value),
                    param[str | None]("Parameter75.Name", parameter75_name),
                    param[str | None]("Parameter75.Value", parameter75_value),
                    param[str | None]("Parameter76.Name", parameter76_name),
                    param[str | None]("Parameter76.Value", parameter76_value),
                    param[str | None]("Parameter77.Name", parameter77_name),
                    param[str | None]("Parameter77.Value", parameter77_value),
                    param[str | None]("Parameter78.Name", parameter78_name),
                    param[str | None]("Parameter78.Value", parameter78_value),
                    param[str | None]("Parameter79.Name", parameter79_name),
                    param[str | None]("Parameter79.Value", parameter79_value),
                    param[str | None]("Parameter80.Name", parameter80_name),
                    param[str | None]("Parameter80.Value", parameter80_value),
                    param[str | None]("Parameter81.Name", parameter81_name),
                    param[str | None]("Parameter81.Value", parameter81_value),
                    param[str | None]("Parameter82.Name", parameter82_name),
                    param[str | None]("Parameter82.Value", parameter82_value),
                    param[str | None]("Parameter83.Name", parameter83_name),
                    param[str | None]("Parameter83.Value", parameter83_value),
                    param[str | None]("Parameter84.Name", parameter84_name),
                    param[str | None]("Parameter84.Value", parameter84_value),
                    param[str | None]("Parameter85.Name", parameter85_name),
                    param[str | None]("Parameter85.Value", parameter85_value),
                    param[str | None]("Parameter86.Name", parameter86_name),
                    param[str | None]("Parameter86.Value", parameter86_value),
                    param[str | None]("Parameter87.Name", parameter87_name),
                    param[str | None]("Parameter87.Value", parameter87_value),
                    param[str | None]("Parameter88.Name", parameter88_name),
                    param[str | None]("Parameter88.Value", parameter88_value),
                    param[str | None]("Parameter89.Name", parameter89_name),
                    param[str | None]("Parameter89.Value", parameter89_value),
                    param[str | None]("Parameter90.Name", parameter90_name),
                    param[str | None]("Parameter90.Value", parameter90_value),
                    param[str | None]("Parameter91.Name", parameter91_name),
                    param[str | None]("Parameter91.Value", parameter91_value),
                    param[str | None]("Parameter92.Name", parameter92_name),
                    param[str | None]("Parameter92.Value", parameter92_value),
                    param[str | None]("Parameter93.Name", parameter93_name),
                    param[str | None]("Parameter93.Value", parameter93_value),
                    param[str | None]("Parameter94.Name", parameter94_name),
                    param[str | None]("Parameter94.Value", parameter94_value),
                    param[str | None]("Parameter95.Name", parameter95_name),
                    param[str | None]("Parameter95.Value", parameter95_value),
                    param[str | None]("Parameter96.Name", parameter96_name),
                    param[str | None]("Parameter96.Value", parameter96_value),
                    param[str | None]("Parameter97.Name", parameter97_name),
                    param[str | None]("Parameter97.Value", parameter97_value),
                    param[str | None]("Parameter98.Name", parameter98_name),
                    param[str | None]("Parameter98.Value", parameter98_value),
                    param[str | None]("Parameter99.Name", parameter99_name),
                    param[str | None]("Parameter99.Value", parameter99_value),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountCallSiprec],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_siprec(
        self,
        account_sid: str,
        call_sid: str,
        sid: str,
        status: SiprecEnumUpdateStatusOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountCallSiprec, RawError]:
        """Stop a Siprec using either the SID of the Siprec resource or the ``name`` used when creating the resource

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created this
                Siprec resource.
            call_sid: The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the Siprec resource
                is associated with.
            sid: The SID of the Siprec resource, or the ``name`` used when creating the resource
            status: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Siprec/{Sid}.json"),
            path_params=[
                param[str]("AccountSid", account_sid), param[str]("CallSid", call_sid), param[str]("Sid", sid)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[SiprecEnumUpdateStatusOrStr]("Status", status)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountCallSiprec],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401SiprecWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_siprec(
        self,
        account_sid: str,
        call_sid: str,
        *,
        name: str | None = None,
        connector_name: str | None = None,
        track: SiprecEnumTrackOrStr | None = None,
        status_callback: str | None = None,
        status_callback_method: StatusCallbackMethod17OrStr | None = None,
        parameter1_name: str | None = None,
        parameter1_value: str | None = None,
        parameter2_name: str | None = None,
        parameter2_value: str | None = None,
        parameter3_name: str | None = None,
        parameter3_value: str | None = None,
        parameter4_name: str | None = None,
        parameter4_value: str | None = None,
        parameter5_name: str | None = None,
        parameter5_value: str | None = None,
        parameter6_name: str | None = None,
        parameter6_value: str | None = None,
        parameter7_name: str | None = None,
        parameter7_value: str | None = None,
        parameter8_name: str | None = None,
        parameter8_value: str | None = None,
        parameter9_name: str | None = None,
        parameter9_value: str | None = None,
        parameter10_name: str | None = None,
        parameter10_value: str | None = None,
        parameter11_name: str | None = None,
        parameter11_value: str | None = None,
        parameter12_name: str | None = None,
        parameter12_value: str | None = None,
        parameter13_name: str | None = None,
        parameter13_value: str | None = None,
        parameter14_name: str | None = None,
        parameter14_value: str | None = None,
        parameter15_name: str | None = None,
        parameter15_value: str | None = None,
        parameter16_name: str | None = None,
        parameter16_value: str | None = None,
        parameter17_name: str | None = None,
        parameter17_value: str | None = None,
        parameter18_name: str | None = None,
        parameter18_value: str | None = None,
        parameter19_name: str | None = None,
        parameter19_value: str | None = None,
        parameter20_name: str | None = None,
        parameter20_value: str | None = None,
        parameter21_name: str | None = None,
        parameter21_value: str | None = None,
        parameter22_name: str | None = None,
        parameter22_value: str | None = None,
        parameter23_name: str | None = None,
        parameter23_value: str | None = None,
        parameter24_name: str | None = None,
        parameter24_value: str | None = None,
        parameter25_name: str | None = None,
        parameter25_value: str | None = None,
        parameter26_name: str | None = None,
        parameter26_value: str | None = None,
        parameter27_name: str | None = None,
        parameter27_value: str | None = None,
        parameter28_name: str | None = None,
        parameter28_value: str | None = None,
        parameter29_name: str | None = None,
        parameter29_value: str | None = None,
        parameter30_name: str | None = None,
        parameter30_value: str | None = None,
        parameter31_name: str | None = None,
        parameter31_value: str | None = None,
        parameter32_name: str | None = None,
        parameter32_value: str | None = None,
        parameter33_name: str | None = None,
        parameter33_value: str | None = None,
        parameter34_name: str | None = None,
        parameter34_value: str | None = None,
        parameter35_name: str | None = None,
        parameter35_value: str | None = None,
        parameter36_name: str | None = None,
        parameter36_value: str | None = None,
        parameter37_name: str | None = None,
        parameter37_value: str | None = None,
        parameter38_name: str | None = None,
        parameter38_value: str | None = None,
        parameter39_name: str | None = None,
        parameter39_value: str | None = None,
        parameter40_name: str | None = None,
        parameter40_value: str | None = None,
        parameter41_name: str | None = None,
        parameter41_value: str | None = None,
        parameter42_name: str | None = None,
        parameter42_value: str | None = None,
        parameter43_name: str | None = None,
        parameter43_value: str | None = None,
        parameter44_name: str | None = None,
        parameter44_value: str | None = None,
        parameter45_name: str | None = None,
        parameter45_value: str | None = None,
        parameter46_name: str | None = None,
        parameter46_value: str | None = None,
        parameter47_name: str | None = None,
        parameter47_value: str | None = None,
        parameter48_name: str | None = None,
        parameter48_value: str | None = None,
        parameter49_name: str | None = None,
        parameter49_value: str | None = None,
        parameter50_name: str | None = None,
        parameter50_value: str | None = None,
        parameter51_name: str | None = None,
        parameter51_value: str | None = None,
        parameter52_name: str | None = None,
        parameter52_value: str | None = None,
        parameter53_name: str | None = None,
        parameter53_value: str | None = None,
        parameter54_name: str | None = None,
        parameter54_value: str | None = None,
        parameter55_name: str | None = None,
        parameter55_value: str | None = None,
        parameter56_name: str | None = None,
        parameter56_value: str | None = None,
        parameter57_name: str | None = None,
        parameter57_value: str | None = None,
        parameter58_name: str | None = None,
        parameter58_value: str | None = None,
        parameter59_name: str | None = None,
        parameter59_value: str | None = None,
        parameter60_name: str | None = None,
        parameter60_value: str | None = None,
        parameter61_name: str | None = None,
        parameter61_value: str | None = None,
        parameter62_name: str | None = None,
        parameter62_value: str | None = None,
        parameter63_name: str | None = None,
        parameter63_value: str | None = None,
        parameter64_name: str | None = None,
        parameter64_value: str | None = None,
        parameter65_name: str | None = None,
        parameter65_value: str | None = None,
        parameter66_name: str | None = None,
        parameter66_value: str | None = None,
        parameter67_name: str | None = None,
        parameter67_value: str | None = None,
        parameter68_name: str | None = None,
        parameter68_value: str | None = None,
        parameter69_name: str | None = None,
        parameter69_value: str | None = None,
        parameter70_name: str | None = None,
        parameter70_value: str | None = None,
        parameter71_name: str | None = None,
        parameter71_value: str | None = None,
        parameter72_name: str | None = None,
        parameter72_value: str | None = None,
        parameter73_name: str | None = None,
        parameter73_value: str | None = None,
        parameter74_name: str | None = None,
        parameter74_value: str | None = None,
        parameter75_name: str | None = None,
        parameter75_value: str | None = None,
        parameter76_name: str | None = None,
        parameter76_value: str | None = None,
        parameter77_name: str | None = None,
        parameter77_value: str | None = None,
        parameter78_name: str | None = None,
        parameter78_value: str | None = None,
        parameter79_name: str | None = None,
        parameter79_value: str | None = None,
        parameter80_name: str | None = None,
        parameter80_value: str | None = None,
        parameter81_name: str | None = None,
        parameter81_value: str | None = None,
        parameter82_name: str | None = None,
        parameter82_value: str | None = None,
        parameter83_name: str | None = None,
        parameter83_value: str | None = None,
        parameter84_name: str | None = None,
        parameter84_value: str | None = None,
        parameter85_name: str | None = None,
        parameter85_value: str | None = None,
        parameter86_name: str | None = None,
        parameter86_value: str | None = None,
        parameter87_name: str | None = None,
        parameter87_value: str | None = None,
        parameter88_name: str | None = None,
        parameter88_value: str | None = None,
        parameter89_name: str | None = None,
        parameter89_value: str | None = None,
        parameter90_name: str | None = None,
        parameter90_value: str | None = None,
        parameter91_name: str | None = None,
        parameter91_value: str | None = None,
        parameter92_name: str | None = None,
        parameter92_value: str | None = None,
        parameter93_name: str | None = None,
        parameter93_value: str | None = None,
        parameter94_name: str | None = None,
        parameter94_value: str | None = None,
        parameter95_name: str | None = None,
        parameter95_value: str | None = None,
        parameter96_name: str | None = None,
        parameter96_value: str | None = None,
        parameter97_name: str | None = None,
        parameter97_value: str | None = None,
        parameter98_name: str | None = None,
        parameter98_value: str | None = None,
        parameter99_name: str | None = None,
        parameter99_value: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountCallSiprec, RawError]:
        """Create a Siprec

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created this
                Siprec resource.
            call_sid: The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the Siprec resource
                is associated with.
            name: The user-specified name of this Siprec, if one was given when the Siprec was created. This may be used
                to stop the Siprec.
            connector_name: Unique name used when configuring the connector via Marketplace Add-on.
            track: One of ``inbound_track``, ``outbound_track``, ``both_tracks``.
            status_callback: Absolute URL of the status callback.
            status_callback_method: The http method for the status_callback (one of GET, POST).
            parameter1_name: Parameter name
            parameter1_value: Parameter value
            parameter2_name: Parameter name
            parameter2_value: Parameter value
            parameter3_name: Parameter name
            parameter3_value: Parameter value
            parameter4_name: Parameter name
            parameter4_value: Parameter value
            parameter5_name: Parameter name
            parameter5_value: Parameter value
            parameter6_name: Parameter name
            parameter6_value: Parameter value
            parameter7_name: Parameter name
            parameter7_value: Parameter value
            parameter8_name: Parameter name
            parameter8_value: Parameter value
            parameter9_name: Parameter name
            parameter9_value: Parameter value
            parameter10_name: Parameter name
            parameter10_value: Parameter value
            parameter11_name: Parameter name
            parameter11_value: Parameter value
            parameter12_name: Parameter name
            parameter12_value: Parameter value
            parameter13_name: Parameter name
            parameter13_value: Parameter value
            parameter14_name: Parameter name
            parameter14_value: Parameter value
            parameter15_name: Parameter name
            parameter15_value: Parameter value
            parameter16_name: Parameter name
            parameter16_value: Parameter value
            parameter17_name: Parameter name
            parameter17_value: Parameter value
            parameter18_name: Parameter name
            parameter18_value: Parameter value
            parameter19_name: Parameter name
            parameter19_value: Parameter value
            parameter20_name: Parameter name
            parameter20_value: Parameter value
            parameter21_name: Parameter name
            parameter21_value: Parameter value
            parameter22_name: Parameter name
            parameter22_value: Parameter value
            parameter23_name: Parameter name
            parameter23_value: Parameter value
            parameter24_name: Parameter name
            parameter24_value: Parameter value
            parameter25_name: Parameter name
            parameter25_value: Parameter value
            parameter26_name: Parameter name
            parameter26_value: Parameter value
            parameter27_name: Parameter name
            parameter27_value: Parameter value
            parameter28_name: Parameter name
            parameter28_value: Parameter value
            parameter29_name: Parameter name
            parameter29_value: Parameter value
            parameter30_name: Parameter name
            parameter30_value: Parameter value
            parameter31_name: Parameter name
            parameter31_value: Parameter value
            parameter32_name: Parameter name
            parameter32_value: Parameter value
            parameter33_name: Parameter name
            parameter33_value: Parameter value
            parameter34_name: Parameter name
            parameter34_value: Parameter value
            parameter35_name: Parameter name
            parameter35_value: Parameter value
            parameter36_name: Parameter name
            parameter36_value: Parameter value
            parameter37_name: Parameter name
            parameter37_value: Parameter value
            parameter38_name: Parameter name
            parameter38_value: Parameter value
            parameter39_name: Parameter name
            parameter39_value: Parameter value
            parameter40_name: Parameter name
            parameter40_value: Parameter value
            parameter41_name: Parameter name
            parameter41_value: Parameter value
            parameter42_name: Parameter name
            parameter42_value: Parameter value
            parameter43_name: Parameter name
            parameter43_value: Parameter value
            parameter44_name: Parameter name
            parameter44_value: Parameter value
            parameter45_name: Parameter name
            parameter45_value: Parameter value
            parameter46_name: Parameter name
            parameter46_value: Parameter value
            parameter47_name: Parameter name
            parameter47_value: Parameter value
            parameter48_name: Parameter name
            parameter48_value: Parameter value
            parameter49_name: Parameter name
            parameter49_value: Parameter value
            parameter50_name: Parameter name
            parameter50_value: Parameter value
            parameter51_name: Parameter name
            parameter51_value: Parameter value
            parameter52_name: Parameter name
            parameter52_value: Parameter value
            parameter53_name: Parameter name
            parameter53_value: Parameter value
            parameter54_name: Parameter name
            parameter54_value: Parameter value
            parameter55_name: Parameter name
            parameter55_value: Parameter value
            parameter56_name: Parameter name
            parameter56_value: Parameter value
            parameter57_name: Parameter name
            parameter57_value: Parameter value
            parameter58_name: Parameter name
            parameter58_value: Parameter value
            parameter59_name: Parameter name
            parameter59_value: Parameter value
            parameter60_name: Parameter name
            parameter60_value: Parameter value
            parameter61_name: Parameter name
            parameter61_value: Parameter value
            parameter62_name: Parameter name
            parameter62_value: Parameter value
            parameter63_name: Parameter name
            parameter63_value: Parameter value
            parameter64_name: Parameter name
            parameter64_value: Parameter value
            parameter65_name: Parameter name
            parameter65_value: Parameter value
            parameter66_name: Parameter name
            parameter66_value: Parameter value
            parameter67_name: Parameter name
            parameter67_value: Parameter value
            parameter68_name: Parameter name
            parameter68_value: Parameter value
            parameter69_name: Parameter name
            parameter69_value: Parameter value
            parameter70_name: Parameter name
            parameter70_value: Parameter value
            parameter71_name: Parameter name
            parameter71_value: Parameter value
            parameter72_name: Parameter name
            parameter72_value: Parameter value
            parameter73_name: Parameter name
            parameter73_value: Parameter value
            parameter74_name: Parameter name
            parameter74_value: Parameter value
            parameter75_name: Parameter name
            parameter75_value: Parameter value
            parameter76_name: Parameter name
            parameter76_value: Parameter value
            parameter77_name: Parameter name
            parameter77_value: Parameter value
            parameter78_name: Parameter name
            parameter78_value: Parameter value
            parameter79_name: Parameter name
            parameter79_value: Parameter value
            parameter80_name: Parameter name
            parameter80_value: Parameter value
            parameter81_name: Parameter name
            parameter81_value: Parameter value
            parameter82_name: Parameter name
            parameter82_value: Parameter value
            parameter83_name: Parameter name
            parameter83_value: Parameter value
            parameter84_name: Parameter name
            parameter84_value: Parameter value
            parameter85_name: Parameter name
            parameter85_value: Parameter value
            parameter86_name: Parameter name
            parameter86_value: Parameter value
            parameter87_name: Parameter name
            parameter87_value: Parameter value
            parameter88_name: Parameter name
            parameter88_value: Parameter value
            parameter89_name: Parameter name
            parameter89_value: Parameter value
            parameter90_name: Parameter name
            parameter90_value: Parameter value
            parameter91_name: Parameter name
            parameter91_value: Parameter value
            parameter92_name: Parameter name
            parameter92_value: Parameter value
            parameter93_name: Parameter name
            parameter93_value: Parameter value
            parameter94_name: Parameter name
            parameter94_value: Parameter value
            parameter95_name: Parameter name
            parameter95_value: Parameter value
            parameter96_name: Parameter name
            parameter96_value: Parameter value
            parameter97_name: Parameter name
            parameter97_value: Parameter value
            parameter98_name: Parameter name
            parameter98_value: Parameter value
            parameter99_name: Parameter name
            parameter99_value: Parameter value
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Siprec.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("CallSid", call_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("Name", name),
                    param[str | None]("ConnectorName", connector_name),
                    param[SiprecEnumTrackOrStr | None]("Track", track),
                    param[str | None]("StatusCallback", status_callback),
                    param[StatusCallbackMethod17OrStr | None]("StatusCallbackMethod", status_callback_method),
                    param[str | None]("Parameter1.Name", parameter1_name),
                    param[str | None]("Parameter1.Value", parameter1_value),
                    param[str | None]("Parameter2.Name", parameter2_name),
                    param[str | None]("Parameter2.Value", parameter2_value),
                    param[str | None]("Parameter3.Name", parameter3_name),
                    param[str | None]("Parameter3.Value", parameter3_value),
                    param[str | None]("Parameter4.Name", parameter4_name),
                    param[str | None]("Parameter4.Value", parameter4_value),
                    param[str | None]("Parameter5.Name", parameter5_name),
                    param[str | None]("Parameter5.Value", parameter5_value),
                    param[str | None]("Parameter6.Name", parameter6_name),
                    param[str | None]("Parameter6.Value", parameter6_value),
                    param[str | None]("Parameter7.Name", parameter7_name),
                    param[str | None]("Parameter7.Value", parameter7_value),
                    param[str | None]("Parameter8.Name", parameter8_name),
                    param[str | None]("Parameter8.Value", parameter8_value),
                    param[str | None]("Parameter9.Name", parameter9_name),
                    param[str | None]("Parameter9.Value", parameter9_value),
                    param[str | None]("Parameter10.Name", parameter10_name),
                    param[str | None]("Parameter10.Value", parameter10_value),
                    param[str | None]("Parameter11.Name", parameter11_name),
                    param[str | None]("Parameter11.Value", parameter11_value),
                    param[str | None]("Parameter12.Name", parameter12_name),
                    param[str | None]("Parameter12.Value", parameter12_value),
                    param[str | None]("Parameter13.Name", parameter13_name),
                    param[str | None]("Parameter13.Value", parameter13_value),
                    param[str | None]("Parameter14.Name", parameter14_name),
                    param[str | None]("Parameter14.Value", parameter14_value),
                    param[str | None]("Parameter15.Name", parameter15_name),
                    param[str | None]("Parameter15.Value", parameter15_value),
                    param[str | None]("Parameter16.Name", parameter16_name),
                    param[str | None]("Parameter16.Value", parameter16_value),
                    param[str | None]("Parameter17.Name", parameter17_name),
                    param[str | None]("Parameter17.Value", parameter17_value),
                    param[str | None]("Parameter18.Name", parameter18_name),
                    param[str | None]("Parameter18.Value", parameter18_value),
                    param[str | None]("Parameter19.Name", parameter19_name),
                    param[str | None]("Parameter19.Value", parameter19_value),
                    param[str | None]("Parameter20.Name", parameter20_name),
                    param[str | None]("Parameter20.Value", parameter20_value),
                    param[str | None]("Parameter21.Name", parameter21_name),
                    param[str | None]("Parameter21.Value", parameter21_value),
                    param[str | None]("Parameter22.Name", parameter22_name),
                    param[str | None]("Parameter22.Value", parameter22_value),
                    param[str | None]("Parameter23.Name", parameter23_name),
                    param[str | None]("Parameter23.Value", parameter23_value),
                    param[str | None]("Parameter24.Name", parameter24_name),
                    param[str | None]("Parameter24.Value", parameter24_value),
                    param[str | None]("Parameter25.Name", parameter25_name),
                    param[str | None]("Parameter25.Value", parameter25_value),
                    param[str | None]("Parameter26.Name", parameter26_name),
                    param[str | None]("Parameter26.Value", parameter26_value),
                    param[str | None]("Parameter27.Name", parameter27_name),
                    param[str | None]("Parameter27.Value", parameter27_value),
                    param[str | None]("Parameter28.Name", parameter28_name),
                    param[str | None]("Parameter28.Value", parameter28_value),
                    param[str | None]("Parameter29.Name", parameter29_name),
                    param[str | None]("Parameter29.Value", parameter29_value),
                    param[str | None]("Parameter30.Name", parameter30_name),
                    param[str | None]("Parameter30.Value", parameter30_value),
                    param[str | None]("Parameter31.Name", parameter31_name),
                    param[str | None]("Parameter31.Value", parameter31_value),
                    param[str | None]("Parameter32.Name", parameter32_name),
                    param[str | None]("Parameter32.Value", parameter32_value),
                    param[str | None]("Parameter33.Name", parameter33_name),
                    param[str | None]("Parameter33.Value", parameter33_value),
                    param[str | None]("Parameter34.Name", parameter34_name),
                    param[str | None]("Parameter34.Value", parameter34_value),
                    param[str | None]("Parameter35.Name", parameter35_name),
                    param[str | None]("Parameter35.Value", parameter35_value),
                    param[str | None]("Parameter36.Name", parameter36_name),
                    param[str | None]("Parameter36.Value", parameter36_value),
                    param[str | None]("Parameter37.Name", parameter37_name),
                    param[str | None]("Parameter37.Value", parameter37_value),
                    param[str | None]("Parameter38.Name", parameter38_name),
                    param[str | None]("Parameter38.Value", parameter38_value),
                    param[str | None]("Parameter39.Name", parameter39_name),
                    param[str | None]("Parameter39.Value", parameter39_value),
                    param[str | None]("Parameter40.Name", parameter40_name),
                    param[str | None]("Parameter40.Value", parameter40_value),
                    param[str | None]("Parameter41.Name", parameter41_name),
                    param[str | None]("Parameter41.Value", parameter41_value),
                    param[str | None]("Parameter42.Name", parameter42_name),
                    param[str | None]("Parameter42.Value", parameter42_value),
                    param[str | None]("Parameter43.Name", parameter43_name),
                    param[str | None]("Parameter43.Value", parameter43_value),
                    param[str | None]("Parameter44.Name", parameter44_name),
                    param[str | None]("Parameter44.Value", parameter44_value),
                    param[str | None]("Parameter45.Name", parameter45_name),
                    param[str | None]("Parameter45.Value", parameter45_value),
                    param[str | None]("Parameter46.Name", parameter46_name),
                    param[str | None]("Parameter46.Value", parameter46_value),
                    param[str | None]("Parameter47.Name", parameter47_name),
                    param[str | None]("Parameter47.Value", parameter47_value),
                    param[str | None]("Parameter48.Name", parameter48_name),
                    param[str | None]("Parameter48.Value", parameter48_value),
                    param[str | None]("Parameter49.Name", parameter49_name),
                    param[str | None]("Parameter49.Value", parameter49_value),
                    param[str | None]("Parameter50.Name", parameter50_name),
                    param[str | None]("Parameter50.Value", parameter50_value),
                    param[str | None]("Parameter51.Name", parameter51_name),
                    param[str | None]("Parameter51.Value", parameter51_value),
                    param[str | None]("Parameter52.Name", parameter52_name),
                    param[str | None]("Parameter52.Value", parameter52_value),
                    param[str | None]("Parameter53.Name", parameter53_name),
                    param[str | None]("Parameter53.Value", parameter53_value),
                    param[str | None]("Parameter54.Name", parameter54_name),
                    param[str | None]("Parameter54.Value", parameter54_value),
                    param[str | None]("Parameter55.Name", parameter55_name),
                    param[str | None]("Parameter55.Value", parameter55_value),
                    param[str | None]("Parameter56.Name", parameter56_name),
                    param[str | None]("Parameter56.Value", parameter56_value),
                    param[str | None]("Parameter57.Name", parameter57_name),
                    param[str | None]("Parameter57.Value", parameter57_value),
                    param[str | None]("Parameter58.Name", parameter58_name),
                    param[str | None]("Parameter58.Value", parameter58_value),
                    param[str | None]("Parameter59.Name", parameter59_name),
                    param[str | None]("Parameter59.Value", parameter59_value),
                    param[str | None]("Parameter60.Name", parameter60_name),
                    param[str | None]("Parameter60.Value", parameter60_value),
                    param[str | None]("Parameter61.Name", parameter61_name),
                    param[str | None]("Parameter61.Value", parameter61_value),
                    param[str | None]("Parameter62.Name", parameter62_name),
                    param[str | None]("Parameter62.Value", parameter62_value),
                    param[str | None]("Parameter63.Name", parameter63_name),
                    param[str | None]("Parameter63.Value", parameter63_value),
                    param[str | None]("Parameter64.Name", parameter64_name),
                    param[str | None]("Parameter64.Value", parameter64_value),
                    param[str | None]("Parameter65.Name", parameter65_name),
                    param[str | None]("Parameter65.Value", parameter65_value),
                    param[str | None]("Parameter66.Name", parameter66_name),
                    param[str | None]("Parameter66.Value", parameter66_value),
                    param[str | None]("Parameter67.Name", parameter67_name),
                    param[str | None]("Parameter67.Value", parameter67_value),
                    param[str | None]("Parameter68.Name", parameter68_name),
                    param[str | None]("Parameter68.Value", parameter68_value),
                    param[str | None]("Parameter69.Name", parameter69_name),
                    param[str | None]("Parameter69.Value", parameter69_value),
                    param[str | None]("Parameter70.Name", parameter70_name),
                    param[str | None]("Parameter70.Value", parameter70_value),
                    param[str | None]("Parameter71.Name", parameter71_name),
                    param[str | None]("Parameter71.Value", parameter71_value),
                    param[str | None]("Parameter72.Name", parameter72_name),
                    param[str | None]("Parameter72.Value", parameter72_value),
                    param[str | None]("Parameter73.Name", parameter73_name),
                    param[str | None]("Parameter73.Value", parameter73_value),
                    param[str | None]("Parameter74.Name", parameter74_name),
                    param[str | None]("Parameter74.Value", parameter74_value),
                    param[str | None]("Parameter75.Name", parameter75_name),
                    param[str | None]("Parameter75.Value", parameter75_value),
                    param[str | None]("Parameter76.Name", parameter76_name),
                    param[str | None]("Parameter76.Value", parameter76_value),
                    param[str | None]("Parameter77.Name", parameter77_name),
                    param[str | None]("Parameter77.Value", parameter77_value),
                    param[str | None]("Parameter78.Name", parameter78_name),
                    param[str | None]("Parameter78.Value", parameter78_value),
                    param[str | None]("Parameter79.Name", parameter79_name),
                    param[str | None]("Parameter79.Value", parameter79_value),
                    param[str | None]("Parameter80.Name", parameter80_name),
                    param[str | None]("Parameter80.Value", parameter80_value),
                    param[str | None]("Parameter81.Name", parameter81_name),
                    param[str | None]("Parameter81.Value", parameter81_value),
                    param[str | None]("Parameter82.Name", parameter82_name),
                    param[str | None]("Parameter82.Value", parameter82_value),
                    param[str | None]("Parameter83.Name", parameter83_name),
                    param[str | None]("Parameter83.Value", parameter83_value),
                    param[str | None]("Parameter84.Name", parameter84_name),
                    param[str | None]("Parameter84.Value", parameter84_value),
                    param[str | None]("Parameter85.Name", parameter85_name),
                    param[str | None]("Parameter85.Value", parameter85_value),
                    param[str | None]("Parameter86.Name", parameter86_name),
                    param[str | None]("Parameter86.Value", parameter86_value),
                    param[str | None]("Parameter87.Name", parameter87_name),
                    param[str | None]("Parameter87.Value", parameter87_value),
                    param[str | None]("Parameter88.Name", parameter88_name),
                    param[str | None]("Parameter88.Value", parameter88_value),
                    param[str | None]("Parameter89.Name", parameter89_name),
                    param[str | None]("Parameter89.Value", parameter89_value),
                    param[str | None]("Parameter90.Name", parameter90_name),
                    param[str | None]("Parameter90.Value", parameter90_value),
                    param[str | None]("Parameter91.Name", parameter91_name),
                    param[str | None]("Parameter91.Value", parameter91_value),
                    param[str | None]("Parameter92.Name", parameter92_name),
                    param[str | None]("Parameter92.Value", parameter92_value),
                    param[str | None]("Parameter93.Name", parameter93_name),
                    param[str | None]("Parameter93.Value", parameter93_value),
                    param[str | None]("Parameter94.Name", parameter94_name),
                    param[str | None]("Parameter94.Value", parameter94_value),
                    param[str | None]("Parameter95.Name", parameter95_name),
                    param[str | None]("Parameter95.Value", parameter95_value),
                    param[str | None]("Parameter96.Name", parameter96_name),
                    param[str | None]("Parameter96.Value", parameter96_value),
                    param[str | None]("Parameter97.Name", parameter97_name),
                    param[str | None]("Parameter97.Value", parameter97_value),
                    param[str | None]("Parameter98.Name", parameter98_name),
                    param[str | None]("Parameter98.Value", parameter98_value),
                    param[str | None]("Parameter99.Name", parameter99_name),
                    param[str | None]("Parameter99.Value", parameter99_value),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountCallSiprec],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_siprec(
        self,
        account_sid: str,
        call_sid: str,
        sid: str,
        status: SiprecEnumUpdateStatusOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountCallSiprec, RawError]:
        """Stop a Siprec using either the SID of the Siprec resource or the ``name`` used when creating the resource

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created this
                Siprec resource.
            call_sid: The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the Siprec resource
                is associated with.
            sid: The SID of the Siprec resource, or the ``name`` used when creating the resource
            status: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Siprec/{Sid}.json"),
            path_params=[
                param[str]("AccountSid", account_sid), param[str]("CallSid", call_sid), param[str]("Sid", sid)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[SiprecEnumUpdateStatusOrStr]("Status", status)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountCallSiprec],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
