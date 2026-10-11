from datetime import datetime

from tinydate import days_between, parse_date


def test_parse_date():
    assert parse_date("2026-04-22") == datetime(2026, 4, 22)


def test_parse_date_strips_whitespace():
    assert parse_date("2026-04-22\n") == datetime(2026, 4, 22)


def test_days_between():
    assert days_between("2026-04-22", "2026-04-25") == 3
