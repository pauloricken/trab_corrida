from observers.audit_and_receipt import Auditor, ReceiptPrinter
from domain.models import Ride

def test_observer_records():
    r = Ride(origin='A', destination='B', km=5, duration_min=10, city='itajai', hour=12)
    auditor = Auditor()
    auditor.update('ride_completed', {'ride': r, 'total': 20.0})
    assert len(auditor.entries) == 1
