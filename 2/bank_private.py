class BankAccount: # Создание класса
    def __init__(self, balance): # Создание конструктора с аргументом баланса
        self.__balance = balance # Баланс
    
    def deposit(self, amount): # Метод для депозита
        if amount > 0: self.__balance += amount
    
    def withdraw(self, amount): # Благотворительность
        if 0 < amount <= self.__balance: self.__balance -= amount
        else: print("Недостаточно средств")

    def get_balance(self): # Получение баланса
        return self.__balance

account = BankAccount(1000) # Создание экземпляра класса
account.deposit(500) # Зачисление депозита на аккаунт
print(account.get_balance()) # Вывод баланса

# Приват нужен чтобы пользователь случайно не изменил баланс.