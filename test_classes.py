"""
Тестування всіх класів для завдань 1-5
"""

from classes import BankAccount, Car, Employee, Rectangle, Product


def test_bank_account():
    """Тестування класу BankAccount"""
    print("=" * 50)
    print("ЗАВДАННЯ 1: BankAccount")
    print("=" * 50)
    
    account = BankAccount("1234567890", 1000)
    print(f"Номер рахунку: {account.account_number}")
    print(f"Баланс: {account.balance}\n")
    
    account.deposit(500)
    account.deposit(200)
    account.withdraw(300)
    account.withdraw(2000)  # Недостатньо коштів
    
    print()


def test_car():
    """Тестування класу Car"""
    print("=" * 50)
    print("ЗАВДАННЯ 2: Car")
    print("=" * 50)
    
    car1 = Car("Toyota", "Camry", 2022)
    car2 = Car("BMW", "X5", 2023)
    car3 = Car("Honda", "Civic", 2021)
    
    print(f"Автомобіль 1: {car1.get_info()}")
    print(f"Автомобіль 2: {car2.get_info()}")
    print(f"Автомобіль 3: {car3.get_info()}")
    
    print()


def test_employee():
    """Тестування класу Employee"""
    print("=" * 50)
    print("ЗАВДАННЯ 3: Employee")
    print("=" * 50)
    
    emp1 = Employee("Іван", "Програміст", 50000)
    emp2 = Employee("Марія", "Менеджер", 45000)
    emp3 = Employee("Петро", "Дизайнер", 40000)
    
    print(emp1.get_salary_info())
    print(emp2.get_salary_info())
    print(emp3.get_salary_info())
    
    print()


def test_rectangle():
    """Тестування класу Rectangle"""
    print("=" * 50)
    print("ЗАВДАННЯ 4: Rectangle")
    print("=" * 50)
    
    rect1 = Rectangle(5, 10)
    rect2 = Rectangle(7, 3)
    
    print(f"Прямокутник 1 (5x10):")
    print(f"  Площа: {rect1.calculate_area()}")
    print(f"  Периметр: {rect1.calculate_perimeter()}\n")
    
    print(f"Прямокутник 2 (7x3):")
    print(f"  Площа: {rect2.calculate_area()}")
    print(f"  Периметр: {rect2.calculate_perimeter()}")
    
    print()


def test_product():
    """Тестування класу Product"""
    print("=" * 50)
    print("ЗАВДАННЯ 5: Product")
    print("=" * 50)
    
    prod1 = Product("Ноутбук", 15000, 2)
    prod2 = Product("Мишка", 500, 10)
    
    print("Продукт 1:")
    prod1.display_info()
    print(f"\nПродукт 2:")
    prod2.display_info()
    
    print()


if __name__ == "__main__":
    test_bank_account()
    test_car()
    test_employee()
    test_rectangle()
    test_product()
    
    print("=" * 50)
    print("Всі тести успішно завершені!")
    print("=" * 50)
