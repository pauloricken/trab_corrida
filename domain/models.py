from dataclasses import dataclass

@dataclass
class Ride:
    origin: str
    destination: str
    km: float
    duration_min: float
    city: str
    hour: int  # 0-23
