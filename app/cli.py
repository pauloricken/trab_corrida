from infra.config_singleton import ConfigSingleton
from factory.ride_factory import RideFactory
from strategies.pricing import DynamicCityPricing
from decorators.taxes import BaseFare, ServiceFee, Toll, AirportSurcharge
from observers.audit_and_receipt import ReceiptPrinter, Auditor

def demo_run():
    cfg = ConfigSingleton()  # defaults can be overridden
    cfg.set(base_price=5.0, price_per_km=2.5, audit_log='audit.log')

    # create a ride via factory (example data)
    ride = RideFactory.create(origin='Centro', destination='Aeroporto', km=12.0, duration_min=25, city='Itajai', hour=21)

    # strategy: calculate base fare
    strategy = DynamicCityPricing()
    base_amount = strategy.calculate(ride, cfg)

    # decorator: build fare and apply taxes as layers (service + toll + airport)
    fare = BaseFare(base_amount)
    fare = ServiceFee(fare, fee=2.5)
    fare = Toll(fare, toll_amount=8.0)
    # optionally airport; detect by destination name
    if 'aero' in ride.destination.lower():
        fare = AirportSurcharge(fare, surcharge=12.0)

    total = fare.total()

    # observers: receipt + auditor
    receipt = ReceiptPrinter()
    auditor = Auditor()
    # notify observers
    for obs in (receipt, auditor):
        obs.update('ride_completed', {'ride': ride, 'total': total})

    print('Desenvolvido por: Josué Fuchter Maas')

if __name__ == '__main__':
    demo_run()
