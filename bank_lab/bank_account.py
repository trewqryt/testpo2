
class BankAccount:
    def __init__(self, owner, account_number):
        self.owner = owner
        self.account_number = account_number
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")

        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")

        if amount > self.balance:
            raise ValueError("Недостаточно средств")

        self.balance -= amount

    def transfer(self, other_account, amount):
        if amount <= 0:
            raise ValueError("Сумма перевода должна быть положительной")

        if amount > self.balance:
            raise ValueError("Недостаточно средств")

        self.balance -= amount
        other_account.balance += amount

    def get_balance(self):
        return self.balance

    def is_empty(self):
        return self.balance == 0


def main():
    print("=== БАНКОВСКИЙ СЧЁТ ===")

    owner = input("Введите имя владельца: ")
    account_number = input("Введите номер счёта: ")

    account = BankAccount(owner, account_number)

    while True:
        print("\n--- МЕНЮ ---")
        print("1. Пополнить счёт")
        print("2. Снять деньги")
        print("3. Показать баланс")
        print("4. Проверить, пустой ли счёт")
        print("5. Выход")

        choice = input("Выберите действие: ")

        try:
            if choice == "1":
                amount = float(input("Введите сумму пополнения: "))
                account.deposit(amount)
                print("Счёт успешно пополнен.")

            elif choice == "2":
                amount = float(input("Введите сумму снятия: "))
                account.withdraw(amount)
                print("Деньги успешно сняты.")

            elif choice == "3":
                print(f"Владелец: {account.owner}")
                print(f"Номер счёта: {account.account_number}")
                print(f"Баланс: {account.get_balance()}")

            elif choice == "4":
                if account.is_empty():
                    print("Счёт пустой.")
                else:
                    print("Счёт не пустой.")

            elif choice == "5":
                print("Программа завершена.")
                break

            else:
                print("Неверный выбор. Попробуйте ещё раз.")

        except ValueError as error:
            print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()
