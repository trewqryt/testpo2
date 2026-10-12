import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("Albert", "123456")
        self.other_account = BankAccount("John", "654321")

    # Проверка создания счёта
    def test_create_account(self):
        self.assertEqual(self.account.owner, "Albert")
        self.assertEqual(self.account.account_number, "123456")
        self.assertEqual(self.account.get_balance(), 0)

    # Проверка пополнения
    def test_deposit(self):
        self.account.deposit(1000)

        self.assertEqual(self.account.get_balance(), 1000)

    # Проверка нескольких пополнений
    def test_multiple_deposits(self):
        self.account.deposit(1000)
        self.account.deposit(500)

        self.assertEqual(self.account.get_balance(), 1500)

    # Проверка отрицательного пополнения
    def test_deposit_negative(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    # Проверка пополнения нулём
    def test_deposit_zero(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)

    # Проверка снятия
    def test_withdraw(self):
        self.account.deposit(1000)
        self.account.withdraw(300)

        self.assertEqual(self.account.get_balance(), 700)

    # Проверка снятия большей суммы
    def test_withdraw_more_than_balance(self):
        self.account.deposit(500)

        with self.assertRaises(ValueError):
            self.account.withdraw(1000)

        # Баланс не должен измениться
        self.assertEqual(self.account.get_balance(), 500)

    # Проверка отрицательного снятия
    def test_withdraw_negative(self):
        self.account.deposit(500)

        with self.assertRaises(ValueError):
            self.account.withdraw(-100)

    # Проверка перевода
    def test_transfer(self):
        self.account.deposit(1000)

        self.account.transfer(self.other_account, 400)

        self.assertEqual(self.account.get_balance(), 600)
        self.assertEqual(self.other_account.get_balance(), 400)

    # Проверка перевода всей суммы
    def test_transfer_all_money(self):
        self.account.deposit(1000)

        self.account.transfer(self.other_account, 1000)

        self.assertEqual(self.account.get_balance(), 0)
        self.assertEqual(self.other_account.get_balance(), 1000)

    # Проверка перевода большей суммы
    def test_transfer_more_than_balance(self):
        self.account.deposit(500)

        with self.assertRaises(ValueError):
            self.account.transfer(self.other_account, 1000)

        # Оба счёта должны остаться без изменений
        self.assertEqual(self.account.get_balance(), 500)
        self.assertEqual(self.other_account.get_balance(), 0)

    # Проверка отрицательного перевода
    def test_transfer_negative(self):
        self.account.deposit(500)

        with self.assertRaises(ValueError):
            self.account.transfer(self.other_account, -100)

        self.assertEqual(self.account.get_balance(), 500)
        self.assertEqual(self.other_account.get_balance(), 0)

    # Проверка получения баланса
    def test_get_balance(self):
        self.account.deposit(1500)

        self.assertEqual(self.account.get_balance(), 1500)

    # Проверка пустого счёта
    def test_is_empty(self):
        self.assertTrue(self.account.is_empty())

    # Проверка непустого счёта
    def test_is_not_empty(self):
        self.account.deposit(100)

        self.assertFalse(self.account.is_empty())

    # Проверка счёта после снятия всех денег
    def test_is_empty_after_withdraw(self):
        self.account.deposit(1000)
        self.account.withdraw(1000)

        self.assertTrue(self.account.is_empty())


if __name__ == "__main__":
    unittest.main()