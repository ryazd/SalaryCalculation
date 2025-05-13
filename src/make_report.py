from typing import List, Dict


class MakePayoutReport():
    def make(self, workers: List[dict]):
        columns:     Dict[str, int]  = {
            'start': 15,
            'name': 18,
            'hours': 8,
            'rate': 8,
        } 
        
        departments: Dict[str, list] = {}
        title: str = f"{' ':{columns['start']}}{'name':<{columns['name']}}{'hours':<{columns['hours']}}{'rate':<{columns['rate']}}payout"

        print(title)
        for w in workers:
            if w['department'] in departments:
                departments[w['department']].append(w)
            else:
                departments[w['department']] = [w]
        for dep, ws in departments.items():
            total_p: int = 0
            totla_h: int = 0
            print(dep)
            for w in ws:
                payout: int = w['rate'] * w['hours_worked']
                totla_h += w['hours_worked']
                total_p += payout
                print(f"{'-'*(columns['start'] - 1)} {w['name']:{columns['name']}}{w['hours_worked']:<{columns['hours']}}{w['rate']:<{columns['rate']}}${payout}")
            print(f"{' '*(columns['start'] + columns['name'])}{totla_h:<{columns['hours'] + columns['rate']}}${total_p}")