from abc import ABC, abstractmethod

# Interface for payment processing
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Interface for refund processing
class RefundProcessor(ABC):
    @abstractmethod
    def process_refund(self, amount):
        pass

# OnlinePaymentProcessor implements PaymentProcessor and RefundProcessor interfaces
class OnlinePaymentProcessor(PaymentProcessor, RefundProcessor):
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")

    def process_refund(self, amount):
        print(f"Processing refund of ${amount}")

# Some parts of the system only need to process payments
class PaymentHandler:
    def __init__(self, payment_processor):
        self.payment_processor = payment_processor

    def perform_payment(self, amount):
        self.payment_processor.process_payment(amount)

# Some other parts of the system need to process and refund payments
class PaymentRefundHandler:
    def __init__(self, payment_processor):
        self.payment_processor = payment_processor

    def perform_payment(self, amount):
        self.payment_processor.process_payment(amount)

    def perform_refund(self, amount):
        self.payment_processor.process_refund(amount)


if __name__ == "__main__":
    # Creating an instance of OnlinePaymentProcessor
    payment_processor = OnlinePaymentProcessor()

    # Using PaymentHandler to perform payments
    payment_handler = PaymentHandler(payment_processor)
    payment_handler.perform_payment(100)

    # Using PaymentRefundHandler to perform payments and refunds
    payment_refund_handler = PaymentRefundHandler(payment_processor)
    payment_refund_handler.perform_payment(200)
    payment_refund_handler.perform_refund(50)
