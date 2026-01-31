
class BankAccount:
    
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):

        if amount > 0:
            self.balance += amount
            print(f"Депозит {amount} успішно додано. Новий баланс: {self.balance}")
        else:
            print("Сума повинна бути додатною")
    
    def withdraw(self, amount):

        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Зняття {amount} успішне. Новий баланс: {self.balance}")
                return True
            else:
                print(f"Недостатньо коштів. Баланс: {self.balance}, запит: {amount}")
                return False
        else:
            print("Сума повинна бути додатною")
            return False


class Car:

    def __init__(self, make, model, year):

        self.make = make
        self.model = model
        self.year = year
    
    def get_info(self):
        
        return f"{self.year} {self.make} {self.model}"


class Employee:

    def __init__(self, name, position, salary):

        self.name = name
        self.position = position
        self.salary = salary
    
    def get_salary_info(self):

        return f"Заробітна плата {self.name}: {self.salary}"


class Rectangle:

    
    def __init__(self, width, height):
    
        self.width = width
        self.height = height
    
    def calculate_area(self):
 
        return self.width * self.height
    
    def calculate_perimeter(self):

        return 2 * (self.width + self.height)


class Product:

    def __init__(self, name, price, quantity):

        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate_total_price(self):

        return self.price * self.quantity
    
    def display_info(self):

        total = self.calculate_total_price()
        print(f"Товар: {self.name}")
        print(f"Ціна: {self.price}")
        print(f"Кількість: {self.quantity}")
        print(f"Загальна вартість: {total}")
