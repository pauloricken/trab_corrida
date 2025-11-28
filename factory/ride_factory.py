from domain.models import Ride

class RideFactory:
    @staticmethod
    def create(origin: str, destination: str, km: float, duration_min: float, city: str, hour: int) -> Ride:
        # basic validation and normalization
        if km < 0:
            raise ValueError('km must be >= 0')
        if not (0 <= hour <= 23):
            raise ValueError('hour must be in 0..23')
        return Ride(origin=origin, destination=destination, km=float(km), duration_min=float(duration_min), city=city, hour=int(hour))
