from shared import notify as notify
from shared.observer import Observer


class CachBackApplication(Observer):

    def update(self, notify: notify.Notify, payment: any) -> None:
        print("Notificacao Cachback")
        print(payment)
