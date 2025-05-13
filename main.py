import argparse
from src.data_parser import CSVParser
from src.choice_report import ChoiceReport
from typing import List


def args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='+', help='CSV файлы')
    parser.add_argument('--report', required=True, choices=['payout'], help='Тип отчета')
    return parser.parse_args()


if __name__ == '__main__':
    args = args_parser()
    
    workers: List[dict] = []
    for file in args.files:
        csv_parser: List[dict] = CSVParser(file)
        workers.extend(csv_parser.parse())
    report = ChoiceReport.choice(args.report)
    report.make(workers)
    

