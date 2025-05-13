import pytest
from src.data_parser import CSVParser


def test_invalid_format_file():
    with pytest.raises(TypeError) as ex:
        CSVParser('data/data1.docx')
    assert 'Неправильный формат файла' in str(ex.value)


def test_csv_parser_data1():
    csv_parser = CSVParser('data_test/data_test1.csv')
    workers = csv_parser.parse()
    assert workers == [{
        'name': 'Alice Johnson',
        'department': 'Marketing',
        'hours_worked': 160,
        'rate': 50
    }]


def test_csv_parser_data1_anothet_order():
    csv_parser = CSVParser('data_test/data_test1_another_order.csv')
    workers = csv_parser.parse()
    assert workers == [{
        'name': 'Alice Johnson',
        'department': 'Marketing',
        'hours_worked': 160,
        'rate': 50
    }]


def test_csv_parser_rate():
    csv_parser = CSVParser('data_test/data_test2.csv')
    workers = csv_parser.parse()
    assert workers == [{
        'name': 'Grace Lee',
        'department': 'HR',
        'hours_worked': 160,
        'rate': 45
    }]


def test_csv_parser_salary():
    csv_parser = CSVParser('data_test/data_test3.csv')
    workers = csv_parser.parse()
    assert workers == [{
        'name': 'Karen White',
        'department': 'Sales',
        'hours_worked': 165,
        'rate': 50
    }]


def test_more_line():
    csv_parser = CSVParser('data_test/data_test4.csv')
    workers = csv_parser.parse()
    assert workers == [{
            'name': 'Alice Johnson',
            'department': 'Marketing',
            'hours_worked': 160,
            'rate': 50
        },
        {
            'name': 'John',
            'department': 'HR',
            'hours_worked': 162,
            'rate': 11
        }
    ]