salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital_needed = 0
current_spend = spend

for month in range(months):
    deficit = current_spend - salary
    if deficit > 0:
        money_capital_needed += deficit
    current_spend *= (1 + increase)

money_capital_needed = round(money_capital_needed)
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital_needed)
