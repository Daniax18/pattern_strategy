# Mauvaise version (avant refactoring)

class NotificationService:
    def send_reminder(self, user, method):
        message = "Reminder: your book is due soon."

        # ❌ CODE SMELL 1: if/else → violation Open/Closed
        if method == "email":
            print(f"Sending EMAIL to {user.email}: {message}")

        # ❌ CODE SMELL 2: duplication logique
        elif method == "sms":
            print(f"Sending SMS to {user.phone}: {message}")

        # ❌ CODE SMELL 3: difficile à étendre (push, whatsapp, etc.)
        else:
            raise ValueError("Unknown method")