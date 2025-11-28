from abc import ABC, abstractmethod

class FareComponent(ABC):
    @abstractmethod
    def total(self) -> float:
        raise NotImplementedError

class BaseFare(FareComponent):
    def __init__(self, amount: float):
        self._amount = float(amount)
    def total(self) -> float:
        return float(self._amount)

class FareDecorator(FareComponent):
    def __init__(self, wrapped: FareComponent):
        self._wrapped = wrapped
    def total(self) -> float:
        return self._wrapped.total()

class ServiceFee(FareDecorator):
    def __init__(self, wrapped: FareComponent, fee: float = 2.5):
        super().__init__(wrapped)
        self.fee = float(fee)
    def total(self) -> float:
        return round(super().total() + self.fee, 2)

class Toll(FareDecorator):
    def __init__(self, wrapped: FareComponent, toll_amount: float = 8.0):
        super().__init__(wrapped)
        self.toll_amount = float(toll_amount)
    def total(self) -> float:
        return round(super().total() + self.toll_amount, 2)

class AirportSurcharge(FareDecorator):
    def __init__(self, wrapped: FareComponent, surcharge: float = 12.0):
        super().__init__(wrapped)
        self.surcharge = float(surcharge)
    def total(self) -> float:
        return round(super().total() + self.surcharge, 2)
