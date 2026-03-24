from abc import ABC, abstractmethod

class NotificationStrategy(ABC):
    @abstractmethod
    def send(self, user, message):
        pass


class EmailNotification(NotificationStrategy):
    def send(self, user, message):
        print(f"Sending EMAIL to {user.email}: {message}")
        return True


class SmsNotification(NotificationStrategy):
    def send(self, user, message):
        print(f"Sending SMS to {user.phone}: {message}")
        return True


class PushNotification(NotificationStrategy):
    def send(self, user, message):
        print(f"Sending PUSH to {user.phone}: {message}")
        return True