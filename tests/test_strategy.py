from infra.config_singleton import ConfigSingleton
from factory.ride_factory import RideFactory
from strategies.pricing import DynamicCityPricing

def test_strategy_diff_hours():
    cfg = ConfigSingleton()
    r1 = RideFactory.create('A','B',10,10,'itajai',17)
    r2 = RideFactory.create('A','B',10,10,'itajai',20)
    s = DynamicCityPricing()
    assert s.calculate(r1, cfg) != s.calculate(r2, cfg)
