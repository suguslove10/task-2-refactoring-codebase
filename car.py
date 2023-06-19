from abc import ABC, abstractmethod
from datetime import datetime


class Car(ABC):
    def __init__(self, last_service_date: datetime):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self) -> bool:
        """
        Check if the car needs a service.

        Returns:
            bool: True if the car needs service, False otherwise.
        """
        pass
