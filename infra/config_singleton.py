import os

class ConfigSingleton:
    _instance = None
    def __new__(cls, *a, **k):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init(*a, **k)
        return cls._instance

    def _init(self, base_price=5.0, price_per_km=2.5, audit_log='audit.log'):
        self.base_price = base_price
        self.price_per_km = price_per_km
        self.audit_log = audit_log
        self.log_enabled = True
        # ensure audit directory exists if path contains dirs
        d = os.path.dirname(self.audit_log)
        if d:
            os.makedirs(d, exist_ok=True)

    def set(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
