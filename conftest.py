import pytest
from mbtest import server
from mbtest.imposters import Imposter, Predicate, Response, Stub


@pytest.fixture(scope="session")
def mock_server(request):
    return server.mock_server(request)


@pytest.fixture(scope="function")
def by_msisdn_imposter():
    return Imposter(Stub(Predicate(path="/api/v2/by_msisdn/", method="POST"),
                         Response(body="sausages")))
