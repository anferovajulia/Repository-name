salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
month = 10
money=0
spend_1=6000
for month in range(2, month+1):
    spend = spend*1.03
    spend_1 += spend
for month in range(1,month+1):
    money += salary
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:",round(spend_1-money,2))
