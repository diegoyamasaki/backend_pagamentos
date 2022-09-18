from abc import ABC
from abc import ABC, abstractmethod

from shared.notify import Notify

class Observer(ABC):

    @abstractmethod
    def update(self, notify: Notify) -> None:
        pass