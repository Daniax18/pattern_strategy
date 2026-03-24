from models.user import User
from services.notification_service import NotificationService
from services.strategies import EmailNotification, SmsNotification, PushNotification


def main():
    user = User(
        nom="Koto",
        email="koto@mail.com",
        phone=1234
    )

    print("=== EMAIL ===")
    email_service = NotificationService(EmailNotification())
    email_service.send_reminder(user)

    print("\n=== SMS ===")
    sms_service = NotificationService(SmsNotification())
    sms_service.send_reminder(user)

    print("\n=== PUSH ===")
    push_service = NotificationService(PushNotification())
    push_service.send_reminder(user)


if __name__ == "__main__":
    main()