from src.model.entities.inscritos import Inscritos
from abc import ABC, abstractmethod

class SubscribersRepositoryInterface(ABC):
    @abstractmethod
    def insert(self, subscriber_info: dict) -> None: pass
            
    @abstractmethod
    def select_subscriber(self, email: str, event_id: int) -> Inscritos: pass