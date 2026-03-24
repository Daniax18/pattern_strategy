from services.strategies import NotificationStrategy

class NotificationService:
    def __init__(self, strategy: NotificationStrategy):
        self.strategy = strategy

    def send_reminder(self, user):
        message = "Reminder: J-1 avant le rendu du livre."
        return self.strategy.send(user, message)