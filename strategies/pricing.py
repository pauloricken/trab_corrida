from abc import ABC, abstractmethod

class PricingStrategy(ABC):
    @abstractmethod
    def calculate(self, ride, config):
        """Return base fare (float) before decorators"""
        raise NotImplementedError

class DynamicCityPricing(PricingStrategy):
    """Option A: city multipliers + peak hours multiplier (18-23)."""
    CITY_BASE_PER_KM = {
        'itajai': 2.5,
        'navegantes': 2.2,
        'blumenau': 2.3
    }

    def calculate(self, ride, config):
        base_per_km = self.CITY_BASE_PER_KM.get(ride.city.lower(), config.price_per_km)
        # peak hours 18..23 inclusive
        if 18 <= ride.hour <= 23:
            hour_multiplier = 1.5
        else:
            hour_multiplier = 1.0
        base = config.base_price + (ride.km * base_per_km * hour_multiplier)
        return round(base, 2)
