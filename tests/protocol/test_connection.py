from unittest.mock import patch

from tests import protocol


class ConnectionHandlerTest(protocol.BaseTestCase):
    def test_close_closes_the_client_connection(self):
        with patch.object(self.session, "close") as close_mock:
            self.send_request("close")
            close_mock.assert_called_once_with()
        self.assertEqualResponse("OK")

    def test_empty_request(self):
        self.send_request("")
        self.assertNoResponse()

        self.send_request("  ")
        self.assertNoResponse()

    def test_kill(self):
        self.send_request("kill")
        self.assertEqualResponse(
            'ACK [4@0] {kill} you don\'t have permission for "kill"'
        )

    def test_ping(self):
        self.send_request("ping")
        self.assertEqualResponse("OK")

    def test_malformed_comamnd(self):
        self.send_request("GET / HTTP/1.1")
        self.assertNoResponse()
