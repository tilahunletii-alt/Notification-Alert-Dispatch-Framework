from abc import ABC, abstractmethod


# 1. Interface Segregation & OCP: Abstract Sender Interface
class NotificationSender(ABC):

  @abstractmethod
  def send(self, recipient: str, message: str) -> None:
    pass


# 2. Single Responsibility: Concrete Channels
class EmailSender(NotificationSender):

  def send(self, recipient: str, message: str) -> None:
    print(f"[Email] To: {recipient} | Message: {message}")


class SMSSender(NotificationSender):

  def send(self, recipient: str, message: str) -> None:
    print(f"[SMS] To: {recipient} | Message: {message}")


class SlackSender(NotificationSender):

  def send(self, recipient: str, message: str) -> None:
    print(f"[Slack] To: {recipient} | Message: {message}")


class WhatsAppSender(NotificationSender):

  def send(self, recipient: str, message: str) -> None:
    print(f"[WhatsApp] To: {recipient} | Message: {message}")


# 3. Dependency Inversion & Open/Closed: Notification Service
class NotificationService:

  def __init__(self, sender: NotificationSender):
    # Dependency Injection: depends on the abstraction, not concrete classes
    self._sender = sender

  def send_alert(self, recipient: str, message: str) -> None:
    self._sender.send(recipient, message)