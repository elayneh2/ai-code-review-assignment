from __future__ import annotations

from typing import Iterable, Any


def _is_email_invalid(email: str) -> bool:
    """
    Lightweight email validation.

    Valid if:
    - exactly one "@"
    - local and domain parts are non-empty
    - no whitespace
    - domain contains at least one dot and doesn't start/end with dot
    """
    if not isinstance(email, str):
        return False

    email = email.strip()
    if not email or any(char.isspace() for char in email):
        return False

    if email.count("@") != 1:
        return False

    local, domain = email.split("@")
    if not local or not domain:
        return False

    if "." not in domain:
        return False
    if domain.startswith(".") or domain.endswith("."):
        return False

    return True


def count_valid_emails(emails: Iterable[Any]) -> int:
    """
    Count valid emails in the input iterable using _is_email_invalid.

    - Safely ignores non-string entries.
    - Returns 0 for empty input.
    """
    count = 0
    for email in emails:
        if _is_email_invalid(email):
            count += 1
    return count