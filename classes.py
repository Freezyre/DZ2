
class BankAccount:
    """Клас для управління банківським рахунком"""
    
    def __init__(self, account_number, balance=0):
        """
        Ініціалізація банківського рахунку
        
        Args:
            account_number (str): Номер рахунку
            balance (float): Початковий баланс (за замовчуванням 0)
        """
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        """
        Додає суму до балансу рахунку
        
        Args:
            amount (float): Сума для додавання
        """
        if amount > 0:
            self.balance += amount
            print(f"Депозит {amount} успішно додано. Новий баланс: {self.balance}")
        else:
            print("Сума повинна бути додатною")
    
    def withdraw(self, amount):
        """
        Знімає суму з рахунку, перевіряючи достатність коштів
        
        Args:
            amount (float): Сума для зняття
        
        Returns:
            bool: True якщо зняття успішне, False якщо недостатньо коштів
        """
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
    """Клас для представлення автомобіля"""
    
    def __init__(self, make, model, year):
        """
        Ініціалізація автомобіля
        
        Args:
            make (str): Марка автомобіля
            model (str): Модель автомобіля
            year (int): Рік випуску
        """
        self.make = make
        self.model = model
        self.year = year
    
    def get_info(self):
        """
        Повертає інформацію про автомобіль
        
        Returns:
            str: Інформація у форматі "[рік] [марка] [модель]"
        """
        return f"{self.year} {self.make} {self.model}"


class Employee:
    """Клас для представлення працівника"""
    
    def __init__(self, name, position, salary):
        """
        Ініціалізація працівника
        
        Args:
            name (str): Ім'я працівника
            position (str): Посада працівника
            salary (float): Заробітна плата
        """
        self.name = name
        self.position = position
        self.salary = salary
    
    def get_salary_info(self):
        """
        Повертає інформацію про заробітну плату
        
        Returns:
            str: Інформація у форматі "Заробітна плата [ім'я]: [заробітна плата]"
        """
        return f"Заробітна плата {self.name}: {self.salary}"


class Rectangle:
    """Клас для представлення прямокутника"""
    
    def __init__(self, width, height):
        """
        Ініціалізація прямокутника
        
        Args:
            width (float): Ширина прямокутника
            height (float): Висота прямокутника
        """
        self.width = width
        self.height = height
    
    def calculate_area(self):
        """
        Обчислює площу прямокутника
        
        Returns:
            float: Площа прямокутника
        """
        return self.width * self.height
    
    def calculate_perimeter(self):
        """
        Обчислює периметр прямокутника
        
        Returns:
            float: Периметр прямокутника
        """
        return 2 * (self.width + self.height)


class Product:
    """Клас для представлення товару"""
    
    def __init__(self, name, price, quantity):
        """
        Ініціалізація товару
        
        Args:
            name (str): Назва товару
            price (float): Ціна товару
            quantity (int): Кількість одиниць товару
        """
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate_total_price(self):
        """
        Обчислює загальну вартість товарів
        
        Returns:
            float: Загальна вартість (ціна * кількість)
        """
        return self.price * self.quantity
    
    def display_info(self):
        """
        Виводить інформацію про товар
        """
        total = self.calculate_total_price()
        print(f"Товар: {self.name}")
        print(f"Ціна: {self.price}")
        print(f"Кількість: {self.quantity}")
        print(f"Загальна вартість: {total}")
