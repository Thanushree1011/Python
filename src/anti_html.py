
"""Download a webpage and print its text without HTML tags."""

import logging
import sys
from html.parser import HTMLParser
from urllib.error import URLError
from urllib.request import Request, urlopen

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)


class TextExtractor(HTMLParser):
    """Extract readable text from HTML content."""

    def __init__(self):
        super().__init__()
        self.text_parts = []
        self.skip_content = 0

    def handle_starttag(self, tag, attrs):
        if tag.lower() in {"script", "style"}:
            self.skip_content += 1

    def handle_endtag(self, tag):
        if tag.lower() in {"script", "style"} and self.skip_content:
            self.skip_content -= 1

    def handle_data(self, data):
        if not self.skip_content and data.strip():
            self.text_parts.append(data.strip())


def strip_html(html):
    """Remove HTML tags and return the visible text."""
    parser = TextExtractor()
    parser.feed(html)
    parser.close()
    return " ".join(parser.text_parts)


def fetch_page(url, timeout=10):
    """Download a webpage and return its HTML."""
    if not url.startswith(("http://", "https://")):
        raise ValueError("URL must start with http:// or https://")

    request = Request(
        url,
        headers={"User-Agent": "Python anti_html assignment"},
    )

    with urlopen(request, timeout=timeout) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, errors="replace")


def main():
    """Download the URL supplied on the command line and print its text."""
    if len(sys.argv) != 2:
        print("Usage: python anti_html.py <URL>")
        return 1

    try:
        html = fetch_page(sys.argv[1])
        print(strip_html(html))
        return 0
    except (ValueError, URLError, OSError) as error:
        LOGGER.error("Could not download webpage: %s", error)
        return 1


if __name__ == "__main__":
    sys.exit(main())
