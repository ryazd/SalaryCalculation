from typing import List, Dict


class CSVParser():
    def __init__(self, filename: str):
        if not filename.endswith('.csv'):
            raise TypeError(f'Неправильный формат файла: {filename}')
        self.filename:  str             = filename
        self.columns:   Dict[str, str]  = {
            'name': 'name',
            'department': 'department',
            'hours_worked': 'hours_worked',
            'hourly_rate': 'rate',
            'rate': 'rate',
            'salary': 'rate'
        }

    def parse(self) -> List[dict]:
        with open(self.filename, encoding='utf-8') as f:
            title:   str            = f.readline().strip().split(',')
            ids:     Dict[str, int] = {self.columns[item] : i for i, item in enumerate(title) if item in self.columns}
            workers: List[dict]     = []
            
            for line in f:
                worker = line.strip().split(',')
                workers.append({
                    'name': worker[ids['name']],
                    'department': worker[ids['department']],
                    'hours_worked': int(worker[ids['hours_worked']]),
                    'rate': int(worker[ids['rate']])
                })
            return workers
