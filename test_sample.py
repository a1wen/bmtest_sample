import requests
import json
from hamcrest import assert_that, is_
from brunns.matchers.response import response_with
from mbtest.matchers import had_request
from mbtest.imposters import Imposter, Predicate, Response, Stub
from utils.response import MsisdnResponse
from utils.enums import ResponseCode


def test_request_to_mock_server(mock_server):
    default_response = MsisdnResponse(code=ResponseCode.SUCCESS.value, is_person_in_white_list=True,
                                      is_person_in_stop_list=False, is_person_in_alarm_list=False,
                                      is_person_in_mdw_list=False, is_person_in_terror_list=False)

    data = default_response.json()

    imposter = Imposter(Stub(Predicate(path="/api/v2/by_msisdn/") & Predicate(method=Predicate.Method.POST),
                             Response(body=data)))

    with mock_server(imposter) as server:
        response = requests.post("{}/api/v2/by_msisdn/".format(imposter.url))
        body = response.text

        assert_that("We got the expected response", response, is_(response_with(status_code=200, body=data)))

        assert_that("The mock server recorded the request", server, had_request(path="/api/v2/by_msisdn/", method="GET"))
        print(body)
