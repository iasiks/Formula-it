money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

month = 0
budget = money_capital + salary
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while spend < budget:
    budget -= spend
    budget += salary
    spend *= 1 + increase

    month += 1

print("Количество месяцев, которое можно протянуть без долгов:", month)
