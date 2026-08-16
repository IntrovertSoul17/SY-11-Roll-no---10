from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def make_payment(self, amount):
        pass


class UPI(Payment):

    def make_payment(self, amount):
        print("Payment of ₹", amount, "made through UPI")


class Card(Payment):

    def make_payment(self, amount):
        print("Payment of ₹", amount, "made through Card")


class NetBanking(Payment):

    def make_payment(self, amount):
        print("Payment of ₹", amount, "made through Net Banking")


class PaymentSystem:

    def __init__(self, payment_method):
        self.payment_method = payment_method

    def change_method(self, payment_method):
        self.payment_method = payment_method

    def pay(self, amount):
        self.payment_method.make_payment(amount)


print("1. UPI")
print("2. Card")
print("3. Net Banking")

choice = int(input("Enter your choice: "))
amount = float(input("Enter amount: ₹"))

if choice == 1:
    method = UPI()
elif choice == 2:
    method = Card()
elif choice == 3:
    method = NetBanking()
else:
    print("Invalid choice")
    exit()

system = PaymentSystem(method)
system.pay(amount)

# Changing payment method at runtime
print("\nChanging payment method...")

system.change_method(Card())
system.pay(amount)