from abc import ABC, abstractmethod

# Abstraction for the email sending functionality
class EmailSenderInterface(ABC):
    @abstractmethod
    def send_email(self, recipient, subject, message):
        pass

# Concrete implementation of the EmailSenderInterface
class EmailSender(EmailSenderInterface):
    def send_email(self, recipient, subject, message):
        print(f"Sending email to {recipient}: {subject} - {message}")

# NotificationService now depends on the EmailSenderInterface, not the concrete EmailSender
class NotificationService:
    def __init__(self, email_sender):
        self.email_sender = email_sender

    def send_notification(self, recipient, message):
        self.email_sender.send_email(recipient, "Notification", message)


if __name__ == "__main__":
    # Creating an instance of EmailSender
    email_sender = EmailSender()

    # Creating an instance of NotificationService, injecting the email_sender dependency
    notification_service = NotificationService(email_sender)

    # Using the NotificationService to send a notification
    notification_service.send_notification("user@example.com", "Hello, this is a notification!")
