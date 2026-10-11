"""Small ISO 8601 date helpers."""

from datetime import datetime


def parse_date(value: str) -> datetime:
    """Parse an ISO 8601 date or datetime."""
    return datetime.fromisoformat(value)


def days_between(start: str, end: str) -> int:
    """Return the whole number of days from start to end."""
    return (parse_date(end) - parse_date(start)).days
