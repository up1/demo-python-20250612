class Book:
    def __init__(self, title, stock, price):
        self.title = title
        self.stock = stock
        self.price = price

    def __str__(self):
        return f"Title: {self.title}, Stock: {self.stock}, Price: ${self.price}"

class OrderItem:
    def __init__(self):
        self.book = None
        self.quantity = 0

    def add_book(self, book: Book, quantity: int):
        self.book = book
        self.quantity = quantity

    def __str__(self):
        if self.book is None:
            return "No book added."
        return f"Book: {self.book}, Quantity: {self.quantity}, Total Price: ${self.book.price * self.quantity}"

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item: OrderItem):
        self.items.append(item)

    def total_price(self):
        return sum(item.book.price * item.quantity for item in self.items if item.book is not None)

    def __str__(self):
        return "\n".join(str(item) for item in self.items) + f"\nTotal Price: ${self.total_price()}"

    
# Example usage
if __name__ == "__main__":
    book1 = Book("Potter 1", 10, 8)
    book2 = Book("Potter 2", 10, 8)
    orderItem1 = OrderItem()
    orderItem1.add_book(book1, 2)
    orderItem2 = OrderItem()
    orderItem2.add_book(book2, 1)
    order1 = Order()
    order1.add_item(orderItem1)
    order1.add_item(orderItem2)
    print(order1)

class DiscountProcessor:
    def __init__(self, order: Order):
        self.order = order
    
    def find_best_discount(self):
        # TODO
        # For simplicity, let's assume a flat 10% discount
        return 0.10

class PaymentProcessor:
    def __init__(self, order: Order):
        self.order = order

    def process_payment(self, payment_method: str):
        if payment_method == "credit_card":
            return True
        elif payment_method == "paypal":
            return True
        else:
            raise ValueError("Unsupported payment method")