from decorators.taxes import BaseFare, ServiceFee, Toll, AirportSurcharge

def test_decorator_layers():
    base = BaseFare(10.0)
    with_service = ServiceFee(base, fee=2.5)
    with_toll = Toll(with_service, toll_amount=8.0)
    with_air = AirportSurcharge(with_toll, surcharge=12.0)
    assert with_air.total() == 32.5
