"""Small ISO 8601 date helpers."""

from datetime import datetime


def parse_date(value: str) -> datetime:
    """Parse an ISO 8601 date or datetime."""
    return datetime.fromisoformat(value.strip())


def days_between(start: str, end: str) -> int:
    """Return whole days from start to end; the result may be negative."""
    return (parse_date(end) - parse_date(start)).days
