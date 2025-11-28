from typing import List, Dict
from infra.config_singleton import ConfigSingleton
import datetime

class Observer:
    def update(self, event: str, payload: Dict):
        raise NotImplementedError

class ReceiptPrinter(Observer):
    def update(self, event: str, payload: Dict):
        if event == 'ride_completed':
            ride = payload['ride']
            total = payload['total']
            print('\n--- RECIBO ---')
            print(f'Origem: {ride.origin}')
            print(f'Destino: {ride.destination}')
            print(f'Cidade: {ride.city}')
            print(f'Kilômetros: {ride.km} km')
            print(f'Hora: {ride.hour}h')
            print(f'Valor: R${total:.2f}')
            print('---------------\n')

class Auditor(Observer):
    def __init__(self):
        self.entries = []
        cfg = ConfigSingleton()
        self.log_path = cfg.audit_log if hasattr(cfg, 'audit_log') else 'audit.log'

    def update(self, event: str, payload: Dict):
        if event == 'ride_completed':
            entry = {
                'time': datetime.datetime.now().isoformat(),
                'ride': {
                    'origin': payload['ride'].origin,
                    'destination': payload['ride'].destination,
                    'city': payload['ride'].city,
                    'km': payload['ride'].km,
                    'hour': payload['ride'].hour,
                },
                'total': payload['total']
            }
            self.entries.append(entry)
            # append to file
            try:
                with open(self.log_path, 'a', encoding='utf-8') as f:
                    f.write(str(entry) + '\n')
            except Exception as e:
                print(f"Falha ao gravar auditoria: {e}")
