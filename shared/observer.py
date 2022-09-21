from __future__ import annotations
from abc import ABC, abstractmethod
import shared.notify as notify


class Observer(ABC):

    @abstractmethod
    def update(self, notify: notify.Notify, payment: any) -> None:
        pass