
"""Unit tests for anti_html."""

import unittest
from unittest.mock import MagicMock, patch
from urllib.error import URLError

from anti_html import fetch_page, strip_html


class TestStripHtml(unittest.TestCase):
    def test_removes_html_tags(self):
        self.assertEqual(
            strip_html("<h1>Hello</h1><p>Python</p>"),
            "Hello Python",
        )

    def test_ignores_script_and_style_content(self):
        html = (
            "<style>hidden style</style>"
            "<script>hidden script</script>"
            "<p>Visible text</p>"
        )
        self.assertEqual(strip_html(html), "Visible text")

    def test_handles_empty_html(self):
        self.assertEqual(strip_html(""), "")


class TestFetchPage(unittest.TestCase):
    @patch("anti_html.urlopen")
    def test_fetches_html(self, mock_urlopen):
        response = MagicMock()
        response.read.return_value = b"<p>Hello</p>"
        response.headers.get_content_charset.return_value = "utf-8"
        mock_urlopen.return_value.__enter__.return_value = response

        result = fetch_page("https://example.com")

        self.assertEqual(result, "<p>Hello</p>")
        mock_urlopen.assert_called_once()

    def test_rejects_invalid_url(self):
        with self.assertRaises(ValueError):
            fetch_page("example.com")

    @patch("anti_html.urlopen", side_effect=URLError("Network error"))
    def test_handles_network_error(self, mock_urlopen):
        with self.assertRaises(URLError):
            fetch_page("https://example.com")


if __name__ == "__main__":
    unittest.main()
