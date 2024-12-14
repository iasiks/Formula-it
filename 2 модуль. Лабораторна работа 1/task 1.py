# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Union

class PaymentProcess:
    def __init__(self, currency: str, available_money: Union[int,float], transaction_limit: Union[int, float]):
        """
        Создание и подготовка к работе объекта платежного процессора.

        :param currency: Валюта платежей
        :param available_money: Имеющаяся на счету сумма денег
        :param transaction_limit: Ежедневный лимит платежей

        Example
        >>> payment = PaymentProcess('USD',500,200) # инициализация экземпляра класса
        """

        if not isinstance(currency, str):
            raise TypeError('Валюта должна быть типа string')
        self.currency = currency

        if not isinstance(available_money, (int, float)):
            raise TypeError("Имеющаяся на счету сумма денег должна быть типа int или float")
        if transaction_limit < 0:
            raise ValueError('Имеющаяся на счету сумма денег должна быть положительным числом или равняться нулю')
        self.available_money = available_money

        if not isinstance(transaction_limit, (int, float)):
            raise TypeError("Ежедневный лимит платежей должен быть типа int или float")
        if transaction_limit < 0:
            raise ValueError('Ежедневный лимит платежей должен быть положительным числом')
        self.transaction_limit = transaction_limit

    def transaction_process(self, amount: Union[int, float], recipient: str):
        """
        Выполняет перевод средств

        :param amount: Сумма перевода
        :param recipient: Получатель платежа.

        :raise ValueError: Если сумма платежа превышает ежедневный лимит

        Example:
        >>> payment = PaymentProcess('USD',500,200)
        >>> payment.transaction_process(150, 'Asel')
        """

        if not isinstance(amount, (int,float)):
            raise TypeError("Сумма перевода должна быть типа int или float")
        if amount > self.transaction_limit:
            raise ValueError('Сумма перевода не должна превышать ежедневный лимит транзакций')
        ...

    def salary(self, earned: Union[float, int]):
        """
        :param earned: Пополнение заработной платой

        :raise ValueError: Если зарплата имеет отрицательное значение

        Example:
        >>> payment = PaymentProcess('USD',500,200)
        >>> payment.salary(1520.5)
        """
        if not isinstance(earned, (int,float)) or earned < 0 :
            raise ValueError('Зарплата должна быть положительным числом и быть типа int или float')
        ...


class UserManager:
    def __init__(self, admin_email: str):
        """
        Создает объект менеджера пользователей.

        :param admin_email: Email администратора.
        :raise ValueError:  Если email пользователя не типа string  или не имеет @

        Example:
        >>> user = UserManager('asel@outlook.com')
        """
        if not isinstance(admin_email, str) or "@" not in admin_email:
            raise ValueError("Адрес электронной почты администратора должен быть действительным.")
        self.admin_email = admin_email


    def add_user(self,user_id: int, email: str):
        """
        Добавляет нового пользователя.

        :param user_id: Уникальный идентификатор пользователя.
        :param email: Электронная почта пользователя.

        :raise ValueError: Если email пользователя не типа string или не имеет @

        Example:
        >>> user = UserManager('asel@outlook.com')
        >>> user.add_user(13082002,'kairat@gmail.com')
        """
        if not isinstance(email, str) or "@" not in email:
            raise ValueError("Адрес электронной почты должен быть действительным.")
        if not isinstance(user_id, int):
            raise TypeError('Id пользователя должен быть типа int')
        ...


    def remove_user(self, user_id: int):
        """
        Удаляет пользователя по идентификатору.

        :param user_id: Уникальный идентификатор пользователя.

        Example:
        >>> user = UserManager('asel@outlook.com')
        >>> user.remove_user(13082002)
        """
        ...


    def list_users(self) -> list:
        """
        Возвращает список всех пользователей.

        :return: Список пользователей (например, [{'user_id': '1', 'email': 'test@example.com'}]).

        Example:
        >>> user = UserManager('asel@outlook.com')
        >>> user.list_users()
        """
        ...

class DeliveryService:
    def __init__(self, max_weight: Union[int, float], region: str):
        """
        Создает объект сервиса доставки.

        :param max_weight: Максимальный вес отправления в килограммах.
        :param region: Регион доставки (например, "EU", "US").

        :raise ValueError: Максимальный вес отправления в килограммах должен быть положительным

        Example:
        >>> delivery = DeliveryService(90,'RU')
        """
        if not isinstance(max_weight, (int, float)) or max_weight <= 0:
            raise ValueError("Максимальный вес отправления в килограммах должен быть положительным.")
        if not isinstance(region, str):
            raise TypeError("Регион отправления должен быть типа string.")

        self.max_weight = max_weight
        self.region = region


    def calculate_cost(self, weight: Union[float,int], distance: Union[int, float]) -> float:
        """
        Рассчитывает стоимость доставки.

        :param weight: Вес отправления в килограммах.
        :param distance: Расстояние в километрах.
        :return: Стоимость доставки.

        :raise ValueError: Вес отправления должен быть меньше или равен max_weight
        :raise ValueError: Расстояние должно быть положительным

        Example:
        >>> delivery = DeliveryService(90,'RU')
        >>> delivery.calculate_cost(50.5, 150)
        """

        if not isinstance(weight, (int,float)) or weight > self.max_weight:
            raise ValueError("Вес отправления должен быть меньше или равен max_weight и иметь тип float.")
        if not isinstance(distance, (int,float)) or distance < 0:
            raise ValueError(' Расстояние должно быть положительным')

        ...


    def track_package(self, tracking_id: str) -> str:
        """
        Отслеживает статус отправления.

        :param tracking_id: Идентификатор отправления.
        :return: Статус отправления (например, "In transit", "Delivered").

        Example:
        >>> delivery = DeliveryService(90,'RU')
        >>> delivery.track_package('id1502')
        """
        ...


if __name__ == "__main__":
    doctest.testmod() # TODO работоспособность экземпляров класса проверить с помощью doctest

    pass
