from .make_report import MakePayoutReport


class ChoiceReport():
    report_types: dict = {
        'payout': MakePayoutReport
    }

    @classmethod
    def choice(cls, report_type: str):
        if report_type not in cls.report_types:
            raise ValueError(f'Неизвестный тип отчета: {report_type}')
        return cls.report_types[report_type]()