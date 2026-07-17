import html
import re


# Matches any HTML/XML-style tag, e.g. <div>, </div>, <br/>, <li class="x">
_TAG_RE = re.compile(r"<[^>]+>")

# Block-level / line-break tags that should leave a line break behind
# instead of just vanishing (otherwise adjacent text gets smashed together,
# e.g. "<li>A</li><li>B</li>" -> "AB" instead of "A\nB")
_BLOCK_TAG_RE = re.compile(
    r"</?(div|p|li|ul|ol|br|h[1-6]|tr|table)[^>]*>",
    re.IGNORECASE
)


def strip_html(value):
    """
    Removes stray HTML tags and un-escapes HTML entities from a string.
    Gemini is instructed not to output HTML, but LLMs occasionally do it
    anyway (e.g. <b>, <ul><li>, <br>) which Streamlit then renders as
    literal visible text instead of formatted content. This is a
    defense-in-depth cleanup step so the UI never shows raw markup.
    """

    if not isinstance(value, str):
        return value

    cleaned = _BLOCK_TAG_RE.sub("\n", value)

    cleaned = _TAG_RE.sub("", cleaned)

    cleaned = html.unescape(cleaned)

    # Collapse leftover blank lines left behind by removed block tags
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)

    return cleaned.strip()


def sanitize_backlog(data):
    """
    Recursively walks a parsed backlog (dicts/lists/strings) and strips
    HTML from every string value. Numbers, booleans, and None pass through
    unchanged.
    """

    if isinstance(data, dict):
        return {
            key: sanitize_backlog(value)
            for key, value in data.items()
        }

    if isinstance(data, list):
        return [
            sanitize_backlog(item)
            for item in data
        ]

    if isinstance(data, str):
        return strip_html(data)

    return data
