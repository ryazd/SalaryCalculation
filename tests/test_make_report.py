import pytest
from src.make_report import MakePayoutReport


def test_payout_report(capsys):
    workers = [{'name': 'Karen White', 'department': 'Sales', 'hours_worked': 165, 'rate': 50}]

    report = MakePayoutReport()
    report.make(workers)
    result = capsys.readouterr().out
    assert 'payout' in result
    assert '$8250' in result


def test_payout_report_many_line(capsys):
    workers = [
        {'name': 'Alice Johnson', 'department': 'Marketing', 'hours_worked': 160, 'rate': 50},
        {'name': 'John', 'department': 'Marketing', 'hours_worked': 162, 'rate': 11}
    ]

    report = MakePayoutReport()
    report.make(workers)
    result = capsys.readouterr().out
    assert '$9782' in result
    assert '322' in result
