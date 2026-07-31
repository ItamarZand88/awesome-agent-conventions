#!/usr/bin/env python3
"""Tests for link-check retry behavior."""
import unittest
import urllib.error
from unittest.mock import patch

import check_links


class FakeResponse:
    """Minimal context-managed response for urllib tests."""

    status = 200

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return False

    def geturl(self):
        return "https://example.com/page"


def http_error(code):
    """Return an HTTPError suitable for a mocked urlopen call."""
    return urllib.error.HTTPError(
        "https://example.com/page",
        code,
        "test response",
        None,
        None,
    )


class CheckLinkTests(unittest.TestCase):
    """Cover retry decisions for dead-link status codes."""

    item = ("target", "example", "https://example.com/page")

    @patch("check_links.time.sleep")
    @patch("check_links.urllib.request.urlopen")
    def test_retries_transient_404(self, urlopen, sleep):
        urlopen.side_effect = [http_error(404), FakeResponse()]

        result = check_links.check(self.item)

        self.assertEqual(result, (self.item, "ok", 200))
        self.assertEqual(urlopen.call_count, 2)
        sleep.assert_called_once_with(1.5)

    @patch("check_links.time.sleep")
    @patch("check_links.urllib.request.urlopen")
    def test_fails_after_persistent_404(self, urlopen, sleep):
        urlopen.side_effect = [http_error(404) for _ in range(3)]

        result = check_links.check(self.item)

        self.assertEqual(result, (self.item, "fail", 404))
        self.assertEqual(urlopen.call_count, 3)
        self.assertEqual(sleep.call_count, 2)

    @patch("check_links.time.sleep")
    @patch("check_links.urllib.request.urlopen")
    def test_fails_immediately_on_410(self, urlopen, sleep):
        urlopen.side_effect = http_error(410)

        result = check_links.check(self.item)

        self.assertEqual(result, (self.item, "fail", 410))
        urlopen.assert_called_once()
        sleep.assert_not_called()


if __name__ == "__main__":
    unittest.main()
