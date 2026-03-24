from models.user import User
from services.notification_service import NotificationService
from services.strategies import EmailNotification, SmsNotification, PushNotification


def test_email_notification():
    user = User(email="test@mail.com")
    service = NotificationService(EmailNotification())

    result = service.send_reminder(user)
    assert result is True


def test_sms_notification():
    user = User(phone="12345678")
    service = NotificationService(SmsNotification())

    result = service.send_reminder(user)
    assert result is True


def test_push_notification():
    user = User(phone="12345678")
    service = NotificationService(PushNotification())

    result = service.send_reminder(user)
    assert result is True

#set PYTHONPATH=.
#pytest