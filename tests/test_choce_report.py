from src.choice_report import ChoiceReport
from src.make_report import MakePayoutReport
import pytest


def test_return_payout():
    report = ChoiceReport.choice('payout')
    assert isinstance(report, MakePayoutReport)


def test_invalid_type_report():
    with pytest.raises(ValueError) as ex:
        ChoiceReport.choice('badtype')
    assert 'Неизвестный тип отчета:' in str(ex.value)