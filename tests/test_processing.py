import pytest

from src.processing import filter_by_state, sort_by_date

data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


@pytest.mark.parametrize(
    "input_data, expected_result",
    [
        (data, [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}]),
    ],
)
def test_filter_state(input_data: list, expected_result: str) -> None:
    assert filter_by_state(input_data) == expected_result


def sort_by_date_test() -> None:
    assert sort_by_date(data) == data
